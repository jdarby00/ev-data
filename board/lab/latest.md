# Research lab report

Built 2026-11-20T19:35:40Z UTC from 7968 logged code candidates (6707 settled, 2702 with a close, 107 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 5242, ROI -4.6%; CLV n 1226 over 100 games, -8.5%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 296, ROI -4.6%; CLV n 369 over 98 games, +2.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1169, ROI -1.7%; CLV n 1107 over 90 games, -1.7%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 6707, ROI -4.1%; CLV n 2605 over 91 games, -4.5%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 97 over 16 games, +3.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2214, ROI -4.9%; CLV n 1043 over 100 games, -8.3%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 80, ROI +0.1%; CLV n 75 over 47 games, -2.6%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1385, ROI -2.4%; CLV n 1401 over 106 games, -0.6%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 3028, ROI -4.3%; CLV n 183 over 71 games, -9.6%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 66, ROI -8.1%; CLV n 74 over 47 games, -3.7%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 749, ROI +0.3%; CLV n 418 over 89 games, -4.0%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1129, ROI -8.7%; CLV n 805 over 91 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1259, ROI -4.0%; CLV n 374 over 85 games, -2.8%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 996, ROI -1.4%; CLV n 470 over 87 games, -3.5%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 152, ROI +10.2%; CLV n 152 over 66 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI +10.2%; CLV n 43 over 27 games, -5.5%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 791, ROI -2.9%; CLV n 215 over 77 games, -3.9%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 440, ROI -13.9%; CLV n 44 over 30 games, -7.0%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 37, ROI -10.7%; CLV n 39 over 25 games, -3.5%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1663, ROI -1.9%; CLV n 1574 over 97 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 4978, ROI -4.7%; CLV n 977 over 94 games, -6.2%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI -4.8%; CLV n 35 over 22 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 5624, ROI -3.5%; CLV n 1565 over 96 games, -5.7%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1083, ROI -7.2%; CLV n 1137 over 107 games, -2.2%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 3811, ROI -4.5%; CLV n 456 over 96 games, -9.3%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 769, ROI -5.3%; CLV n 701 over 87 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 658, ROI +0.6%; CLV n 738 over 106 games, +1.1%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1469, ROI -4.3%; CLV n 807 over 91 games, -7.8%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 3188, ROI -4.9%; CLV n 1187 over 99 games, -8.5%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 879, ROI -4.3%; CLV n 813 over 89 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 33, ROI +16.0%; CLV n 41 over 32 games, +4.5%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 36 over 14 games, +7.1%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2004, ROI -3.9%; CLV n 39 over 26 games, -7.9%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 5234, ROI -4.6%; CLV n 1218 over 100 games, -8.6%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 260, ROI -5.7%; CLV n 282 over 92 games, +1.6%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1175, ROI -1.4%; CLV n 1113 over 90 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +4.1%; CLV n 89 over 36 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1017, ROI -4.9%; CLV n 598 over 87 games, -3.1%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 3530, ROI -3.4%; CLV n 1075 over 87 games, -5.3%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2160, ROI -4.8%; CLV n 1029 over 100 games, -3.7%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2281, ROI -6.4%; CLV n 1064 over 106 games, -3.9%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 4426, ROI -2.9%; CLV n 1638 over 91 games, -4.4%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 6092, ROI -5.1%; CLV n 2124 over 107 games, -4.8%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 615, ROI +6.2%; CLV n 578 over 54 games, -2.2%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 296, ROI -4.6%; CLV n 288 over 82 games, +1.6%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1169, ROI -1.7%; CLV n 1107 over 90 games, -1.7%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 5242, ROI -4.6%; CLV n 1210 over 91 games, -8.6%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 81 over 16 games, +5.8%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 37, ROI -10.7%; CLV n 39 over 25 games, -3.5%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 166, ROI -1.1%; CLV n 169 over 71 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 902, ROI -1.0%; CLV n 839 over 89 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 267, ROI -3.9%; CLV n 268 over 71 games, -1.3%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 631, ROI -1.8%; CLV n 612 over 96 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI -4.8%; CLV n 35 over 22 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 4545, ROI -4.9%; CLV n 540 over 85 games, -11.3%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 749, ROI +0.3%; CLV n 418 over 89 games, -4.0%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1129, ROI -8.7%; CLV n 805 over 91 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1259, ROI -4.0%; CLV n 374 over 85 games, -2.8%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 996, ROI -1.4%; CLV n 470 over 87 games, -3.5%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 152, ROI +10.2%; CLV n 152 over 66 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 66, ROI -8.1%; CLV n 66 over 41 games, -3.6%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI +10.2%; CLV n 43 over 27 games, -5.5%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 791, ROI -2.9%; CLV n 215 over 77 games, -3.9%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 440, ROI -13.9%; CLV n 44 over 30 games, -7.0%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 7968 | 6707 (93) | 64% | 63% | -4.1% (-6.5% to -1.9%) | 2702 (107) | -4.2% (-4.5% to -3.9%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 7755 | 6707 (93) | 64% | 63% | -4.1% (-6.5% to -1.9%) | 2605 (91) | -4.5% (-4.9% to -4.2%) | -0.1% (-0.4% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 7304 | 6092 (92) | 64% | 64% | -5.1% (-7.9% to -2.7%) | 2124 (107) | -4.8% (-5.2% to -4.3%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 6593 | 5624 (93) | 66% | 65% | -3.5% (-5.9% to -1.0%) | 1565 (96) | -5.7% (-6.1% to -5.2%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 6204 | 5242 (93) | 68% | 67% | -4.6% (-7.2% to -1.9%) | 1226 (100) | -8.5% (-9.0% to -8.1%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 6174 | 5242 (93) | 68% | 67% | -4.6% (-7.2% to -1.9%) | 1210 (91) | -8.6% (-9.0% to -8.1%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 6195 | 5234 (93) | 68% | 67% | -4.6% (-7.2% to -2.1%) | 1218 (100) | -8.6% (-9.0% to -8.1%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 5845 | 4978 (92) | 67% | 66% | -4.7% (-7.8% to -1.5%) | 977 (94) | -6.2% (-6.9% to -5.5%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 5386 | 4545 (86) | 69% | 68% | -4.9% (-8.0% to -1.8%) | 540 (85) | -11.3% (-12.0% to -10.6%) | -0.9% (-1.2% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 5099 | 4426 (93) | 64% | 63% | -2.9% (-5.8% to -0.2%) | 1638 (91) | -4.4% (-4.9% to -4.0%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 4542 | 3811 (89) | 70% | 69% | -4.5% (-7.2% to -1.8%) | 456 (96) | -9.3% (-9.9% to -8.7%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 4462 | 3530 (75) | 66% | 65% | -3.4% (-6.5% to -0.3%) | 1075 (87) | -5.3% (-5.9% to -4.8%) | -0.2% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 3776 | 3188 (93) | 64% | 64% | -4.9% (-7.9% to -1.8%) | 1187 (99) | -8.5% (-9.0% to -8.1%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 3576 | 3028 (80) | 72% | 71% | -4.3% (-7.4% to -1.6%) | 183 (71) | -9.6% (-10.6% to -8.5%) | -0.9% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 2869 | 2281 (91) | 62% | 64% | -6.4% (-10.1% to -3.0%) | 1064 (106) | -3.9% (-4.4% to -3.4%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 2628 | 2214 (93) | 63% | 62% | -4.9% (-8.0% to -1.5%) | 1043 (100) | -8.3% (-8.8% to -7.9%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 2441 | 2160 (92) | 61% | 62% | -4.8% (-8.1% to -1.8%) | 1029 (100) | -3.7% (-4.1% to -3.3%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2373 | 2004 (66) | 74% | 73% | -3.9% (-6.6% to -1.2%) | 39 (26) | -7.9% (-9.8% to -6.2%) | +0.1% (-0.6% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1853 | 1663 (93) | 55% | 55% | -1.9% (-6.7% to +2.9%) | 1574 (97) | -3.5% (-3.9% to -3.2%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1703 | 1469 (93) | 62% | 61% | -4.3% (-8.0% to -0.9%) | 807 (91) | -7.8% (-8.2% to -7.4%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1670 | 1385 (92) | 47% | 49% | -2.4% (-8.5% to +3.8%) | 1401 (106) | -0.6% (-0.9% to -0.2%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1445 | 1259 (92) | 63% | 63% | -4.0% (-7.9% to -0.1%) | 374 (85) | -2.8% (-3.2% to -2.4%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1445 | 1259 (92) | 63% | 63% | -4.0% (-7.9% to -0.1%) | 374 (85) | -2.8% (-3.2% to -2.4%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1276 | 1175 (92) | 49% | 50% | -1.4% (-7.9% to +5.3%) | 1113 (90) | -1.8% (-2.1% to -1.5%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1270 | 1169 (92) | 49% | 50% | -1.7% (-8.5% to +5.1%) | 1107 (90) | -1.7% (-2.1% to -1.4%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1270 | 1169 (92) | 49% | 50% | -1.7% (-8.5% to +5.1%) | 1107 (90) | -1.7% (-2.1% to -1.4%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1275 | 1129 (93) | 60% | 62% | -8.7% (-12.2% to -5.2%) | 805 (91) | -5.7% (-6.0% to -5.3%) | -0.4% (-0.6% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1275 | 1129 (93) | 60% | 62% | -8.7% (-12.2% to -5.2%) | 805 (91) | -5.7% (-6.0% to -5.3%) | -0.4% (-0.6% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1375 | 1083 (93) | 50% | 53% | -7.2% (-12.6% to -1.4%) | 1137 (107) | -2.2% (-2.6% to -1.8%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1065 | 1017 (85) | 59% | 60% | -4.9% (-9.3% to +0.1%) | 598 (87) | -3.1% (-3.6% to -2.7%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1132 | 996 (90) | 61% | 60% | -1.4% (-6.1% to +3.2%) | 470 (87) | -3.5% (-4.2% to -2.9%) | +0.3% (-0.2% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1132 | 996 (90) | 61% | 60% | -1.4% (-6.1% to +3.2%) | 470 (87) | -3.5% (-4.2% to -2.9%) | +0.3% (-0.2% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 989 | 902 (91) | 49% | 51% | -1.0% (-8.7% to +6.2%) | 839 (89) | -1.9% (-2.3% to -1.5%) | +0.6% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 964 | 879 (89) | 50% | 53% | -4.3% (-11.3% to +3.0%) | 813 (89) | -2.1% (-2.4% to -1.8%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 926 | 791 (87) | 65% | 64% | -2.9% (-7.4% to +1.5%) | 215 (77) | -3.9% (-4.5% to -3.4%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 926 | 791 (87) | 65% | 64% | -2.9% (-7.4% to +1.5%) | 215 (77) | -3.9% (-4.5% to -3.4%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 838 | 769 (89) | 49% | 52% | -5.3% (-13.0% to +2.5%) | 701 (87) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 871 | 749 (92) | 62% | 60% | +0.3% (-5.0% to +5.4%) | 418 (89) | -4.0% (-4.6% to -3.5%) | -0.3% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 871 | 749 (92) | 62% | 60% | +0.3% (-5.0% to +5.4%) | 418 (89) | -4.0% (-4.6% to -3.5%) | -0.3% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 885 | 658 (92) | 45% | 46% | +0.6% (-7.3% to +8.5%) | 738 (106) | +1.1% (+0.6% to +1.5%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 723 | 631 (93) | 64% | 62% | -1.8% (-7.5% to +4.0%) | 612 (96) | -6.6% (-7.0% to -6.3%) | -0.8% (-1.1% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 664 | 615 (56) | 56% | 53% | +6.2% (-0.8% to +12.9%) | 578 (54) | -2.2% (-2.5% to -1.9%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 707 | 603 (66) | 70% | 68% | -3.9% (-8.4% to +0.5%) | 13 (9) | -19.7% (9 games) | -2.9% (2 games) | hypothesis (range includes zero) |
| stat/market = pr | 707 | 603 (66) | 70% | 68% | -3.9% (-8.4% to +0.5%) | 13 (9) | -19.7% (9 games) | -2.9% (2 games) | hypothesis (range includes zero) |
| chance = 40-50% | 598 | 553 (91) | 45% | 46% | -0.1% (-8.3% to +8.3%) | 558 (93) | +0.2% (-0.2% to +0.6%) | +0.5% (+0.1% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 571 | 479 (66) | 70% | 69% | -4.0% (-9.0% to +0.4%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 571 | 479 (66) | 70% | 69% | -4.0% (-9.0% to +0.4%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 523 | 440 (73) | 62% | 68% | -13.9% (-21.0% to -6.8%) | 44 (30) | -7.0% (-10.1% to -4.0%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 523 | 440 (73) | 62% | 68% | -13.9% (-21.0% to -6.8%) | 44 (30) | -7.0% (-10.1% to -4.0%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 494 | 296 (85) | 44% | 48% | -4.6% (-15.4% to +5.7%) | 369 (98) | +2.5% (+1.9% to +3.2%) | -1.6% (-2.1% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 311 | 296 (85) | 44% | 48% | -4.6% (-15.4% to +5.7%) | 288 (82) | +1.6% (+1.1% to +2.2%) | -1.4% (-1.9% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 281 | 267 (71) | 47% | 49% | -3.9% (-18.8% to +10.8%) | 268 (71) | -1.3% (-1.8% to -0.7%) | +0.6% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 333 | 260 (83) | 43% | 48% | -5.7% (-16.2% to +4.9%) | 282 (92) | +1.6% (+1.1% to +2.2%) | -1.1% (-1.5% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 178 | 166 (70) | 43% | 46% | -1.1% (-17.5% to +16.1%) | 169 (71) | +2.2% (+1.4% to +2.9%) | -1.8% (-2.5% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 169 | 152 (66) | 72% | 62% | +10.2% (-1.4% to +21.4%) | 152 (66) | -5.7% (-6.2% to -5.2%) | -0.7% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 169 | 152 (66) | 72% | 62% | +10.2% (-1.4% to +21.4%) | 152 (66) | -5.7% (-6.2% to -5.2%) | -0.7% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 141 | 130 (61) | 44% | 50% | -9.0% (-25.9% to +7.8%) | 123 (62) | +0.9% (-0.1% to +1.8%) | -1.1% (-1.9% to -0.2%) | hypothesis (range includes zero) |
| tier = Lean | 94 | 80 (48) | 56% | 57% | +0.1% (-15.5% to +15.1%) | 75 (47) | -2.6% (-3.6% to -1.7%) | -1.2% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 80 | 66 (41) | 64% | 67% | -8.1% (-27.2% to +10.9%) | 66 (41) | -3.6% (-4.6% to -2.5%) | -0.1% (-1.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 95 | 66 (41) | 64% | 67% | -8.1% (-27.2% to +10.9%) | 74 (47) | -3.7% (-4.6% to -2.6%) | -0.2% (-1.1% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 56 | 43 (27) | 72% | 61% | +10.2% (-13.1% to +29.1%) | 43 (27) | -5.5% (-6.3% to -4.6%) | -1.0% (-1.7% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 56 | 43 (27) | 72% | 61% | +10.2% (-13.1% to +29.1%) | 43 (27) | -5.5% (-6.3% to -4.6%) | -1.0% (-1.7% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 164 | 38 (21) | 45% | 48% | +4.1% (-31.3% to +42.9%) | 89 (36) | +5.3% (+3.8% to +7.0%) | -3.1% (-4.8% to -1.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = home | 46 | 37 (23) | 62% | 68% | -10.7% (-35.5% to +13.6%) | 39 (25) | -3.5% (-4.4% to -2.5%) | +0.0% (-0.9% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 46 | 37 (23) | 62% | 68% | -10.7% (-35.5% to +13.6%) | 39 (25) | -3.5% (-4.4% to -2.5%) | +0.0% (-0.9% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 51 | 33 (26) | 42% | 38% | +16.0% (-24.3% to +60.5%) | 41 (32) | +4.5% (+2.9% to +6.0%) | +0.8% (-1.2% to +2.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 49 | 29 (18) | 66% | 67% | -4.8% (-33.8% to +23.5%) | 35 (22) | -3.9% (-5.6% to -1.9%) | -0.5% (-2.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 49 | 29 (18) | 66% | 67% | -4.8% (-33.8% to +23.5%) | 35 (22) | -3.9% (-5.6% to -1.9%) | -0.5% (-2.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 96 | 0 (0) | – | – | – (–) | 36 (14) | +7.1% (+4.5% to +10.6%) | -1.4% (-3.3% to +1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 55 | 0 (0) | – | – | – (–) | 28 (14) | +5.9% (+4.3% to +7.6%) | -1.7% (-2.7% to -0.9%) | hypothesis |
| lane = likely, sport = nfl | 29 | 0 (0) | – | – | – (–) | 16 (9) | -5.5% (9 games) | -0.7% (9 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
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
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 175 | 0 (0) | – | – | – (–) | 77 (16) | +6.1% (+4.6% to +7.8%) | -2.1% (-3.6% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
