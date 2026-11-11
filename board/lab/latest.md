# Research lab report

Built 2026-11-11T19:35:17Z UTC from 1439 logged code candidates (652 settled, 608 with a close, 26 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 210 over 25 games, -6.4%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 106, ROI +0.8%; CLV n 103 over 25 games, +1.5%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 313, ROI -15.0%; CLV n 295 over 25 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 652, ROI -7.2%; CLV n 606 over 25 games, -2.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 207, ROI -1.1%; CLV n 184 over 25 games, -6.4%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 400, ROI -11.7%; CLV n 381 over 26 games, -0.9%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +16.1%; CLV n 95 over 25 games, -2.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 186, ROI -13.4%; CLV n 165 over 25 games, -3.7%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.8%; CLV n 104 over 23 games, -2.3%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 116, ROI -24.0%; CLV n 111 over 23 games, -1.4%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 48, ROI +18.4%; CLV n 48 over 20 games, -6.0%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 61, ROI -20.5%; CLV n 52 over 18 games, -2.9%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 457, ROI -3.3%; CLV n 418 over 25 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 189, ROI -18.5%; CLV n 182 over 24 games, -1.4%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 350, ROI +3.2%; CLV n 323 over 25 games, -2.8%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 302, ROI -19.2%; CLV n 285 over 26 games, -2.9%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 92, ROI -3.5%; CLV n 82 over 21 games, -7.1%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 210, ROI -9.7%; CLV n 189 over 25 games, -2.5%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: negative ROI (settled 202, ROI -13.5%; CLV n 202 over 26 games, +0.4%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 148, ROI +2.7%; CLV n 135 over 25 games, -5.7%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 210 over 25 games, -6.4%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 240, ROI -8.1%; CLV n 220 over 25 games, -2.0%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 229, ROI -0.8%; CLV n 206 over 25 games, -6.5%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 89, ROI -0.8%; CLV n 85 over 25 games, +1.0%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 316, ROI -14.9%; CLV n 298 over 25 games, -1.8%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 169, ROI -5.4%; CLV n 164 over 23 games, -2.1%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 148, ROI +4.8%; CLV n 144 over 12 games, -3.4%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 335, ROI -13.4%; CLV n 300 over 25 games, -3.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 280, ROI +1.7%; CLV n 270 over 25 games, -3.4%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 372, ROI -13.8%; CLV n 338 over 25 games, -2.4%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 482, ROI -11.2%; CLV n 462 over 26 games, -3.1%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 170, ROI +4.1%; CLV n 146 over 14 games, -2.0%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 106, ROI +0.8%; CLV n 101 over 24 games, +1.4%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 313, ROI -15.0%; CLV n 295 over 25 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 210 over 25 games, -6.4%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 52, ROI -9.8%; CLV n 51 over 22 games, +2.4%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 219, ROI -9.5%; CLV n 202 over 25 games, -2.2%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 94, ROI -27.6%; CLV n 93 over 21 games, -1.1%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 184, ROI -0.1%; CLV n 166 over 25 games, -6.3%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -9.2%; CLV n 38 over 17 games, -7.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +16.1%; CLV n 95 over 25 games, -2.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 186, ROI -13.4%; CLV n 165 over 25 games, -3.7%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.8%; CLV n 104 over 23 games, -2.3%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 116, ROI -24.0%; CLV n 111 over 23 games, -1.4%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 48, ROI +18.4%; CLV n 48 over 20 games, -6.0%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 61, ROI -20.5%; CLV n 52 over 18 games, -2.9%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 1439 | 652 (27) | 51% | 54% | -7.2% (-13.7% to -0.9%) | 608 (26) | -2.8% (-3.2% to -2.5%) | -0.3% (-0.6% to -0.0%) |  |
| sport = nba | 1333 | 652 (27) | 51% | 54% | -7.2% (-13.7% to -0.9%) | 606 (25) | -2.9% (-3.2% to -2.5%) | -0.3% (-0.6% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 1241 | 482 (26) | 50% | 55% | -11.2% (-18.7% to -3.8%) | 462 (26) | -3.1% (-3.7% to -2.6%) | -0.3% (-0.6% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 598 | 457 (27) | 54% | 55% | -3.3% (-12.0% to +5.3%) | 418 (25) | -3.5% (-4.1% to -3.0%) | -0.3% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 587 | 400 (27) | 43% | 49% | -11.7% (-21.3% to -2.0%) | 381 (26) | -0.9% (-1.4% to -0.4%) | -0.0% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 849 | 372 (27) | 45% | 53% | -13.8% (-23.5% to -4.7%) | 338 (25) | -2.4% (-3.0% to -1.9%) | -0.1% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 951 | 350 (27) | 58% | 55% | +3.2% (-5.0% to +10.4%) | 323 (25) | -2.8% (-3.3% to -2.3%) | -0.2% (-0.5% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 539 | 335 (26) | 48% | 54% | -13.4% (-22.7% to -4.7%) | 300 (25) | -3.0% (-3.7% to -2.3%) | -0.4% (-0.9% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 402 | 316 (27) | 42% | 50% | -14.9% (-27.3% to -1.9%) | 298 (25) | -1.8% (-2.4% to -1.3%) | +0.5% (+0.0% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 398 | 313 (27) | 42% | 50% | -15.0% (-27.3% to -2.3%) | 295 (25) | -1.8% (-2.4% to -1.3%) | +0.5% (-0.0% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 398 | 313 (27) | 42% | 50% | -15.0% (-27.3% to -2.3%) | 295 (25) | -1.8% (-2.4% to -1.3%) | +0.5% (-0.0% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 488 | 302 (27) | 44% | 53% | -19.2% (-29.5% to -9.8%) | 285 (26) | -2.9% (-3.3% to -2.5%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 590 | 280 (25) | 59% | 56% | +1.7% (-6.5% to +9.7%) | 270 (25) | -3.4% (-4.1% to -2.6%) | -0.6% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 300 | 240 (27) | 48% | 53% | -8.1% (-21.4% to +5.1%) | 220 (25) | -2.0% (-2.5% to -1.4%) | -0.4% (-0.9% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 405 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 210 (25) | -6.4% (-7.1% to -5.7%) | -0.7% (-1.3% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 829 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 210 (25) | -6.4% (-7.1% to -5.7%) | -0.7% (-1.3% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 815 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 210 (25) | -6.4% (-7.1% to -5.7%) | -0.7% (-1.3% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 824 | 229 (27) | 66% | 62% | -0.8% (-10.1% to +8.0%) | 206 (25) | -6.5% (-7.1% to -5.9%) | -0.7% (-1.3% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 294 | 219 (27) | 45% | 51% | -9.5% (-24.2% to +4.3%) | 202 (25) | -2.2% (-2.9% to -1.4%) | +0.4% (-0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 264 | 210 (27) | 47% | 52% | -9.7% (-25.9% to +5.9%) | 189 (25) | -2.5% (-3.1% to -1.8%) | -0.5% (-1.0% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 298 | 207 (27) | 65% | 62% | -1.1% (-10.5% to +8.2%) | 184 (25) | -6.4% (-7.0% to -5.8%) | -0.7% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 339 | 202 (27) | 39% | 46% | -13.5% (-27.9% to -0.4%) | 202 (26) | +0.4% (-0.1% to +1.0%) | +0.2% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative ROI |
| side = over | 726 | 189 (26) | 42% | 51% | -18.5% (-36.8% to -3.2%) | 182 (24) | -1.4% (-2.2% to -0.5%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 295 | 186 (27) | 51% | 57% | -13.4% (-22.3% to -5.5%) | 165 (25) | -3.7% (-4.3% to -3.2%) | -0.0% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 295 | 186 (27) | 51% | 57% | -13.4% (-22.3% to -5.5%) | 165 (25) | -3.7% (-4.3% to -3.2%) | -0.0% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 242 | 184 (27) | 66% | 62% | -0.1% (-11.6% to +10.7%) | 166 (25) | -6.3% (-7.0% to -5.7%) | -0.7% (-1.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 214 | 170 (27) | 39% | 46% | -13.6% (-28.9% to +0.7%) | 168 (25) | -0.1% (-0.7% to +0.5%) | +0.2% (-0.3% to +0.7%) | hypothesis (range includes zero) |
| status change = yes | 198 | 170 (16) | 54% | 53% | +4.1% (-8.8% to +16.3%) | 146 (14) | -2.0% (-2.5% to -1.5%) | -0.4% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 198 | 169 (25) | 50% | 52% | -5.4% (-15.2% to +5.0%) | 164 (23) | -2.1% (-2.6% to -1.6%) | -0.5% (-0.9% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 702 | 148 (12) | 60% | 56% | +4.8% (-4.2% to +15.1%) | 144 (12) | -3.4% (-4.3% to -2.7%) | +0.2% (-0.4% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 207 | 148 (27) | 66% | 61% | +2.7% (-8.6% to +13.0%) | 135 (25) | -5.7% (-6.4% to -5.1%) | -0.6% (-1.2% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 176 | 116 (24) | 39% | 50% | -24.0% (-39.9% to -7.2%) | 111 (23) | -1.4% (-2.1% to -0.6%) | -0.3% (-1.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 176 | 116 (24) | 39% | 50% | -24.0% (-39.9% to -7.2%) | 111 (23) | -1.4% (-2.1% to -0.6%) | -0.3% (-1.0% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 227 | 110 (26) | 45% | 52% | -10.8% (-28.3% to +6.8%) | 104 (23) | -2.3% (-2.9% to -1.8%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 227 | 110 (26) | 45% | 52% | -10.8% (-28.3% to +6.8%) | 104 (23) | -2.3% (-2.9% to -1.8%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 212 | 106 (25) | 47% | 48% | +0.8% (-17.1% to +19.2%) | 103 (25) | +1.5% (+0.7% to +2.1%) | -1.8% (-2.5% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 120 | 106 (25) | 47% | 48% | +0.8% (-17.1% to +19.2%) | 101 (24) | +1.4% (+0.6% to +2.0%) | -1.8% (-2.5% to -1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 177 | 100 (26) | 60% | 51% | +16.1% (-0.7% to +31.8%) | 95 (25) | -2.4% (-3.5% to -1.4%) | -0.6% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 177 | 100 (26) | 60% | 51% | +16.1% (-0.7% to +31.8%) | 95 (25) | -2.4% (-3.5% to -1.4%) | -0.6% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = over | 104 | 94 (21) | 35% | 49% | -27.6% (-47.1% to -4.8%) | 93 (21) | -1.1% (-1.8% to -0.1%) | +0.8% (+0.2% to +1.6%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 629 | 92 (23) | 66% | 64% | -3.5% (-20.0% to +11.2%) | 82 (21) | -7.1% (-8.0% to -6.3%) | -0.8% (-1.4% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 129 | 89 (25) | 47% | 48% | -0.8% (-18.5% to +16.5%) | 85 (25) | +1.0% (+0.2% to +1.8%) | -1.3% (-2.0% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pra | 151 | 61 (21) | 41% | 52% | -20.5% (-42.3% to -1.3%) | 52 (18) | -2.9% (-3.5% to -2.2%) | +0.1% (-0.4% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 151 | 61 (21) | 41% | 52% | -20.5% (-42.3% to -1.3%) | 52 (18) | -2.9% (-3.5% to -2.2%) | +0.1% (-0.4% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 62 | 54 (21) | 54% | 50% | +11.0% (-12.3% to +31.4%) | 50 (20) | +0.3% (-1.2% to +1.7%) | -1.7% (-3.2% to -0.4%) | hypothesis (range includes zero) |
| lane = value, side = over | 62 | 52 (23) | 40% | 46% | -9.8% (-39.7% to +19.5%) | 51 (22) | +2.4% (+0.8% to +3.7%) | -1.9% (-3.4% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 67 | 48 (20) | 77% | 63% | +18.4% (-3.9% to +36.5%) | 48 (20) | -6.0% (-6.9% to -5.1%) | -1.2% (-2.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 67 | 48 (20) | 77% | 63% | +18.4% (-3.9% to +36.5%) | 48 (20) | -6.0% (-6.9% to -5.1%) | -1.2% (-2.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 560 | 43 (20) | 60% | 62% | -9.2% (-31.2% to +12.4%) | 38 (17) | -7.2% (-8.3% to -6.3%) | -0.8% (-1.6% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 531 | 26 (14) | 73% | 66% | +5.0% (-15.1% to +27.4%) | 26 (14) | -6.4% (-7.8% to -5.0%) | -1.0% (-1.8% to -0.1%) | hypothesis |
| tier = Lean | 23 | 19 (12) | 58% | 57% | +4.0% (-24.0% to +31.9%) | 17 (11) | -2.1% (-4.4% to -0.4%) | -1.3% (-4.2% to +0.4%) | hypothesis |
| edge = 6%+ | 84 | 18 (9) | 50% | 48% | +15.4% (9 games) | 19 (10) | +3.4% (+1.3% to +6.3%) | -3.8% (-6.7% to -1.5%) | hypothesis |
| sport = nba, stat/market = blk | 19 | 16 (10) | 88% | 62% | +31.4% (+5.9% to +50.4%) | 16 (10) | -6.0% (-7.4% to -4.5%) | -0.9% (-1.7% to -0.2%) | hypothesis |
| stat/market = blk | 19 | 16 (10) | 88% | 62% | +31.4% (+5.9% to +50.4%) | 16 (10) | -6.0% (-7.4% to -4.5%) | -0.9% (-1.7% to -0.2%) | hypothesis |
| chance = 30-40% | 19 | 9 (6) | 22% | 38% | -39.3% (6 games) | 8 (5) | +5.9% (5 games) | +2.9% (5 games) | hypothesis |
| sport = nba, stat/market = ra | 65 | 9 (7) | 33% | 51% | -32.7% (7 games) | 9 (7) | +4.8% (7 games) | +0.4% (7 games) | hypothesis |
| stat/market = ra | 65 | 9 (7) | 33% | 51% | -32.7% (7 games) | 9 (7) | +4.8% (7 games) | +0.4% (7 games) | hypothesis |
| sport = nba, stat/market = moneyline | 20 | 6 (4) | 100% | 63% | +54.3% (4 games) | 6 (4) | -2.0% (4 games) | +1.0% (4 games) | hypothesis |
| stat/market = moneyline | 27 | 6 (4) | 100% | 63% | +54.3% (4 games) | 6 (4) | -2.0% (4 games) | +1.0% (4 games) | hypothesis |
| lane = likely, side = home | 11 | 4 (3) | 100% | 61% | +59.2% (3 games) | 4 (3) | -0.6% (3 games) | +2.1% (3 games) | hypothesis |
| side = home | 11 | 4 (3) | 100% | 61% | +59.2% (3 games) | 4 (3) | -0.6% (3 games) | +2.1% (3 games) | hypothesis |
| lane = likely, side = away | 16 | 2 (1) | 100% | 67% | +44.6% (–) | 2 (1) | -4.8% (–) | -1.3% (–) | hypothesis |
| side = away | 16 | 2 (1) | 100% | 67% | +44.6% (–) | 2 (1) | -4.8% (–) | -1.3% (–) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 1 (1) | +6.1% (–) | +0.7% (–) | hypothesis |
| chance = 70-80% | 369 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| chance = 80-90% | 55 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| sport = nba, stat/market = pa | 62 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nba, stat/market = pr | 74 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl | 105 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| sport = nfl, stat/market = anytime_td | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| sport = nfl, stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = moneyline | 6 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pa | 62 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pr | 74 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
