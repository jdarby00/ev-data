# Test bench report

46240 graded prop sides (both sides of every prop): 29816 NBA, 16424 NFL; 2026-09-13 to 2026-11-20. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.0% | 50.3% | +2.7% (+0.5% to +4.9%) | +3.1% / +2.5% | +0.8% (n=1549) | 1876 | 140 |
| NBA combo unders PR/RA/PRA | edge (both halves agree) | 52.3% | 50.3% | +2.0% (+0.2% to +3.8%) | +1.9% / +2.1% | -0.5% (n=4484) | 5474 | 140 |
| NBA assists unders | no edge | 52.1% | 50.8% | +1.3% (-0.6% to +3.2%) | +4.1% / -0.5% | -4.3% (n=1182) | 1505 | 140 |
| NBA all unders | no edge | 52.0% | 50.7% | +1.3% (-0.0% to +2.6%) | +1.6% / +1.2% | -2.1% (n=12122) | 14908 | 140 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.8% | 50.2% | +2.6% (-0.6% to +6.1%) | +5.7% / +0.9% | -3.1% (n=343) | 2433 | 114 |
| NFL receiving-yards overs | no edge | 51.6% | 50.0% | +1.6% (-1.1% to +4.3%) | +2.5% / +1.2% | +1.0% (n=372) | 2399 | 114 |
| Favourites 65%+ (both leagues) | no edge | 66.5% | 67.6% | -1.1% (-5.0% to +3.0%) | -1.6% / -0.3% | -3.1% (n=66) | 319 | 141 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 32 | 25.0% | 23.5% |
| 30%–40% | 1347 | 37.3% | 37.0% |
| 40%–45% | 3159 | 41.4% | 42.9% |
| 45%–50% | 15836 | 47.5% | 48.4% |
| 50%–55% | 21320 | 51.8% | 51.2% |
| 55%–60% | 3163 | 58.6% | 57.1% |
| 60%–70% | 1351 | 62.5% | 62.9% |
| 70%–100% | 32 | 75.0% | 76.5% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 621 | 8 | 603 | 48.6% | 50.3% | -9.5% |
| r15_combo_under | 1352 | 8 | 1315 | 51.3% | 50.2% | -3.5% |
| r15_pra_under | 665 | 8 | 648 | 50.9% | 50.2% | -3.7% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
