"""Player game logs for soccer and NHL from ESPN's public JSON, for the leg checks (PICKS PROTOCOL gate 1a).

Writes one row per player per game with every stat ESPN lists for him:
  data/soccer/gamelogs_2026_27.csv  (Premier League, La Liga, Bundesliga, Serie A, Champions League)
  data/nhl/gamelogs_2026_27.csv
Columns are date, league, event, team, opp, player, starter, sub_in, then ESPN's own stat names (whatever the
feed carries: shots, shots on target, goals, assists, time on ice...). A date is done only when every game on
it is final. Usage: python3 -I pipeline/espn_gamelogs.py [--sport soccer|nhl] [--refetch]
"""
import argparse
import datetime as dt
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, path, read_csv, today_et, to_et, write_csv  # noqa: E402

SITE = "https://site.api.espn.com/apis/site/v2/sports"
SPORTS = {
    "soccer": {"leagues": [("soccer", "eng.1"), ("soccer", "esp.1"), ("soccer", "ger.1"), ("soccer", "ita.1"),
                           ("soccer", "uefa.champions")], "start": dt.date(2026, 8, 8)},
    "nhl": {"leagues": [("hockey", "nhl")], "start": dt.date(2026, 10, 6)},
}
BASE = ["date", "league", "event", "team", "opp", "player", "starter", "sub_in"]


def _clean(v):
    return str(v if v is not None else "").strip()


def parse_summary(summ, date_iso, league, event_id):
    """Rows from either ESPN layout: boxscore.players (NHL, by category) or rosters (soccer, per-player stat list)."""
    rows = {}

    def row(team, opp, name):
        return rows.setdefault((team, name), {"date": date_iso, "league": league, "event": event_id, "team": team,
                                              "opp": opp, "player": name, "starter": "", "sub_in": ""})
    teams = summ.get("boxscore", {}).get("players") or []
    abbrs = [t.get("team", {}).get("abbreviation", "") for t in teams]
    for i, team in enumerate(teams):
        opp = abbrs[1 - i] if len(abbrs) == 2 else ""
        for st in team.get("statistics", []):
            keys = st.get("keys") or st.get("labels") or []
            for a in st.get("athletes", []):
                name = (a.get("athlete") or {}).get("displayName", "")
                if not name or not a.get("stats"):
                    continue
                r = row(abbrs[i], opp, name)
                r["starter"] = str(int(bool(a.get("starter")))) if "starter" in a else r["starter"]
                for k, v in zip(keys, a["stats"]):
                    r.setdefault(_clean(k), _clean(v))
    rosters = summ.get("rosters") or []
    rabbr = [t.get("team", {}).get("abbreviation", "") for t in rosters]
    for i, team in enumerate(rosters):
        opp = rabbr[1 - i] if len(rabbr) == 2 else ""
        for a in team.get("roster") or []:
            name = (a.get("athlete") or {}).get("displayName", "")
            played = a.get("starter") or a.get("subbedIn")
            if not name or not played:
                continue  # unused substitutes have no game to count
            r = row(rabbr[i], opp, name)
            r["starter"], r["sub_in"] = str(int(bool(a.get("starter")))), str(int(bool(a.get("subbedIn"))))
            for s in a.get("stats") or []:
                k = _clean(s.get("name") or s.get("abbreviation"))
                if k:
                    r.setdefault(k, _clean(s.get("value") if s.get("value") is not None else s.get("displayValue")))
    return list(rows.values())


def fetch_date(sport, league, d):
    """(rows, unfinished games) for one league and date, or (None, 0) on a network failure."""
    sb = get_json(f"{SITE}/{sport}/{league}/scoreboard?dates={d:%Y%m%d}")
    if sb is None:
        return None, 0
    rows, unfinished = [], 0
    for ev in sb.get("events", []):
        if ev.get("status", {}).get("type", {}).get("state") != "post":
            unfinished += 1
            continue
        if not ev.get("status", {}).get("type", {}).get("completed", True):
            continue  # postponed or abandoned
        summ = get_json(f"{SITE}/{sport}/{league}/summary?event={ev['id']}")
        if summ is None:
            return None, 0
        rows += parse_summary(summ, to_et(ev["date"]).date().isoformat(), league, ev["id"])
        time.sleep(0.2)
    return rows, unfinished


def run(name, refetch=False, end=None):
    cfg = SPORTS[name]
    out = path("data", name, "gamelogs_2026_27.csv")
    checked_path = path("data", name, "_checked_dates.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    existing = read_csv(out) if os.path.exists(out) else []
    checked = set(open(checked_path).read().split()) if os.path.exists(checked_path) else set()
    d, end = cfg["start"], end or today_et() - dt.timedelta(days=1)
    added, failed = 0, []
    while d <= end:
        if refetch or d.isoformat() not in checked:
            day_rows, ok, unfinished = [], True, 0
            for sport, league in cfg["leagues"]:
                rows, u = fetch_date(sport, league, d)
                if rows is None:
                    ok = False
                    break
                day_rows += rows
                unfinished += u
            if not ok:
                failed.append(d.isoformat())
            else:
                if not unfinished or d < today_et() - dt.timedelta(days=3):
                    checked.add(d.isoformat())
                if day_rows:
                    existing = [r for r in existing if r["date"] != d.isoformat()] + day_rows
                    added += len(day_rows)
        d += dt.timedelta(days=1)
    stats = sorted({k for r in existing for k in r} - set(BASE))
    existing.sort(key=lambda r: (r["date"], r["league"], r["event"], r["team"], r["player"]))
    write_csv(out, [{c: r.get(c, "") for c in BASE + stats} for r in existing], BASE + stats)
    with open(checked_path, "w") as fh:
        fh.write("\n".join(sorted(checked)) + "\n")
    print(f"{name} game logs: +{added} rows, {len(existing)} total, {len({r['event'] for r in existing})} games, "
          f"stats {stats[:12]}{'...' if len(stats) > 12 else ''}, failed dates: {failed[:5] or 'none'}")
    return 1 if failed and not added else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sport", choices=list(SPORTS))
    ap.add_argument("--refetch", action="store_true")
    a = ap.parse_args()
    rc = 0
    for name in ([a.sport] if a.sport else list(SPORTS)):
        rc |= run(name, a.refetch)
    return rc


if __name__ == "__main__":
    sys.exit(main())
