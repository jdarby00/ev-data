# Research lab report

Built 2026-11-28T11:11:02Z UTC from 12055 logged code candidates (11221 settled, 4193 with a close, 180 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 9104, ROI -5.1%; CLV n 2026 over 164 games, -8.8%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 403, ROI -9.0%; CLV n 552 over 156 games, +2.8%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1714, ROI -0.4%; CLV n 1615 over 145 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 11221, ROI -4.5%; CLV n 4001 over 146 games, -5.0%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 190 over 32 games, +4.4%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 3867, ROI -5.6%; CLV n 1726 over 164 games, -8.7%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 134, ROI +2.3%; CLV n 126 over 81 games, -2.4%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1983, ROI -2.3%; CLV n 2041 over 177 games, -0.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 5237, ROI -4.8%; CLV n 300 over 117 games, -9.3%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.0%; CLV n 127 over 84 games, -3.8%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1291, ROI -1.9%; CLV n 700 over 142 games, -4.9%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1812, ROI -9.0%; CLV n 1272 over 145 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 2074, ROI -3.8%; CLV n 536 over 138 games, -3.2%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1676, ROI -3.0%; CLV n 720 over 141 games, -4.3%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 202, ROI +8.4%; CLV n 202 over 94 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 57, ROI +9.5%; CLV n 57 over 36 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1353, ROI -3.5%; CLV n 310 over 120 games, -4.3%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 764, ROI -8.5%; CLV n 61 over 44 games, -7.6%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 155 over 32 games, +6.4%)
- **stat/market = pa**: IN-SAMPLE SIGNAL: negative ROI (settled 836, ROI -4.2%; CLV n 8 over 8 games, -15.4%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 1046, ROI -5.2%; CLV n 25 over 17 games, -20.7%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 67, ROI -8.5%; CLV n 75 over 50 games, -3.9%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 2439, ROI -1.8%; CLV n 2316 over 157 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 8672, ROI -5.2%; CLV n 1595 over 152 games, -7.2%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -12.4%; CLV n 52 over 34 games, -3.8%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 155 over 32 games, +6.4%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 9688, ROI -4.2%; CLV n 2540 over 156 games, -6.2%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1533, ROI -6.6%; CLV n 1653 over 178 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 6690, ROI -5.0%; CLV n 753 over 157 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 1125, ROI -2.8%; CLV n 1020 over 142 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 934, ROI -1.8%; CLV n 1091 over 176 games, +1.1%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 2472, ROI -5.1%; CLV n 1329 over 146 games, -8.1%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 5593, ROI -5.2%; CLV n 1956 over 160 games, -8.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 1287, ROI -2.8%; CLV n 1182 over 144 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 49, ROI +0.2%; CLV n 63 over 51 games, +4.5%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 80 over 29 games, +7.2%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 53 over 26 games, +5.8%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 3461, ROI -5.0%; CLV n 70 over 48 games, -7.2%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 9094, ROI -5.2%; CLV n 2016 over 164 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 361, ROI -10.7%; CLV n 403 over 146 games, +1.6%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1721, ROI -0.2%; CLV n 1622 over 145 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 45, ROI +6.8%; CLV n 152 over 58 games, +6.0%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1465, ROI -6.7%; CLV n 808 over 128 games, -3.4%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 6275, ROI -3.1%; CLV n 1807 over 150 games, -5.5%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 3481, ROI -6.1%; CLV n 1578 over 171 games, -4.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3746, ROI -7.0%; CLV n 1599 over 178 games, -4.1%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 7475, ROI -3.3%; CLV n 2594 over 146 games, -4.9%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 10367, ROI -5.3%; CLV n 3387 over 180 games, -5.1%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 854, ROI +4.5%; CLV n 806 over 85 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 403, ROI -9.0%; CLV n 390 over 124 games, +1.4%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1714, ROI -0.4%; CLV n 1615 over 145 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 9104, ROI -5.1%; CLV n 1996 over 146 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 162 over 32 games, +6.1%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 67, ROI -8.5%; CLV n 75 over 50 games, -3.9%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: negative ROI (settled 185, ROI -14.6%; CLV n 177 over 90 games, +0.7%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 218, ROI -4.3%; CLV n 220 over 100 games, +2.0%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1348, ROI +0.8%; CLV n 1252 over 142 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 366, ROI -4.8%; CLV n 363 over 110 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 906, ROI -2.9%; CLV n 887 over 153 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -12.4%; CLV n 52 over 34 games, -3.8%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 8088, ROI -5.3%; CLV n 1012 over 142 games, -11.3%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 155 over 32 games, +6.4%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1291, ROI -1.9%; CLV n 700 over 142 games, -4.9%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1812, ROI -9.0%; CLV n 1272 over 145 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 2074, ROI -3.8%; CLV n 536 over 138 games, -3.2%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1676, ROI -3.0%; CLV n 720 over 141 games, -4.3%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 202, ROI +8.4%; CLV n 202 over 94 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.0%; CLV n 110 over 71 games, -3.9%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 57, ROI +9.5%; CLV n 57 over 36 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1353, ROI -3.5%; CLV n 310 over 120 games, -4.3%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 764, ROI -8.5%; CLV n 61 over 44 games, -7.6%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 155 over 32 games, +6.4%)
- **sport = nba, stat/market = pa**: IN-SAMPLE SIGNAL: negative ROI (settled 836, ROI -4.2%; CLV n 8 over 8 games, -15.4%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 1046, ROI -5.2%; CLV n 25 over 17 games, -20.7%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 12055 | 11221 (148) | 64% | 64% | -4.5% (-6.1% to -2.8%) | 4193 (180) | -4.5% (-4.8% to -4.3%) | -0.2% (-0.4% to -0.1%) |  |
| sport = nba | 11745 | 11221 (148) | 64% | 64% | -4.5% (-6.1% to -2.8%) | 4001 (146) | -5.0% (-5.2% to -4.7%) | -0.1% (-0.3% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 11172 | 10367 (147) | 65% | 65% | -5.3% (-7.1% to -3.5%) | 3387 (180) | -5.1% (-5.4% to -4.7%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 10163 | 9688 (148) | 66% | 66% | -4.2% (-6.1% to -2.4%) | 2540 (156) | -6.2% (-6.5% to -5.8%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 9602 | 9104 (148) | 68% | 67% | -5.1% (-7.0% to -3.2%) | 2026 (164) | -8.8% (-9.1% to -8.5%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 9558 | 9104 (148) | 68% | 67% | -5.1% (-7.0% to -3.2%) | 1996 (146) | -8.8% (-9.2% to -8.5%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 9592 | 9094 (148) | 68% | 67% | -5.2% (-7.0% to -3.3%) | 2016 (164) | -8.8% (-9.1% to -8.5%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 9091 | 8672 (147) | 66% | 66% | -5.2% (-7.4% to -3.0%) | 1595 (152) | -7.2% (-7.7% to -6.7%) | -0.5% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 8484 | 8088 (141) | 68% | 68% | -5.3% (-7.5% to -3.1%) | 1012 (142) | -11.3% (-11.8% to -10.8%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 7771 | 7475 (148) | 64% | 64% | -3.3% (-5.3% to -1.3%) | 2594 (146) | -4.9% (-5.2% to -4.6%) | +0.0% (-0.1% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 7085 | 6690 (144) | 70% | 69% | -5.0% (-7.0% to -2.9%) | 753 (157) | -9.5% (-10.0% to -9.1%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 6842 | 6275 (127) | 67% | 65% | -3.1% (-5.2% to -1.1%) | 1807 (150) | -5.5% (-5.9% to -5.0%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 5897 | 5593 (148) | 64% | 64% | -5.2% (-7.3% to -3.0%) | 1956 (160) | -8.8% (-9.2% to -8.5%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 5512 | 5237 (135) | 71% | 71% | -4.8% (-6.8% to -2.8%) | 300 (117) | -9.3% (-10.0% to -8.6%) | -0.7% (-1.1% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 4090 | 3867 (148) | 62% | 62% | -5.6% (-7.9% to -3.1%) | 1726 (164) | -8.7% (-9.0% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 4284 | 3746 (145) | 63% | 65% | -7.0% (-9.8% to -4.1%) | 1599 (178) | -4.1% (-4.5% to -3.6%) | -0.6% (-0.8% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 3687 | 3481 (147) | 61% | 63% | -6.1% (-8.8% to -3.4%) | 1578 (171) | -4.1% (-4.5% to -3.8%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 3650 | 3461 (121) | 73% | 73% | -5.0% (-7.0% to -3.0%) | 70 (48) | -7.2% (-8.6% to -6.0%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 2575 | 2472 (148) | 61% | 61% | -5.1% (-7.6% to -2.5%) | 1329 (146) | -8.1% (-8.4% to -7.7%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2569 | 2439 (148) | 55% | 55% | -1.8% (-5.8% to +2.2%) | 2316 (157) | -3.5% (-3.8% to -3.2%) | +0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 2159 | 2074 (147) | 64% | 63% | -3.8% (-6.6% to -1.0%) | 536 (138) | -3.2% (-3.7% to -2.9%) | +0.3% (+0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 2159 | 2074 (147) | 64% | 63% | -3.8% (-6.6% to -1.0%) | 536 (138) | -3.2% (-3.7% to -2.9%) | +0.3% (+0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 2316 | 1983 (147) | 47% | 49% | -2.3% (-7.1% to +2.4%) | 2041 (177) | -0.5% (-0.8% to -0.2%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1893 | 1812 (148) | 60% | 62% | -9.0% (-11.6% to -6.5%) | 1272 (145) | -5.7% (-6.0% to -5.5%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1893 | 1812 (148) | 60% | 62% | -9.0% (-11.6% to -6.5%) | 1272 (145) | -5.7% (-6.0% to -5.5%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1779 | 1721 (147) | 50% | 50% | -0.2% (-5.6% to +5.3%) | 1622 (145) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1772 | 1714 (147) | 50% | 50% | -0.4% (-5.7% to +5.1%) | 1615 (145) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1772 | 1714 (147) | 50% | 50% | -0.4% (-5.7% to +5.1%) | 1615 (145) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1735 | 1676 (145) | 62% | 61% | -3.0% (-6.4% to +0.2%) | 720 (141) | -4.3% (-4.8% to -3.8%) | +0.2% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1735 | 1676 (145) | 62% | 61% | -3.0% (-6.4% to +0.2%) | 720 (141) | -4.3% (-4.8% to -3.8%) | +0.2% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1892 | 1533 (148) | 50% | 53% | -6.6% (-11.0% to -2.0%) | 1653 (178) | -2.1% (-2.4% to -1.8%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1526 | 1465 (123) | 58% | 60% | -6.7% (-10.3% to -2.8%) | 808 (128) | -3.4% (-3.7% to -3.0%) | -0.4% (-0.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1419 | 1353 (142) | 65% | 65% | -3.5% (-6.5% to -0.4%) | 310 (120) | -4.3% (-4.8% to -3.8%) | +0.3% (+0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1419 | 1353 (142) | 65% | 65% | -3.5% (-6.5% to -0.4%) | 310 (120) | -4.3% (-4.8% to -3.8%) | +0.3% (+0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1394 | 1348 (144) | 51% | 51% | +0.8% (-5.2% to +7.0%) | 1252 (142) | -1.9% (-2.2% to -1.6%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1361 | 1291 (147) | 62% | 61% | -1.9% (-5.7% to +1.8%) | 700 (142) | -4.9% (-5.4% to -4.5%) | -0.3% (-0.7% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1361 | 1291 (147) | 62% | 61% | -1.9% (-5.7% to +1.8%) | 700 (142) | -4.9% (-5.4% to -4.5%) | -0.3% (-0.7% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1337 | 1287 (142) | 51% | 53% | -2.8% (-8.5% to +3.1%) | 1182 (144) | -2.1% (-2.3% to -1.8%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 1168 | 1125 (142) | 50% | 53% | -2.8% (-8.8% to +3.6%) | 1020 (142) | -2.4% (-2.6% to -2.1%) | +0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 1097 | 1046 (120) | 69% | 68% | -5.2% (-8.7% to -1.6%) | 25 (17) | -20.7% (-22.5% to -18.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 1097 | 1046 (120) | 69% | 68% | -5.2% (-8.7% to -1.6%) | 25 (17) | -20.7% (-22.5% to -18.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 1227 | 934 (147) | 44% | 46% | -1.8% (-7.9% to +4.4%) | 1091 (176) | +1.1% (+0.7% to +1.5%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 978 | 906 (148) | 64% | 62% | -2.9% (-7.8% to +1.8%) | 887 (153) | -6.6% (-6.9% to -6.4%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 883 | 854 (87) | 56% | 53% | +4.5% (-1.1% to +9.8%) | 806 (85) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pa | 877 | 836 (121) | 70% | 69% | -4.2% (-7.9% to -0.7%) | 8 (8) | -15.4% (8 games) | -4.4% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pa | 877 | 836 (121) | 70% | 69% | -4.2% (-7.9% to -0.7%) | 8 (8) | -15.4% (8 games) | -4.4% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| chance = 40-50% | 821 | 781 (146) | 45% | 46% | -0.9% (-7.7% to +5.7%) | 789 (150) | -0.0% (-0.4% to +0.3%) | +0.4% (+0.1% to +0.8%) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 803 | 764 (128) | 66% | 68% | -8.5% (-13.6% to -3.5%) | 61 (44) | -7.6% (-10.2% to -5.1%) | -2.5% (-3.9% to -1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 803 | 764 (128) | 66% | 68% | -8.5% (-13.6% to -3.5%) | 61 (44) | -7.6% (-10.2% to -5.1%) | -2.5% (-3.9% to -1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 681 | 403 (127) | 42% | 48% | -9.0% (-18.5% to -0.7%) | 552 (156) | +2.8% (+2.2% to +3.4%) | -1.5% (-1.9% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 415 | 403 (127) | 42% | 48% | -9.0% (-18.5% to -0.7%) | 390 (124) | +1.4% (+0.9% to +2.0%) | -1.4% (-1.8% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 378 | 366 (110) | 46% | 49% | -4.8% (-16.3% to +7.5%) | 363 (110) | -1.4% (-1.8% to -0.9%) | +0.5% (+0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 455 | 361 (124) | 41% | 48% | -10.7% (-20.0% to -1.7%) | 403 (146) | +1.6% (+1.1% to +2.1%) | -1.2% (-1.6% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 229 | 218 (98) | 42% | 46% | -4.3% (-18.1% to +10.3%) | 220 (100) | +2.0% (+1.3% to +2.6%) | -1.8% (-2.5% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 218 | 202 (94) | 71% | 63% | +8.4% (-1.6% to +17.5%) | 202 (94) | -5.7% (-6.1% to -5.3%) | -0.6% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 218 | 202 (94) | 71% | 63% | +8.4% (-1.6% to +17.5%) | 202 (94) | -5.7% (-6.1% to -5.3%) | -0.6% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 197 | 185 (87) | 41% | 50% | -14.6% (-28.4% to -0.8%) | 177 (90) | +0.7% (-0.1% to +1.6%) | -1.0% (-1.7% to -0.2%) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Lean | 137 | 134 (83) | 57% | 57% | +2.3% (-10.6% to +15.1%) | 126 (81) | -2.4% (-3.1% to -1.7%) | -0.7% (-1.3% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 116 | 110 (71) | 63% | 68% | -10.0% (-24.4% to +3.9%) | 110 (71) | -3.9% (-4.7% to -3.0%) | -0.5% (-1.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 140 | 110 (71) | 63% | 68% | -10.0% (-24.4% to +3.9%) | 127 (84) | -3.8% (-4.5% to -3.1%) | -0.4% (-1.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 78 | 67 (44) | 64% | 68% | -8.5% (-27.1% to +9.2%) | 75 (50) | -3.9% (-4.7% to -3.1%) | -0.5% (-1.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 78 | 67 (44) | 64% | 68% | -8.5% (-27.1% to +9.2%) | 75 (50) | -3.9% (-4.7% to -3.1%) | -0.5% (-1.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 67 | 57 (36) | 72% | 61% | +9.5% (-8.1% to +25.6%) | 57 (36) | -5.6% (-6.3% to -4.9%) | -1.0% (-1.6% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 67 | 57 (36) | 72% | 61% | +9.5% (-8.1% to +25.6%) | 57 (36) | -5.6% (-6.3% to -4.9%) | -1.0% (-1.6% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| chance = 30-40% | 73 | 49 (39) | 37% | 38% | +0.2% (-32.3% to +35.1%) | 63 (51) | +4.5% (+3.3% to +5.7%) | +1.2% (-0.1% to +2.5%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 6%+ | 229 | 45 (27) | 47% | 48% | +6.8% (-24.1% to +40.0%) | 152 (58) | +6.0% (+4.9% to +7.2%) | -2.4% (-3.5% to -1.3%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 62 | 43 (27) | 60% | 67% | -12.4% (-38.0% to +11.2%) | 52 (34) | -3.8% (-4.9% to -2.5%) | -0.4% (-1.5% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 62 | 43 (27) | 60% | 67% | -12.4% (-38.0% to +11.2%) | 52 (34) | -3.8% (-4.9% to -2.5%) | -0.4% (-1.5% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 141 | 0 (0) | – | – | – (–) | 80 (29) | +7.2% (+5.6% to +8.9%) | -1.3% (-2.6% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 81 | 0 (0) | – | – | – (–) | 53 (26) | +5.8% (+4.7% to +6.9%) | -1.7% (-2.4% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, sport = nfl | 41 | 0 (0) | – | – | – (–) | 28 (16) | -5.4% (-6.1% to -4.7%) | -0.7% (-1.2% to -0.1%) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 255 | 0 (0) | – | – | – (–) | 155 (32) | +6.4% (+5.4% to +7.4%) | -1.7% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 266 | 0 (0) | – | – | – (–) | 162 (32) | +6.1% (+5.1% to +7.1%) | -1.8% (-2.6% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 255 | 0 (0) | – | – | – (–) | 155 (32) | +6.4% (+5.4% to +7.4%) | -1.7% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 307 | 0 (0) | – | – | – (–) | 190 (32) | +4.4% (+3.4% to +5.5%) | -1.6% (-2.3% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 255 | 0 (0) | – | – | – (–) | 155 (32) | +6.4% (+5.4% to +7.4%) | -1.7% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 21 | 0 (0) | – | – | – (–) | 15 (11) | -3.8% (-4.6% to -3.0%) | -0.6% (-1.5% to +0.3%) | hypothesis |
| sport = nfl, stat/market = pass_tds | 11 | 0 (0) | – | – | – (–) | 7 (7) | -6.4% (7 games) | -0.0% (7 games) | hypothesis |
| sport = nfl, stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 255 | 0 (0) | – | – | – (–) | 155 (32) | +6.4% (+5.4% to +7.4%) | -1.7% (-2.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 11 | 0 (0) | – | – | – (–) | 7 (7) | -6.4% (7 games) | -0.0% (7 games) | hypothesis |
| stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| stat/market = rush_att | 4 | 0 (0) | – | – | – (–) | 3 (3) | -1.9% (3 games) | -6.4% (3 games) | hypothesis |
