# Test bench report

36938 graded prop sides (both sides of every prop): 21028 NBA, 15910 NFL; 2026-09-13 to 2026-11-15. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 54.7% | 50.3% | +4.4% (+1.7% to +7.1%) | +1.5% / +5.7% | +5.7% (n=979) | 1306 | 102 |
| NBA combo unders PR/RA/PRA | one half only | 53.2% | 50.3% | +3.0% (+0.8% to +5.0%) | +1.0% / +3.8% | +2.5% (n=2848) | 3838 | 102 |
| NBA assists unders | edge (both halves agree) | 53.3% | 50.9% | +2.4% (+0.2% to +4.6%) | +3.6% / +1.8% | -1.5% (n=745) | 1068 | 102 |
| NBA all unders | one half only | 52.5% | 50.7% | +1.8% (+0.2% to +3.3%) | +0.7% / +2.3% | -0.4% (n=7728) | 10514 | 102 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.3% | 50.2% | +2.1% (-1.3% to +5.6%) | +5.4% / +0.6% | -4.6% (n=317) | 2346 | 112 |
| NFL receiving-yards overs | no edge | 51.5% | 50.1% | +1.5% (-1.3% to +4.1%) | +3.1% / +0.8% | +0.7% (n=345) | 2316 | 112 |
| Favourites 65%+ (both leagues) | no edge | 66.6% | 67.6% | -1.1% (-5.3% to +3.1%) | +1.0% / -2.8% | -2.5% (n=44) | 293 | 123 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 29 | 24.1% | 23.3% |
| 30%–40% | 1137 | 37.3% | 36.9% |
| 40%–45% | 2489 | 42.2% | 42.9% |
| 45%–50% | 12144 | 48.1% | 48.4% |
| 50%–55% | 17482 | 51.3% | 51.1% |
| 55%–60% | 2487 | 57.9% | 57.1% |
| 60%–70% | 1141 | 62.6% | 63.1% |
| 70%–100% | 29 | 75.9% | 76.7% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 230 | 3 | 221 | 48.0% | 50.1% | -9.3% |
| r15_combo_under | 508 | 3 | 488 | 51.6% | 50.3% | -2.9% |
| r15_pra_under | 248 | 3 | 239 | 51.0% | 50.2% | -3.5% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
