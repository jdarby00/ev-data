# Research lab report

Built 2026-11-22T11:10:45Z UTC from 8569 logged code candidates (7942 settled, 3091 with a close, 124 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 6302, ROI -4.4%; CLV n 1449 over 117 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 317, ROI -5.8%; CLV n 390 over 110 games, +2.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1323, ROI -2.2%; CLV n 1252 over 105 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 7942, ROI -4.1%; CLV n 2992 over 106 games, -4.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 97 over 16 games, +3.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2672, ROI -4.5%; CLV n 1233 over 117 games, -8.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -2.9%; CLV n 93 over 58 games, -2.7%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1541, ROI -2.9%; CLV n 1549 over 121 games, -0.6%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 3630, ROI -4.3%; CLV n 216 over 84 games, -9.6%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 79, ROI -2.7%; CLV n 89 over 57 games, -3.8%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 894, ROI +0.2%; CLV n 497 over 104 games, -4.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -8.8%; CLV n 915 over 106 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1483, ROI -4.8%; CLV n 419 over 99 games, -3.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1185, ROI -1.6%; CLV n 547 over 101 games, -4.0%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 171, ROI +9.2%; CLV n 171 over 77 games, -5.8%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 946, ROI -3.6%; CLV n 243 over 88 games, -4.2%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 532, ROI -9.6%; CLV n 49 over 34 games, -7.8%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 724, ROI -5.0%; CLV n 19 over 13 games, -20.1%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 46, ROI -5.8%; CLV n 50 over 33 games, -3.8%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1879, ROI -1.8%; CLV n 1781 over 112 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5984, ROI -4.8%; CLV n 1144 over 109 games, -6.7%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 6736, ROI -3.6%; CLV n 1833 over 113 games, -5.9%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1206, ROI -6.9%; CLV n 1258 over 122 games, -2.3%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 4582, ROI -4.4%; CLV n 537 over 112 games, -9.6%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 869, ROI -6.0%; CLV n 790 over 101 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 727, ROI -0.0%; CLV n 809 over 121 games, +1.0%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1764, ROI -4.1%; CLV n 955 over 106 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 3854, ROI -4.7%; CLV n 1404 over 114 games, -8.7%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 995, ROI -5.3%; CLV n 918 over 103 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +8.2%; CLV n 46 over 35 games, +4.9%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 36 over 14 games, +7.1%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2398, ROI -3.8%; CLV n 45 over 31 games, -8.1%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 6292, ROI -4.5%; CLV n 1439 over 117 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 282, ROI -6.6%; CLV n 304 over 104 games, +1.7%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1330, ROI -2.0%; CLV n 1259 over 105 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +4.1%; CLV n 89 over 36 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1117, ROI -5.8%; CLV n 644 over 98 games, -3.2%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 4253, ROI -3.2%; CLV n 1242 over 101 games, -5.5%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2572, ROI -4.8%; CLV n 1205 over 117 games, -4.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2727, ROI -5.9%; CLV n 1204 over 123 games, -4.2%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 5215, ROI -3.1%; CLV n 1887 over 106 games, -4.6%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 7254, ROI -5.1%; CLV n 2444 over 124 games, -5.0%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 688, ROI +6.3%; CLV n 647 over 62 games, -2.4%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 317, ROI -5.8%; CLV n 309 over 94 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1323, ROI -2.2%; CLV n 1252 over 105 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 6302, ROI -4.4%; CLV n 1431 over 106 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 81 over 16 games, +5.8%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 46, ROI -5.8%; CLV n 50 over 33 games, -3.8%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 137, ROI -10.4%; CLV n 131 over 68 games, +0.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 180, ROI -2.2%; CLV n 182 over 78 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1030, ROI -1.5%; CLV n 958 over 104 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 293, ROI -5.0%; CLV n 294 over 83 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -0.6%; CLV n 692 over 111 games, -6.7%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5511, ROI -4.9%; CLV n 668 over 100 games, -11.5%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 894, ROI +0.2%; CLV n 497 over 104 games, -4.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1305, ROI -8.8%; CLV n 915 over 106 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1483, ROI -4.8%; CLV n 419 over 99 games, -3.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1185, ROI -1.6%; CLV n 547 over 101 games, -4.0%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 171, ROI +9.2%; CLV n 171 over 77 games, -5.8%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 79, ROI -2.7%; CLV n 79 over 49 games, -3.7%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 946, ROI -3.6%; CLV n 243 over 88 games, -4.2%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 532, ROI -9.6%; CLV n 49 over 34 games, -7.8%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 724, ROI -5.0%; CLV n 19 over 13 games, -20.1%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 8569 | 7942 (108) | 64% | 64% | -4.1% (-6.2% to -2.0%) | 3091 (124) | -4.5% (-4.8% to -4.1%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 8354 | 7942 (108) | 64% | 64% | -4.1% (-6.2% to -2.0%) | 2992 (106) | -4.8% (-5.1% to -4.5%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 7853 | 7254 (107) | 65% | 65% | -5.1% (-7.5% to -2.9%) | 2444 (124) | -5.0% (-5.4% to -4.6%) | -0.2% (-0.4% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 7105 | 6736 (108) | 66% | 65% | -3.6% (-5.9% to -1.4%) | 1833 (113) | -5.9% (-6.4% to -5.5%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 6685 | 6302 (108) | 68% | 67% | -4.4% (-6.6% to -2.1%) | 1449 (117) | -8.7% (-9.1% to -8.3%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 6653 | 6302 (108) | 68% | 67% | -4.4% (-6.6% to -2.1%) | 1431 (106) | -8.8% (-9.2% to -8.4%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 6675 | 6292 (108) | 68% | 67% | -4.5% (-6.8% to -2.3%) | 1439 (117) | -8.8% (-9.1% to -8.4%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 6312 | 5984 (107) | 67% | 66% | -4.8% (-7.6% to -2.1%) | 1144 (109) | -6.7% (-7.4% to -6.0%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 5818 | 5511 (101) | 68% | 68% | -4.9% (-7.5% to -2.2%) | 668 (100) | -11.5% (-12.1% to -10.9%) | -0.9% (-1.2% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 5479 | 5215 (108) | 64% | 63% | -3.1% (-5.7% to -0.7%) | 1887 (106) | -4.6% (-5.0% to -4.3%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 4888 | 4582 (104) | 70% | 69% | -4.4% (-6.7% to -2.0%) | 537 (112) | -9.6% (-10.1% to -9.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 4680 | 4253 (89) | 67% | 65% | -3.2% (-6.1% to -0.5%) | 1242 (101) | -5.5% (-6.0% to -5.0%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 4085 | 3854 (108) | 64% | 64% | -4.7% (-7.5% to -2.0%) | 1404 (114) | -8.7% (-9.1% to -8.3%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 3848 | 3630 (95) | 72% | 71% | -4.3% (-6.8% to -1.9%) | 216 (84) | -9.6% (-10.5% to -8.7%) | -0.8% (-1.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3090 | 2727 (106) | 63% | 64% | -5.9% (-9.3% to -2.7%) | 1204 (123) | -4.2% (-4.7% to -3.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 2837 | 2672 (108) | 63% | 62% | -4.5% (-7.3% to -1.5%) | 1233 (117) | -8.6% (-8.9% to -8.2%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 2721 | 2572 (107) | 62% | 62% | -4.8% (-7.8% to -2.0%) | 1205 (117) | -4.1% (-4.5% to -3.7%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2545 | 2398 (81) | 74% | 73% | -3.8% (-6.1% to -1.4%) | 45 (31) | -8.1% (-10.0% to -6.4%) | +0.2% (-0.5% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1980 | 1879 (108) | 55% | 55% | -1.8% (-6.1% to +2.7%) | 1781 (112) | -3.5% (-3.8% to -3.2%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1841 | 1764 (108) | 62% | 61% | -4.1% (-7.2% to -1.1%) | 955 (106) | -8.0% (-8.3% to -7.6%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1782 | 1541 (107) | 47% | 49% | -2.9% (-8.3% to +2.7%) | 1549 (121) | -0.6% (-1.0% to -0.3%) | +0.2% (-0.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1554 | 1483 (107) | 63% | 63% | -4.8% (-8.3% to -1.3%) | 419 (99) | -3.0% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1554 | 1483 (107) | 63% | 63% | -4.8% (-8.3% to -1.3%) | 419 (99) | -3.0% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1379 | 1330 (107) | 49% | 50% | -2.0% (-8.2% to +4.3%) | 1259 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1372 | 1323 (107) | 49% | 50% | -2.2% (-8.6% to +4.1%) | 1252 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1372 | 1323 (107) | 49% | 50% | -2.2% (-8.6% to +4.1%) | 1252 (105) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1362 | 1305 (108) | 60% | 62% | -8.8% (-12.0% to -5.6%) | 915 (106) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1362 | 1305 (108) | 60% | 62% | -8.8% (-12.0% to -5.6%) | 915 (106) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1464 | 1206 (108) | 50% | 53% | -6.9% (-12.0% to -1.7%) | 1258 (122) | -2.3% (-2.7% to -2.0%) | -0.2% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1228 | 1185 (105) | 62% | 61% | -1.6% (-5.9% to +2.6%) | 547 (101) | -4.0% (-4.5% to -3.4%) | +0.2% (-0.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1228 | 1185 (105) | 62% | 61% | -1.6% (-5.9% to +2.6%) | 547 (101) | -4.0% (-4.5% to -3.4%) | +0.2% (-0.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1168 | 1117 (96) | 58% | 60% | -5.8% (-10.1% to -1.3%) | 644 (98) | -3.2% (-3.6% to -2.8%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1068 | 1030 (106) | 49% | 51% | -1.5% (-8.4% to +5.1%) | 958 (104) | -1.9% (-2.2% to -1.5%) | +0.7% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1036 | 995 (103) | 49% | 53% | -5.3% (-11.9% to +1.1%) | 918 (103) | -2.1% (-2.4% to -1.8%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 999 | 946 (102) | 65% | 64% | -3.6% (-7.5% to +0.2%) | 243 (88) | -4.2% (-4.8% to -3.7%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 999 | 946 (102) | 65% | 64% | -3.6% (-7.5% to +0.2%) | 243 (88) | -4.2% (-4.8% to -3.7%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 953 | 894 (107) | 62% | 60% | +0.2% (-4.5% to +4.8%) | 497 (104) | -4.4% (-4.9% to -3.8%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 953 | 894 (107) | 62% | 60% | +0.2% (-4.5% to +4.8%) | 497 (104) | -4.4% (-4.9% to -3.8%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 903 | 869 (103) | 49% | 52% | -6.0% (-13.0% to +0.7%) | 790 (101) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 937 | 727 (107) | 45% | 46% | -0.0% (-7.4% to +7.2%) | 809 (121) | +1.0% (+0.6% to +1.4%) | +0.4% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pr | 764 | 724 (80) | 69% | 68% | -5.0% (-9.3% to -1.1%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 764 | 724 (80) | 69% | 68% | -5.0% (-9.3% to -1.1%) | 19 (13) | -20.1% (-22.3% to -17.5%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = likely, side = under | 765 | 712 (108) | 65% | 62% | -0.6% (-5.9% to +4.7%) | 692 (111) | -6.7% (-7.0% to -6.3%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 716 | 688 (64) | 57% | 53% | +6.3% (-0.7% to +12.4%) | 647 (62) | -2.4% (-2.7% to -2.0%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 641 | 607 (106) | 45% | 46% | +0.3% (-7.2% to +8.0%) | 614 (108) | +0.1% (-0.3% to +0.5%) | +0.5% (+0.1% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 607 | 576 (81) | 70% | 69% | -3.1% (-7.5% to +0.9%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 607 | 576 (81) | 70% | 69% | -3.1% (-7.5% to +0.9%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 563 | 532 (88) | 65% | 68% | -9.6% (-15.9% to -3.6%) | 49 (34) | -7.8% (-10.7% to -4.9%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 563 | 532 (88) | 65% | 68% | -9.6% (-15.9% to -3.6%) | 49 (34) | -7.8% (-10.7% to -4.9%) | -2.3% (-4.0% to -0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 512 | 317 (97) | 43% | 48% | -5.8% (-16.0% to +4.2%) | 390 (110) | +2.5% (+1.9% to +3.2%) | -1.5% (-2.0% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 329 | 317 (97) | 43% | 48% | -5.8% (-16.0% to +4.2%) | 309 (94) | +1.7% (+1.1% to +2.3%) | -1.3% (-1.7% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 304 | 293 (83) | 46% | 49% | -5.0% (-18.5% to +8.9%) | 294 (83) | -1.4% (-1.9% to -0.8%) | +0.6% (+0.1% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 351 | 282 (95) | 43% | 48% | -6.6% (-16.7% to +3.5%) | 304 (104) | +1.7% (+1.2% to +2.3%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 190 | 180 (77) | 43% | 46% | -2.2% (-18.0% to +14.1%) | 182 (78) | +2.2% (+1.5% to +3.0%) | -1.7% (-2.4% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 183 | 171 (77) | 71% | 63% | +9.2% (-1.2% to +19.6%) | 171 (77) | -5.8% (-6.2% to -5.3%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 183 | 171 (77) | 71% | 63% | +9.2% (-1.2% to +19.6%) | 171 (77) | -5.8% (-6.2% to -5.3%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 147 | 137 (67) | 43% | 50% | -10.4% (-27.0% to +6.5%) | 131 (68) | +0.9% (+0.1% to +1.9%) | -0.8% (-1.7% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 102 | 99 (59) | 55% | 57% | -2.9% (-16.4% to +11.1%) | 93 (58) | -2.7% (-3.6% to -1.9%) | -1.1% (-1.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 85 | 79 (49) | 67% | 67% | -2.7% (-20.2% to +13.9%) | 79 (49) | -3.7% (-4.7% to -2.7%) | -0.3% (-1.3% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 102 | 79 (49) | 67% | 67% | -2.7% (-20.2% to +13.9%) | 89 (57) | -3.8% (-4.7% to -2.8%) | -0.3% (-1.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 56 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 56 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 53 | 46 (29) | 65% | 68% | -5.8% (-28.0% to +16.5%) | 50 (33) | -3.8% (-4.9% to -2.8%) | -0.3% (-1.5% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 53 | 46 (29) | 65% | 68% | -5.8% (-28.0% to +16.5%) | 50 (33) | -3.8% (-4.9% to -2.8%) | -0.3% (-1.5% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 56 | 38 (29) | 39% | 38% | +8.2% (-28.3% to +48.0%) | 46 (35) | +4.9% (+3.5% to +6.4%) | +1.4% (-0.4% to +3.1%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 6%+ | 164 | 38 (21) | 45% | 48% | +4.1% (-31.3% to +42.9%) | 89 (36) | +5.3% (+3.8% to +7.0%) | -3.1% (-4.8% to -1.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 49 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 49 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 96 | 0 (0) | – | – | – (–) | 36 (14) | +7.1% (+4.5% to +10.6%) | -1.4% (-3.3% to +1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 55 | 0 (0) | – | – | – (–) | 28 (14) | +5.9% (+4.3% to +7.6%) | -1.7% (-2.7% to -0.9%) | hypothesis |
| lane = likely, sport = nfl | 29 | 0 (0) | – | – | – (–) | 16 (9) | -5.5% (9 games) | -0.7% (9 games) | hypothesis |
| lane = likely, sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| lane = value, side = yes | 175 | 0 (0) | – | – | – (–) | 77 (16) | +6.1% (+4.6% to +7.8%) | -2.1% (-3.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 183 | 0 (0) | – | – | – (–) | 81 (16) | +5.8% (+4.4% to +7.4%) | -2.2% (-3.6% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 175 | 0 (0) | – | – | – (–) | 77 (16) | +6.1% (+4.6% to +7.8%) | -2.1% (-3.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 212 | 0 (0) | – | – | – (–) | 97 (16) | +3.9% (+2.4% to +5.6%) | -2.0% (-3.1% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 175 | 0 (0) | – | – | – (–) | 77 (16) | +6.1% (+4.6% to +7.8%) | -2.1% (-3.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 14 | 0 (0) | – | – | – (–) | 8 (6) | -4.4% (6 games) | -1.2% (6 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
| sport = soccer | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| sport = soccer, stat/market = moneyline | 3 | 0 (0) | – | – | – (–) | 2 (2) | -2.4% (2 games) | +3.5% (2 games) | hypothesis |
| stat/market = anytime_td | 175 | 0 (0) | – | – | – (–) | 77 (16) | +6.1% (+4.6% to +7.8%) | -2.1% (-3.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
