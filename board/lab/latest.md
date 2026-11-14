# Research lab report

Built 2026-11-14T11:10:21Z UTC from 3089 logged code candidates (2880 settled, 1346 with a close, 50 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 2056, ROI -5.5%; CLV n 557 over 49 games, -7.4%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 191, ROI -1.6%; CLV n 190 over 45 games, +1.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 633, ROI -1.8%; CLV n 599 over 48 games, -1.6%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2880, ROI -4.4%; CLV n 1342 over 48 games, -3.5%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 820, ROI -4.7%; CLV n 472 over 49 games, -7.2%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI +1.1%; CLV n 36 over 24 games, -2.0%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 785, ROI -1.9%; CLV n 753 over 50 games, -0.7%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 1236, ROI -6.0%; CLV n 85 over 35 games, -8.4%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 344, ROI +0.4%; CLV n 223 over 48 games, -3.3%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 534, ROI -7.9%; CLV n 395 over 48 games, -4.8%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 522, ROI -5.7%; CLV n 202 over 46 games, -2.1%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 424, ROI -1.3%; CLV n 239 over 45 games, -1.7%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 96, ROI +13.9%; CLV n 96 over 40 games, -5.6%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 330, ROI -4.0%; CLV n 107 over 39 games, -3.8%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 169, ROI -14.5%; CLV n 17 over 13 games, -0.8%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 227, ROI -8.1%; CLV n 5 over 3 games, -18.2%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 927, ROI +0.7%; CLV n 871 over 49 games, -3.2%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1925, ROI -7.0%; CLV n 444 over 47 games, -4.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 2286, ROI -3.0%; CLV n 769 over 48 games, -4.1%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 594, ROI -9.8%; CLV n 577 over 50 games, -2.8%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 1522, ROI -6.5%; CLV n 216 over 45 games, -8.2%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 410, ROI -3.0%; CLV n 376 over 48 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 398, ROI -0.9%; CLV n 398 over 50 games, +0.7%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 550, ROI -2.1%; CLV n 356 over 48 games, -6.7%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 1184, ROI -4.5%; CLV n 544 over 49 games, -7.3%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 472, ROI -2.2%; CLV n 438 over 48 games, -1.9%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative ROI (settled 822, ROI -6.7%; CLV n 13 over 10 games, -10.6%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 2048, ROI -5.6%; CLV n 549 over 49 games, -7.5%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 165, ROI -2.8%; CLV n 163 over 45 games, +1.3%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 640, ROI -1.7%; CLV n 606 over 48 games, -1.6%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 511, ROI -8.9%; CLV n 322 over 44 games, -2.6%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 1409, ROI -0.2%; CLV n 486 over 35 games, -4.6%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 960, ROI -8.2%; CLV n 538 over 49 games, -3.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1081, ROI -6.3%; CLV n 570 over 49 games, -4.0%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 1799, ROI -3.2%; CLV n 776 over 48 games, -3.2%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2538, ROI -5.6%; CLV n 1035 over 50 games, -4.0%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 342, ROI +4.5%; CLV n 311 over 29 games, -1.8%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 191, ROI -1.6%; CLV n 187 over 43 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 633, ROI -1.8%; CLV n 599 over 48 games, -1.6%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2056, ROI -5.5%; CLV n 556 over 48 games, -7.4%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 107, ROI -13.3%; CLV n 108 over 40 games, +1.9%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI +0.9%; CLV n 455 over 48 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 146, ROI -10.9%; CLV n 144 over 38 games, -0.9%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 356, ROI -2.5%; CLV n 337 over 49 games, -6.2%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1672, ROI -6.3%; CLV n 192 over 40 games, -10.0%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 344, ROI +0.4%; CLV n 223 over 48 games, -3.3%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 534, ROI -7.9%; CLV n 395 over 48 games, -4.8%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 522, ROI -5.7%; CLV n 202 over 46 games, -2.1%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 424, ROI -1.3%; CLV n 239 over 45 games, -1.7%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 96, ROI +13.9%; CLV n 96 over 40 games, -5.6%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 330, ROI -4.0%; CLV n 107 over 39 games, -3.8%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 169, ROI -14.5%; CLV n 17 over 13 games, -0.8%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 227, ROI -8.1%; CLV n 5 over 3 games, -18.2%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 3089 | 2880 (50) | 62% | 63% | -4.4% (-8.5% to -0.4%) | 1346 (50) | -3.5% (-3.9% to -3.2%) | -0.1% (-0.3% to +0.1%) |  |
| sport = nba | 2981 | 2880 (50) | 62% | 63% | -4.4% (-8.5% to -0.4%) | 1342 (48) | -3.5% (-3.9% to -3.2%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 2741 | 2538 (49) | 63% | 64% | -5.6% (-10.4% to -1.3%) | 1035 (50) | -4.0% (-4.5% to -3.6%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 2367 | 2286 (50) | 66% | 65% | -3.0% (-7.9% to +1.6%) | 769 (48) | -4.1% (-4.6% to -3.6%) | +0.1% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 2152 | 2056 (50) | 68% | 68% | -5.5% (-9.8% to -1.1%) | 557 (49) | -7.4% (-7.9% to -6.9%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 2137 | 2056 (50) | 68% | 68% | -5.5% (-9.8% to -1.1%) | 556 (48) | -7.4% (-7.9% to -6.9%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 2144 | 2048 (50) | 68% | 68% | -5.6% (-10.3% to -1.4%) | 549 (49) | -7.5% (-8.0% to -7.0%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 1990 | 1925 (49) | 65% | 66% | -7.0% (-13.0% to -1.4%) | 444 (47) | -4.2% (-5.0% to -3.2%) | -0.6% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 1861 | 1799 (50) | 63% | 63% | -3.2% (-9.0% to +1.8%) | 776 (48) | -3.2% (-3.6% to -2.7%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 1730 | 1672 (43) | 69% | 69% | -6.3% (-11.7% to -0.7%) | 192 (40) | -10.0% (-11.0% to -9.1%) | -1.0% (-1.5% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 1599 | 1522 (46) | 70% | 70% | -6.5% (-11.4% to -1.6%) | 216 (45) | -8.2% (-8.7% to -7.6%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 1533 | 1409 (35) | 68% | 65% | -0.2% (-5.4% to +4.6%) | 486 (35) | -4.6% (-5.3% to -3.9%) | +0.1% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 1288 | 1236 (37) | 71% | 72% | -6.0% (-11.2% to -1.1%) | 85 (35) | -8.4% (-9.5% to -7.2%) | -0.8% (-1.3% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 1246 | 1184 (50) | 64% | 64% | -4.5% (-9.6% to +0.9%) | 544 (49) | -7.3% (-7.8% to -6.8%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1228 | 1081 (48) | 61% | 63% | -6.3% (-11.2% to -0.9%) | 570 (49) | -4.0% (-4.5% to -3.5%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1016 | 960 (49) | 58% | 61% | -8.2% (-14.1% to -2.2%) | 538 (49) | -3.1% (-3.6% to -2.6%) | +0.0% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 969 | 927 (50) | 56% | 55% | +0.7% (-4.8% to +6.5%) | 871 (49) | -3.2% (-3.7% to -2.8%) | +0.1% (-0.2% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 851 | 822 (23) | 73% | 73% | -6.7% (-11.5% to -2.3%) | 13 (10) | -10.6% (-15.2% to -6.6%) | -1.4% (5 games) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 864 | 820 (50) | 63% | 62% | -4.7% (-9.5% to +0.2%) | 472 (49) | -7.2% (-7.8% to -6.7%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 897 | 785 (50) | 48% | 49% | -1.9% (-9.3% to +5.3%) | 753 (50) | -0.7% (-1.2% to -0.3%) | +0.2% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 656 | 640 (50) | 49% | 50% | -1.7% (-10.7% to +7.0%) | 606 (48) | -1.6% (-2.0% to -1.1%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 649 | 633 (50) | 49% | 50% | -1.8% (-10.7% to +7.0%) | 599 (48) | -1.6% (-2.0% to -1.1%) | +0.7% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 649 | 633 (50) | 49% | 50% | -1.8% (-10.7% to +7.0%) | 599 (48) | -1.6% (-2.0% to -1.1%) | +0.7% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 722 | 594 (50) | 49% | 53% | -9.8% (-16.4% to -3.6%) | 577 (50) | -2.8% (-3.1% to -2.4%) | -0.2% (-0.5% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 569 | 550 (50) | 63% | 61% | -2.1% (-7.5% to +3.9%) | 356 (48) | -6.7% (-7.3% to -6.1%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 551 | 534 (50) | 59% | 61% | -7.9% (-13.5% to -2.8%) | 395 (48) | -4.8% (-5.3% to -4.3%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 551 | 534 (50) | 59% | 61% | -7.9% (-13.5% to -2.8%) | 395 (48) | -4.8% (-5.3% to -4.3%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 539 | 522 (49) | 60% | 62% | -5.7% (-12.8% to +0.5%) | 202 (46) | -2.1% (-2.5% to -1.6%) | +0.3% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 539 | 522 (49) | 60% | 62% | -5.7% (-12.8% to +0.5%) | 202 (46) | -2.1% (-2.5% to -1.6%) | +0.3% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 540 | 511 (47) | 55% | 59% | -8.9% (-15.0% to -2.7%) | 322 (44) | -2.6% (-3.1% to -2.1%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 501 | 487 (50) | 50% | 51% | +0.9% (-8.3% to +9.8%) | 455 (48) | -1.8% (-2.4% to -1.2%) | +0.7% (+0.2% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 487 | 472 (50) | 51% | 53% | -2.2% (-11.7% to +6.6%) | 438 (48) | -1.9% (-2.3% to -1.5%) | -0.2% (-0.5% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 430 | 424 (47) | 59% | 58% | -1.3% (-10.0% to +7.0%) | 239 (45) | -1.7% (-2.3% to -1.0%) | +0.5% (-0.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 430 | 424 (47) | 59% | 58% | -1.3% (-10.0% to +7.0%) | 239 (45) | -1.7% (-2.3% to -1.0%) | +0.5% (-0.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 421 | 410 (50) | 50% | 52% | -3.0% (-13.2% to +6.5%) | 376 (48) | -2.3% (-2.7% to -1.9%) | -0.2% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 500 | 398 (50) | 45% | 46% | -0.9% (-10.2% to +8.7%) | 398 (50) | +0.7% (+0.2% to +1.2%) | +0.6% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 381 | 356 (50) | 64% | 62% | -2.5% (-10.1% to +5.0%) | 337 (49) | -6.2% (-6.6% to -5.8%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 362 | 344 (49) | 60% | 58% | +0.4% (-6.8% to +7.6%) | 223 (48) | -3.3% (-4.0% to -2.4%) | -0.3% (-0.9% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 362 | 344 (49) | 60% | 58% | +0.4% (-6.8% to +7.6%) | 223 (48) | -3.3% (-4.0% to -2.4%) | -0.3% (-0.9% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 348 | 342 (31) | 55% | 53% | +4.5% (-3.6% to +12.7%) | 311 (29) | -1.8% (-2.1% to -1.4%) | +0.1% (-0.2% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 346 | 334 (50) | 44% | 46% | -2.3% (-12.5% to +8.1%) | 331 (48) | +0.3% (-0.3% to +0.9%) | +0.6% (+0.1% to +1.2%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pra | 342 | 330 (44) | 64% | 64% | -4.0% (-11.5% to +2.9%) | 107 (39) | -3.8% (-4.7% to -3.0%) | -0.1% (-0.5% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 342 | 330 (44) | 64% | 64% | -4.0% (-11.5% to +2.9%) | 107 (39) | -3.8% (-4.7% to -3.0%) | -0.1% (-0.5% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 232 | 227 (23) | 68% | 70% | -8.1% (-15.5% to -1.4%) | 5 (3) | -18.2% (3 games) | -3.4% (–) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 232 | 227 (23) | 68% | 70% | -8.1% (-15.5% to -1.4%) | 5 (3) | -18.2% (3 games) | -3.4% (–) | IN-SAMPLE SIGNAL: negative ROI |
| lane = value | 288 | 191 (44) | 46% | 48% | -1.6% (-14.3% to +10.7%) | 190 (45) | +1.6% (+1.0% to +2.2%) | -1.6% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 195 | 191 (44) | 46% | 48% | -1.6% (-14.3% to +10.7%) | 187 (43) | +1.5% (+0.9% to +2.1%) | -1.6% (-2.1% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pa | 183 | 178 (23) | 70% | 70% | -6.1% (-13.7% to +1.2%) | 2 (2) | -10.6% (2 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 183 | 178 (23) | 70% | 70% | -6.1% (-13.7% to +1.2%) | 2 (2) | -10.6% (2 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 176 | 169 (30) | 62% | 69% | -14.5% (-25.8% to -2.9%) | 17 (13) | -0.8% (-4.1% to +2.6%) | -1.8% (-4.1% to +0.3%) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 176 | 169 (30) | 62% | 69% | -14.5% (-25.8% to -2.9%) | 17 (13) | -0.8% (-4.1% to +2.6%) | -1.8% (-4.1% to +0.3%) | IN-SAMPLE SIGNAL: negative ROI |
| edge = 3-6% | 198 | 165 (44) | 45% | 48% | -2.8% (-16.9% to +10.2%) | 163 (45) | +1.3% (+0.7% to +1.9%) | -1.2% (-1.8% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 148 | 146 (38) | 43% | 49% | -10.9% (-29.7% to +8.7%) | 144 (38) | -0.9% (-1.5% to -0.1%) | +0.9% (+0.3% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 112 | 107 (41) | 38% | 46% | -13.3% (-32.0% to +5.4%) | 108 (40) | +1.9% (+1.0% to +2.9%) | -2.1% (-3.0% to -1.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 103 | 96 (40) | 75% | 63% | +13.9% (-1.7% to +27.6%) | 96 (40) | -5.6% (-6.3% to -4.9%) | -0.4% (-1.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 103 | 96 (40) | 75% | 63% | +13.9% (-1.7% to +27.6%) | 96 (40) | -5.6% (-6.3% to -4.9%) | -0.4% (-1.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 87 | 84 (33) | 55% | 50% | +13.2% (-7.4% to +33.1%) | 79 (32) | +1.0% (-0.2% to +2.2%) | -0.8% (-1.9% to +0.2%) | hypothesis (range includes zero) |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| tier = Lean | 40 | 39 (26) | 56% | 57% | +1.1% (-20.5% to +24.2%) | 36 (24) | -2.0% (-3.6% to -0.3%) | -1.1% (-2.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 29 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| sport = nba, stat/market = moneyline | 34 | 28 (17) | 71% | 66% | +5.2% (-24.8% to +31.3%) | 28 (17) | -3.9% (-5.1% to -2.7%) | -0.5% (-1.6% to +0.6%) | hypothesis |
| stat/market = blk | 29 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| stat/market = moneyline | 41 | 28 (17) | 71% | 66% | +5.2% (-24.8% to +31.3%) | 28 (17) | -3.9% (-5.1% to -2.7%) | -0.5% (-1.6% to +0.6%) | hypothesis |
| edge = 6%+ | 91 | 27 (14) | 48% | 48% | +10.2% (-31.5% to +59.7%) | 28 (15) | +3.5% (+1.6% to +5.5%) | -3.3% (-5.5% to -1.5%) | hypothesis |
| chance = 30-40% | 26 | 18 (13) | 44% | 38% | +20.3% (-43.0% to +85.9%) | 17 (12) | +4.3% (+2.6% to +6.2%) | +1.1% (-1.6% to +4.2%) | hypothesis |
| lane = likely, side = home | 19 | 16 (10) | 81% | 66% | +18.2% (-13.6% to +46.0%) | 16 (10) | -2.6% (-4.4% to -1.0%) | +0.6% (-1.0% to +2.0%) | hypothesis |
| side = home | 19 | 16 (10) | 81% | 66% | +18.2% (-13.6% to +46.0%) | 16 (10) | -2.6% (-4.4% to -1.0%) | +0.6% (-1.0% to +2.0%) | hypothesis |
| lane = likely, side = away | 22 | 12 (7) | 58% | 67% | -12.1% (7 games) | 12 (7) | -5.6% (7 games) | -1.9% (7 games) | hypothesis |
| side = away | 22 | 12 (7) | 58% | 67% | -12.1% (7 games) | 12 (7) | -5.6% (7 games) | -1.9% (7 games) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 29 | 0 (0) | – | – | – (–) | 2 (2) | +5.8% (2 games) | +0.4% (2 games) | hypothesis |
| lane = likely, sport = nfl | 14 | 0 (0) | – | – | – (–) | 1 (1) | -9.2% (–) | -1.8% (–) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 89 | 0 (0) | – | – | – (–) | 3 (2) | +6.5% (2 games) | -0.4% (2 games) | hypothesis |
| lane = value, sport = nfl | 93 | 0 (0) | – | – | – (–) | 3 (2) | +6.5% (2 games) | -0.4% (2 games) | hypothesis |
| side = yes | 89 | 0 (0) | – | – | – (–) | 3 (2) | +6.5% (2 games) | -0.4% (2 games) | hypothesis |
| sport = nfl | 107 | 0 (0) | – | – | – (–) | 4 (2) | +2.6% (2 games) | -0.8% (2 games) | hypothesis |
| sport = nfl, stat/market = anytime_td | 89 | 0 (0) | – | – | – (–) | 3 (2) | +6.5% (2 games) | -0.4% (2 games) | hypothesis |
| sport = nfl, stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = moneyline | 6 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = receptions | 6 | 0 (0) | – | – | – (–) | 1 (1) | -9.2% (–) | -1.8% (–) | hypothesis |
| sport = nfl, stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 89 | 0 (0) | – | – | – (–) | 3 (2) | +6.5% (2 games) | -0.4% (2 games) | hypothesis |
| stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 6 | 0 (0) | – | – | – (–) | 1 (1) | -9.2% (–) | -1.8% (–) | hypothesis |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
