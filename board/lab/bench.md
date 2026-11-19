# Test bench report

42958 graded prop sides (both sides of every prop): 26788 NBA, 16170 NFL; 2026-09-13 to 2026-11-18. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.0% | 50.3% | +2.7% (+0.2% to +5.2%) | +2.6% / +2.8% | +0.9% (n=1359) | 1686 | 127 |
| NBA combo unders PR/RA/PRA | edge (both halves agree) | 52.3% | 50.3% | +2.1% (+0.1% to +3.9%) | +1.8% / +2.2% | -0.3% (n=3929) | 4919 | 127 |
| NBA assists unders | no edge | 52.6% | 50.7% | +1.9% (-0.1% to +3.9%) | +3.3% / +0.9% | -2.9% (n=1027) | 1350 | 127 |
| NBA all unders | no edge | 52.0% | 50.7% | +1.3% (-0.2% to +2.7%) | +1.5% / +1.2% | -2.0% (n=10608) | 13394 | 127 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.7% | 50.2% | +2.5% (-0.8% to +6.0%) | +5.7% / +0.6% | -3.0% (n=333) | 2394 | 113 |
| NFL receiving-yards overs | no edge | 51.9% | 50.0% | +1.9% (-0.9% to +4.5%) | +2.5% / +1.6% | +2.0% (n=359) | 2356 | 113 |
| Favourites 65%+ (both leagues) | no edge | 66.1% | 67.5% | -1.4% (-5.6% to +2.7%) | -0.9% / -2.0% | -5.6% (n=59) | 310 | 133 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 29 | 24.1% | 23.3% |
| 30%–40% | 1278 | 37.4% | 37.0% |
| 40%–45% | 2920 | 41.9% | 42.9% |
| 45%–50% | 14543 | 47.8% | 48.4% |
| 50%–55% | 19955 | 51.6% | 51.1% |
| 55%–60% | 2922 | 58.1% | 57.1% |
| 60%–70% | 1282 | 62.5% | 63.0% |
| 70%–100% | 29 | 75.9% | 76.7% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 481 | 6 | 465 | 49.0% | 50.2% | -7.8% |
| r15_combo_under | 1060 | 6 | 1027 | 51.8% | 50.2% | -2.4% |
| r15_pra_under | 520 | 6 | 505 | 50.9% | 50.2% | -3.8% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
