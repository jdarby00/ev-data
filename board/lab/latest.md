# Research lab report

Built 2026-11-11T11:10:14Z UTC from 780 logged code candidates (601 settled, 586 with a close, 25 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 213, ROI -0.9%; CLV n 202 over 24 games, -6.3%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 96, ROI +4.3%; CLV n 97 over 24 games, +1.3%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 292, ROI -14.2%; CLV n 287 over 24 games, -1.9%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 601, ROI -6.6%; CLV n 584 over 24 games, -2.9%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 191, ROI -2.3%; CLV n 176 over 24 games, -6.3%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 369, ROI -10.4%; CLV n 367 over 25 games, -1.0%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 93, ROI +11.8%; CLV n 93 over 24 games, -2.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 170, ROI -12.3%; CLV n 155 over 24 games, -3.8%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -10.9%; CLV n 100 over 22 games, -2.4%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 109, ROI -22.1%; CLV n 108 over 22 games, -1.5%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +17.5%; CLV n 47 over 19 games, -6.0%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 56, ROI -16.9%; CLV n 51 over 17 games, -3.0%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 417, ROI -2.4%; CLV n 401 over 24 games, -3.6%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 180, ROI -17.6%; CLV n 177 over 23 games, -1.5%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 318, ROI +4.0%; CLV n 308 over 24 games, -2.9%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 283, ROI -18.4%; CLV n 278 over 25 games, -2.9%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 83, ROI -5.3%; CLV n 78 over 20 games, -7.0%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 193, ROI -7.8%; CLV n 183 over 24 games, -2.6%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 137, ROI +2.9%; CLV n 131 over 24 games, -5.7%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 213, ROI -0.9%; CLV n 202 over 24 games, -6.3%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 221, ROI -7.3%; CLV n 214 over 24 games, -2.1%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 211, ROI -1.6%; CLV n 198 over 24 games, -6.4%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 293, ROI -14.2%; CLV n 290 over 24 games, -1.9%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 167, ROI -4.3%; CLV n 162 over 22 games, -2.1%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 111, ROI +6.9%; CLV n 126 over 11 games, -3.6%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 323, ROI -12.4%; CLV n 298 over 24 games, -3.0%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 256, ROI +0.9%; CLV n 253 over 24 games, -3.5%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 345, ROI -12.1%; CLV n 333 over 24 games, -2.4%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 444, ROI -11.7%; CLV n 440 over 25 games, -3.2%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 157, ROI +8.1%; CLV n 146 over 14 games, -2.0%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 96, ROI +4.3%; CLV n 95 over 23 games, +1.2%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 292, ROI -14.2%; CLV n 287 over 24 games, -1.9%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 213, ROI -0.9%; CLV n 202 over 24 games, -6.3%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 48, ROI -7.1%; CLV n 48 over 21 games, +2.3%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 199, ROI -7.3%; CLV n 195 over 24 games, -2.3%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 93, ROI -29.0%; CLV n 92 over 20 games, -1.1%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 170, ROI -1.8%; CLV n 159 over 24 games, -6.3%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 39, ROI -3.6%; CLV n 37 over 16 games, -7.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 93, ROI +11.8%; CLV n 93 over 24 games, -2.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 170, ROI -12.3%; CLV n 155 over 24 games, -3.8%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 99, ROI -10.9%; CLV n 100 over 22 games, -2.4%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 109, ROI -22.1%; CLV n 108 over 22 games, -1.5%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 47, ROI +17.5%; CLV n 47 over 19 games, -6.0%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 56, ROI -16.9%; CLV n 51 over 17 games, -3.0%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 780 | 601 (25) | 52% | 54% | -6.6% (-14.1% to +0.0%) | 586 (25) | -2.9% (-3.2% to -2.5%) | -0.3% (-0.6% to -0.0%) |  |
| sport = nba | 674 | 601 (25) | 52% | 54% | -6.6% (-14.1% to +0.0%) | 584 (24) | -2.9% (-3.3% to -2.6%) | -0.3% (-0.7% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 606 | 444 (24) | 50% | 55% | -11.7% (-20.0% to -3.4%) | 440 (25) | -3.2% (-3.7% to -2.6%) | -0.3% (-0.7% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 479 | 417 (25) | 55% | 55% | -2.4% (-11.9% to +6.0%) | 401 (24) | -3.6% (-4.2% to -3.0%) | -0.4% (-0.9% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 501 | 369 (25) | 43% | 49% | -10.4% (-21.6% to -0.6%) | 367 (25) | -1.0% (-1.5% to -0.6%) | -0.1% (-0.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 383 | 345 (25) | 46% | 52% | -12.1% (-21.9% to -2.7%) | 333 (24) | -2.4% (-3.0% to -1.9%) | -0.1% (-0.6% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 377 | 323 (24) | 49% | 54% | -12.4% (-21.9% to -3.6%) | 298 (24) | -3.0% (-3.7% to -2.3%) | -0.4% (-1.0% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 365 | 318 (25) | 58% | 56% | +4.0% (-4.9% to +11.4%) | 308 (24) | -2.9% (-3.4% to -2.4%) | -0.3% (-0.6% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 324 | 293 (25) | 43% | 50% | -14.2% (-27.4% to -0.6%) | 290 (24) | -1.9% (-2.5% to -1.4%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 321 | 292 (25) | 42% | 50% | -14.2% (-27.6% to -1.2%) | 287 (24) | -1.9% (-2.5% to -1.4%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 321 | 292 (25) | 42% | 50% | -14.2% (-27.6% to -1.2%) | 287 (24) | -1.9% (-2.5% to -1.4%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 415 | 283 (25) | 44% | 53% | -18.4% (-28.9% to -8.5%) | 278 (25) | -2.9% (-3.3% to -2.4%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 397 | 256 (23) | 59% | 57% | +0.9% (-7.8% to +9.2%) | 253 (24) | -3.5% (-4.3% to -2.7%) | -0.6% (-1.1% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 248 | 221 (25) | 48% | 53% | -7.3% (-20.6% to +5.2%) | 214 (24) | -2.1% (-2.6% to -1.5%) | -0.5% (-1.0% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 259 | 213 (25) | 65% | 62% | -0.9% (-10.9% to +8.5%) | 202 (24) | -6.3% (-7.0% to -5.7%) | -0.6% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 259 | 213 (25) | 65% | 62% | -0.9% (-10.9% to +8.5%) | 202 (24) | -6.3% (-7.0% to -5.7%) | -0.6% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 245 | 213 (25) | 65% | 62% | -0.9% (-10.9% to +8.5%) | 202 (24) | -6.3% (-7.0% to -5.7%) | -0.6% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 255 | 211 (25) | 65% | 62% | -1.6% (-11.7% to +7.9%) | 198 (24) | -6.4% (-7.1% to -5.8%) | -0.7% (-1.3% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 226 | 199 (25) | 46% | 51% | -7.3% (-22.8% to +6.6%) | 195 (24) | -2.3% (-3.0% to -1.5%) | +0.3% (-0.4% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 215 | 193 (25) | 48% | 52% | -7.8% (-23.8% to +6.4%) | 183 (24) | -2.6% (-3.2% to -2.0%) | -0.6% (-1.1% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 228 | 191 (25) | 64% | 62% | -2.3% (-12.9% to +7.3%) | 176 (24) | -6.3% (-7.0% to -5.7%) | -0.6% (-1.1% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 299 | 188 (25) | 39% | 46% | -12.8% (-27.1% to +0.7%) | 194 (25) | +0.4% (-0.2% to +0.9%) | +0.2% (-0.3% to +0.7%) | hypothesis (range includes zero) |
| side = over | 194 | 180 (24) | 43% | 51% | -17.6% (-36.1% to -1.0%) | 177 (23) | -1.5% (-2.2% to -0.6%) | -0.3% (-0.9% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 196 | 170 (25) | 65% | 62% | -1.8% (-13.6% to +9.4%) | 159 (24) | -6.3% (-7.0% to -5.7%) | -0.7% (-1.3% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 188 | 170 (25) | 51% | 57% | -12.3% (-21.2% to -3.7%) | 155 (24) | -3.8% (-4.3% to -3.2%) | -0.0% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 188 | 170 (25) | 51% | 57% | -12.3% (-21.2% to -3.7%) | 155 (24) | -3.8% (-4.3% to -3.2%) | -0.0% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 198 | 167 (24) | 50% | 52% | -4.3% (-14.0% to +6.0%) | 162 (22) | -2.1% (-2.7% to -1.6%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 179 | 159 (25) | 40% | 46% | -11.8% (-27.8% to +4.1%) | 161 (24) | -0.2% (-0.7% to +0.3%) | +0.1% (-0.3% to +0.7%) | hypothesis (range includes zero) |
| status change = yes | 174 | 157 (15) | 56% | 52% | +8.1% (-4.1% to +19.7%) | 146 (14) | -2.0% (-2.5% to -1.5%) | -0.4% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 153 | 137 (25) | 66% | 61% | +2.9% (-8.8% to +14.0%) | 131 (24) | -5.7% (-6.4% to -5.1%) | -0.5% (-1.2% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 205 | 111 (10) | 61% | 57% | +6.9% (-2.7% to +20.2%) | 126 (11) | -3.6% (-4.5% to -2.9%) | +0.1% (-0.6% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 116 | 109 (22) | 39% | 50% | -22.1% (-38.8% to -4.4%) | 108 (22) | -1.5% (-2.2% to -0.7%) | -0.4% (-1.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 116 | 109 (22) | 39% | 50% | -22.1% (-38.8% to -4.4%) | 108 (22) | -1.5% (-2.2% to -0.7%) | -0.4% (-1.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 113 | 99 (24) | 45% | 52% | -10.9% (-27.7% to +5.5%) | 100 (22) | -2.4% (-2.9% to -1.8%) | -0.4% (-0.9% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 113 | 99 (24) | 45% | 52% | -10.9% (-27.7% to +5.5%) | 100 (22) | -2.4% (-2.9% to -1.8%) | -0.4% (-0.9% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 200 | 96 (23) | 49% | 49% | +4.3% (-14.1% to +21.6%) | 97 (24) | +1.3% (+0.5% to +2.0%) | -2.0% (-2.6% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 108 | 96 (23) | 49% | 49% | +4.3% (-14.1% to +21.6%) | 95 (23) | +1.2% (+0.4% to +1.9%) | -2.0% (-2.7% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 95 | 93 (20) | 34% | 49% | -29.0% (-48.4% to -6.5%) | 92 (20) | -1.1% (-1.8% to -0.2%) | +0.8% (+0.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 106 | 93 (24) | 58% | 51% | +11.8% (-3.9% to +26.1%) | 93 (24) | -2.4% (-3.5% to -1.3%) | -0.6% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 106 | 93 (24) | 58% | 51% | +11.8% (-3.9% to +26.1%) | 93 (24) | -2.4% (-3.5% to -1.3%) | -0.6% (-1.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 113 | 83 (21) | 65% | 64% | -5.3% (-21.9% to +9.8%) | 78 (20) | -7.0% (-7.8% to -6.2%) | -0.8% (-1.4% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 119 | 79 (23) | 49% | 49% | +3.3% (-15.7% to +19.4%) | 79 (24) | +0.8% (-0.0% to +1.6%) | -1.5% (-2.2% to -0.8%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pra | 63 | 56 (19) | 43% | 52% | -16.9% (-37.7% to +2.0%) | 51 (17) | -3.0% (-3.6% to -2.3%) | +0.1% (-0.4% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 63 | 56 (19) | 43% | 52% | -16.9% (-37.7% to +2.0%) | 51 (17) | -3.0% (-3.6% to -2.3%) | +0.1% (-0.4% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 55 | 48 (21) | 42% | 47% | -7.1% (-36.2% to +22.1%) | 48 (21) | +2.3% (+0.7% to +3.8%) | -2.0% (-3.6% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = under | 57 | 48 (19) | 56% | 50% | +15.7% (-7.9% to +37.2%) | 47 (19) | +0.1% (-1.6% to +1.5%) | -1.9% (-3.4% to -0.6%) | hypothesis (range includes zero) |
| sport = nba, stat/market = stl | 50 | 47 (19) | 77% | 63% | +17.5% (-5.4% to +35.9%) | 47 (19) | -6.0% (-7.0% to -5.1%) | -1.1% (-2.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 50 | 47 (19) | 77% | 63% | +17.5% (-5.4% to +35.9%) | 47 (19) | -6.0% (-7.0% to -5.1%) | -1.1% (-2.0% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 44 | 39 (18) | 64% | 62% | -3.6% (-24.2% to +15.4%) | 37 (16) | -7.2% (-8.3% to -6.3%) | -0.8% (-1.7% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 31 | 22 (13) | 77% | 66% | +11.0% (-12.9% to +31.6%) | 26 (14) | -6.4% (-7.8% to -5.0%) | -1.0% (-1.8% to -0.1%) | hypothesis |
| tier = Lean | 20 | 19 (12) | 58% | 57% | +4.0% (-24.0% to +31.9%) | 17 (11) | -2.1% (-4.4% to -0.4%) | -1.3% (-4.2% to +0.4%) | hypothesis |
| edge = 6%+ | 82 | 18 (9) | 50% | 48% | +15.4% (9 games) | 19 (10) | +3.4% (+1.3% to +6.3%) | -3.8% (-6.7% to -1.5%) | hypothesis |
| sport = nba, stat/market = blk | 17 | 15 (9) | 93% | 62% | +40.2% (9 games) | 16 (10) | -6.0% (-7.4% to -4.5%) | -0.9% (-1.7% to -0.2%) | hypothesis |
| stat/market = blk | 17 | 15 (9) | 93% | 62% | +40.2% (9 games) | 16 (10) | -6.0% (-7.4% to -4.5%) | -0.9% (-1.7% to -0.2%) | hypothesis |
| chance = 30-40% | 17 | 8 (5) | 25% | 38% | -31.8% (5 games) | 7 (4) | +5.7% (4 games) | +2.9% (4 games) | hypothesis |
| sport = nba, stat/market = ra | 9 | 8 (6) | 38% | 51% | -24.2% (6 games) | 8 (6) | +4.2% (6 games) | -0.2% (6 games) | hypothesis |
| stat/market = ra | 9 | 8 (6) | 38% | 51% | -24.2% (6 games) | 8 (6) | +4.2% (6 games) | -0.2% (6 games) | hypothesis |
| lane = likely, side = home | 7 | 4 (3) | 100% | 61% | +59.2% (3 games) | 4 (3) | -0.6% (3 games) | +2.1% (3 games) | hypothesis |
| side = home | 7 | 4 (3) | 100% | 61% | +59.2% (3 games) | 4 (3) | -0.6% (3 games) | +2.1% (3 games) | hypothesis |
| sport = nba, stat/market = moneyline | 12 | 4 (3) | 100% | 61% | +59.2% (3 games) | 6 (4) | -2.0% (4 games) | +1.0% (4 games) | hypothesis |
| stat/market = moneyline | 19 | 4 (3) | 100% | 61% | +59.2% (3 games) | 6 (4) | -2.0% (4 games) | +1.0% (4 games) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 1 (1) | +6.1% (–) | +0.7% (–) | hypothesis |
| lane = likely, side = away | 12 | 0 (0) | – | – | – (–) | 2 (1) | -4.8% (–) | -1.3% (–) | hypothesis |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| side = away | 12 | 0 (0) | – | – | – (–) | 2 (1) | -4.8% (–) | -1.3% (–) | hypothesis |
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
