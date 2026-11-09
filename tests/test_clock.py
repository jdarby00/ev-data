"""Offline tests for the clock: fake time, no dispatches, no git. Run: python3 -I tests/test_clock.py -v"""
import datetime as dt
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import clock as C  # noqa: E402

UTC = dt.timezone.utc
DAY = dt.date(2026, 11, 4)  # EST (UTC-5)


def utc(h, m=0, d=4):
    return dt.datetime(2026, 11, d, h, m, tzinfo=UTC)


NO_GAMES = lambda url: {"events": []}  # noqa: E731 - no network in tests

SLATE = {"games": [{"tip_et": "2026-11-04 19:00", "state": "pre"}, {"tip_et": "2026-11-04 19:30", "state": "pre"},
                   {"tip_et": "2026-11-04 22:00", "state": "pre"}]}


def group(tip, closed=False):
    snaps = [{"kind": "lock", "fetched_at": "2026-11-04T19:30:00Z"}]
    if closed:
        snaps.append({"kind": "close", "fetched_at": tip})
    return {"commence_time": tip, "snapshots": snaps}


class NoOps(unittest.TestCase):
    """The original tests: NBA board refreshes and collector closes only (no ops jobs, no other sports)."""

    def setUp(self):
        self._ops = mock.patch.object(C, "OPS_JOBS", [])
        self._ops.start()
        self.addCleanup(self._ops.stop)


class Plan(NoOps):
    def test_day_jobs_and_close_clusters(self):
        jobs = C.plan(utc(13), DAY, SLATE, None, {})
        keys = [(C.iso(f), k) for f, k, _, _ in jobs]
        self.assertEqual(keys[:3], [("2026-11-04T19:05:00Z", "board_1405"), ("2026-11-04T19:25:00Z", "auto_1425"),
                                    ("2026-11-04T19:45:00Z", "board_1445")])
        closes = [(C.iso(f), [C.iso(t) for t in cov]) for f, _, a, cov in jobs if a == "close"]
        # 7:00 and 7:30 pm tips share one call at 6:48 pm (7:30 is 42 min later: too far), so three calls
        self.assertEqual(closes, [("2026-11-04T23:48:00Z", ["2026-11-05T00:00:00Z"]),
                                  ("2026-11-05T00:18:00Z", ["2026-11-05T00:30:00Z"]),
                                  ("2026-11-05T02:48:00Z", ["2026-11-05T03:00:00Z"])])

    def test_tips_close_together_share_a_call(self):
        prices = {"groups": {"a": group("2026-11-05T00:10:00Z"), "b": group("2026-11-05T00:35:00Z"),
                             "c": group("2026-11-05T00:40:00Z")}}
        closes = [(C.iso(f), len(cov)) for f, _, a, cov in C.plan(utc(13), DAY, SLATE, prices, {}) if a == "close"]
        self.assertEqual(closes, [("2026-11-04T23:58:00Z", 1), ("2026-11-05T00:23:00Z", 2)])

    def test_published_prices_decide_which_tips_need_a_close(self):
        prices = {"groups": {"a": group("2026-11-05T00:10:00Z", closed=True), "b": group("2026-11-05T03:10:00Z")}}
        closes = [C.iso(f) for f, _, a, _ in C.plan(utc(13), DAY, SLATE, prices, {}) if a == "close"]
        self.assertEqual(closes, ["2026-11-05T02:58:00Z"])  # the closed 7:10 pm game is skipped

    def test_done_jobs_and_late_starts(self):
        done = {"board_1405": "x", "auto_1425": "x", "board_1445": "x", "close:2026-11-05T00:00:00Z": "x"}
        jobs = C.plan(utc(23, 30), DAY, SLATE, None, done)
        # board_1615 is late but still useful before the 7 pm tip; the 7 pm close is done
        self.assertEqual([k for _, k, _, _ in jobs][0], "board_1615")
        self.assertNotIn("2026-11-05T00:00:00Z", [C.iso(t) for _, _, _, cov in jobs for t in cov])
        # after the first tip, a board refresh is no longer useful, and tips 3 min away are dropped
        jobs = C.plan(utc(2, 58, d=5), DAY, SLATE, None, {})
        self.assertEqual(jobs, [])

    def test_no_games_no_jobs(self):
        self.assertEqual(C.plan(utc(13), DAY, {"games": []}, None, {}), [])


