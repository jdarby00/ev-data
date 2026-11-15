# Research lab report

Built 2026-11-15T23:28:57Z UTC from 4432 logged code candidates (3288 settled, 1681 with a close, 72 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 2392, ROI -4.7%; CLV n 695 over 66 games, -7.6%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 202, ROI -3.7%; CLV n 279 over 66 games, +2.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 694, ROI -2.6%; CLV n 707 over 59 games, -1.5%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 3288, ROI -4.2%; CLV n 1597 over 59 games, -3.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 84 over 13 games, +3.8%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 948, ROI -4.9%; CLV n 591 over 66 games, -7.4%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -0.2%; CLV n 43 over 29 games, -1.8%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 1444, ROI -4.6%; CLV n 104 over 43 games, -8.9%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI -5.9%; CLV n 43 over 27 games, -3.3%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 391, ROI +0.7%; CLV n 268 over 59 games, -3.3%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 593, ROI -8.1%; CLV n 485 over 59 games, -5.2%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 594, ROI -5.0%; CLV n 236 over 54 games, -2.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -1.4%; CLV n 283 over 56 games, -2.0%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +12.3%; CLV n 102 over 44 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 384, ROI -5.0%; CLV n 127 over 48 games, -3.7%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 200, ROI -13.7%; CLV n 22 over 16 games, -1.9%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 66 over 13 games, +6.0%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1003, ROI -0.5%; CLV n 1020 over 64 games, -3.2%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2252, ROI -5.8%; CLV n 552 over 62 games, -4.7%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 66 over 13 games, +6.0%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 2647, ROI -2.7%; CLV n 930 over 63 games, -4.5%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 641, ROI -10.5%; CLV n 751 over 72 games, -2.0%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 1770, ROI -5.3%; CLV n 274 over 62 games, -8.6%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 447, ROI -4.6%; CLV n 439 over 57 games, -2.2%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 431, ROI -1.8%; CLV n 528 over 72 games, +1.3%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 640, ROI -2.6%; CLV n 440 over 59 games, -6.9%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 1393, ROI -4.1%; CLV n 679 over 65 games, -7.6%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 513, ROI -3.3%; CLV n 510 over 59 games, -1.9%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative ROI (settled 949, ROI -5.5%; CLV n 16 over 13 games, -9.0%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 2384, ROI -4.8%; CLV n 687 over 66 games, -7.7%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 176, ROI -5.1%; CLV n 210 over 64 games, +1.7%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 701, ROI -2.5%; CLV n 714 over 59 games, -1.5%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 27, ROI +10.2%; CLV n 70 over 27 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 559, ROI -8.1%; CLV n 384 over 59 games, -2.7%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 1609, ROI +0.6%; CLV n 613 over 54 games, -4.1%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1120, ROI -9.2%; CLV n 684 over 66 games, -3.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1155, ROI -6.5%; CLV n 718 over 71 games, -3.2%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 2133, ROI -2.9%; CLV n 963 over 59 games, -3.5%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2915, ROI -5.2%; CLV n 1331 over 72 games, -3.8%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 373, ROI +3.8%; CLV n 350 over 35 games, -1.8%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 202, ROI -3.7%; CLV n 209 over 53 games, +1.6%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 694, ROI -2.6%; CLV n 707 over 59 games, -1.5%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2392, ROI -4.7%; CLV n 681 over 59 games, -7.7%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 70 over 13 games, +5.7%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 113, ROI -13.8%; CLV n 123 over 49 games, +2.0%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 536, ROI -0.1%; CLV n 542 over 59 games, -1.7%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 378, ROI -3.4%; CLV n 388 over 63 games, -6.3%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1981, ROI -5.0%; CLV n 264 over 53 games, -10.3%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 66 over 13 games, +6.0%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 391, ROI +0.7%; CLV n 268 over 59 games, -3.3%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 593, ROI -8.1%; CLV n 485 over 59 games, -5.2%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 594, ROI -5.0%; CLV n 236 over 54 games, -2.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -1.4%; CLV n 283 over 56 games, -2.0%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +12.3%; CLV n 102 over 44 games, -5.6%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI -5.9%; CLV n 36 over 22 games, -3.0%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 384, ROI -5.0%; CLV n 127 over 48 games, -3.7%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 200, ROI -13.7%; CLV n 22 over 16 games, -1.9%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 66 over 13 games, +6.0%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 4432 | 3288 (55) | 63% | 63% | -4.2% (-7.8% to -0.6%) | 1681 (72) | -3.4% (-3.7% to -3.0%) | -0.2% (-0.4% to +0.1%) |  |
| sport = nba | 4231 | 3288 (55) | 63% | 63% | -4.2% (-7.8% to -0.6%) | 1597 (59) | -3.8% (-4.0% to -3.4%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 4003 | 2915 (54) | 64% | 64% | -5.2% (-9.4% to -1.4%) | 1331 (72) | -3.8% (-4.2% to -3.3%) | -0.3% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 3459 | 2647 (55) | 66% | 65% | -2.7% (-7.1% to +1.5%) | 930 (63) | -4.5% (-4.9% to -4.0%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 3197 | 2392 (55) | 68% | 68% | -4.7% (-8.8% to -0.9%) | 695 (66) | -7.6% (-8.1% to -7.2%) | -0.6% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 3168 | 2392 (55) | 68% | 68% | -4.7% (-8.8% to -0.9%) | 681 (59) | -7.7% (-8.1% to -7.2%) | -0.5% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 3189 | 2384 (55) | 68% | 68% | -4.8% (-8.9% to -1.1%) | 687 (66) | -7.7% (-8.2% to -7.3%) | -0.5% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 2992 | 2252 (54) | 66% | 66% | -5.8% (-10.8% to -0.9%) | 552 (62) | -4.7% (-5.5% to -3.9%) | -0.4% (-0.9% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 2788 | 2133 (55) | 63% | 63% | -2.9% (-7.6% to +1.4%) | 963 (59) | -3.5% (-3.9% to -3.1%) | +0.1% (-0.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 2676 | 1981 (48) | 69% | 69% | -5.0% (-9.9% to -0.3%) | 264 (53) | -10.3% (-11.1% to -9.6%) | -0.9% (-1.4% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 2381 | 1770 (51) | 70% | 70% | -5.3% (-9.7% to -0.8%) | 274 (62) | -8.6% (-9.1% to -8.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 2205 | 1609 (40) | 69% | 66% | +0.6% (-4.2% to +5.0%) | 613 (54) | -4.1% (-4.8% to -3.2%) | -0.1% (-0.6% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 1908 | 1444 (42) | 72% | 71% | -4.6% (-9.4% to +0.0%) | 104 (43) | -8.9% (-10.0% to -7.9%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 1895 | 1393 (55) | 64% | 64% | -4.1% (-8.7% to +0.7%) | 679 (65) | -7.6% (-8.1% to -7.2%) | -0.5% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1644 | 1155 (53) | 61% | 63% | -6.5% (-11.3% to -1.4%) | 718 (71) | -3.2% (-3.9% to -2.5%) | -0.5% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1518 | 1120 (54) | 58% | 61% | -9.2% (-14.4% to -4.0%) | 684 (66) | -3.1% (-3.5% to -2.7%) | +0.0% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1217 | 1003 (55) | 55% | 55% | -0.5% (-5.8% to +4.6%) | 1020 (64) | -3.2% (-3.6% to -2.9%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1247 | 949 (28) | 74% | 73% | -5.5% (-10.0% to -1.3%) | 16 (13) | -9.0% (-13.0% to -5.6%) | -0.7% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 1289 | 948 (55) | 63% | 62% | -4.9% (-9.2% to -0.6%) | 591 (66) | -7.4% (-7.9% to -7.0%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1179 | 853 (55) | 47% | 49% | -3.0% (-9.9% to +3.6%) | 943 (72) | -0.3% (-0.7% to +0.2%) | +0.1% (-0.2% to +0.4%) | hypothesis (range includes zero) |
| edge = 0-3% | 842 | 701 (55) | 48% | 50% | -2.5% (-10.6% to +5.6%) | 714 (59) | -1.5% (-1.9% to -1.2%) | +0.7% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 835 | 694 (55) | 48% | 50% | -2.6% (-11.0% to +5.5%) | 707 (59) | -1.5% (-1.9% to -1.1%) | +0.8% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 835 | 694 (55) | 48% | 50% | -2.6% (-11.0% to +5.5%) | 707 (59) | -1.5% (-1.9% to -1.1%) | +0.8% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 973 | 641 (55) | 48% | 53% | -10.5% (-16.7% to -4.4%) | 751 (72) | -2.0% (-2.5% to -1.5%) | -0.3% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 838 | 640 (55) | 63% | 61% | -2.6% (-7.3% to +2.5%) | 440 (59) | -6.9% (-7.4% to -6.4%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 777 | 594 (54) | 61% | 62% | -5.0% (-11.6% to +0.6%) | 236 (54) | -2.0% (-2.5% to -1.6%) | +0.4% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 777 | 594 (54) | 61% | 62% | -5.0% (-11.6% to +0.6%) | 236 (54) | -2.0% (-2.5% to -1.6%) | +0.4% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 741 | 593 (55) | 59% | 62% | -8.1% (-13.2% to -3.5%) | 485 (59) | -5.2% (-5.6% to -4.8%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 741 | 593 (55) | 59% | 62% | -8.1% (-13.2% to -3.5%) | 485 (59) | -5.2% (-5.6% to -4.8%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 709 | 559 (52) | 55% | 59% | -8.1% (-13.8% to -2.1%) | 384 (59) | -2.7% (-3.2% to -2.2%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 650 | 536 (55) | 50% | 51% | -0.1% (-8.7% to +7.8%) | 542 (59) | -1.7% (-2.2% to -1.2%) | +0.7% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 625 | 513 (54) | 50% | 53% | -3.3% (-12.2% to +5.5%) | 510 (59) | -1.9% (-2.2% to -1.5%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 614 | 487 (52) | 60% | 59% | -1.4% (-9.2% to +5.9%) | 283 (56) | -2.0% (-2.6% to -1.4%) | +0.6% (+0.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 614 | 487 (52) | 60% | 59% | -1.4% (-9.2% to +5.9%) | 283 (56) | -2.0% (-2.6% to -1.4%) | +0.6% (+0.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 546 | 447 (54) | 49% | 52% | -4.6% (-14.7% to +4.7%) | 439 (57) | -2.2% (-2.6% to -1.8%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 667 | 431 (55) | 45% | 46% | -1.8% (-10.9% to +7.3%) | 528 (72) | +1.3% (+0.8% to +1.8%) | +0.3% (-0.2% to +0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 510 | 391 (54) | 61% | 59% | +0.7% (-5.8% to +7.5%) | 268 (59) | -3.3% (-4.0% to -2.6%) | -0.2% (-0.8% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 510 | 391 (54) | 61% | 59% | +0.7% (-5.8% to +7.5%) | 268 (59) | -3.3% (-4.0% to -2.6%) | -0.2% (-0.8% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 492 | 384 (49) | 63% | 64% | -5.0% (-11.9% to +1.3%) | 127 (48) | -3.7% (-4.5% to -3.0%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 492 | 384 (49) | 63% | 64% | -5.0% (-11.9% to +1.3%) | 127 (48) | -3.7% (-4.5% to -3.0%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 462 | 378 (55) | 63% | 62% | -3.4% (-10.4% to +3.7%) | 388 (63) | -6.3% (-6.7% to -5.9%) | -0.5% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 429 | 373 (35) | 55% | 53% | +3.8% (-3.9% to +11.9%) | 350 (35) | -1.8% (-2.2% to -1.5%) | +0.2% (-0.2% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 432 | 364 (55) | 44% | 46% | -3.1% (-13.0% to +6.6%) | 394 (63) | +0.3% (-0.2% to +0.9%) | +0.5% (-0.1% to +1.1%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 356 | 268 (28) | 70% | 69% | -4.4% (-12.0% to +2.6%) | 7 (5) | -19.4% (5 games) | -3.4% (–) | hypothesis (range includes zero) |
| stat/market = pr | 356 | 268 (28) | 70% | 69% | -4.4% (-12.0% to +2.6%) | 7 (5) | -19.4% (5 games) | -3.4% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 284 | 210 (28) | 70% | 70% | -4.7% (-11.3% to +1.7%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 284 | 210 (28) | 70% | 70% | -4.7% (-11.3% to +1.7%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| lane = value | 400 | 202 (49) | 45% | 48% | -3.7% (-16.4% to +8.6%) | 279 (66) | +2.6% (+1.9% to +3.4%) | -1.7% (-2.2% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 228 | 202 (49) | 45% | 48% | -3.7% (-16.4% to +8.6%) | 209 (53) | +1.6% (+1.0% to +2.1%) | -1.5% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ra | 266 | 200 (35) | 62% | 69% | -13.7% (-23.6% to -4.0%) | 22 (16) | -1.9% (-5.1% to +1.2%) | -1.7% (-3.5% to +0.0%) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 266 | 200 (35) | 62% | 69% | -13.7% (-23.6% to -4.0%) | 22 (16) | -1.9% (-5.1% to +1.2%) | -1.7% (-3.5% to +0.0%) | IN-SAMPLE SIGNAL: negative ROI |
| edge = 3-6% | 256 | 176 (49) | 44% | 48% | -5.1% (-19.1% to +7.4%) | 210 (64) | +1.7% (+1.2% to +2.3%) | -1.2% (-1.6% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 185 | 158 (42) | 43% | 49% | -11.0% (-27.3% to +6.6%) | 165 (46) | -0.8% (-1.4% to +0.0%) | +1.0% (+0.5% to +1.7%) | hypothesis (range includes zero) |
| lane = value, side = over | 131 | 113 (43) | 38% | 46% | -13.8% (-32.8% to +5.4%) | 123 (49) | +2.0% (+1.1% to +2.8%) | -2.0% (-2.8% to -1.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 112 | 100 (43) | 74% | 63% | +12.3% (-3.5% to +26.0%) | 102 (44) | -5.6% (-6.3% to -4.9%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 112 | 100 (43) | 74% | 63% | +12.3% (-3.5% to +26.0%) | 102 (44) | -5.6% (-6.3% to -4.9%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 105 | 89 (37) | 53% | 50% | +9.0% (-11.4% to +27.9%) | 90 (41) | +0.9% (-0.1% to +2.0%) | -1.0% (-1.9% to -0.1%) | hypothesis (range includes zero) |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| tier = Lean | 56 | 43 (29) | 56% | 57% | -0.2% (-19.9% to +21.4%) | 43 (29) | -1.8% (-3.2% to -0.4%) | -0.9% (-2.2% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 45 | 33 (20) | 64% | 66% | -5.9% (-33.7% to +20.8%) | 36 (22) | -3.0% (-4.6% to -1.2%) | +0.4% (-1.1% to +2.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 59 | 33 (20) | 64% | 66% | -5.9% (-33.7% to +20.8%) | 43 (27) | -3.3% (-4.7% to -1.7%) | +0.1% (-1.2% to +1.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 34 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| stat/market = blk | 34 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| edge = 6%+ | 145 | 27 (14) | 48% | 48% | +10.2% (-31.5% to +59.7%) | 70 (27) | +5.3% (+3.5% to +7.5%) | -3.1% (-5.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 30-40% | 37 | 19 (14) | 42% | 38% | +14.0% (-49.4% to +79.3%) | 28 (21) | +4.3% (+3.1% to +5.6%) | +0.2% (-1.6% to +2.2%) | hypothesis |
| lane = likely, side = home | 22 | 17 (11) | 82% | 66% | +20.7% (-11.0% to +46.6%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| side = home | 22 | 17 (11) | 82% | 66% | +20.7% (-11.0% to +46.6%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| lane = likely, side = away | 37 | 16 (9) | 44% | 66% | -34.1% (9 games) | 24 (14) | -3.9% (-5.7% to -1.2%) | -0.4% (-2.2% to +2.3%) | hypothesis |
| side = away | 37 | 16 (9) | 44% | 66% | -34.1% (9 games) | 24 (14) | -3.9% (-5.7% to -1.2%) | -0.4% (-2.2% to +2.3%) | hypothesis |
| chance = 10-20% | 89 | 0 (0) | – | – | – (–) | 29 (11) | +7.0% (+4.0% to +11.4%) | -1.1% (-3.6% to +1.9%) | hypothesis |
| chance = 20-30% | 52 | 0 (0) | – | – | – (–) | 25 (12) | +6.1% (+4.4% to +8.0%) | -1.6% (-2.6% to -0.6%) | hypothesis |
| lane = likely, sport = nfl | 28 | 0 (0) | – | – | – (–) | 14 (7) | -5.6% (7 games) | -0.8% (7 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 164 | 0 (0) | – | – | – (–) | 66 (13) | +6.0% (+4.5% to +8.2%) | -2.1% (-3.8% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 172 | 0 (0) | – | – | – (–) | 70 (13) | +5.7% (+4.2% to +7.7%) | -2.2% (-3.8% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 164 | 0 (0) | – | – | – (–) | 66 (13) | +6.0% (+4.5% to +8.2%) | -2.1% (-3.8% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 200 | 0 (0) | – | – | – (–) | 84 (13) | +3.8% (+2.2% to +5.8%) | -2.0% (-3.4% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 164 | 0 (0) | – | – | – (–) | 66 (13) | +6.0% (+4.5% to +8.2%) | -2.1% (-3.8% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 13 | 0 (0) | – | – | – (–) | 7 (5) | -4.4% (5 games) | -1.3% (5 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 4 (3) | -5.7% (3 games) | -1.5% (3 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 164 | 0 (0) | – | – | – (–) | 66 (13) | +6.0% (+4.5% to +8.2%) | -2.1% (-3.8% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 4 (3) | -5.7% (3 games) | -1.5% (3 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
