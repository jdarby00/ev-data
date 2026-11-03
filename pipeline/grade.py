"""Nightly grader: settles every ledger bet from ESPN box scores, measures closing-line
value from the collector's snapshots, and writes the scoreboard. Standard library only.

Reads:  ledger/bets.jsonl, ledger/amendments.jsonl, data/nba/boxscores_2026_27.csv,
        data/nba/_checked_dates.txt, data/nba/slate/*.json, prices/*.json
Writes: ledger/results.jsonl (derived, rewritten each run), ledger/scoreboard.md,
        ledger/state/seen.json (content hash of every bet ever seen, for tamper checks)

Usage: python3 -I pipeline/grade.py
"""
import datetime as dt
import glob
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger as L  # noqa: E402
from common import ET, num, path, read_csv  # noqa: E402

BOX = path("data", "nba", "boxscores_2026_27.csv")
CHECKED = path("data", "nba", "_checked_dates.txt")
SLATES = path("data", "nba", "slate", "x.json").rsplit("/", 1)[0]
PRICES = path("prices", "x.json").rsplit("/", 1)[0]
RESULTS = path("ledger", "results.jsonl")
BOARD = path("ledger", "scoreboard.md")
SEEN = path("ledger", "state", "seen.json")
PAPER_START = 500.0
SCORED_SOURCES = {"collector", "slip"}  # web prices are assumed and reported apart
MARKET_KEYS = {"points": "player_points", "rebounds": "player_rebounds", "assists": "player_assists",
               "threes": "player_threes", "pra": "player_points_rebounds_assists",
               "pr": "player_points_rebounds", "pa": "player_points_assists",
               "ra": "player_rebounds_assists", "spread": "spreads", "total": "totals",
               "moneyline": "h2h"}
BUCKETS = [(0.50, 0.55), (0.55, 0.60), (0.60, 0.65), (0.65, 0.70), (0.70, 1.01)]


# ---------- small helpers ----------

def norm_name(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z ]", " ", s.replace("-", " "))
    return " ".join(w for w in s.split() if w not in {"jr", "sr", "ii", "iii", "iv", "v"})


def dec(american):
    a = float(american)
    return 1 + a / 100 if a > 0 else 1 + 100 / -a


def to_american(d):
    return round((d - 1) * 100) if d >= 2 else round(-100 / (d - 1))


def ts(s):
    return L.parse_ts(s) if s else None


# ---------- data loading ----------

def load_box(rows):
    """Index box scores: players[(date, name)] -> rows; teams[(date, abbr)] -> event info."""
    players, teams = {}, {}
    for r in rows:
        d = r["date"]
        players.setdefault((d, norm_name(r["player"])), []).append(r)
        t = teams.setdefault((d, r["team"]), {"event": r["event"], "opp": r["opp"], "home": r["home"], "pts": 0.0})
        t["pts"] += num(r.get("points"))
    return players, teams


def load_checked(p=CHECKED):
    if not os.path.exists(p):
        return set()
    with open(p) as fh:
        return {line.strip() for line in fh if line.strip()}


