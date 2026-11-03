# Ledger

Every bet, real or paper, from every contestant. Graded by code, never by hand.

| File | Who writes it | What |
| --- | --- | --- |
| `bets.jsonl` | Claude runs, via `pipeline/ledger.py add` | One row per bet. **Append only**: rows are never edited or removed. |
| `amendments.jsonl` | Claude runs, via `ledger.py withdraw` / `settle` | Withdrawals (before the start only) and hand settlements. |
| `results.jsonl` | `pipeline/grade.py` (every pipeline run) | Result, actual stat, profit, closing price and CLV per bet. Derived. |
| `scoreboard.md` | `pipeline/grade.py` | Jake's real money, paper contestants at real prices, assumed prices apart, calibration, open items. Derived. |
| `state/seen.json` | `pipeline/grade.py` | First-seen hash of every bet, so any later edit or removal is flagged on the scoreboard. |

## Logging bets from a run (before the first game starts)

1. Write the card and paper bets to a JSON file (a list of bet objects; the field list is at the top of `pipeline/ledger.py`).
2. `python3 -I pipeline/ledger.py add bets.json`. It checks every row and adds nothing if any row is wrong.
3. Commit `ledger/bets.jsonl` and push to `main` (pull with rebase first).

Example:

```json
[{"date": "2026-11-04", "contestant": "card", "sport": "nba", "game": "NY@BOS", "team": "BOS",
  "player": "Jayson Tatum", "market": "points", "side": "over", "line": 27.5,
  "book": "fanduel", "price": -110, "price_source": "collector", "price_ts": "2026-11-04T21:46:43Z",
  "stake": 5, "p_market": 0.55, "p_ours": 0.62, "p_final": 0.564, "tier": "Straight"}]
```

- `game` uses ESPN abbreviations (NY, GS, SA, NO, UTAH, WSH), as in `data/nba/slate/<date>.json`.
- `price` is the plain price; a profit boost goes in `boost` (0.25 = 25%). Bonus bets: `"promo": "bonus_bet"`; bet resets: `"promo": "reset"`.
- Jake's own bets: `"contestant": "jake", "real": true`, his real stake, `"price_source": "slip"`.
- Web prices are allowed but scored apart (`"price_source": "web"`).

## Other commands

- Withdraw before the start: `python3 -I pipeline/ledger.py withdraw <id> --reason "..."`
- Settle what the grader can't (soccer, NFL, NHL for now): `python3 -I pipeline/ledger.py settle <id> --result win --actual 2 --reason "source, time"`
- Check: `python3 -I pipeline/ledger.py verify`; list: `python3 -I pipeline/ledger.py show --date 2026-11-04`

## What the grader does

- NBA props and game lines are settled from `data/nba/boxscores_2026_27.csv` once the date is in `_checked_dates.txt`. A player who didn't play, or isn't in the box score, is void (as the books do).
- Parlays: any losing leg loses; void legs drop out and the price is rebuilt from the remaining legs' prices.
- A bet logged after its start is marked late and not scored; a withdrawal after the start is ignored.
- CLV needs a collector snapshot taken after the bet and before the start, in `prices/<date>.json`.

The 2 Nov rows are a backfill from `picks_log.md`, used to check the grader against the hand grading (it matched to the cent). History before 2 Nov stays in the Claude project's `picks_log.md`.
