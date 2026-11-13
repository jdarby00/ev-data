# Test bench report

28116 graded prop sides (both sides of every prop): 16058 NBA, 12058 NFL; 2026-09-13 to 2026-11-12. Built by dk-odds backtest/bench.py.

Residual = how often the side won minus the fair chance the books gave it. The range is a game-clustered 90% range. An idea counts only when the range excludes zero AND each half of the dates (earlier, later) shows at least 1 point in the same direction.

## Ideas under test

| Idea | Sides | Games | Won | Fair | Residual (90% range) | ROI at price | Halves | Verdict |
|---|---|---|---|---|---|---|---|---|
| NBA PRA unders (R15) | 987 | 79 | 55.5% | 50.2% | +5.3% (+2.1% to +8.3%) | +9.5% (n=660) | +0.4% / +7.7% | one half only |
| NBA combo unders PR/RA/PRA | 2909 | 79 | 53.9% | 50.2% | +3.7% (+1.1% to +6.1%) | +5.7% (n=1919) | -0.4% / +5.7% | one half only |
| NBA assists unders | 819 | 79 | 54.7% | 51.0% | +3.7% (+1.3% to +6.1%) | +2.5% (n=496) | +2.7% / +4.4% | edge (both halves agree) |
| NBA all unders | 8029 | 79 | 53.1% | 50.7% | +2.4% (+0.6% to +4.2%) | +2.2% (n=5243) | -0.4% / +4.0% | one half only |
| NFL rushing unders (yds, rush+rec, att) | 1745 | 100 | 52.3% | 50.2% | +2.1% (-1.6% to +6.2%) | -5.5% (n=175) | +5.4% / -0.3% | no edge |
| NFL receiving-yards overs | 1690 | 100 | 53.0% | 50.0% | +3.0% (+0.1% to +5.9%) | +3.3% (n=194) | +3.1% / +2.9% | edge (both halves agree) |
| Favourites 65%+ (both leagues) | 262 | 107 | 68.3% | 67.5% | +0.8% (-3.7% to +5.3%) | -1.7% (n=32) | -1.6% / +2.8% | no edge |

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

No r15 rows in the ledger yet (first night 13 Nov).