def load_slates(folder=SLATES):
    """Team names and tip times: names[full name] -> abbr, tips[(date, AWAY@HOME)] -> aware UTC."""
    names, tips = {}, {}
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        try:
            with open(f) as fh:
                s = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        for g in s.get("games", []):
            names[g.get("away_name", "")] = g.get("away")
            names[g.get("home_name", "")] = g.get("home")
            try:
                tip = dt.datetime.strptime(g["tip_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
                tips[(s.get("date"), f"{g['away']}@{g['home']}")] = tip.astimezone(dt.timezone.utc)
            except (KeyError, ValueError):
                pass
    names.pop("", None)
    return names, tips


def load_prices(folder=PRICES):
    out = {}
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        try:
            with open(f) as fh:
                out[os.path.basename(f)[:-5]] = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
    return out


# ---------- settling ----------

def stat_value(r, market):
    p, rb, a = num(r.get("points")), num(r.get("rebounds")), num(r.get("assists"))
    t = num(r.get("threePointFieldGoalsMade-threePointFieldGoalsAttempted"))
    return {"points": p, "rebounds": rb, "assists": a, "threes": t, "pra": p + rb + a,
            "pr": p + rb, "pa": p + a, "ra": rb + a}[market]


def over_under(actual, line, side):
    if actual == line:
        return "push"
    return "win" if (actual > line) == (side == "over") else "loss"


def find_game(teams, date, game):
    """Points per team for AWAY@HOME on a date, or None if that game isn't in the box scores."""
    away, home = game.split("@", 1)
    a, h = teams.get((date, away)), teams.get((date, home))
    if not a or not h or a["opp"] != home or a["event"] != h["event"]:
        return None
    return {away: a["pts"], home: h["pts"]}


def settle_selection(sel, date, box, checked):
    """One selection -> (result or None if pending, actual, reason)."""
    players, teams = box
    if date not in checked:
        return None, None, "box scores for this date not in yet"
    m = sel["market"]
    if m in L.PROP_MARKETS:
        rows = players.get((date, norm_name(sel["player"])), [])
        if sel.get("team"):
            rows = [r for r in rows if r["team"] == sel["team"]] or rows
        if len(rows) > 1:
            return None, None, "two players with this name; add team"
        if not rows:
            return "void", None, "player not in the box score (inactive or name mismatch)"
        r = rows[0]
        if r.get("dnp") == "1" or num(r.get("minutes")) <= 0:
            return "void", None, "did not play"
        actual = stat_value(r, m)
        return over_under(actual, float(sel["line"]), sel["side"]), actual, ""
    if m in L.GAME_MARKETS:
        g = find_game(teams, date, sel["game"])
        if not g:
            return "void", None, "game not in the box scores (postponed?)"
        away, home = sel["game"].split("@", 1)
        if m == "total":
            actual = g[away] + g[home]
            return over_under(actual, float(sel["line"]), sel["side"]), actual, ""
        if m == "team_total":
            if sel["team"] not in g:
                return None, None, "team not in this game"
            return over_under(g[sel["team"]], float(sel["line"]), sel["side"]), g[sel["team"]], ""
        side = sel["side"]
        if side not in g:
            return None, None, f"side {side} not in this game"
        other = home if side == away else away
        margin = g[side] - g[other]
        if m == "moneyline":
            return ("win" if margin > 0 else "loss"), margin, ""
        cover = margin + float(sel["line"])
        return ("push" if cover == 0 else "win" if cover > 0 else "loss"), margin, ""
    return None, None, "market needs a manual settle"


def payout(b, result, price):
    """Cash profit and stake counted toward ROI, given a result and plain American price."""
    stake = float(b.get("stake", 5))
    promo = b.get("promo", "none")
    staked = 0.0 if promo == "bonus_bet" else stake
    if result == "win":
        return stake * (dec(price) - 1) * (1 + float(b.get("boost", 0))), staked
    if result == "loss":
        return (0.0 if promo == "bonus_bet" else -stake), staked
    return 0.0, 0.0  # push or void


# ---------- closing-line value ----------

def devig_side(outcomes, player, line, side_label):
    """Average multiplicative no-vig chance of one side across books quoting both sides."""
    ps = []
    for book, outs in outcomes.items():
        mine = [o for o in outs if norm_name(o.get("player")) == player and o.get("line") == line]
        a = [o for o in mine if o.get("side") == side_label]
        others = [o for o in mine if o.get("side") != side_label]
        if a and others:
            qa, qb = 1 / dec(a[0]["price"]), 1 / dec(others[0]["price"])
            ps.append(qa / (qa + qb))
    return sum(ps) / len(ps) if ps else None


def closing(b, prices, names, tips):
    """Closing snapshot info for a single bet, or a reason it can't be measured."""
    key = MARKET_KEYS.get(b["market"])
    day = prices.get(b["date"])
    if not key or not day or b.get("legs"):
        return {"clv_reason": "no collector prices for this market"}
    away, home = b["game"].split("@", 1)
    group = None
    for g in day.get("groups", {}).values():
        if g.get("market") == key and {names.get(g.get("api_away")), names.get(g.get("api_home"))} == {away, home}:
            group = g
            break
    if not group:
        return {"clv_reason": "market not priced by the collector"}
    tip = ts(group.get("commence_time")) or tips.get((b["date"], b["game"]))
    bet_ts = ts(b["price_ts"])
    later = [s for s in group.get("snapshots", [])
             if ts(s["fetched_at"]) > bet_ts and (tip is None or ts(s["fetched_at"]) <= tip)]
    if not later:
        return {"clv_reason": "no snapshot after the bet and before the start"}
    snap = max(later, key=lambda s: s["fetched_at"])
    outcomes = {bk: v.get("outcomes", []) for bk, v in snap.get("books", {}).items()}
    if b["market"] in L.PROP_MARKETS:
        who, label = norm_name(b["player"]), b["side"].capitalize()
    elif b["market"] == "total":
        who, label = "", b["side"].capitalize()
    else:
        full = {v: k for k, v in names.items()}.get(b["side"])
        who, label = "", full
    line = None if b["market"] == "moneyline" else float(b["line"])
    if b["market"] == "spread":
        line = float(b["line"])
    fair = devig_side(outcomes, who, line, label)
    same = [o for o in outcomes.get(b["book"], [])
            if norm_name(o.get("player")) == who and o.get("line") == line and o.get("side") == label]
    out = {"close_ts": snap["fetched_at"], "close_kind": snap.get("kind"),
           "close_price": same[0]["price"] if same else None,
           "close_fair": round(fair, 4) if fair is not None else None}
    if fair is None:
        out["clv_reason"] = "line moved or one side missing at the close"
        return out
    out["clv_ev"] = round(fair * dec(b["price"]) - 1, 4)
    if same:
        out["beat_close"] = dec(b["price"]) > dec(same[0]["price"])
    return out


# ---------- one bet ----------

def grade_bet(b, amends, box, checked, prices, names, tips):
    r = {"id": b["id"], "date": b["date"], "contestant": b["contestant"], "real": b.get("real", False),
         "price_source": b["price_source"], "p_final": b.get("p_final"), "status": "pending"}
    tip = tips.get((b["date"], b["game"])) if not b.get("legs") else None
    if tip and ts(b.get("created_at")) and ts(b["created_at"]) >= tip:
        r.update(status="late", reason="logged after the start; not scored")
        return r
    for a in amends:
        if a["action"] == "withdraw":
            if tip and ts(a["at"]) >= tip:
                r["issue"] = "withdrawal after the start ignored"
                continue
            r.update(status="withdrawn", reason=a.get("reason", ""))
            return r
    manual = [a for a in amends if a["action"] == "settle"]
    price = b["price"]
    if manual:
        result, actual, reason = manual[-1]["result"], manual[-1].get("actual"), "settled by hand"
    elif b.get("legs"):
        results = []
        for leg in b["legs"]:
            res, _, why = settle_selection(leg, b["date"], box, checked)
            results.append((res, leg, why))
        if any(res is None for res, _, _ in results):
            r["reason"] = "; ".join(w for res, _, w in results if res is None)
            return r
        if any(res == "loss" for res, _, _ in results):
            result = "loss"
        elif all(res in ("void", "push") for res, _, _ in results):
            result = "void"
        else:
            live = [leg for res, leg, _ in results if res == "win"]
            if len(live) < len(b["legs"]):
                if not all("price" in leg for leg in live):
                    r.update(status="needs_review", reason="a leg voided and leg prices are missing")
                    return r
                d = 1.0
                for leg in live:
                    d *= dec(leg["price"])
                price = to_american(d)
            result = "win"
        actual, reason = None, ""
        r["legs"] = [res for res, _, _ in results]
    else:
        result, actual, reason = settle_selection(b, b["date"], box, checked)
        if result is None:
            r["reason"] = reason
            return r
    profit, staked = payout(b, result, price)
    r.update(status="graded", result=result, actual=actual, profit=profit, staked=staked, reason=reason,
             bonus_earned=float(b.get("stake", 5)) if (b.get("promo") == "reset" and result == "loss") else 0.0)
    r.update(closing(b, prices, names, tips))
    return r


# ---------- scoreboard ----------

def summarise(rows):
    g = [x for x in rows if x["status"] == "graded"]
    w = sum(x["result"] == "win" for x in g)
    lo = sum(x["result"] == "loss" for x in g)
    pu = sum(x["result"] == "push" for x in g)
    vo = sum(x["result"] == "void" for x in g)
    staked = sum(x["staked"] for x in g)
    profit = round(sum(x["profit"] for x in g), 2)
    run = peak = dd = 0.0
    for x in g:
        run += x["profit"]
        peak = max(peak, run)
        dd = max(dd, peak - run)
    clv = [x["clv_ev"] for x in g if x.get("clv_ev") is not None and x["result"] != "void"]
    beat = [x["beat_close"] for x in g if x.get("beat_close") is not None and x["result"] != "void"]
    return {"n": len(g), "w": w, "l": lo, "p": pu, "v": vo, "staked": round(staked, 2), "profit": profit,
            "roi": (profit / staked) if staked else None, "max_dd": round(dd, 2),
            "clv_n": len(clv), "clv_avg": (sum(clv) / len(clv)) if clv else None,
            "beat_pct": (sum(beat) / len(beat)) if beat else None,
            "pending": sum(x["status"] == "pending" for x in rows)}


def calibration(rows):
    out = []
    g = [x for x in rows if x["status"] == "graded" and x.get("p_final") and x["result"] in ("win", "loss")]
    for lo, hi in BUCKETS:
        b = [x for x in g if lo <= x["p_final"] < hi]
        if b:
            out.append((lo, hi, len(b), sum(x["p_final"] for x in b) / len(b),
                        sum(x["result"] == "win" for x in b) / len(b)))
    brier = (sum((x["p_final"] - (x["result"] == "win")) ** 2 for x in g) / len(g)) if g else None
    return out, brier


def pct(x, d=1):
    return "–" if x is None else f"{x * 100:+.{d}f}%" if x < 0 or x > 0 else f"{0:.{d}f}%"


def table(groups, real=False):
    head = "| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |"
    lines = [head, "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name in sorted(groups, key=lambda k: -summarise(groups[k])["profit"]):
        s = summarise(groups[name])
        bank = f"${s['profit']:+.2f}" if real else f"${PAPER_START + s['profit']:.2f}"
        beat = "–" if s["beat_pct"] is None else f"{s['beat_pct'] * 100:.0f}%"
        clv = "–" if not s["clv_n"] else f"{s['clv_n']}, {pct(s['clv_avg'])}, {beat}"
        lines.append(f"| {name} | {s['n']} | {s['w']}–{s['l']}–{s['p']}–{s['v']} | ${s['profit']:+.2f} | "
                     f"{pct(s['roi'])} | {bank} | ${s['max_dd']:.2f} | {clv} | {s['pending']} |")
    return lines


def scoreboard(bets, results, problems, now=None):
    now = now or dt.datetime.now(ET)
    by = {r["id"]: r for r in results}
    lines = ["# Scoreboard", "",
             f"Built {now.strftime('%a %d %b %Y, %-I:%M %p ET')} by `pipeline/grade.py` from `ledger/bets.jsonl`. "
             "Derived file: don't edit it; it's rebuilt every pipeline run.", ""]
    if problems:
        lines += ["## Ledger problems", ""] + [f"- {p}" for p in problems] + [""]
    real = {}
    paper, web = {}, {}
    for b in bets:
        r = by[b["id"]]
        if r["status"] in ("withdrawn", "late"):
            continue
        if b.get("real"):
            real.setdefault(b["contestant"], []).append(r)
        elif b["price_source"] in SCORED_SOURCES:
            paper.setdefault(b["contestant"], []).append(r)
        else:
            web.setdefault(b["contestant"], []).append(r)
    lines += ["## Jake's real money", ""]
    lines += table(real, real=True) if real else ["No real bets logged yet."]
    lines += ["", f"## Paper contestants at real prices (start ${PAPER_START:.0f}, logged stake)", "",
              "CLV is the expected value of the bet price against the de-vigged closing price "
              "(all books quoting both sides). It needs a collector snapshot taken after the bet and "
              "before the start. Beat close = the bet price is better than the same book's closing price.", ""]
    lines += table(paper) if paper else ["No paper bets at real prices yet."]
    if web:
        lines += ["", "## Assumed (web) prices, reported apart", ""] + table(web)
    cal_rows = [by[b["id"]] for b in bets if b["price_source"] in SCORED_SOURCES and by[b["id"]]["status"] == "graded"]
    cal, brier = calibration(cal_rows)
    lines += ["", "## Calibration (real-price bets with a final win chance)", ""]
    if cal:
        lines += ["| Stated chance | Bets | Avg stated | Hit rate |", "| --- | --- | --- | --- |"]
        lines += [f"| {lo * 100:.0f}–{min(hi, 1) * 100:.0f}% | {n} | {p * 100:.1f}% | {h * 100:.1f}% |"
                  for lo, hi, n, p, h in cal]
        lines += ["", f"Brier score {brier:.3f} (a coin flip is 0.250)."]
    else:
        lines += ["No graded bets with a stated chance yet."]
    issues = [(r["id"], r.get("reason") or r.get("issue")) for r in results
              if r["status"] in ("needs_review",) or r.get("issue")]
    pend = [r for r in results if r["status"] == "pending"]
    lines += ["", "## Open items", ""]
    lines += [f"- {i}: {why}" for i, why in issues] or []
    lines += [f"- {len(pend)} pending (waiting for box scores or a manual settle)."] if pend else []
    if not issues and not pend:
        lines += ["None."]
    return "\n".join(lines) + "\n"


# ---------- main ----------

def run(bets_path=L.BETS, amend_path=L.AMEND, box_path=BOX, checked_path=CHECKED, slates=SLATES,
        prices_dir=PRICES, results_path=RESULTS, board_path=BOARD, seen_path=SEEN, now=None):
    bets = L.read_jsonl(bets_path)
    problems = L.verify(bets_path, seen_path)
    amends = {}
    for a in L.read_jsonl(amend_path):
        amends.setdefault(a["bet_id"], []).append(a)
    box = load_box(read_csv(box_path))
    checked = load_checked(checked_path)
    names, tips = load_slates(slates)
    prices = load_prices(prices_dir)
    bets.sort(key=lambda b: (b["date"], b.get("created_at", ""), b["id"]))
    results = [grade_bet(b, amends.get(b["id"], []), box, checked, prices, names, tips) for b in bets]
    with open(results_path, "w") as fh:
        for r in results:
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    with open(board_path, "w") as fh:
        fh.write(scoreboard(bets, results, problems, now))
    seen = {}
    if os.path.exists(seen_path):
        with open(seen_path) as fh:
            seen = json.load(fh)
    for b in bets:
        seen.setdefault(b["id"], L.row_hash(b))  # first-seen hash is kept for good
    os.makedirs(os.path.dirname(seen_path), exist_ok=True)
    with open(seen_path, "w") as fh:
        json.dump(seen, fh, indent=0, sort_keys=True)
    return bets, results, problems


def main():
    bets, results, problems = run()
    graded = sum(r["status"] == "graded" for r in results)
    print(f"{len(bets)} bets, {graded} graded, {sum(r['status'] == 'pending' for r in results)} pending")
    for p in problems:
        print("PROBLEM", p)


if __name__ == "__main__":
    main()
