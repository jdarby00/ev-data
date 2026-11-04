"""Code screener: finds DraftKings and FanDuel prices that beat the other books' fair price,
and logs them to the ledger as shadow bets. No Claude, no API calls. Standard library only.

For every priced player prop (and game total) in prices/<date>.json, at the latest snapshot
taken before now:
  * fair chance of a side = average of each OTHER book's multiplicative no-vig chance at the
    same line (leave-one-out: the book being bet never sets its own fair price);
  * edge = fair x decimal price - 1, for the side at DraftKings or FanDuel.

Contestants (paper, $5 flat, logged once per selection per day, before the start):
  screener       edge >= 3%, fair from 2+ other books
  screener_wide  edge >= 2%, fair from 1+ other book (looser; shows whether the bar matters)

Prices outside -300..+300 are skipped (high margin, thin markets). The screen is written to
board/nba/<date>-screen.md (every edge >= 0, for the Claude runs to read) and .json.

Usage: python3 -I pipeline/screener.py [--date YYYY-MM-DD] [--log] [--now ISO]
Without --log it only writes the screen files.
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grade as G  # noqa: E402
import ledger as L  # noqa: E402
from common import ET, path, today_et  # noqa: E402

BET_BOOKS = ("draftkings", "fanduel")
MARKETS = {v: k for k, v in G.MARKET_KEYS.items() if v.startswith("player_")}
MARKETS["totals"] = "total"
PRICE_FLOOR, PRICE_CAP = -300, 300
START_BUFFER_MIN = 10  # don't log a bet this close to the start
CONTESTANTS = {"screener": (0.03, 2), "screener_wide": (0.02, 1)}  # name: (min edge, min other books)
UTC = dt.timezone.utc


def novig(over, under):
    qo, qu = 1 / G.dec(over), 1 / G.dec(under)
    return qo / (qo + qu), qu / (qo + qu)


def latest_snapshot(group, now):
    snaps = [s for s in group.get("snapshots", []) if s.get("books") and G.ts(s["fetched_at"]) <= now]
    return max(snaps, key=lambda s: s["fetched_at"]) if snaps else None


def screen_group(group, now):
    """Rows for one game-market: every DK/FD side with a leave-one-out fair price."""
    market = MARKETS.get(group.get("market"))
    snap = latest_snapshot(group, now)
    if not market or not snap:
        return []
    quotes = {}  # (who, line) -> book -> {"Over": price, "Under": price}
    for book, v in snap["books"].items():
        for o in v.get("outcomes", []):
            if o.get("side") not in ("Over", "Under") or o.get("price") is None:
                continue
            quotes.setdefault((o.get("player") or "", o.get("line")), {}).setdefault(book, {})[o["side"]] = o["price"]
    rows = []
    for (who, line), books in quotes.items():
        two_sided = {b: p for b, p in books.items() if "Over" in p and "Under" in p}
        for bet_book in BET_BOOKS:
            if bet_book not in books:
                continue
            others = {b: p for b, p in two_sided.items() if b != bet_book}
            if not others:
                continue
            fair_over = sum(novig(p["Over"], p["Under"])[0] for p in others.values()) / len(others)
            for side, price in books[bet_book].items():
                if not PRICE_FLOOR <= price <= PRICE_CAP or -100 < price < 100:
                    continue
                fair = fair_over if side == "Over" else 1 - fair_over
                rows.append({"market": market, "player": who, "line": line, "side": side.lower(),
                             "book": bet_book, "price": price, "fair": round(fair, 4),
                             "edge": round(fair * G.dec(price) - 1, 4), "n_other": len(others),
                             "other_books": sorted(others), "price_ts": snap["fetched_at"],
                             "snapshot": snap.get("kind"), "tip": group.get("commence_time"),
                             "api_away": group.get("api_away"), "api_home": group.get("api_home")})
    return rows


def screen(prices, now):
    rows = []
    for group in (prices or {}).get("groups", {}).values():
        rows += screen_group(group, now)
    rows.sort(key=lambda r: -r["edge"])
    return rows


def best_per_selection(rows, min_edge, min_other):
    """The single best qualifying (book, side) for each prop. When both sides look like edges,
    two books simply disagree; only the larger edge is kept, so the bets never offset."""
    best = {}
    for r in rows:
        if r["edge"] < min_edge or r["n_other"] < min_other:
            continue
        key = (r["api_away"], r["api_home"], r["market"], r["player"])
        if key not in best or r["edge"] > best[key]["edge"]:
            best[key] = r
    return list(best.values())


def to_bet(r, contestant, date, names):
    away, home = names.get(r["api_away"]), names.get(r["api_home"])
    if not away or not home:
        return None
    b = {"date": date, "contestant": contestant, "sport": "nba", "game": f"{away}@{home}",
         "market": r["market"], "side": r["side"], "line": r["line"], "book": r["book"],
         "price": r["price"], "price_source": "collector", "price_ts": r["price_ts"], "stake": 5,
         "p_market": r["fair"], "p_final": r["fair"], "tier": "screener",
         "notes": f"edge {r['edge'] * 100:+.1f}% vs {'+'.join(r['other_books'])} ({r['snapshot']} snapshot)",
         "source": "pipeline/screener.py"}
    if r["player"]:
        b["player"] = r["player"]
    return b


def already_logged(existing, b):
    """One bet per prop per contestant per day, whatever its line, side or price."""
    key = lambda x: (x["date"], x["contestant"], x["game"], x["market"], x.get("player"))  # noqa: E731
    return any(key(x) == key(b) for x in existing)


def log_bets(rows, date, now, names, bets_path=L.BETS):
    existing = L.read_jsonl(bets_path)
    new = []
    for contestant, (min_edge, min_other) in CONTESTANTS.items():
        for r in best_per_selection(rows, min_edge, min_other):
            tip = G.ts(r["tip"]) if r["tip"] else None
            if not tip or tip - now < dt.timedelta(minutes=START_BUFFER_MIN):
                continue
            b = to_bet(r, contestant, date, names)
            if b and not already_logged(existing + new, b):
                new.append(b)
    if new:
        good, _, errors = L.add(new, bets_path)
        if errors:
            raise SystemExit("screener: ledger refused rows: " + "; ".join(errors))
        return good
    return []


def to_markdown(rows, date, now, logged):
    lines = [f"# Price screen, {date}", "",
             f"Built {now.astimezone(ET).strftime('%-I:%M %p ET')} from the latest collector snapshot of each "
             "market. Fair = other books' average no-vig chance at the same line (the bet book is left out). "
             "Edge = fair x decimal price - 1. A screen, not a pick: research still vetoes (status, minutes, role).", "",
             f"Shadow bets logged this run: {len(logged)}.", "",
             "| Edge | Fair | Book price | Selection | Others | Snapshot |", "| --- | --- | --- | --- | --- | --- |"]
    shown = [r for r in rows if r["edge"] >= 0][:60]
    for r in shown:
        sel = f"{r['player'] or (r['api_away'] or '') + ' @ ' + (r['api_home'] or '')} {r['side']} {r['line']} {r['market']}"
        lines.append(f"| {r['edge'] * 100:+.1f}% | {r['fair'] * 100:.1f}% | {r['book']} {r['price']:+d} | {sel} | "
                     f"{'+'.join(r['other_books'])} | {r['snapshot']} {r['price_ts'][11:16]}Z |")
    if not shown:
        lines.append("| – | – | – | No DK or FD price beats the other books' fair price. | – | – |")
    return "\n".join(lines) + "\n"


def run(date, now, log=False, prices_dir=G.PRICES, slates=G.SLATES, out_dir=None, bets_path=L.BETS):
    prices = G.load_prices(prices_dir).get(date)
    rows = screen(prices, now)
    names, _ = G.load_slates(slates)
    logged = log_bets(rows, date, now, names, bets_path) if log else []
    out_dir = out_dir or os.path.dirname(path("board", "nba", "x"))
    with open(os.path.join(out_dir, f"{date}-screen.json"), "w") as fh:
        json.dump({"date": date, "built": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "rows": rows}, fh, indent=0)
    with open(os.path.join(out_dir, f"{date}-screen.md"), "w") as fh:
        fh.write(to_markdown(rows, date, now, logged))
    return rows, logged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today_et().isoformat())
    ap.add_argument("--now", help="ISO time, for replays (default: now)")
    ap.add_argument("--log", action="store_true", help="log qualifying shadow bets to the ledger")
    args = ap.parse_args()
    now = G.ts(args.now) if args.now else dt.datetime.now(UTC)
    if not os.path.exists(os.path.join(G.PRICES, f"{args.date}.json")):
        print(f"no prices for {args.date}; nothing to screen")
        return
    rows, logged = run(args.date, now, args.log)
    print(f"{len(rows)} priced sides screened; {sum(r['edge'] >= 0.03 for r in rows)} at 3%+; "
          f"{len(logged)} shadow bets logged")


if __name__ == "__main__":
    main()
