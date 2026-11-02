"""Fit and test the NBA projection model. Local tool (needs pandas, numpy); not run in Actions.

1. Dispersion per stat: 2025-26 season, walk-forward, stat given actual minutes.
2. Recency and prior strength: 2026-27 games from --fit-from on, using 2025-26 as the prior.
3. Market test: Odds Gap closing NBA props before --fit-from (out of sample), vs the books' consensus.

Usage: python3 tools/fit_model.py --props <props.csv.gz> --logs <gamelogs_nba_2026.csv.gz> [--fit-from 2026-10-27]
"""
import argparse
import itertools
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.special import gammaln

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
import nba_model  # noqa: E402

BASE = ["pts", "reb", "ast", "tpm"]


def load_box(p):
    df = pd.read_csv(p, dtype=str)
    if "dnp" in df:
        df = df[df["dnp"] != "1"]
    out = pd.DataFrame({
        "date": df["date"], "pid": df["espn_id"], "player": df["player"], "team": df["team"],
        "min": pd.to_numeric(df["minutes"], errors="coerce"),
        "pts": pd.to_numeric(df["points"], errors="coerce"),
        "reb": pd.to_numeric(df["rebounds"], errors="coerce"),
        "ast": pd.to_numeric(df["assists"], errors="coerce"),
        "tpm": pd.to_numeric(df["threePointFieldGoalsMade-threePointFieldGoalsAttempted"].str.split("-").str[0], errors="coerce"),
    }).dropna()
    out = out[out["min"] > 0]
    return out.sort_values(["pid", "date"]).reset_index(drop=True)


def nb_logpmf(k, mu, r):
    mu = np.maximum(mu, 1e-6)
    return gammaln(k + r) - gammaln(r) - gammaln(k + 1) + r * np.log(r / (r + mu)) + k * np.log(mu / (r + mu))


def fit_dispersion(prev):
    """Per stat: player's season-to-date rate x actual minutes as the mean; ML over a grid of r."""
    rows = []
    for pid, g in prev.groupby("pid"):
        g = g.reset_index(drop=True)
        cm = g["min"].cumsum().shift(1)
        for s in BASE:
            g["c_" + s] = g[s].cumsum().shift(1)
        g = g[g.index >= 8]
        if g.empty:
            continue
        for s, parts in nba_model.PARTS.items():
            rate = sum(g["c_" + x] for x in parts) / cm[g.index]
            rows.append(pd.DataFrame({"stat": s, "mu": rate * g["min"], "k": sum(g[x] for x in parts)}))
    d = pd.concat(rows)
    grid = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 60, 100, 200]
    best = {}
    for s, sub in d.groupby("stat"):
        sub = sub[sub["mu"] > 0]
        if s in nba_model.NORMAL_STATS:  # variance = phi * mean; phi by moments
            best[s] = round(float(np.mean((sub["k"] - sub["mu"]) ** 2 / sub["mu"])), 2)
            continue
        ll = {r: nb_logpmf(sub["k"].values, sub["mu"].values, r).sum() for r in grid}
        best[s] = max(ll, key=ll.get)
    return best


def prior_table(prev):
    t = prev.groupby("pid").agg(gp=("min", "size"), min_total=("min", "sum"),
                                pts=("pts", "sum"), reb=("reb", "sum"), ast=("ast", "sum"), tpm=("tpm", "sum"))
    return {pid: dict(r) for pid, r in t.iterrows()}


def history(cur):
    h = defaultdict(list)
    for r in cur.itertuples():
        h[r.pid].append({"date": r.date, "min": r.min, "pts": r.pts, "reb": r.reb, "ast": r.ast, "tpm": r.tpm})
    return h


