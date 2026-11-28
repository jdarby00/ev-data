# Test bench report

60916 graded prop sides (both sides of every prop): 40140 NBA, 20776 NFL; 2026-09-13 to 2026-11-27. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | no edge | 52.0% | 50.3% | +1.7% (-0.2% to +3.6%) | +5.3% / -0.6% | -1.8% (n=2235) | 2562 | 186 |
| NBA combo unders PR/RA/PRA | no edge | 51.5% | 50.3% | +1.2% (-0.3% to +2.7%) | +3.7% / -0.4% | -2.6% (n=6423) | 7413 | 186 |
| NBA assists unders | no edge | 51.3% | 50.7% | +0.6% (-1.0% to +2.2%) | +3.7% / -1.5% | -5.5% (n=1700) | 2023 | 186 |
| NBA all unders | no edge | 51.6% | 50.6% | +0.9% (-0.2% to +2.1%) | +2.4% / -0.1% | -3.2% (n=17284) | 20070 | 186 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 53.2% | 50.2% | +3.0% (-0.4% to +6.6%) | +2.1% / +4.2% | -2.1% (n=529) | 3102 | 130 |
| NFL receiving-yards overs | no edge | 50.5% | 50.0% | +0.5% (-1.9% to +2.9%) | +3.0% / -2.3% | -2.8% (n=569) | 3116 | 130 |
| Favourites 65%+ (both leagues) | no edge | 67.5% | 67.7% | -0.2% (-4.0% to +3.6%) | +0.6% / -1.7% | -0.1% (n=95) | 382 | 172 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 46 | 23.9% | 23.6% |
| 30%–40% | 1668 | 36.7% | 37.1% |
| 40%–45% | 4158 | 41.5% | 42.9% |
| 45%–50% | 21132 | 47.8% | 48.4% |
| 50%–55% | 28029 | 51.6% | 51.2% |
| 55%–60% | 4164 | 58.4% | 57.1% |
| 60%–70% | 1673 | 63.2% | 62.9% |
| 70%–100% | 46 | 76.1% | 76.4% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 1080 | 14 | 1053 | 48.7% | 50.4% | -8.8% |
| r15_combo_under | 2346 | 14 | 2290 | 50.4% | 50.2% | -4.9% |
| r15_pra_under | 1153 | 14 | 1126 | 50.3% | 50.3% | -5.2% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
