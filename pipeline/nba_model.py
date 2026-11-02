"""NBA player-stat projection model. Standard library only.

For one player before one game:
  minutes  ~ Normal(mu, sd), truncated to [0, 48], from recent minutes shrunk toward last season
  rate     = stat per minute, recent games (decay-weighted) shrunk toward last season (or a league prior)
  stat | m ~ Negative binomial with mean rate * m and a per-stat dispersion fitted on 2025-26

P(over line) integrates the count distribution over the minutes distribution. Combos (PRA, PR, RA)
use their own rate and dispersion. All tuning constants live in PARAMS and are fitted offline by
tools/fit_model.py; the fitted values and their evidence are recorded in MODEL.md.
"""
import math
from statistics import NormalDist

# Box-score columns behind each stat (combos are sums).
PARTS = {"pts": ["pts"], "reb": ["reb"], "ast": ["ast"], "tpm": ["tpm"],
         "pra": ["pts", "reb", "ast"], "pr": ["pts", "reb"], "ra": ["reb", "ast"]}

PARAMS = {  # fitted 2 Nov 2026 by tools/fit_model.py; evidence in MODEL.md
    "decay": 0.8,           # weight of a game n games back = decay ** n
    "k_min": 0.5,           # last season's minutes count as this many recent games
    "k_rate_min": 100.0,    # last season's per-minute rate counts as this many recent minutes
    "min_sd_floor": 6.0,    # never assume minutes are more certain than this (sd, minutes)
    "min_sd_prior": 6.0,    # sd used when there's little minutes history
    "blowout_spread": 10.0, # at or beyond this spread, regulars lose some minutes
    "blowout_cut": 1.5,     # minutes cut for 28+ minute players in projected blowouts
    # Count stats: negative binomial size r. Scoring stats (NORMAL_STATS): variance = phi * mean, given minutes.
    "dispersion": {"pts": 2.3, "reb": 40, "ast": 30, "tpm": 20, "pra": 2.6, "pr": 2.6, "ra": 40},
    # Per-minute rates of 2025-26 players averaging under 20 minutes; used with no last-season history.
    "league_rate": {"pts": 0.3717, "reb": 0.1906, "ast": 0.0899, "tpm": 0.0467},
}

NORMAL_STATS = {"pts", "pra", "pr"}  # points move in 2s and 3s, so a count model overstates their spread

_ND = NormalDist()
_Q = 15
_QUANTS = [_ND.inv_cdf((i + 0.5) / _Q) for i in range(_Q)]


def nb_pmf_list(mean, r, kmax):
    """pmf[0..kmax] of a negative binomial with the given mean and size r (Poisson as r -> inf)."""
    mean = max(mean, 1e-6)
    p = r / (r + mean)
    pmf = [p ** r]
    for k in range(1, kmax + 1):
        pmf.append(pmf[-1] * (k - 1 + r) / k * (1 - p))
    return pmf


def normal_pmf_list(mean, phi, kmax):
    """Integer pmf from a normal with variance phi * mean, continuity-corrected, mass below 0 put at 0."""
    sd = math.sqrt(max(phi * mean, 0.25))
    cdf = [_ND.cdf((k + 0.5 - mean) / sd) for k in range(kmax + 1)]
    pmf = [cdf[0]] + [cdf[k] - cdf[k - 1] for k in range(1, kmax + 1)]
    return pmf