def score_params(cur, priors, params, fit_from):
    """Log-likelihood of 2026-27 outcomes from fit_from on: minutes (normal) + stats given actual minutes (NB)."""
    hist = history(cur)
    ll_min, ll_stat, n = 0.0, 0.0, 0
    for pid, games in hist.items():
        for i, g in enumerate(games):
            if g["date"] < fit_from:
                continue
            pr = priors.get(pid)
            proj = nba_model.project(games[:i], pr, params=params)
            if proj is None:
                continue
            ll_min += -0.5 * ((g["min"] - proj.mu_min) / proj.sd_min) ** 2 - math.log(proj.sd_min)
            for s in ("reb", "ast", "tpm"):
                ll_stat += float(nb_logpmf(np.array([g[s]]), np.array([proj.rates[s] * g["min"]]), params["dispersion"][s])[0])
            mu = max(proj.rates["pts"] * g["min"], 0.5)
            var = params["dispersion"]["pts"] * mu
            ll_stat += -0.5 * (g["pts"] - mu) ** 2 / var - 0.5 * math.log(var)
            n += 1
    return ll_min, ll_stat, n


def market_test(cur, priors, params, props_path, logs_path, before):
    props = pd.read_csv(props_path, dtype=str)
    props = props[props["player_id"].str.startswith("nba:") & (props["anchor"] == "close")]
    mk = {"player_points": "pts", "player_rebounds": "reb", "player_assists": "ast", "player_threes": "tpm",
          "player_points_rebounds_assists": "pra", "player_points_rebounds": "pr", "player_rebounds_assists": "ra"}
    props = props[props["market"].isin(mk)]
    logs = pd.read_csv(logs_path, dtype=str)
    logs = logs[logs["game_date"] < before]
    res_col = {"pts": "player_points", "reb": "player_rebounds", "ast": "player_assists", "tpm": "player_threes",
               "pra": "player_points_rebounds_assists", "pr": "player_points_rebounds", "ra": "player_rebounds_assists"}
    lg = {(r.player_id, r.game_date): r for r in logs.itertuples()}
    hist = history(cur)
    out = []
    for r in props.itertuples():
        g = lg.get((r.player_id, r.game_date))
        if g is None or r.game_date >= before:
            continue
        stat, line = mk[r.market], float(r.line)
        pid = str(g.espn_player_id).split(".")[0]
        games = [x for x in hist.get(pid, []) if x["date"] < r.game_date]
        sp = pd.to_numeric(g.close_spread, errors="coerce")
        proj = nba_model.project(games, priors.get(pid), spread=None if pd.isna(sp) else sp, params=params)
        if proj is None:
            continue
        actual = pd.to_numeric(getattr(g, res_col[stat]), errors="coerce")
        if pd.isna(actual) or actual == line:
            continue
        out.append({"date": r.game_date, "stat": stat, "line": line, "p_model": proj.p_over(stat, line),
                    "p_mkt": float(r.consensus_fair) / 100, "over": int(actual > line), "n_prior": len(games)})
    return pd.DataFrame(out)


