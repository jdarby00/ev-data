# Test bench report

57968 graded prop sides (both sides of every prop): 37446 NBA, 20522 NFL; 2026-09-13 to 2026-11-26. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | no edge | 51.7% | 50.3% | +1.4% (-0.5% to +3.4%) | +5.3% / -1.0% | -2.3% (n=2045) | 2372 | 175 |
| NBA combo unders PR/RA/PRA | no edge | 51.3% | 50.3% | +1.1% (-0.5% to +2.6%) | +3.6% / -0.6% | -2.9% (n=5911) | 6901 | 175 |
| NBA assists unders | no edge | 51.2% | 50.7% | +0.5% (-1.4% to +2.2%) | +4.4% / -2.3% | -6.0% (n=1554) | 1877 | 175 |
| NBA all unders | no edge | 51.4% | 50.7% | +0.8% (-0.5% to +2.0%) | +2.6% / -0.4% | -3.5% (n=15937) | 18723 | 175 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 53.1% | 50.2% | +2.9% (-0.5% to +6.5%) | +1.7% / +4.3% | -2.6% (n=518) | 3063 | 129 |
| NFL receiving-yards overs | no edge | 50.5% | 50.0% | +0.5% (-1.9% to +2.9%) | +3.3% / -2.7% | -2.9% (n=556) | 3072 | 129 |
| Favourites 65%+ (both leagues) | no edge | 67.4% | 67.7% | -0.3% (-4.1% to +3.6%) | +0.6% / -2.1% | -1.3% (n=85) | 365 | 165 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 41 | 24.4% | 23.7% |
| 30%–40% | 1595 | 37.1% | 37.1% |
| 40%–45% | 3952 | 41.2% | 42.9% |
| 45%–50% | 19977 | 47.9% | 48.4% |
| 50%–55% | 26805 | 51.6% | 51.2% |
| 55%–60% | 3957 | 58.8% | 57.1% |
| 60%–70% | 1600 | 62.9% | 62.9% |
| 70%–100% | 41 | 75.6% | 76.3% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 948 | 13 | 922 | 48.0% | 50.4% | -10.2% |
| r15_combo_under | 2076 | 13 | 2023 | 50.3% | 50.2% | -5.3% |
| r15_pra_under | 1022 | 13 | 996 | 50.2% | 50.2% | -5.3% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
