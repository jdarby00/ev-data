# Test bench report

54508 graded prop sides (both sides of every prop): 34790 NBA, 19718 NFL; 2026-09-13 to 2026-11-23. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | edge (both halves agree) | 52.4% | 50.3% | +2.1% (+0.1% to +4.2%) | +3.9% / +1.2% | -0.7% (n=1861) | 2188 | 163 |
| NBA combo unders PR/RA/PRA | no edge | 51.8% | 50.3% | +1.5% (-0.1% to +3.1%) | +2.9% / +0.8% | -1.9% (n=5404) | 6394 | 163 |
| NBA assists unders | no edge | 51.7% | 50.7% | +1.0% (-0.9% to +2.7%) | +5.0% / -1.6% | -4.9% (n=1424) | 1747 | 163 |
| NBA all unders | no edge | 51.7% | 50.7% | +1.1% (-0.2% to +2.2%) | +2.2% / +0.4% | -2.9% (n=14609) | 17395 | 163 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 53.1% | 50.2% | +2.9% (-0.7% to +6.7%) | +5.0% / +1.9% | -2.4% (n=477) | 2934 | 126 |
| NFL receiving-yards overs | no edge | 51.1% | 50.0% | +1.1% (-1.4% to +3.6%) | +2.2% / +0.6% | -1.0% (n=519) | 2935 | 126 |
| Favourites 65%+ (both leagues) | no edge | 66.8% | 67.6% | -0.8% (-4.6% to +3.0%) | -0.7% / -1.0% | -0.5% (n=80) | 352 | 158 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 36 | 27.8% | 23.4% |
| 30%–40% | 1521 | 37.2% | 37.1% |
| 40%–45% | 3716 | 41.3% | 42.9% |
| 45%–50% | 18686 | 47.9% | 48.4% |
| 50%–55% | 25267 | 51.6% | 51.2% |
| 55%–60% | 3720 | 58.7% | 57.1% |
| 60%–70% | 1526 | 62.7% | 62.9% |
| 70%–100% | 36 | 72.2% | 76.6% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 846 | 12 | 805 | 48.1% | 50.4% | -10.2% |
| r15_combo_under | 1832 | 12 | 1763 | 50.7% | 50.2% | -4.6% |
| r15_pra_under | 903 | 12 | 868 | 51.0% | 50.2% | -3.7% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
