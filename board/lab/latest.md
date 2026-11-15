# Research lab report

Built 2026-11-15T19:35:26Z UTC from 4303 logged code candidates (3288 settled, 1548 with a close, 64 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 2392, ROI -4.7%; CLV n 641 over 59 games, -7.6%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 202, ROI -3.7%; CLV n 247 over 58 games, +2.4%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 694, ROI -2.6%; CLV n 660 over 54 games, -1.5%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 3288, ROI -4.2%; CLV n 1489 over 54 games, -3.7%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 59 over 10 games, +4.3%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 948, ROI -4.9%; CLV n 542 over 59 games, -7.3%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 43, ROI -0.2%; CLV n 40 over 27 games, -1.9%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 1444, ROI -4.6%; CLV n 99 over 40 games, -8.7%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI -5.9%; CLV n 38 over 24 games, -3.0%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 391, ROI +0.7%; CLV n 250 over 54 games, -3.3%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 593, ROI -8.1%; CLV n 444 over 54 games, -5.1%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 594, ROI -5.0%; CLV n 218 over 50 games, -2.0%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -1.4%; CLV n 264 over 51 games, -1.8%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +12.3%; CLV n 100 over 43 games, -5.7%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 384, ROI -5.0%; CLV n 120 over 44 games, -3.8%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 200, ROI -13.7%; CLV n 21 over 15 games, -2.1%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 49 over 10 games, +6.2%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1003, ROI -0.5%; CLV n 947 over 57 games, -3.3%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 2252, ROI -5.8%; CLV n 514 over 55 games, -4.5%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 49 over 10 games, +6.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 2647, ROI -2.7%; CLV n 868 over 56 games, -4.4%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 641, ROI -10.5%; CLV n 680 over 64 games, -2.1%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 1770, ROI -5.3%; CLV n 255 over 55 games, -8.5%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 447, ROI -4.6%; CLV n 407 over 52 games, -2.3%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 431, ROI -1.8%; CLV n 483 over 64 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 640, ROI -2.6%; CLV n 403 over 54 games, -6.8%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 1393, ROI -4.1%; CLV n 626 over 58 games, -7.5%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 513, ROI -3.3%; CLV n 473 over 52 games, -1.9%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative ROI (settled 949, ROI -5.5%; CLV n 15 over 12 games, -9.3%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 2384, ROI -4.8%; CLV n 633 over 59 games, -7.6%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 176, ROI -5.1%; CLV n 189 over 56 games, +1.6%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 701, ROI -2.5%; CLV n 667 over 54 games, -1.6%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 27, ROI +10.2%; CLV n 59 over 23 games, +5.3%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 559, ROI -8.1%; CLV n 351 over 53 games, -2.7%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 1609, ROI +0.6%; CLV n 571 over 48 games, -4.1%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 1120, ROI -9.2%; CLV n 626 over 59 games, -3.2%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 1155, ROI -6.5%; CLV n 654 over 63 games, -3.4%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 2133, ROI -2.9%; CLV n 894 over 54 games, -3.4%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2915, ROI -5.2%; CLV n 1206 over 64 games, -3.8%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 373, ROI +3.8%; CLV n 342 over 33 games, -1.8%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 202, ROI -3.7%; CLV n 197 over 48 games, +1.5%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 694, ROI -2.6%; CLV n 660 over 54 games, -1.5%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 2392, ROI -4.7%; CLV n 632 over 54 games, -7.6%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 50 over 10 games, +6.1%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 113, ROI -13.8%; CLV n 116 over 44 games, +1.9%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 536, ROI -0.1%; CLV n 501 over 54 games, -1.8%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 378, ROI -3.4%; CLV n 364 over 57 games, -6.3%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 1981, ROI -5.0%; CLV n 239 over 47 games, -10.2%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 49 over 10 games, +6.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 391, ROI +0.7%; CLV n 250 over 54 games, -3.3%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 593, ROI -8.1%; CLV n 444 over 54 games, -5.1%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 594, ROI -5.0%; CLV n 218 over 50 games, -2.0%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 487, ROI -1.4%; CLV n 264 over 51 games, -1.8%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 100, ROI +12.3%; CLV n 100 over 43 games, -5.7%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 33, ROI -5.9%; CLV n 34 over 21 games, -2.9%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 384, ROI -5.0%; CLV n 120 over 44 games, -3.8%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative ROI (settled 200, ROI -13.7%; CLV n 21 over 15 games, -2.1%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 49 over 10 games, +6.2%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 4303 | 3288 (55) | 63% | 63% | -4.2% (-7.8% to -0.6%) | 1548 (64) | -3.4% (-3.8% to -3.0%) | -0.1% (-0.4% to +0.1%) |  |
| sport = nba | 4103 | 3288 (55) | 63% | 63% | -4.2% (-7.8% to -0.6%) | 1489 (54) | -3.7% (-4.0% to -3.4%) | -0.0% (-0.3% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 3913 | 2915 (54) | 64% | 64% | -5.2% (-9.4% to -1.4%) | 1206 (64) | -3.8% (-4.3% to -3.3%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 3373 | 2647 (55) | 66% | 65% | -2.7% (-7.1% to +1.5%) | 868 (56) | -4.4% (-4.8% to -3.9%) | +0.1% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 3123 | 2392 (55) | 68% | 68% | -4.7% (-8.8% to -0.9%) | 641 (59) | -7.6% (-8.0% to -7.1%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 3094 | 2392 (55) | 68% | 68% | -4.7% (-8.8% to -0.9%) | 632 (54) | -7.6% (-8.1% to -7.1%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 3115 | 2384 (55) | 68% | 68% | -4.8% (-8.9% to -1.1%) | 633 (59) | -7.6% (-8.1% to -7.1%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 2911 | 2252 (54) | 66% | 66% | -5.8% (-10.8% to -0.9%) | 514 (55) | -4.5% (-5.3% to -3.7%) | -0.4% (-0.9% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 2704 | 2133 (55) | 63% | 63% | -2.9% (-7.6% to +1.4%) | 894 (54) | -3.4% (-3.9% to -3.0%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 2612 | 1981 (48) | 69% | 69% | -5.0% (-9.9% to -0.3%) | 239 (47) | -10.2% (-11.0% to -9.4%) | -0.9% (-1.4% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 2335 | 1770 (51) | 70% | 70% | -5.3% (-9.7% to -0.8%) | 255 (55) | -8.5% (-9.0% to -7.9%) | -0.7% (-1.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 2205 | 1609 (40) | 69% | 66% | +0.6% (-4.2% to +5.0%) | 571 (48) | -4.1% (-4.9% to -3.2%) | -0.1% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 1868 | 1444 (42) | 72% | 71% | -4.6% (-9.4% to +0.0%) | 99 (40) | -8.7% (-9.8% to -7.7%) | -0.9% (-1.4% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 1843 | 1393 (55) | 64% | 64% | -4.1% (-8.7% to +0.7%) | 626 (58) | -7.5% (-8.0% to -7.0%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 1599 | 1155 (53) | 61% | 63% | -6.5% (-11.3% to -1.4%) | 654 (63) | -3.4% (-4.0% to -2.7%) | -0.5% (-0.9% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 1489 | 1120 (54) | 58% | 61% | -9.2% (-14.4% to -4.0%) | 626 (59) | -3.2% (-3.6% to -2.7%) | +0.0% (-0.4% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1171 | 1003 (55) | 55% | 55% | -0.5% (-5.8% to +4.6%) | 947 (57) | -3.3% (-3.7% to -2.9%) | +0.1% (-0.2% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 1225 | 949 (28) | 74% | 73% | -5.5% (-10.0% to -1.3%) | 15 (12) | -9.3% (-13.4% to -5.7%) | -0.8% (7 games) | IN-SAMPLE SIGNAL: negative ROI |
| tier = Straight | 1255 | 948 (55) | 63% | 62% | -4.9% (-9.2% to -0.6%) | 542 (59) | -7.3% (-7.9% to -6.8%) | -0.5% (-0.8% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1131 | 853 (55) | 47% | 49% | -3.0% (-9.9% to +3.6%) | 867 (64) | -0.4% (-0.9% to +0.1%) | +0.1% (-0.2% to +0.5%) | hypothesis (range includes zero) |
| edge = 0-3% | 799 | 701 (55) | 48% | 50% | -2.5% (-10.6% to +5.6%) | 667 (54) | -1.6% (-1.9% to -1.1%) | +0.7% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 792 | 694 (55) | 48% | 50% | -2.6% (-11.0% to +5.5%) | 660 (54) | -1.5% (-1.9% to -1.1%) | +0.8% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 792 | 694 (55) | 48% | 50% | -2.6% (-11.0% to +5.5%) | 660 (54) | -1.5% (-1.9% to -1.1%) | +0.8% (+0.4% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 930 | 641 (55) | 48% | 53% | -10.5% (-16.7% to -4.4%) | 680 (64) | -2.1% (-2.6% to -1.6%) | -0.3% (-0.6% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 807 | 640 (55) | 63% | 61% | -2.6% (-7.3% to +2.5%) | 403 (54) | -6.8% (-7.4% to -6.2%) | -0.4% (-0.8% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 745 | 594 (54) | 61% | 62% | -5.0% (-11.6% to +0.6%) | 218 (50) | -2.0% (-2.4% to -1.6%) | +0.3% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 745 | 594 (54) | 61% | 62% | -5.0% (-11.6% to +0.6%) | 218 (50) | -2.0% (-2.4% to -1.6%) | +0.3% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 724 | 593 (55) | 59% | 62% | -8.1% (-13.2% to -3.5%) | 444 (54) | -5.1% (-5.5% to -4.6%) | -0.3% (-0.6% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 724 | 593 (55) | 59% | 62% | -8.1% (-13.2% to -3.5%) | 444 (54) | -5.1% (-5.5% to -4.6%) | -0.3% (-0.6% to +0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 609 | 559 (52) | 55% | 59% | -8.1% (-13.8% to -2.1%) | 351 (53) | -2.7% (-3.2% to -2.2%) | -0.5% (-0.8% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 619 | 536 (55) | 50% | 51% | -0.1% (-8.7% to +7.8%) | 501 (54) | -1.8% (-2.3% to -1.3%) | +0.7% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 583 | 513 (54) | 50% | 53% | -3.3% (-12.2% to +5.5%) | 473 (52) | -1.9% (-2.3% to -1.5%) | -0.2% (-0.5% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 581 | 487 (52) | 60% | 59% | -1.4% (-9.2% to +5.9%) | 264 (51) | -1.8% (-2.4% to -1.2%) | +0.6% (+0.1% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 581 | 487 (52) | 60% | 59% | -1.4% (-9.2% to +5.9%) | 264 (51) | -1.8% (-2.4% to -1.2%) | +0.6% (+0.1% to +1.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 507 | 447 (54) | 49% | 52% | -4.6% (-14.7% to +4.7%) | 407 (52) | -2.3% (-2.7% to -1.9%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 654 | 431 (55) | 45% | 46% | -1.8% (-10.9% to +7.3%) | 483 (64) | +1.2% (+0.7% to +1.8%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ast | 497 | 391 (54) | 61% | 59% | +0.7% (-5.8% to +7.5%) | 250 (54) | -3.3% (-4.0% to -2.5%) | -0.2% (-0.9% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 497 | 391 (54) | 61% | 59% | +0.7% (-5.8% to +7.5%) | 250 (54) | -3.3% (-4.0% to -2.5%) | -0.2% (-0.9% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 476 | 384 (49) | 63% | 64% | -5.0% (-11.9% to +1.3%) | 120 (44) | -3.8% (-4.7% to -3.1%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 476 | 384 (49) | 63% | 64% | -5.0% (-11.9% to +1.3%) | 120 (44) | -3.8% (-4.7% to -3.1%) | -0.1% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = under | 453 | 378 (55) | 63% | 62% | -3.4% (-10.4% to +3.7%) | 364 (57) | -6.3% (-6.7% to -5.9%) | -0.5% (-0.8% to -0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 390 | 373 (35) | 55% | 53% | +3.8% (-3.9% to +11.9%) | 342 (33) | -1.8% (-2.2% to -1.5%) | +0.2% (-0.1% to +0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 40-50% | 420 | 364 (55) | 44% | 46% | -3.1% (-13.0% to +6.6%) | 370 (57) | +0.3% (-0.2% to +0.9%) | +0.5% (-0.1% to +1.1%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pr | 350 | 268 (28) | 70% | 69% | -4.4% (-12.0% to +2.6%) | 7 (5) | -19.4% (5 games) | -3.4% (–) | hypothesis (range includes zero) |
| stat/market = pr | 350 | 268 (28) | 70% | 69% | -4.4% (-12.0% to +2.6%) | 7 (5) | -19.4% (5 games) | -3.4% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 277 | 210 (28) | 70% | 70% | -4.7% (-11.3% to +1.7%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 277 | 210 (28) | 70% | 70% | -4.7% (-11.3% to +1.7%) | 3 (3) | -14.9% (3 games) | -5.5% (–) | hypothesis (range includes zero) |
| lane = value | 388 | 202 (49) | 45% | 48% | -3.7% (-16.4% to +8.6%) | 247 (58) | +2.4% (+1.7% to +3.3%) | -1.7% (-2.3% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 217 | 202 (49) | 45% | 48% | -3.7% (-16.4% to +8.6%) | 197 (48) | +1.5% (+0.9% to +2.1%) | -1.6% (-2.1% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = ra | 264 | 200 (35) | 62% | 69% | -13.7% (-23.6% to -4.0%) | 21 (15) | -2.1% (-5.3% to +1.1%) | -1.6% (-3.6% to +0.2%) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = ra | 264 | 200 (35) | 62% | 69% | -13.7% (-23.6% to -4.0%) | 21 (15) | -2.1% (-5.3% to +1.1%) | -1.6% (-3.6% to +0.2%) | IN-SAMPLE SIGNAL: negative ROI |
| edge = 3-6% | 244 | 176 (49) | 44% | 48% | -5.1% (-19.1% to +7.4%) | 189 (56) | +1.6% (+1.0% to +2.1%) | -1.2% (-1.7% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 173 | 158 (42) | 43% | 49% | -11.0% (-27.3% to +6.6%) | 159 (42) | -0.7% (-1.3% to +0.1%) | +1.1% (+0.5% to +1.8%) | hypothesis (range includes zero) |
| lane = value, side = over | 126 | 113 (43) | 38% | 46% | -13.8% (-32.8% to +5.4%) | 116 (44) | +1.9% (+1.0% to +2.8%) | -2.1% (-2.9% to -1.3%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 111 | 100 (43) | 74% | 63% | +12.3% (-3.5% to +26.0%) | 100 (43) | -5.7% (-6.4% to -5.0%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 111 | 100 (43) | 74% | 63% | +12.3% (-3.5% to +26.0%) | 100 (43) | -5.7% (-6.4% to -5.0%) | -0.5% (-1.2% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 99 | 89 (37) | 53% | 50% | +9.0% (-11.4% to +27.9%) | 82 (35) | +0.9% (-0.2% to +2.1%) | -0.9% (-1.9% to +0.1%) | hypothesis (range includes zero) |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| tier = Lean | 49 | 43 (29) | 56% | 57% | -0.2% (-19.9% to +21.4%) | 40 (27) | -1.9% (-3.3% to -0.5%) | -1.0% (-2.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 44 | 33 (20) | 64% | 66% | -5.9% (-33.7% to +20.8%) | 34 (21) | -2.9% (-4.5% to -0.9%) | +0.6% (-1.0% to +2.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 58 | 33 (20) | 64% | 66% | -5.9% (-33.7% to +20.8%) | 38 (24) | -3.0% (-4.5% to -1.2%) | +0.4% (-1.1% to +2.2%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = blk | 34 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| stat/market = blk | 34 | 28 (18) | 68% | 61% | +5.3% (-25.7% to +33.3%) | 28 (18) | -5.5% (-6.5% to -4.4%) | -1.3% (-2.3% to -0.5%) | hypothesis |
| edge = 6%+ | 145 | 27 (14) | 48% | 48% | +10.2% (-31.5% to +59.7%) | 59 (23) | +5.3% (+3.2% to +7.9%) | -3.2% (-5.7% to -1.0%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 30-40% | 37 | 19 (14) | 42% | 38% | +14.0% (-49.4% to +79.3%) | 24 (17) | +4.5% (+3.1% to +5.9%) | +0.6% (-1.4% to +2.9%) | hypothesis |
| lane = likely, side = home | 22 | 17 (11) | 82% | 66% | +20.7% (-11.0% to +46.6%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| side = home | 22 | 17 (11) | 82% | 66% | +20.7% (-11.0% to +46.6%) | 19 (13) | -2.5% (-3.9% to -1.0%) | +0.9% (-0.5% to +2.1%) | hypothesis |
| lane = likely, side = away | 36 | 16 (9) | 44% | 66% | -34.1% (9 games) | 19 (11) | -3.5% (-5.8% to -0.1%) | -0.1% (-2.4% to +3.3%) | hypothesis |
| side = away | 36 | 16 (9) | 44% | 66% | -34.1% (9 games) | 19 (11) | -3.5% (-5.8% to -0.1%) | -0.1% (-2.4% to +3.3%) | hypothesis |
| chance = 10-20% | 88 | 0 (0) | – | – | – (–) | 21 (8) | +7.0% (8 games) | -1.0% (8 games) | hypothesis |
| chance = 20-30% | 52 | 0 (0) | – | – | – (–) | 19 (9) | +6.7% (9 games) | -1.5% (9 games) | hypothesis |
| lane = likely, sport = nfl | 28 | 0 (0) | – | – | – (–) | 9 (5) | -5.6% (5 games) | -0.9% (5 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 163 | 0 (0) | – | – | – (–) | 49 (10) | +6.2% (+4.1% to +9.0%) | -2.3% (-4.6% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 171 | 0 (0) | – | – | – (–) | 50 (10) | +6.1% (+4.1% to +8.9%) | -2.3% (-4.5% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 163 | 0 (0) | – | – | – (–) | 49 (10) | +6.2% (+4.1% to +9.0%) | -2.3% (-4.6% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 199 | 0 (0) | – | – | – (–) | 59 (10) | +4.3% (+2.3% to +7.1%) | -2.1% (-3.9% to -0.1%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 163 | 0 (0) | – | – | – (–) | 49 (10) | +6.2% (+4.1% to +9.0%) | -2.3% (-4.6% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 1 (1) | +2.6% (–) | -0.6% (–) | hypothesis |
| sport = nfl, stat/market = moneyline | 13 | 0 (0) | – | – | – (–) | 4 (3) | -4.0% (3 games) | -1.2% (3 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 3 (3) | -6.6% (3 games) | -0.4% (3 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 2 (2) | -7.4% (2 games) | -1.0% (2 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 163 | 0 (0) | – | – | – (–) | 49 (10) | +6.2% (+4.1% to +9.0%) | -2.3% (-4.6% to +0.0%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 1 (1) | +2.6% (–) | -0.6% (–) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 3 (3) | -6.6% (3 games) | -0.4% (3 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 2 (2) | -7.4% (2 games) | -1.0% (2 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
