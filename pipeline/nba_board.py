"""Daily NBA board: player baselines for every team on today's slate.

Reads the season box scores, last season's box scores and today's slate, then writes
  board/nba/<date>.json  (full detail, for code)
  board/nba/<date>.md    (compact, for Claude and Jake)

Per player: games, starts, minutes (season, last 5, spread over last 10), points,
rebounds, assists and threes (season and last 5), last season's averages, games
missed recently, and tonight's injury status. Per team: rest, back-to-back, who is
out and how many minutes that frees, and simple with/without splits for absent players.

This is step 2 of the redesign (baselines). Step 3 adds projections and probabilities.

Usage: python3 -I pipeline/nba_board.py [--date YYYY-MM-DD]
"""
import argparse
import datetime as dt
import json
import os
import statistics as stats
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import num, path, read_csv, today_et, write_json  # noqa: E402
import nba_model  # noqa: E402

PROJ_STATS = ["pts", "reb", "ast", "tpm", "pra"]
MODEL_NOTE = ("Projections are minutes x per-minute rates with fitted spreads. Ranges are honest (83-91% of outcomes "
              "landed inside the 10-90% band in testing), but the centre does not beat the betting market: on 2,607 "
              "closing props (20-26 Oct 2026) the model's Brier score was 0.259 vs the market's 0.248. Use it for "
              "minutes, ranges and where to look, never as a win chance on its own. See MODEL.md.")


def projection_summary(rows, prior_rows, spread):
    games = [{"min": num(r["minutes"]), "pts": num(r.get("points")), "reb": num(r.get("rebounds")),
              "ast": num(r.get("assists")), "tpm": num(r.get(STATS["tpm"]))} for r in rows]
    prior = None
    if prior_rows:
        prior = {"gp": len(prior_rows), "min_total": sum(num(r["minutes"]) for r in prior_rows)}
        for k, c in STATS.items():
            prior[k] = sum(num(r.get(c)) for r in prior_rows)
    pr = nba_model.project(games, prior, spread=spread)
    if pr is None:
        return None
    out = {"min": round(pr.mu_min, 1), "min_sd": round(pr.sd_min, 1),
           "min_p10": round(max(0.0, pr.mu_min - 1.2816 * pr.sd_min), 1), "stats": {}}
    for s in PROJ_STATS:
        p10, p50, p90 = pr.quantile(s, 0.1), pr.quantile(s, 0.5), pr.quantile(s, 0.9)
        ladder = {}
        for k in range(max(0, p10 - 1), p90 + 2):
            ladder[f"{k + 0.5:g}"] = round(pr.p_over(s, k + 0.5), 3)
        out["stats"][s] = {"mean": round(pr.mean(s), 1), "p10": p10, "p50": p50, "p90": p90, "p_over": ladder}
    return out

STATS = {"pts": "points", "reb": "rebounds", "ast": "assists",
         "tpm": "threePointFieldGoalsMade-threePointFieldGoalsAttempted"}
OUT_WORDS = ("out",)
RISK_WORDS = ("doubtful", "questionable", "day-to-day", "game-time", "probable")


def mean(xs):
    return round(sum(xs) / len(xs), 1) if xs else None


def sd(xs):
    return round(stats.pstdev(xs), 1) if len(xs) >= 2 else None


def player_lines(rows):
    """rows: one player's played games, oldest first."""
    mins = [num(r["minutes"]) for r in rows]
    out = {"gp": len(rows), "starts_l5": sum(int(r.get("starter") or 0) for r in rows[-5:]),
           "min": mean(mins), "min_l5": mean(mins[-5:]), "min_sd_l10": sd(mins[-10:]),
           "min_log_l5": [int(m) for m in mins[-5:]]}
    for k, col in STATS.items():
        vals = [num(r.get(col)) for r in rows]
        out[k] = mean(vals)
        out[k + "_l5"] = mean(vals[-5:])
        out[k + "_log_l5"] = [int(v) for v in vals[-5:]]
    return out


