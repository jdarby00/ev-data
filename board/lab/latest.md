# Research lab report

Built 2026-11-09T23:02:46Z UTC from 537 logged code candidates (302 settled, 203 with a close, 9 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **stat/market = ast**: IN-SAMPLE SIGNAL: positive ROI (settled 55, ROI +20.1%; CLV n 36 over 9 games, -2.4%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative ROI (settled 53, ROI -23.8%; CLV n 38 over 8 games, -1.9%)
- **side = over**: IN-SAMPLE SIGNAL: negative ROI (settled 112, ROI -26.6%; CLV n 84 over 9 games, -2.2%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative ROI (settled 153, ROI -18.6%; CLV n 102 over 9 games, -2.9%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative ROI (settled 155, ROI -14.6%; CLV n 97 over 9 games, -3.1%)
- **status change = no**: IN-SAMPLE SIGNAL: negative ROI (settled 194, ROI -13.0%; CLV n 137 over 9 games, -3.8%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: positive ROI (settled 55, ROI +20.1%; CLV n 36 over 9 games, -2.4%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative ROI (settled 53, ROI -23.8%; CLV n 38 over 8 games, -1.9%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 537 | 302 (13) | 50% | 54% | -7.7% (-17.1% to +1.9%) | 203 (9) | -3.2% (9 games) | -0.4% (9 games) |  |
| sport = nba | 431 | 302 (13) | 50% | 54% | -7.7% (-17.1% to +1.9%) | 203 (9) | -3.2% (9 games) | -0.4% (9 games) | hypothesis (range includes zero) |
| status change = no | 425 | 194 (12) | 48% | 54% | -13.0% (-24.6% to -0.6%) | 137 (9) | -3.8% (9 games) | -0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Value | 354 | 193 (13) | 43% | 49% | -10.6% (-22.8% to +2.1%) | 134 (9) | -1.5% (9 games) | -0.2% (9 games) | hypothesis (range includes zero) |
| side = under | 294 | 190 (13) | 57% | 55% | +3.5% (-10.9% to +16.6%) | 119 (9) | -3.9% (9 games) | -0.3% (9 games) | hypothesis (range includes zero) |
| flagged = 2-6h before | 306 | 166 (12) | 49% | 54% | -11.2% (-25.0% to +0.3%) | 119 (8) | -3.7% (8 games) | -0.6% (8 games) | hypothesis (range includes zero) |
| minutes moved = yes | 235 | 155 (13) | 45% | 53% | -14.6% (-27.2% to -2.6%) | 97 (9) | -3.1% (9 games) | -0.5% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| book = fanduel | 308 | 153 (13) | 43% | 52% | -18.6% (-34.5% to -3.0%) | 102 (9) | -2.9% (9 games) | -0.4% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| edge = 0-3% | 215 | 153 (13) | 44% | 50% | -11.2% (-27.9% to +6.8%) | 109 (9) | -2.1% (9 games) | +0.4% (9 games) | hypothesis (range includes zero) |
| lane = early | 214 | 153 (13) | 44% | 50% | -10.8% (-26.0% to +7.4%) | 110 (9) | -2.0% (9 games) | +0.4% (9 games) | hypothesis (range includes zero) |
| lane = early, sport = nba | 214 | 153 (13) | 44% | 50% | -10.8% (-26.0% to +7.4%) | 110 (9) | -2.0% (9 games) | +0.4% (9 games) | hypothesis (range includes zero) |
| book = draftkings | 229 | 149 (13) | 58% | 56% | +3.5% (-6.8% to +12.2%) | 101 (9) | -3.5% (9 games) | -0.5% (9 games) | hypothesis (range includes zero) |
| minutes moved = no | 302 | 147 (11) | 56% | 55% | -0.4% (-15.0% to +11.7%) | 106 (8) | -3.3% (8 games) | -0.3% (8 games) | hypothesis (range includes zero) |
| chance = 50-60% | 154 | 115 (13) | 45% | 53% | -12.6% (-26.9% to +2.7%) | 75 (9) | -2.2% (9 games) | -0.7% (9 games) | hypothesis (range includes zero) |
| side = over | 140 | 112 (13) | 38% | 51% | -26.6% (-52.4% to -4.3%) | 84 (9) | -2.2% (9 games) | -0.6% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| status change = yes | 112 | 108 (10) | 54% | 53% | +1.9% (-11.2% to +14.7%) | 66 (7) | -2.0% (7 games) | -0.5% (7 games) | hypothesis (range includes zero) |
| price = +101 or longer | 232 | 101 (13) | 42% | 46% | -8.1% (-24.2% to +6.8%) | 70 (9) | -0.2% (9 games) | +0.5% (9 games) | hypothesis (range includes zero) |
| chance = 60-70% | 170 | 98 (13) | 64% | 62% | -2.4% (-18.3% to +13.6%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| lane = likely | 170 | 98 (13) | 64% | 62% | -2.4% (-18.3% to +13.6%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| lane = likely, sport = nba | 156 | 98 (13) | 64% | 62% | -2.4% (-18.3% to +13.6%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| edge = under 0% | 168 | 97 (13) | 64% | 62% | -3.1% (-18.6% to +12.4%) | 63 (9) | -7.1% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| price = -129 to +100 | 128 | 97 (13) | 44% | 53% | -14.0% (-27.3% to +0.9%) | 66 (9) | -2.7% (9 games) | -0.9% (9 games) | hypothesis (range includes zero) |
| lane = early, side = under | 140 | 94 (13) | 50% | 51% | +1.7% (-17.6% to +20.9%) | 58 (9) | -2.2% (9 games) | +0.5% (9 games) | hypothesis (range includes zero) |
| tier = Straight | 152 | 91 (13) | 64% | 62% | -2.9% (-18.9% to +13.8%) | 59 (9) | -7.2% (9 games) | -1.1% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = tpm | 114 | 90 (13) | 56% | 57% | -6.2% (-16.9% to +3.4%) | 54 (9) | -3.9% (9 games) | -0.1% (9 games) | hypothesis (range includes zero) |
| stat/market = tpm | 114 | 90 (13) | 56% | 57% | -6.2% (-16.9% to +3.4%) | 54 (9) | -3.9% (9 games) | -0.1% (9 games) | hypothesis (range includes zero) |
| flagged = under 2h before | 126 | 89 (13) | 46% | 52% | -11.8% (-25.2% to +0.5%) | 58 (9) | -2.4% (9 games) | -0.6% (9 games) | hypothesis (range includes zero) |
| chance = 40-50% | 121 | 83 (13) | 42% | 46% | -7.0% (-24.9% to +11.9%) | 62 (9) | -1.0% (9 games) | +0.1% (9 games) | hypothesis (range includes zero) |
| lane = likely, side = under | 125 | 75 (13) | 67% | 62% | +1.7% (-17.1% to +21.7%) | 48 (9) | -6.9% (9 games) | -1.0% (9 games) | hypothesis (range includes zero) |
| price = -199 to -130 | 96 | 62 (13) | 65% | 61% | +1.9% (-11.6% to +17.1%) | 43 (9) | -6.3% (9 games) | -0.9% (9 games) | hypothesis (range includes zero) |
| lane = early, side = over | 74 | 59 (10) | 34% | 49% | -30.8% (-57.8% to +5.4%) | 52 (8) | -1.8% (8 games) | +0.3% (8 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = ast | 79 | 55 (12) | 60% | 50% | +20.1% (+0.8% to +40.4%) | 36 (9) | -2.4% (9 games) | -0.5% (9 games) | IN-SAMPLE SIGNAL: positive ROI |
| stat/market = ast | 79 | 55 (12) | 60% | 50% | +20.1% (+0.8% to +40.4%) | 36 (9) | -2.4% (9 games) | -0.5% (9 games) | IN-SAMPLE SIGNAL: positive ROI |
| sport = nba, stat/market = pts | 67 | 53 (13) | 43% | 52% | -14.9% (-33.7% to +2.8%) | 38 (9) | -2.8% (9 games) | -0.9% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = reb | 75 | 53 (11) | 40% | 51% | -23.8% (-45.4% to -1.4%) | 38 (8) | -1.9% (8 games) | -0.3% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pts | 67 | 53 (13) | 43% | 52% | -14.9% (-33.7% to +2.8%) | 38 (9) | -2.8% (9 games) | -0.9% (9 games) | hypothesis (range includes zero) |
| stat/market = reb | 75 | 53 (11) | 40% | 51% | -23.8% (-45.4% to -1.4%) | 38 (8) | -1.9% (8 games) | -0.3% (8 games) | IN-SAMPLE SIGNAL: negative ROI |
| lane = value | 153 | 51 (12) | 43% | 48% | -8.4% (-36.5% to +11.7%) | 30 (9) | +0.6% (9 games) | -2.1% (9 games) | hypothesis (range includes zero) |
| lane = value, sport = nba | 61 | 51 (12) | 43% | 48% | -8.4% (-36.5% to +11.7%) | 30 (9) | +0.6% (9 games) | -2.1% (9 games) | hypothesis (range includes zero) |
| flagged = 6h+ before | 105 | 47 (5) | 64% | 56% | +12.5% (5 games) | 26 (3) | -2.9% (3 games) | +0.6% (3 games) | too few games (<10) |
| edge = 3-6% | 79 | 42 (12) | 48% | 48% | +0.9% (-32.1% to +22.5%) | 26 (9) | +0.2% (9 games) | -1.4% (9 games) | hypothesis (range includes zero) |
| price = -200 or shorter | 81 | 42 (12) | 64% | 64% | -6.3% (-33.3% to +18.5%) | 24 (8) | -7.6% (8 games) | -1.0% (8 games) | hypothesis (range includes zero) |
| lane = value, side = over | 36 | 30 (12) | 33% | 47% | -26.8% (-67.1% to +4.5%) | 17 (9) | +1.6% (9 games) | -2.6% (9 games) | hypothesis (range includes zero) |
| sport = nba, stat/market = pra | 40 | 27 (10) | 41% | 52% | -20.9% (-49.6% to +3.1%) | 18 (6) | -3.5% (6 games) | -0.2% (6 games) | hypothesis |
| stat/market = pra | 40 | 27 (10) | 41% | 52% | -20.9% (-49.6% to +3.1%) | 18 (6) | -3.5% (6 games) | -0.2% (6 games) | hypothesis |
| lane = likely, side = over | 30 | 23 (11) | 57% | 63% | -15.9% (-48.4% to +13.1%) | 15 (7) | -7.8% (7 games) | -1.3% (7 games) | hypothesis |
| lane = value, side = under | 29 | 21 (9) | 57% | 50% | +17.7% (9 games) | 13 (6) | -0.7% (6 games) | -1.3% (6 games) | hypothesis |
| sport = nba, stat/market = stl | 36 | 18 (9) | 56% | 64% | -17.2% (9 games) | 15 (8) | -6.1% (8 games) | -0.8% (8 games) | hypothesis |
| stat/market = stl | 36 | 18 (9) | 56% | 64% | -17.2% (9 games) | 15 (8) | -6.1% (8 games) | -0.8% (8 games) | hypothesis |
| tier = Lean | 13 | 11 (7) | 55% | 57% | -2.6% (7 games) | 6 (4) | -0.1% (4 games) | +0.3% (4 games) | hypothesis |
| edge = 6%+ | 75 | 10 (4) | 30% | 50% | -34.4% (4 games) | 5 (3) | +2.9% (3 games) | -4.8% (3 games) | hypothesis |
| tier = Best bet | 18 | 7 (6) | 71% | 66% | +2.9% (6 games) | 4 (4) | -5.4% (4 games) | +0.1% (4 games) | hypothesis |
| chance = 30-40% | 15 | 6 (4) | 33% | 38% | -9.0% (4 games) | 3 (2) | +8.2% (2 games) | +8.6% (2 games) | hypothesis |
| sport = nba, stat/market = blk | 9 | 4 (3) | 75% | 58% | +11.1% (3 games) | 3 (2) | -10.1% (2 games) | -2.6% (2 games) | hypothesis |
| stat/market = blk | 9 | 4 (3) | 75% | 58% | +11.1% (3 games) | 3 (2) | -10.1% (2 games) | -2.6% (2 games) | hypothesis |
| sport = nba, stat/market = ra | 3 | 2 (2) | 50% | 52% | +4.0% (2 games) | 1 (1) | +5.7% (–) | +0.3% (–) | hypothesis |
| stat/market = ra | 3 | 2 (2) | 50% | 52% | +4.0% (2 games) | 1 (1) | +5.7% (–) | +0.3% (–) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, side = away | 10 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, side = home | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = away | 10 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = home | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| side = yes | 88 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = nba, stat/market = moneyline | 8 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
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
| stat/market = moneyline | 15 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = pass_tds | 4 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = receptions | 5 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = rush_att | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
