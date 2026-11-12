# Research lab report

Built 2026-11-12T01:38:01Z UTC from 1708 logged code candidates (652 settled, 774 with a close, 33 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 278 over 32 games, -6.5%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 106, ROI +0.8%; CLV n 122 over 30 games, +1.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 313, ROI -15.0%; CLV n 374 over 32 games, -1.8%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 652, ROI -7.2%; CLV n 772 over 32 games, -2.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 207, ROI -1.1%; CLV n 244 over 32 games, -6.3%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 400, ROI -11.7%; CLV n 474 over 33 games, -0.9%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 26, ROI +5.0%; CLV n 34 over 19 games, -7.8%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +16.1%; CLV n 119 over 32 games, -2.5%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 186, ROI -13.4%; CLV n 211 over 32 games, -3.9%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.8%; CLV n 132 over 30 games, -2.2%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 116, ROI -24.0%; CLV n 137 over 30 games, -1.1%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 48, ROI +18.4%; CLV n 62 over 25 games, -5.8%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 61, ROI -20.5%; CLV n 67 over 24 games, -3.4%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 457, ROI -3.3%; CLV n 535 over 32 games, -3.3%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 189, ROI -18.5%; CLV n 224 over 31 games, -1.9%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 350, ROI +3.2%; CLV n 414 over 32 games, -2.9%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 302, ROI -19.2%; CLV n 360 over 33 games, -2.9%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 92, ROI -3.5%; CLV n 107 over 28 games, -7.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 210, ROI -9.7%; CLV n 238 over 32 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: negative ROI (settled 202, ROI -13.5%; CLV n 250 over 33 games, +0.5%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 148, ROI +2.7%; CLV n 179 over 32 games, -5.7%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 276 over 32 games, -6.4%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 240, ROI -8.1%; CLV n 276 over 32 games, -1.9%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 229, ROI -0.8%; CLV n 274 over 32 games, -6.5%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 89, ROI -0.8%; CLV n 101 over 30 games, +1.3%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 316, ROI -14.9%; CLV n 377 over 32 games, -1.8%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 169, ROI -5.4%; CLV n 192 over 30 games, -2.2%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 148, ROI +4.8%; CLV n 227 over 19 games, -3.3%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 335, ROI -13.4%; CLV n 355 over 32 games, -3.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 280, ROI +1.7%; CLV n 329 over 32 games, -3.5%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 372, ROI -13.8%; CLV n 445 over 32 games, -2.5%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 482, ROI -11.2%; CLV n 566 over 33 games, -3.3%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 170, ROI +4.1%; CLV n 208 over 19 games, -2.0%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 106, ROI +0.8%; CLV n 120 over 29 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 313, ROI -15.0%; CLV n 374 over 32 games, -1.8%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 233, ROI -0.4%; CLV n 278 over 32 games, -6.5%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 52, ROI -9.8%; CLV n 64 over 27 games, +2.6%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 219, ROI -9.5%; CLV n 273 over 32 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 94, ROI -27.6%; CLV n 101 over 25 games, -1.2%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 184, ROI -0.1%; CLV n 206 over 32 games, -6.2%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -9.2%; CLV n 59 over 24 games, -8.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +16.1%; CLV n 119 over 32 games, -2.5%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 186, ROI -13.4%; CLV n 211 over 32 games, -3.9%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 110, ROI -10.8%; CLV n 132 over 30 games, -2.2%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 116, ROI -24.0%; CLV n 137 over 30 games, -1.1%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 48, ROI +18.4%; CLV n 62 over 25 games, -5.8%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 61, ROI -20.5%; CLV n 67 over 24 games, -3.4%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 1708 | 652 (27) | 51% | 54% | -7.2% (-13.7% to -0.9%) | 774 (33) | -2.9% (-3.2% to -2.6%) | -0.2% (-0.5% to +0.1%) |  |
| sport = nba | 1602 | 652 (27) | 51% | 54% | -7.2% (-13.7% to -0.9%) | 772 (32) | -2.9% (-3.3% to -2.6%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 1427 | 482 (26) | 50% | 55% | -11.2% (-18.7% to -3.8%) | 566 (33) | -3.3% (-3.8% to -2.8%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 676 | 457 (27) | 54% | 55% | -3.3% (-12.0% to +5.3%) | 535 (32) | -3.3% (-3.9% to -2.8%) | -0.1% (-0.6% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 659 | 400 (27) | 43% | 49% | -11.7% (-21.3% to -2.0%) | 474 (33) | -0.9% (-1.4% to -0.4%) | +0.1% (-0.3% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 1027 | 372 (27) | 45% | 53% | -13.8% (-23.5% to -4.7%) | 445 (32) | -2.5% (-3.0% to -2.1%) | +0.1% (-0.3% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 1163 | 350 (27) | 58% | 55% | +3.2% (-5.0% to +10.4%) | 414 (32) | -2.9% (-3.4% to -2.5%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 679 | 335 (26) | 48% | 54% | -13.4% (-22.7% to -4.7%) | 355 (32) | -3.0% (-3.7% to -2.4%) | -0.4% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 456 | 316 (27) | 42% | 50% | -14.9% (-27.3% to -1.9%) | 377 (32) | -1.8% (-2.2% to -1.3%) | +0.6% (+0.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 452 | 313 (27) | 42% | 50% | -15.0% (-27.3% to -2.3%) | 374 (32) | -1.8% (-2.2% to -1.3%) | +0.6% (+0.1% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 452 | 313 (27) | 42% | 50% | -15.0% (-27.3% to -2.3%) | 374 (32) | -1.8% (-2.2% to -1.3%) | +0.6% (+0.1% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 545 | 302 (27) | 44% | 53% | -19.2% (-29.5% to -9.8%) | 360 (33) | -2.9% (-3.3% to -2.5%) | -0.4% (-0.7% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 681 | 280 (25) | 59% | 56% | +1.7% (-6.5% to +9.7%) | 329 (32) | -3.5% (-4.2% to -2.8%) | -0.6% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 343 | 240 (27) | 48% | 53% | -8.1% (-21.4% to +5.1%) | 276 (32) | -1.9% (-2.4% to -1.4%) | -0.1% (-0.7% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 526 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 276 (32) | -6.4% (-6.9% to -5.9%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 1023 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 278 (32) | -6.5% (-7.0% to -5.9%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 1009 | 233 (27) | 66% | 62% | -0.4% (-9.9% to +8.5%) | 278 (32) | -6.5% (-7.0% to -5.9%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 1018 | 229 (27) | 66% | 62% | -0.8% (-10.1% to +8.0%) | 274 (32) | -6.5% (-7.0% to -6.0%) | -0.6% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 338 | 219 (27) | 45% | 51% | -9.5% (-24.2% to +4.3%) | 273 (32) | -1.9% (-2.6% to -1.3%) | +0.6% (-0.0% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 299 | 210 (27) | 47% | 52% | -9.7% (-25.9% to +5.9%) | 238 (32) | -2.4% (-2.9% to -1.8%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 365 | 207 (27) | 65% | 62% | -1.1% (-10.5% to +8.2%) | 244 (32) | -6.3% (-6.7% to -5.8%) | -0.5% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 378 | 202 (27) | 39% | 46% | -13.5% (-27.9% to -0.4%) | 250 (33) | +0.5% (-0.0% to +1.0%) | +0.3% (-0.1% to +0.8%) | IN-SAMPLE SIGNAL: negative ROI |
| side = over | 915 | 189 (26) | 42% | 51% | -18.5% (-36.8% to -3.2%) | 224 (31) | -1.9% (-2.8% to -1.1%) | -0.4% (-1.0% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 341 | 186 (27) | 51% | 57% | -13.4% (-22.3% to -5.5%) | 211 (32) | -3.9% (-4.4% to -3.4%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 341 | 186 (27) | 51% | 57% | -13.4% (-22.3% to -5.5%) | 211 (32) | -3.9% (-4.4% to -3.4%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 268 | 184 (27) | 66% | 62% | -0.1% (-11.6% to +10.7%) | 206 (32) | -6.2% (-6.7% to -5.6%) | -0.5% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 246 | 170 (27) | 39% | 46% | -13.6% (-28.9% to +0.7%) | 210 (32) | -0.0% (-0.6% to +0.5%) | +0.2% (-0.3% to +0.7%) | hypothesis (range includes zero) |
| status change = yes | 281 | 170 (16) | 54% | 53% | +4.1% (-8.8% to +16.3%) | 208 (19) | -2.0% (-2.4% to -1.5%) | -0.2% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 327 | 169 (25) | 50% | 52% | -5.4% (-15.2% to +5.0%) | 192 (30) | -2.2% (-2.7% to -1.8%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 702 | 148 (12) | 60% | 56% | +4.8% (-4.2% to +15.1%) | 227 (19) | -3.3% (-4.1% to -2.6%) | +0.4% (-0.2% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 244 | 148 (27) | 66% | 61% | +2.7% (-8.6% to +13.0%) | 179 (32) | -5.7% (-6.2% to -5.2%) | -0.5% (-1.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 228 | 116 (24) | 39% | 50% | -24.0% (-39.9% to -7.2%) | 137 (30) | -1.1% (-1.9% to -0.4%) | -0.0% (-0.7% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 228 | 116 (24) | 39% | 50% | -24.0% (-39.9% to -7.2%) | 137 (30) | -1.1% (-1.9% to -0.4%) | -0.0% (-0.7% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 282 | 110 (26) | 45% | 52% | -10.8% (-28.3% to +6.8%) | 132 (30) | -2.2% (-2.7% to -1.7%) | -0.0% (-0.5% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 282 | 110 (26) | 45% | 52% | -10.8% (-28.3% to +6.8%) | 132 (30) | -2.2% (-2.7% to -1.7%) | -0.0% (-0.5% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 233 | 106 (25) | 47% | 48% | +0.8% (-17.1% to +19.2%) | 122 (30) | +1.6% (+0.9% to +2.3%) | -1.7% (-2.3% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 141 | 106 (25) | 47% | 48% | +0.8% (-17.1% to +19.2%) | 120 (29) | +1.5% (+0.8% to +2.2%) | -1.7% (-2.3% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 205 | 100 (26) | 60% | 51% | +16.1% (-0.7% to +31.8%) | 119 (32) | -2.5% (-3.4% to -1.5%) | -0.6% (-1.5% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 205 | 100 (26) | 60% | 51% | +16.1% (-0.7% to +31.8%) | 119 (32) | -2.5% (-3.4% to -1.5%) | -0.6% (-1.5% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = over | 114 | 94 (21) | 35% | 49% | -27.6% (-47.1% to -4.8%) | 101 (25) | -1.2% (-1.9% to -0.4%) | +0.6% (+0.1% to +1.4%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 787 | 92 (23) | 66% | 64% | -3.5% (-20.0% to +11.2%) | 107 (28) | -7.5% (-8.2% to -6.8%) | -0.7% (-1.1% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 144 | 89 (25) | 47% | 48% | -0.8% (-18.5% to +16.5%) | 101 (30) | +1.3% (+0.5% to +2.0%) | -1.2% (-1.8% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pra | 180 | 61 (21) | 41% | 52% | -20.5% (-42.3% to -1.3%) | 67 (24) | -3.4% (-4.2% to -2.6%) | +0.0% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 180 | 61 (21) | 41% | 52% | -20.5% (-42.3% to -1.3%) | 67 (24) | -3.4% (-4.2% to -2.6%) | +0.0% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 70 | 54 (21) | 54% | 50% | +11.0% (-12.3% to +31.4%) | 56 (22) | +0.2% (-1.2% to +1.5%) | -1.7% (-3.0% to -0.5%) | hypothesis (range includes zero) |
| lane = value, side = over | 75 | 52 (23) | 40% | 46% | -9.8% (-39.7% to +19.5%) | 64 (27) | +2.6% (+1.4% to +3.8%) | -1.7% (-2.9% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 76 | 48 (20) | 77% | 63% | +18.4% (-3.9% to +36.5%) | 62 (25) | -5.8% (-6.7% to -4.8%) | -0.8% (-1.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 76 | 48 (20) | 77% | 63% | +18.4% (-3.9% to +36.5%) | 62 (25) | -5.8% (-6.7% to -4.8%) | -0.8% (-1.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 726 | 43 (20) | 60% | 62% | -9.2% (-31.2% to +12.4%) | 59 (24) | -8.2% (-9.1% to -7.3%) | -1.0% (-1.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 658 | 26 (14) | 73% | 66% | +5.0% (-15.1% to +27.4%) | 34 (19) | -7.8% (-9.7% to -6.2%) | -1.1% (-1.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Lean | 26 | 19 (12) | 58% | 57% | +4.0% (-24.0% to +31.9%) | 22 (15) | -2.1% (-3.8% to -0.8%) | -1.3% (-3.4% to +0.0%) | hypothesis |
| edge = 6%+ | 90 | 18 (9) | 50% | 48% | +15.4% (9 games) | 22 (12) | +3.0% (+1.1% to +5.4%) | -3.7% (-6.2% to -1.6%) | hypothesis |
| sport = nba, stat/market = blk | 23 | 16 (10) | 88% | 62% | +31.4% (+5.9% to +50.4%) | 21 (13) | -5.4% (-6.8% to -4.0%) | -0.7% (-1.4% to -0.2%) | hypothesis |
| stat/market = blk | 23 | 16 (10) | 88% | 62% | +31.4% (+5.9% to +50.4%) | 21 (13) | -5.4% (-6.8% to -4.0%) | -0.7% (-1.4% to -0.2%) | hypothesis |
| chance = 30-40% | 19 | 9 (6) | 22% | 38% | -39.3% (6 games) | 8 (5) | +5.9% (5 games) | +2.9% (5 games) | hypothesis |
| sport = nba, stat/market = ra | 76 | 9 (7) | 33% | 51% | -32.7% (7 games) | 10 (8) | +4.0% (8 games) | -0.2% (8 games) | hypothesis |
| stat/market = ra | 76 | 9 (7) | 33% | 51% | -32.7% (7 games) | 10 (8) | +4.0% (8 games) | -0.2% (8 games) | hypothesis |
| sport = nba, stat/market = moneyline | 22 | 6 (4) | 100% | 63% | +54.3% (4 games) | 13 (8) | -3.5% (8 games) | -0.3% (8 games) | hypothesis |
| stat/market = moneyline | 29 | 6 (4) | 100% | 63% | +54.3% (4 games) | 13 (8) | -3.5% (8 games) | -0.3% (8 games) | hypothesis |
| lane = likely, side = home | 12 | 4 (3) | 100% | 61% | +59.2% (3 games) | 7 (5) | -1.6% (5 games) | +1.3% (5 games) | hypothesis |
| side = home | 12 | 4 (3) | 100% | 61% | +59.2% (3 games) | 7 (5) | -1.6% (5 games) | +1.3% (5 games) | hypothesis |
| lane = likely, side = away | 17 | 2 (1) | 100% | 67% | +44.6% (–) | 6 (3) | -5.7% (3 games) | -2.2% (3 games) | hypothesis |
| side = away | 17 | 2 (1) | 100% | 67% | +44.6% (–) | 6 (3) | -5.7% (3 games) | -2.2% (3 games) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 1 (1) | +6.1% (–) | +0.7% (–) | hypothesis |
| chance = 70-80% | 442 | 0 (0) | – | – | – (–) | 2 (1) | -14.5% (–) | – (–) | hypothesis |
| chance = 80-90% | 55 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| sport = nba, stat/market = pa | 77 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nba, stat/market = pr | 92 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
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
| stat/market = pa | 77 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pr | 92 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
