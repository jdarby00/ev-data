# Research lab report

Built 2026-11-26T19:36:04Z UTC from 11051 logged code candidates (10252 settled, 3875 with a close, 166 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 8259, ROI -4.8%; CLV n 1844 over 151 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 375, ROI -10.0%; CLV n 505 over 143 games, +2.9%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1618, ROI -1.1%; CLV n 1526 over 134 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 10252, ROI -4.4%; CLV n 3704 over 135 games, -4.9%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 169 over 29 games, +4.3%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 3517, ROI -5.1%; CLV n 1574 over 151 games, -8.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 126, ROI +0.2%; CLV n 120 over 75 games, -2.5%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1867, ROI -3.0%; CLV n 1911 over 163 games, -0.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 4742, ROI -4.5%; CLV n 270 over 106 games, -9.3%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -9.7%; CLV n 115 over 75 games, -3.8%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1169, ROI -1.4%; CLV n 636 over 131 games, -4.7%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1661, ROI -9.8%; CLV n 1163 over 134 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1904, ROI -4.1%; CLV n 503 over 127 games, -3.1%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -2.7%; CLV n 676 over 130 games, -4.2%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 192, ROI +10.9%; CLV n 192 over 89 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 56, ROI +11.5%; CLV n 56 over 35 games, -5.5%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1229, ROI -3.4%; CLV n 294 over 111 games, -4.1%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 686, ROI -8.0%; CLV n 55 over 40 games, -7.9%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 29 games, +6.5%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 958, ROI -5.1%; CLV n 22 over 15 games, -20.7%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 58, ROI -5.9%; CLV n 66 over 44 games, -3.7%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 2291, ROI -1.9%; CLV n 2174 over 145 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 7862, ROI -5.0%; CLV n 1450 over 141 games, -7.0%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 29 games, +6.5%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 8806, ROI -3.9%; CLV n 2326 over 145 games, -6.0%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1446, ROI -7.3%; CLV n 1549 over 164 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 6042, ROI -4.9%; CLV n 676 over 144 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 1067, ROI -3.7%; CLV n 967 over 131 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 872, ROI -2.4%; CLV n 1011 over 162 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 2271, ROI -4.2%; CLV n 1221 over 135 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 5078, ROI -4.9%; CLV n 1782 over 147 games, -8.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 1217, ROI -3.9%; CLV n 1119 over 133 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 44, ROI -0.0%; CLV n 57 over 46 games, +4.7%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 71 over 26 games, +7.4%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 44 over 23 games, +6.0%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 3131, ROI -4.4%; CLV n 62 over 44 games, -7.4%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 8249, ROI -4.8%; CLV n 1834 over 151 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 337, ROI -10.4%; CLV n 375 over 133 games, +1.8%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1625, ROI -0.9%; CLV n 1533 over 134 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 41, ROI -3.5%; CLV n 133 over 51 games, +6.1%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1427, ROI -6.5%; CLV n 788 over 122 games, -3.4%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 5541, ROI -3.1%; CLV n 1604 over 138 games, -5.3%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 3284, ROI -5.7%; CLV n 1483 over 157 games, -4.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3438, ROI -5.7%; CLV n 1482 over 164 games, -4.0%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 6814, ROI -3.7%; CLV n 2393 over 135 games, -4.7%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 9434, ROI -5.1%; CLV n 3103 over 166 games, -5.0%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 818, ROI +4.6%; CLV n 772 over 80 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 375, ROI -10.0%; CLV n 362 over 114 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1618, ROI -1.1%; CLV n 1526 over 134 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 8259, ROI -4.8%; CLV n 1816 over 135 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 143 over 29 games, +6.1%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 58, ROI -5.9%; CLV n 66 over 44 games, -3.7%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 173, ROI -14.7%; CLV n 165 over 84 games, +1.0%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 202, ROI -6.0%; CLV n 204 over 92 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1271, ROI +0.0%; CLV n 1181 over 132 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 347, ROI -5.2%; CLV n 345 over 102 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 847, ROI -2.2%; CLV n 828 over 141 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 7313, ROI -5.0%; CLV n 901 over 131 games, -11.3%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 29 games, +6.5%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1169, ROI -1.4%; CLV n 636 over 131 games, -4.7%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1661, ROI -9.8%; CLV n 1163 over 134 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1904, ROI -4.1%; CLV n 503 over 127 games, -3.1%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -2.7%; CLV n 676 over 130 games, -4.2%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 192, ROI +10.9%; CLV n 192 over 89 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -9.7%; CLV n 99 over 63 games, -3.8%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 56, ROI +11.5%; CLV n 56 over 35 games, -5.5%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1229, ROI -3.4%; CLV n 294 over 111 games, -4.1%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 686, ROI -8.0%; CLV n 55 over 40 games, -7.9%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 29 games, +6.5%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 958, ROI -5.1%; CLV n 22 over 15 games, -20.7%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 11051 | 10252 (137) | 64% | 64% | -4.4% (-6.0% to -2.6%) | 3875 (166) | -4.5% (-4.7% to -4.2%) | -0.2% (-0.3% to -0.0%) |  |
| sport = nba | 10753 | 10252 (137) | 64% | 64% | -4.4% (-6.0% to -2.6%) | 3704 (135) | -4.9% (-5.1% to -4.6%) | -0.1% (-0.2% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 10205 | 9434 (136) | 65% | 65% | -5.1% (-7.1% to -3.2%) | 3103 (166) | -5.0% (-5.3% to -4.6%) | -0.2% (-0.4% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 9259 | 8806 (137) | 66% | 66% | -3.9% (-5.9% to -2.0%) | 2326 (145) | -6.0% (-6.4% to -5.7%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 8735 | 8259 (137) | 68% | 67% | -4.8% (-6.8% to -2.8%) | 1844 (151) | -8.7% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 8693 | 8259 (137) | 68% | 67% | -4.8% (-6.8% to -2.8%) | 1816 (135) | -8.8% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 8725 | 8249 (137) | 68% | 67% | -4.8% (-6.8% to -2.9%) | 1834 (151) | -8.8% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 8263 | 7862 (136) | 67% | 66% | -5.0% (-7.4% to -2.6%) | 1450 (141) | -7.0% (-7.6% to -6.5%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 7692 | 7313 (130) | 68% | 68% | -5.0% (-7.3% to -2.8%) | 901 (131) | -11.3% (-11.8% to -10.8%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 7101 | 6814 (137) | 64% | 64% | -3.7% (-5.8% to -1.7%) | 2393 (135) | -4.7% (-5.1% to -4.4%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 6419 | 6042 (133) | 70% | 69% | -4.9% (-6.9% to -2.7%) | 676 (144) | -9.5% (-10.0% to -9.0%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 6089 | 5541 (116) | 67% | 65% | -3.1% (-5.3% to -0.9%) | 1604 (138) | -5.3% (-5.8% to -4.9%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 5365 | 5078 (137) | 64% | 64% | -4.9% (-7.2% to -2.7%) | 1782 (147) | -8.8% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 5007 | 4742 (124) | 72% | 71% | -4.5% (-6.7% to -2.4%) | 270 (106) | -9.3% (-10.1% to -8.6%) | -0.7% (-1.1% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 3728 | 3517 (137) | 63% | 62% | -5.1% (-7.5% to -2.6%) | 1574 (151) | -8.6% (-9.0% to -8.3%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3950 | 3438 (134) | 64% | 64% | -5.7% (-8.5% to -2.9%) | 1482 (164) | -4.0% (-4.5% to -3.5%) | -0.6% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 3477 | 3284 (136) | 62% | 63% | -5.7% (-8.4% to -2.9%) | 1483 (157) | -4.1% (-4.5% to -3.8%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 3315 | 3131 (110) | 74% | 73% | -4.4% (-6.4% to -2.3%) | 62 (44) | -7.4% (-8.9% to -6.1%) | -0.3% (-1.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2415 | 2291 (137) | 55% | 55% | -1.9% (-6.0% to +2.3%) | 2174 (145) | -3.5% (-3.7% to -3.2%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 2370 | 2271 (137) | 62% | 61% | -4.2% (-6.7% to -1.4%) | 1221 (135) | -8.0% (-8.3% to -7.7%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1986 | 1904 (136) | 63% | 63% | -4.1% (-6.9% to -1.2%) | 503 (127) | -3.1% (-3.5% to -2.7%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1986 | 1904 (136) | 63% | 63% | -4.1% (-6.9% to -1.2%) | 503 (127) | -3.1% (-3.5% to -2.7%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 2187 | 1867 (136) | 47% | 49% | -3.0% (-8.0% to +1.9%) | 1911 (163) | -0.5% (-0.8% to -0.2%) | +0.2% (-0.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1734 | 1661 (137) | 59% | 62% | -9.8% (-12.6% to -7.2%) | 1163 (134) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1734 | 1661 (137) | 59% | 62% | -9.8% (-12.6% to -7.2%) | 1163 (134) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1680 | 1625 (136) | 49% | 50% | -0.9% (-6.5% to +4.8%) | 1533 (134) | -1.8% (-2.0% to -1.6%) | +0.6% (+0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1673 | 1618 (136) | 49% | 50% | -1.1% (-6.7% to +4.5%) | 1526 (134) | -1.8% (-2.0% to -1.5%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1673 | 1618 (136) | 49% | 50% | -1.1% (-6.7% to +4.5%) | 1526 (134) | -1.8% (-2.0% to -1.5%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1597 | 1541 (134) | 62% | 61% | -2.7% (-6.3% to +0.9%) | 676 (130) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1597 | 1541 (134) | 62% | 61% | -2.7% (-6.3% to +0.9%) | 676 (130) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1792 | 1446 (137) | 50% | 53% | -7.3% (-11.9% to -2.7%) | 1549 (164) | -2.1% (-2.5% to -1.8%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1485 | 1427 (118) | 58% | 60% | -6.5% (-10.2% to -2.5%) | 788 (122) | -3.4% (-3.7% to -3.0%) | -0.4% (-0.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1315 | 1271 (134) | 50% | 51% | +0.0% (-6.3% to +6.1%) | 1181 (132) | -1.9% (-2.2% to -1.6%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1294 | 1229 (131) | 65% | 64% | -3.4% (-6.6% to -0.0%) | 294 (111) | -4.1% (-4.7% to -3.6%) | +0.3% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1294 | 1229 (131) | 65% | 64% | -3.4% (-6.6% to -0.0%) | 294 (111) | -4.1% (-4.7% to -3.6%) | +0.3% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1265 | 1217 (131) | 50% | 53% | -3.9% (-9.8% to +2.1%) | 1119 (133) | -2.1% (-2.3% to -1.8%) | -0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1236 | 1169 (136) | 62% | 61% | -1.4% (-5.3% to +2.6%) | 636 (131) | -4.7% (-5.1% to -4.2%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1236 | 1169 (136) | 62% | 61% | -1.4% (-5.3% to +2.6%) | 636 (131) | -4.7% (-5.1% to -4.2%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 1108 | 1067 (131) | 50% | 53% | -3.7% (-9.9% to +2.8%) | 967 (131) | -2.4% (-2.6% to -2.1%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 1007 | 958 (109) | 69% | 68% | -5.1% (-8.7% to -1.3%) | 22 (15) | -20.7% (-22.7% to -18.4%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 1007 | 958 (109) | 69% | 68% | -5.1% (-8.7% to -1.3%) | 22 (15) | -20.7% (-22.7% to -18.4%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 1154 | 872 (136) | 44% | 46% | -2.4% (-8.7% to +4.1%) | 1011 (162) | +1.2% (+0.8% to +1.6%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 915 | 847 (137) | 64% | 62% | -2.2% (-7.4% to +2.5%) | 828 (141) | -6.6% (-6.9% to -6.3%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 846 | 818 (82) | 56% | 53% | +4.6% (-1.3% to +10.2%) | 772 (80) | -2.4% (-2.7% to -2.1%) | -0.0% (-0.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pa | 796 | 757 (110) | 71% | 69% | -2.9% (-6.7% to +0.6%) | 8 (8) | -15.4% (8 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 796 | 757 (110) | 71% | 69% | -2.9% (-6.7% to +0.6%) | 8 (8) | -15.4% (8 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| chance = 40-50% | 771 | 732 (135) | 45% | 46% | -1.1% (-7.8% to +5.6%) | 740 (139) | +0.1% (-0.3% to +0.4%) | +0.5% (+0.2% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 724 | 686 (117) | 66% | 68% | -8.0% (-13.1% to -2.8%) | 55 (40) | -7.9% (-10.4% to -5.2%) | -2.1% (-3.7% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 724 | 686 (117) | 66% | 68% | -8.0% (-13.1% to -2.8%) | 55 (40) | -7.9% (-10.4% to -5.2%) | -2.1% (-3.7% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 643 | 375 (117) | 41% | 48% | -10.0% (-19.5% to -1.1%) | 505 (143) | +2.9% (+2.3% to +3.6%) | -1.3% (-1.8% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 387 | 375 (117) | 41% | 48% | -10.0% (-19.5% to -1.1%) | 362 (114) | +1.7% (+1.1% to +2.2%) | -1.2% (-1.7% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 358 | 347 (102) | 46% | 49% | -5.2% (-17.5% to +7.2%) | 345 (102) | -1.4% (-1.8% to -0.9%) | +0.5% (+0.2% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 429 | 337 (114) | 41% | 48% | -10.4% (-20.0% to -1.1%) | 375 (133) | +1.8% (+1.3% to +2.3%) | -0.9% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 213 | 202 (90) | 41% | 46% | -6.0% (-19.6% to +8.8%) | 204 (92) | +2.2% (+1.5% to +2.8%) | -1.7% (-2.4% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 208 | 192 (89) | 72% | 62% | +10.9% (+1.0% to +20.4%) | 192 (89) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 208 | 192 (89) | 72% | 62% | +10.9% (+1.0% to +20.4%) | 192 (89) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 185 | 173 (81) | 41% | 50% | -14.7% (-29.3% to +0.3%) | 165 (84) | +1.0% (+0.2% to +1.8%) | -0.8% (-1.5% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 129 | 126 (76) | 56% | 57% | +0.2% (-12.4% to +13.6%) | 120 (75) | -2.5% (-3.2% to -1.8%) | -0.8% (-1.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 105 | 99 (63) | 63% | 68% | -9.7% (-25.1% to +5.7%) | 99 (63) | -3.8% (-4.7% to -2.9%) | -0.4% (-1.2% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 128 | 99 (63) | 63% | 68% | -9.7% (-25.1% to +5.7%) | 115 (75) | -3.8% (-4.6% to -3.0%) | -0.4% (-1.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 69 | 58 (38) | 66% | 68% | -5.9% (-26.1% to +13.6%) | 66 (44) | -3.7% (-4.7% to -2.9%) | -0.3% (-1.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 69 | 58 (38) | 66% | 68% | -5.9% (-26.1% to +13.6%) | 66 (44) | -3.7% (-4.7% to -2.9%) | -0.3% (-1.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 66 | 56 (35) | 73% | 61% | +11.5% (-6.1% to +27.3%) | 56 (35) | -5.5% (-6.2% to -4.8%) | -0.9% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 66 | 56 (35) | 73% | 61% | +11.5% (-6.1% to +27.3%) | 56 (35) | -5.5% (-6.2% to -4.8%) | -0.9% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| chance = 30-40% | 67 | 44 (35) | 36% | 38% | -0.0% (-35.1% to +36.7%) | 57 (46) | +4.7% (+3.5% to +5.9%) | +1.1% (-0.4% to +2.5%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 6%+ | 217 | 41 (23) | 41% | 48% | -3.5% (-36.6% to +34.1%) | 133 (51) | +6.1% (+4.9% to +7.5%) | -2.4% (-3.6% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 137 | 0 (0) | – | – | – (–) | 71 (26) | +7.4% (+5.6% to +9.3%) | -1.0% (-2.3% to +0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 76 | 0 (0) | – | – | – (–) | 44 (23) | +6.0% (+4.7% to +7.3%) | -1.6% (-2.4% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, sport = nfl | 39 | 0 (0) | – | – | – (–) | 26 (14) | -5.5% (-6.1% to -4.8%) | -0.7% (-1.3% to -0.1%) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 245 | 0 (0) | – | – | – (–) | 136 (29) | +6.5% (+5.4% to +7.6%) | -1.5% (-2.5% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 256 | 0 (0) | – | – | – (–) | 143 (29) | +6.1% (+5.1% to +7.3%) | -1.7% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 245 | 0 (0) | – | – | – (–) | 136 (29) | +6.5% (+5.4% to +7.6%) | -1.5% (-2.5% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 295 | 0 (0) | – | – | – (–) | 169 (29) | +4.3% (+3.2% to +5.6%) | -1.5% (-2.3% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 245 | 0 (0) | – | – | – (–) | 136 (29) | +6.5% (+5.4% to +7.6%) | -1.5% (-2.5% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 20 | 0 (0) | – | – | – (–) | 14 (10) | -3.9% (-4.7% to -3.1%) | -0.7% (-1.6% to +0.2%) | hypothesis |
| sport = nfl, stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| sport = nfl, stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 245 | 0 (0) | – | – | – (–) | 136 (29) | +6.5% (+5.4% to +7.6%) | -1.5% (-2.5% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 10 | 0 (0) | – | – | – (–) | 6 (6) | -6.4% (6 games) | -0.0% (6 games) | hypothesis |
| stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