class Loop(NoOps):
    def setUp(self):
        super().setUp()
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "data", "nba", "slate"))
        with open(os.path.join(self.root, "data", "nba", "slate", "2026-11-04.json"), "w") as fh:
            json.dump(SLATE, fh)
        self.p = mock.patch.object(C, "ROOT", self.root)
        self.p.start()

    def tearDown(self):
        self.p.stop()
        shutil.rmtree(self.root)

    def test_runs_the_whole_day_in_order_without_repeats(self):
        t = [utc(18, 0)]
        sent = []

        def fake_dispatch(action, dry_run=False):
            sent.append((C.iso(t[0]), action))
            return True, f"dry {action}"

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "dispatch", fake_dispatch), mock.patch.object(C, "RUN_BUDGET", dt.timedelta(hours=12)):
            C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=NO_GAMES)
        self.assertEqual(sent, [("2026-11-04T19:05:00Z", "board"), ("2026-11-04T19:25:00Z", "auto"),
                                ("2026-11-04T19:45:00Z", "board"), ("2026-11-04T21:15:00Z", "board"), ("2026-11-04T23:48:00Z", "close"),
                                ("2026-11-05T00:18:00Z", "close"), ("2026-11-05T02:48:00Z", "close")])

    def test_hands_over_before_the_time_limit(self):
        t = [utc(12, 0)]
        sent = []

        def fake_dispatch(action, dry_run=False):
            sent.append(action)
            return True, "ok"

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "dispatch", fake_dispatch):
            C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=NO_GAMES)
        self.assertEqual(sent, ["self"])  # 14:05 ET is more than 5 h 35 min after a 7 am ET start
        self.assertEqual(t[0], utc(12, 0) + C.RUN_BUDGET)

    def test_missing_token_is_logged_not_retried_forever(self):
        with mock.patch.dict(os.environ, {"DK_ODDS_DISPATCH": "", "GITHUB_TOKEN": ""}):
            ok, note = C.dispatch("auto")
        self.assertFalse(ok)
        self.assertIn("DK_ODDS_DISPATCH not set", note)


SUNDAY = dt.date(2026, 11, 8)
NFL_8NOV = ["2026-11-08T14:30:00Z"] + ["2026-11-08T18:00:00Z"] * 7 + ["2026-11-08T21:05:00Z", "2026-11-08T21:25:00Z",
                                                                       "2026-11-09T01:20:00Z"]


def board(dates, state="pre"):
    return {"events": [{"date": d, "status": {"type": {"state": state}}} for d in dates]}


