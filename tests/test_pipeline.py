"""Offline tests: synthetic ESPN payloads, no network. Run: python3 -I tests/test_pipeline.py -v"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import common  # noqa: E402
import nba_board  # noqa: E402
import nba_boxscores  # noqa: E402
import nba_slate  # noqa: E402

KEYS = ["minutes", "points", "fieldGoalsMade-fieldGoalsAttempted", "threePointFieldGoalsMade-threePointFieldGoalsAttempted",
        "freeThrowsMade-freeThrowsAttempted", "rebounds", "offensiveRebounds", "defensiveRebounds", "assists",
        "turnovers", "steals", "blocks", "fouls", "plusMinus"]


def ath(pid, name, mins, pts, reb, ast, tpm, starter=False, dnp=False, reason=""):
    if dnp:
        return {"athlete": {"id": pid, "displayName": name}, "starter": False, "didNotPlay": True,
                "reason": reason, "stats": []}
    return {"athlete": {"id": pid, "displayName": name}, "starter": starter,
            "stats": [str(mins), str(pts), "5-10", f"{tpm}-{tpm + 2}", "1-1", str(reb), "1", str(reb - 1),
                      str(ast), "2", "1", "0", "3", "+4"]}


def summary(home_players, away_players):
    return {"header": {"competitions": [{"competitors": [
                {"homeAway": "home", "team": {"abbreviation": "BOS"}},
                {"homeAway": "away", "team": {"abbreviation": "NY"}}]}]},
            "boxscore": {"players": [
                {"team": {"abbreviation": "NY"}, "statistics": [{"keys": KEYS, "athletes": away_players}]},
                {"team": {"abbreviation": "BOS"}, "statistics": [{"keys": KEYS, "athletes": home_players}]}]}}


class Common(unittest.TestCase):
    def test_num(self):
        self.assertEqual(common.num("+5"), 5)
        self.assertEqual(common.num("-3"), -3)
        self.assertEqual(common.num("7-15"), 7)
        self.assertEqual(common.num(""), 0.0)
        self.assertEqual(common.num("--", None), None)

    def test_to_et(self):
        self.assertEqual(common.to_et("2026-11-03T00:30Z").strftime("%Y-%m-%d %H:%M"), "2026-11-02 19:30")


class Boxscores(unittest.TestCase):
    def test_parse_summary_played_and_dnp(self):
        s = summary([ath("1", "Home Star", 36, 30, 8, 5, 3, starter=True),
                     ath("2", "Home Big", 0, 0, 0, 0, 0, dnp=True, reason="RIGHT KNEE SORENESS")],
                    [ath("3", "Away Guard", 34, 22, 4, 9, 2, starter=True)])
        rows = nba_boxscores.parse_summary(s, "2026-11-01", "e1")
        self.assertEqual(len(rows), 3)
        star = next(r for r in rows if r["player"] == "Home Star")
        self.assertEqual((star["team"], star["opp"], star["home"], star["starter"]), ("BOS", "NY", 1, 1))
        self.assertEqual(star["points"], "30")
        big = next(r for r in rows if r["player"] == "Home Big")
        self.assertEqual((big["dnp"], big["dnp_reason"], big["minutes"]), (1, "RIGHT KNEE SORENESS", "0"))
        guard = next(r for r in rows if r["player"] == "Away Guard")
        self.assertEqual((guard["team"], guard["opp"], guard["home"]), ("NY", "BOS", 0))


class Slate(unittest.TestCase):
    def test_parse_scoreboard(self):
        sb = {"events": [{"id": "9", "date": "2026-11-03T00:30Z", "season": {"type": 2},
                          "status": {"type": {"state": "pre"}},
                          "competitions": [{"competitors": [
                              {"homeAway": "home", "team": {"abbreviation": "BOS", "displayName": "Boston Celtics"}},
                              {"homeAway": "away", "team": {"abbreviation": "NY", "displayName": "New York Knicks"}}],
                              "odds": [{"details": "BOS -4.5", "spread": -4.5, "overUnder": 224.5,
                                        "provider": {"name": "DraftKings"}}]}]}]}
        g = nba_slate.parse_scoreboard(sb)[0]
        self.assertEqual((g["away"], g["home"], g["tip_et"], g["total"]), ("NY", "BOS", "2026-11-02 19:30", 224.5))

    def test_injuries_and_changes(self):
        payload = {"injuries": [{"displayName": "Boston Celtics", "injuries": [
            {"athlete": {"displayName": "Home Big"}, "status": "Out", "shortComment": "Knee.", "date": "x"}]}]}
        inj = nba_slate.parse_injuries(payload)
        self.assertEqual(inj["Boston Celtics"][0]["status"], "Out")
        old = {"Boston Celtics": [{"player": "Home Big", "status": "Questionable"},
                                  {"player": "Bench Guy", "status": "Day-To-Day"}]}
        ch = nba_slate.status_changes(old, inj, "2026-11-02 17:00")
        self.assertIn({"at_et": "2026-11-02 17:00", "team": "Boston Celtics", "player": "Home Big",
                       "from": "Questionable", "to": "Out"}, ch)
        self.assertTrue(any(c["player"] == "Bench Guy" and c["to"] == "removed from report" for c in ch))


class Board(unittest.TestCase):
    def setUp(self):
        rows = []
        # Six BOS games. Home Big plays the first three, misses the last three; Home Star scores more without him.
        for i in range(6):
            date, ev = f"2026-10-2{i}", f"e{i}"
            big_out = i >= 3
            s = summary([ath("1", "Home Star", 36, 34 if big_out else 24, 6, 5, 3, starter=True),
                         ath("2", "Home Big", 30, 12, 10, 1, 0, starter=True, dnp=big_out, reason="KNEE")],
                        [ath("3", "Away Guard", 34, 22, 4, 9, 2, starter=True)])
            rows += nba_boxscores.parse_summary(s, date, ev)
        self.box = [{k: str(v) for k, v in r.items()} for r in rows]
        self.slate = {"updated_et": "2026-11-02 11:00", "status_changes": [],
                      "games": [{"event": "9", "tip_et": "2026-11-02 19:30", "away": "NY", "home": "BOS",
                                 "spread_text": "BOS -4.5", "total": 224.5, "odds_source": "DraftKings"}],
                      "injuries": {"Boston Celtics": [{"player": "Home Big", "status": "Out", "detail": "Knee."},
                                                      {"player": "Long Term", "status": "Out", "detail": "Foot."}]}}
        self.slate["games"][0].update(home_name="Boston Celtics", away_name="New York Knicks")

    def test_build_and_markdown(self):
        b = nba_board.build("2026-11-02", self.box, [], self.slate)
        bos = b["teams"]["BOS"]
        self.assertEqual(bos["out"], ["Home Big"])
        self.assertEqual(bos["freed_minutes"], 30.0)
        self.assertEqual(bos["out_no_games_this_season"], ["Long Term"])
        star = next(p for p in bos["players"] if p["player"] == "Home Star")
        self.assertEqual((star["gp"], star["pts"], star["pts_l5"]), (6, 29.0, 30.0))
        big = next(p for p in bos["players"] if p["player"] == "Home Big")
        self.assertEqual(big["missed_l5"], 3)
        ww = bos["with_without"][0]
        self.assertEqual((ww["absent"], ww["teammate"], ww["delta"]["pts"]), ("Home Big", "Home Star", 10.0))
        md = nba_board.to_markdown(b)
        self.assertIn("## NY @ BOS, 19:30 ET", md)
        self.assertIn("Without Home Big: Home Star", md)
        self.assertIn("Out all season so far (already in the lines): Long Term", md)
        self.assertNotIn("2026-11-02 |", md)  # today's date never counted as a played game

    def test_projection_present_and_sane(self):
        b = nba_board.build("2026-11-02", self.box, [], self.slate)
        star = next(p for p in b["teams"]["BOS"]["players"] if p["player"] == "Home Star")
        q = star["proj"]["stats"]["pts"]
        self.assertTrue(q["p10"] < q["p50"] < q["p90"])
        self.assertTrue(20 <= q["p50"] <= 36)
        ladder = q["p_over"]
        keys = sorted(ladder, key=float)
        self.assertGreater(ladder[keys[0]], ladder[keys[-1]])  # over chance falls as the line rises
        big = next(p for p in b["teams"]["BOS"]["players"] if p["player"] == "Home Big")
        self.assertIsNone(big["proj"])  # out tonight: no projection

    def test_model_push_handling(self):
        import nba_model
        pr = nba_model.project([{"min": 30, "pts": 20, "reb": 5, "ast": 5, "tpm": 2}] * 5, None)
        self.assertAlmostEqual(pr.p_over("reb", 5.5) + (1 - pr.p_over("reb", 5.5)), 1.0)
        self.assertTrue(0 < pr.p_over("reb", 5) < 1)

    def test_future_rows_ignored(self):
        future = dict(self.box[0], date="2026-11-03")
        b = nba_board.build("2026-11-02", self.box + [future], [], self.slate)
        star = next(p for p in b["teams"]["BOS"]["players"] if p["player"] == "Home Star")
        self.assertEqual(star["gp"], 6)


class TestUnfinishedDate(unittest.TestCase):
    """11 Nov: a run at 00:17 ET marked 10 Nov checked while two late games were still being played."""

    def test_unfinished_games_are_counted_and_skipped(self):
        import datetime as dt
        from unittest import mock
        sb = {"events": [{"id": "1", "date": "2026-11-11T02:00Z", "status": {"type": {"state": "post"}}, "season": {"type": 2}},
                         {"id": "2", "date": "2026-11-11T04:00Z", "status": {"type": {"state": "in"}}, "season": {"type": 2}}]}
        with mock.patch.object(nba_boxscores, "get_json", lambda u: sb if "scoreboard" in u else {}), \
                mock.patch.object(nba_boxscores, "parse_summary", lambda *a: [{"date": "2026-11-10"}]), \
                mock.patch.object(nba_boxscores.time, "sleep", lambda s: None):
            rows = nba_boxscores.fetch_date(dt.date(2026, 11, 10))
        self.assertEqual(len(rows), 1)
        self.assertEqual(nba_boxscores.fetch_date.unfinished, 1)


if __name__ == "__main__":
    unittest.main()
