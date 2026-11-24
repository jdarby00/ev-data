# Research lab report

Built 2026-11-24T19:35:51Z UTC from 10333 logged code candidates (9329 settled, 3589 with a close, 153 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 7466, ROI -4.9%; CLV n 1690 over 139 games, -8.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 355, ROI -7.3%; CLV n 478 over 134 games, +3.0%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1508, ROI -1.1%; CLV n 1421 over 122 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 9329, ROI -4.4%; CLV n 3425 over 123 games, -4.8%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 162 over 28 games, +4.3%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 3177, ROI -4.7%; CLV n 1445 over 139 games, -8.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 114, ROI -0.2%; CLV n 108 over 68 games, -2.5%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1749, ROI -2.4%; CLV n 1791 over 150 games, -0.4%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 4289, ROI -5.0%; CLV n 245 over 97 games, -9.4%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 91, ROI -9.5%; CLV n 107 over 69 games, -3.9%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1057, ROI -1.0%; CLV n 578 over 120 games, -4.5%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1511, ROI -9.1%; CLV n 1055 over 122 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1746, ROI -4.0%; CLV n 472 over 116 games, -3.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1394, ROI -3.4%; CLV n 629 over 118 games, -4.2%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 191, ROI +10.7%; CLV n 191 over 88 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 53, ROI +12.3%; CLV n 53 over 33 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1116, ROI -3.1%; CLV n 275 over 102 games, -4.2%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 626, ROI -9.3%; CLV n 53 over 38 games, -8.3%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 863, ROI -5.4%; CLV n 21 over 14 games, -20.6%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 50, ROI -4.9%; CLV n 58 over 38 games, -3.8%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 2137, ROI -1.4%; CLV n 2023 over 133 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 7101, ROI -5.2%; CLV n 1330 over 129 games, -6.9%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 7978, ROI -3.9%; CLV n 2139 over 133 games, -6.0%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1351, ROI -7.1%; CLV n 1450 over 151 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 5454, ROI -5.0%; CLV n 621 over 132 games, -9.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 994, ROI -4.3%; CLV n 898 over 120 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 819, ROI -0.6%; CLV n 952 over 150 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 2062, ROI -4.3%; CLV n 1118 over 123 games, -8.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 4576, ROI -5.2%; CLV n 1633 over 135 games, -8.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 1136, ROI -4.1%; CLV n 1042 over 122 games, -2.0%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 42, ROI -2.1%; CLV n 54 over 43 games, +4.7%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 68 over 25 games, +7.4%)
- **chance = 20-30%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 43 over 22 games, +6.0%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2840, ROI -4.3%; CLV n 57 over 40 games, -7.4%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 7457, ROI -4.9%; CLV n 1681 over 139 games, -8.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 318, ROI -7.7%; CLV n 354 over 125 games, +1.9%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1514, ROI -0.9%; CLV n 1427 over 122 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 40, ROI -1.1%; CLV n 127 over 49 games, +6.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1299, ROI -6.3%; CLV n 735 over 114 games, -3.4%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 5105, ROI -3.5%; CLV n 1487 over 126 games, -5.3%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2925, ROI -5.0%; CLV n 1367 over 145 games, -4.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3151, ROI -5.9%; CLV n 1406 over 151 games, -4.0%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 6178, ROI -3.6%; CLV n 2183 over 123 games, -4.7%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 8551, ROI -5.2%; CLV n 2857 over 153 games, -4.9%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 778, ROI +5.2%; CLV n 732 over 75 games, -2.3%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 355, ROI -7.3%; CLV n 342 over 106 games, +1.8%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1508, ROI -1.1%; CLV n 1421 over 122 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 7466, ROI -4.9%; CLV n 1662 over 123 games, -8.8%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 136 over 28 games, +6.2%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 50, ROI -4.9%; CLV n 58 over 38 games, -3.8%)
- **lane = value, side = under**: IN-SAMPLE SIGNAL: positive CLV (settled 159, ROI -11.1%; CLV n 151 over 78 games, +1.2%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 196, ROI -4.2%; CLV n 198 over 88 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1180, ROI +0.4%; CLV n 1093 over 121 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 328, ROI -6.3%; CLV n 328 over 94 games, -1.4%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 798, ROI -2.1%; CLV n 779 over 130 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -15.1%; CLV n 49 over 31 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 6577, ROI -5.1%; CLV n 804 over 119 games, -11.4%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 1057, ROI -1.0%; CLV n 578 over 120 games, -4.5%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1511, ROI -9.1%; CLV n 1055 over 122 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1746, ROI -4.0%; CLV n 472 over 116 games, -3.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1394, ROI -3.4%; CLV n 629 over 118 games, -4.2%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 191, ROI +10.7%; CLV n 191 over 88 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 91, ROI -9.5%; CLV n 91 over 57 games, -3.9%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 53, ROI +12.3%; CLV n 53 over 33 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 1116, ROI -3.1%; CLV n 275 over 102 games, -4.2%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 626, ROI -9.3%; CLV n 53 over 38 games, -8.3%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 129 over 28 games, +6.5%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 863, ROI -5.4%; CLV n 21 over 14 games, -20.6%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 10333 | 9329 (125) | 64% | 64% | -4.4% (-6.3% to -2.5%) | 3589 (153) | -4.4% (-4.7% to -4.1%) | -0.2% (-0.3% to -0.0%) |  |
| sport = nba | 10051 | 9329 (125) | 64% | 64% | -4.4% (-6.3% to -2.5%) | 3425 (123) | -4.8% (-5.1% to -4.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 9525 | 8551 (124) | 64% | 65% | -5.2% (-7.4% to -3.4%) | 2857 (153) | -4.9% (-5.3% to -4.6%) | -0.2% (-0.4% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 8633 | 7978 (125) | 66% | 66% | -3.9% (-6.0% to -1.9%) | 2139 (133) | -6.0% (-6.4% to -5.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 8143 | 7466 (125) | 68% | 67% | -4.9% (-6.9% to -2.9%) | 1690 (139) | -8.7% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 8101 | 7466 (125) | 68% | 67% | -4.9% (-6.9% to -2.9%) | 1662 (123) | -8.8% (-9.2% to -8.5%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 8134 | 7457 (125) | 68% | 67% | -4.9% (-7.0% to -2.9%) | 1681 (139) | -8.8% (-9.1% to -8.4%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 7695 | 7101 (124) | 66% | 66% | -5.2% (-7.7% to -2.6%) | 1330 (129) | -6.9% (-7.5% to -6.3%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 7148 | 6577 (118) | 68% | 68% | -5.1% (-7.5% to -2.8%) | 804 (119) | -11.4% (-12.0% to -10.9%) | -0.8% (-1.1% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 6619 | 6178 (125) | 64% | 63% | -3.6% (-5.9% to -1.5%) | 2183 (123) | -4.7% (-5.0% to -4.3%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 5989 | 5454 (121) | 70% | 69% | -5.0% (-7.2% to -2.7%) | 621 (132) | -9.5% (-10.0% to -9.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 5830 | 5105 (105) | 66% | 65% | -3.5% (-5.9% to -1.2%) | 1487 (126) | -5.3% (-5.7% to -4.8%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 4980 | 4576 (125) | 64% | 64% | -5.2% (-7.6% to -2.8%) | 1633 (135) | -8.8% (-9.2% to -8.4%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 4683 | 4289 (112) | 71% | 71% | -5.0% (-7.3% to -2.8%) | 245 (97) | -9.4% (-10.2% to -8.6%) | -0.8% (-1.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 3460 | 3177 (125) | 63% | 62% | -4.7% (-7.2% to -1.9%) | 1445 (139) | -8.6% (-9.0% to -8.3%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 3714 | 3151 (122) | 63% | 64% | -5.9% (-8.9% to -2.9%) | 1406 (151) | -4.0% (-4.5% to -3.5%) | -0.6% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 3147 | 2925 (124) | 62% | 62% | -5.0% (-7.7% to -2.3%) | 1367 (145) | -4.0% (-4.4% to -3.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 3108 | 2840 (98) | 74% | 73% | -4.3% (-6.5% to -2.0%) | 57 (40) | -7.4% (-9.1% to -6.0%) | -0.2% (-0.9% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 2287 | 2137 (125) | 55% | 55% | -1.4% (-5.9% to +2.9%) | 2023 (133) | -3.5% (-3.8% to -3.2%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 2205 | 2062 (125) | 62% | 61% | -4.3% (-7.2% to -1.6%) | 1118 (123) | -8.0% (-8.3% to -7.7%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 2071 | 1749 (124) | 47% | 49% | -2.4% (-7.5% to +2.9%) | 1791 (150) | -0.4% (-0.8% to -0.1%) | +0.2% (-0.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1864 | 1746 (124) | 63% | 63% | -4.0% (-7.1% to -1.0%) | 472 (116) | -3.0% (-3.4% to -2.6%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1864 | 1746 (124) | 63% | 63% | -4.0% (-7.1% to -1.0%) | 472 (116) | -3.0% (-3.4% to -2.6%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1589 | 1514 (124) | 49% | 50% | -0.9% (-6.6% to +5.0%) | 1427 (122) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1619 | 1511 (125) | 60% | 62% | -9.1% (-12.0% to -6.3%) | 1055 (122) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1619 | 1511 (125) | 60% | 62% | -9.1% (-12.0% to -6.3%) | 1055 (122) | -5.7% (-6.0% to -5.4%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1583 | 1508 (124) | 49% | 50% | -1.1% (-7.1% to +4.7%) | 1421 (122) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1583 | 1508 (124) | 49% | 50% | -1.1% (-7.1% to +4.7%) | 1421 (122) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1489 | 1394 (122) | 61% | 61% | -3.4% (-7.3% to +0.4%) | 629 (118) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1489 | 1394 (122) | 61% | 61% | -3.4% (-7.3% to +0.4%) | 629 (118) | -4.2% (-4.7% to -3.6%) | +0.3% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1700 | 1351 (125) | 50% | 53% | -7.1% (-11.8% to -2.4%) | 1450 (151) | -2.1% (-2.4% to -1.7%) | -0.2% (-0.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1356 | 1299 (110) | 58% | 60% | -6.3% (-10.2% to -2.1%) | 735 (114) | -3.4% (-3.8% to -2.9%) | -0.4% (-0.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1243 | 1180 (123) | 50% | 51% | +0.4% (-6.3% to +7.0%) | 1093 (121) | -1.9% (-2.2% to -1.6%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 1195 | 1136 (120) | 50% | 53% | -4.1% (-10.4% to +2.3%) | 1042 (122) | -2.0% (-2.3% to -1.8%) | -0.0% (-0.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 1205 | 1116 (119) | 65% | 64% | -3.1% (-6.6% to +0.4%) | 275 (102) | -4.2% (-4.7% to -3.6%) | +0.4% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 1205 | 1116 (119) | 65% | 64% | -3.1% (-6.6% to +0.4%) | 275 (102) | -4.2% (-4.7% to -3.6%) | +0.4% (+0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 1148 | 1057 (124) | 62% | 60% | -1.0% (-5.4% to +3.3%) | 578 (120) | -4.5% (-5.0% to -4.1%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 1148 | 1057 (124) | 62% | 60% | -1.0% (-5.4% to +3.3%) | 578 (120) | -4.5% (-5.0% to -4.1%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 1045 | 994 (120) | 50% | 52% | -4.3% (-10.9% to +2.1%) | 898 (120) | -2.4% (-2.6% to -2.1%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 934 | 863 (97) | 69% | 68% | -5.4% (-9.4% to -1.4%) | 21 (14) | -20.6% (-22.7% to -18.2%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 934 | 863 (97) | 69% | 68% | -5.4% (-9.4% to -1.4%) | 21 (14) | -20.6% (-22.7% to -18.2%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 1094 | 819 (124) | 45% | 46% | -0.6% (-7.1% to +6.1%) | 952 (150) | +1.2% (+0.8% to +1.7%) | +0.3% (+0.0% to +0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 873 | 798 (125) | 64% | 62% | -2.1% (-7.1% to +2.8%) | 779 (130) | -6.6% (-6.9% to -6.3%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 808 | 778 (77) | 56% | 53% | +5.2% (-0.8% to +10.9%) | 732 (75) | -2.3% (-2.7% to -2.0%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 731 | 685 (123) | 46% | 46% | +0.7% (-6.6% to +7.9%) | 692 (127) | +0.1% (-0.3% to +0.4%) | +0.5% (+0.2% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 740 | 681 (98) | 70% | 69% | -3.1% (-7.3% to +0.7%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 740 | 681 (98) | 70% | 69% | -3.1% (-7.3% to +0.7%) | 7 (7) | -15.1% (7 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 681 | 626 (105) | 66% | 68% | -9.3% (-14.8% to -3.7%) | 53 (38) | -8.3% (-11.0% to -5.6%) | -2.2% (-3.9% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 681 | 626 (105) | 66% | 68% | -9.3% (-14.8% to -3.7%) | 53 (38) | -8.3% (-11.0% to -5.6%) | -2.2% (-3.9% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 607 | 355 (109) | 42% | 48% | -7.3% (-16.8% to +1.4%) | 478 (134) | +3.0% (+2.4% to +3.7%) | -1.3% (-1.7% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 367 | 355 (109) | 42% | 48% | -7.3% (-16.8% to +1.4%) | 342 (106) | +1.8% (+1.2% to +2.4%) | -1.2% (-1.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 340 | 328 (94) | 46% | 49% | -6.3% (-18.5% to +6.5%) | 328 (94) | -1.4% (-1.9% to -0.9%) | +0.5% (+0.2% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 406 | 318 (107) | 42% | 48% | -7.7% (-16.9% to +1.5%) | 354 (125) | +1.9% (+1.4% to +2.4%) | -0.9% (-1.3% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 207 | 196 (86) | 42% | 46% | -4.2% (-18.4% to +11.2%) | 198 (88) | +2.2% (+1.5% to +2.9%) | -1.7% (-2.4% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 208 | 191 (88) | 72% | 62% | +10.7% (+0.9% to +20.0%) | 191 (88) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 208 | 191 (88) | 72% | 62% | +10.7% (+0.9% to +20.0%) | 191 (88) | -5.7% (-6.1% to -5.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 171 | 159 (75) | 43% | 50% | -11.1% (-25.8% to +3.8%) | 151 (78) | +1.2% (+0.4% to +2.1%) | -0.6% (-1.4% to +0.2%) | IN-SAMPLE SIGNAL: positive CLV |
| tier = Lean | 119 | 114 (69) | 56% | 57% | -0.2% (-13.4% to +13.8%) | 108 (68) | -2.5% (-3.3% to -1.8%) | -0.9% (-1.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 99 | 91 (57) | 63% | 68% | -9.5% (-26.1% to +6.6%) | 91 (57) | -3.9% (-4.8% to -2.9%) | -0.5% (-1.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 122 | 91 (57) | 63% | 68% | -9.5% (-26.1% to +6.6%) | 107 (69) | -3.9% (-4.6% to -3.1%) | -0.5% (-1.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 64 | 53 (33) | 74% | 61% | +12.3% (-5.6% to +29.2%) | 53 (33) | -5.6% (-6.3% to -4.9%) | -1.0% (-1.6% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 64 | 53 (33) | 74% | 61% | +12.3% (-5.6% to +29.2%) | 53 (33) | -5.6% (-6.3% to -4.9%) | -1.0% (-1.6% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| lane = likely, side = home | 63 | 50 (32) | 66% | 68% | -4.9% (-26.9% to +15.1%) | 58 (38) | -3.8% (-4.9% to -2.9%) | -0.4% (-1.5% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 63 | 50 (32) | 66% | 68% | -4.9% (-26.9% to +15.1%) | 58 (38) | -3.8% (-4.9% to -2.9%) | -0.4% (-1.5% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 64 | 42 (33) | 36% | 38% | -2.1% (-38.0% to +35.6%) | 54 (43) | +4.7% (+3.5% to +6.0%) | +1.1% (-0.4% to +2.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 59 | 41 (25) | 59% | 67% | -15.1% (-41.0% to +10.5%) | 49 (31) | -3.9% (-5.1% to -2.5%) | -0.5% (-1.7% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 204 | 40 (22) | 42% | 48% | -1.1% (-36.1% to +36.6%) | 127 (49) | +6.3% (+5.0% to +7.7%) | -2.3% (-3.6% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
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
