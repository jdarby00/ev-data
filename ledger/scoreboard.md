# Scoreboard

Built Sat 07 Nov 2026, 2:37 PM ET by `pipeline/grade.py` from `ledger/bets.jsonl`. Derived file: don't edit it; it's rebuilt every pipeline run.

## Jake's real money

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| jake | 3 | 0–3–0–0 | $-20.00 | -100.0% | $-20.00 | $20.00 | – | 0 |

## Paper contestants at real prices (start $500, logged stake)

CLV is the expected value of the bet price against the de-vigged closing price (all books quoting both sides). It needs a collector snapshot taken after the bet and before the start. Beat close = the bet price is better than the same book's closing price.

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| always_under | 99 | 53–40–0–6 | $+38.82 | +8.3% | $538.82 | $28.18 | 43, -5.6%, 45% | 0 |
| card | 3 | 3–0–0–0 | $+13.90 | +92.7% | $513.90 | $0.00 | – | 0 |
| screener | 4 | 3–1–0–0 | $+13.82 | +69.1% | $513.82 | $5.00 | – | 0 |
| boosted_50 | 2 | 2–0–0–0 | $+9.93 | +99.3% | $509.93 | $0.00 | 1, -6.1%, 0% | 0 |
| boosted_20 | 2 | 2–0–0–0 | $+7.94 | +79.4% | $507.94 | $0.00 | 1, -6.1%, 0% | 0 |
| boost_leans | 1 | 1–0–0–0 | $+4.41 | +88.2% | $504.41 | $0.00 | 1, -6.1%, 0% | 0 |
| screener_wide | 6 | 3–3–0–0 | $+3.82 | +12.7% | $503.82 | $10.00 | – | 2 |
| boost_parlay_50 | 1 | 0–1–0–0 | $-5.00 | -100.0% | $495.00 | $5.00 | – | 0 |
| b_selective | 7 | 3–4–0–0 | $-9.85 | -28.1% | $490.15 | $10.00 | 1, -10.2%, – | 0 |
| blend_selective | 7 | 3–4–0–0 | $-9.85 | -28.1% | $490.15 | $20.00 | 1, -10.2%, – | 0 |
| leans | 4 | 1–3–0–0 | $-10.90 | -54.5% | $489.10 | $15.00 | 2, -3.1%, – | 0 |
| a_selective | 6 | 2–4–0–0 | $-13.06 | -43.5% | $486.94 | $16.00 | 1, -10.2%, – | 0 |
| b_every | 34 | 17–17–0–0 | $-13.50 | -7.9% | $486.50 | $34.26 | 13, -4.5%, 80% | 0 |
| lower_bar | 14 | 6–8–0–0 | $-16.70 | -23.9% | $483.30 | $25.65 | 4, -3.9%, 0% | 0 |
| chalk | 32 | 13–17–0–2 | $-44.12 | -29.4% | $455.88 | $53.43 | 10, -6.7%, 60% | 0 |
| always_over | 98 | 41–54–0–3 | $-64.69 | -13.6% | $435.31 | $103.27 | 43, -4.6%, 51% | 0 |
| blend_every | 87 | 37–48–0–2 | $-101.40 | -23.9% | $398.60 | $107.65 | 43, -5.7%, 49% | 0 |
| a_every | 97 | 39–53–0–5 | $-110.79 | -24.1% | $389.21 | $110.79 | 41, -6.0%, 40% | 0 |

## Assumed (web) prices, reported apart

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a_every | 17 | 10–7–0–0 | $+4.78 | +5.6% | $504.78 | $15.00 | – | 0 |
| blend_every | 19 | 11–8–0–0 | $+4.68 | +4.9% | $504.68 | $17.73 | – | 0 |
| b_every | 19 | 11–8–0–0 | $+4.68 | +4.9% | $504.68 | $6.45 | – | 0 |
| chalk | 5 | 0–0–0–5 | $+0.00 | – | $500.00 | $0.00 | – | 0 |
| boosted_50 | 1 | 0–0–0–1 | $+0.00 | – | $500.00 | $0.00 | – | 0 |
| always_over | 28 | 10–9–0–9 | $-1.92 | -2.0% | $498.08 | $32.35 | – | 0 |
| lower_bar | 1 | 0–1–0–0 | $-5.00 | -100.0% | $495.00 | $5.00 | – | 0 |
| leans | 1 | 0–1–0–0 | $-5.00 | -100.0% | $495.00 | $5.00 | – | 0 |
| always_under | 29 | 9–11–0–9 | $-16.88 | -16.9% | $483.12 | $41.84 | – | 0 |

## Calibration (real-price bets with a final win chance)

| Stated chance | Bets | Avg stated | Hit rate |
| --- | --- | --- | --- |
| 50–55% | 76 | 53.4% | 50.0% |
| 55–60% | 186 | 56.9% | 47.3% |
| 60–65% | 72 | 62.3% | 29.2% |
| 65–70% | 12 | 67.5% | 100.0% |

Brier score 0.261 (a coin flip is 0.250).

## Open items

- a6ac9837fa5c: withdrawal after the start ignored
- 2 pending (waiting for box scores or a manual settle).
