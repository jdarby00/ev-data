"""Offline tests for the ledger and grader: synthetic files in a temp folder, no network.
Run: python3 -I tests/test_ledger.py -v"""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import grade as G  # noqa: E402
import ledger as L  # noqa: E402

COLS = ["date", "event", "team", "opp", "home", "espn_id", "player", "starter", "dnp", "dnp_reason", "minutes",
        "points", "rebounds", "offensiveRebounds", "defensiveRebounds", "assists", "steals", "blocks", "turnovers",
        "fouls", "plusMinus", "fieldGoalsMade-fieldGoalsAttempted",
        "threePointFieldGoalsMade-threePointFieldGoalsAttempted", "freeThrowsMade-freeThrowsAttempted"]
DAY = "2026-11-02"
# NY at BOS, tip 7:30 pm ET = 00:30 UTC on 3 Nov. BOS 110, NY 104.
BOX = [
    [DAY, "e1", "BOS", "NY", "1", "1", "Jayson Tatum", "1", "0", "", "36", "30", "8", "", "", "5", "", "", "", "", "",
     "10-20", "4-9", "6-6"],
    [DAY, "e1", "BOS", "NY", "1", "2", "Derrick White", "1", "0", "", "34", "80", "4", "", "", "6", "", "", "", "", "",
     "", "3-8", ""],
    [DAY, "e1", "NY", "BOS", "0", "3", "Jalen Brunson", "1", "0", "", "37", "26", "3", "", "", "9", "", "", "", "", "",
     "", "2-6", ""],
    [DAY, "e1", "NY", "BOS", "0", "4", "Mitchell Robinson", "0", "1", "KNEE", "0", "", "", "", "", "", "", "", "", "",
     "", "", "", ""],
    [DAY, "e1", "NY", "BOS", "0", "5", "Josh Hart", "1", "0", "", "35", "78", "9", "", "", "7", "", "", "", "", "", "",
     "1-3", ""],
]
SLATE = {"date": DAY, "games": [{"event": "e1", "tip_et": f"{DAY} 19:30", "away": "NY", "home": "BOS",
                                 "away_name": "New York Knicks", "home_name": "Boston Celtics"}]}


def outs(player, line, over, under):
    return [{"player": player, "side": "Over", "line": line, "price": over},
            {"player": player, "side": "Under", "line": line, "price": under}]


PRICES = {"date": DAY, "groups": {"basketball_nba|knicks@celtics|player_points": {
    "api_away": "New York Knicks", "api_home": "Boston Celtics", "market": "player_points",
    "commence_time": "2026-11-03T00:30:00Z", "snapshots": [
        {"kind": "lock", "fetched_at": "2026-11-02T21:00:00Z",
         "books": {"draftkings": {"outcomes": outs("Jayson Tatum", 27.5, -110, -110)},
                   "fanduel": {"outcomes": outs("Jayson Tatum", 27.5, -110, -110)}}},
        {"kind": "close", "fetched_at": "2026-11-03T00:15:00Z",
         "books": {"draftkings": {"outcomes": outs("Jayson Tatum", 27.5, -130, 110)},
                   "fanduel": {"outcomes": outs("Jayson Tatum", 27.5, -125, 105)}}},
        {"kind": "close", "fetched_at": "2026-11-03T01:00:00Z",  # after the tip: must be ignored
         "books": {"draftkings": {"outcomes": outs("Jayson Tatum", 27.5, -500, 350)}}}]}}}


def bet(**kw):
    b = {"date": DAY, "contestant": "card", "sport": "nba", "game": "NY@BOS", "market": "points",
         "player": "Jayson Tatum", "side": "over", "line": 27.5, "book": "draftkings", "price": -110,
         "price_source": "collector", "price_ts": "2026-11-02T21:00:00Z", "created_at": "2026-11-02T21:30:00Z"}
    b.update(kw)
    return b


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.d, "slate"))
        os.makedirs(os.path.join(self.d, "prices"))
        with open(os.path.join(self.d, "box.csv"), "w") as fh:
            fh.write(",".join(COLS) + "\n" + "\n".join(",".join(r) for r in BOX) + "\n")
        with open(os.path.join(self.d, "checked.txt"), "w") as fh:
            fh.write(DAY + "\n")
        with open(os.path.join(self.d, "slate", f"{DAY}.json"), "w") as fh:
            json.dump(SLATE, fh)
        with open(os.path.join(self.d, "prices", f"{DAY}.json"), "w") as fh:
            json.dump(PRICES, fh)
        self.bets = os.path.join(self.d, "bets.jsonl")
        self.amend = os.path.join(self.d, "amend.jsonl")

    def tearDown(self):
        shutil.rmtree(self.d)

    def add(self, *rows):
        good, _, errs = L.add(list(rows), self.bets)
        self.assertEqual(errs, [])
        return good

    def run_grader(self):
        p = lambda n: os.path.join(self.d, n)  # noqa: E731
        _, results, problems = G.run(self.bets, self.amend, p("box.csv"), p("checked.txt"), p("slate"),
                                     p("prices"), p("results.jsonl"), p("board.md"), p("seen.json"))
        with open(p("board.md")) as fh:
            self.board = fh.read()
        return {r["id"]: r for r in results}, problems


