# Test bench report

31312 graded prop sides (both sides of every prop): 19254 NBA, 12058 NFL; 2026-09-13 to 2026-11-14. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 54.8% | 50.3% | +4.5% (+1.8% to +7.2%) | +1.5% / +6.0% | +6.2% (n=869) | 1196 | 93 |
| NBA combo unders PR/RA/PRA | one half only | 53.5% | 50.3% | +3.3% (+1.0% to +5.4%) | +1.0% / +4.4% | +3.5% (n=2517) | 3507 | 93 |
| NBA assists unders | edge (both halves agree) | 54.1% | 50.9% | +3.2% (+1.0% to +5.4%) | +3.6% / +3.0% | +0.8% (n=654) | 977 | 93 |
| NBA all unders | one half only | 52.7% | 50.7% | +2.0% (+0.3% to +3.6%) | +0.7% / +2.7% | +0.3% (n=6841) | 9627 | 93 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.3% | 50.2% | +2.1% (-1.6% to +6.2%) | +5.4% / -0.3% | -5.5% (n=175) | 1745 | 100 |
| NFL receiving-yards overs | edge (both halves agree) | 53.0% | 50.0% | +3.0% (+0.1% to +5.9%) | +3.1% / +2.9% | +3.3% (n=194) | 1690 | 100 |
| Favourites 65%+ (both leagues) | no edge | 68.3% | 67.6% | +0.7% (-3.8% to +5.2%) | -1.6% / +2.7% | -1.9% (n=35) | 265 | 110 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 24 | 20.8% | 23.2% |
| 30%–40% | 1027 | 36.5% | 36.9% |
| 40%–45% | 2213 | 42.0% | 42.9% |
| 45%–50% | 10422 | 47.7% | 48.4% |
| 50%–55% | 14360 | 51.7% | 51.2% |
| 55%–60% | 2211 | 58.0% | 57.1% |
| 60%–70% | 1031 | 63.3% | 63.1% |
| 70%–100% | 24 | 79.2% | 76.8% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 230 | 3 | 136 | 50.7% | 50.3% | -3.8% |
| r15_combo_under | 508 | 3 | 299 | 53.2% | 50.3% | -0.3% |
| r15_pra_under | 248 | 3 | 150 | 50.7% | 50.3% | -4.8% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