class FreeCloses(NoOps):
    """TEST_PLAN R3 (dk-odds): closes before every NBA/NFL/soccer start, not only the priced NBA tips."""

    def starts(self, dates):
        return sorted({C.parse_utc(d) for d in dates})

    def test_nfl_sunday_gets_a_call_before_every_window(self):
        jobs = C.plan(dt.datetime(2026, 11, 8, 12, 0, tzinfo=UTC), SUNDAY, {"games": []}, None, {}, self.starts(NFL_8NOV))
        free = [(C.iso(f), [C.iso(t) for t in cov]) for f, _, a, cov in jobs if a == "freeclose"]
        # 9:30 am London game, the 1 pm window (7 games, one call), 4:05 and 4:25 pm (20 min apart: two calls,
        # 4:25 would be 32 min after a 3:53 call, outside closing.py's window), Sunday night
        self.assertEqual(free, [("2026-11-08T14:18:00Z", ["2026-11-08T14:30:00Z"]),
                                ("2026-11-08T17:48:00Z", ["2026-11-08T18:00:00Z"]),
                                ("2026-11-08T20:53:00Z", ["2026-11-08T21:05:00Z"]),
                                ("2026-11-08T21:13:00Z", ["2026-11-08T21:25:00Z"]),
                                ("2026-11-09T01:08:00Z", ["2026-11-09T01:20:00Z"])])
        for fire, cov in free:  # every covered start sits inside closing.py's -2..25 minute window at the fire time
            for t in cov:
                m = (C.parse_utc(t) - C.parse_utc(fire)).total_seconds() / 60
                self.assertTrue(C.LAST_CALL_MIN < m <= C.FREE_REACH_MIN)

    def test_collector_tips_are_not_doubled_and_done_starts_are_skipped(self):
        prices = {"groups": {"a": group("2026-11-05T00:10:00Z")}}
        starts = self.starts(["2026-11-05T00:10:00Z", "2026-11-04T15:00:00Z", "2026-11-04T17:30:00Z"])
        done = {"fclose:2026-11-04T15:00:00Z": "x"}
        jobs = C.plan(utc(13), DAY, {"games": []}, prices, done, starts)
        self.assertEqual([(a, [C.iso(t) for t in cov]) for _, _, a, cov in jobs],
                         [("freeclose", ["2026-11-04T17:30:00Z"]), ("close", ["2026-11-05T00:10:00Z"])])
        # a tip the collector already closed (recorded as close:<tip>) gets no free call either
        jobs = C.plan(utc(13), DAY, {"games": []}, None, {"close:2026-11-05T00:10:00Z": "x"}, starts[2:])
        self.assertEqual(jobs, [])

    def test_collector_reach_and_failed_collector_calls(self):
        # collector call at 23:58 for a 00:10 tip also lists a 00:24 tip (inside its 28-min cluster) but closing.py
        # can't see it from there (26 min after its fire, beyond the 20-min reach): the free closes take it
        prices = {"groups": {"a": group("2026-11-05T00:10:00Z"), "b": group("2026-11-05T00:24:00Z")}}
        starts = self.starts(["2026-11-05T00:10:00Z", "2026-11-05T00:24:00Z"])
        jobs = C.plan(utc(13), DAY, {"games": []}, prices, {}, starts)
        self.assertEqual([(a, [C.iso(t) for t in cov]) for _, _, a, cov in jobs],
                         [("close", ["2026-11-05T00:10:00Z", "2026-11-05T00:24:00Z"]),
                          ("freeclose", ["2026-11-05T00:24:00Z"])])
        # a collector call that gave up (closefail) leaves its tip to the free closes
        done = {"close:2026-11-05T00:10:00Z": "x", "closefail:2026-11-05T00:10:00Z": "x"}
        jobs = C.plan(utc(23, 50), DAY, {"games": []}, None, done, starts[:1])
        self.assertEqual([a for _, _, a, _ in jobs], ["freeclose"])

    def test_late_start_and_no_starts(self):
        starts = self.starts(["2026-11-04T17:30:00Z"])
        # 10 min before the start: fire immediately (overdue), still inside the window
        jobs = C.plan(utc(17, 20), DAY, {"games": []}, None, {}, starts)
        self.assertEqual([a for _, _, a, _ in jobs], ["freeclose"])
        self.assertEqual(C.plan(utc(17, 28), DAY, {"games": []}, None, {}, starts), [])  # 2 min out: dropped
        self.assertEqual(C.plan(utc(13), DAY, {"games": []}, None, {}, []), [])

    def test_scoreboard_starts(self):
        seen = []

        def get(url):
            seen.append(url)
            if "nfl" in url:
                return {"events": board(["2026-11-08T18:00Z", "2026-11-08T18:00Z"])["events"]
                        + board(["2026-11-08T14:30Z"], "in")["events"]}
            if "eng.1" in url:
                return None  # a failed fetch
            return board([])

        starts, ok = C.scoreboard_starts(SUNDAY, get)
        self.assertFalse(ok)
        self.assertEqual([C.iso(t) for t in starts], ["2026-11-08T18:00:00Z"])  # live game skipped, duplicates merged
        self.assertEqual(len(seen), 7)
        self.assertTrue(all("dates=20261108" in u for u in seen))

    def test_screen_fallback(self):
        root = tempfile.mkdtemp()
        os.makedirs(os.path.join(root, "board", "nfl"))
        with open(os.path.join(root, "board", "nfl", "2026-11-08-screen.json"), "w") as fh:
            json.dump({"games": [{"start_utc": "2026-11-08T18:00Z", "state": "pre"},
                                 {"start_utc": "2026-11-08T14:30Z", "state": "post"}, {"state": "pre"}]}, fh)
        self.assertEqual([C.iso(t) for t in C.screen_starts(root, SUNDAY)], ["2026-11-08T18:00:00Z"])
        shutil.rmtree(root)

    def test_run_dispatches_free_closes_and_keeps_the_cache_on_a_failed_fetch(self):
        root = tempfile.mkdtemp()
        sent, calls, t = [], [0], [dt.datetime(2026, 11, 8, 17, 0, tzinfo=UTC)]

        def get(url):
            calls[0] += 1
            if calls[0] > 7:  # every later refresh fails for NFL: the cached starts must be kept
                return None if "nfl" in url else board([])
            return board(NFL_8NOV) if "nfl" in url else board([])

        def fake_dispatch(action, dry_run=False):
            sent.append((C.iso(t[0]), action))
            return True, f"dry {action}"

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "ROOT", root), mock.patch.object(C, "dispatch", fake_dispatch), \
                mock.patch.object(C, "RUN_BUDGET", dt.timedelta(hours=12)):
            state = C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=get)
        self.assertEqual(sent, [("2026-11-08T17:48:00Z", "freeclose"), ("2026-11-08T20:53:00Z", "freeclose"),
                                ("2026-11-08T21:13:00Z", "freeclose"), ("2026-11-09T01:08:00Z", "freeclose")])
        self.assertIn("fclose:2026-11-08T21:25:00Z", state["done"])
        shutil.rmtree(root)


