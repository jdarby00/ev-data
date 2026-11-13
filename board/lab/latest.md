# Research lab report

Built 2026-11-13T19:35:21Z UTC from 2796 logged code candidates (1955 settled, 1003 with a close, 41 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 1322, ROI -4.5%; CLV n 399 over 40 games, -6.8%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 146, ROI -1.6%; CLV n 144 over 37 games, +1.9%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -2.5%; CLV n 460 over 39 games, -1.5%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1955, ROI -3.8%; CLV n 999 over 39 games, -3.1%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 500, ROI -4.0%; CLV n 337 over 40 games, -6.5%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 606, ROI -2.7%; CLV n 579 over 41 games, -0.7%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 822, ROI -4.8%; CLV n 62 over 26 games, -8.2%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 239, ROI +6.7%; CLV n 159 over 39 games, -2.7%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 382, ROI -7.7%; CLV n 285 over 39 games, -4.3%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 355, ROI -5.0%; CLV n 162 over 37 games, -2.2%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 286, ROI -4.2%; CLV n 172 over 36 games, -1.0%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 80, ROI +10.7%; CLV n 80 over 32 games, -5.5%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 217, ROI -7.7%; CLV n 80 over 31 games, -3.9%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 107, ROI -17.5%; CLV n 14 over 11 games, +0.7%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 716, ROI +0.3%; CLV n 665 over 40 games, -3.2%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1217, ROI -6.7%; CLV n 313 over 38 games, -3.0%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 1486, ROI -1.9%; CLV n 552 over 39 games, -3.5%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 469, ROI -9.6%; CLV n 451 over 41 games, -2.7%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 994, ROI -5.9%; CLV n 158 over 36 games, -7.8%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 319, ROI -1.3%; CLV n 290 over 39 games, -2.2%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 306, ROI -4.2%; CLV n 306 over 41 games, +0.8%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 336, ROI +0.6%; CLV n 249 over 39 games, -6.0%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 725, ROI -2.9%; CLV n 393 over 40 games, -6.7%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 363, ROI -0.3%; CLV n 335 over 39 games, -1.7%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative ROI (settled 547, ROI -6.3%; CLV n 6 over 4 games, -13.9%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 1316, ROI -4.7%; CLV n 393 over 40 games, -6.8%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 121, ROI -2.0%; CLV n 118 over 37 games, +1.5%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 492, ROI -2.3%; CLV n 465 over 39 games, -1.6%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 368, ROI -6.5%; CLV n 245 over 37 games, -2.5%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 845, ROI +2.4%; CLV n 329 over 26 games, -3.6%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 742, ROI -9.5%; CLV n 429 over 40 games, -3.1%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 682, ROI -4.7%; CLV n 414 over 40 games, -3.7%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 1273, ROI -3.3%; CLV n 589 over 39 games, -2.7%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1656, ROI -5.4%; CLV n 735 over 41 games, -3.7%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 299, ROI +5.1%; CLV n 268 over 25 games, -1.7%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 146, ROI -1.6%; CLV n 141 over 35 games, +1.8%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -2.5%; CLV n 460 over 39 games, -1.5%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1322, ROI -4.5%; CLV n 398 over 39 games, -6.8%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 76, ROI -14.5%; CLV n 76 over 32 games, +2.8%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 366, ROI -0.2%; CLV n 340 over 39 games, -1.8%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 280, ROI -2.1%; CLV n 260 over 40 games, -6.0%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1020, ROI -5.9%; CLV n 117 over 31 games, -9.1%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 239, ROI +6.7%; CLV n 159 over 39 games, -2.7%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 382, ROI -7.7%; CLV n 285 over 39 games, -4.3%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 355, ROI -5.0%; CLV n 162 over 37 games, -2.2%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 286, ROI -4.2%; CLV n 172 over 36 games, -1.0%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 80, ROI +10.7%; CLV n 80 over 32 games, -5.5%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 217, ROI -7.7%; CLV n 80 over 31 games, -3.9%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 107, ROI -17.5%; CLV n 14 over 11 games, +0.7%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 2796 | 1955 (41) | 62% | 62% | -3.8% (-8.3% to +0.7%) | 1003 (41) | -3.1% (-3.5% to -2.8%) | -0.0% (-0.3% to +0.2%) |  |
| sport = nba | 2688 | 1955 (41) | 62% | 62% | -3.8% (-8.3% to +0.7%) | 999 (39) | -3.1% (-3.5% to -2.8%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 2486 | 1656 (40) | 63% | 64% | -5.4% (-10.8% to -0.8%) | 735 (41) | -3.7% (-4.2% to -3.2%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 2150 | 1486 (41) | 66% | 65% | -1.9% (-7.6% to +3.4%) | 552 (39) | -3.5% (-4.0% to -2.9%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 1973 | 1322 (41) | 69% | 68% | -4.5% (-9.6% to +0.9%) | 399 (40) | -6.8% (-7.1% to -6.3%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 1958 | 1322 (41) | 69% | 68% | -4.5% (-9.6% to +0.9%) | 398 (39) | -6.8% (-7.1% to -6.3%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 1965 | 1316 (41) | 69% | 69% | -4.7% (-9.8% to +0.7%) | 393 (40) | -6.8% (-7.2% to -6.4%) | -0.4% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 1695 | 1273 (41) | 63% | 62% | -3.3% (-9.0% to +1.8%) | 589 (39) | -2.7% (-3.2% to -2.3%) | +0.3% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 1798 | 1217 (40) | 65% | 67% | -6.7% (-13.4% to -0.5%) | 313 (38) | -3.0% (-3.9% to -2.1%) | -0.2% (-0.7% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 1578 | 1020 (34) | 70% | 70% | -5.9% (-12.1% to +0.4%) | 117 (31) | -9.1% (-9.8% to -8.3%) | -0.9% (-1.4% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 1486 | 994 (37) | 71% | 71% | -5.9% (-11.7% to +0.2%) | 158 (36) | -7.8% (-8.4% to -7.1%) | -0.6% (-1.0% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 1528 | 845 (26) | 70% | 66% | +2.4% (-2.1% to +6.9%) | 329 (26) | -3.6% (-4.3% to -3.0%) | +0.4% (-0.0% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 1190 | 822 (28) | 73% | 72% | -4.8% (-11.1% to +1.5%) | 62 (26) | -8.2% (-9.7% to -6.7%) | -0.9% (-1.5% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 871 | 742 (40) | 57% | 61% | -9.5% (-15.8% to -3.2%) | 429 (40) | -3.1% (-3.6% to -2.5%) | -0.1% (-0.6% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 1135 | 725 (41) | 65% | 63% | -2.9% (-9.0% to +3.5%) | 393 (40) | -6.7% (-7.0% to -6.2%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 868 | 716 (41) | 56% | 55% | +0.3% (-6.4% to +7.1%) | 665 (40) | -3.2% (-3.7% to -2.8%) | +0.1% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1101 | 682 (39) | 61% | 62% | -4.7% (-11.7% to +3.1%) | 414 (40) | -3.7% (-4.3% to -3.1%) | -0.4% (-0.9% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 789 | 606 (41) | 47% | 49% | -2.7% (-11.2% to +6.0%) | 579 (41) | -0.7% (-1.1% to -0.2%) | +0.3% (-0.1% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 783 | 547 (14) | 73% | 74% | -6.3% (-11.9% to -0.5%) | 6 (4) | -13.9% (4 games) | -0.8% (–) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 783 | 500 (41) | 63% | 62% | -4.0% (-10.2% to +2.5%) | 337 (40) | -6.5% (-6.9% to -6.1%) | -0.4% (-0.8% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 573 | 492 (41) | 49% | 50% | -2.3% (-13.6% to +8.3%) | 465 (39) | -1.6% (-2.0% to -1.1%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 566 | 487 (41) | 48% | 50% | -2.5% (-13.4% to +7.9%) | 460 (39) | -1.5% (-1.9% to -1.1%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 566 | 487 (41) | 48% | 50% | -2.5% (-13.4% to +7.9%) | 460 (39) | -1.5% (-1.9% to -1.1%) | +0.7% (+0.3% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 646 | 469 (41) | 49% | 53% | -9.6% (-17.6% to -2.1%) | 451 (41) | -2.7% (-3.1% to -2.3%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 511 | 382 (41) | 59% | 61% | -7.7% (-14.3% to -1.9%) | 285 (39) | -4.3% (-4.8% to -3.8%) | +0.0% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 511 | 382 (41) | 59% | 61% | -7.7% (-14.3% to -1.9%) | 285 (39) | -4.3% (-4.8% to -3.8%) | +0.0% (-0.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 397 | 368 (39) | 55% | 58% | -6.5% (-13.9% to +1.6%) | 245 (37) | -2.5% (-3.1% to -2.1%) | -0.4% (-0.7% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 436 | 366 (41) | 50% | 50% | -0.2% (-11.5% to +10.6%) | 340 (39) | -1.8% (-2.3% to -1.3%) | +0.7% (+0.1% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 419 | 363 (41) | 52% | 52% | -0.3% (-11.4% to +10.2%) | 335 (39) | -1.7% (-2.1% to -1.3%) | -0.1% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 479 | 355 (40) | 60% | 61% | -5.0% (-13.3% to +2.4%) | 162 (37) | -2.2% (-2.7% to -1.8%) | +0.1% (-0.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 479 | 355 (40) | 60% | 61% | -5.0% (-13.3% to +2.4%) | 162 (37) | -2.2% (-2.7% to -1.8%) | +0.1% (-0.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 498 | 336 (41) | 65% | 61% | +0.6% (-6.2% to +7.5%) | 249 (39) | -6.0% (-6.4% to -5.6%) | -0.4% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 367 | 319 (41) | 51% | 52% | -1.3% (-14.1% to +10.5%) | 290 (39) | -2.2% (-2.7% to -1.8%) | -0.2% (-0.6% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 445 | 306 (41) | 43% | 46% | -4.2% (-15.4% to +7.4%) | 306 (41) | +0.8% (+0.2% to +1.2%) | +0.7% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| status change = yes | 310 | 299 (27) | 56% | 53% | +5.1% (-3.7% to +14.5%) | 268 (25) | -1.7% (-2.0% to -1.2%) | +0.2% (-0.3% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 379 | 286 (38) | 56% | 58% | -4.2% (-16.6% to +7.3%) | 172 (36) | -1.0% (-1.7% to -0.3%) | +0.4% (-0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 379 | 286 (38) | 56% | 58% | -4.2% (-16.6% to +7.3%) | 172 (36) | -1.0% (-1.7% to -0.3%) | +0.4% (-0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 354 | 280 (41) | 64% | 62% | -2.1% (-10.0% to +5.7%) | 260 (40) | -6.0% (-6.5% to -5.5%) | -0.4% (-0.8% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 303 | 259 (41) | 43% | 46% | -5.1% (-16.8% to +7.1%) | 256 (39) | +0.2% (-0.3% to +0.8%) | +0.5% (+0.1% to +1.0%) | hypothesis (range includes zero) |
| sport = nba, stat/market = ast | 320 | 239 (40) | 63% | 58% | +6.7% (-0.9% to +14.6%) | 159 (39) | -2.7% (-3.5% to -1.8%) | -0.2% (-1.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 320 | 239 (40) | 63% | 58% | +6.7% (-0.9% to +14.6%) | 159 (39) | -2.7% (-3.5% to -1.8%) | -0.2% (-1.0% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 306 | 217 (35) | 61% | 64% | -7.7% (-17.6% to +0.9%) | 80 (31) | -3.9% (-4.9% to -2.9%) | -0.1% (-0.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 306 | 217 (35) | 61% | 64% | -7.7% (-17.6% to +0.9%) | 80 (31) | -3.9% (-4.9% to -2.9%) | -0.1% (-0.6% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 257 | 146 (36) | 46% | 48% | -1.6% (-17.0% to +12.7%) | 144 (37) | +1.9% (+1.2% to +2.6%) | -1.4% (-1.9% to -0.8%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 164 | 146 (36) | 46% | 48% | -1.6% (-17.0% to +12.7%) | 141 (35) | +1.8% (+1.1% to +2.5%) | -1.4% (-2.0% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = pr | 211 | 132 (14) | 73% | 71% | -3.8% (-11.9% to +4.9%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| stat/market = pr | 211 | 132 (14) | 73% | 71% | -3.8% (-11.9% to +4.9%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| edge = 3-6% | 168 | 121 (36) | 46% | 48% | -2.0% (-19.2% to +14.2%) | 118 (37) | +1.5% (+0.7% to +2.2%) | -1.0% (-1.6% to -0.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 130 | 121 (31) | 44% | 49% | -9.4% (-28.6% to +13.3%) | 120 (31) | -0.8% (-1.6% to +0.0%) | +1.0% (+0.4% to +1.7%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 161 | 110 (14) | 72% | 72% | -5.0% (-11.8% to +2.2%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| stat/market = pa | 161 | 110 (14) | 72% | 72% | -5.0% (-11.8% to +2.2%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 163 | 107 (21) | 60% | 69% | -17.5% (-31.0% to -4.5%) | 14 (11) | +0.7% (-3.0% to +4.3%) | -0.9% (-3.0% to +1.1%) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 163 | 107 (21) | 60% | 69% | -17.5% (-31.0% to -4.5%) | 14 (11) | +0.7% (-3.0% to +4.3%) | -0.9% (-3.0% to +1.1%) | IN-SAMPLE SIGNAL: negative ROI |
| sport = nba, stat/market = stl | 98 | 80 (32) | 72% | 63% | +10.7% (-7.5% to +25.8%) | 80 (32) | -5.5% (-6.3% to -4.6%) | -0.4% (-1.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 98 | 80 (32) | 72% | 63% | +10.7% (-7.5% to +25.8%) | 80 (32) | -5.5% (-6.3% to -4.6%) | -0.4% (-1.3% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = over | 90 | 76 (33) | 38% | 46% | -14.5% (-37.9% to +8.2%) | 76 (32) | +2.8% (+1.6% to +3.8%) | -1.5% (-2.6% to -0.5%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = under | 78 | 70 (27) | 54% | 50% | +12.4% (-10.5% to +33.5%) | 65 (26) | +0.7% (-0.5% to +1.9%) | -1.3% (-2.5% to -0.3%) | hypothesis (range includes zero) |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| tier = Lean | 34 | 27 (19) | 59% | 57% | +6.6% (-16.7% to +31.3%) | 25 (18) | -1.9% (-3.4% to -0.8%) | -1.2% (-2.9% to +0.0%) | hypothesis |
| edge = 6%+ | 90 | 26 (13) | 46% | 48% | +5.0% (-38.3% to +53.6%) | 27 (14) | +3.9% (+2.0% to +6.1%) | -2.9% (-5.0% to -1.1%) | hypothesis |
| sport = nba, stat/market = blk | 26 | 25 (16) | 68% | 61% | +2.4% (-30.8% to +31.9%) | 25 (16) | -5.4% (-6.5% to -4.3%) | -0.8% (-1.4% to -0.3%) | hypothesis |
| stat/market = blk | 26 | 25 (16) | 68% | 61% | +2.4% (-30.8% to +31.9%) | 25 (16) | -5.4% (-6.5% to -4.3%) | -0.8% (-1.4% to -0.3%) | hypothesis |
| sport = nba, stat/market = moneyline | 34 | 22 (13) | 86% | 65% | +28.1% (+2.4% to +48.5%) | 22 (13) | -3.6% (-5.0% to -2.1%) | -0.2% (-1.5% to +1.1%) | hypothesis |
| stat/market = moneyline | 41 | 22 (13) | 86% | 65% | +28.1% (+2.4% to +48.5%) | 22 (13) | -3.6% (-5.0% to -2.1%) | -0.2% (-1.5% to +1.1%) | hypothesis |
| lane = likely, side = home | 19 | 15 (9) | 80% | 65% | +17.5% (9 games) | 15 (9) | -2.8% (9 games) | +0.4% (9 games) | hypothesis |
| side = home | 19 | 15 (9) | 80% | 65% | +17.5% (9 games) | 15 (9) | -2.8% (9 games) | +0.4% (9 games) | hypothesis |
| chance = 30-40% | 23 | 11 (7) | 36% | 38% | -0.5% (7 games) | 10 (6) | +5.9% (6 games) | +3.1% (6 games) | hypothesis |
| lane = likely, side = away | 22 | 7 (4) | 100% | 64% | +50.7% (4 games) | 7 (4) | -5.2% (4 games) | -1.6% (4 games) | hypothesis |
| side = away | 22 | 7 (4) | 100% | 64% | +50.7% (4 games) | 7 (4) | -5.2% (4 games) | -1.6% (4 games) | hypothesis |
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