def build(date_iso, box, prior, slate):
    by_team_games = defaultdict(list)  # team -> sorted unique (date, event)
    played = defaultdict(list)          # espn_id -> played rows
    listed = defaultdict(dict)          # espn_id -> {event: row} including DNP
    last_team = {}
    for r in box:
        if r["date"] >= date_iso:
            continue
        by_team_games[r["team"]].append((r["date"], r["event"]))
        listed[r["espn_id"]][r["event"]] = r
        last_team[r["espn_id"]] = (r["date"], r["team"], r["player"])
        if not int(r.get("dnp") or 0) and num(r.get("minutes")) > 0:
            played[r["espn_id"]].append(r)
    for t in by_team_games:
        by_team_games[t] = sorted(set(by_team_games[t]))
    prior_by_id, prior_by_name = defaultdict(list), defaultdict(list)
    for r in prior:
        prior_by_id[r["espn_id"]].append(r)
        prior_by_name[r["player"]].append(r)

    status = {}
    for team_rows in slate.get("injuries", {}).values():
        for r in team_rows:
            status[r["player"]] = r

    teams_out = {}
    for g in slate.get("games", []):
        for side, opp in (("away", "home"), ("home", "away")):
            team = g[side]
            games = by_team_games.get(team, [])
            last_date = games[-1][0] if games else None
            rest = (dt.date.fromisoformat(date_iso) - dt.date.fromisoformat(last_date)).days - 1 if last_date else None
            roster = [pid for pid, (d, t, n) in last_team.items() if t == team]
            last5 = [e for _, e in games[-5:]]
            players = []
            for pid in roster:
                name = last_team[pid][2]
                rows = sorted(played.get(pid, []), key=lambda r: r["date"])
                line = player_lines(rows) if rows else {"gp": 0}
                missed = [e for e in last5 if e not in listed[pid] or int(listed[pid][e].get("dnp") or 0)]
                dnp_reasons = [listed[pid][e]["dnp_reason"] for e in last5
                               if e in listed[pid] and listed[pid][e].get("dnp_reason")]
                pr = prior_by_id.get(pid, [])
                prior_line = None
                if pr:
                    prior_line = {"gp": len(pr), "min": mean([num(r["minutes"]) for r in pr]),
                                  **{k: mean([num(r.get(c)) for r in pr]) for k, c in STATS.items()}}
                st = status.get(name)
                is_out = bool(st) and st["status"].lower().startswith(OUT_WORDS)
                proj = None if is_out else projection_summary(rows, pr, g.get("spread"))
                players.append({"espn_id": pid, "player": name, "status": st["status"] if st else "",
                                "status_detail": st["detail"] if st else "", **line, "proj": proj,
                                "missed_l5": len(missed), "dnp_reasons_l5": dnp_reasons, "last_season": prior_line})
            seen = {p["player"] for p in players}
            for r in slate.get("injuries", {}).get(g.get(side + "_name", ""), []):
                if r["player"] in seen:
                    continue  # injured all season: no box-score rows, but Claude still needs to see him
                pr = prior_by_name.get(r["player"], [])
                prior_line = ({"gp": len(pr), "min": mean([num(x["minutes"]) for x in pr]),
                               **{k: mean([num(x.get(c)) for x in pr]) for k, c in STATS.items()}} if pr else None)
                players.append({"espn_id": "", "player": r["player"], "status": r["status"],
                                "status_detail": r["detail"], "gp": 0, "missed_l5": len(last5),
                                "dnp_reasons_l5": [], "last_season": prior_line})
            players.sort(key=lambda p: -(p.get("min_l5") or 0))
            out_players = [p for p in players if p["status"].lower().startswith(OUT_WORDS) and p.get("gp")]
            out_all_season = [p["player"] for p in players if p["status"].lower().startswith(OUT_WORDS) and not p.get("gp")]
            freed = round(sum(p.get("min") or 0 for p in out_players), 1)
            teams_out[team] = {"team": team, "opp": g[opp], "home": side == "home", "games_played": len(games),
                               "last_game": last_date, "rest_days": rest, "back_to_back": rest == 0,
                               "out": [p["player"] for p in out_players], "freed_minutes": freed,
                               "out_no_games_this_season": out_all_season,
                               "with_without": with_without(team, out_players, players, games, listed, played),
                               "players": players}
    return {"date": date_iso, "slate_updated_et": slate.get("updated_et"), "model_note": MODEL_NOTE,
            "games": slate.get("games", []),
            "status_changes": slate.get("status_changes", []), "teams": teams_out}


def with_without(team, out_players, players, games, listed, played):
    """For each player out tonight: teammates' averages in games he missed vs games he played.
    Only reported with 2+ games on each side; small samples are labelled with n."""
    res = []
    events = [e for _, e in games]
    for op in out_players:
        oid = op["espn_id"]
        without = [e for e in events if e not in listed[oid] or int(listed[oid][e].get("dnp") or 0)]
        with_ = [e for e in events if e not in without]
        if len(without) < 2 or len(with_) < 2:
            continue
        for p in players:
            if p["espn_id"] == oid or p.get("status", "").lower().startswith(OUT_WORDS):
                continue
            rows = {r["event"]: r for r in played.get(p["espn_id"], [])}
            a = [rows[e] for e in with_ if e in rows]
            b = [rows[e] for e in without if e in rows]
            if len(a) < 2 or len(b) < 2:
                continue
            delta = {k: round(mean([num(r.get(c)) for r in b]) - mean([num(r.get(c)) for r in a]), 1)
                     for k, c in [("min", "minutes")] + list(STATS.items())}
            if max(abs(delta["min"]), abs(delta["pts"]), abs(delta["reb"]), abs(delta["ast"])) >= 2:
                res.append({"absent": op["player"], "teammate": p["player"], "n_with": len(a),
                            "n_without": len(b), "delta": delta})
    res.sort(key=lambda x: -abs(x["delta"]["min"]))
    return res[:8]


