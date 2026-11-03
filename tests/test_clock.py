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


SLATE = {"games": [{"tip_et": "2026-11-04 19:00", "state": "pre"}, {"tip_et": "2026-11-04 19:30", "state": "pre"},
                   {"tip_et": "2026-11-04 22:00", "state": "pre"}]}


def group(tip, closed=False):
    snaps = [{"kind": "lock", "fetched_at": "2026-11-04T19:30:00Z"}]
    if closed:
        snaps.append({"kind": "close", "fetched_at": tip})
    return {"commence_time": tip, "snapshots": snaps}


class Plan(unittest.TestCase):
    def test_day_jobs_and_close_clusters(self):
        jobs = C.plan(utc(13), DAY, SLATE, None, {})
        keys = [(C.iso(f), k) for f, k, _, _ in jobs]
        self.assertEqual(keys[:3], [("2026-11-04T19:05:00Z", "board_1405"), ("2026-11-04T19:25:00Z", "auto_1425"),
                                    ("2026-11-04T21:15:00Z", "board_1615")])
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
        done = {"board_1405": "x", "auto_1425": "x", "close:2026-11-05T00:00:00Z": "x"}
        jobs = C.plan(utc(23, 30), DAY, SLATE, None, done)
        # board_1615 is late but still useful before the 7 pm tip; the 7 pm close is done
        self.assertEqual([k for _, k, _, _ in jobs][0], "board_1615")
        self.assertNotIn("2026-11-05T00:00:00Z", [C.iso(t) for _, _, _, cov in jobs for t in cov])
        # after the first tip, a board refresh is no longer useful, and tips 3 min away are dropped
        jobs = C.plan(utc(2, 58, d=5), DAY, SLATE, None, {})
        self.assertEqual(jobs, [])

    def test_no_games_no_jobs(self):
        self.assertEqual(C.plan(utc(13), DAY, {"games": []}, None, {}), [])


class Loop(unittest.TestCase):
    def setUp(self):
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
            C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep)
        self.assertEqual(sent, [("2026-11-04T19:05:00Z", "board"), ("2026-11-04T19:25:00Z", "auto"),
                                ("2026-11-04T21:15:00Z", "board"), ("2026-11-04T23:48:00Z", "close"),
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
            C.run(dry_run=True, now_fn=lambda: t[0], sleep=sleep)
        self.assertEqual(sent, ["self"])  # 14:05 ET is more than 5 h 35 min after a 7 am ET start
        self.assertEqual(t[0], utc(12, 0) + C.RUN_BUDGET)

    def test_missing_token_is_logged_not_retried_forever(self):
        with mock.patch.dict(os.environ, {"DK_ODDS_DISPATCH": "", "GITHUB_TOKEN": ""}):
            ok, note = C.dispatch("auto")
        self.assertFalse(ok)
        self.assertIn("DK_ODDS_DISPATCH not set", note)


if __name__ == "__main__":
    unittest.main()
