# Test bench report

30318 graded prop sides (both sides of every prop): 18260 NBA, 12058 NFL; 2026-09-13 to 2026-11-13. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Verdict | Won | Fair | Residual (90% range) | Halves | ROI at price | Sides | Games |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | one half only | 55.0% | 50.3% | +4.8% (+2.0% to +7.6%) | +0.4% / +6.6% | +7.2% (n=803) | 1130 | 88 |
| NBA combo unders PR/RA/PRA | one half only | 53.6% | 50.3% | +3.3% (+1.0% to +5.6%) | -0.4% / +4.9% | +3.9% (n=2336) | 3326 | 88 |
| NBA assists unders | edge (both halves agree) | 54.5% | 50.9% | +3.6% (+1.3% to +5.8%) | +2.7% / +4.1% | +2.0% (n=605) | 928 | 88 |
| NBA all unders | one half only | 52.9% | 50.7% | +2.2% (+0.5% to +3.9%) | -0.4% / +3.4% | +1.0% (n=6344) | 9130 | 88 |
| NFL rushing unders (yds, rush+rec, att) | no edge | 52.3% | 50.2% | +2.1% (-1.6% to +6.2%) | +5.4% / -0.3% | -5.5% (n=175) | 1745 | 100 |
| NFL receiving-yards overs | edge (both halves agree) | 53.0% | 50.0% | +3.0% (+0.1% to +5.9%) | +3.1% / +2.9% | +3.3% (n=194) | 1690 | 100 |
| Favourites 65%+ (both leagues) | no edge | 68.3% | 67.6% | +0.7% (-3.8% to +5.2%) | -1.6% / +2.7% | -1.9% (n=35) | 265 | 110 |

## Calibration: do the books' chances come true?

| Fair chance | Sides | Won | Fair |
|---|---|---|---|
| 0%–30% | 24 | 20.8% | 23.2% |
| 30%–40% | 1012 | 36.4% | 36.9% |
| 40%–45% | 2138 | 42.0% | 42.9% |
| 45%–50% | 10016 | 47.7% | 48.4% |
| 50%–55% | 13952 | 51.7% | 51.1% |
| 55%–60% | 2137 | 58.1% | 57.1% |
| 60%–70% | 1015 | 63.4% | 63.1% |
| 70%–100% | 24 | 79.2% | 76.8% |

## R15 forward test (paper, ev-data ledger)

| Contestant | Rows | Nights | Graded | Won | Fair | ROI |
|---|---|---|---|---|---|---|
| r15_ast_under | 98 | 1 | 96 | 51.0% | 50.0% | -2.3% |
| r15_combo_under | 211 | 1 | 207 | 53.1% | 50.2% | -0.4% |
| r15_pra_under | 105 | 1 | 103 | 52.4% | 50.3% | -1.5% |

Pass mark (pre-registered): 15+ nights and 500+ r15_pra_under rows, ROI > 0, day-resampled 5% bound above -2%.