def fmt(v, d="–"):
    return d if v is None else (f"{v:g}" if isinstance(v, float) else str(v))


def to_markdown(board):
    lines = [f"# NBA board, {board['date']}", "",
             f"Slate updated {board['slate_updated_et']} ET. Baselines from ESPN box scores. "
             "L5 = last 5 games played; Min sd = spread of minutes over the last 10. Status from ESPN's injury feed.", "",
             "Stat cells: last 5 / season → projected median (10–90% range). Minutes: → projected (10% floor). "
             + MODEL_NOTE, ""]
    if board["status_changes"]:
        lines += ["## Status changes today", ""]
        lines += [f"- {c['at_et'][11:]} {c['team']}: {c['player']} {c['from']} → {c['to']}" for c in board["status_changes"][-15:]]
        lines.append("")
    for g in board["games"]:
        a, h = board["teams"].get(g["away"]), board["teams"].get(g["home"])
        lines += [f"## {g['away']} @ {g['home']}, {g['tip_et'][11:]} ET",
                  f"Line: {g['spread_text'] or 'n/a'}, total {fmt(g['total'])} ({g['odds_source'] or 'ESPN'})."]
        for t in (a, h):
            if not t:
                continue
            flags = []
            if t["back_to_back"]:
                flags.append("back-to-back")
            elif t["rest_days"] is not None:
                flags.append(f"{t['rest_days']} rest day{'s' if t['rest_days'] != 1 else ''}")
            outs = ", ".join(t["out"]) or ("none who have played this season" if t["out_no_games_this_season"] else "none listed")
            extra = (f" Out all season so far (already in the lines): {', '.join(t['out_no_games_this_season'])}."
                     if t["out_no_games_this_season"] else "")
            lines.append(f"**{t['team']}** ({', '.join(flags) or 'rest n/a'}). Out: {outs}. "
                         f"Freed minutes: {fmt(t['freed_minutes'])}.{extra}")
            for w in t["with_without"][:4]:
                d = w["delta"]
                lines.append(f"- Without {w['absent']}: {w['teammate']} min {d['min']:+g}, pts {d['pts']:+g}, "
                             f"reb {d['reb']:+g}, ast {d['ast']:+g} (n={w['n_without']} vs {w['n_with']})")
            lines += ["", "| Player | Status | Min L5 (sd) → proj (floor) | Pts | Reb | Ast | 3PM | PRA |",
                      "|---|---|---|---|---|---|---|---|"]
            for p in [p for p in t["players"] if (p.get("min_l5") or 0) >= 12 or p["status"]][:11]:
                if not p.get("gp"):
                    ls = p.get("last_season") or {}
                    note = f"none this season; last season {fmt(ls.get('min'))} min, {fmt(ls.get('pts'))} pts" if ls else "no games"
                    lines.append(f"| {p['player']} | {p['status'] or '–'} | {note} | | | | |")
                    continue
                pj = p.get("proj")
                def cell(k):
                    base = f"{fmt(p.get(k + '_l5'))}/{fmt(p.get(k))}" if k != "pra" else "–"
                    if not pj:
                        return base
                    q = pj["stats"][k]
                    return f"{base} → {q['p50']} ({q['p10']}–{q['p90']})" if k != "pra" else f"{q['p50']} ({q['p10']}–{q['p90']})"
                mins = f"{fmt(p['min_l5'])} ({fmt(p['min_sd_l10'])})"
                if pj:
                    mins += f" → {fmt(pj['min'])} ({fmt(pj['min_p10'])})"
                lines.append(f"| {p['player']} | {p['status'] or '–'} | {mins} | {cell('pts')} | {cell('reb')} | "
                             f"{cell('ast')} | {cell('tpm')} | {cell('pra')} |")
            lines.append("")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today_et().isoformat())
    a = ap.parse_args()
    slate_p = path("data", "nba", "slate", f"{a.date}.json")
    if not os.path.exists(slate_p):
        print("board: no slate file; run nba_slate.py first")
        return 1
    slate = json.load(open(slate_p))
    if not slate.get("games"):
        print("board: no games today")
        return 0
    board = build(a.date, read_csv(path("data", "nba", "boxscores_2026_27.csv")),
                  read_csv(path("data", "nba", "boxscores_2025_26.csv.gz")), slate)
    write_json(path("board", "nba", f"{a.date}.json"), board)
    md = to_markdown(board)
    with open(path("board", "nba", f"{a.date}.md"), "w") as fh:
        fh.write(md)
    with open(path("board", "nba", "latest.md"), "w") as fh:
        fh.write(md)
    print(f"board {a.date}: {len(board['teams'])} teams, markdown {len(md)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