MONDAY = dt.date(2026, 11, 9)


def et(day, h, m=0):
    return dt.datetime.combine(day, dt.time(h, m), C.ET).astimezone(UTC)


class OpsJobs(unittest.TestCase):
    """Jake, 9 Nov: none of dk-odds' scheduled runs fired from 3:43 am to 4:25 pm ET; the clock fires them."""

    def ops(self, now, day, slate, done=None):
        return [(C.iso(f), k, a) for f, k, a, _ in C.plan(now, day, slate, None, done or {}) if not k.startswith("close")]

    def test_monday_with_nba_and_nfl_night(self):
        got = self.ops(et(MONDAY, 4, 0), MONDAY, {"games": [{"tip_et": "2026-11-09 19:30", "state": "pre"}]})
        keys = [k for _, k, _ in got]
        self.assertEqual(keys, ["box_0520", "lab_0610", "escreen_1040", "board_1405", "auto_1425", "lab_1435",
                                "board_1445", "board_1615", "mscreen_1615", "escreen_1620", "news_1840"])
        self.assertEqual(got[1], ("2026-11-09T11:10:00Z", "lab_0610", "lab"))  # 6:10 am EST
        for _, _, a in got:
            self.assertIn(a, C.ACTIONS)

    def test_weekday_filters_and_no_nba_night(self):
        sat, sun, tue = dt.date(2026, 11, 7), dt.date(2026, 11, 8), dt.date(2026, 11, 10)
        empty = {"games": []}
        self.assertIn("mscreen_0645", [k for _, k, _ in self.ops(et(sat, 4), sat, empty)])
        sun_keys = [k for _, k, _ in self.ops(et(sun, 4), sun, empty)]
        self.assertTrue({"mscreen_0645", "mscreen_1030", "mscreen_1615"} <= set(sun_keys))
        tue_keys = [k for _, k, _ in self.ops(et(tue, 4), tue, empty)]
        self.assertIn("mscreen_1040", tue_keys)
        self.assertNotIn("mscreen_0645", tue_keys)
        self.assertNotIn("news_1840", tue_keys)  # no NBA tonight: no late-news re-screen (it may spend credits)
        self.assertNotIn("board_1405", tue_keys)  # board refreshes still need an NBA slate

    def test_late_windows_and_done(self):
        slate = {"games": [{"tip_et": "2026-11-09 19:30", "state": "pre"}]}
        # clock restarted at 9:00 am: lab 6:10 still worth running (4 h window), box scores (2 h) no longer
        keys = [k for _, k, _ in self.ops(et(MONDAY, 9, 0), MONDAY, slate)]
        self.assertIn("lab_0610", keys)
        self.assertNotIn("box_0520", keys)
        # 4:42 pm: the 4:20 screen is past its 20-min window; the 4:15 NFL screen too (25 min)
        keys = [k for _, k, _ in self.ops(et(MONDAY, 16, 42), MONDAY, slate)]
        self.assertNotIn("escreen_1620", keys)
        self.assertNotIn("mscreen_1615", keys)
        self.assertIn("news_1840", keys)
        keys = [k for _, k, _ in self.ops(et(MONDAY, 4), MONDAY, slate, {"lab_0610": "x"})]
        self.assertNotIn("lab_0610", keys)


