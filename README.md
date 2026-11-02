# ev-data

Public data pipeline for Jake's betting assistant. GitHub Actions does the counting for free; Claude reads the results and does the research.

No secrets live here. Odds API prices stay in the private `dk-odds` repo.

## What runs

`.github/workflows/nba.yml`, five times a day (ET): 5:20 am, 10:40 am, 2:10 pm, 4:20 pm, 5:40 pm.

1. **Box scores** (5:20 am): yesterday's games from ESPN's public JSON, appended to `data/nba/boxscores_2026_27.csv`. Players who were listed but didn't play are kept (`dnp=1`, with ESPN's reason), so missed games and with/without effects can be measured.
2. **Slate**: today's games, tip times, ESPN-listed spread and total, and injuries, in `data/nba/slate/<date>.json`. Each refresh logs status changes since the last one.
3. **Board**: per-player baselines for every team playing today, in `board/nba/<date>.json` (full) and `board/nba/<date>.md` (compact). `board/nba/latest.md` is always the newest.

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
| `pipeline/` | The code (standard library only) |
| `tests/` | Offline tests: `python3 -I tests/test_pipeline.py -v` |

## Roadmap

Step 3 adds projections and calibrated probabilities to the board; step 4 grades every logged pick nightly. See the review in the Claude project.
