# Research lab report

Built 2026-11-17T19:35:45Z UTC from 5651 logged code candidates (4839 settled, 2079 with a close, 85 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 3679, ROI -4.3%; CLV n 900 over 79 games, -8.2%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 255, ROI -3.9%; CLV n 327 over 78 games, +2.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 905, ROI -2.2%; CLV n 852 over 70 games, -1.6%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 4839, ROI -3.9%; CLV n 1985 over 70 games, -4.2%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 94 over 15 games, +4.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 1520, ROI -4.8%; CLV n 762 over 79 games, -8.0%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 65, ROI -3.9%; CLV n 61 over 36 games, -2.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 2159, ROI -4.0%; CLV n 138 over 53 games, -9.2%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI -4.2%; CLV n 55 over 35 games, -3.1%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 559, ROI -1.0%; CLV n 329 over 70 games, -3.6%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 846, ROI -8.4%; CLV n 605 over 70 games, -5.5%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 896, ROI -5.5%; CLV n 288 over 65 games, -2.6%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 721, ROI +0.9%; CLV n 361 over 67 games, -2.8%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 118, ROI +8.5%; CLV n 118 over 51 games, -5.6%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +7.4%; CLV n 33 over 22 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 556, ROI -3.1%; CLV n 157 over 58 games, -3.8%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 305, ROI -8.7%; CLV n 31 over 22 games, -4.9%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 422, ROI -6.0%; CLV n 12 over 8 games, -19.3%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1293, ROI -1.9%; CLV n 1216 over 76 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 3499, ROI -4.7%; CLV n 734 over 73 games, -5.4%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 24, ROI -14.4%; CLV n 30 over 18 games, -3.6%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 3978, ROI -2.6%; CLV n 1161 over 75 games, -5.1%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 861, ROI -10.0%; CLV n 918 over 85 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 2696, ROI -4.3%; CLV n 347 over 75 games, -8.9%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 598, ROI -5.7%; CLV n 542 over 68 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 533, ROI +0.3%; CLV n 609 over 85 games, +1.3%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1012, ROI -4.2%; CLV n 581 over 70 games, -7.4%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 2200, ROI -4.0%; CLV n 870 over 78 games, -8.1%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 683, ROI -4.2%; CLV n 629 over 70 games, -2.0%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 22, ROI +12.1%; CLV n 30 over 23 games, +4.3%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 35 over 13 games, +7.2%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 1429, ROI -4.7%; CLV n 30 over 20 games, -8.5%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 3671, ROI -4.4%; CLV n 892 over 79 games, -8.2%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 223, ROI -4.6%; CLV n 245 over 74 games, +1.5%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 911, ROI -2.0%; CLV n 858 over 70 games, -1.7%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 34, ROI +1.8%; CLV n 84 over 32 games, +5.5%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 806, ROI -4.9%; CLV n 495 over 70 games, -2.8%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 2405, ROI -2.2%; CLV n 786 over 66 games, -4.8%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1628, ROI -6.0%; CLV n 798 over 78 games, -3.4%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1641, ROI -6.2%; CLV n 839 over 84 games, -3.4%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 3198, ROI -2.8%; CLV n 1240 over 70 games, -4.0%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 4359, ROI -4.6%; CLV n 1633 over 85 games, -4.3%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 480, ROI +2.0%; CLV n 446 over 43 games, -2.1%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 255, ROI -3.9%; CLV n 249 over 63 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 905, ROI -2.2%; CLV n 852 over 70 games, -1.6%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 3679, ROI -4.3%; CLV n 884 over 70 games, -8.2%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 78 over 15 games, +5.9%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 144, ROI -1.5%; CLV n 148 over 58 games, +2.1%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 689, ROI -0.1%; CLV n 636 over 70 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 216, ROI -9.1%; CLV n 216 over 55 games, -1.0%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 493, ROI -3.3%; CLV n 475 over 75 games, -6.5%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 24, ROI -14.4%; CLV n 30 over 18 games, -3.6%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 3139, ROI -4.5%; CLV n 370 over 64 games, -11.0%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 559, ROI -1.0%; CLV n 329 over 70 games, -3.6%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 846, ROI -8.4%; CLV n 605 over 70 games, -5.5%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 896, ROI -5.5%; CLV n 288 over 65 games, -2.6%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 721, ROI +0.9%; CLV n 361 over 67 games, -2.8%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 118, ROI +8.5%; CLV n 118 over 51 games, -5.6%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI -4.2%; CLV n 47 over 29 games, -2.9%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI +7.4%; CLV n 33 over 22 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 556, ROI -3.1%; CLV n 157 over 58 games, -3.8%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 305, ROI -8.7%; CLV n 31 over 22 games, -4.9%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 422, ROI -6.0%; CLV n 12 over 8 games, -19.3%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 5651 | 4839 (72) | 63% | 63% | -3.9% (-6.8% to -1.2%) | 2079 (85) | -3.8% (-4.2% to -3.4%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 5441 | 4839 (72) | 63% | 63% | -3.9% (-6.8% to -1.2%) | 1985 (70) | -4.2% (-4.5% to -3.8%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 5149 | 4359 (71) | 64% | 64% | -4.6% (-7.9% to -1.7%) | 1633 (85) | -4.3% (-4.7% to -3.8%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 4518 | 3978 (72) | 67% | 65% | -2.6% (-5.8% to +0.3%) | 1161 (75) | -5.1% (-5.6% to -4.6%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 4235 | 3679 (72) | 68% | 67% | -4.3% (-7.5% to -1.3%) | 900 (79) | -8.2% (-8.6% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 4205 | 3679 (72) | 68% | 67% | -4.3% (-7.5% to -1.3%) | 884 (70) | -8.2% (-8.7% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 4227 | 3671 (72) | 68% | 68% | -4.4% (-7.5% to -1.4%) | 892 (79) | -8.2% (-8.6% to -7.7%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 3993 | 3499 (71) | 67% | 66% | -4.7% (-8.6% to -1.0%) | 734 (73) | -5.4% (-6.1% to -4.7%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 3600 | 3198 (72) | 64% | 63% | -2.8% (-6.1% to +0.4%) | 1240 (70) | -4.0% (-4.5% to -3.6%) | +0.0% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 3603 | 3139 (65) | 69% | 68% | -4.5% (-8.1% to -0.9%) | 370 (64) | -11.0% (-11.8% to -10.2%) | -0.9% (-1.2% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 3116 | 2696 (68) | 71% | 70% | -4.3% (-7.6% to -1.0%) | 347 (75) | -8.9% (-9.5% to -8.4%) | -0.7% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 3006 | 2405 (54) | 67% | 66% | -2.2% (-5.8% to +1.5%) | 786 (66) | -4.8% (-5.5% to -4.0%) | -0.2% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 2554 | 2200 (72) | 65% | 64% | -4.0% (-7.6% to -0.6%) | 870 (78) | -8.1% (-8.6% to -7.6%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 2468 | 2159 (59) | 72% | 71% | -4.0% (-7.6% to -0.7%) | 138 (53) | -9.2% (-10.2% to -8.2%) | -0.7% (-1.1% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 2051 | 1641 (70) | 62% | 64% | -6.2% (-10.8% to -1.8%) | 839 (84) | -3.4% (-4.0% to -2.8%) | -0.6% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1795 | 1628 (71) | 61% | 62% | -6.0% (-10.2% to -2.3%) | 798 (78) | -3.4% (-3.9% to -2.9%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 1767 | 1520 (72) | 63% | 62% | -4.8% (-8.3% to -1.1%) | 762 (79) | -8.0% (-8.4% to -7.5%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1626 | 1429 (45) | 74% | 73% | -4.7% (-8.3% to -1.4%) | 30 (20) | -8.5% (-10.8% to -6.5%) | -0.1% (-1.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1413 | 1293 (72) | 55% | 55% | -1.9% (-6.9% to +2.9%) | 1216 (76) | -3.5% (-3.8% to -3.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1348 | 1095 (72) | 47% | 49% | -2.5% (-8.8% to +3.7%) | 1118 (85) | -0.4% (-0.8% to +0.1%) | +0.1% (-0.2% to +0.4%) | hypothesis (range includes zero) |
| price = -199 to -130 | 1148 | 1012 (72) | 62% | 61% | -4.2% (-8.3% to -0.2%) | 581 (70) | -7.4% (-7.9% to -6.9%) | -0.6% (-1.0% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 976 | 911 (72) | 49% | 50% | -2.0% (-9.2% to +5.4%) | 858 (70) | -1.7% (-2.0% to -1.3%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 970 | 905 (72) | 49% | 50% | -2.2% (-9.4% to +4.9%) | 852 (70) | -1.6% (-2.0% to -1.3%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 970 | 905 (72) | 49% | 50% | -2.2% (-9.4% to +4.9%) | 852 (70) | -1.6% (-2.0% to -1.3%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1010 | 896 (71) | 62% | 63% | -5.5% (-10.4% to -1.2%) | 288 (65) | -2.6% (-3.0% to -2.1%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1010 | 896 (71) | 62% | 63% | -5.5% (-10.4% to -1.2%) | 288 (65) | -2.6% (-3.0% to -2.1%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1133 | 861 (72) | 48% | 53% | -10.0% (-16.3% to -3.8%) | 918 (85) | -2.1% (-2.5% to -1.6%) | -0.4% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 940 | 846 (72) | 60% | 62% | -8.4% (-12.8% to -4.1%) | 605 (70) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 940 | 846 (72) | 60% | 62% | -8.4% (-12.8% to -4.1%) | 605 (70) | -5.5% (-5.9% to -5.1%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 850 | 806 (67) | 58% | 59% | -4.9% (-10.4% to +0.6%) | 495 (70) | -2.8% (-3.2% to -2.4%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 794 | 721 (69) | 62% | 60% | +0.9% (-5.5% to +6.7%) | 361 (67) | -2.8% (-3.5% to -2.1%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 794 | 721 (69) | 62% | 60% | +0.9% (-5.5% to +6.7%) | 361 (67) | -2.8% (-3.5% to -2.1%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 737 | 689 (72) | 50% | 51% | -0.1% (-7.3% to +6.8%) | 636 (70) | -1.8% (-2.3% to -1.4%) | +0.6% (+0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 736 | 683 (70) | 50% | 53% | -4.2% (-11.8% to +3.2%) | 629 (70) | -2.0% (-2.3% to -1.7%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 641 | 598 (70) | 49% | 52% | -5.7% (-13.2% to +1.7%) | 542 (68) | -2.3% (-2.7% to -2.0%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 625 | 559 (71) | 61% | 59% | -1.0% (-6.8% to +4.8%) | 329 (70) | -3.6% (-4.2% to -2.9%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 625 | 559 (71) | 61% | 59% | -1.0% (-6.8% to +4.8%) | 329 (70) | -3.6% (-4.2% to -2.9%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 627 | 556 (66) | 65% | 64% | -3.1% (-8.2% to +1.7%) | 157 (58) | -3.8% (-4.5% to -3.1%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 627 | 556 (66) | 65% | 64% | -3.1% (-8.2% to +1.7%) | 157 (58) | -3.8% (-4.5% to -3.1%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 746 | 533 (72) | 45% | 46% | +0.3% (-8.2% to +8.8%) | 609 (85) | +1.3% (+0.8% to +1.8%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 559 | 493 (72) | 63% | 62% | -3.3% (-9.7% to +3.2%) | 475 (75) | -6.5% (-6.9% to -6.1%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 502 | 480 (45) | 54% | 53% | +2.0% (-5.7% to +9.3%) | 446 (43) | -2.1% (-2.5% to -1.8%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 489 | 455 (72) | 45% | 46% | -0.9% (-9.8% to +8.5%) | 459 (74) | +0.3% (-0.1% to +0.8%) | +0.5% (-0.0% to +0.9%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 481 | 422 (45) | 68% | 69% | -6.0% (-11.3% to -0.5%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 481 | 422 (45) | 68% | 69% | -6.0% (-11.3% to -0.5%) | 12 (8) | -19.3% (8 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = pa | 378 | 336 (45) | 71% | 69% | -3.5% (-9.2% to +1.9%) | 4 (4) | -16.1% (4 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 378 | 336 (45) | 71% | 69% | -3.5% (-9.2% to +1.9%) | 4 (4) | -16.1% (4 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 355 | 305 (52) | 66% | 68% | -8.7% (-16.8% to -1.3%) | 31 (22) | -4.9% (-8.1% to -1.7%) | -2.3% (-4.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 355 | 305 (52) | 66% | 68% | -8.7% (-16.8% to -1.3%) | 31 (22) | -4.9% (-8.1% to -1.7%) | -2.3% (-4.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 446 | 255 (66) | 44% | 48% | -3.9% (-16.2% to +7.2%) | 327 (78) | +2.5% (+1.9% to +3.2%) | -1.7% (-2.2% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 266 | 255 (66) | 44% | 48% | -3.9% (-16.2% to +7.2%) | 249 (63) | +1.5% (+0.9% to +2.0%) | -1.6% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 3-6% | 289 | 223 (66) | 44% | 48% | -4.6% (-16.5% to +7.2%) | 245 (74) | +1.5% (+0.9% to +2.0%) | -1.3% (-1.7% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 233 | 216 (55) | 44% | 49% | -9.1% (-24.4% to +8.2%) | 216 (55) | -1.0% (-1.5% to -0.3%) | +0.8% (+0.3% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 157 | 144 (57) | 44% | 46% | -1.5% (-19.4% to +16.1%) | 148 (58) | +2.1% (+1.4% to +2.8%) | -1.8% (-2.6% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 132 | 118 (51) | 71% | 63% | +8.5% (-6.1% to +21.6%) | 118 (51) | -5.6% (-6.2% to -5.0%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 132 | 118 (51) | 71% | 63% | +8.5% (-6.1% to +21.6%) | 118 (51) | -5.6% (-6.2% to -5.0%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 117 | 111 (49) | 45% | 50% | -7.0% (-26.6% to +11.6%) | 105 (49) | +0.5% (-0.5% to +1.5%) | -1.2% (-2.2% to -0.3%) | hypothesis (range includes zero) |
| tier = Lean | 68 | 65 (37) | 54% | 57% | -3.9% (-20.6% to +12.9%) | 61 (36) | -2.5% (-3.6% to -1.4%) | -1.3% (-2.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = moneyline | 58 | 47 (29) | 66% | 67% | -4.2% (-27.0% to +17.3%) | 47 (29) | -2.9% (-4.2% to -1.5%) | +0.5% (-0.7% to +1.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 73 | 47 (29) | 66% | 67% | -4.2% (-27.0% to +17.3%) | 55 (35) | -3.1% (-4.2% to -1.8%) | +0.3% (-0.8% to +1.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 159 | 34 (18) | 44% | 48% | +1.8% (-36.4% to +43.0%) | 84 (32) | +5.5% (+3.9% to +7.3%) | -2.9% (-4.6% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = blk | 41 | 33 (22) | 70% | 61% | +7.4% (-20.6% to +31.6%) | 33 (22) | -5.6% (-6.5% to -4.7%) | -1.1% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 41 | 33 (22) | 70% | 61% | +7.4% (-20.6% to +31.6%) | 33 (22) | -5.6% (-6.5% to -4.7%) | -1.1% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = away | 41 | 24 (14) | 58% | 66% | -14.4% (-47.4% to +19.6%) | 30 (18) | -3.6% (-5.2% to -1.3%) | -0.2% (-1.8% to +2.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 41 | 24 (14) | 58% | 66% | -14.4% (-47.4% to +19.6%) | 30 (18) | -3.6% (-5.2% to -1.3%) | -0.2% (-1.8% to +2.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = home | 32 | 23 (15) | 74% | 68% | +6.3% (-23.1% to +32.8%) | 25 (17) | -2.6% (-3.8% to -1.5%) | +0.8% (-0.2% to +1.7%) | hypothesis |
| side = home | 32 | 23 (15) | 74% | 68% | +6.3% (-23.1% to +32.8%) | 25 (17) | -2.6% (-3.8% to -1.5%) | +0.8% (-0.2% to +1.7%) | hypothesis |
| chance = 30-40% | 43 | 22 (17) | 41% | 38% | +12.1% (-43.7% to +68.6%) | 30 (23) | +4.3% (+3.2% to +5.5%) | +0.3% (-1.4% to +2.2%) | IN-SAMPLE SIGNAL: positive CLV |
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
