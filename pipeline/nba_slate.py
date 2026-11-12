"""Today's NBA slate: games, tip times (ET), ESPN-listed spread and total, and injuries.

Writes data/nba/slate/<date>.json. Run several times a day; each run overwrites the
file with the latest injuries and lines, and keeps a short history of status changes
so late downgrades are visible.

Usage: python3 -I pipeline/nba_slate.py [--date YYYY-MM-DD]
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ESPN, ET, get_json, path, today_et, to_et, write_json  # noqa: E402


def parse_scoreboard(sb):
    games = []
    for ev in sb.get("events", []):
        comp = (ev.get("competitions") or [{}])[0]
        teams = {c.get("homeAway"): c.get("team", {}) for c in comp.get("competitors", [])}
        odds = (comp.get("odds") or [{}])[0]
        tip = to_et(ev["date"])
        games.append({
            "event": ev.get("id"),
            "tip_et": tip.strftime("%Y-%m-%d %H:%M"),
            "away": teams.get("away", {}).get("abbreviation", ""),
            "home": teams.get("home", {}).get("abbreviation", ""),
            "away_name": teams.get("away", {}).get("displayName", ""),
            "home_name": teams.get("home", {}).get("displayName", ""),
            "state": ev.get("status", {}).get("type", {}).get("state", ""),
            "spread_text": odds.get("details", ""),
            "spread": odds.get("spread"),
            "total": odds.get("overUnder"),
            "odds_source": (odds.get("provider") or {}).get("name", ""),
            "season_type": ev.get("season", {}).get("type"),
        })
    games.sort(key=lambda g: (g["tip_et"], g["home"]))
    return games


def parse_injuries(payload):
    """ESPN injuries feed -> {team display name: [ {player, status, detail, date} ]}."""
    out = {}
    for team in (payload or {}).get("injuries", []):
        name = team.get("displayName") or team.get("team", {}).get("displayName", "")
        rows = []
        for inj in team.get("injuries", []):
            ath = inj.get("athlete", {})
            rows.append({
                "player": ath.get("displayName", ""),
                "status": inj.get("status", ""),
                "detail": inj.get("shortComment") or inj.get("longComment") or "",
                "type": (inj.get("type") or {}).get("description", ""),
                "updated": inj.get("date", ""),
            })
        if name:
            out[name] = rows
    return out


def status_changes(old_inj, new_inj, stamp):
    """List of status changes between two injury maps (only for teams present in both runs)."""
    changes = []
    for team, rows in new_inj.items():
        before = {r["player"]: r["status"] for r in old_inj.get(team, [])}
        for r in rows:
            prev = before.get(r["player"])
            if prev != r["status"]:
                changes.append({"at_et": stamp, "team": team, "player": r["player"],
                                "from": prev or "not listed", "to": r["status"]})
        now = {r["player"] for r in rows}
        for p, st in before.items():
            if p not in now:
                changes.append({"at_et": stamp, "team": team, "player": p, "from": st, "to": "removed from report"})
    return changes


def keep_lines(games, old_games):
    """ESPN drops the spread and total once a game starts. Keep the last pre-game line (12 Nov: two legs were on a
    team that lost by 34 and there was no saved spread to test a big-underdog rule with)."""
    old = {g.get("event"): g for g in old_games or []}
    for g in games:
        o = old.get(g.get("event"))
        if g.get("spread") is None and o and o.get("spread") is not None:
            for k in ("spread_text", "spread", "total", "odds_source"):
                g[k] = o.get(k)
    return games


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today_et().isoformat())
    a = ap.parse_args()
    d = dt.date.fromisoformat(a.date)
    sb = get_json(f"{ESPN}/scoreboard?dates={d:%Y%m%d}")
    if sb is None:
        print("slate: scoreboard fetch failed")
        return 1
    games = parse_scoreboard(sb)
    names = {g["home_name"] for g in games} | {g["away_name"] for g in games}
    inj_all = parse_injuries(get_json(f"{ESPN}/injuries"))
    injuries = {t: rows for t, rows in inj_all.items() if t in names}
    out_path = path("data", "nba", "slate", f"{d.isoformat()}.json")
    stamp = dt.datetime.now(ET).strftime("%Y-%m-%d %H:%M")
    old = json.load(open(out_path)) if os.path.exists(out_path) else {}
    games = keep_lines(games, old.get("games"))
    changes = old.get("status_changes", [])
    if old.get("injuries") and injuries:
        changes += status_changes(old["injuries"], injuries, stamp)
    write_json(out_path, {
        "date": d.isoformat(), "updated_et": stamp, "source": "ESPN public scoreboard and injuries feeds",
        "injuries_fetched": bool(inj_all), "games": games, "injuries": injuries, "status_changes": changes,
    })
    print(f"slate {d}: {len(games)} games, injury lists for {len(injuries)} teams, {len(changes)} status changes logged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