class Ledger(Base):
    def test_validation_catches_bad_rows(self):
        errs = L.validate(bet(price=-90, side="sideways", book="pinnacle"))
        self.assertTrue(any("price" in e for e in errs))
        self.assertTrue(any("side" in e for e in errs))
        self.assertTrue(any("book" in e for e in errs))
        self.assertIn("player required for a prop", L.validate(bet(player=None)))
        self.assertTrue(any("team abbreviation" in e for e in L.validate(bet(market="spread", side="over"))))

    def test_add_is_all_or_nothing_and_skips_duplicates(self):
        good, _, errs = L.add([bet(), bet(price=50)], self.bets)
        self.assertEqual((good, len(errs)), ([], 1))
        self.assertEqual(L.read_jsonl(self.bets), [])
        self.add(bet())
        good, skipped, _ = L.add([bet()], self.bets)
        self.assertEqual((good, len(skipped)), ([], 1))

    def test_verify_flags_edits_and_removals(self):
        self.add(bet(), bet(side="under", price=-110))
        self.run_grader()  # records first-seen hashes
        rows = L.read_jsonl(self.bets)
        rows[0]["price"] = 150  # someone edits a logged price
        with open(self.bets, "w") as fh:
            fh.write(json.dumps(rows[0]) + "\n")  # ...and drops the second row
        problems = L.verify(self.bets, os.path.join(self.d, "seen.json"))
        self.assertTrue(any("doesn't match its content" in p for p in problems))
        self.assertTrue(any("removed" in p for p in problems))


class Settling(Base):
    def test_props_win_loss_push_void(self):
        a, b, c, d, e = self.add(bet(),  # 30 pts over 27.5 -> win
                                 bet(player="Jalen Brunson", side="over", line=26),  # 26 -> push
                                 bet(player="Jalen Brunson", market="threes", side="over", line=2.5),  # 2 -> loss
                                 bet(player="Mitchell Robinson", market="rebounds", side="under", line=7.5),  # DNP
                                 bet(player="Jayson Tatum", market="pra", side="under", line=40.5))  # 43 -> loss
        res, problems = self.run_grader()
        self.assertEqual(problems, [])
        self.assertEqual([res[x["id"]]["result"] for x in (a, b, c, d, e)], ["win", "push", "loss", "void", "loss"])
        self.assertAlmostEqual(res[a["id"]]["profit"], 5 * 100 / 110)
        self.assertEqual(res[e["id"]]["actual"], 43)
        self.assertEqual(res[d["id"]]["reason"], "did not play")

    def test_name_matching_ignores_accents_and_suffixes(self):
        self.assertEqual(G.norm_name("Luka Dončić"), G.norm_name("luka doncic"))
        self.assertEqual(G.norm_name("Kelly Oubre Jr."), G.norm_name("Kelly Oubre"))

    def test_game_lines(self):
        # BOS 30+80 = 110, NY 26+78 = 104
        rows = self.add(bet(market="total", player=None, side="under", line=214.5),
                        bet(market="spread", player=None, side="NY", line=6.5),
                        bet(market="spread", player=None, side="BOS", line=-6),
                        bet(market="moneyline", player=None, side="NY", line=None),
                        bet(market="team_total", player=None, team="NY", side="over", line=103.5))
        res, _ = self.run_grader()
        self.assertEqual([res[x["id"]]["result"] for x in rows], ["win", "win", "push", "loss", "win"])

    def test_pending_until_box_scores_arrive(self):
        (b,) = self.add(bet(date="2026-11-04", price_ts="2026-11-04T21:00:00Z", created_at="2026-11-04T21:00:00Z"))
        res, _ = self.run_grader()
        self.assertEqual(res[b["id"]]["status"], "pending")

    def test_parlay_with_a_void_leg_reprices(self):
        legs = [dict(game="NY@BOS", market="points", player="Jayson Tatum", side="over", line=27.5, price=-110),
                dict(game="NY@BOS", market="rebounds", player="Mitchell Robinson", side="over", line=6.5, price=120),
                dict(game="NY@BOS", market="total", side="under", line=214.5, price=-110)]
        (p,) = self.add(bet(market="other", player=None, side="over", line=None, price=600, legs=legs, boost=0.5))
        res, _ = self.run_grader()
        r = res[p["id"]]
        self.assertEqual((r["result"], r["legs"]), ("win", ["win", "void", "win"]))
        two_leg = (1 + 100 / 110) ** 2
        self.assertAlmostEqual(r["profit"], 5 * (G.dec(G.to_american(two_leg)) - 1) * 1.5, places=1)

    def test_promos(self):
        rows = self.add(bet(promo="bonus_bet", price=200, stake=10),  # win: profit only, no stake at risk
                        bet(promo="bonus_bet", price=200, stake=10, side="under"),  # loss costs no cash
                        bet(promo="reset", stake=10, side="under", price=-110))  # loss returns a bonus bet
        res, _ = self.run_grader()
        a, b, c = (res[x["id"]] for x in rows)
        self.assertEqual((a["profit"], a["staked"]), (20.0, 0.0))
        self.assertEqual((b["profit"], b["staked"]), (0.0, 0.0))
        self.assertEqual((c["profit"], c["bonus_earned"]), (-10.0, 10.0))

    def test_late_bets_and_withdrawals(self):
        late, early, after = self.add(bet(created_at="2026-11-03T00:45:00Z"),
                                      bet(side="under"), bet(contestant="leans"))
        L.append_jsonl(self.amend, [{"bet_id": early["id"], "action": "withdraw", "at": "2026-11-02T23:00:00Z"},
                                    {"bet_id": after["id"], "action": "withdraw", "at": "2026-11-03T01:00:00Z"}])
        res, _ = self.run_grader()
        self.assertEqual(res[late["id"]]["status"], "late")
        self.assertEqual(res[early["id"]]["status"], "withdrawn")
        self.assertEqual(res[after["id"]]["status"], "graded")  # too late to withdraw
        self.assertIn("ignored", res[after["id"]]["issue"])

    def test_manual_settle(self):
        (b,) = self.add(bet(sport="soccer", game="ROM@MUN", market="moneyline", side="MUN", player=None, line=None,
                            price=150))
        L.append_jsonl(self.amend, [{"bet_id": b["id"], "action": "settle", "result": "win", "at": "x"}])
        res, _ = self.run_grader()
        self.assertEqual((res[b["id"]]["result"], res[b["id"]]["profit"]), ("win", 7.5))


