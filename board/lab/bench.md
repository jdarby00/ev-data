# Test bench report

28116 graded prop sides (both sides of every prop): 16058 NBA, 12058 NFL; 2026-09-13 to 2026-11-12. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | one half only | 55.5% | 50.2% | +5.3% (+2.1% to +8.3%) | +0.4% / +7.7% | +9.5% (n=660) | 987 | 79 |
| NBA combo unders PR/RA/PRA | one half only | 53.9% | 50.2% | +3.7% (+1.1% to +6.1%) | -0.4% / +5.7% | +5.7% (n=1919) | 2909 | 79 |
| NBA assists unders | edge (both halves agree) | 54.7% | 51.0% | +3.7% (+1.3% to +6.1%) | +2.7% / +4.4% | +2.5% (n=496) | 819 | 79 |
| NBA all unders | one half only | 53.1% | 50.7% | +2.4% (+0.6% to +4.2%) | -0.4% / +4.0% | +2.2% (n=5243) | 8029 | 79 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.3% | 50.2% | +2.1% (-1.6% to +6.2%) | +5.4% / -0.3% | -5.5% (n=175) | 1745 | 100 |
| NFL receiving-yards overs | edge (both halves agree) | 53.0% | 50.0% | +3.0% (+0.1% to +5.9%) | +3.1% / +2.9% | +3.3% (n=194) | 1690 | 100 |
| Favourites 65%+ (both leagues) | no edge | 68.3% | 67.5% | +0.8% (-3.7% to +5.3%) | -1.6% / +2.8% | -1.7% (n=32) | 262 | 107 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 23 | 17.4% | 23.3% |
| 30%–40% | 962 | 36.5% | 36.8% |
| 40%–45% | 1974 | 41.6% | 42.9% |
| 45%–50% | 9130 | 47.7% | 48.4% |
| 50%–55% | 13066 | 51.6% | 51.1% |
| 55%–60% | 1973 | 58.4% | 57.1% |
| 60%–70% | 965 | 63.3% | 63.2% |
| 70%–100% | 23 | 82.6% | 76.7% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 98 | 1 | 0 | 0.0% | 0.0% | +0.0% |
| r15_combo_under | 211 | 1 | 0 | 0.0% | 0.0% | +0.0% |
| r15_pra_under | 105 | 1 | 0 | 0.0% | 0.0% | +0.0% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
