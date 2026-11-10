# Research lab report

Built 2026-11-10T18:38:10Z UTC from 643 logged code candidates (455 settled, 203 with a close, 9 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = early**: IN-SAMPLE SIGNAL: negative ROI (settled 227, ROI -23.8%; CLV n 110 over 9 games, -2.0%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative ROI (settled 455, ROI -12.6%; CLV n 203 over 9 games, -3.2%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative ROI (settled 285, ROI -19.7%; CLV n 134 over 9 games, -1.5%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative ROI (settled 125, ROI -12.8%; CLV n 54 over 9 games, -3.9%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative ROI (settled 75, ROI -24.1%; CLV n 38 over 9 games, -2.8%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative ROI (settled 85, ROI -27.8%; CLV n 38 over 8 games, -1.9%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative ROI (settled 40, ROI -32.3%; CLV n 18 over 6 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative ROI (settled 155, ROI -24.3%; CLV n 84 over 9 games, -2.2%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative ROI (settled 226, ROI -22.1%; CLV n 102 over 9 games, -2.9%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative ROI (settled 137, ROI -23.8%; CLV n 66 over 9 games, -2.7%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: negative ROI (settled 154, ROI -16.8%; CLV n 70 over 9 games, -0.2%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative ROI (settled 163, ROI -19.4%; CLV n 75 over 9 games, -2.2%)
- **chance = 40-50%**: IN-SAMPLE SIGNAL: negative ROI (settled 127, ROI -17.8%; CLV n 62 over 9 games, -1.0%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative ROI (settled 228, ROI -23.6%; CLV n 109 over 9 games, -2.1%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative ROI (settled 266, ROI -18.4%; CLV n 119 over 8 games, -3.7%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative ROI (settled 255, ROI -22.2%; CLV n 97 over 9 games, -3.1%)
- **status change = no**: IN-SAMPLE SIGNAL: negative ROI (settled 340, ROI -18.0%; CLV n 137 over 9 games, -3.8%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative ROI (settled 227, ROI -23.8%; CLV n 110 over 9 games, -2.0%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative ROI (settled 143, ROI -17.9%; CLV n 58 over 9 games, -2.2%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative ROI (settled 84, ROI -33.8%; CLV n 52 over 8 games, -1.8%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative ROI (settled 125, ROI -12.8%; CLV n 54 over 9 games, -3.9%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative ROI (settled 75, ROI -24.1%; CLV n 38 over 9 games, -2.8%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative ROI (settled 85, ROI -27.8%; CLV n 38 over 8 games, -1.9%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative ROI (settled 40, ROI -32.3%; CLV n 18 over 6 games, -3.5%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 643 | 455 (21) | 48% | 54% | -12.6% (-20.0% to -5.0%) | 203 (9) | -3.2% (9 games) | -0.4% (9 games) |  |
| sport = nba | 537 | 455 (21) | 48% | 54% | -12.6% (-20.0% to -5.0%) | 203 (9) | -3.2% (9 games) | -0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| status change = no | 524 | 340 (20) | 46% | 54% | -18.0% (-26.4% to -9.5%) | 137 (9) | -3.8% (9 games) | -0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| side = under | 372 | 298 (21) | 53% | 55% | -7.0% (-18.9% to +4.3%) | 119 (9) | -3.9% (9 games) | -0.3% (9 games) | hypothesis (range includes zero) |
| tier = Value | 407 | 285 (21) | 39% | 49% | -19.7% (-30.0% to -9.2%) | 134 (9) | -1.5% (9 games) | -0.2% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| flagged = 2-6h before | 308 | 266 (20) | 46% | 54% | -18.4% (-29.0% to -8.4%) | 119 (8) | -3.7% (8 games) | -0.6% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| minutes moved = yes | 298 | 255 (21) | 41% | 52% | -22.2% (-31.2% to -12.8%) | 97 (9) | -3.1% (9 games) | -0.5% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| book = draftkings | 283 | 229 (21) | 55% | 56% | -3.2% (-12.4% to +5.1%) | 101 (9) | -3.5% (9 games) | -0.5% (9 games) | hypothesis (range includes zero) |
| edge = 0-3% | 257 | 228 (21) | 38% | 50% | -23.6% (-36.2% to -9.8%) | 109 (9) | -2.1% (9 games) | +0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = early | 254 | 227 (21) | 37% | 50% | -23.8% (-36.6% to -10.3%) | 110 (9) | -2.0% (9 games) | +0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = early, sport = nba | 254 | 227 (21) | 37% | 50% | -23.8% (-36.6% to -10.3%) | 110 (9) | -2.0% (9 games) | +0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| book = fanduel | 360 | 226 (21) | 42% | 52% | -22.1% (-34.2% to -10.3%) | 102 (9) | -2.9% (9 games) | -0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| minutes moved = no | 345 | 200 (19) | 57% | 56% | -0.4% (-11.1% to +9.6%) | 106 (8) | -3.3% (8 games) | -0.3% (8 games) | hypothesis (range includes zero) |
| chance = 50-60% | 185 | 163 (21) | 42% | 52% | -19.4% (-32.2% to -6.0%) | 75 (9) | -2.2% (9 games) | -0.7% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| chance = 60-70% | 221 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| lane = likely | 221 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| lane = likely, sport = nba | 207 | 157 (21) | 66% | 62% | -0.4% (-12.9% to +11.3%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| edge = under 0% | 217 | 155 (21) | 65% | 62% | -1.2% (-13.4% to +10.2%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| side = over | 167 | 155 (20) | 39% | 51% | -24.3% (-43.6% to -7.0%) | 84 (9) | -2.2% (9 games) | -0.6% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| price = +101 or longer | 260 | 154 (21) | 38% | 46% | -16.8% (-31.6% to -3.4%) | 70 (9) | -0.2% (9 games) | +0.5% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 197 | 144 (21) | 65% | 62% | -1.4% (-14.0% to +10.7%) | 59 (9) | -7.2% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| lane = early, side = under | 168 | 143 (21) | 41% | 50% | -17.9% (-34.0% to -1.5%) | 58 (9) | -2.2% (9 games) | +0.5% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| flagged = under 2h before | 167 | 138 (20) | 47% | 52% | -10.0% (-20.1% to +0.9%) | 58 (9) | -2.4% (9 games) | -0.6% (9 games) | hypothesis (range includes zero) |
| price = -129 to +100 | 155 | 137 (21) | 39% | 52% | -23.8% (-37.2% to -10.2%) | 66 (9) | -2.7% (9 games) | -0.9% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| chance = 40-50% | 144 | 127 (21) | 37% | 46% | -17.8% (-33.8% to -2.2%) | 62 (9) | -1.0% (9 games) | +0.1% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = tpm | 152 | 125 (21) | 51% | 57% | -12.8% (-23.1% to -3.9%) | 54 (9) | -3.9% (9 games) | -0.1% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = tpm | 152 | 125 (21) | 51% | 57% | -12.8% (-23.1% to -3.9%) | 54 (9) | -3.9% (9 games) | -0.1% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = likely, side = under | 167 | 124 (21) | 66% | 62% | +0.6% (-15.4% to +15.4%) | 48 (9) | -6.9% (9 games) | -1.0% (9 games) | hypothesis (range includes zero) |
| status change = yes | 119 | 115 (12) | 54% | 53% | +3.2% (-10.7% to +17.6%) | 66 (7) | -2.0% (7 games) | -0.5% (7 games) | hypothesis (range includes zero) |
| price = -199 to -130 | 126 | 98 (21) | 66% | 61% | +4.4% (-7.7% to +16.0%) | 43 (9) | -6.3% (9 games) | -0.9% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = reb | 92 | 85 (18) | 36% | 50% | -27.8% (-45.0% to -7.4%) | 38 (8) | -1.9% (8 games) | -0.3% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = reb | 92 | 85 (18) | 36% | 50% | -27.8% (-45.0% to -7.4%) | 38 (8) | -1.9% (8 games) | -0.3% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = early, side = over | 86 | 84 (17) | 32% | 49% | -33.8% (-54.2% to -9.5%) | 52 (8) | -1.8% (8 games) | +0.3% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = ast | 91 | 78 (20) | 56% | 51% | +9.5% (-7.5% to +26.5%) | 36 (9) | -2.4% (9 games) | -0.5% (9 games) | hypothesis (range includes zero) |
| stat/market = ast | 91 | 78 (20) | 56% | 51% | +9.5% (-7.5% to +26.5%) | 36 (9) | -2.4% (9 games) | -0.5% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = pts | 87 | 75 (20) | 39% | 52% | -24.1% (-40.2% to -8.6%) | 38 (9) | -2.8% (9 games) | -0.9% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pts | 87 | 75 (20) | 39% | 52% | -24.1% (-40.2% to -8.6%) | 38 (9) | -2.8% (9 games) | -0.9% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = value | 168 | 71 (19) | 45% | 48% | -4.0% (-23.7% to +13.8%) | 30 (9) | +0.6% (9 games) | -2.1% (9 games) | hypothesis (range includes zero) |
| lane = value, sport = nba | 76 | 71 (19) | 45% | 48% | -4.0% (-23.7% to +13.8%) | 30 (9) | +0.6% (9 games) | -2.1% (9 games) | hypothesis (range includes zero) |
| price = -200 or shorter | 102 | 66 (18) | 65% | 64% | -5.0% (-24.3% to +12.4%) | 24 (8) | -7.6% (8 games) | -1.0% (8 games) | hypothesis (range includes zero) |
| edge = 3-6% | 92 | 59 (19) | 49% | 48% | +4.3% (-18.0% to +22.0%) | 26 (9) | +0.2% (9 games) | -1.4% (9 games) | hypothesis (range includes zero) |
| flagged = 6h+ before | 168 | 51 (6) | 63% | 56% | +10.3% (6 games) | 26 (3) | -2.9% (3 games) | +0.6% (3 games) | too few games (<10) |
| lane = value, side = over | 43 | 40 (18) | 38% | 47% | -16.9% (-44.1% to +8.3%) | 17 (9) | +1.6% (9 games) | -2.6% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = pra | 45 | 40 (16) | 35% | 52% | -32.3% (-52.1% to -13.5%) | 18 (6) | -3.5% (6 games) | -0.2% (6 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pra | 45 | 40 (16) | 35% | 52% | -32.3% (-52.1% to -13.5%) | 18 (6) | -3.5% (6 games) | -0.2% (6 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = stl | 43 | 35 (16) | 71% | 63% | +6.7% (-21.3% to +29.1%) | 15 (8) | -6.1% (8 games) | -0.8% (8 games) | hypothesis (range includes zero) |
| stat/market = stl | 43 | 35 (16) | 71% | 63% | +6.7% (-21.3% to +29.1%) | 15 (8) | -6.1% (8 games) | -0.8% (8 games) | hypothesis (range includes zero) |
| lane = likely, side = over | 38 | 31 (15) | 61% | 62% | -8.1% (-33.0% to +15.4%) | 15 (7) | -7.8% (7 games) | -1.3% (7 games) | hypothesis (range includes zero) |
| lane = value, side = under | 37 | 31 (15) | 55% | 50% | +12.6% (-23.1% to +42.5%) | 13 (6) | -0.7% (6 games) | -1.3% (6 games) | hypothesis (range includes zero) |
| edge = 6%+ | 77 | 13 (7) | 31% | 49% | -32.3% (7 games) | 5 (3) | +2.9% (3 games) | -4.8% (3 games) | hypothesis |
| tier = Best bet | 24 | 13 (10) | 77% | 66% | +10.5% (-18.1% to +33.5%) | 4 (4) | -5.4% (4 games) | +0.1% (4 games) | hypothesis |
| tier = Lean | 15 | 13 (9) | 54% | 57% | -4.6% (9 games) | 6 (4) | -0.1% (4 games) | +0.3% (4 games) | hypothesis |
| sport = nba, stat/market = blk | 13 | 11 (6) | 91% | 61% | +36.5% (6 games) | 3 (2) | -10.1% (2 games) | -2.6% (2 games) | hypothesis |
| stat/market = blk | 13 | 11 (6) | 91% | 61% | +36.5% (6 games) | 3 (2) | -10.1% (2 games) | -2.6% (2 games) | hypothesis |
| chance = 30-40% | 16 | 8 (5) | 25% | 38% | -31.8% (5 games) | 3 (2) | +8.2% (2 games) | +8.6% (2 games) | hypothesis |
| sport = nba, stat/market = ra | 5 | 4 (4) | 25% | 52% | -48.0% (4 games) | 1 (1) | +5.7% (–) | +0.3% (–) | hypothesis |
| stat/market = ra | 5 | 4 (4) | 25% | 52% | -48.0% (4 games) | 1 (1) | +5.7% (–) | +0.3% (–) | hypothesis |
| lane = likely, side = home | 5 | 2 (2) | 100% | 62% | +59.4% (2 games) | 0 (0) | – (–) | – (–) | hypothesis |
| side = home | 5 | 2 (2) | 100% | 62% | +59.4% (2 games) | 0 (0) | – (–) | – (–) | hypothesis |
| sport = nba, stat/market = moneyline | 9 | 2 (2) | 100% | 62% | +59.4% (2 games) | 0 (0) | – (–) | – (–) | hypothesis |
| stat/market = moneyline | 16 | 2 (2) | 100% | 62% | +59.4% (2 games) | 0 (0) | – (–) | – (–) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, side = away | 11 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = away | 11 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = yes | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl | 105 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = anytime_td | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = moneyline | 6 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nfl, stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = ints | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
