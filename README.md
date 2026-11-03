# ev-data

Public data pipeline for Jake's betting assistant. GitHub Actions does the counting for free; Claude reads the results and does the research.

No secrets live here. Odds API prices stay in the private `dk-odds` repo.

## What runs

`.github/workflows/nba.yml`, five times a day (ET): 5:20 am, 10:40 am, 2:10 pm, 4:20 pm, 5:40 pm.

1. **Box scores** (5:20 am): yesterday's games from ESPN's public JSON, appended to `data/nba/boxscores_2026_27.csv`. Players who were listed but didn't play are kept (`dnp=1`, with ESPN's reason), so missed games and with/without effects can be measured.
2. **Slate**: today's games, tip times, ESPN-listed spread and total, and injuries, in `data/nba/slate/<date>.json`. Each refresh logs status changes since the last one.
3. **Board**: per-player baselines for every team playing today, in `board/nba/<date>.json` (full) and `board/nba/<date>.md` (compact). `board/nba/latest.md` is always the newest.
4. **Clock** (`.github/workflows/clock.yml`): GitHub's cron runs hours late, so one long job sleeps until each timed job is due and dispatches it on the minute: pipeline refreshes at 2:05 and 4:15 pm, dk-odds' price request at 2:25 pm, and a close snapshot 12 minutes before each cluster of tips. Dispatching dk-odds needs the `DK_ODDS_DISPATCH` secret (a fine-grained token with Actions read/write on dk-odds only). What it did each day is in `clock/<date>.json`.
5. **Grading** (every run): `pipeline/grade.py` settles the bet ledger from the box scores, measures closing-line value from `prices/`, and rebuilds `ledger/scoreboard.md`. See `ledger/README.md`.

## Reading it from a Claude run

- Clone it: `git clone --depth 1 https://github.com/jdarby00/ev-data` (public, no auth). This is the path to use.
- raw.githubusercontent.com is blocked by the Claude cloud proxy (checked 2 Nov).
- Fallback: WebFetch `https://github.com/jdarby00/ev-data/blob/main/board/nba/<date>.md`. It returns a model summary, not the exact text, so ask about one game at a time.

## Files

| Path | What |
| --- | --- |
| `data/nba/boxscores_2026_27.csv` | Current season, one row per player per game |
| `data/nba/boxscores_2025_26.csv.gz` | Last season, for priors |
| `data/nba/slate/<date>.json` | Games, lines, injuries, status changes |
| `board/nba/<date>.json` / `.md` | Player baselines, rest, freed minutes, with/without splits |
| `clock/<date>.json` | What the clock dispatched and when |
| `ledger/bets.jsonl` | Every bet, append only (`pipeline/ledger.py add`) |
| `ledger/scoreboard.md` | Graded results, CLV, drawdowns and calibration per contestant |
| `pipeline/` | The code (standard library only) |
| `tests/` | Offline tests: `python3 -I tests/test_pipeline.py -v` and `python3 -I tests/test_ledger.py -v` |

## Roadmap

Done: board (step 2), projections (step 3), ledger and grading (step 4). Next: a code screener that logs its own candidates to the ledger. See REVIEW_2026-11-03 in the Claude project.
