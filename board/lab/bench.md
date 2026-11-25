# Test bench report

55164 graded prop sides (both sides of every prop): 35446 NBA, 19718 NFL; 2026-09-13 to 2026-11-24. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | no edge | 52.0% | 50.3% | +1.7% (-0.3% to +3.7%) | +5.3% / -0.7% | -1.6% (n=1905) | 2232 | 166 |
| NBA combo unders PR/RA/PRA | no edge | 51.6% | 50.3% | +1.3% (-0.4% to +2.9%) | +3.6% / -0.4% | -2.4% (n=5529) | 6519 | 166 |
| NBA assists unders | no edge | 51.5% | 50.7% | +0.7% (-1.1% to +2.5%) | +4.4% / -2.1% | -5.4% (n=1453) | 1776 | 166 |
| NBA all unders | no edge | 51.5% | 50.7% | +0.9% (-0.3% to +2.1%) | +2.6% / -0.3% | -3.3% (n=14937) | 17723 | 166 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 53.1% | 50.2% | +2.9% (-0.7% to +6.7%) | +5.0% / +1.9% | -2.4% (n=477) | 2934 | 126 |
| NFL receiving-yards overs | no edge | 51.1% | 50.0% | +1.1% (-1.4% to +3.6%) | +2.2% / +0.6% | -1.0% (n=519) | 2935 | 126 |
| Favourites 65%+ (both leagues) | no edge | 66.9% | 67.6% | -0.6% (-4.4% to +3.1%) | -0.7% / -0.5% | +0.5% (n=82) | 354 | 160 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 36 | 27.8% | 23.4% |
| 30%–40% | 1539 | 37.2% | 37.1% |
| 40%–45% | 3759 | 41.3% | 42.9% |
| 45%–50% | 18953 | 47.9% | 48.4% |
| 50%–55% | 25534 | 51.6% | 51.2% |
| 55%–60% | 3763 | 58.7% | 57.1% |
| 60%–70% | 1544 | 62.8% | 62.9% |
| 70%–100% | 36 | 72.2% | 76.6% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 912 | 13 | 832 | 47.8% | 50.3% | -10.5% |
| r15_combo_under | 1912 | 13 | 1826 | 50.5% | 50.2% | -4.9% |
| r15_pra_under | 943 | 13 | 897 | 50.6% | 50.2% | -4.5% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
