# Research lab report

Built 2026-11-16T11:10:29Z UTC from 4448 logged code candidates (4024 settled, 1799 with a close, 76 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 2986, ROI -5.2%; CLV n 745 over 70 games, -7.9%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 226, ROI -5.1%; CLV n 292 over 70 games, +2.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 812, ROI -3.4%; CLV n 762 over 62 games, -1.6%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 4024, ROI -4.8%; CLV n 1713 over 62 games, -3.9%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 86 over 14 games, +3.7%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 1197, ROI -5.2%; CLV n 630 over 70 games, -7.6%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 55, ROI -2.4%; CLV n 51 over 32 games, -2.4%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 1789, ROI -5.1%; CLV n 115 over 46 games, -9.1%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI +1.2%; CLV n 46 over 29 games, -3.2%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 476, ROI +0.3%; CLV n 290 over 62 games, -3.5%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -9.6%; CLV n 514 over 62 games, -5.3%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 741, ROI -7.0%; CLV n 256 over 57 games, -2.2%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 597, ROI -1.9%; CLV n 307 over 59 games, -2.4%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 102, ROI +10.1%; CLV n 102 over 44 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 467, ROI -4.7%; CLV n 139 over 51 games, -3.9%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 253, ROI -11.1%; CLV n 26 over 19 games, -3.4%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 67 over 14 games, +6.0%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1155, ROI -1.4%; CLV n 1084 over 68 games, -3.3%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2830, ROI -6.3%; CLV n 602 over 65 games, -5.0%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 67 over 14 games, +6.0%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 3271, ROI -3.2%; CLV n 993 over 66 games, -4.7%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 753, ROI -11.7%; CLV n 806 over 76 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 2207, ROI -5.3%; CLV n 294 over 66 games, -8.8%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 533, ROI -5.9%; CLV n 480 over 60 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 483, ROI -2.2%; CLV n 553 over 76 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 801, ROI -4.2%; CLV n 472 over 62 games, -7.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 1760, ROI -4.2%; CLV n 723 over 69 games, -7.8%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 605, ROI -4.7%; CLV n 554 over 62 games, -2.0%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 30 over 12 games, +7.0%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative ROI (settled 1176, ROI -6.5%; CLV n 22 over 15 games, -8.6%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 2978, ROI -5.2%; CLV n 737 over 70 games, -7.9%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 197, ROI -5.1%; CLV n 220 over 67 games, +1.6%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 819, ROI -3.3%; CLV n 769 over 62 games, -1.7%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 30, ROI -0.9%; CLV n 73 over 29 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 681, ROI -8.2%; CLV n 425 over 63 games, -2.7%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 1930, ROI -2.1%; CLV n 669 over 58 games, -4.5%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1413, ROI -6.9%; CLV n 705 over 69 games, -3.2%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1376, ROI -7.3%; CLV n 738 over 75 games, -3.2%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 2648, ROI -3.5%; CLV n 1061 over 62 games, -3.8%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 3609, ROI -5.5%; CLV n 1414 over 76 games, -4.0%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 415, ROI +1.3%; CLV n 385 over 38 games, -2.0%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 226, ROI -5.1%; CLV n 221 over 56 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 812, ROI -3.4%; CLV n 762 over 62 games, -1.6%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2986, ROI -5.2%; CLV n 730 over 62 games, -7.9%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 71 over 14 games, +5.7%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 125, ROI -11.1%; CLV n 130 over 52 games, +1.9%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 632, ROI -0.4%; CLV n 582 over 62 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 180, ROI -14.3%; CLV n 180 over 47 games, -1.0%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 422, ROI -3.9%; CLV n 407 over 67 games, -6.4%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2525, ROI -5.5%; CLV n 292 over 56 games, -10.7%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 67 over 14 games, +6.0%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 476, ROI +0.3%; CLV n 290 over 62 games, -3.5%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 712, ROI -9.6%; CLV n 514 over 62 games, -5.3%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 741, ROI -7.0%; CLV n 256 over 57 games, -2.2%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 597, ROI -1.9%; CLV n 307 over 59 games, -2.4%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 102, ROI +10.1%; CLV n 102 over 44 games, -5.6%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI +1.2%; CLV n 39 over 24 games, -3.0%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 467, ROI -4.7%; CLV n 139 over 51 games, -3.9%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 253, ROI -11.1%; CLV n 26 over 19 games, -3.4%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 67 over 14 games, +6.0%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 4448 | 4024 (64) | 63% | 63% | -4.8% (-8.1% to -1.8%) | 1799 (76) | -3.5% (-3.9% to -3.1%) | -0.2% (-0.4% to +0.0%) |  |
| sport = nba | 4246 | 4024 (64) | 63% | 63% | -4.8% (-8.1% to -1.8%) | 1713 (62) | -3.9% (-4.2% to -3.6%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 4016 | 3609 (63) | 64% | 64% | -5.5% (-9.2% to -2.2%) | 1414 (76) | -4.0% (-4.4% to -3.5%) | -0.3% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 3468 | 3271 (64) | 66% | 65% | -3.2% (-7.0% to +0.2%) | 993 (66) | -4.7% (-5.2% to -4.2%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 3202 | 2986 (64) | 68% | 68% | -5.2% (-8.8% to -1.7%) | 745 (70) | -7.9% (-8.3% to -7.4%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 3173 | 2986 (64) | 68% | 68% | -5.2% (-8.8% to -1.7%) | 730 (62) | -7.9% (-8.4% to -7.4%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 3194 | 2978 (64) | 68% | 68% | -5.2% (-8.7% to -1.8%) | 737 (70) | -7.9% (-8.4% to -7.5%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 3000 | 2830 (63) | 66% | 66% | -6.3% (-10.8% to -2.1%) | 602 (65) | -5.0% (-5.8% to -4.2%) | -0.5% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 2799 | 2648 (64) | 63% | 63% | -3.5% (-7.5% to -0.1%) | 1061 (62) | -3.8% (-4.2% to -3.3%) | +0.1% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 2680 | 2525 (57) | 69% | 69% | -5.5% (-9.6% to -1.5%) | 292 (56) | -10.7% (-11.3% to -9.9%) | -0.9% (-1.3% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 2383 | 2207 (60) | 70% | 70% | -5.3% (-9.0% to -1.7%) | 294 (66) | -8.8% (-9.4% to -8.2%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 2205 | 1930 (46) | 67% | 65% | -2.1% (-6.4% to +2.0%) | 669 (58) | -4.5% (-5.3% to -3.6%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 1910 | 1789 (51) | 72% | 71% | -5.1% (-9.3% to -1.2%) | 115 (46) | -9.1% (-10.2% to -8.1%) | -0.9% (-1.4% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 1898 | 1760 (64) | 64% | 64% | -4.2% (-8.1% to -0.4%) | 723 (69) | -7.8% (-8.3% to -7.3%) | -0.6% (-0.9% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1518 | 1413 (63) | 60% | 62% | -6.9% (-11.6% to -2.3%) | 705 (69) | -3.2% (-3.6% to -2.8%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1649 | 1376 (62) | 61% | 63% | -7.3% (-11.6% to -2.6%) | 738 (75) | -3.2% (-3.9% to -2.6%) | -0.6% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 1292 | 1197 (64) | 62% | 62% | -5.2% (-8.7% to -1.2%) | 630 (70) | -7.6% (-8.1% to -7.2%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1249 | 1176 (37) | 73% | 73% | -6.5% (-10.3% to -2.8%) | 22 (15) | -8.6% (-11.7% to -6.2%) | -0.5% (-1.6% to +0.5%) | IN-SAMPLE SIGNAL: negative ROI |
| side = under | 1224 | 1155 (64) | 55% | 55% | -1.4% (-6.4% to +3.4%) | 1084 (68) | -3.3% (-3.7% to -2.9%) | +0.0% (-0.3% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1189 | 983 (64) | 47% | 49% | -3.9% (-10.2% to +2.2%) | 1003 (76) | -0.4% (-0.8% to +0.1%) | +0.1% (-0.3% to +0.4%) | hypothesis (range includes zero) |
| edge = 0-3% | 848 | 819 (64) | 48% | 50% | -3.3% (-10.4% to +4.0%) | 769 (62) | -1.7% (-2.0% to -1.3%) | +0.7% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 841 | 812 (64) | 48% | 50% | -3.4% (-10.8% to +4.0%) | 762 (62) | -1.6% (-2.0% to -1.2%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 841 | 812 (64) | 48% | 50% | -3.4% (-10.8% to +4.0%) | 762 (62) | -1.6% (-2.0% to -1.2%) | +0.7% (+0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 841 | 801 (64) | 62% | 61% | -4.2% (-8.6% to +0.3%) | 472 (62) | -7.0% (-7.6% to -6.5%) | -0.6% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 980 | 753 (64) | 47% | 53% | -11.7% (-18.4% to -5.0%) | 806 (76) | -2.1% (-2.5% to -1.6%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 782 | 741 (63) | 60% | 62% | -7.0% (-12.2% to -2.2%) | 256 (57) | -2.2% (-2.6% to -1.8%) | +0.4% (+0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 782 | 741 (63) | 60% | 62% | -7.0% (-12.2% to -2.2%) | 256 (57) | -2.2% (-2.6% to -1.8%) | +0.4% (+0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 744 | 712 (64) | 59% | 62% | -9.6% (-14.4% to -5.0%) | 514 (62) | -5.3% (-5.7% to -4.8%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 744 | 712 (64) | 59% | 62% | -9.6% (-14.4% to -5.0%) | 514 (62) | -5.3% (-5.7% to -4.8%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 725 | 681 (60) | 56% | 59% | -8.2% (-13.2% to -2.9%) | 425 (63) | -2.7% (-3.1% to -2.2%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 655 | 632 (64) | 50% | 51% | -0.4% (-7.9% to +6.4%) | 582 (62) | -1.8% (-2.3% to -1.3%) | +0.6% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 631 | 605 (62) | 49% | 53% | -4.7% (-12.6% to +3.0%) | 554 (62) | -2.0% (-2.3% to -1.6%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 616 | 597 (61) | 60% | 59% | -1.9% (-8.8% to +4.7%) | 307 (59) | -2.4% (-3.0% to -1.7%) | +0.4% (-0.2% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 616 | 597 (61) | 60% | 59% | -1.9% (-8.8% to +4.7%) | 307 (59) | -2.4% (-3.0% to -1.7%) | +0.4% (-0.2% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 552 | 533 (62) | 49% | 52% | -5.9% (-14.2% to +2.1%) | 480 (60) | -2.3% (-2.7% to -2.0%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 672 | 483 (64) | 44% | 46% | -2.2% (-11.2% to +6.4%) | 553 (76) | +1.2% (+0.7% to +1.8%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 512 | 476 (63) | 61% | 59% | +0.3% (-6.0% to +6.9%) | 290 (62) | -3.5% (-4.1% to -2.8%) | -0.3% (-0.9% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 512 | 476 (63) | 61% | 59% | +0.3% (-6.0% to +6.9%) | 290 (62) | -3.5% (-4.1% to -2.8%) | -0.3% (-0.9% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 493 | 467 (58) | 63% | 64% | -4.7% (-10.8% to +0.6%) | 139 (51) | -3.9% (-4.6% to -3.2%) | +0.0% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 493 | 467 (58) | 63% | 64% | -4.7% (-10.8% to +0.6%) | 139 (51) | -3.9% (-4.6% to -3.2%) | +0.0% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 463 | 422 (64) | 63% | 62% | -3.9% (-11.1% to +3.3%) | 407 (67) | -6.4% (-6.8% to -6.0%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 432 | 415 (40) | 54% | 53% | +1.3% (-6.6% to +9.4%) | 385 (38) | -2.0% (-2.3% to -1.6%) | +0.1% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 436 | 413 (64) | 44% | 46% | -3.1% (-11.9% to +6.2%) | 417 (66) | +0.3% (-0.2% to +0.8%) | +0.5% (-0.1% to +1.0%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 356 | 337 (37) | 69% | 69% | -4.9% (-11.2% to +1.7%) | 8 (6) | -20.1% (6 games) | -3.4% (–) | hypothesis (range includes zero) |
| stat/market = pr | 356 | 337 (37) | 69% | 69% | -4.9% (-11.2% to +1.7%) | 8 (6) | -20.1% (6 games) | -3.4% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 284 | 271 (37) | 71% | 70% | -3.4% (-9.2% to +2.0%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 284 | 271 (37) | 71% | 70% | -3.4% (-9.2% to +2.0%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 267 | 253 (44) | 64% | 69% | -11.1% (-20.6% to -2.2%) | 26 (19) | -3.4% (-6.7% to -0.1%) | -1.8% (-3.5% to -0.1%) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 267 | 253 (44) | 64% | 69% | -11.1% (-20.6% to -2.2%) | 26 (19) | -3.4% (-6.7% to -0.1%) | -1.8% (-3.5% to -0.1%) | IN-SAMPLE SIGNAL: negative ROI |
| lane = value | 405 | 226 (58) | 44% | 48% | -5.1% (-17.2% to +6.6%) | 292 (70) | +2.5% (+1.8% to +3.2%) | -1.7% (-2.2% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 232 | 226 (58) | 44% | 48% | -5.1% (-17.2% to +6.6%) | 221 (56) | +1.5% (+0.9% to +2.0%) | -1.6% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 3-6% | 258 | 197 (58) | 44% | 48% | -5.1% (-18.0% to +7.0%) | 220 (67) | +1.6% (+1.1% to +2.1%) | -1.2% (-1.6% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 186 | 180 (47) | 42% | 49% | -14.3% (-29.6% to +2.5%) | 180 (47) | -1.0% (-1.6% to -0.2%) | +0.9% (+0.3% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 134 | 125 (50) | 39% | 46% | -11.1% (-28.9% to +6.3%) | 130 (52) | +1.9% (+1.1% to +2.8%) | -2.1% (-2.9% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 112 | 102 (44) | 73% | 63% | +10.1% (-5.6% to +23.8%) | 102 (44) | -5.6% (-6.3% to -4.9%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 112 | 102 (44) | 73% | 63% | +10.1% (-5.6% to +23.8%) | 102 (44) | -5.6% (-6.3% to -4.9%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 106 | 101 (44) | 50% | 50% | +2.2% (-17.1% to +21.5%) | 95 (44) | +0.8% (-0.2% to +1.9%) | -0.9% (-1.8% to -0.0%) | hypothesis (range includes zero) |
| tier = Lean | 57 | 55 (33) | 55% | 57% | -2.4% (-21.2% to +17.7%) | 51 (32) | -2.4% (-3.7% to -1.1%) | -1.2% (-2.3% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = moneyline | 45 | 39 (24) | 69% | 66% | +1.2% (-24.9% to +23.5%) | 39 (24) | -3.0% (-4.5% to -1.3%) | +0.4% (-1.0% to +2.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 59 | 39 (24) | 69% | 66% | +1.2% (-24.9% to +23.5%) | 46 (29) | -3.2% (-4.5% to -1.7%) | +0.2% (-1.1% to +1.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 148 | 30 (16) | 43% | 48% | -0.9% (-41.8% to +44.3%) | 73 (29) | +5.3% (+3.6% to +7.3%) | -3.1% (-5.1% to -1.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = blk | 35 | 29 (19) | 66% | 61% | +1.7% (-27.9% to +28.7%) | 29 (19) | -5.5% (-6.4% to -4.5%) | -1.2% (-2.3% to -0.5%) | hypothesis |
| stat/market = blk | 35 | 29 (19) | 66% | 61% | +1.7% (-27.9% to +28.7%) | 29 (19) | -5.5% (-6.4% to -4.5%) | -1.2% (-2.3% to -0.5%) | hypothesis |
| lane = likely, side = away | 37 | 21 (12) | 57% | 67% | -16.3% (-51.5% to +19.4%) | 27 (16) | -3.8% (-5.5% to -1.3%) | -0.3% (-2.1% to +2.1%) | hypothesis |
| side = away | 37 | 21 (12) | 57% | 67% | -16.3% (-51.5% to +19.4%) | 27 (16) | -3.8% (-5.5% to -1.3%) | -0.3% (-2.1% to +2.1%) | hypothesis |
| chance = 30-40% | 37 | 20 (15) | 40% | 38% | +8.3% (-50.7% to +71.0%) | 28 (21) | +4.3% (+3.1% to +5.6%) | +0.2% (-1.6% to +2.2%) | hypothesis |
| lane = likely, side = home | 22 | 18 (12) | 83% | 66% | +21.6% (-7.4% to +46.5%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| side = home | 22 | 18 (12) | 83% | 66% | +21.6% (-7.4% to +46.5%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| chance = 10-20% | 90 | 0 (0) | – | – | – (–) | 30 (12) | +7.0% (+4.1% to +11.3%) | -1.1% (-3.5% to +1.8%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 52 | 0 (0) | – | – | – (–) | 25 (12) | +6.1% (+4.4% to +8.0%) | -1.6% (-2.6% to -0.6%) | hypothesis |
| lane = likely, sport = nfl | 28 | 0 (0) | – | – | – (–) | 15 (8) | -5.7% (8 games) | -0.8% (8 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 165 | 0 (0) | – | – | – (–) | 67 (14) | +6.0% (+4.6% to +8.1%) | -2.1% (-3.7% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 173 | 0 (0) | – | – | – (–) | 71 (14) | +5.7% (+4.3% to +7.6%) | -2.2% (-3.7% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 165 | 0 (0) | – | – | – (–) | 67 (14) | +6.0% (+4.6% to +8.1%) | -2.1% (-3.7% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 201 | 0 (0) | – | – | – (–) | 86 (14) | +3.7% (+2.1% to +5.8%) | -1.9% (-3.2% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 165 | 0 (0) | – | – | – (–) | 67 (14) | +6.0% (+4.6% to +8.1%) | -2.1% (-3.7% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 13 | 0 (0) | – | – | – (–) | 7 (5) | -4.4% (5 games) | -1.3% (5 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 165 | 0 (0) | – | – | – (–) | 67 (14) | +6.0% (+4.6% to +8.1%) | -2.1% (-3.7% to -0.3%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
