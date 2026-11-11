# Research lab report

Built 2026-11-11T00:11:28Z UTC from 770 logged code candidates (455 settled, 414 with a close, 20 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 157, ROI -0.4%; CLV n 134 over 19 games, -6.6%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 71, ROI -4.0%; CLV n 69 over 19 games, +1.3%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 227, ROI -23.8%; CLV n 211 over 19 games, -2.0%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 455, ROI -12.6%; CLV n 412 over 19 games, -3.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 144, ROI -1.4%; CLV n 121 over 19 games, -6.6%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 285, ROI -19.7%; CLV n 269 over 20 games, -1.2%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 78, ROI +9.5%; CLV n 73 over 19 games, -2.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 125, ROI -12.8%; CLV n 102 over 19 games, -3.6%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 75, ROI -24.1%; CLV n 71 over 17 games, -2.4%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 85, ROI -27.8%; CLV n 80 over 17 games, -1.5%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 35, ROI +6.7%; CLV n 35 over 16 games, -6.8%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 40, ROI -32.3%; CLV n 34 over 13 games, -3.1%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 298, ROI -7.0%; CLV n 263 over 19 games, -4.1%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 155, ROI -24.3%; CLV n 147 over 18 games, -1.1%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 229, ROI -3.2%; CLV n 202 over 19 games, -3.1%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 226, ROI -22.1%; CLV n 212 over 20 games, -2.8%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 66, ROI -5.0%; CLV n 56 over 16 games, -7.0%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 137, ROI -23.8%; CLV n 121 over 19 games, -2.9%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: negative ROI (settled 154, ROI -16.8%; CLV n 152 over 20 games, +0.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 98, ROI +4.4%; CLV n 85 over 19 games, -5.9%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 157, ROI -0.4%; CLV n 134 over 19 games, -6.6%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 163, ROI -19.4%; CLV n 148 over 19 games, -2.2%)
- **chance = 40-50%**: IN-SAMPLE SIGNAL: negative ROI (settled 127, ROI -17.8%; CLV n 123 over 19 games, -0.5%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 155, ROI -1.2%; CLV n 132 over 19 games, -6.7%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 228, ROI -23.6%; CLV n 212 over 19 games, -2.0%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 138, ROI -10.0%; CLV n 133 over 18 games, -1.9%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 266, ROI -18.4%; CLV n 233 over 19 games, -3.3%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 200, ROI -0.4%; CLV n 190 over 19 games, -3.1%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 255, ROI -22.2%; CLV n 224 over 19 games, -2.8%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 340, ROI -18.0%; CLV n 320 over 20 games, -3.2%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 115, ROI +3.2%; CLV n 94 over 10 games, -2.1%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 71, ROI -4.0%; CLV n 67 over 18 games, +1.1%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 227, ROI -23.8%; CLV n 211 over 19 games, -2.0%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 157, ROI -0.4%; CLV n 134 over 19 games, -6.6%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 40, ROI -16.9%; CLV n 38 over 17 games, +3.2%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 143, ROI -17.9%; CLV n 128 over 19 games, -2.6%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative ROI (settled 84, ROI -33.8%; CLV n 83 over 17 games, -1.1%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 124, ROI +0.6%; CLV n 106 over 19 games, -6.5%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 78, ROI +9.5%; CLV n 73 over 19 games, -2.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 125, ROI -12.8%; CLV n 102 over 19 games, -3.6%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 75, ROI -24.1%; CLV n 71 over 17 games, -2.4%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 85, ROI -27.8%; CLV n 80 over 17 games, -1.5%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 35, ROI +6.7%; CLV n 35 over 16 games, -6.8%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 40, ROI -32.3%; CLV n 34 over 13 games, -3.1%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 770 | 455 (21) | 48% | 54% | -12.6% (-20.0% to -5.0%) | 414 (20) | -2.9% (-3.3% to -2.5%) | -0.4% (-0.8% to -0.0%) |  |
| sport = nba | 664 | 455 (21) | 48% | 54% | -12.6% (-20.0% to -5.0%) | 412 (19) | -3.0% (-3.4% to -2.6%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 599 | 340 (20) | 46% | 54% | -18.0% (-26.4% to -9.5%) | 320 (20) | -3.2% (-3.8% to -2.7%) | -0.3% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 473 | 298 (21) | 53% | 55% | -7.0% (-18.9% to +4.3%) | 263 (19) | -4.1% (-4.7% to -3.4%) | -0.7% (-1.3% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 491 | 285 (21) | 39% | 49% | -19.7% (-30.0% to -9.2%) | 269 (20) | -1.2% (-1.7% to -0.6%) | -0.2% (-0.8% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 376 | 266 (20) | 46% | 54% | -18.4% (-29.0% to -8.4%) | 233 (19) | -3.3% (-4.0% to -2.6%) | -0.5% (-0.9% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 379 | 255 (21) | 41% | 52% | -22.2% (-31.2% to -12.8%) | 224 (19) | -2.8% (-3.4% to -2.1%) | -0.4% (-1.0% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 362 | 229 (21) | 55% | 56% | -3.2% (-12.4% to +5.1%) | 202 (19) | -3.1% (-3.8% to -2.5%) | -0.3% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 318 | 228 (21) | 38% | 50% | -23.6% (-36.2% to -9.8%) | 212 (19) | -2.0% (-2.7% to -1.3%) | +0.4% (-0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 315 | 227 (21) | 37% | 50% | -23.8% (-36.6% to -10.3%) | 211 (19) | -2.0% (-2.7% to -1.3%) | +0.4% (-0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 315 | 227 (21) | 37% | 50% | -23.8% (-36.6% to -10.3%) | 211 (19) | -2.0% (-2.7% to -1.3%) | +0.4% (-0.2% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 408 | 226 (21) | 42% | 52% | -22.1% (-34.2% to -10.3%) | 212 (20) | -2.8% (-3.2% to -2.3%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 391 | 200 (19) | 57% | 56% | -0.4% (-11.1% to +9.6%) | 190 (19) | -3.1% (-3.9% to -2.3%) | -0.4% (-1.0% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 243 | 163 (21) | 42% | 52% | -19.4% (-32.2% to -6.0%) | 148 (19) | -2.2% (-2.9% to -1.5%) | -0.8% (-1.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 259 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 134 (19) | -6.6% (-7.1% to -6.0%) | -0.8% (-1.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 259 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 134 (19) | -6.6% (-7.1% to -6.0%) | -0.8% (-1.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 245 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 134 (19) | -6.6% (-7.1% to -6.0%) | -0.8% (-1.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 255 | 155 (21) | 65% | 62% | -1.2% (-13.4% to +10.2%) | 132 (19) | -6.7% (-7.2% to -6.1%) | -0.9% (-1.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 190 | 155 (20) | 39% | 51% | -24.3% (-43.6% to -7.0%) | 147 (18) | -1.1% (-2.0% to -0.1%) | +0.0% (-0.5% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 294 | 154 (21) | 38% | 46% | -16.8% (-31.6% to -3.4%) | 152 (20) | +0.2% (-0.4% to +0.9%) | +0.2% (-0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 228 | 144 (21) | 65% | 62% | -1.4% (-14.0% to +10.7%) | 121 (19) | -6.6% (-7.2% to -6.0%) | -0.8% (-1.3% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 222 | 143 (21) | 41% | 50% | -17.9% (-34.0% to -1.5%) | 128 (19) | -2.6% (-3.6% to -1.5%) | +0.0% (-0.9% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 189 | 138 (20) | 47% | 52% | -10.0% (-20.1% to +0.9%) | 133 (18) | -1.9% (-2.5% to -1.4%) | -0.4% (-0.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 210 | 137 (21) | 39% | 52% | -23.8% (-37.2% to -10.2%) | 121 (19) | -2.9% (-3.7% to -2.1%) | -0.9% (-1.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 174 | 127 (21) | 37% | 46% | -17.8% (-33.8% to -2.2%) | 123 (19) | -0.5% (-1.1% to +0.2%) | +0.2% (-0.4% to +0.8%) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = tpm | 186 | 125 (21) | 51% | 57% | -12.8% (-23.1% to -3.9%) | 102 (19) | -3.6% (-4.2% to -3.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 186 | 125 (21) | 51% | 57% | -12.8% (-23.1% to -3.9%) | 102 (19) | -3.6% (-4.2% to -3.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 196 | 124 (21) | 66% | 62% | +0.6% (-15.4% to +15.4%) | 106 (19) | -6.5% (-7.1% to -6.0%) | -0.9% (-1.4% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 171 | 115 (12) | 54% | 53% | +3.2% (-10.7% to +17.6%) | 94 (10) | -2.1% (-2.6% to -1.4%) | -0.8% (-1.1% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 153 | 98 (21) | 66% | 61% | +4.4% (-7.7% to +16.0%) | 85 (19) | -5.9% (-6.5% to -5.3%) | -0.8% (-1.3% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 113 | 85 (18) | 36% | 50% | -27.8% (-45.0% to -7.4%) | 80 (17) | -1.5% (-2.3% to -0.7%) | -0.5% (-1.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 113 | 85 (18) | 36% | 50% | -27.8% (-45.0% to -7.4%) | 80 (17) | -1.5% (-2.3% to -0.7%) | -0.5% (-1.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = over | 93 | 84 (17) | 32% | 49% | -33.8% (-54.2% to -9.5%) | 83 (17) | -1.1% (-1.8% to +0.0%) | +0.9% (+0.3% to +1.8%) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = ast | 105 | 78 (20) | 56% | 51% | +9.5% (-7.5% to +26.5%) | 73 (19) | -2.4% (-3.7% to -0.9%) | -0.6% (-1.9% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 105 | 78 (20) | 56% | 51% | +9.5% (-7.5% to +26.5%) | 73 (19) | -2.4% (-3.7% to -0.9%) | -0.6% (-1.9% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 111 | 75 (20) | 39% | 52% | -24.1% (-40.2% to -8.6%) | 71 (17) | -2.4% (-3.1% to -1.7%) | -0.4% (-1.1% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 111 | 75 (20) | 39% | 52% | -24.1% (-40.2% to -8.6%) | 71 (17) | -2.4% (-3.1% to -1.7%) | -0.4% (-1.1% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 196 | 71 (19) | 45% | 48% | -4.0% (-23.7% to +13.8%) | 69 (19) | +1.3% (+0.2% to +2.1%) | -2.1% (-2.7% to -1.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 104 | 71 (19) | 45% | 48% | -4.0% (-23.7% to +13.8%) | 67 (18) | +1.1% (+0.1% to +1.9%) | -2.1% (-2.8% to -1.5%) | IN-SAMPLE SIGNAL: positive CLV |
| price = -200 or shorter | 113 | 66 (18) | 65% | 64% | -5.0% (-24.3% to +12.4%) | 56 (16) | -7.0% (-7.9% to -6.2%) | -0.7% (-1.4% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 115 | 59 (19) | 49% | 48% | +4.3% (-18.0% to +22.0%) | 56 (19) | +0.4% (-0.6% to +1.1%) | -2.0% (-2.7% to -1.4%) | hypothesis (range includes zero) |
| flagged = 6h+ before | 205 | 51 (6) | 63% | 56% | +10.3% (6 games) | 48 (6) | -3.9% (6 games) | -0.3% (6 games) | too few games (<10) |
| lane = value, side = over | 53 | 40 (18) | 38% | 47% | -16.9% (-44.1% to +8.3%) | 38 (17) | +3.2% (+1.4% to +4.6%) | -1.2% (-2.5% to -0.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pra | 61 | 40 (16) | 35% | 52% | -32.3% (-52.1% to -13.5%) | 34 (13) | -3.1% (-3.9% to -2.3%) | +0.1% (-0.7% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 61 | 40 (16) | 35% | 52% | -32.3% (-52.1% to -13.5%) | 34 (13) | -3.1% (-3.9% to -2.3%) | +0.1% (-0.7% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = stl | 50 | 35 (16) | 71% | 63% | +6.7% (-21.3% to +29.1%) | 35 (16) | -6.8% (-7.5% to -6.0%) | -1.1% (-1.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 50 | 35 (16) | 71% | 63% | +6.7% (-21.3% to +29.1%) | 35 (16) | -6.8% (-7.5% to -6.0%) | -1.1% (-1.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 44 | 31 (15) | 61% | 62% | -8.1% (-33.0% to +15.4%) | 26 (12) | -7.4% (-8.9% to -6.2%) | -0.9% (-2.0% to -0.1%) | hypothesis (range includes zero) |
| lane = value, side = under | 55 | 31 (15) | 55% | 50% | +12.6% (-23.1% to +42.5%) | 29 (14) | -1.6% (-3.1% to -0.1%) | -3.3% (-4.9% to -1.7%) | hypothesis (range includes zero) |
| edge = 6%+ | 82 | 13 (7) | 31% | 49% | -32.3% (7 games) | 14 (8) | +5.0% (8 games) | -1.9% (8 games) | hypothesis |
| tier = Best bet | 31 | 13 (10) | 77% | 66% | +10.5% (-18.1% to +33.5%) | 13 (10) | -6.2% (-7.5% to -5.1%) | -0.7% (-1.6% to +0.1%) | hypothesis |
| tier = Lean | 20 | 13 (9) | 54% | 57% | -4.6% (9 games) | 11 (8) | -1.1% (8 games) | +0.1% (8 games) | hypothesis |
| sport = nba, stat/market = blk | 17 | 11 (6) | 91% | 61% | +36.5% (6 games) | 11 (6) | -6.2% (6 games) | -0.9% (6 games) | hypothesis |
| stat/market = blk | 17 | 11 (6) | 91% | 61% | +36.5% (6 games) | 11 (6) | -6.2% (6 games) | -0.9% (6 games) | hypothesis |
| chance = 30-40% | 17 | 8 (5) | 25% | 38% | -31.8% (5 games) | 7 (4) | +5.7% (4 games) | +2.9% (4 games) | hypothesis |
| sport = nba, stat/market = ra | 9 | 4 (4) | 25% | 52% | -48.0% (4 games) | 4 (4) | +3.9% (4 games) | -0.9% (4 games) | hypothesis |
| stat/market = ra | 9 | 4 (4) | 25% | 52% | -48.0% (4 games) | 4 (4) | +3.9% (4 games) | -0.9% (4 games) | hypothesis |
| lane = likely, side = home | 7 | 2 (2) | 100% | 62% | +59.4% (2 games) | 2 (2) | +1.2% (2 games) | +2.8% (2 games) | hypothesis |
| side = home | 7 | 2 (2) | 100% | 62% | +59.4% (2 games) | 2 (2) | +1.2% (2 games) | +2.8% (2 games) | hypothesis |
| sport = nba, stat/market = moneyline | 12 | 2 (2) | 100% | 62% | +59.4% (2 games) | 2 (2) | +1.2% (2 games) | +2.8% (2 games) | hypothesis |
| stat/market = moneyline | 19 | 2 (2) | 100% | 62% | +59.4% (2 games) | 2 (2) | +1.2% (2 games) | +2.8% (2 games) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 1 (1) | +6.1% (–) | +0.7% (–) | hypothesis |
| lane = likely, side = away | 12 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| side = away | 12 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
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
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
