# Research lab report

Built 2026-11-17T02:34:22Z UTC from 5299 logged code candidates (4024 settled, 2080 with a close, 85 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 2986, ROI -5.2%; CLV n 901 over 79 games, -8.2%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 226, ROI -5.1%; CLV n 327 over 78 games, +2.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 812, ROI -3.4%; CLV n 852 over 70 games, -1.6%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 4024, ROI -4.8%; CLV n 1986 over 70 games, -4.2%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 94 over 15 games, +4.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 1197, ROI -5.2%; CLV n 763 over 79 games, -8.0%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 55, ROI -2.4%; CLV n 61 over 36 games, -2.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 1789, ROI -5.1%; CLV n 138 over 53 games, -9.2%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI +1.2%; CLV n 55 over 35 games, -3.1%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 476, ROI +0.3%; CLV n 329 over 70 games, -3.6%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -9.6%; CLV n 606 over 70 games, -5.5%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 741, ROI -7.0%; CLV n 288 over 65 games, -2.6%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 597, ROI -1.9%; CLV n 361 over 67 games, -2.8%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 102, ROI +10.1%; CLV n 118 over 51 games, -5.6%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI +1.7%; CLV n 33 over 22 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 467, ROI -4.7%; CLV n 157 over 58 games, -3.8%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 253, ROI -11.1%; CLV n 31 over 22 games, -4.9%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1155, ROI -1.4%; CLV n 1217 over 76 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2830, ROI -6.3%; CLV n 734 over 73 games, -5.4%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 21, ROI -16.3%; CLV n 30 over 18 games, -3.6%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 3271, ROI -3.2%; CLV n 1162 over 75 games, -5.1%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 753, ROI -11.7%; CLV n 918 over 85 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 2207, ROI -5.3%; CLV n 348 over 75 games, -8.9%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 533, ROI -5.9%; CLV n 542 over 68 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 483, ROI -2.2%; CLV n 609 over 85 games, +1.3%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 801, ROI -4.2%; CLV n 581 over 70 games, -7.4%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 1760, ROI -4.2%; CLV n 871 over 78 games, -8.1%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 605, ROI -4.7%; CLV n 629 over 70 games, -2.0%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 20, ROI +8.3%; CLV n 30 over 23 games, +4.3%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 35 over 13 games, +7.2%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 1176, ROI -6.5%; CLV n 30 over 20 games, -8.5%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 2978, ROI -5.2%; CLV n 893 over 79 games, -8.2%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 197, ROI -5.1%; CLV n 245 over 74 games, +1.5%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 819, ROI -3.3%; CLV n 858 over 70 games, -1.7%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 30, ROI -0.9%; CLV n 84 over 32 games, +5.5%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 681, ROI -8.2%; CLV n 495 over 70 games, -2.8%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 1930, ROI -2.1%; CLV n 787 over 66 games, -4.8%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1413, ROI -6.9%; CLV n 798 over 78 games, -3.4%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1376, ROI -7.3%; CLV n 840 over 84 games, -3.4%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 2648, ROI -3.5%; CLV n 1240 over 70 games, -4.0%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3609, ROI -5.5%; CLV n 1634 over 85 games, -4.3%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 415, ROI +1.3%; CLV n 446 over 43 games, -2.1%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 226, ROI -5.1%; CLV n 249 over 63 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 812, ROI -3.4%; CLV n 852 over 70 games, -1.6%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2986, ROI -5.2%; CLV n 885 over 70 games, -8.2%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 78 over 15 games, +5.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 125, ROI -11.1%; CLV n 148 over 58 games, +2.1%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 632, ROI -0.4%; CLV n 636 over 70 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 180, ROI -14.3%; CLV n 216 over 55 games, -1.0%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 422, ROI -3.9%; CLV n 476 over 75 games, -6.5%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 21, ROI -16.3%; CLV n 30 over 18 games, -3.6%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2525, ROI -5.5%; CLV n 370 over 64 games, -11.0%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 476, ROI +0.3%; CLV n 329 over 70 games, -3.6%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -9.6%; CLV n 606 over 70 games, -5.5%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 741, ROI -7.0%; CLV n 288 over 65 games, -2.6%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 597, ROI -1.9%; CLV n 361 over 67 games, -2.8%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 102, ROI +10.1%; CLV n 118 over 51 games, -5.6%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI +1.2%; CLV n 47 over 29 games, -2.9%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI +1.7%; CLV n 33 over 22 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 467, ROI -4.7%; CLV n 157 over 58 games, -3.8%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 253, ROI -11.1%; CLV n 31 over 22 games, -4.9%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 5299 | 4024 (64) | 63% | 63% | -4.8% (-8.1% to -1.8%) | 2080 (85) | -3.8% (-4.2% to -3.4%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 5089 | 4024 (64) | 63% | 63% | -4.8% (-8.1% to -1.8%) | 1986 (70) | -4.2% (-4.5% to -3.8%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 4801 | 3609 (63) | 64% | 64% | -5.5% (-9.2% to -2.2%) | 1634 (85) | -4.3% (-4.7% to -3.8%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 4202 | 3271 (64) | 66% | 65% | -3.2% (-7.0% to +0.2%) | 1162 (75) | -5.1% (-5.6% to -4.6%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 3923 | 2986 (64) | 68% | 68% | -5.2% (-8.8% to -1.7%) | 901 (79) | -8.2% (-8.6% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 3893 | 2986 (64) | 68% | 68% | -5.2% (-8.8% to -1.7%) | 885 (70) | -8.2% (-8.7% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 3915 | 2978 (64) | 68% | 68% | -5.2% (-8.7% to -1.8%) | 893 (79) | -8.2% (-8.6% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 3691 | 2830 (63) | 66% | 66% | -6.3% (-10.8% to -2.1%) | 734 (73) | -5.4% (-6.1% to -4.7%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 3364 | 2648 (64) | 63% | 63% | -3.5% (-7.5% to -0.1%) | 1240 (70) | -4.0% (-4.5% to -3.6%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 3316 | 2525 (57) | 69% | 69% | -5.5% (-9.6% to -1.5%) | 370 (64) | -11.0% (-11.8% to -10.2%) | -0.9% (-1.2% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 2894 | 2207 (60) | 70% | 70% | -5.3% (-9.0% to -1.7%) | 348 (75) | -8.9% (-9.5% to -8.3%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 2704 | 1930 (46) | 67% | 65% | -2.1% (-6.4% to +2.0%) | 787 (66) | -4.8% (-5.5% to -4.0%) | -0.2% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 2291 | 1789 (51) | 72% | 71% | -5.1% (-9.3% to -1.2%) | 138 (53) | -9.2% (-10.2% to -8.2%) | -0.7% (-1.1% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 2357 | 1760 (64) | 64% | 64% | -4.2% (-8.1% to -0.4%) | 871 (78) | -8.1% (-8.6% to -7.6%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1745 | 1413 (63) | 60% | 62% | -6.9% (-11.6% to -2.3%) | 798 (78) | -3.4% (-3.9% to -2.9%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1935 | 1376 (62) | 61% | 63% | -7.3% (-11.6% to -2.6%) | 840 (84) | -3.4% (-4.0% to -2.8%) | -0.6% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 1632 | 1197 (64) | 62% | 62% | -5.2% (-8.7% to -1.2%) | 763 (79) | -8.0% (-8.4% to -7.5%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1511 | 1176 (37) | 73% | 73% | -6.5% (-10.3% to -2.8%) | 30 (20) | -8.5% (-10.8% to -6.5%) | -0.1% (-1.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1368 | 1155 (64) | 55% | 55% | -1.4% (-6.4% to +3.4%) | 1217 (76) | -3.5% (-3.8% to -3.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1308 | 983 (64) | 47% | 49% | -3.9% (-10.2% to +2.2%) | 1118 (85) | -0.4% (-0.8% to +0.1%) | +0.1% (-0.2% to +0.4%) | hypothesis (range includes zero) |
| edge = 0-3% | 941 | 819 (64) | 48% | 50% | -3.3% (-10.4% to +4.0%) | 858 (70) | -1.7% (-2.0% to -1.3%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 935 | 812 (64) | 48% | 50% | -3.4% (-10.8% to +4.0%) | 852 (70) | -1.6% (-2.0% to -1.3%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 935 | 812 (64) | 48% | 50% | -3.4% (-10.8% to +4.0%) | 852 (70) | -1.6% (-2.0% to -1.3%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1058 | 801 (64) | 62% | 61% | -4.2% (-8.6% to +0.3%) | 581 (70) | -7.4% (-7.9% to -6.9%) | -0.6% (-1.0% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1097 | 753 (64) | 47% | 53% | -11.7% (-18.4% to -5.0%) | 918 (85) | -2.1% (-2.5% to -1.6%) | -0.4% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 941 | 741 (63) | 60% | 62% | -7.0% (-12.2% to -2.2%) | 288 (65) | -2.6% (-3.0% to -2.1%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 941 | 741 (63) | 60% | 62% | -7.0% (-12.2% to -2.2%) | 288 (65) | -2.6% (-3.0% to -2.1%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 882 | 712 (64) | 59% | 62% | -9.6% (-14.4% to -5.0%) | 606 (70) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 882 | 712 (64) | 59% | 62% | -9.6% (-14.4% to -5.0%) | 606 (70) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 850 | 681 (60) | 56% | 59% | -8.2% (-13.2% to -2.9%) | 495 (70) | -2.8% (-3.2% to -2.4%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 713 | 632 (64) | 50% | 51% | -0.4% (-7.9% to +6.4%) | 636 (70) | -1.8% (-2.3% to -1.4%) | +0.6% (+0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 710 | 605 (62) | 49% | 53% | -4.7% (-12.6% to +3.0%) | 629 (70) | -2.0% (-2.3% to -1.7%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 745 | 597 (61) | 60% | 59% | -1.9% (-8.8% to +4.7%) | 361 (67) | -2.8% (-3.5% to -2.1%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 745 | 597 (61) | 60% | 59% | -1.9% (-8.8% to +4.7%) | 361 (67) | -2.8% (-3.5% to -2.1%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 618 | 533 (62) | 49% | 52% | -5.9% (-14.2% to +2.1%) | 542 (68) | -2.3% (-2.7% to -2.0%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 729 | 483 (64) | 44% | 46% | -2.2% (-11.2% to +6.4%) | 609 (85) | +1.3% (+0.8% to +1.8%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 597 | 476 (63) | 61% | 59% | +0.3% (-6.0% to +6.9%) | 329 (70) | -3.6% (-4.2% to -2.9%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 597 | 476 (63) | 61% | 59% | +0.3% (-6.0% to +6.9%) | 329 (70) | -3.6% (-4.2% to -2.9%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 585 | 467 (58) | 63% | 64% | -4.7% (-10.8% to +0.6%) | 157 (58) | -3.8% (-4.5% to -3.1%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 585 | 467 (58) | 63% | 64% | -4.7% (-10.8% to +0.6%) | 157 (58) | -3.8% (-4.5% to -3.1%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 539 | 422 (64) | 63% | 62% | -3.9% (-11.1% to +3.3%) | 476 (75) | -6.5% (-6.9% to -6.2%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 498 | 415 (40) | 54% | 53% | +1.3% (-6.6% to +9.4%) | 446 (43) | -2.1% (-2.5% to -1.8%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 478 | 413 (64) | 44% | 46% | -3.1% (-11.9% to +6.2%) | 459 (74) | +0.3% (-0.1% to +0.8%) | +0.5% (-0.0% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 444 | 337 (37) | 69% | 69% | -4.9% (-11.2% to +1.7%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | hypothesis (range includes zero) |
| stat/market = pr | 444 | 337 (37) | 69% | 69% | -4.9% (-11.2% to +1.7%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 351 | 271 (37) | 71% | 70% | -3.4% (-9.2% to +2.0%) | 4 (4) | -16.1% (4 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 351 | 271 (37) | 71% | 70% | -3.4% (-9.2% to +2.0%) | 4 (4) | -16.1% (4 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 322 | 253 (44) | 64% | 69% | -11.1% (-20.6% to -2.2%) | 31 (22) | -4.9% (-8.1% to -1.7%) | -2.3% (-4.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 322 | 253 (44) | 64% | 69% | -11.1% (-20.6% to -2.2%) | 31 (22) | -4.9% (-8.1% to -1.7%) | -2.3% (-4.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 441 | 226 (58) | 44% | 48% | -5.1% (-17.2% to +6.6%) | 327 (78) | +2.5% (+1.9% to +3.2%) | -1.7% (-2.2% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 261 | 226 (58) | 44% | 48% | -5.1% (-17.2% to +6.6%) | 249 (63) | +1.5% (+0.9% to +2.0%) | -1.6% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 3-6% | 284 | 197 (58) | 44% | 48% | -5.1% (-18.0% to +7.0%) | 245 (74) | +1.5% (+0.9% to +2.0%) | -1.3% (-1.7% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 222 | 180 (47) | 42% | 49% | -14.3% (-29.6% to +2.5%) | 216 (55) | -1.0% (-1.5% to -0.3%) | +0.8% (+0.3% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 153 | 125 (50) | 39% | 46% | -11.1% (-28.9% to +6.3%) | 148 (58) | +2.1% (+1.4% to +2.8%) | -1.8% (-2.6% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 128 | 102 (44) | 73% | 63% | +10.1% (-5.6% to +23.8%) | 118 (51) | -5.6% (-6.2% to -5.0%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 128 | 102 (44) | 73% | 63% | +10.1% (-5.6% to +23.8%) | 118 (51) | -5.6% (-6.2% to -5.0%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 116 | 101 (44) | 50% | 50% | +2.2% (-17.1% to +21.5%) | 105 (49) | +0.5% (-0.5% to +1.5%) | -1.2% (-2.2% to -0.3%) | hypothesis (range includes zero) |
| tier = Lean | 68 | 55 (33) | 55% | 57% | -2.4% (-21.2% to +17.7%) | 61 (36) | -2.5% (-3.6% to -1.4%) | -1.3% (-2.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = moneyline | 53 | 39 (24) | 69% | 66% | +1.2% (-24.9% to +23.5%) | 47 (29) | -2.9% (-4.2% to -1.5%) | +0.5% (-0.7% to +1.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 68 | 39 (24) | 69% | 66% | +1.2% (-24.9% to +23.5%) | 55 (35) | -3.1% (-4.2% to -1.8%) | +0.3% (-0.8% to +1.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 159 | 30 (16) | 43% | 48% | -0.9% (-41.8% to +44.3%) | 84 (32) | +5.5% (+3.9% to +7.3%) | -2.9% (-4.6% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = blk | 41 | 29 (19) | 66% | 61% | +1.7% (-27.9% to +28.7%) | 33 (22) | -5.6% (-6.5% to -4.7%) | -1.1% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 41 | 29 (19) | 66% | 61% | +1.7% (-27.9% to +28.7%) | 33 (22) | -5.6% (-6.5% to -4.7%) | -1.1% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = away | 40 | 21 (12) | 57% | 67% | -16.3% (-51.5% to +19.4%) | 30 (18) | -3.6% (-5.2% to -1.3%) | -0.2% (-1.8% to +2.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 40 | 21 (12) | 57% | 67% | -16.3% (-51.5% to +19.4%) | 30 (18) | -3.6% (-5.2% to -1.3%) | -0.2% (-1.8% to +2.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 40 | 20 (15) | 40% | 38% | +8.3% (-50.7% to +71.0%) | 30 (23) | +4.3% (+3.2% to +5.5%) | +0.3% (-1.4% to +2.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = home | 28 | 18 (12) | 83% | 66% | +21.6% (-7.4% to +46.5%) | 25 (17) | -2.6% (-3.8% to -1.5%) | +0.8% (-0.2% to +1.7%) | hypothesis |
| side = home | 28 | 18 (12) | 83% | 66% | +21.6% (-7.4% to +46.5%) | 25 (17) | -2.6% (-3.8% to -1.5%) | +0.8% (-0.2% to +1.7%) | hypothesis |
| chance = 10-20% | 95 | 0 (0) | – | – | – (–) | 35 (13) | +7.2% (+4.6% to +10.8%) | -1.3% (-3.4% to +1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 53 | 0 (0) | – | – | – (–) | 26 (13) | +6.2% (+4.5% to +7.9%) | -1.5% (-2.5% to -0.6%) | hypothesis |
| lane = likely, sport = nfl | 29 | 0 (0) | – | – | – (–) | 16 (9) | -5.5% (9 games) | -0.7% (9 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 180 | 0 (0) | – | – | – (–) | 78 (15) | +5.9% (+4.6% to +7.8%) | -2.2% (-3.5% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 209 | 0 (0) | – | – | – (–) | 94 (15) | +4.0% (+2.5% to +5.8%) | -1.9% (-3.1% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 14 | 0 (0) | – | – | – (–) | 8 (6) | -4.4% (6 games) | -1.2% (6 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