class Chain(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.p = mock.patch.object(C, "ROOT", self.root)
        self.p.start()

    def tearDown(self):
        self.p.stop()
        shutil.rmtree(self.root)

    def test_rolls_into_the_next_day_and_hands_over(self):
        t = [et(MONDAY, 20, 0)]
        sent = []

        def fake_dispatch(action, dry_run=False):
            sent.append((C.iso(t[0]), action))
            return True, "ok"

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "dispatch", fake_dispatch):
            C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=NO_GAMES, chain=True)
        # nothing left Monday night: the run sleeps past midnight instead of stopping, and its 5 h 35 min budget ends
        # at 1:35 am ET Tuesday, before Tuesday's first job, so it hands over to a fresh run and stops
        self.assertEqual(sent, [("2026-11-10T06:35:00Z", "self")])
        self.assertTrue(os.path.exists(os.path.join(self.root, "clock")))

    def test_chain_fires_tomorrows_jobs_and_writes_tomorrows_state(self):
        t = [et(MONDAY, 23, 0)]
        sent = []

        def fake_dispatch(action, dry_run=False):
            sent.append((C.iso(t[0]), action))
            return True, "ok"

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "dispatch", fake_dispatch), mock.patch.object(C, "RUN_BUDGET", dt.timedelta(hours=12)):
            state = C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=NO_GAMES, chain=True)
        self.assertEqual(sent[:2], [("2026-11-10T10:20:00Z", "boxscores"), ("2026-11-10T11:10:00Z", "lab")])
        self.assertEqual(sent[-1][1], "self")
        self.assertEqual(state["date"], "2026-11-10")
        self.assertIn("lab_0610", state["done"])

    def test_without_chain_it_stops_at_midnight(self):
        t = [et(MONDAY, 23, 0)]

        def sleep(s):
            t[0] += dt.timedelta(seconds=s)

        with mock.patch.object(C, "dispatch", lambda a, dry_run=False: (True, "ok")):
            state = C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep, get=NO_GAMES)
        self.assertEqual(state["date"], "2026-11-09")  # returned on "nothing left today" at 11 pm

    def test_hand_over_is_retried(self):
        calls = []

        def flaky(action, dry_run=False):
            calls.append(action)
            return (len(calls) >= 2), "HTTP 500" if len(calls) < 2 else "ok"

        naps = []
        state = {"log": [], "done": {}}
        with mock.patch.object(C, "dispatch", flaky):
            ok = C.hand_over(state, "unused", MONDAY, et(MONDAY, 12), True, naps.append)
        self.assertTrue(ok)
        self.assertEqual((calls, naps), (["self", "self"], [30]))
        with mock.patch.object(C, "dispatch", lambda a, dry_run=False: (False, "HTTP 500")):
            self.assertFalse(C.hand_over(state, "unused", MONDAY, et(MONDAY, 12), True, naps.append))


if __name__ == "__main__":
    unittest.main()
