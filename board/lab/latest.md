# Research lab report

Built 2026-11-18T19:23:11Z UTC from 6433 logged code candidates (5285 settled, 2238 with a close, 90 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 4044, ROI -4.3%; CLV n 977 over 84 games, -8.3%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 267, ROI -5.4%; CLV n 338 over 82 games, +2.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 974, ROI -3.7%; CLV n 923 over 74 games, -1.7%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 5285, ROI -4.2%; CLV n 2144 over 75 games, -4.2%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 94 over 15 games, +4.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 1688, ROI -3.9%; CLV n 826 over 84 games, -8.0%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 68, ROI -3.0%; CLV n 64 over 38 games, -2.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 2356, ROI -4.6%; CLV n 151 over 57 games, -9.5%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 52, ROI -5.3%; CLV n 60 over 39 games, -3.3%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 601, ROI -0.9%; CLV n 350 over 74 games, -3.7%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 921, ROI -8.9%; CLV n 658 over 75 games, -5.5%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 991, ROI -6.2%; CLV n 313 over 70 games, -2.7%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 784, ROI +0.5%; CLV n 387 over 72 games, -2.9%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 126, ROI +9.8%; CLV n 126 over 55 games, -5.7%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 34, ROI +4.3%; CLV n 34 over 23 games, -5.4%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 610, ROI -3.2%; CLV n 173 over 62 games, -3.9%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 339, ROI -8.7%; CLV n 34 over 25 games, -5.3%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 461, ROI -5.8%; CLV n 12 over 8 games, -19.3%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1376, ROI -2.9%; CLV n 1300 over 81 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 3857, ROI -4.7%; CLV n 804 over 78 games, -5.6%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 25, ROI -11.5%; CLV n 31 over 19 games, -3.8%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 4362, ROI -3.1%; CLV n 1258 over 80 games, -5.3%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 923, ROI -9.5%; CLV n 980 over 90 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 2943, ROI -4.7%; CLV n 376 over 80 games, -9.1%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 646, ROI -6.7%; CLV n 590 over 72 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 563, ROI -1.9%; CLV n 640 over 89 games, +1.3%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1133, ROI -2.7%; CLV n 632 over 75 games, -7.5%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 2437, ROI -3.8%; CLV n 943 over 83 games, -8.3%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 738, ROI -5.6%; CLV n 684 over 74 games, -2.0%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 26, ROI +5.7%; CLV n 34 over 25 games, +4.6%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 35 over 13 games, +7.2%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 1557, ROI -4.9%; CLV n 34 over 22 games, -8.1%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 4036, ROI -4.3%; CLV n 969 over 84 games, -8.3%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 235, ROI -6.3%; CLV n 256 over 78 games, +1.6%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 980, ROI -3.5%; CLV n 929 over 74 games, -1.7%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 34, ROI +1.8%; CLV n 84 over 32 games, +5.5%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 846, ROI -3.9%; CLV n 520 over 74 games, -2.8%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 2708, ROI -3.5%; CLV n 871 over 71 games, -5.0%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1731, ROI -5.6%; CLV n 847 over 83 games, -3.5%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1788, ROI -6.4%; CLV n 893 over 89 games, -3.5%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 3497, ROI -3.1%; CLV n 1345 over 75 games, -4.2%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 4791, ROI -4.9%; CLV n 1778 over 90 games, -4.4%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 494, ROI +2.1%; CLV n 460 over 44 games, -2.1%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 267, ROI -5.4%; CLV n 260 over 67 games, +1.6%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 974, ROI -3.7%; CLV n 923 over 74 games, -1.7%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 4044, ROI -4.3%; CLV n 961 over 75 games, -8.3%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 78 over 15 games, +5.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 151, ROI -4.2%; CLV n 155 over 61 games, +2.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 736, ROI -3.0%; CLV n 685 over 74 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 238, ROI -5.8%; CLV n 238 over 59 games, -1.2%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 524, ROI -1.8%; CLV n 506 over 80 games, -6.6%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 25, ROI -11.5%; CLV n 31 over 19 games, -3.8%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 3468, ROI -4.6%; CLV n 411 over 69 games, -11.1%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 601, ROI -0.9%; CLV n 350 over 74 games, -3.7%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 921, ROI -8.9%; CLV n 658 over 75 games, -5.5%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 991, ROI -6.2%; CLV n 313 over 70 games, -2.7%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 784, ROI +0.5%; CLV n 387 over 72 games, -2.9%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 126, ROI +9.8%; CLV n 126 over 55 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 52, ROI -5.3%; CLV n 52 over 33 games, -3.2%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 34, ROI +4.3%; CLV n 34 over 23 games, -5.4%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 610, ROI -3.2%; CLV n 173 over 62 games, -3.9%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 339, ROI -8.7%; CLV n 34 over 25 games, -5.3%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 461, ROI -5.8%; CLV n 12 over 8 games, -19.3%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 6433 | 5285 (77) | 63% | 63% | -4.2% (-7.0% to -1.6%) | 2238 (90) | -3.9% (-4.2% to -3.5%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 6223 | 5285 (77) | 63% | 63% | -4.2% (-7.0% to -1.6%) | 2144 (75) | -4.2% (-4.6% to -3.9%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 5921 | 4791 (76) | 64% | 64% | -4.9% (-8.0% to -1.9%) | 1778 (90) | -4.4% (-4.8% to -3.9%) | -0.3% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 5225 | 4362 (77) | 66% | 65% | -3.1% (-6.2% to -0.3%) | 1258 (80) | -5.3% (-5.8% to -4.8%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 4906 | 4044 (77) | 68% | 67% | -4.3% (-7.3% to -1.4%) | 977 (84) | -8.3% (-8.7% to -7.8%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 4876 | 4044 (77) | 68% | 67% | -4.3% (-7.3% to -1.4%) | 961 (75) | -8.3% (-8.8% to -7.8%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 4898 | 4036 (77) | 68% | 67% | -4.3% (-7.2% to -1.4%) | 969 (84) | -8.3% (-8.8% to -7.8%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 4623 | 3857 (76) | 66% | 66% | -4.7% (-8.3% to -1.1%) | 804 (78) | -5.6% (-6.3% to -4.8%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 4104 | 3497 (77) | 64% | 63% | -3.1% (-6.7% to +0.0%) | 1345 (75) | -4.2% (-4.6% to -3.8%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 4209 | 3468 (70) | 69% | 68% | -4.6% (-8.0% to -1.2%) | 411 (69) | -11.1% (-12.0% to -10.3%) | -0.8% (-1.2% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 3598 | 2943 (73) | 70% | 70% | -4.7% (-7.7% to -1.6%) | 376 (80) | -9.1% (-9.8% to -8.5%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 3691 | 2708 (59) | 66% | 65% | -3.5% (-7.1% to +0.3%) | 871 (71) | -5.0% (-5.6% to -4.3%) | -0.2% (-0.5% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 2978 | 2437 (77) | 65% | 64% | -3.8% (-7.2% to -0.4%) | 943 (83) | -8.3% (-8.8% to -7.8%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 2840 | 2356 (64) | 72% | 71% | -4.6% (-7.9% to -1.4%) | 151 (57) | -9.5% (-10.7% to -8.4%) | -0.7% (-1.1% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 2329 | 1788 (75) | 62% | 64% | -6.4% (-10.7% to -2.4%) | 893 (89) | -3.5% (-4.0% to -2.9%) | -0.5% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1852 | 1731 (76) | 61% | 62% | -5.6% (-9.5% to -2.0%) | 847 (83) | -3.5% (-3.9% to -3.0%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 2066 | 1688 (77) | 63% | 62% | -3.9% (-7.3% to -0.2%) | 826 (84) | -8.0% (-8.5% to -7.6%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1873 | 1557 (50) | 74% | 73% | -4.9% (-8.0% to -1.9%) | 34 (22) | -8.1% (-10.1% to -6.3%) | -0.1% (-0.8% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1559 | 1376 (77) | 54% | 55% | -2.9% (-7.6% to +2.0%) | 1300 (81) | -3.5% (-3.8% to -3.1%) | -0.0% (-0.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1453 | 1173 (76) | 46% | 49% | -4.1% (-10.5% to +2.3%) | 1197 (89) | -0.4% (-0.8% to -0.0%) | +0.1% (-0.2% to +0.4%) | hypothesis (range includes zero) |
| price = -199 to -130 | 1341 | 1133 (77) | 63% | 61% | -2.7% (-6.7% to +1.1%) | 632 (75) | -7.5% (-8.0% to -7.0%) | -0.6% (-1.0% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1149 | 991 (76) | 61% | 63% | -6.2% (-10.8% to -1.8%) | 313 (70) | -2.7% (-3.2% to -2.2%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1149 | 991 (76) | 61% | 63% | -6.2% (-10.8% to -1.8%) | 313 (70) | -2.7% (-3.2% to -2.2%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1068 | 980 (76) | 48% | 50% | -3.5% (-10.8% to +3.7%) | 929 (74) | -1.7% (-2.0% to -1.3%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1062 | 974 (76) | 48% | 50% | -3.7% (-11.0% to +3.4%) | 923 (74) | -1.7% (-2.0% to -1.3%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1062 | 974 (76) | 48% | 50% | -3.7% (-11.0% to +3.4%) | 923 (74) | -1.7% (-2.0% to -1.3%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1208 | 923 (77) | 49% | 53% | -9.5% (-15.8% to -3.3%) | 980 (90) | -2.1% (-2.5% to -1.7%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1052 | 921 (77) | 59% | 62% | -8.9% (-13.1% to -4.8%) | 658 (75) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1052 | 921 (77) | 59% | 62% | -8.9% (-13.1% to -4.8%) | 658 (75) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 890 | 846 (72) | 58% | 59% | -3.9% (-8.9% to +1.4%) | 520 (74) | -2.8% (-3.2% to -2.5%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 901 | 784 (74) | 62% | 60% | +0.5% (-5.1% to +5.7%) | 387 (72) | -2.9% (-3.6% to -2.2%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 901 | 784 (74) | 62% | 60% | +0.5% (-5.1% to +5.7%) | 387 (72) | -2.9% (-3.6% to -2.2%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 805 | 738 (74) | 49% | 53% | -5.6% (-13.3% to +1.9%) | 684 (74) | -2.0% (-2.3% to -1.7%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 813 | 736 (76) | 49% | 51% | -3.0% (-10.4% to +4.3%) | 685 (74) | -1.8% (-2.2% to -1.4%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 704 | 646 (74) | 48% | 52% | -6.7% (-14.4% to +1.3%) | 590 (72) | -2.4% (-2.7% to -2.0%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 725 | 610 (71) | 64% | 64% | -3.2% (-8.3% to +1.6%) | 173 (62) | -3.9% (-4.6% to -3.3%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 725 | 610 (71) | 64% | 64% | -3.2% (-8.3% to +1.6%) | 173 (62) | -3.9% (-4.6% to -3.3%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 710 | 601 (76) | 61% | 60% | -0.9% (-6.3% to +4.5%) | 350 (74) | -3.7% (-4.3% to -3.1%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 710 | 601 (76) | 61% | 60% | -0.9% (-6.3% to +4.5%) | 350 (74) | -3.7% (-4.3% to -3.1%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 790 | 563 (76) | 44% | 46% | -1.9% (-10.1% to +6.8%) | 640 (89) | +1.3% (+0.8% to +1.8%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 618 | 524 (77) | 64% | 62% | -1.8% (-8.3% to +4.4%) | 506 (80) | -6.6% (-6.9% to -6.2%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 512 | 494 (46) | 54% | 53% | +2.1% (-5.4% to +9.2%) | 460 (44) | -2.1% (-2.4% to -1.8%) | -0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 528 | 477 (76) | 44% | 46% | -2.3% (-10.5% to +6.7%) | 482 (78) | +0.3% (-0.1% to +0.8%) | +0.5% (+0.0% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 565 | 461 (50) | 68% | 69% | -5.8% (-11.0% to -0.6%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 565 | 461 (50) | 68% | 69% | -5.8% (-11.0% to -0.6%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = pa | 440 | 366 (50) | 70% | 69% | -3.9% (-9.1% to +1.1%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 440 | 366 (50) | 70% | 69% | -3.9% (-9.1% to +1.1%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 420 | 339 (57) | 66% | 68% | -8.7% (-16.2% to -1.8%) | 34 (25) | -5.3% (-8.9% to -2.1%) | -2.0% (-4.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 420 | 339 (57) | 66% | 68% | -8.7% (-16.2% to -1.8%) | 34 (25) | -5.3% (-8.9% to -2.1%) | -2.0% (-4.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 465 | 267 (70) | 43% | 48% | -5.4% (-16.8% to +6.1%) | 338 (82) | +2.6% (+1.9% to +3.3%) | -1.6% (-2.1% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 285 | 267 (70) | 43% | 48% | -5.4% (-16.8% to +6.1%) | 260 (67) | +1.6% (+1.0% to +2.1%) | -1.5% (-1.9% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 249 | 238 (59) | 46% | 49% | -5.8% (-21.4% to +10.9%) | 238 (59) | -1.2% (-1.7% to -0.6%) | +0.7% (+0.2% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 308 | 235 (70) | 43% | 48% | -6.3% (-17.5% to +5.2%) | 256 (78) | +1.6% (+1.0% to +2.1%) | -1.2% (-1.6% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 165 | 151 (60) | 42% | 46% | -4.2% (-21.9% to +12.2%) | 155 (61) | +2.2% (+1.5% to +2.9%) | -1.7% (-2.4% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 152 | 126 (55) | 72% | 63% | +9.8% (-4.1% to +21.9%) | 126 (55) | -5.7% (-6.3% to -5.1%) | -0.5% (-1.1% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 152 | 126 (55) | 72% | 63% | +9.8% (-4.1% to +21.9%) | 126 (55) | -5.7% (-6.3% to -5.1%) | -0.5% (-1.1% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 128 | 116 (52) | 45% | 50% | -7.1% (-26.4% to +10.7%) | 109 (52) | +0.6% (-0.4% to +1.6%) | -1.2% (-2.1% to -0.3%) | hypothesis (range includes zero) |
| tier = Lean | 74 | 68 (39) | 54% | 57% | -3.0% (-20.0% to +13.8%) | 64 (38) | -2.5% (-3.5% to -1.5%) | -1.2% (-2.2% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 64 | 52 (33) | 65% | 67% | -5.3% (-26.1% to +14.7%) | 52 (33) | -3.2% (-4.3% to -1.8%) | +0.3% (-0.8% to +1.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 79 | 52 (33) | 65% | 67% | -5.3% (-26.1% to +14.7%) | 60 (39) | -3.3% (-4.3% to -2.1%) | +0.1% (-0.9% to +1.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| edge = 6%+ | 159 | 34 (18) | 44% | 48% | +1.8% (-36.4% to +43.0%) | 84 (32) | +5.5% (+3.9% to +7.3%) | -2.9% (-4.6% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = blk | 45 | 34 (23) | 68% | 61% | +4.3% (-23.2% to +28.2%) | 34 (23) | -5.4% (-6.3% to -4.3%) | -1.1% (-1.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 45 | 34 (23) | 68% | 61% | +4.3% (-23.2% to +28.2%) | 34 (23) | -5.4% (-6.3% to -4.3%) | -1.1% (-1.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 36 | 27 (18) | 70% | 68% | +0.5% (-27.4% to +24.3%) | 29 (20) | -2.8% (-3.8% to -1.8%) | +0.6% (-0.2% to +1.5%) | hypothesis |
| side = home | 36 | 27 (18) | 70% | 68% | +0.5% (-27.4% to +24.3%) | 29 (20) | -2.8% (-3.8% to -1.8%) | +0.6% (-0.2% to +1.5%) | hypothesis |
| chance = 30-40% | 46 | 26 (19) | 38% | 38% | +5.7% (-40.9% to +55.4%) | 34 (25) | +4.6% (+3.3% to +5.9%) | +0.8% (-0.9% to +2.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 43 | 25 (15) | 60% | 66% | -11.5% (-42.8% to +22.8%) | 31 (19) | -3.8% (-5.5% to -1.7%) | -0.4% (-2.0% to +1.7%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 43 | 25 (15) | 60% | 66% | -11.5% (-42.8% to +22.8%) | 31 (19) | -3.8% (-5.5% to -1.7%) | -0.4% (-2.0% to +1.7%) | IN-SAMPLE SIGNAL: negative CLV |
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
