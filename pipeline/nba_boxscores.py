"""Incremental NBA box scores for the current season, from ESPN's public JSON.

Writes data/nba/boxscores_2026_27.csv: one row per player per game, including
players who were listed but did not play (dnp=1, with ESPN's reason), so later
steps can measure with/without effects and missed games.

Usage: python3 -I pipeline/nba_boxscores.py [--start 2026-10-20] [--end YYYY-MM-DD]
The end defaults to yesterday (ET). Dates already in the file are skipped unless
--refetch is given.
"""
import argparse
import datetime as dt
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ESPN, get_json, path, read_csv, today_et, to_et, write_csv  # noqa: E402

OUT = path("data", "nba", "boxscores_2026_27.csv")
CHECKED = path("data", "nba", "_checked_dates.txt")  # finished dates, including days with no games
SEASON_START = dt.date(2026, 10, 20)
STAT_KEYS = ["minutes", "points", "rebounds", "offensiveRebounds", "defensiveRebounds", "assists",
             "steals", "blocks", "turnovers", "fouls", "plusMinus",
             "fieldGoalsMade-fieldGoalsAttempted", "threePointFieldGoalsMade-threePointFieldGoalsAttempted",
             "freeThrowsMade-freeThrowsAttempted"]
COLS = ["date", "event", "team", "opp", "home", "espn_id", "player", "starter", "dnp", "dnp_reason"] + STAT_KEYS


def parse_summary(summ, date_iso, event_id):
    """Turn one ESPN summary payload into player rows (played and DNP)."""
    rows = []
    teams = summ.get("boxscore", {}).get("players", [])
    abbrs = [t.get("team", {}).get("abbreviation", "") for t in teams]
    home_abbr = ""
    for comp in summ.get("header", {}).get("competitions", [])[:1]:
        for c in comp.get("competitors", []):
            if c.get("homeAway") == "home":
                home_abbr = c.get("team", {}).get("abbreviation", "")
    for i, team in enumerate(teams):
        tabb = abbrs[i]
        opp = abbrs[1 - i] if len(abbrs) == 2 else ""
        for st in team.get("statistics", [])[:1]:
            keys = st.get("keys") or []
            for a in st.get("athletes", []):
                ath = a.get("athlete", {})
                base = {"date": date_iso, "event": event_id, "team": tabb, "opp": opp,
                        "home": int(tabb == home_abbr), "espn_id": ath.get("id", ""),
                        "player": ath.get("displayName", ""), "starter": int(bool(a.get("starter"))),
                        "dnp": 0, "dnp_reason": ""}
                if a.get("didNotPlay") or not a.get("stats"):
                    base.update(dnp=1, dnp_reason=(a.get("reason") or "").strip(), minutes="0")
                    rows.append(base)
                    continue
                rec = dict(zip(keys, a["stats"]))
                base.update({k: rec.get(k, "") for k in STAT_KEYS})
                rows.append(base)
    return rows


def fetch_date(d):
    sb = get_json(f"{ESPN}/scoreboard?dates={d:%Y%m%d}")
    if sb is None:
        return None  # network failure: leave the date for the next run
    rows = []
    for ev in sb.get("events", []):
        state = ev.get("status", {}).get("type", {}).get("state")
        stype = ev.get("season", {}).get("type")
        if state != "post" or stype not in (2, 3, None):  # regular season and playoffs, finished only
            continue
        summ = get_json(f"{ESPN}/summary?event={ev['id']}")
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
    existing = read_csv(OUT)
    have = {r["date"] for r in existing}
    checked = set(open(CHECKED).read().split()) if os.path.exists(CHECKED) else set()
    have |= checked
    d, end = dt.date.fromisoformat(a.start), dt.date.fromisoformat(a.end)
    added, failed = 0, []
    while d <= end:
        if a.refetch or d.isoformat() not in have:
            rows = fetch_date(d)
            if rows is None:
                failed.append(d.isoformat())
            else:
                checked.add(d.isoformat())
            if rows:
                existing = [r for r in existing if r["date"] != d.isoformat()] + rows
                added += len(rows)
        d += dt.timedelta(days=1)
    existing.sort(key=lambda r: (r["date"], r["event"], r["team"], r["player"]))
    write_csv(OUT, existing, COLS)
    with open(CHECKED, "w") as fh:
        fh.write("\n".join(sorted(checked)) + "\n")
    print(f"box scores: +{added} rows, {len(existing)} total, failed dates: {failed or 'none'}")
    return 1 if failed and not added else 0


if __name__ == "__main__":
    sys.exit(main())
