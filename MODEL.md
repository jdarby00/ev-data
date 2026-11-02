# NBA projection model: what it is and how well it does

Fitted and tested 2 Nov 2026. Code: `pipeline/nba_model.py`. Fit and test: `tools/fit_model.py` (local; needs pandas, numpy, scipy). Full numbers: `tools/fit_report.json`.

## How it works

- **Minutes:** recent minutes (each game back weighted 0.8×) shrunk lightly toward last season's average, which counts as half a game. A 1.5-minute cut for 28+ minute players when the spread is 10 or more. The spread of minutes comes from the last 10 games, never under 6 minutes.
- **Rates:** points, rebounds, assists and threes per minute, recent games shrunk toward last season's rate, which counts as 100 minutes. Players with no last season use the rate of 2025-26 players averaging under 20 minutes.
- **Distribution:** given minutes, rebounds, assists, threes and reb+ast follow a negative binomial; points, PRA and PR follow a normal with variance = φ × mean (points move in 2s and 3s, so a count model overstates their spread). φ and the dispersions were fitted on 2025-26 box scores, walk-forward. Chances integrate over the minutes distribution, and pushes on whole lines are removed.

## Test results

**Data.** The prior-strength settings were fitted on 2026-27 games from 27 Oct to 1 Nov (888 player-games). The market test used **2,607 closing NBA props from 20–26 Oct 2026** (Odds Gap consensus of 7–19 books), which the fit never saw.

**The model does not beat the market.**

| | Brier (lower is better) | Log loss |
| --- | --- | --- |
| Market consensus | 0.248 | 0.689 |
| Model alone | 0.259 | 0.715 |
| Best blend, 10% model | 0.248 | 0.689 |

- Choosing the blend weight on alternate days and testing on the rest gave a weight of 0.0–0.2, and never beat the market on the test days.
- It's worse in every market: points, rebounds, assists, threes, PRA, PR and RA.
- It's **overconfident at the extremes**: when it said 26%, the over hit 44%; at 74%, it hit 58%. The lines carry role and rotation knowledge that box scores don't.
- Betting rules built on it (50/50 with the market, 60%+ final, 3% edge at a DraftKings-like price) returned about break-even (296 bets, +0.4%) and lost at 65%+ (86 bets, −12.8%).

**The ranges are honest.** On the 888 fit games, the share of outcomes inside the projected 10–90% band:

| Points | Rebounds | Assists | Threes | PRA | Minutes |
| --- | --- | --- | --- | --- | --- |
| 83% | 89% | 91% | 91% | 82% | 84% |

The target is 80%, so the bands are honest to slightly cautious.

## How to use it

- **Do** use it for minutes floors, realistic ranges, spotting where a line sits far from a player's usual output, and working out what changes when a teammate sits.
- **Don't** treat its chance of an over as a win probability, or as evidence the market is wrong. A big gap between the model and the line is a reason to look for news, not a reason to bet.
- Edges come from information the line hasn't absorbed (late injuries, role changes), price differences between books, and promos.

## Limits

Early season: most players had 0–3 games this season when tested. Closing lines are the sharpest prices of the day; DraftKings' earlier lines may be softer, which this test couldn't measure. Retest monthly as the season fills in.