def evaluate(df):
    rep = {"n": len(df)}
    y = df["over"].values
    brier = lambda p: float(np.mean((p - y) ** 2))
    logl = lambda p: float(-np.mean(y * np.log(np.clip(p, 1e-4, 1)) + (1 - y) * np.log(np.clip(1 - p, 1e-4, 1))))
    rep["brier_market"], rep["brier_model"] = brier(df["p_mkt"].values), brier(df["p_model"].values)
    rep["logloss_market"], rep["logloss_model"] = logl(df["p_mkt"].values), logl(df["p_model"].values)
    blends = {}
    for w in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        p = w * df["p_model"].values + (1 - w) * df["p_mkt"].values
        blends[w] = {"brier": round(brier(p), 5), "logloss": round(logl(p), 5)}
    rep["blends"] = blends
    # Calibration of the model alone, by decile of predicted over chance
    df = df.copy()
    df["bin"] = pd.cut(df["p_model"], [0, .2, .3, .4, .45, .5, .55, .6, .7, .8, 1])
    rep["calibration"] = {str(k): {"n": int(len(v)), "pred": round(float(v["p_model"].mean()), 3),
                                   "actual": round(float(v["over"].mean()), 3)} for k, v in df.groupby("bin", observed=True)}
    # Selection: final = 50/50, either side, DK-like price = fair side + 3.5 points of margin
    sel = {}
    for bar in [0.55, 0.60, 0.65]:
        for w in [0.3, 0.5]:
            bets, profit = 0, 0.0
            for r in df.itertuples():
                for side_p_model, side_mkt, win in ((r.p_model, r.p_mkt, r.over), (1 - r.p_model, 1 - r.p_mkt, 1 - r.over)):
                    final = w * side_p_model + (1 - w) * side_mkt
                    price = 1 / min(0.97, side_mkt + 0.035)
                    edge = final * (price - 1) - (1 - final)
                    if final >= bar and edge >= 0.03:
                        bets += 1
                        profit += (price - 1) if win else -1
            sel[f"w{w}_bar{bar}"] = {"bets": bets, "roi": round(profit / bets, 3) if bets else None}
    rep["selection"] = sel
    rep["by_stat"] = {s: {"n": int(len(v)), "brier_model": round(brier_sub(v, "p_model"), 4),
                          "brier_market": round(brier_sub(v, "p_mkt"), 4)} for s, v in df.groupby("stat")}
    return rep


def brier_sub(v, col):
    return float(np.mean((v[col].values - v["over"].values) ** 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--props", required=True)
    ap.add_argument("--logs", required=True)
    ap.add_argument("--fit-from", default="2026-10-27")
    ap.add_argument("--out", default=os.path.join(ROOT, "tools", "fit_report.json"))
    a = ap.parse_args()
    prev = load_box(os.path.join(ROOT, "data", "nba", "boxscores_2025_26.csv.gz"))
    cur = load_box(os.path.join(ROOT, "data", "nba", "boxscores_2026_27.csv"))
    priors = prior_table(prev)
    params = json.loads(json.dumps(nba_model.PARAMS))
    params["dispersion"] = fit_dispersion(prev)
    print("dispersion", params["dispersion"])
    # league prior rates for players with no last-season data: low-minute players in 2025-26
    lowmin = prev.groupby("pid").filter(lambda g: g["min"].mean() < 20)
    params["league_rate"] = {s: round(float(lowmin[s].sum() / lowmin["min"].sum()), 4) for s in BASE}
    print("league_rate", params["league_rate"])
    best, results = None, []
    for decay, k_min, k_rate, sdf in itertools.product([0.7, 0.8, 0.9], [0.5, 1, 3], [25, 50, 100, 250], [4, 6, 8]):
        params.update(decay=decay, k_min=k_min, k_rate_min=k_rate, min_sd_floor=sdf, min_sd_prior=max(sdf, 5.5))
        llm, lls, n = score_params(cur, priors, params, a.fit_from)
        results.append((llm + lls, llm, lls, decay, k_min, k_rate, sdf, n))
    results.sort(key=lambda r: r[0], reverse=True)
    _, llm, lls, decay, k_min, k_rate, sdf, n = results[0]
    params.update(decay=decay, k_min=k_min, k_rate_min=k_rate, min_sd_floor=sdf, min_sd_prior=max(sdf, 5.5))
    print(f"best: decay {decay}, k_min {k_min}, k_rate_min {k_rate} (fit games n={n})")
    df = market_test(cur, priors, params, a.props, a.logs, a.fit_from)
    rep = evaluate(df)
    rep["params"] = params
    rep["fit_grid_top5"] = [r[3:] for r in results[:5]]
    json.dump(rep, open(a.out, "w"), indent=1, default=str)
    print(json.dumps({k: rep[k] for k in ("n", "brier_market", "brier_model", "logloss_market", "logloss_model", "blends", "selection")}, indent=1, default=str))
    print(json.dumps(rep["calibration"], indent=1))
    print(json.dumps(rep["by_stat"], indent=1))


if __name__ == "__main__":
    main()
