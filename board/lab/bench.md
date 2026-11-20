# Test bench report

44148 graded prop sides (both sides of every prop): 27724 NBA, 16424 NFL; 2026-09-13 to 2026-11-19. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.0% | 50.3% | +2.8% (+0.4% to +5.2%) | +2.6% / +2.9% | +1.0% (n=1415) | 1742 | 131 |
| NBA combo unders PR/RA/PRA | edge (both halves agree) | 52.4% | 50.3% | +2.1% (+0.2% to +3.9%) | +1.8% / +2.3% | -0.3% (n=4101) | 5091 | 131 |
| NBA assists unders | no edge | 52.4% | 50.8% | +1.6% (-0.4% to +3.5%) | +3.3% / +0.6% | -3.5% (n=1073) | 1396 | 131 |
| NBA all unders | no edge | 52.0% | 50.7% | +1.3% (-0.1% to +2.7%) | +1.5% / +1.2% | -2.1% (n=11076) | 13862 | 131 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.8% | 50.2% | +2.6% (-0.6% to +6.1%) | +5.7% / +0.9% | -3.1% (n=343) | 2433 | 114 |
| NFL receiving-yards overs | no edge | 51.6% | 50.0% | +1.6% (-1.1% to +4.3%) | +2.5% / +1.2% | +1.0% (n=372) | 2399 | 114 |
| Favourites 65%+ (both leagues) | no edge | 65.9% | 67.5% | -1.6% (-5.8% to +2.5%) | -1.6% / -1.6% | -6.3% (n=61) | 314 | 136 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 30 | 26.7% | 23.5% |
| 30%–40% | 1306 | 37.6% | 37.0% |
| 40%–45% | 3000 | 41.7% | 42.9% |
| 45%–50% | 14993 | 47.7% | 48.4% |
| 50%–55% | 20475 | 51.7% | 51.2% |
| 55%–60% | 3004 | 58.3% | 57.1% |
| 60%–70% | 1310 | 62.3% | 63.0% |
| 70%–100% | 30 | 73.3% | 76.5% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 524 | 7 | 507 | 48.7% | 50.3% | -8.8% |
| r15_combo_under | 1150 | 7 | 1115 | 51.7% | 50.2% | -2.6% |
| r15_pra_under | 563 | 7 | 547 | 50.8% | 50.2% | -4.0% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
