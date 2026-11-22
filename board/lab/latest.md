# Research lab report

Built 2026-11-22T19:35:51Z UTC from 9199 logged code candidates (7942 settled, 3125 with a close, 131 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 6302, ROI -4.4%; CLV n 1456 over 120 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 317, ROI -5.8%; CLV n 417 over 117 games, +2.8%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1323, ROI -2.2%; CLV n 1252 over 105 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 7942, ROI -4.1%; CLV n 2992 over 106 games, -4.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 131 over 23 games, +3.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2672, ROI -4.5%; CLV n 1240 over 120 games, -8.5%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -2.9%; CLV n 93 over 58 games, -2.7%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -2.9%; CLV n 1576 over 128 games, -0.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 3630, ROI -4.3%; CLV n 216 over 84 games, -9.6%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 79, ROI -2.7%; CLV n 93 over 59 games, -3.8%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 894, ROI +0.2%; CLV n 497 over 104 games, -4.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -8.8%; CLV n 915 over 106 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1483, ROI -4.8%; CLV n 419 over 99 games, -3.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1185, ROI -1.6%; CLV n 547 over 101 games, -4.0%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 171, ROI +9.2%; CLV n 171 over 77 games, -5.8%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 946, ROI -3.6%; CLV n 243 over 88 games, -4.2%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 532, ROI -9.6%; CLV n 49 over 34 games, -7.8%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 102 over 23 games, +6.3%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 724, ROI -5.0%; CLV n 19 over 13 games, -20.1%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 46, ROI -5.8%; CLV n 54 over 35 games, -3.7%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1879, ROI -1.8%; CLV n 1784 over 115 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5984, ROI -4.8%; CLV n 1146 over 111 games, -6.7%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 102 over 23 games, +6.3%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 6736, ROI -3.6%; CLV n 1835 over 115 games, -5.9%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1206, ROI -6.9%; CLV n 1290 over 129 games, -2.2%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 4582, ROI -4.4%; CLV n 544 over 115 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 869, ROI -6.0%; CLV n 791 over 102 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 727, ROI -0.0%; CLV n 835 over 128 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1764, ROI -4.1%; CLV n 955 over 106 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 3854, ROI -4.7%; CLV n 1409 over 117 games, -8.7%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 995, ROI -5.3%; CLV n 919 over 104 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +8.2%; CLV n 49 over 38 games, +4.9%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 50 over 21 games, +7.1%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 36 over 19 games, +6.1%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2398, ROI -3.8%; CLV n 47 over 32 games, -8.0%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 6292, ROI -4.5%; CLV n 1446 over 120 games, -8.7%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 282, ROI -6.6%; CLV n 314 over 109 games, +1.8%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1330, ROI -2.0%; CLV n 1259 over 105 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +4.1%; CLV n 106 over 43 games, +5.8%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1117, ROI -5.8%; CLV n 644 over 98 games, -3.2%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 4253, ROI -3.2%; CLV n 1261 over 106 games, -5.4%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2572, ROI -4.8%; CLV n 1220 over 123 games, -4.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2727, ROI -5.9%; CLV n 1238 over 130 games, -4.0%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 5215, ROI -3.1%; CLV n 1887 over 106 games, -4.6%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 7254, ROI -5.1%; CLV n 2478 over 131 games, -4.9%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 688, ROI +6.3%; CLV n 647 over 62 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 317, ROI -5.8%; CLV n 309 over 94 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1323, ROI -2.2%; CLV n 1252 over 105 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 6302, ROI -4.4%; CLV n 1431 over 106 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 108 over 23 games, +5.9%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 46, ROI -5.8%; CLV n 54 over 35 games, -3.7%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 137, ROI -10.4%; CLV n 133 over 70 games, +0.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 180, ROI -2.2%; CLV n 182 over 78 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1030, ROI -1.5%; CLV n 958 over 104 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 293, ROI -5.0%; CLV n 294 over 83 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -0.6%; CLV n 693 over 112 games, -6.7%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5511, ROI -4.9%; CLV n 670 over 102 games, -11.5%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 102 over 23 games, +6.3%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 894, ROI +0.2%; CLV n 497 over 104 games, -4.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -8.8%; CLV n 915 over 106 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1483, ROI -4.8%; CLV n 419 over 99 games, -3.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1185, ROI -1.6%; CLV n 547 over 101 games, -4.0%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 171, ROI +9.2%; CLV n 171 over 77 games, -5.8%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 79, ROI -2.7%; CLV n 79 over 49 games, -3.7%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 946, ROI -3.6%; CLV n 243 over 88 games, -4.2%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 532, ROI -9.6%; CLV n 49 over 34 games, -7.8%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 102 over 23 games, +6.3%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 724, ROI -5.0%; CLV n 19 over 13 games, -20.1%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 9199 | 7942 (108) | 64% | 64% | -4.1% (-6.2% to -2.0%) | 3125 (131) | -4.4% (-4.7% to -4.0%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 8927 | 7942 (108) | 64% | 64% | -4.1% (-6.2% to -2.0%) | 2992 (106) | -4.8% (-5.1% to -4.5%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 8462 | 7254 (107) | 65% | 65% | -5.1% (-7.5% to -2.9%) | 2478 (131) | -4.9% (-5.3% to -4.5%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 7641 | 6736 (108) | 66% | 65% | -3.6% (-5.9% to -1.4%) | 1835 (115) | -5.9% (-6.3% to -5.5%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 7199 | 6302 (108) | 68% | 67% | -4.4% (-6.6% to -2.1%) | 1456 (120) | -8.7% (-9.1% to -8.3%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 7159 | 6302 (108) | 68% | 67% | -4.4% (-6.6% to -2.1%) | 1431 (106) | -8.8% (-9.2% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 7189 | 6292 (108) | 68% | 67% | -4.5% (-6.8% to -2.3%) | 1446 (120) | -8.7% (-9.2% to -8.3%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 6793 | 5984 (107) | 67% | 66% | -4.8% (-7.6% to -2.1%) | 1146 (111) | -6.7% (-7.3% to -6.0%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 6284 | 5511 (101) | 68% | 68% | -4.9% (-7.5% to -2.2%) | 670 (102) | -11.5% (-12.1% to -10.9%) | -0.9% (-1.2% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 5871 | 5215 (108) | 64% | 63% | -3.1% (-5.7% to -0.7%) | 1887 (106) | -4.6% (-5.0% to -4.3%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 5278 | 4582 (104) | 70% | 69% | -4.4% (-6.7% to -2.0%) | 544 (115) | -9.5% (-10.1% to -9.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 5125 | 4253 (89) | 67% | 65% | -3.2% (-6.1% to -0.5%) | 1261 (106) | -5.4% (-5.9% to -4.8%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 4400 | 3854 (108) | 64% | 64% | -4.7% (-7.5% to -2.0%) | 1409 (117) | -8.7% (-9.1% to -8.3%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 4142 | 3630 (95) | 72% | 71% | -4.3% (-6.8% to -1.9%) | 216 (84) | -9.6% (-10.5% to -8.7%) | -0.8% (-1.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3328 | 2727 (106) | 63% | 64% | -5.9% (-9.3% to -2.7%) | 1238 (130) | -4.0% (-4.5% to -3.5%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 3057 | 2672 (108) | 63% | 62% | -4.5% (-7.3% to -1.5%) | 1240 (120) | -8.5% (-8.9% to -8.2%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 2887 | 2572 (107) | 62% | 62% | -4.8% (-7.8% to -2.0%) | 1220 (123) | -4.0% (-4.4% to -3.5%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2744 | 2398 (81) | 74% | 73% | -3.8% (-6.1% to -1.4%) | 47 (32) | -8.0% (-9.9% to -6.3%) | +0.2% (-0.5% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2070 | 1879 (108) | 55% | 55% | -1.8% (-6.1% to +2.7%) | 1784 (115) | -3.5% (-3.9% to -3.2%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1965 | 1764 (108) | 62% | 61% | -4.1% (-7.2% to -1.1%) | 955 (106) | -8.0% (-8.3% to -7.6%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1895 | 1541 (107) | 47% | 49% | -2.9% (-8.3% to +2.7%) | 1576 (128) | -0.5% (-0.8% to -0.2%) | +0.2% (-0.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1655 | 1483 (107) | 63% | 63% | -4.8% (-8.3% to -1.3%) | 419 (99) | -3.0% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1655 | 1483 (107) | 63% | 63% | -4.8% (-8.3% to -1.3%) | 419 (99) | -3.0% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1433 | 1330 (107) | 49% | 50% | -2.0% (-8.2% to +4.3%) | 1259 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1426 | 1323 (107) | 49% | 50% | -2.2% (-8.6% to +4.1%) | 1252 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1426 | 1323 (107) | 49% | 50% | -2.2% (-8.6% to +4.1%) | 1252 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1442 | 1305 (108) | 60% | 62% | -8.8% (-12.0% to -5.6%) | 915 (106) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1442 | 1305 (108) | 60% | 62% | -8.8% (-12.0% to -5.6%) | 915 (106) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1558 | 1206 (108) | 50% | 53% | -6.9% (-12.0% to -1.7%) | 1290 (129) | -2.2% (-2.5% to -1.8%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1327 | 1185 (105) | 62% | 61% | -1.6% (-5.9% to +2.6%) | 547 (101) | -4.0% (-4.5% to -3.4%) | +0.2% (-0.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1327 | 1185 (105) | 62% | 61% | -1.6% (-5.9% to +2.6%) | 547 (101) | -4.0% (-4.5% to -3.4%) | +0.2% (-0.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1187 | 1117 (96) | 58% | 60% | -5.8% (-10.1% to -1.3%) | 644 (98) | -3.2% (-3.6% to -2.8%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1113 | 1030 (106) | 49% | 51% | -1.5% (-8.4% to +5.1%) | 958 (104) | -1.9% (-2.2% to -1.5%) | +0.7% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1079 | 995 (103) | 49% | 53% | -5.3% (-11.9% to +1.1%) | 919 (104) | -2.1% (-2.4% to -1.8%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1065 | 946 (102) | 65% | 64% | -3.6% (-7.5% to +0.2%) | 243 (88) | -4.2% (-4.8% to -3.7%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1065 | 946 (102) | 65% | 64% | -3.6% (-7.5% to +0.2%) | 243 (88) | -4.2% (-4.8% to -3.7%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1015 | 894 (107) | 62% | 60% | +0.2% (-4.5% to +4.8%) | 497 (104) | -4.4% (-4.9% to -3.8%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1015 | 894 (107) | 62% | 60% | +0.2% (-4.5% to +4.8%) | 497 (104) | -4.4% (-4.9% to -3.8%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 943 | 869 (103) | 49% | 52% | -6.0% (-13.0% to +0.7%) | 791 (102) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 1013 | 727 (107) | 45% | 46% | -0.0% (-7.4% to +7.2%) | 835 (128) | +1.2% (+0.8% to +1.6%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pr | 822 | 724 (80) | 69% | 68% | -5.0% (-9.3% to -1.1%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 822 | 724 (80) | 69% | 68% | -5.0% (-9.3% to -1.1%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = likely, side = under | 801 | 712 (108) | 65% | 62% | -0.6% (-5.9% to +4.7%) | 693 (112) | -6.7% (-7.0% to -6.3%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 737 | 688 (64) | 57% | 53% | +6.3% (-0.7% to +12.4%) | 647 (62) | -2.4% (-2.7% to -2.0%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 666 | 607 (106) | 45% | 46% | +0.3% (-7.2% to +8.0%) | 615 (109) | +0.1% (-0.3% to +0.5%) | +0.5% (+0.1% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 646 | 576 (81) | 70% | 69% | -3.1% (-7.5% to +0.9%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 646 | 576 (81) | 70% | 69% | -3.1% (-7.5% to +0.9%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 611 | 532 (88) | 65% | 68% | -9.6% (-15.9% to -3.6%) | 49 (34) | -7.8% (-10.7% to -4.9%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 611 | 532 (88) | 65% | 68% | -9.6% (-15.9% to -3.6%) | 49 (34) | -7.8% (-10.7% to -4.9%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 574 | 317 (97) | 43% | 48% | -5.8% (-16.0% to +4.2%) | 417 (117) | +2.8% (+2.2% to +3.5%) | -1.5% (-1.9% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 342 | 317 (97) | 43% | 48% | -5.8% (-16.0% to +4.2%) | 309 (94) | +1.7% (+1.1% to +2.3%) | -1.3% (-1.7% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 313 | 293 (83) | 46% | 49% | -5.0% (-18.5% to +8.9%) | 294 (83) | -1.4% (-1.9% to -0.8%) | +0.6% (+0.1% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 378 | 282 (95) | 43% | 48% | -6.6% (-16.7% to +3.5%) | 314 (109) | +1.8% (+1.2% to +2.3%) | -1.0% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 196 | 180 (77) | 43% | 46% | -2.2% (-18.0% to +14.1%) | 182 (78) | +2.2% (+1.5% to +3.0%) | -1.7% (-2.4% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 192 | 171 (77) | 71% | 63% | +9.2% (-1.2% to +19.6%) | 171 (77) | -5.8% (-6.2% to -5.3%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 192 | 171 (77) | 71% | 63% | +9.2% (-1.2% to +19.6%) | 171 (77) | -5.8% (-6.2% to -5.3%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 156 | 137 (67) | 43% | 50% | -10.4% (-27.0% to +6.5%) | 133 (70) | +0.9% (+0.1% to +1.9%) | -0.9% (-1.7% to -0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 105 | 99 (59) | 55% | 57% | -2.9% (-16.4% to +11.1%) | 93 (58) | -2.7% (-3.6% to -1.9%) | -1.1% (-1.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 92 | 79 (49) | 67% | 67% | -2.7% (-20.2% to +13.9%) | 79 (49) | -3.7% (-4.7% to -2.7%) | -0.3% (-1.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 114 | 79 (49) | 67% | 67% | -2.7% (-20.2% to +13.9%) | 93 (59) | -3.8% (-4.7% to -2.8%) | -0.3% (-1.2% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 60 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 60 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 59 | 46 (29) | 65% | 68% | -5.8% (-28.0% to +16.5%) | 54 (35) | -3.7% (-4.8% to -2.8%) | -0.3% (-1.4% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 59 | 46 (29) | 65% | 68% | -5.8% (-28.0% to +16.5%) | 54 (35) | -3.7% (-4.8% to -2.8%) | -0.3% (-1.4% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 60 | 38 (29) | 39% | 38% | +8.2% (-28.3% to +48.0%) | 49 (38) | +4.9% (+3.5% to +6.3%) | +1.2% (-0.4% to +2.8%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 6%+ | 199 | 38 (21) | 45% | 48% | +4.1% (-31.3% to +42.9%) | 106 (43) | +5.8% (+4.4% to +7.2%) | -2.8% (-4.2% to -1.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 55 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 55 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 127 | 0 (0) | – | – | – (–) | 50 (21) | +7.1% (+5.2% to +9.5%) | -1.3% (-2.8% to +0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 68 | 0 (0) | – | – | – (–) | 36 (19) | +6.1% (+4.8% to +7.6%) | -1.5% (-2.4% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, sport = nfl | 37 | 0 (0) | – | – | – (–) | 23 (12) | -5.6% (-6.3% to -4.8%) | -0.9% (-1.5% to -0.1%) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 222 | 0 (0) | – | – | – (–) | 102 (23) | +6.3% (+5.1% to +7.6%) | -1.9% (-3.0% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 232 | 0 (0) | – | – | – (–) | 108 (23) | +5.9% (+4.9% to +7.2%) | -2.0% (-3.0% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 222 | 0 (0) | – | – | – (–) | 102 (23) | +6.3% (+5.1% to +7.6%) | -1.9% (-3.0% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 269 | 0 (0) | – | – | – (–) | 131 (23) | +3.9% (+2.7% to +5.3%) | -1.8% (-2.6% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 222 | 0 (0) | – | – | – (–) | 102 (23) | +6.3% (+5.1% to +7.6%) | -1.9% (-3.0% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 19 | 0 (0) | – | – | – (–) | 12 (8) | -4.1% (8 games) | -0.9% (8 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 9 | 0 (0) | – | – | – (–) | 5 (5) | -6.2% (5 games) | -0.1% (5 games) | hypothesis |
| sport = nfl, stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 3 | 0 (0) | – | – | – (–) | 2 (2) | -1.8% (2 games) | -6.9% (2 games) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 222 | 0 (0) | – | – | – (–) | 102 (23) | +6.3% (+5.1% to +7.6%) | -1.9% (-3.0% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 9 | 0 (0) | – | – | – (–) | 5 (5) | -6.2% (5 games) | -0.1% (5 games) | hypothesis |
| stat/market = receptions | 13 | 0 (0) | – | – | – (–) | 8 (7) | -6.2% (7 games) | -2.0% (7 games) | hypothesis |
| stat/market = rush_att | 3 | 0 (0) | – | – | – (–) | 2 (2) | -1.8% (2 games) | -6.9% (2 games) | hypothesis |
