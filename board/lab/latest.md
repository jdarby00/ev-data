# Research lab report

Built 2026-11-21T11:10:43Z UTC from 8101 logged code candidates (7513 settled, 2945 with a close, 116 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 5941, ROI -4.3%; CLV n 1367 over 109 games, -8.6%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 307, ROI -3.6%; CLV n 380 over 105 games, +2.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1265, ROI -2.4%; CLV n 1198 over 99 games, -1.7%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 7513, ROI -4.0%; CLV n 2848 over 100 games, -4.7%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 97 over 16 games, +3.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2520, ROI -4.5%; CLV n 1167 over 109 games, -8.5%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 96, ROI -3.6%; CLV n 90 over 55 games, -2.6%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1476, ROI -2.5%; CLV n 1488 over 115 games, -0.6%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 3421, ROI -4.2%; CLV n 200 over 78 games, -9.4%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 74, ROI -6.2%; CLV n 82 over 52 games, -3.5%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 842, ROI +0.9%; CLV n 467 over 98 games, -4.3%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1243, ROI -8.6%; CLV n 872 over 100 games, -5.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1402, ROI -5.2%; CLV n 403 over 93 games, -2.9%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1120, ROI -1.4%; CLV n 517 over 96 games, -3.7%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 165, ROI +10.6%; CLV n 165 over 73 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 891, ROI -3.2%; CLV n 233 over 85 games, -4.1%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 500, ROI -11.0%; CLV n 48 over 33 games, -8.0%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 681, ROI -4.4%; CLV n 16 over 12 games, -19.9%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -12.4%; CLV n 43 over 28 games, -3.3%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1808, ROI -1.7%; CLV n 1713 over 106 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5631, ROI -4.7%; CLV n 1073 over 103 games, -6.6%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 6361, ROI -3.5%; CLV n 1739 over 105 games, -5.8%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1152, ROI -6.9%; CLV n 1206 over 116 games, -2.3%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 4312, ROI -4.5%; CLV n 499 over 104 games, -9.4%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 832, ROI -6.2%; CLV n 759 over 95 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 697, ROI +1.1%; CLV n 777 over 115 games, +1.0%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1672, ROI -3.7%; CLV n 910 over 100 games, -7.9%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 3621, ROI -4.7%; CLV n 1326 over 108 games, -8.6%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 954, ROI -5.5%; CLV n 883 over 97 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 34, ROI +12.6%; CLV n 42 over 33 games, +4.8%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 36 over 14 games, +7.1%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 2270, ROI -3.6%; CLV n 41 over 28 games, -7.8%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 5932, ROI -4.4%; CLV n 1358 over 109 games, -8.6%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 272, ROI -4.2%; CLV n 294 over 99 games, +1.7%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1271, ROI -2.1%; CLV n 1204 over 99 games, -1.8%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 38, ROI +4.1%; CLV n 89 over 36 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1069, ROI -4.9%; CLV n 626 over 94 games, -3.2%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 4068, ROI -3.5%; CLV n 1194 over 96 games, -5.5%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2376, ROI -4.4%; CLV n 1125 over 109 games, -3.9%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2563, ROI -5.8%; CLV n 1154 over 115 games, -4.2%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 4950, ROI -3.1%; CLV n 1791 over 100 games, -4.5%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 6858, ROI -5.1%; CLV n 2328 over 116 games, -4.9%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 655, ROI +7.4%; CLV n 617 over 57 games, -2.3%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 307, ROI -3.6%; CLV n 299 over 89 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1265, ROI -2.4%; CLV n 1198 over 99 games, -1.7%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 5941, ROI -4.3%; CLV n 1351 over 100 games, -8.6%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 81 over 16 games, +5.8%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 41, ROI -12.4%; CLV n 43 over 28 games, -3.3%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 174, ROI -0.5%; CLV n 177 over 75 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 990, ROI -1.6%; CLV n 922 over 98 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 275, ROI -5.2%; CLV n 276 over 77 games, -1.3%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 685, ROI -0.8%; CLV n 665 over 105 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +1.6%; CLV n 39 over 24 games, -3.8%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 5182, ROI -4.8%; CLV n 620 over 94 games, -11.4%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 842, ROI +0.9%; CLV n 467 over 98 games, -4.3%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1243, ROI -8.6%; CLV n 872 over 100 games, -5.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1402, ROI -5.2%; CLV n 403 over 93 games, -2.9%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 1120, ROI -1.4%; CLV n 517 over 96 games, -3.7%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 165, ROI +10.6%; CLV n 165 over 73 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 74, ROI -6.2%; CLV n 74 over 46 games, -3.4%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +7.2%; CLV n 47 over 30 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 891, ROI -3.2%; CLV n 233 over 85 games, -4.1%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 500, ROI -11.0%; CLV n 48 over 33 games, -8.0%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 77 over 16 games, +6.1%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 681, ROI -4.4%; CLV n 16 over 12 games, -19.9%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 8101 | 7513 (102) | 64% | 64% | -4.0% (-6.2% to -1.8%) | 2945 (116) | -4.4% (-4.7% to -4.0%) | -0.2% (-0.4% to +0.0%) |  |
| sport = nba | 7888 | 7513 (102) | 64% | 64% | -4.0% (-6.2% to -1.8%) | 2848 (100) | -4.7% (-5.0% to -4.4%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 7418 | 6858 (101) | 64% | 65% | -5.1% (-7.6% to -2.8%) | 2328 (116) | -4.9% (-5.3% to -4.5%) | -0.2% (-0.4% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 6695 | 6361 (102) | 66% | 65% | -3.5% (-5.8% to -1.2%) | 1739 (105) | -5.8% (-6.2% to -5.4%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 6292 | 5941 (102) | 68% | 67% | -4.3% (-6.7% to -2.0%) | 1367 (109) | -8.6% (-9.0% to -8.2%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 6262 | 5941 (102) | 68% | 67% | -4.3% (-6.7% to -2.0%) | 1351 (100) | -8.6% (-9.0% to -8.2%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 6283 | 5932 (102) | 68% | 67% | -4.4% (-6.8% to -2.0%) | 1358 (109) | -8.6% (-9.0% to -8.2%) | -0.7% (-0.9% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 5929 | 5631 (101) | 67% | 66% | -4.7% (-7.6% to -1.9%) | 1073 (103) | -6.6% (-7.3% to -5.9%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 5460 | 5182 (95) | 69% | 68% | -4.8% (-7.5% to -2.0%) | 620 (94) | -11.4% (-12.1% to -10.8%) | -0.8% (-1.1% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 5178 | 4950 (102) | 64% | 63% | -3.1% (-5.7% to -0.6%) | 1791 (100) | -4.5% (-4.9% to -4.1%) | +0.1% (-0.1% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 4589 | 4312 (98) | 70% | 69% | -4.5% (-7.0% to -1.8%) | 499 (104) | -9.4% (-10.0% to -8.8%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 4462 | 4068 (84) | 66% | 66% | -3.5% (-6.5% to -0.7%) | 1194 (96) | -5.5% (-6.0% to -4.9%) | -0.1% (-0.5% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 3837 | 3621 (102) | 64% | 64% | -4.7% (-7.5% to -1.8%) | 1326 (108) | -8.6% (-9.0% to -8.2%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 3616 | 3421 (89) | 72% | 71% | -4.2% (-6.9% to -1.6%) | 200 (78) | -9.4% (-10.4% to -8.5%) | -0.8% (-1.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 2923 | 2563 (100) | 63% | 64% | -5.8% (-9.2% to -2.3%) | 1154 (115) | -4.2% (-4.7% to -3.6%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 2676 | 2520 (102) | 63% | 62% | -4.5% (-7.4% to -1.3%) | 1167 (109) | -8.5% (-8.8% to -8.1%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 2519 | 2376 (101) | 62% | 62% | -4.4% (-7.6% to -1.5%) | 1125 (109) | -3.9% (-4.3% to -3.5%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2400 | 2270 (75) | 74% | 73% | -3.6% (-6.1% to -1.1%) | 41 (28) | -7.8% (-9.6% to -6.2%) | +0.0% (-0.7% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1902 | 1808 (102) | 55% | 55% | -1.7% (-6.1% to +2.9%) | 1713 (106) | -3.5% (-3.8% to -3.2%) | -0.0% (-0.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1746 | 1672 (102) | 62% | 61% | -3.7% (-7.0% to -0.6%) | 910 (100) | -7.9% (-8.3% to -7.5%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1710 | 1476 (101) | 47% | 49% | -2.5% (-8.4% to +3.3%) | 1488 (115) | -0.6% (-0.9% to -0.2%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1466 | 1402 (101) | 62% | 63% | -5.2% (-8.9% to -1.6%) | 403 (93) | -2.9% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1466 | 1402 (101) | 62% | 63% | -5.2% (-8.9% to -1.6%) | 403 (93) | -2.9% (-3.4% to -2.5%) | +0.3% (+0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1315 | 1271 (101) | 49% | 50% | -2.1% (-8.4% to +4.5%) | 1204 (99) | -1.8% (-2.0% to -1.5%) | +0.6% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1309 | 1265 (101) | 49% | 50% | -2.4% (-8.8% to +4.2%) | 1198 (99) | -1.7% (-2.0% to -1.4%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1309 | 1265 (101) | 49% | 50% | -2.4% (-8.8% to +4.2%) | 1198 (99) | -1.7% (-2.0% to -1.4%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1296 | 1243 (102) | 60% | 62% | -8.6% (-11.8% to -5.3%) | 872 (100) | -5.7% (-6.0% to -5.3%) | -0.3% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1296 | 1243 (102) | 60% | 62% | -8.6% (-11.8% to -5.3%) | 872 (100) | -5.7% (-6.0% to -5.3%) | -0.3% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1406 | 1152 (102) | 50% | 53% | -6.9% (-12.2% to -1.5%) | 1206 (116) | -2.3% (-2.6% to -1.9%) | -0.2% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 1158 | 1120 (99) | 62% | 61% | -1.4% (-6.0% to +2.9%) | 517 (96) | -3.7% (-4.3% to -3.1%) | +0.3% (-0.1% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 1158 | 1120 (99) | 62% | 61% | -1.4% (-6.0% to +2.9%) | 517 (96) | -3.7% (-4.3% to -3.1%) | +0.3% (-0.1% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1120 | 1069 (92) | 59% | 60% | -4.9% (-9.3% to -0.3%) | 626 (94) | -3.2% (-3.6% to -2.8%) | -0.4% (-0.6% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 1023 | 990 (100) | 49% | 51% | -1.6% (-8.6% to +5.0%) | 922 (98) | -1.9% (-2.2% to -1.5%) | +0.7% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 992 | 954 (97) | 49% | 53% | -5.5% (-12.2% to +1.3%) | 883 (97) | -2.1% (-2.3% to -1.8%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 939 | 891 (96) | 65% | 64% | -3.2% (-7.2% to +0.7%) | 233 (85) | -4.1% (-4.7% to -3.6%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 939 | 891 (96) | 65% | 64% | -3.2% (-7.2% to +0.7%) | 233 (85) | -4.1% (-4.7% to -3.6%) | +0.2% (-0.0% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 897 | 842 (101) | 63% | 60% | +0.9% (-4.0% to +5.7%) | 467 (98) | -4.3% (-4.8% to -3.7%) | -0.3% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 897 | 842 (101) | 63% | 60% | +0.9% (-4.0% to +5.7%) | 467 (98) | -4.3% (-4.8% to -3.7%) | -0.3% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 863 | 832 (97) | 49% | 52% | -6.2% (-13.5% to +0.8%) | 759 (95) | -2.4% (-2.6% to -2.1%) | -0.0% (-0.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 903 | 697 (101) | 46% | 46% | +1.1% (-6.5% to +8.5%) | 777 (115) | +1.0% (+0.6% to +1.5%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 737 | 685 (102) | 65% | 62% | -0.8% (-6.2% to +4.4%) | 665 (105) | -6.6% (-6.9% to -6.3%) | -0.8% (-1.1% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 716 | 681 (75) | 69% | 68% | -4.4% (-8.7% to -0.2%) | 16 (12) | -19.9% (-22.6% to -17.0%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 716 | 681 (75) | 69% | 68% | -4.4% (-8.7% to -0.2%) | 16 (12) | -19.9% (-22.6% to -17.0%) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| status change = yes | 683 | 655 (59) | 57% | 53% | +7.4% (+0.7% to +13.8%) | 617 (57) | -2.3% (-2.6% to -2.0%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 614 | 584 (100) | 46% | 46% | +1.2% (-6.6% to +9.2%) | 589 (102) | +0.1% (-0.2% to +0.5%) | +0.5% (+0.1% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 575 | 548 (75) | 71% | 69% | -2.7% (-7.2% to +1.5%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| stat/market = pa | 575 | 548 (75) | 71% | 69% | -2.7% (-7.2% to +1.5%) | 6 (6) | -14.6% (6 games) | -4.4% (2 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 528 | 500 (82) | 64% | 68% | -11.0% (-17.5% to -4.4%) | 48 (33) | -8.0% (-10.8% to -5.1%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 528 | 500 (82) | 64% | 68% | -11.0% (-17.5% to -4.4%) | 48 (33) | -8.0% (-10.8% to -5.1%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 500 | 307 (92) | 44% | 48% | -3.6% (-14.1% to +6.4%) | 380 (105) | +2.6% (+1.9% to +3.2%) | -1.5% (-2.0% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 317 | 307 (92) | 44% | 48% | -3.6% (-14.1% to +6.4%) | 299 (89) | +1.7% (+1.1% to +2.3%) | -1.3% (-1.8% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 286 | 275 (77) | 46% | 49% | -5.2% (-18.8% to +8.5%) | 276 (77) | -1.3% (-1.8% to -0.7%) | +0.6% (+0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 339 | 272 (90) | 44% | 48% | -4.2% (-14.8% to +5.9%) | 294 (99) | +1.7% (+1.1% to +2.3%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 183 | 174 (74) | 44% | 46% | -0.5% (-15.9% to +16.8%) | 177 (75) | +2.2% (+1.5% to +3.1%) | -1.7% (-2.4% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 177 | 165 (73) | 72% | 62% | +10.6% (-0.6% to +21.1%) | 165 (73) | -5.7% (-6.2% to -5.2%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 177 | 165 (73) | 72% | 62% | +10.6% (-0.6% to +21.1%) | 165 (73) | -5.7% (-6.2% to -5.2%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 142 | 133 (64) | 44% | 50% | -7.7% (-24.8% to +8.7%) | 126 (65) | +0.9% (-0.0% to +1.8%) | -1.0% (-1.8% to -0.1%) | hypothesis (range includes zero) |
| tier = Lean | 99 | 96 (56) | 54% | 57% | -3.6% (-17.6% to +11.1%) | 90 (55) | -2.6% (-3.5% to -1.8%) | -1.0% (-1.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 80 | 74 (46) | 65% | 67% | -6.2% (-24.4% to +11.5%) | 74 (46) | -3.4% (-4.3% to -2.4%) | -0.0% (-0.9% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 95 | 74 (46) | 65% | 67% | -6.2% (-24.4% to +11.5%) | 82 (52) | -3.5% (-4.4% to -2.6%) | -0.1% (-1.0% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 56 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 56 | 47 (30) | 70% | 61% | +7.2% (-14.1% to +25.1%) | 47 (30) | -5.6% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 46 | 41 (26) | 61% | 68% | -12.4% (-34.3% to +11.7%) | 43 (28) | -3.3% (-4.2% to -2.5%) | +0.1% (-0.7% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 46 | 41 (26) | 61% | 68% | -12.4% (-34.3% to +11.7%) | 43 (28) | -3.3% (-4.2% to -2.5%) | +0.1% (-0.7% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 164 | 38 (21) | 45% | 48% | +4.1% (-31.3% to +42.9%) | 89 (36) | +5.3% (+3.8% to +7.0%) | -3.1% (-4.8% to -1.6%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 30-40% | 52 | 34 (27) | 41% | 38% | +12.6% (-27.0% to +55.1%) | 42 (33) | +4.8% (+3.2% to +6.4%) | +1.1% (-0.8% to +2.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 49 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 49 | 33 (20) | 70% | 67% | +1.6% (-24.4% to +26.8%) | 39 (24) | -3.8% (-5.2% to -2.0%) | -0.4% (-1.8% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
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
