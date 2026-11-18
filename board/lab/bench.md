# Test bench report

40232 graded prop sides (both sides of every prop): 24062 NBA, 16170 NFL; 2026-09-13 to 2026-11-17. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.6% | 50.3% | +3.3% (+0.7% to +5.9%) | +2.0% / +3.9% | +2.6% (n=1170) | 1497 | 115 |
| NBA combo unders PR/RA/PRA | no edge | 52.2% | 50.3% | +1.9% (-0.2% to +3.9%) | +1.2% / +2.3% | -0.4% (n=3410) | 4400 | 115 |
| NBA assists unders | no edge | 52.7% | 50.8% | +1.9% (-0.3% to +4.1%) | +3.6% / +0.9% | -2.9% (n=887) | 1210 | 115 |
| NBA all unders | no edge | 52.0% | 50.7% | +1.3% (-0.2% to +2.7%) | +1.0% / +1.4% | -1.9% (n=9245) | 12031 | 115 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.7% | 50.2% | +2.5% (-0.8% to +6.0%) | +5.7% / +0.6% | -3.0% (n=333) | 2394 | 113 |
| NFL receiving-yards overs | no edge | 51.9% | 50.0% | +1.9% (-0.9% to +4.5%) | +2.5% / +1.6% | +2.0% (n=359) | 2356 | 113 |
| Favourites 65%+ (both leagues) | no edge | 66.1% | 67.6% | -1.4% (-5.4% to +2.6%) | -0.9% / -2.1% | -5.7% (n=56) | 307 | 130 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 29 | 24.1% | 23.3% |
| 30%–40% | 1223 | 36.9% | 37.0% |
| 40%–45% | 2727 | 42.0% | 42.9% |
| 45%–50% | 13431 | 47.9% | 48.4% |
| 50%–55% | 18838 | 51.5% | 51.1% |
| 55%–60% | 2728 | 58.0% | 57.1% |
| 60%–70% | 1227 | 63.0% | 63.0% |
| 70%–100% | 29 | 75.9% | 76.7% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 362 | 5 | 350 | 48.6% | 50.3% | -8.9% |
| r15_combo_under | 801 | 5 | 775 | 49.3% | 50.2% | -6.9% |
| r15_pra_under | 389 | 5 | 377 | 51.2% | 50.2% | -3.4% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
