# Test bench report

52086 graded prop sides (both sides of every prop): 32624 NBA, 19462 NFL; 2026-09-13 to 2026-11-22. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.0% | 50.3% | +2.8% (+0.7% to +4.8%) | +3.9% / +2.1% | +0.8% (n=1723) | 2050 | 153 |
| NBA combo unders PR/RA/PRA | edge (both halves agree) | 52.2% | 50.3% | +2.0% (+0.2% to +3.6%) | +2.9% / +1.4% | -0.8% (n=4998) | 5988 | 153 |
| NBA assists unders | no edge | 52.3% | 50.8% | +1.5% (-0.4% to +3.3%) | +5.0% / -0.9% | -3.8% (n=1321) | 1644 | 153 |
| NBA all unders | one half only | 52.1% | 50.7% | +1.4% (+0.1% to +2.7%) | +2.2% / +0.8% | -2.0% (n=13526) | 16312 | 153 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 53.2% | 50.2% | +3.0% (-0.7% to +6.8%) | +5.0% / +2.0% | -1.7% (n=466) | 2891 | 125 |
| NFL receiving-yards overs | no edge | 51.1% | 50.0% | +1.1% (-1.4% to +3.5%) | +2.2% / +0.6% | -0.7% (n=506) | 2893 | 125 |
| Favourites 65%+ (both leagues) | no edge | 66.3% | 67.6% | -1.3% (-5.3% to +2.4%) | -0.9% / -2.0% | -2.7% (n=76) | 347 | 155 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 36 | 27.8% | 23.4% |
| 30%–40% | 1468 | 37.3% | 37.1% |
| 40%–45% | 3519 | 41.5% | 42.9% |
| 45%–50% | 17766 | 47.7% | 48.4% |
| 50%–55% | 24266 | 51.7% | 51.1% |
| 55%–60% | 3523 | 58.5% | 57.1% |
| 60%–70% | 1472 | 62.6% | 62.9% |
| 70%–100% | 36 | 72.2% | 76.6% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 739 | 10 | 717 | 49.1% | 50.4% | -8.4% |
| r15_combo_under | 1604 | 10 | 1559 | 50.9% | 50.2% | -4.1% |
| r15_pra_under | 792 | 10 | 771 | 51.8% | 50.2% | -2.3% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
