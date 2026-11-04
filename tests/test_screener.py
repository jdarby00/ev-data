"""Offline tests for the screener. Run: python3 -I tests/test_screener.py -v"""
import datetime as dt
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import grade as G  # noqa: E402
import ledger as L  # noqa: E402
import screener as S  # noqa: E402

DAY = "2026-11-04"
TIP = "2026-11-05T00:40:00Z"  # 7:40 pm ET
SLATE = {"date": DAY, "games": [{"tip_et": f"{DAY} 19:30", "away": "NY", "home": "BOS",
                                 "away_name": "New York Knicks", "home_name": "Boston Celtics"}]}


def two(player, line, over, under):
    return [{"player": player, "side": "Over", "line": line, "price": over},
            {"player": player, "side": "Under", "line": line, "price": under}]


def prices(dk, fd, mgm, fetched="2026-11-04T19:26:00Z"):
    return {"date": DAY, "groups": {"basketball_nba|knicks@celtics|player_points": {
        "api_away": "New York Knicks", "api_home": "Boston Celtics", "market": "player_points",
        "commence_time": TIP, "snapshots": [{"kind": "lock", "fetched_at": fetched, "books": {
            "draftkings": {"outcomes": dk}, "fanduel": {"outcomes": fd}, "betmgm": {"outcomes": mgm}}}]}}}


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        for sub in ("prices", "slate", "out"):
            os.makedirs(os.path.join(self.d, sub))
        with open(os.path.join(self.d, "slate", f"{DAY}.json"), "w") as fh:
            json.dump(SLATE, fh)
        self.bets = os.path.join(self.d, "bets.jsonl")

    def tearDown(self):
        shutil.rmtree(self.d)

    def write_prices(self, p):
        with open(os.path.join(self.d, "prices", f"{DAY}.json"), "w") as fh:
            json.dump(p, fh)

    def run_screen(self, now="2026-11-04T19:30:00Z", log=True):
        return S.run(DAY, G.ts(now), log, os.path.join(self.d, "prices"), os.path.join(self.d, "slate"),
                     os.path.join(self.d, "out"), self.bets)


class Screen(Base):
    def test_leave_one_out_fair_and_edge(self):
        # FD and MGM both price Tatum 27.5 at -110/-110 (fair 50%); DK hangs +115 on the over.
        self.write_prices(prices(two("Jayson Tatum", 27.5, 115, -145), two("Jayson Tatum", 27.5, -110, -110),
                                 two("Jayson Tatum", 27.5, -110, -110)))
        rows, logged = self.run_screen()
        dk_over = next(r for r in rows if r["book"] == "draftkings" and r["side"] == "over")
        self.assertEqual((dk_over["fair"], dk_over["n_other"]), (0.5, 2))
        self.assertAlmostEqual(dk_over["edge"], 0.5 * 2.15 - 1, places=4)
        self.assertEqual({(b["contestant"], b["book"], b["side"], b["price"]) for b in logged},
                         {("screener", "draftkings", "over", 115), ("screener_wide", "draftkings", "over", 115)})
        b = logged[0]
        self.assertEqual((b["game"], b["player"], b["market"], b["line"], b["price_ts"]),
                         ("NY@BOS", "Jayson Tatum", "points", 27.5, "2026-11-04T19:26:00Z"))
        self.assertEqual(L.verify(self.bets), [])

    def test_a_book_never_sets_its_own_fair_price(self):
        # Only DK quotes both sides: nothing else to compare with, so no rows for DK.
        self.write_prices(prices(two("Jayson Tatum", 27.5, 150, -200), [], []))
        rows, logged = self.run_screen()
        self.assertEqual((rows, logged), ([], []))

    def test_one_side_per_prop_when_books_disagree(self):
        # DK over and FD under both look good against the other: keep only the bigger edge.
        self.write_prices(prices(two("Jayson Tatum", 27.5, 120, -150), two("Jayson Tatum", 27.5, -150, 125), []))
        _, logged = self.run_screen()
        wide = [b for b in logged if b["contestant"] == "screener_wide"]
        self.assertEqual(len(wide), 1)
        self.assertEqual([b for b in logged if b["contestant"] == "screener"], [])  # needs 2 other books

    def test_thresholds_bounds_and_start_buffer(self):
        # 2.5% edge (fair 50% at +105): wide only. A +400 price is outside the bounds and ignored.
        self.write_prices(prices(two("Jayson Tatum", 27.5, 105, -135) + two("Jalen Brunson", 4.5, 400, -700),
                                 two("Jayson Tatum", 27.5, -110, -110) + two("Jalen Brunson", 4.5, 300, -500),
                                 two("Jayson Tatum", 27.5, -110, -110) + two("Jalen Brunson", 4.5, 300, -500)))
        _, logged = self.run_screen()
        self.assertEqual({(b["contestant"], b["player"]) for b in logged}, {("screener_wide", "Jayson Tatum")})
        # within 10 minutes of the start nothing is logged
        os.remove(self.bets)
        _, logged = self.run_screen(now="2026-11-05T00:35:00Z")
        self.assertEqual(logged, [])

    def test_logs_once_per_prop_per_day(self):
        self.write_prices(prices(two("Jayson Tatum", 27.5, 115, -145), two("Jayson Tatum", 27.5, -110, -110),
                                 two("Jayson Tatum", 27.5, -110, -110)))
        _, first = self.run_screen()
        later = prices(two("Jayson Tatum", 27.5, 120, -150), two("Jayson Tatum", 27.5, -110, -110),
                       two("Jayson Tatum", 27.5, -110, -110), fetched="2026-11-04T21:00:00Z")
        self.write_prices(later)
        _, second = self.run_screen(now="2026-11-04T21:05:00Z")
        self.assertEqual((len(first), second), (2, []))

    def test_ignores_snapshots_from_the_future_and_writes_the_screen(self):
        self.write_prices(prices(two("Jayson Tatum", 27.5, 115, -145), two("Jayson Tatum", 27.5, -110, -110),
                                 two("Jayson Tatum", 27.5, -110, -110), fetched="2026-11-04T22:00:00Z"))
        rows, logged = self.run_screen(now="2026-11-04T21:00:00Z")
        self.assertEqual((rows, logged), ([], []))
        rows, _ = self.run_screen(now="2026-11-04T22:05:00Z", log=False)
        with open(os.path.join(self.d, "out", f"{DAY}-screen.md")) as fh:
            md = fh.read()
        self.assertIn("draftkings +115 | Jayson Tatum over 27.5 points", md)


if __name__ == "__main__":
    unittest.main()
