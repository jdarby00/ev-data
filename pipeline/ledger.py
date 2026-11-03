"""Append-only bet ledger. Standard library only.

Files (all in ledger/):
  bets.jsonl        one immutable row per bet (never edited or removed)
  amendments.jsonl  withdrawals (before the start) and manual settlements (sports or
                    bets the grader can't settle, e.g. soccer, NFL, Jake's reported bets)

Usage:
  python3 -I pipeline/ledger.py add FILE.json        # a bet object or a list of them (.jsonl also works)
  python3 -I pipeline/ledger.py withdraw BET_ID --reason "Aldama ruled out 1:18 pm"
  python3 -I pipeline/ledger.py settle BET_ID --result win|loss|push|void [--actual 12] [--reason ...]
  python3 -I pipeline/ledger.py verify               # schema + immutability check
  python3 -I pipeline/ledger.py show [--date YYYY-MM-DD]

A bet row (fields marked * are required):
  date*         ET slate date, YYYY-MM-DD
  contestant*   e.g. card, leans, boost, screener, always_over, jake
  sport*        nba | nfl | nhl | soccer | mlb | other
  game*         "AWAY@HOME" using ESPN abbreviations for NBA (e.g. "ATL@IND")
  market*       points rebounds assists threes pra pr pa ra (player props) or
                spread total moneyline team_total (game lines) or other
  side*         over | under for props, totals and team totals; a team abbreviation
                for spread and moneyline
  line          the number (required except for moneyline)
  player        required for player props
  team          team abbreviation (required for team_total; helps prop matching)
  book*         draftkings | fanduel | betmgm | other
  price*        American odds, e.g. -115 or 140 (the price after any boost is NOT
                entered here; enter the plain price and the boost separately)
  price_source* collector | slip (Jake's betslip) | web (assumed, scored separately)
  price_ts*     ISO time the price was seen (UTC, e.g. 2026-11-02T21:46:43Z)
  stake         dollars, default 5 (paper); Jake's real stake for real bets
  real          true only for Jake's real-money bets; default false
  boost         profit boost as a fraction (0.25 = 25%); default 0
  promo         none | boost | bonus_bet | reset; default none (boost implies boost)
  legs          for a parlay: a list of leg objects (game, market, side, line, player,
                team, price); the bet's own price is then the combined plain price
  p_market, p_ours, p_final   win chances in 0-1 (optional; used for calibration)
  tier, notes, conditions, source   free text
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import path  # noqa: E402

BETS = path("ledger", "bets.jsonl")
AMEND = path("ledger", "amendments.jsonl")

SPORTS = {"nba", "nfl", "nhl", "soccer", "mlb", "other"}
PROP_MARKETS = {"points", "rebounds", "assists", "threes", "pra", "pr", "pa", "ra"}
GAME_MARKETS = {"spread", "total", "moneyline", "team_total"}
BOOKS = {"draftkings", "fanduel", "betmgm", "other"}
SOURCES = {"collector", "slip", "web"}
PROMOS = {"none", "boost", "bonus_bet", "reset"}
RESULTS = {"win", "loss", "push", "void"}
ID_FIELDS = ["date", "contestant", "sport", "game", "market", "player", "team", "side", "line",
             "book", "price", "price_ts", "stake", "real", "boost", "promo", "legs"]


def now_utc():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_jsonl(p):
    if not os.path.exists(p):
        return []
    out = []
    with open(p) as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise ValueError(f"{os.path.basename(p)} line {n}: {e}")
    return out


def append_jsonl(p, rows):
    with open(p, "a") as fh:
        for r in rows:
            fh.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")


def american_ok(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and (x >= 100 or x <= -100)


def parse_ts(s):
    return dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))


def _check_selection(b, where, errs, is_leg=False):
    m = b.get("market")
    if m not in PROP_MARKETS | GAME_MARKETS | {"other"}:
        errs.append(f"{where}market '{m}' unknown")
    side = b.get("side")
    if m in PROP_MARKETS | {"total", "team_total"} and side not in ("over", "under"):
        errs.append(f"{where}side must be over or under for {m}")
    if m in ("spread", "moneyline") and not (isinstance(side, str) and side.isupper()):
        errs.append(f"{where}side must be a team abbreviation for {m}")
    if m in PROP_MARKETS and not b.get("player"):
        errs.append(f"{where}player required for a prop")
    if m == "team_total" and not b.get("team"):
        errs.append(f"{where}team required for team_total")
    if m not in ("moneyline", "other") and not isinstance(b.get("line"), (int, float)):
        errs.append(f"{where}line required")
    if not isinstance(b.get("game"), str) or "@" not in b.get("game", ""):
        errs.append(f"{where}game must look like AWAY@HOME")
    if is_leg and "price" in b and not american_ok(b["price"]):
        errs.append(f"{where}leg price must be American odds")


def validate(b):
    """Return a list of problems with a bet row (empty means valid)."""
    errs = []
    try:
        dt.date.fromisoformat(b.get("date", ""))
    except (TypeError, ValueError):
        errs.append("date must be YYYY-MM-DD")
    for f in ("contestant", "sport", "book", "price", "price_source", "price_ts"):
        if b.get(f) in (None, ""):
            errs.append(f"{f} required")
    if b.get("sport") not in SPORTS:
        errs.append(f"sport '{b.get('sport')}' unknown")
    if b.get("book") not in BOOKS:
        errs.append(f"book '{b.get('book')}' unknown")
    if b.get("price_source") not in SOURCES:
        errs.append(f"price_source '{b.get('price_source')}' unknown")
    if not american_ok(b.get("price")):
        errs.append("price must be American odds (<= -100 or >= 100)")
    try:
        parse_ts(b.get("price_ts"))
    except (TypeError, ValueError):
        errs.append("price_ts must be an ISO time")
    if b.get("promo", "none") not in PROMOS:
        errs.append(f"promo '{b.get('promo')}' unknown")
    boost = b.get("boost", 0)
    if not isinstance(boost, (int, float)) or not 0 <= boost <= 3:
        errs.append("boost must be a fraction such as 0.25")
    stake = b.get("stake", 5)
    if not isinstance(stake, (int, float)) or stake <= 0:
        errs.append("stake must be positive dollars")
    for p in ("p_market", "p_ours", "p_final"):
        if p in b and b[p] is not None and not (isinstance(b[p], (int, float)) and 0 < b[p] < 1):
            errs.append(f"{p} must be a chance between 0 and 1")
    legs = b.get("legs")
    if legs:
        if not isinstance(legs, list) or len(legs) < 2:
            errs.append("legs must be a list of 2 or more")
        else:
            for i, leg in enumerate(legs, 1):
                _check_selection(leg, f"leg {i}: ", errs, is_leg=True)
    else:
        _check_selection(b, "", errs)
    return errs


def bet_id(b):
    key = json.dumps({k: b.get(k) for k in ID_FIELDS}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(key.encode()).hexdigest()[:12]


def normalise(b):
    b = dict(b)
    b.setdefault("stake", 5)
    b.setdefault("real", False)
    b.setdefault("boost", 0)
    b.setdefault("promo", "boost" if b.get("boost") else "none")
    b["id"] = bet_id(b)
    b.setdefault("created_at", now_utc())
    return b


def add(rows, bets_path=BETS):
    """Validate and append. Duplicates (same id) are skipped. Returns (added, skipped, errors)."""
    existing = {b["id"] for b in read_jsonl(bets_path)}
    good, skipped, errors = [], [], []
    for i, raw in enumerate(rows, 1):
        errs = validate(raw)
        if errs:
            errors.append(f"bet {i} ({raw.get('player') or raw.get('game')}): " + "; ".join(errs))
            continue
        b = normalise(raw)
        if b["id"] in existing:
            skipped.append(b["id"])
            continue
        existing.add(b["id"])
        good.append(b)
    if errors:  # all or nothing, so a half-written card never lands
        return [], skipped, errors
    append_jsonl(bets_path, good)
    return good, skipped, errors


def amend(bet_id_, action, reason="", result=None, actual=None, bets_path=BETS, amend_path=AMEND):
    bets = {b["id"]: b for b in read_jsonl(bets_path)}
    if bet_id_ not in bets:
        raise SystemExit(f"no bet with id {bet_id_}")
    row = {"bet_id": bet_id_, "action": action, "at": now_utc(), "reason": reason}
    if action == "settle":
        if result not in RESULTS:
            raise SystemExit("result must be win, loss, push or void")
        row["result"] = result
        if actual is not None:
            row["actual"] = actual
    append_jsonl(amend_path, [row])
    return row


def verify(bets_path=BETS, seen_path=None):
    """Schema check of every row, unique ids, ids match content, and (if a seen-hash
    file is given) that no row the grader has seen before was edited or removed."""
    problems = []
    bets = read_jsonl(bets_path)
    ids = set()
    for n, b in enumerate(bets, 1):
        for e in validate(b):
            problems.append(f"row {n}: {e}")
        if b.get("id") != bet_id(b):
            problems.append(f"row {n}: id {b.get('id')} doesn't match its content (edited?)")
        if b.get("id") in ids:
            problems.append(f"row {n}: duplicate id {b.get('id')}")
        ids.add(b.get("id"))
    if seen_path and os.path.exists(seen_path):
        with open(seen_path) as fh:
            seen = json.load(fh)
        current = {b["id"]: row_hash(b) for b in bets if "id" in b}
        for i, h in seen.items():
            if i not in current:
                problems.append(f"bet {i} was removed from the ledger")
            elif current[i] != h:
                problems.append(f"bet {i} was edited after it was logged")
    return problems


def row_hash(b):
    return hashlib.sha256(json.dumps(b, sort_keys=True).encode()).hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("file")
    w = sub.add_parser("withdraw")
    w.add_argument("bet_id")
    w.add_argument("--reason", required=True)
    s = sub.add_parser("settle")
    s.add_argument("bet_id")
    s.add_argument("--result", required=True)
    s.add_argument("--actual", type=float)
    s.add_argument("--reason", default="")
    sub.add_parser("verify")
    sh = sub.add_parser("show")
    sh.add_argument("--date")
    args = ap.parse_args()

    if args.cmd == "add":
        if args.file.endswith(".jsonl"):  # e.g. the project's ledger_inbox.jsonl
            rows = read_jsonl(args.file)
        else:
            with open(args.file) as fh:
                data = json.load(fh)
            rows = data if isinstance(data, list) else [data]
        good, skipped, errors = add(rows)
        for e in errors:
            print("ERROR", e)
        if errors:
            print("Nothing added (fix the errors and run again).")
            sys.exit(1)
        for b in good:
            print("added", b["id"], b["contestant"], b.get("player") or b["game"], b["market"], b["side"],
                  b.get("line"), b["price"])
        if skipped:
            print("already in the ledger:", ", ".join(skipped))
    elif args.cmd == "withdraw":
        print(amend(args.bet_id, "withdraw", args.reason))
    elif args.cmd == "settle":
        print(amend(args.bet_id, "settle", args.reason, args.result, args.actual))
    elif args.cmd == "verify":
        probs = verify(seen_path=path("ledger", "state", "seen.json"))
        print("\n".join(probs) if probs else "ledger OK")
        sys.exit(1 if probs else 0)
    elif args.cmd == "show":
        for b in read_jsonl(BETS):
            if not args.date or b["date"] == args.date:
                print(b["id"], b["date"], b["contestant"], b.get("player") or b["game"], b["market"], b["side"],
                      b.get("line"), b["price"], b["book"])


if __name__ == "__main__":
    main()
