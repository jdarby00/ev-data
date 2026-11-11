"""Incremental NFL player game logs for the current season, from ESPN's public JSON.

Writes data/nfl/boxscores_2026.csv: one row per player per game with passing, rushing and receiving
numbers, so every NFL prop leg can be checked against the player's own record at its line (PICKS PROTOCOL,
gate 1a: built 11 Nov 2026 because NFL legs had no history check in code).

A date is marked done only when every game on it is final (same rule as the NBA file).
Usage: python3 -I pipeline/nfl_boxscores.py [--start 2026-09-09] [--end YYYY-MM-DD] [--refetch]
"""
import argparse
import datetime as dt
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, path, read_csv, today_et, to_et, write_csv  # noqa: E402

NFL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"
OUT = path("data", "nfl", "boxscores_2026.csv")
CHECKED = path("data", "nfl", "_checked_dates.txt")
SEASON_START = dt.date(2026, 9, 9)
# our column -> (ESPN category, candidate keys or labels; "a/b" style values are split by SPLIT)
FIELDS = {
    "pass_cmp": ("passing", ["completions/passingAttempts", "C/ATT"], 0),
    "pass_att": ("passing", ["completions/passingAttempts", "C/ATT"], 1),
    "pass_yds": ("passing", ["passingYards", "YDS"], None),
    "pass_tds": ("passing", ["passingTouchdowns", "TD"], None),
    "ints": ("passing", ["interceptions", "INT"], None),
    "rush_att": ("rushing", ["rushingAttempts", "CAR"], None),
    "rush_yds": ("rushing", ["rushingYards", "YDS"], None),
    "rush_tds": ("rushing", ["rushingTouchdowns", "TD"], None),
    "long_rush": ("rushing", ["longRushing", "LONG"], None),
    "receptions": ("receiving", ["receptions", "REC"], None),
    "rec_yds": ("receiving", ["receivingYards", "YDS"], None),
    "rec_tds": ("receiving", ["receivingTouchdowns", "TD"], None),
    "long_rec": ("receiving", ["longReception", "LONG"], None),
    "targets": ("receiving", ["receivingTargets", "TGTS"], None),
}
COLS = ["date", "event", "team", "opp", "espn_id", "player"] + list(FIELDS)


def _num(v, part):
    s = str(v if v is not None else "").strip()
    if part is not None:
        bits = s.replace("-", "/").split("/")
        s = bits[part] if len(bits) > part else ""
    try:
        return str(int(float(s)))
    except ValueError:
        return ""


def parse_summary(summ, date_iso, event_id):
    """One ESPN NFL summary -> one row per player who recorded a pass, rush or catch."""
    teams = summ.get("boxscore", {}).get("players", [])
    abbrs = [t.get("team", {}).get("abbreviation", "") for t in teams]
    rows = {}
    for i, team in enumerate(teams):
        tabb = abbrs[i]
        opp = abbrs[1 - i] if len(abbrs) == 2 else ""
        for st in team.get("statistics", []):
            cat = (st.get("name") or "").lower()
            if cat not in ("passing", "rushing", "receiving"):
                continue  # defence, kicking and returns aren't prop stats we check
            keys, labels = st.get("keys") or [], st.get("labels") or []
            for a in st.get("athletes", []):
                ath = a.get("athlete", {})
                name = ath.get("displayName", "")
                if not name:
                    continue
                row = rows.setdefault((tabb, name), {"date": date_iso, "event": event_id, "team": tabb, "opp": opp,
                                                     "espn_id": ath.get("id", ""), "player": name,
                                                     **{c: "0" for c in FIELDS}})
                stats = a.get("stats") or []
                for col, (want, names, part) in FIELDS.items():
                    if want != cat:
                        continue
                    idx = next((keys.index(n) for n in names if n in keys), None)
                    if idx is None:
                        idx = next((labels.index(n) for n in names if n in labels), None)
                    if idx is not None and idx < len(stats):
                        v = _num(stats[idx], part)
                        if v != "":
                            row[col] = v
    return list(rows.values())


def fetch_date(d):
    sb = get_json(f"{NFL}/scoreboard?dates={d:%Y%m%d}")
    if sb is None:
        return None
    rows = []
    fetch_date.unfinished = 0
    for ev in sb.get("events", []):
        state = ev.get("status", {}).get("type", {}).get("state")
        if ev.get("season", {}).get("type") not in (2, 3, None):
            continue
        if state != "post":
            fetch_date.unfinished += 1
            continue
        summ = get_json(f"{NFL}/summary?event={ev['id']}")
        if summ is None:
            return None
        rows += parse_summary(summ, to_et(ev["date"]).date().isoformat(), ev["id"])
        time.sleep(0.25)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=SEASON_START.isoformat())
    ap.add_argument("--end", default=(today_et() - dt.timedelta(days=1)).isoformat())
    ap.add_argument("--refetch", action="store_true")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    existing = read_csv(OUT) if os.path.exists(OUT) else []
    checked = set(open(CHECKED).read().split()) if os.path.exists(CHECKED) else set()
    d, end = dt.date.fromisoformat(a.start), dt.date.fromisoformat(a.end)
    added, failed = 0, []
    while d <= end:
        if a.refetch or d.isoformat() not in checked:
            rows = fetch_date(d)
            if rows is None:
                failed.append(d.isoformat())
            elif not getattr(fetch_date, "unfinished", 0) or d < today_et() - dt.timedelta(days=3):
                checked.add(d.isoformat())
            if rows:
                existing = [r for r in existing if r["date"] != d.isoformat()] + rows
                added += len(rows)
        d += dt.timedelta(days=1)
    existing.sort(key=lambda r: (r["date"], r["event"], r["team"], r["player"]))
    write_csv(OUT, existing, COLS)
    with open(CHECKED, "w") as fh:
        fh.write("\n".join(sorted(checked)) + "\n")
    games = len({r["event"] for r in existing})
    print(f"nfl box scores: +{added} rows, {len(existing)} total over {games} games, failed dates: {failed or 'none'}")
    return 1 if failed and not added else 0


if __name__ == "__main__":
    sys.exit(main())
