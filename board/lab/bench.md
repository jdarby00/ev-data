# Test bench report

47598 graded prop sides (both sides of every prop): 31174 NBA, 16424 NFL; 2026-09-13 to 2026-11-21. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.2% | 50.3% | +2.9% (+0.8% to +5.1%) | +3.1% / +2.8% | +1.1% (n=1639) | 1966 | 146 |
| NBA combo unders PR/RA/PRA | edge (both halves agree) | 52.3% | 50.3% | +2.1% (+0.3% to +3.8%) | +1.9% / +2.1% | -0.5% (n=4736) | 5726 | 146 |
| NBA assists unders | no edge | 52.4% | 50.8% | +1.6% (-0.3% to +3.4%) | +4.1% / +0.1% | -3.6% (n=1256) | 1579 | 146 |
| NBA all unders | edge (both halves agree) | 52.1% | 50.7% | +1.4% (+0.1% to +2.7%) | +1.6% / +1.3% | -2.0% (n=12801) | 15587 | 146 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.8% | 50.2% | +2.6% (-0.6% to +6.1%) | +5.7% / +0.9% | -3.1% (n=343) | 2433 | 114 |
| NFL receiving-yards overs | no edge | 51.6% | 50.0% | +1.6% (-1.1% to +4.3%) | +2.5% / +1.2% | +1.0% (n=372) | 2399 | 114 |
| Favourites 65%+ (both leagues) | no edge | 66.6% | 67.6% | -1.0% (-4.9% to +2.9%) | -0.9% / -1.1% | -2.5% (n=70) | 323 | 143 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 32 | 25.0% | 23.5% |
| 30%–40% | 1370 | 37.3% | 37.1% |
| 40%–45% | 3287 | 41.5% | 42.9% |
| 45%–50% | 16363 | 47.6% | 48.4% |
| 50%–55% | 21849 | 51.8% | 51.2% |
| 55%–60% | 3291 | 58.5% | 57.1% |
| 60%–70% | 1374 | 62.6% | 62.9% |
| 70%–100% | 32 | 75.0% | 76.5% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 689 | 9 | 670 | 49.6% | 50.4% | -7.6% |
| r15_combo_under | 1484 | 9 | 1445 | 51.2% | 50.2% | -3.6% |
| r15_pra_under | 734 | 9 | 716 | 51.4% | 50.2% | -2.9% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
