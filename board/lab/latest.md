# Research lab report

Built 2026-11-12T11:10:20Z UTC from 1718 logged code candidates (1546 settled, 879 with a close, 36 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 969, ROI -3.3%; CLV n 330 over 35 games, -6.7%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 140, ROI -2.1%; CLV n 137 over 33 games, +1.9%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 437, ROI -3.9%; CLV n 412 over 35 games, -1.6%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1546, ROI -3.4%; CLV n 877 over 35 games, -3.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 340, ROI -1.9%; CLV n 284 over 35 games, -6.3%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 552, ROI -3.6%; CLV n 526 over 36 games, -0.7%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 629, ROI -4.1%; CLV n 46 over 22 games, -8.9%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 196, ROI +6.5%; CLV n 137 over 35 games, -2.4%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 334, ROI -9.9%; CLV n 251 over 35 games, -4.0%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 274, ROI -3.9%; CLV n 145 over 33 games, -2.2%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 226, ROI -4.7%; CLV n 152 over 32 games, -1.0%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 70, ROI +16.1%; CLV n 70 over 28 games, -5.4%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 173, ROI -5.7%; CLV n 73 over 27 games, -3.9%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 72, ROI -20.2%; CLV n 11 over 9 games, +4.0%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 641, ROI +1.4%; CLV n 590 over 35 games, -3.2%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 889, ROI -7.3%; CLV n 271 over 34 games, -2.5%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 1122, ROI -0.5%; CLV n 473 over 35 games, -3.2%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 424, ROI -11.0%; CLV n 406 over 36 games, -2.7%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 739, ROI -5.3%; CLV n 130 over 31 games, -7.9%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 288, ROI -1.3%; CLV n 260 over 35 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 281, ROI -6.6%; CLV n 281 over 36 games, +0.8%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 238, ROI +3.8%; CLV n 208 over 35 games, -5.8%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 493, ROI -1.8%; CLV n 326 over 35 games, -6.5%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 330, ROI -0.3%; CLV n 303 over 35 games, -1.7%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 964, ROI -3.5%; CLV n 325 over 35 games, -6.7%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 115, ROI -2.6%; CLV n 111 over 33 games, +1.5%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 441, ROI -3.8%; CLV n 416 over 35 games, -1.6%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 308, ROI -2.5%; CLV n 222 over 33 games, -2.5%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 610, ROI +2.8%; CLV n 277 over 22 games, -3.4%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 628, ROI -9.8%; CLV n 380 over 35 games, -2.9%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 554, ROI -5.4%; CLV n 363 over 35 games, -3.6%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 992, ROI -2.3%; CLV n 516 over 35 games, -2.5%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1267, ROI -5.3%; CLV n 631 over 36 games, -3.5%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 279, ROI +5.2%; CLV n 248 over 22 games, -1.7%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 140, ROI -2.1%; CLV n 135 over 32 games, +1.8%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 437, ROI -3.9%; CLV n 412 over 35 games, -1.6%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 969, ROI -3.3%; CLV n 330 over 35 games, -6.7%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 73, ROI -17.1%; CLV n 73 over 30 games, +2.8%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 324, ROI +0.3%; CLV n 300 over 35 games, -1.8%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 113, ROI -15.9%; CLV n 112 over 27 games, -1.0%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 250, ROI -0.7%; CLV n 228 over 35 games, -6.0%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 703, ROI -4.9%; CLV n 86 over 27 games, -8.9%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 196, ROI +6.5%; CLV n 137 over 35 games, -2.4%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 334, ROI -9.9%; CLV n 251 over 35 games, -4.0%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 274, ROI -3.9%; CLV n 145 over 33 games, -2.2%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 226, ROI -4.7%; CLV n 152 over 32 games, -1.0%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 70, ROI +16.1%; CLV n 70 over 28 games, -5.4%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 173, ROI -5.7%; CLV n 73 over 27 games, -3.9%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 72, ROI -20.2%; CLV n 11 over 9 games, +4.0%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 1718 | 1546 (37) | 62% | 62% | -3.4% (-7.7% to +0.8%) | 879 (36) | -2.9% (-3.3% to -2.6%) | -0.1% (-0.4% to +0.2%) |  |
| sport = nba | 1612 | 1546 (37) | 62% | 62% | -3.4% (-7.7% to +0.8%) | 877 (35) | -3.0% (-3.3% to -2.6%) | -0.1% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 1433 | 1267 (36) | 63% | 64% | -5.3% (-10.2% to -1.0%) | 631 (36) | -3.5% (-4.0% to -2.9%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 1171 | 1122 (37) | 67% | 65% | -0.5% (-5.0% to +4.2%) | 473 (35) | -3.2% (-3.7% to -2.6%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 1031 | 992 (37) | 63% | 62% | -2.3% (-8.8% to +2.6%) | 516 (35) | -2.5% (-3.0% to -2.1%) | +0.2% (-0.2% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 1030 | 969 (37) | 71% | 69% | -3.3% (-7.7% to +1.5%) | 330 (35) | -6.7% (-7.1% to -6.1%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 1016 | 969 (37) | 71% | 69% | -3.3% (-7.7% to +1.5%) | 330 (35) | -6.7% (-7.1% to -6.1%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 1025 | 964 (37) | 71% | 69% | -3.5% (-7.8% to +1.2%) | 325 (35) | -6.7% (-7.2% to -6.2%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 924 | 889 (36) | 65% | 67% | -7.3% (-14.1% to -1.3%) | 271 (34) | -2.5% (-3.4% to -1.5%) | -0.3% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 792 | 739 (33) | 72% | 72% | -5.3% (-10.1% to +0.0%) | 130 (31) | -7.9% (-8.6% to -7.1%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 732 | 703 (30) | 72% | 72% | -4.9% (-10.2% to +0.2%) | 86 (27) | -8.9% (-9.8% to -7.8%) | -0.8% (-1.5% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 677 | 641 (37) | 56% | 55% | +1.4% (-6.2% to +8.6%) | 590 (35) | -3.2% (-3.7% to -2.7%) | +0.1% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 663 | 629 (24) | 74% | 73% | -4.1% (-9.1% to +1.9%) | 46 (22) | -8.9% (-10.7% to -7.0%) | -1.0% (-1.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 679 | 628 (36) | 57% | 60% | -9.8% (-16.2% to -3.6%) | 380 (35) | -2.9% (-3.5% to -2.2%) | -0.2% (-0.6% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 702 | 610 (22) | 70% | 66% | +2.8% (-1.8% to +7.3%) | 277 (22) | -3.4% (-4.2% to -2.6%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 687 | 554 (35) | 60% | 62% | -5.4% (-12.8% to +3.2%) | 363 (35) | -3.6% (-4.2% to -2.9%) | -0.4% (-0.9% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 662 | 552 (37) | 47% | 49% | -3.6% (-13.2% to +6.0%) | 526 (36) | -0.7% (-1.1% to -0.2%) | +0.3% (-0.2% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 530 | 493 (37) | 66% | 63% | -1.8% (-7.3% to +3.8%) | 326 (35) | -6.5% (-7.0% to -6.0%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 457 | 441 (37) | 48% | 50% | -3.8% (-15.5% to +8.0%) | 416 (35) | -1.6% (-2.1% to -1.2%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 453 | 437 (37) | 48% | 50% | -3.9% (-15.5% to +7.3%) | 412 (35) | -1.6% (-2.1% to -1.1%) | +0.7% (+0.3% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 453 | 437 (37) | 48% | 50% | -3.9% (-15.5% to +7.3%) | 412 (35) | -1.6% (-2.1% to -1.1%) | +0.7% (+0.3% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 445 | 426 (10) | 75% | 74% | -4.6% (-9.4% to +1.0%) | 4 (3) | -19.1% (3 games) | – (–) | hypothesis (range includes zero) |
| book = fanduel | 547 | 424 (37) | 48% | 53% | -11.0% (-19.1% to -2.9%) | 406 (36) | -2.7% (-3.1% to -2.3%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 367 | 340 (37) | 64% | 62% | -1.9% (-8.8% to +4.5%) | 284 (35) | -6.3% (-6.7% to -5.9%) | -0.4% (-0.9% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 343 | 334 (37) | 57% | 61% | -9.9% (-17.1% to -3.8%) | 251 (35) | -4.0% (-4.5% to -3.6%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 343 | 334 (37) | 57% | 61% | -9.9% (-17.1% to -3.8%) | 251 (35) | -4.0% (-4.5% to -3.6%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 345 | 330 (37) | 52% | 52% | -0.3% (-12.0% to +10.9%) | 303 (35) | -1.7% (-2.2% to -1.2%) | -0.1% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 338 | 324 (37) | 50% | 51% | +0.3% (-12.6% to +11.9%) | 300 (35) | -1.8% (-2.4% to -1.2%) | +0.7% (+0.1% to +1.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 337 | 308 (35) | 57% | 57% | -2.5% (-10.3% to +5.4%) | 222 (33) | -2.5% (-3.0% to -2.0%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 299 | 288 (37) | 51% | 52% | -1.3% (-15.0% to +10.7%) | 260 (35) | -2.3% (-2.8% to -1.8%) | -0.3% (-0.7% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 381 | 281 (37) | 42% | 46% | -6.6% (-18.8% to +6.1%) | 281 (36) | +0.8% (+0.2% to +1.3%) | +0.6% (+0.1% to +1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| status change = yes | 285 | 279 (24) | 56% | 53% | +5.2% (-4.4% to +14.9%) | 248 (22) | -1.7% (-2.1% to -1.2%) | +0.1% (-0.4% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 284 | 274 (36) | 59% | 60% | -3.9% (-13.9% to +4.8%) | 145 (33) | -2.2% (-2.8% to -1.7%) | +0.1% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 284 | 274 (36) | 59% | 60% | -3.9% (-13.9% to +4.8%) | 145 (33) | -2.2% (-2.8% to -1.7%) | +0.1% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 269 | 250 (37) | 65% | 62% | -0.7% (-9.3% to +7.5%) | 228 (35) | -6.0% (-6.6% to -5.5%) | -0.4% (-0.9% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 246 | 238 (37) | 66% | 61% | +3.8% (-4.3% to +11.5%) | 208 (35) | -5.8% (-6.2% to -5.3%) | -0.4% (-0.9% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 247 | 236 (37) | 42% | 46% | -8.0% (-20.5% to +4.8%) | 234 (35) | +0.2% (-0.3% to +0.8%) | +0.4% (-0.0% to +1.0%) | hypothesis (range includes zero) |
| sport = nba, stat/market = reb | 230 | 226 (34) | 55% | 57% | -4.7% (-18.8% to +7.7%) | 152 (32) | -1.0% (-1.7% to -0.2%) | +0.2% (-0.5% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 230 | 226 (34) | 55% | 57% | -4.7% (-18.8% to +7.7%) | 152 (32) | -1.0% (-1.7% to -0.2%) | +0.2% (-0.5% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 207 | 196 (36) | 62% | 57% | +6.5% (-2.0% to +16.1%) | 137 (35) | -2.4% (-3.3% to -1.4%) | -0.3% (-1.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 207 | 196 (36) | 62% | 57% | +6.5% (-2.0% to +16.1%) | 137 (35) | -2.4% (-3.3% to -1.4%) | -0.3% (-1.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 181 | 173 (31) | 62% | 64% | -5.7% (-16.8% to +2.7%) | 73 (27) | -3.9% (-5.0% to -2.8%) | +0.0% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 181 | 173 (31) | 62% | 64% | -5.7% (-16.8% to +2.7%) | 73 (27) | -3.9% (-5.0% to -2.8%) | +0.0% (-0.4% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 235 | 140 (33) | 46% | 48% | -2.1% (-17.3% to +12.0%) | 137 (33) | +1.9% (+1.2% to +2.7%) | -1.4% (-2.0% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 143 | 140 (33) | 46% | 48% | -2.1% (-17.3% to +12.0%) | 135 (32) | +1.8% (+1.1% to +2.5%) | -1.5% (-2.1% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| edge = 3-6% | 146 | 115 (33) | 46% | 48% | -2.6% (-20.0% to +12.0%) | 111 (33) | +1.5% (+0.7% to +2.2%) | -1.0% (-1.7% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 115 | 113 (27) | 41% | 49% | -15.9% (-34.5% to +7.1%) | 112 (27) | -1.0% (-1.7% to -0.1%) | +0.8% (+0.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 92 | 88 (10) | 77% | 73% | -0.1% (-6.9% to +7.6%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| stat/market = pr | 92 | 88 (10) | 77% | 73% | -0.1% (-6.9% to +7.6%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 78 | 75 (10) | 75% | 74% | -4.1% (-12.1% to +4.5%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| stat/market = pa | 78 | 75 (10) | 75% | 74% | -4.1% (-12.1% to +4.5%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| lane = value, side = over | 77 | 73 (31) | 37% | 46% | -17.1% (-40.0% to +7.5%) | 73 (30) | +2.8% (+1.6% to +4.0%) | -1.5% (-2.7% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ra | 76 | 72 (17) | 58% | 70% | -20.2% (-37.8% to -3.6%) | 11 (9) | +4.0% (9 games) | -0.3% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 76 | 72 (17) | 58% | 70% | -20.2% (-37.8% to -3.6%) | 11 (9) | +4.0% (9 games) | -0.3% (9 games) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = stl | 76 | 70 (28) | 76% | 63% | +16.1% (-1.9% to +31.9%) | 70 (28) | -5.4% (-6.3% to -4.4%) | -0.5% (-1.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 76 | 70 (28) | 76% | 63% | +16.1% (-1.9% to +31.9%) | 70 (28) | -5.4% (-6.3% to -4.4%) | -0.5% (-1.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 70 | 67 (25) | 55% | 50% | +14.2% (-9.3% to +34.8%) | 62 (24) | +0.7% (-0.6% to +2.0%) | -1.4% (-2.6% to -0.3%) | hypothesis (range includes zero) |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| edge = 6%+ | 90 | 26 (13) | 46% | 48% | +5.0% (-38.3% to +53.6%) | 27 (14) | +3.9% (+2.0% to +6.1%) | -2.9% (-5.0% to -1.1%) | hypothesis |
| tier = Lean | 26 | 25 (17) | 56% | 57% | +0.8% (-23.2% to +27.0%) | 23 (16) | -2.0% (-3.6% to -0.8%) | -1.3% (-3.3% to -0.1%) | hypothesis |
| sport = nba, stat/market = blk | 23 | 22 (14) | 73% | 61% | +8.9% (-27.0% to +38.4%) | 22 (14) | -5.5% (-6.7% to -4.2%) | -0.7% (-1.3% to -0.2%) | hypothesis |
| stat/market = blk | 23 | 22 (14) | 73% | 61% | +8.9% (-27.0% to +38.4%) | 22 (14) | -5.5% (-6.7% to -4.2%) | -0.7% (-1.3% to -0.2%) | hypothesis |
| sport = nba, stat/market = moneyline | 22 | 16 (10) | 81% | 63% | +23.4% (-11.1% to +51.7%) | 16 (10) | -3.4% (-5.3% to -1.5%) | -0.1% (-1.9% to +1.6%) | hypothesis |
| stat/market = moneyline | 29 | 16 (10) | 81% | 63% | +23.4% (-11.1% to +51.7%) | 16 (10) | -3.4% (-5.3% to -1.5%) | -0.1% (-1.9% to +1.6%) | hypothesis |
| chance = 30-40% | 19 | 11 (7) | 36% | 38% | -0.5% (7 games) | 10 (6) | +5.9% (6 games) | +3.1% (6 games) | hypothesis |
| lane = likely, side = home | 12 | 9 (6) | 67% | 63% | +2.1% (6 games) | 9 (6) | -2.0% (6 games) | +1.1% (6 games) | hypothesis |
| side = home | 12 | 9 (6) | 67% | 63% | +2.1% (6 games) | 9 (6) | -2.0% (6 games) | +1.1% (6 games) | hypothesis |
| lane = likely, side = away | 17 | 7 (4) | 100% | 64% | +50.7% (4 games) | 7 (4) | -5.2% (4 games) | -1.6% (4 games) | hypothesis |
| side = away | 17 | 7 (4) | 100% | 64% | +50.7% (4 games) | 7 (4) | -5.2% (4 games) | -1.6% (4 games) | hypothesis |
| chance = 10-20% | 49 | 0 (0) | – | – | – (–) | 1 (1) | +8.0% (–) | -1.9% (–) | hypothesis |
| chance = 20-30% | 28 | 0 (0) | – | – | – (–) | 1 (1) | +6.1% (–) | +0.7% (–) | hypothesis |
| lane = likely, sport = nfl | 13 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 88 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
| lane = value, sport = nfl | 92 | 0 (0) | – | – | – (–) | 2 (1) | +7.0% (–) | -0.6% (–) | hypothesis |
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
