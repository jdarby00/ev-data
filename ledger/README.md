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

**If the run can't push** (scheduled runs usually clone anonymously): append the same rows, one JSON object per line, to `claude/ledger_inbox.jsonl` in the Claude project, with `created_at` set to the time they were logged. Any later session that can push imports them with `python3 -I pipeline/ledger.py add ledger_inbox.jsonl`; rows already in the ledger are skipped. Inbox rows lose the git timestamp as proof of when they were logged, so the push route is preferred.

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

## Shadow bets from the screener

`pipeline/screener.py` runs in every pipeline run (and at 2:45 pm ET via the clock, right after the lock prices land). For every DraftKings or FanDuel side it computes a fair chance from the *other* books' no-vig prices at the same line, and logs one paper bet per prop per day:

- `screener`: edge 3%+, fair from 2+ other books.
- `screener_wide`: edge 2%+, fair from 1+ other book.

Only the bigger side is kept when books disagree both ways. Prices outside −300..+300 and props starting within 10 minutes are skipped. The full screen (every non-negative edge) is in `board/nba/<date>-screen.md`. These contestants exist to measure, without Claude and without real money, whether price edges survive to the close and to the result.

## What the grader does

- NBA props and game lines are settled from `data/nba/boxscores_2026_27.csv` once the date is in `_checked_dates.txt`. A player who didn't play, or isn't in the box score, is void (as the books do).
- Parlays: any losing leg loses; void legs drop out and the price is rebuilt from the remaining legs' prices.
- A bet logged after its start is marked late and not scored; a withdrawal after the start is ignored.
- CLV needs a collector snapshot taken after the bet and before the start, in `prices/<date>.json`.

The 2 Nov rows are a backfill from `picks_log.md`, used to check the grader against the hand grading (it matched to the cent). History before 2 Nov stays in the Claude project's `picks_log.md`.
