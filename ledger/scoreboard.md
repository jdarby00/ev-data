# Scoreboard

Built Fri 06 Nov 2026, 9:20 PM ET by `pipeline/grade.py` from `ledger/bets.jsonl`. Derived file: don't edit it; it's rebuilt every pipeline run.

## Jake's real money

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| jake | 2 | 0–2–0–0 | $-10.00 | -100.0% | $-10.00 | $10.00 | – | 1 |

## Paper contestants at real prices (start $500, logged stake)

CLV is the expected value of the bet price against the de-vigged closing price (all books quoting both sides). It needs a collector snapshot taken after the bet and before the start. Beat close = the bet price is better than the same book's closing price.

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| always_under | 75 | 38–31–0–6 | $+14.31 | +4.1% | $514.31 | $26.32 | 41, -5.5%, 43% | 24 |
| screener | 1 | 1–0–0–0 | $+7.90 | +158.0% | $507.90 | $0.00 | – | 3 |
| screener_wide | 1 | 1–0–0–0 | $+7.90 | +158.0% | $507.90 | $0.00 | – | 5 |
| boosted_50 | 1 | 1–0–0–0 | $+5.51 | +110.2% | $505.51 | $0.00 | 1, -6.1%, 0% | 1 |
| boosted_20 | 1 | 1–0–0–0 | $+4.41 | +88.2% | $504.41 | $0.00 | 1, -6.1%, 0% | 1 |
| boost_leans | 1 | 1–0–0–0 | $+4.41 | +88.2% | $504.41 | $0.00 | 1, -6.1%, 0% | 0 |
| b_selective | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 7 |
| a_selective | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 6 |
| blend_selective | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 7 |
| card | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 3 |
| boost_parlay_50 | 1 | 0–1–0–0 | $-5.00 | -100.0% | $495.00 | $5.00 | – | 0 |
| lower_bar | 3 | 1–2–0–0 | $-5.65 | -37.7% | $494.35 | $5.65 | 3, -1.8%, 0% | 11 |
| leans | 3 | 1–2–0–0 | $-5.90 | -39.3% | $494.10 | $10.00 | 1, +4.0%, – | 1 |
| b_every | 11 | 5–6–0–0 | $-8.88 | -16.1% | $491.12 | $16.15 | 11, -4.2%, 78% | 23 |
| always_over | 73 | 31–39–0–3 | $-37.66 | -10.8% | $462.34 | $75.07 | 41, -4.8%, 50% | 25 |
| chalk | 28 | 10–16–0–2 | $-48.43 | -37.3% | $451.57 | $49.02 | 10, -6.7%, 60% | 4 |
| a_every | 73 | 29–39–0–5 | $-83.65 | -24.6% | $416.35 | $91.81 | 39, -6.0%, 38% | 24 |
| blend_every | 64 | 26–36–0–2 | $-87.44 | -28.2% | $412.56 | $89.54 | 41, -5.6%, 47% | 23 |

## Assumed (web) prices, reported apart

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| always_over | 9 | 0–0–0–9 | $+0.00 | – | $500.00 | $0.00 | – | 19 |
| chalk | 5 | 0–0–0–5 | $+0.00 | – | $500.00 | $0.00 | – | 0 |
| always_under | 9 | 0–0–0–9 | $+0.00 | – | $500.00 | $0.00 | – | 20 |
| boosted_50 | 1 | 0–0–0–1 | $+0.00 | – | $500.00 | $0.00 | – | 0 |
| a_every | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 17 |
| blend_every | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 19 |
| b_every | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 19 |
| lower_bar | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 1 |
| leans | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 1 |

## Calibration (real-price bets with a final win chance)

| Stated chance | Bets | Avg stated | Hit rate |
| --- | --- | --- | --- |
| 50–55% | 31 | 52.9% | 38.7% |
| 55–60% | 159 | 56.7% | 47.8% |
| 60–65% | 21 | 61.7% | 19.0% |

Brier score 0.261 (a coin flip is 0.250).

## Open items

- a6ac9837fa5c: box scores for this date not in yet
- 265 pending (waiting for box scores or a manual settle).
