# Research lab report

Built 2026-11-23T19:35:54Z UTC from 9910 logged code candidates (8616 settled, 3370 with a close, 142 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 6870, ROI -5.0%; CLV n 1576 over 128 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 338, ROI -4.9%; CLV n 461 over 128 games, +3.0%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1408, ROI -1.8%; CLV n 1333 over 112 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 8616, ROI -4.5%; CLV n 3210 over 113 games, -4.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 158 over 27 games, +4.4%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2912, ROI -5.0%; CLV n 1346 over 128 games, -8.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 108, ROI -1.1%; CLV n 102 over 63 games, -2.7%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1638, ROI -2.5%; CLV n 1692 over 139 games, -0.4%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 3958, ROI -5.0%; CLV n 230 over 91 games, -9.5%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 87, ROI -5.3%; CLV n 102 over 65 games, -3.9%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 975, ROI -0.1%; CLV n 537 over 111 games, -4.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1407, ROI -8.8%; CLV n 984 over 113 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1602, ROI -4.8%; CLV n 442 over 106 games, -3.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -2.9%; CLV n 596 over 108 games, -4.2%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 181, ROI +11.0%; CLV n 181 over 82 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 50, ROI +9.9%; CLV n 50 over 31 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1021, ROI -4.0%; CLV n 257 over 92 games, -4.1%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 580, ROI -9.3%; CLV n 50 over 35 games, -8.1%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 126 over 27 games, +6.6%)
- **stat/market = pa**: IN-SAMPLE SIGNAL: negative ROI (settled 619, ROI -4.6%; CLV n 7 over 7 games, -15.1%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 789, ROI -5.6%; CLV n 19 over 13 games, -20.1%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 49, ROI -2.9%; CLV n 57 over 37 games, -3.9%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1997, ROI -1.3%; CLV n 1899 over 123 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 6532, ROI -5.4%; CLV n 1243 over 119 games, -6.8%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 38, ROI -8.4%; CLV n 45 over 28 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 126 over 27 games, +6.6%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 7338, ROI -4.1%; CLV n 1988 over 123 games, -6.0%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1278, ROI -6.6%; CLV n 1382 over 140 games, -2.0%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 5006, ROI -5.0%; CLV n 582 over 123 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 924, ROI -5.4%; CLV n 842 over 110 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 776, ROI +0.4%; CLV n 907 over 139 games, +1.3%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1910, ROI -4.6%; CLV n 1039 over 113 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 4202, ROI -5.3%; CLV n 1523 over 125 games, -8.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 1059, ROI -5.1%; CLV n 979 over 112 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 39, ROI +5.4%; CLV n 50 over 39 games, +4.8%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 68 over 25 games, +7.4%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 41 over 21 games, +6.3%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2618, ROI -4.5%; CLV n 53 over 36 games, -7.7%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 6861, ROI -5.1%; CLV n 1567 over 128 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 303, ROI -5.7%; CLV n 340 over 119 games, +1.8%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1414, ROI -1.6%; CLV n 1339 over 112 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +4.1%; CLV n 124 over 47 games, +6.2%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1208, ROI -5.8%; CLV n 692 over 107 games, -3.3%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 4635, ROI -3.6%; CLV n 1375 over 116 games, -5.2%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2773, ROI -5.3%; CLV n 1303 over 134 games, -4.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2919, ROI -5.8%; CLV n 1327 over 141 games, -3.9%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 5697, ROI -3.8%; CLV n 2043 over 113 games, -4.7%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 7882, ROI -5.5%; CLV n 2677 over 142 games, -4.9%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 734, ROI +6.8%; CLV n 693 over 68 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 338, ROI -4.9%; CLV n 328 over 101 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1408, ROI -1.8%; CLV n 1333 over 112 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 6870, ROI -5.0%; CLV n 1549 over 113 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 133 over 27 games, +6.2%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 49, ROI -2.9%; CLV n 57 over 37 games, -3.9%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 147, ROI -9.1%; CLV n 142 over 76 games, +0.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 191, ROI -1.7%; CLV n 193 over 85 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1093, ROI -0.6%; CLV n 1018 over 111 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 315, ROI -5.9%; CLV n 315 over 87 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 757, ROI -0.8%; CLV n 739 over 120 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 38, ROI -8.4%; CLV n 45 over 28 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 6026, ROI -5.5%; CLV n 735 over 109 games, -11.5%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 126 over 27 games, +6.6%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 975, ROI -0.1%; CLV n 537 over 111 games, -4.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1407, ROI -8.8%; CLV n 984 over 113 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1602, ROI -4.8%; CLV n 442 over 106 games, -3.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -2.9%; CLV n 596 over 108 games, -4.2%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 181, ROI +11.0%; CLV n 181 over 82 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 87, ROI -5.3%; CLV n 87 over 54 games, -3.9%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 50, ROI +9.9%; CLV n 50 over 31 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1021, ROI -4.0%; CLV n 257 over 92 games, -4.1%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 580, ROI -9.3%; CLV n 50 over 35 games, -8.1%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 126 over 27 games, +6.6%)
- **sport = nba, stat/market = pa**: IN-SAMPLE SIGNAL: negative ROI (settled 619, ROI -4.6%; CLV n 7 over 7 games, -15.1%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 789, ROI -5.6%; CLV n 19 over 13 games, -20.1%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 9910 | 8616 (115) | 64% | 64% | -4.5% (-6.5% to -2.5%) | 3370 (142) | -4.4% (-4.7% to -4.0%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 9632 | 8616 (115) | 64% | 64% | -4.5% (-6.5% to -2.5%) | 3210 (113) | -4.8% (-5.1% to -4.5%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 9136 | 7882 (114) | 64% | 65% | -5.5% (-7.7% to -3.4%) | 2677 (142) | -4.9% (-5.3% to -4.5%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 8266 | 7338 (115) | 66% | 66% | -4.1% (-6.3% to -2.0%) | 1988 (123) | -6.0% (-6.4% to -5.6%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 7794 | 6870 (115) | 68% | 67% | -5.0% (-7.2% to -2.9%) | 1576 (128) | -8.7% (-9.1% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 7753 | 6870 (115) | 68% | 67% | -5.0% (-7.2% to -2.9%) | 1549 (113) | -8.8% (-9.2% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 7786 | 6861 (115) | 68% | 67% | -5.1% (-7.3% to -3.0%) | 1567 (128) | -8.8% (-9.1% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 7368 | 6532 (114) | 66% | 66% | -5.4% (-8.1% to -2.8%) | 1243 (119) | -6.8% (-7.4% to -6.2%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 6833 | 6026 (108) | 68% | 68% | -5.5% (-8.1% to -3.1%) | 735 (109) | -11.5% (-12.1% to -11.0%) | -0.9% (-1.2% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 6360 | 5697 (115) | 64% | 63% | -3.8% (-6.2% to -1.5%) | 2043 (113) | -4.7% (-5.0% to -4.3%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 5727 | 5006 (111) | 70% | 69% | -5.0% (-7.3% to -2.6%) | 582 (123) | -9.5% (-10.0% to -9.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 5620 | 4635 (95) | 66% | 65% | -3.6% (-6.3% to -1.1%) | 1375 (116) | -5.2% (-5.7% to -4.7%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 4769 | 4202 (115) | 64% | 64% | -5.3% (-7.9% to -2.7%) | 1523 (125) | -8.8% (-9.2% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 4474 | 3958 (102) | 71% | 71% | -5.0% (-7.4% to -2.7%) | 230 (91) | -9.5% (-10.3% to -8.6%) | -0.8% (-1.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3550 | 2919 (113) | 63% | 64% | -5.8% (-9.1% to -2.6%) | 1327 (141) | -3.9% (-4.4% to -3.4%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 3320 | 2912 (115) | 63% | 62% | -5.0% (-7.6% to -2.0%) | 1346 (128) | -8.6% (-9.0% to -8.2%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 3025 | 2773 (114) | 62% | 62% | -5.3% (-8.1% to -2.6%) | 1303 (134) | -4.0% (-4.4% to -3.6%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2970 | 2618 (88) | 74% | 73% | -4.5% (-6.8% to -2.2%) | 53 (36) | -7.7% (-9.4% to -6.2%) | -0.2% (-1.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2198 | 1997 (115) | 55% | 55% | -1.3% (-5.7% to +3.0%) | 1899 (123) | -3.5% (-3.8% to -3.2%) | -0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 2115 | 1910 (115) | 62% | 61% | -4.6% (-7.6% to -1.6%) | 1039 (113) | -8.0% (-8.4% to -7.7%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 2002 | 1638 (114) | 47% | 49% | -2.5% (-7.7% to +2.9%) | 1692 (139) | -0.4% (-0.7% to -0.1%) | +0.2% (-0.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1789 | 1602 (114) | 63% | 63% | -4.8% (-8.0% to -1.6%) | 442 (106) | -3.0% (-3.4% to -2.6%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1789 | 1602 (114) | 63% | 63% | -4.8% (-8.0% to -1.6%) | 442 (106) | -3.0% (-3.4% to -2.6%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1526 | 1414 (114) | 49% | 50% | -1.6% (-7.8% to +4.4%) | 1339 (112) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1521 | 1408 (114) | 49% | 50% | -1.8% (-8.0% to +4.2%) | 1333 (112) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1521 | 1408 (114) | 49% | 50% | -1.8% (-8.0% to +4.2%) | 1333 (112) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1547 | 1407 (115) | 60% | 62% | -8.8% (-11.9% to -5.7%) | 984 (113) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1547 | 1407 (115) | 60% | 62% | -8.8% (-11.9% to -5.7%) | 984 (113) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1423 | 1305 (112) | 61% | 61% | -2.9% (-6.9% to +0.9%) | 596 (108) | -4.2% (-4.7% to -3.6%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1423 | 1305 (112) | 61% | 61% | -2.9% (-6.9% to +0.9%) | 596 (108) | -4.2% (-4.7% to -3.6%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1644 | 1278 (115) | 50% | 53% | -6.6% (-11.4% to -1.6%) | 1382 (140) | -2.0% (-2.4% to -1.7%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1265 | 1208 (103) | 58% | 60% | -5.8% (-10.1% to -1.3%) | 692 (107) | -3.3% (-3.8% to -2.9%) | -0.4% (-0.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1190 | 1093 (113) | 50% | 51% | -0.6% (-7.2% to +5.8%) | 1018 (111) | -1.9% (-2.2% to -1.5%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1154 | 1059 (110) | 49% | 53% | -5.1% (-11.2% to +1.2%) | 979 (112) | -2.1% (-2.3% to -1.8%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1158 | 1021 (109) | 64% | 64% | -4.0% (-7.7% to -0.3%) | 257 (92) | -4.1% (-4.7% to -3.6%) | +0.3% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1158 | 1021 (109) | 64% | 64% | -4.0% (-7.7% to -0.3%) | 257 (92) | -4.1% (-4.7% to -3.6%) | +0.3% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1094 | 975 (114) | 62% | 60% | -0.1% (-4.6% to +4.2%) | 537 (111) | -4.4% (-4.9% to -3.9%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1094 | 975 (114) | 62% | 60% | -0.1% (-4.6% to +4.2%) | 537 (111) | -4.4% (-4.9% to -3.9%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 1009 | 924 (110) | 49% | 52% | -5.4% (-12.1% to +1.3%) | 842 (110) | -2.4% (-2.6% to -2.1%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 898 | 789 (87) | 68% | 68% | -5.6% (-9.8% to -1.4%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 898 | 789 (87) | 68% | 68% | -5.6% (-9.8% to -1.4%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 1059 | 776 (114) | 45% | 46% | +0.4% (-6.4% to +7.4%) | 907 (139) | +1.3% (+0.9% to +1.7%) | +0.3% (-0.0% to +0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 843 | 757 (115) | 65% | 62% | -0.8% (-6.0% to +4.3%) | 739 (120) | -6.6% (-7.0% to -6.3%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 774 | 734 (70) | 57% | 53% | +6.8% (+0.4% to +12.7%) | 693 (68) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 702 | 648 (113) | 46% | 46% | +1.4% (-5.7% to +9.2%) | 656 (117) | +0.1% (-0.3% to +0.5%) | +0.5% (+0.1% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 709 | 619 (88) | 69% | 69% | -4.6% (-8.8% to -0.5%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pa | 709 | 619 (88) | 69% | 69% | -4.6% (-8.8% to -0.5%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = ra | 656 | 580 (95) | 66% | 68% | -9.3% (-15.2% to -3.5%) | 50 (35) | -8.1% (-10.9% to -5.3%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 656 | 580 (95) | 66% | 68% | -9.3% (-15.2% to -3.5%) | 50 (35) | -8.1% (-10.9% to -5.3%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 595 | 338 (104) | 43% | 48% | -4.9% (-14.8% to +4.3%) | 461 (128) | +3.0% (+2.4% to +3.6%) | -1.4% (-1.8% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 358 | 338 (104) | 43% | 48% | -4.9% (-14.8% to +4.3%) | 328 (101) | +1.7% (+1.2% to +2.2%) | -1.2% (-1.7% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 331 | 315 (87) | 46% | 49% | -5.9% (-19.2% to +7.2%) | 315 (87) | -1.4% (-1.9% to -0.8%) | +0.5% (+0.1% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 397 | 303 (102) | 43% | 48% | -5.7% (-15.1% to +3.8%) | 340 (119) | +1.8% (+1.3% to +2.3%) | -0.9% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 204 | 191 (83) | 43% | 46% | -1.7% (-16.1% to +14.0%) | 193 (85) | +2.2% (+1.5% to +3.0%) | -1.6% (-2.3% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 200 | 181 (82) | 72% | 62% | +11.0% (+0.8% to +20.5%) | 181 (82) | -5.7% (-6.2% to -5.3%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 200 | 181 (82) | 72% | 62% | +11.0% (+0.8% to +20.5%) | 181 (82) | -5.7% (-6.2% to -5.3%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 165 | 147 (73) | 44% | 50% | -9.1% (-24.8% to +6.8%) | 142 (76) | +0.9% (+0.1% to +1.8%) | -0.9% (-1.7% to -0.1%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 114 | 108 (64) | 56% | 57% | -1.1% (-14.3% to +12.4%) | 102 (63) | -2.7% (-3.5% to -2.0%) | -1.1% (-1.8% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 96 | 87 (54) | 66% | 67% | -5.3% (-21.8% to +10.6%) | 87 (54) | -3.9% (-4.8% to -2.9%) | -0.5% (-1.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 118 | 87 (54) | 66% | 67% | -5.3% (-21.8% to +10.6%) | 102 (65) | -3.9% (-4.6% to -3.0%) | -0.4% (-1.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 62 | 50 (31) | 72% | 61% | +9.9% (-10.9% to +27.1%) | 50 (31) | -5.6% (-6.3% to -4.8%) | -1.1% (-1.7% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 62 | 50 (31) | 72% | 61% | +9.9% (-10.9% to +27.1%) | 50 (31) | -5.6% (-6.3% to -4.8%) | -1.1% (-1.7% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 60 | 49 (31) | 67% | 68% | -2.9% (-24.4% to +17.5%) | 57 (37) | -3.9% (-5.0% to -2.9%) | -0.4% (-1.6% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 60 | 49 (31) | 67% | 68% | -2.9% (-24.4% to +17.5%) | 57 (37) | -3.9% (-5.0% to -2.9%) | -0.4% (-1.6% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 62 | 39 (30) | 38% | 38% | +5.4% (-31.1% to +44.8%) | 50 (39) | +4.8% (+3.4% to +6.2%) | +1.1% (-0.5% to +2.8%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 6%+ | 201 | 38 (21) | 45% | 48% | +4.1% (-31.3% to +42.9%) | 124 (47) | +6.2% (+4.8% to +7.7%) | -2.4% (-3.7% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 58 | 38 (23) | 63% | 67% | -8.4% (-35.5% to +17.2%) | 45 (28) | -3.9% (-5.1% to -2.3%) | -0.4% (-1.7% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 58 | 38 (23) | 63% | 67% | -8.4% (-35.5% to +17.2%) | 45 (28) | -3.9% (-5.1% to -2.3%) | -0.4% (-1.7% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 129 | 0 (0) | – | – | – (–) | 68 (25) | +7.4% (+5.7% to +9.5%) | -0.9% (-2.3% to +0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 69 | 0 (0) | – | – | – (–) | 41 (21) | +6.3% (+5.0% to +7.6%) | -1.3% (-2.1% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, sport = nfl | 38 | 0 (0) | – | – | – (–) | 25 (13) | -5.6% (-6.2% to -4.9%) | -0.8% (-1.4% to -0.1%) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 226 | 0 (0) | – | – | – (–) | 126 (27) | +6.6% (+5.5% to +7.9%) | -1.5% (-2.5% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 237 | 0 (0) | – | – | – (–) | 133 (27) | +6.2% (+5.2% to +7.5%) | -1.6% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 226 | 0 (0) | – | – | – (–) | 126 (27) | +6.6% (+5.5% to +7.9%) | -1.5% (-2.5% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 275 | 0 (0) | – | – | – (–) | 158 (27) | +4.4% (+3.2% to +5.8%) | -1.5% (-2.3% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 226 | 0 (0) | – | – | – (–) | 126 (27) | +6.6% (+5.5% to +7.9%) | -1.5% (-2.5% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 19 | 0 (0) | – | – | – (–) | 13 (9) | -4.0% (9 games) | -0.8% (9 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| sport = nfl, stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 226 | 0 (0) | – | – | – (–) | 126 (27) | +6.6% (+5.5% to +7.9%) | -1.5% (-2.5% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
