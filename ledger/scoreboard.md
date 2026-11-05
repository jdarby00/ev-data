# Scoreboard

Built Wed 04 Nov 2026, 7:22 PM ET by `pipeline/grade.py` from `ledger/bets.jsonl`. Derived file: don't edit it; it's rebuilt every pipeline run.

## Jake's real money

No real bets logged yet.

## Paper contestants at real prices (start $500, logged stake)

CLV is the expected value of the bet price against the de-vigged closing price (all books quoting both sides). It needs a collector snapshot taken after the bet and before the start. Beat close = the bet price is better than the same book's closing price.

| Contestant | Bets | W–L–P–V | Profit | ROI | Bankroll | Max drawdown | CLV (n, avg, beat close) | Pending |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| always_over | 8 | 5–3–0–0 | $+12.21 | +30.5% | $512.21 | $15.00 | – | 0 |
| screener | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 1 |
| screener_wide | 0 | 0–0–0–0 | $+0.00 | – | $500.00 | $0.00 | – | 1 |
| chalk | 3 | 0–3–0–0 | $-15.00 | -100.0% | $485.00 | $15.00 | – | 0 |
| always_under | 10 | 2–5–0–3 | $-16.52 | -47.2% | $483.48 | $20.37 | – | 0 |
| a_every | 11 | 2–6–0–3 | $-21.52 | -53.8% | $478.48 | $30.00 | – | 0 |

## Calibration (real-price bets with a final win chance)

No graded bets with a stated chance yet.

## Open items

- 2 pending (waiting for box scores or a manual settle).