class Projection:
    def __init__(self, mu_min, sd_min, rates, dispersion):
        self.mu_min, self.sd_min, self.rates, self.disp = mu_min, sd_min, rates, dispersion
        self._cache = {}

    def minutes_points(self):
        return [min(48.0, max(0.0, self.mu_min + self.sd_min * z)) for z in _QUANTS]

    def mean(self, stat):
        return self.rates[stat] * sum(self.minutes_points()) / _Q

    def dist(self, stat):
        """Mixture pmf over counts 0..kmax."""
        if stat in self._cache:
            return self._cache[stat]
        rate, r = self.rates[stat], self.disp[stat]
        kmax = int(max(10, rate * 48 * 2.2 + 10))
        mix = [0.0] * (kmax + 1)
        for m in self.minutes_points():
            pmf = normal_pmf_list(rate * m, r, kmax) if stat in NORMAL_STATS else nb_pmf_list(rate * m, r, kmax)
            for k, v in enumerate(pmf):
                mix[k] += v / _Q
        self._cache[stat] = mix
        return mix

    def p_over(self, stat, line):
        """P(stat > line), with pushes on whole lines removed (as a book voids them)."""
        mix = self.dist(stat)
        if line != int(line):
            k = int(math.floor(line)) + 1
            return max(0.0, min(1.0, 1 - sum(mix[:k])))
        k = int(line)
        push = mix[k] if k < len(mix) else 0.0
        over = 1 - sum(mix[:k + 1])
        return over / (1 - push) if push < 1 else 0.5

    def quantile(self, stat, q):
        acc = 0.0
        for k, v in enumerate(self.dist(stat)):
            acc += v
            if acc >= q:
                return k
        return len(self.dist(stat)) - 1

    def line_at(self, stat, target=0.60):
        """(highest half-point line the over clears with prob >= target,
            lowest half-point line the under clears with prob >= target)."""
        over_line, under_line = None, None
        mix = self.dist(stat)
        cum = 0.0
        for k, v in enumerate(mix):
            cum += v  # P(X <= k)
            if under_line is None and cum >= target:
                under_line = k + 0.5
            if 1 - (cum - v) >= target:  # P(X >= k)
                over_line = k - 0.5
        return over_line, under_line


def project(cur_games, prior, spread=None, params=PARAMS):
    """cur_games: this season's played games before the target, oldest first, each a dict with
    'min' and stat keys pts/reb/ast/tpm. prior: last season totals {'gp','min_total', stat totals} or None.
    Returns a Projection, or None when there's nothing to go on."""
    p = params
    n = len(cur_games)
    if n == 0 and not prior:
        return None
    w = [p["decay"] ** (n - 1 - i) for i in range(n)]
    sw = sum(w)
    # Minutes
    prior_min = prior["min_total"] / prior["gp"] if prior and prior.get("gp") else None
    num = sum(wi * g["min"] for wi, g in zip(w, cur_games))
    if prior_min is not None and sw + p["k_min"] > 0:
        mu = (num + p["k_min"] * prior_min) / (sw + p["k_min"])
    elif sw > 0:
        mu = num / sw
    else:
        return None
    if spread is not None and abs(spread) >= p["blowout_spread"] and mu >= 28:
        mu -= p["blowout_cut"]
    recent = [g["min"] for g in cur_games[-10:]]
    if len(recent) >= 3:
        m = sum(recent) / len(recent)
        sd_obs = math.sqrt(sum((x - m) ** 2 for x in recent) / (len(recent) - 1))
        sd = math.sqrt((len(recent) * sd_obs ** 2 + 3 * p["min_sd_prior"] ** 2) / (len(recent) + 3))
    else:
        sd = p["min_sd_prior"]
    sd = max(sd, p["min_sd_floor"])
    # Rates per minute, base stats then combos as sums
    wmin = sum(wi * g["min"] for wi, g in zip(w, cur_games))
    base = {}
    for s in ("pts", "reb", "ast", "tpm"):
        wstat = sum(wi * g[s] for wi, g in zip(w, cur_games))
        if prior and prior.get("min_total", 0) > 0:
            prior_rate = prior[s] / prior["min_total"]
        else:
            prior_rate = p["league_rate"][s]
        den = wmin + p["k_rate_min"]
        base[s] = (wstat + p["k_rate_min"] * prior_rate) / den if den > 0 else prior_rate
    rates = {k: sum(base[x] for x in parts) for k, parts in PARTS.items()}
    return Projection(max(mu, 0.0), sd, rates, p["dispersion"])
