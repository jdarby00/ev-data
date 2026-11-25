# Research lab report

Built 2026-11-25T11:10:56Z UTC from 10458 logged code candidates (9603 settled, 3673 with a close, 156 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 7706, ROI -4.8%; CLV n 1740 over 142 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 356, ROI -7.5%; CLV n 479 over 135 games, +3.0%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -0.8%; CLV n 1454 over 125 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 9603, ROI -4.2%; CLV n 3509 over 126 games, -4.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 162 over 28 games, +4.3%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 3271, ROI -4.8%; CLV n 1485 over 142 games, -8.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 116, ROI -0.4%; CLV n 110 over 69 games, -2.5%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1781, ROI -2.2%; CLV n 1823 over 153 games, -0.4%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 4435, ROI -4.8%; CLV n 255 over 100 games, -9.4%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 93, ROI -11.4%; CLV n 109 over 70 games, -3.9%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1088, ROI -1.5%; CLV n 595 over 123 games, -4.6%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1561, ROI -8.8%; CLV n 1092 over 125 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1794, ROI -3.8%; CLV n 483 over 119 games, -3.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1438, ROI -3.0%; CLV n 640 over 121 games, -4.2%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 192, ROI +10.9%; CLV n 192 over 89 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 55, ROI +10.8%; CLV n 55 over 34 games, -5.5%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1144, ROI -2.7%; CLV n 277 over 104 games, -4.2%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 645, ROI -9.2%; CLV n 54 over 39 games, -8.1%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 888, ROI -4.9%; CLV n 21 over 14 games, -20.6%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 52, ROI -8.5%; CLV n 60 over 39 games, -4.0%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 2180, ROI -1.4%; CLV n 2065 over 136 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 7330, ROI -5.0%; CLV n 1370 over 132 games, -7.0%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 8226, ROI -3.7%; CLV n 2197 over 136 games, -6.0%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1377, ROI -7.3%; CLV n 1476 over 154 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 5635, ROI -4.7%; CLV n 640 over 135 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 1012, ROI -3.9%; CLV n 916 over 123 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 834, ROI -0.7%; CLV n 967 over 153 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 2122, ROI -4.4%; CLV n 1150 over 126 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 4722, ROI -5.0%; CLV n 1681 over 138 games, -8.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 1156, ROI -3.8%; CLV n 1062 over 125 games, -2.0%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 43, ROI +2.3%; CLV n 55 over 44 games, +4.7%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 68 over 25 games, +7.4%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 43 over 22 games, +6.0%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2934, ROI -4.3%; CLV n 59 over 41 games, -7.4%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 7697, ROI -4.8%; CLV n 1731 over 142 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 319, ROI -8.0%; CLV n 355 over 126 games, +1.9%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1547, ROI -0.6%; CLV n 1460 over 125 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 40, ROI -1.1%; CLV n 127 over 49 games, +6.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1317, ROI -6.0%; CLV n 747 over 116 games, -3.4%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 5304, ROI -3.4%; CLV n 1529 over 129 games, -5.3%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2982, ROI -4.9%; CLV n 1397 over 148 games, -4.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3244, ROI -5.9%; CLV n 1430 over 154 games, -4.0%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 6359, ROI -3.4%; CLV n 2243 over 126 games, -4.7%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 8816, ROI -5.1%; CLV n 2932 over 156 games, -5.0%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 787, ROI +5.1%; CLV n 741 over 76 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 356, ROI -7.5%; CLV n 343 over 107 games, +1.8%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -0.8%; CLV n 1454 over 125 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 7706, ROI -4.8%; CLV n 1712 over 126 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 28 games, +6.2%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 52, ROI -8.5%; CLV n 60 over 39 games, -4.0%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 159, ROI -11.1%; CLV n 151 over 78 games, +1.2%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 197, ROI -4.7%; CLV n 199 over 89 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1207, ROI +0.5%; CLV n 1120 over 124 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 334, ROI -5.3%; CLV n 334 over 96 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 814, ROI -2.2%; CLV n 794 over 133 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 6799, ROI -5.0%; CLV n 837 over 122 games, -11.4%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1088, ROI -1.5%; CLV n 595 over 123 games, -4.6%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1561, ROI -8.8%; CLV n 1092 over 125 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1794, ROI -3.8%; CLV n 483 over 119 games, -3.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1438, ROI -3.0%; CLV n 640 over 121 games, -4.2%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 192, ROI +10.9%; CLV n 192 over 89 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 93, ROI -11.4%; CLV n 93 over 58 games, -4.0%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 55, ROI +10.8%; CLV n 55 over 34 games, -5.5%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1144, ROI -2.7%; CLV n 277 over 104 games, -4.2%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 645, ROI -9.2%; CLV n 54 over 39 games, -8.1%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 888, ROI -4.9%; CLV n 21 over 14 games, -20.6%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 10458 | 9603 (128) | 64% | 64% | -4.2% (-6.0% to -2.5%) | 3673 (156) | -4.4% (-4.7% to -4.1%) | -0.2% (-0.3% to +0.0%) |  |
| sport = nba | 10176 | 9603 (128) | 64% | 64% | -4.2% (-6.0% to -2.5%) | 3509 (126) | -4.8% (-5.1% to -4.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 9643 | 8816 (127) | 65% | 65% | -5.1% (-7.1% to -3.2%) | 2932 (156) | -5.0% (-5.3% to -4.6%) | -0.2% (-0.4% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 8737 | 8226 (128) | 66% | 66% | -3.7% (-5.7% to -1.7%) | 2197 (136) | -6.0% (-6.4% to -5.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 8246 | 7706 (128) | 68% | 67% | -4.8% (-6.7% to -2.8%) | 1740 (142) | -8.7% (-9.1% to -8.4%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 8204 | 7706 (128) | 68% | 67% | -4.8% (-6.7% to -2.8%) | 1712 (126) | -8.8% (-9.2% to -8.5%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 8237 | 7697 (128) | 68% | 67% | -4.8% (-6.9% to -2.8%) | 1731 (142) | -8.8% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 7791 | 7330 (127) | 67% | 66% | -5.0% (-7.4% to -2.5%) | 1370 (132) | -7.0% (-7.6% to -6.4%) | -0.5% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 7235 | 6799 (121) | 68% | 68% | -5.0% (-7.3% to -2.7%) | 837 (122) | -11.4% (-11.9% to -10.9%) | -0.8% (-1.1% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 6706 | 6359 (128) | 64% | 64% | -3.4% (-5.6% to -1.2%) | 2243 (126) | -4.7% (-5.0% to -4.4%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 6056 | 5635 (124) | 70% | 69% | -4.7% (-6.9% to -2.5%) | 640 (135) | -9.5% (-10.0% to -9.0%) | -0.8% (-1.1% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 5918 | 5304 (108) | 66% | 65% | -3.4% (-5.5% to -1.1%) | 1529 (129) | -5.3% (-5.8% to -4.9%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 5049 | 4722 (128) | 64% | 64% | -5.0% (-7.4% to -2.7%) | 1681 (138) | -8.8% (-9.1% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 4736 | 4435 (115) | 72% | 71% | -4.8% (-7.0% to -2.6%) | 255 (100) | -9.4% (-10.2% to -8.7%) | -0.9% (-1.2% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 3510 | 3271 (128) | 63% | 62% | -4.8% (-7.1% to -2.2%) | 1485 (142) | -8.6% (-9.0% to -8.3%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3752 | 3244 (125) | 63% | 64% | -5.9% (-8.9% to -3.1%) | 1430 (154) | -4.0% (-4.5% to -3.5%) | -0.6% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 3165 | 2982 (127) | 62% | 62% | -4.9% (-7.6% to -2.4%) | 1397 (148) | -4.1% (-4.4% to -3.7%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 3142 | 2934 (101) | 74% | 73% | -4.3% (-6.3% to -2.1%) | 59 (41) | -7.4% (-9.0% to -6.1%) | -0.3% (-1.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2313 | 2180 (128) | 55% | 55% | -1.4% (-5.5% to +2.9%) | 2065 (136) | -3.5% (-3.7% to -3.2%) | +0.1% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 2241 | 2122 (128) | 62% | 61% | -4.4% (-7.0% to -1.5%) | 1150 (126) | -8.0% (-8.4% to -7.7%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1886 | 1794 (127) | 63% | 63% | -3.8% (-6.9% to -0.8%) | 483 (119) | -3.0% (-3.5% to -2.7%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1886 | 1794 (127) | 63% | 63% | -3.8% (-6.9% to -0.8%) | 483 (119) | -3.0% (-3.5% to -2.7%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 2092 | 1781 (127) | 48% | 49% | -2.2% (-7.1% to +3.0%) | 1823 (153) | -0.4% (-0.8% to -0.1%) | +0.2% (+0.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1647 | 1561 (128) | 60% | 62% | -8.8% (-11.9% to -6.0%) | 1092 (125) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1647 | 1561 (128) | 60% | 62% | -8.8% (-11.9% to -6.0%) | 1092 (125) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1607 | 1547 (127) | 50% | 50% | -0.6% (-6.3% to +5.2%) | 1460 (125) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1601 | 1541 (127) | 49% | 50% | -0.8% (-6.6% to +5.1%) | 1454 (125) | -1.8% (-2.0% to -1.5%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1601 | 1541 (127) | 49% | 50% | -0.8% (-6.6% to +5.1%) | 1454 (125) | -1.8% (-2.0% to -1.5%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1507 | 1438 (125) | 61% | 61% | -3.0% (-6.7% to +0.6%) | 640 (121) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1507 | 1438 (125) | 61% | 61% | -3.0% (-6.7% to +0.6%) | 640 (121) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1721 | 1377 (128) | 50% | 53% | -7.3% (-12.2% to -2.5%) | 1476 (154) | -2.1% (-2.4% to -1.7%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1375 | 1317 (112) | 58% | 60% | -6.0% (-10.2% to -1.8%) | 747 (116) | -3.4% (-3.8% to -2.9%) | -0.4% (-0.6% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1254 | 1207 (126) | 50% | 51% | +0.5% (-6.0% to +6.8%) | 1120 (124) | -1.9% (-2.2% to -1.5%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1205 | 1156 (123) | 50% | 53% | -3.8% (-10.0% to +2.6%) | 1062 (125) | -2.0% (-2.3% to -1.8%) | -0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1212 | 1144 (122) | 65% | 64% | -2.7% (-6.2% to +0.7%) | 277 (104) | -4.2% (-4.7% to -3.6%) | +0.4% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1212 | 1144 (122) | 65% | 64% | -2.7% (-6.2% to +0.7%) | 277 (104) | -4.2% (-4.7% to -3.6%) | +0.4% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1166 | 1088 (127) | 62% | 61% | -1.5% (-5.8% to +2.5%) | 595 (123) | -4.6% (-5.0% to -4.1%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1166 | 1088 (127) | 62% | 61% | -1.5% (-5.8% to +2.5%) | 595 (123) | -4.6% (-5.0% to -4.1%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 1054 | 1012 (123) | 50% | 52% | -3.9% (-10.5% to +2.6%) | 916 (123) | -2.4% (-2.6% to -2.1%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 945 | 888 (100) | 69% | 68% | -4.9% (-8.7% to -1.1%) | 21 (14) | -20.6% (-22.7% to -18.2%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 945 | 888 (100) | 69% | 68% | -4.9% (-8.7% to -1.1%) | 21 (14) | -20.6% (-22.7% to -18.2%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 1107 | 834 (127) | 45% | 46% | -0.7% (-7.3% to +6.2%) | 967 (153) | +1.2% (+0.8% to +1.6%) | +0.3% (+0.1% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 886 | 814 (128) | 64% | 62% | -2.2% (-7.3% to +2.8%) | 794 (133) | -6.6% (-6.9% to -6.3%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 815 | 787 (78) | 56% | 53% | +5.1% (-0.9% to +11.1%) | 741 (76) | -2.4% (-2.7% to -2.1%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pa | 749 | 705 (101) | 71% | 69% | -2.9% (-7.0% to +1.0%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 749 | 705 (101) | 71% | 69% | -2.9% (-7.0% to +1.0%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| chance = 40-50% | 742 | 698 (126) | 45% | 46% | +0.5% (-6.5% to +7.4%) | 705 (130) | +0.1% (-0.3% to +0.4%) | +0.6% (+0.2% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 689 | 645 (108) | 66% | 68% | -9.2% (-14.6% to -3.6%) | 54 (39) | -8.1% (-10.8% to -5.4%) | -2.2% (-3.8% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 689 | 645 (108) | 66% | 68% | -9.2% (-14.6% to -3.6%) | 54 (39) | -8.1% (-10.8% to -5.4%) | -2.2% (-3.8% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 611 | 356 (110) | 42% | 48% | -7.5% (-16.8% to +1.3%) | 479 (135) | +3.0% (+2.4% to +3.7%) | -1.3% (-1.7% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 371 | 356 (110) | 42% | 48% | -7.5% (-16.8% to +1.3%) | 343 (107) | +1.8% (+1.2% to +2.3%) | -1.2% (-1.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 347 | 334 (96) | 46% | 49% | -5.3% (-17.9% to +8.0%) | 334 (96) | -1.4% (-1.9% to -0.9%) | +0.5% (+0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 409 | 319 (108) | 42% | 48% | -8.0% (-17.2% to +1.3%) | 355 (126) | +1.9% (+1.4% to +2.4%) | -0.9% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 209 | 197 (87) | 42% | 46% | -4.7% (-18.8% to +10.1%) | 199 (89) | +2.2% (+1.5% to +2.9%) | -1.7% (-2.4% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 208 | 192 (89) | 72% | 62% | +10.9% (+1.0% to +20.4%) | 192 (89) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 208 | 192 (89) | 72% | 62% | +10.9% (+1.0% to +20.4%) | 192 (89) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 173 | 159 (75) | 43% | 50% | -11.1% (-25.8% to +3.8%) | 151 (78) | +1.2% (+0.4% to +2.1%) | -0.6% (-1.4% to +0.2%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 120 | 116 (70) | 56% | 57% | -0.4% (-13.8% to +13.0%) | 110 (69) | -2.5% (-3.3% to -1.8%) | -0.9% (-1.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 102 | 93 (58) | 61% | 68% | -11.4% (-27.4% to +4.4%) | 93 (58) | -4.0% (-4.9% to -3.0%) | -0.6% (-1.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 125 | 93 (58) | 61% | 68% | -11.4% (-27.4% to +4.4%) | 109 (70) | -3.9% (-4.7% to -3.2%) | -0.5% (-1.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 65 | 55 (34) | 73% | 61% | +10.8% (-7.2% to +27.3%) | 55 (34) | -5.5% (-6.2% to -4.9%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 65 | 55 (34) | 73% | 61% | +10.8% (-7.2% to +27.3%) | 55 (34) | -5.5% (-6.2% to -4.9%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 66 | 52 (33) | 63% | 68% | -8.5% (-29.8% to +12.0%) | 60 (39) | -4.0% (-5.0% to -3.0%) | -0.5% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 66 | 52 (33) | 63% | 68% | -8.5% (-29.8% to +12.0%) | 60 (39) | -4.0% (-5.0% to -3.0%) | -0.5% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| chance = 30-40% | 65 | 43 (34) | 37% | 38% | +2.3% (-32.6% to +39.5%) | 55 (44) | +4.7% (+3.5% to +6.0%) | +1.2% (-0.2% to +2.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 205 | 40 (22) | 42% | 48% | -1.1% (-36.1% to +36.6%) | 127 (49) | +6.3% (+5.0% to +7.7%) | -2.3% (-3.6% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 10-20% | 129 | 0 (0) | – | – | – (–) | 68 (25) | +7.4% (+5.7% to +9.5%) | -0.9% (-2.3% to +0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 71 | 0 (0) | – | – | – (–) | 43 (22) | +6.0% (+4.7% to +7.3%) | -1.5% (-2.3% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, sport = nfl | 39 | 0 (0) | – | – | – (–) | 26 (14) | -5.5% (-6.1% to -4.8%) | -0.7% (-1.3% to -0.1%) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 229 | 0 (0) | – | – | – (–) | 129 (28) | +6.5% (+5.4% to +7.7%) | -1.5% (-2.6% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 240 | 0 (0) | – | – | – (–) | 136 (28) | +6.2% (+5.1% to +7.4%) | -1.7% (-2.7% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 229 | 0 (0) | – | – | – (–) | 129 (28) | +6.5% (+5.4% to +7.7%) | -1.5% (-2.6% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 279 | 0 (0) | – | – | – (–) | 162 (28) | +4.3% (+3.1% to +5.6%) | -1.5% (-2.4% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 229 | 0 (0) | – | – | – (–) | 129 (28) | +6.5% (+5.4% to +7.7%) | -1.5% (-2.6% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 20 | 0 (0) | – | – | – (–) | 14 (10) | -3.9% (-4.7% to -3.1%) | -0.7% (-1.6% to +0.2%) | hypothesis |
| sport = nfl, stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| sport = nfl, stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 229 | 0 (0) | – | – | – (–) | 129 (28) | +6.5% (+5.4% to +7.7%) | -1.5% (-2.6% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