class ClosingLine(Base):
    def test_clv_uses_last_snapshot_before_the_start(self):
        (b,) = self.add(bet())
        res, _ = self.run_grader()
        r = res[b["id"]]
        self.assertEqual(r["close_ts"], "2026-11-03T00:15:00Z")
        q = lambda a: 1 / G.dec(a)  # noqa: E731
        fair = ((q(-130) / (q(-130) + q(110))) + (q(-125) / (q(-125) + q(105)))) / 2
        self.assertAlmostEqual(r["close_fair"], fair, places=4)
        self.assertAlmostEqual(r["clv_ev"], fair * G.dec(-110) - 1, places=4)
        self.assertTrue(r["beat_close"])  # -110 beat DK's -130 close

    def test_no_clv_without_a_later_snapshot(self):
        (b,) = self.add(bet(price_ts="2026-11-03T00:20:00Z"))
        res, _ = self.run_grader()
        self.assertIsNone(res[b["id"]].get("clv_ev"))
        self.assertIn("no snapshot", res[b["id"]]["clv_reason"])


class Scoreboard(Base):
    def test_sections_drawdown_and_separation(self):
        self.add(bet(created_at="2026-11-02T20:00:00Z"),  # win +4.55
                 bet(side="under", created_at="2026-11-02T20:01:00Z"),  # loss -5
                 bet(player="Jalen Brunson", market="threes", line=2.5, created_at="2026-11-02T20:02:00Z"),  # -5
                 bet(contestant="jake", real=True, stake=2, created_at="2026-11-02T20:03:00Z"),
                 bet(contestant="guess", price_source="web", created_at="2026-11-02T20:04:00Z", p_final=0.6))
        self.run_grader()
        self.assertIn("| card | 3 | 1–2–0–0 | $-5.45 |", self.board)
        self.assertIn("$10.00 |", self.board)  # max drawdown 10 after the win
        real = self.board.split("## Jake's real money")[1].split("## Paper")[0]
        self.assertIn("| jake | 1 |", real)
        self.assertIn("## Assumed (web) prices", self.board)
        self.assertNotIn("| guess |", self.board.split("## Assumed")[0])


if __name__ == "__main__":
    unittest.main()
