# Test bench report

39078 graded prop sides (both sides of every prop): 22908 NBA, 16170 NFL; 2026-09-13 to 2026-11-16. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 53.7% | 50.3% | +3.4% (+0.6% to +6.2%) | +2.0% / +4.1% | +2.9% (n=1097) | 1424 | 110 |
| NBA combo unders PR/RA/PRA | no edge | 52.3% | 50.3% | +2.0% (-0.2% to +4.1%) | +1.2% / +2.5% | -0.0% (n=3197) | 4187 | 110 |
| NBA assists unders | edge (both halves agree) | 53.2% | 50.8% | +2.4% (+0.2% to +4.6%) | +3.6% / +1.6% | -1.6% (n=832) | 1155 | 110 |
| NBA all unders | no edge | 52.0% | 50.7% | +1.3% (-0.3% to +2.8%) | +1.0% / +1.5% | -1.7% (n=8668) | 11454 | 110 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.7% | 50.2% | +2.5% (-0.8% to +6.0%) | +5.7% / +0.6% | -3.0% (n=333) | 2394 | 113 |
| NFL receiving-yards overs | no edge | 51.9% | 50.0% | +1.9% (-0.9% to +4.5%) | +2.5% / +1.6% | +2.0% (n=359) | 2356 | 113 |
| Favourites 65%+ (both leagues) | no edge | 66.2% | 67.6% | -1.4% (-5.6% to +2.8%) | +1.0% / -3.3% | -4.8% (n=51) | 302 | 128 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 29 | 24.1% | 23.3% |
| 30%–40% | 1190 | 37.3% | 36.9% |
| 40%–45% | 2639 | 42.0% | 42.9% |
| 45%–50% | 12975 | 47.9% | 48.4% |
| 50%–55% | 18382 | 51.5% | 51.1% |
| 55%–60% | 2640 | 58.0% | 57.1% |
| 60%–70% | 1194 | 62.6% | 63.0% |
| 70%–100% | 29 | 75.9% | 76.7% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 362 | 5 | 300 | 50.0% | 50.3% | -6.0% |
| r15_combo_under | 801 | 5 | 664 | 49.8% | 50.2% | -6.0% |
| r15_pra_under | 389 | 5 | 325 | 51.4% | 50.2% | -2.9% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
