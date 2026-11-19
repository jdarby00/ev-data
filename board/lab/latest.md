# Research lab report

Built 2026-11-19T11:10:39Z UTC from 6925 logged code candidates (6373 settled, 2605 with a close, 102 games with a close). 90% ranges resample whole games, because props in one game move together. A slice is flagged only with 30+ bets, 10+ games and a range that excludes zero, and even then it is an in-sample signal: a finding needs a pre-registered out-of-sample check (TEST_PLAN.md). Many slices are tested at once, so expect some flags by chance. CLV includes the market EV at flag time (the vig paid, or our edge when positive); "close move" (CLV minus that) is what the close did afterwards (descriptive, not flagged). Ranges on fewer than 10 games are not shown: a bootstrap over that few games is too narrow to trust (they stay in latest.json).

## In-sample signals

- **lane = likely**: IN-SAMPLE SIGNAL: negative CLV (settled 4943, ROI -4.8%; CLV n 1162 over 96 games, -8.5%)
- **lane = value**: IN-SAMPLE SIGNAL: positive CLV (settled 291, ROI -4.6%; CLV n 362 over 94 games, +2.6%)
- **lane = early**: IN-SAMPLE SIGNAL: negative CLV (settled 1139, ROI -1.1%; CLV n 1081 over 86 games, -1.7%)
- **sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 6373, ROI -4.1%; CLV n 2511 over 87 games, -4.4%)
- **sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 94 over 15 games, +4.0%)
- **tier = Straight**: IN-SAMPLE SIGNAL: negative CLV (settled 2089, ROI -4.9%; CLV n 989 over 96 games, -8.3%)
- **tier = Lean**: IN-SAMPLE SIGNAL: negative CLV (settled 80, ROI +0.1%; CLV n 75 over 47 games, -2.6%)
- **tier = Value**: IN-SAMPLE SIGNAL: negative CLV (settled 1350, ROI -2.0%; CLV n 1368 over 101 games, -0.5%)
- **tier = Best bet**: IN-SAMPLE SIGNAL: negative CLV (settled 2854, ROI -4.7%; CLV n 173 over 67 games, -9.4%)
- **stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 64, ROI -9.8%; CLV n 72 over 46 games, -3.7%)
- **stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 716, ROI +1.1%; CLV n 404 over 85 games, -3.9%)
- **stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1080, ROI -8.7%; CLV n 771 over 87 games, -5.6%)
- **stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1193, ROI -4.8%; CLV n 361 over 82 games, -2.7%)
- **stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 950, ROI -0.4%; CLV n 454 over 83 games, -3.4%)
- **stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 144, ROI +9.2%; CLV n 144 over 63 games, -5.8%)
- **stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 42, ROI +9.2%; CLV n 42 over 26 games, -5.5%)
- **stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 752, ROI -3.4%; CLV n 211 over 74 games, -3.8%)
- **stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 417, ROI -13.1%; CLV n 42 over 29 games, -6.6%)
- **stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 564, ROI -4.8%; CLV n 13 over 9 games, -19.7%)
- **side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 35, ROI -13.9%; CLV n 37 over 24 games, -3.4%)
- **side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 1612, ROI -1.7%; CLV n 1529 over 93 games, -3.5%)
- **side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 4697, ROI -4.9%; CLV n 930 over 90 games, -6.0%)
- **side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI -4.8%; CLV n 35 over 22 games, -3.9%)
- **side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **book = draftkings**: IN-SAMPLE SIGNAL: negative CLV (settled 5321, ROI -3.4%; CLV n 1500 over 92 games, -5.5%)
- **book = fanduel**: IN-SAMPLE SIGNAL: negative CLV (settled 1052, ROI -7.5%; CLV n 1105 over 102 games, -2.2%)
- **price = -200 or shorter**: IN-SAMPLE SIGNAL: negative CLV (settled 3585, ROI -4.9%; CLV n 428 over 92 games, -9.2%)
- **price = -129 to +100**: IN-SAMPLE SIGNAL: negative CLV (settled 754, ROI -4.4%; CLV n 690 over 84 games, -2.4%)
- **price = +101 or longer**: IN-SAMPLE SIGNAL: positive CLV (settled 638, ROI +0.5%; CLV n 716 over 101 games, +1.2%)
- **price = -199 to -130**: IN-SAMPLE SIGNAL: negative CLV (settled 1396, ROI -4.0%; CLV n 771 over 87 games, -7.8%)
- **chance = 60-70%**: IN-SAMPLE SIGNAL: negative CLV (settled 3007, ROI -5.0%; CLV n 1125 over 95 games, -8.5%)
- **chance = 50-60%**: IN-SAMPLE SIGNAL: negative CLV (settled 863, ROI -3.7%; CLV n 801 over 86 games, -2.1%)
- **chance = 30-40%**: IN-SAMPLE SIGNAL: positive CLV (settled 31, ROI +14.2%; CLV n 39 over 30 games, +4.9%)
- **chance = 10-20%**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 35 over 13 games, +7.2%)
- **chance = 70-80%**: IN-SAMPLE SIGNAL: negative CLV (settled 1886, ROI -4.3%; CLV n 37 over 24 games, -7.6%)
- **edge = under 0%**: IN-SAMPLE SIGNAL: negative CLV (settled 4934, ROI -4.8%; CLV n 1153 over 96 games, -8.5%)
- **edge = 3-6%**: IN-SAMPLE SIGNAL: positive CLV (settled 256, ROI -5.1%; CLV n 277 over 89 games, +1.7%)
- **edge = 0-3%**: IN-SAMPLE SIGNAL: negative CLV (settled 1146, ROI -0.9%; CLV n 1088 over 86 games, -1.7%)
- **edge = 6%+**: IN-SAMPLE SIGNAL: positive CLV (settled 37, ROI -0.8%; CLV n 87 over 34 games, +5.5%)
- **flagged = under 2h before**: IN-SAMPLE SIGNAL: negative CLV (settled 953, ROI -4.9%; CLV n 572 over 83 games, -3.0%)
- **flagged = 6h+ before**: IN-SAMPLE SIGNAL: negative CLV (settled 3344, ROI -3.7%; CLV n 1035 over 83 games, -5.2%)
- **flagged = 2-6h before**: IN-SAMPLE SIGNAL: negative CLV (settled 2076, ROI -4.5%; CLV n 998 over 95 games, -3.6%)
- **minutes moved = no**: IN-SAMPLE SIGNAL: negative CLV (settled 2135, ROI -6.4%; CLV n 1004 over 101 games, -3.8%)
- **minutes moved = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 4238, ROI -2.9%; CLV n 1601 over 87 games, -4.3%)
- **status change = no**: IN-SAMPLE SIGNAL: negative CLV (settled 5781, ROI -5.1%; CLV n 2050 over 102 games, -4.6%)
- **status change = yes**: IN-SAMPLE SIGNAL: negative CLV (settled 592, ROI +5.9%; CLV n 555 over 51 games, -2.2%)
- **lane = value, sport = nba**: IN-SAMPLE SIGNAL: positive CLV (settled 291, ROI -4.6%; CLV n 284 over 79 games, +1.7%)
- **lane = early, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 1139, ROI -1.1%; CLV n 1081 over 86 games, -1.7%)
- **lane = likely, sport = nba**: IN-SAMPLE SIGNAL: negative CLV (settled 4943, ROI -4.8%; CLV n 1146 over 87 games, -8.5%)
- **lane = value, sport = nfl**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 78 over 15 games, +5.9%)
- **lane = likely, side = home**: IN-SAMPLE SIGNAL: negative CLV (settled 35, ROI -13.9%; CLV n 37 over 24 games, -3.4%)
- **lane = value, side = over**: IN-SAMPLE SIGNAL: positive CLV (settled 163, ROI -1.1%; CLV n 166 over 69 games, +2.3%)
- **lane = early, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 880, ROI -0.5%; CLV n 822 over 86 games, -1.9%)
- **lane = early, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 259, ROI -3.4%; CLV n 259 over 68 games, -1.2%)
- **lane = likely, side = under**: IN-SAMPLE SIGNAL: negative CLV (settled 604, ROI -1.9%; CLV n 585 over 92 games, -6.7%)
- **lane = likely, side = away**: IN-SAMPLE SIGNAL: negative CLV (settled 29, ROI -4.8%; CLV n 35 over 22 games, -3.9%)
- **lane = likely, side = over**: IN-SAMPLE SIGNAL: negative CLV (settled 4275, ROI -5.1%; CLV n 505 over 81 games, -11.2%)
- **lane = value, side = yes**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = ast**: IN-SAMPLE SIGNAL: negative CLV (settled 716, ROI +1.1%; CLV n 404 over 85 games, -3.9%)
- **sport = nba, stat/market = tpm**: IN-SAMPLE SIGNAL: negative CLV (settled 1080, ROI -8.7%; CLV n 771 over 87 games, -5.6%)
- **sport = nba, stat/market = pts**: IN-SAMPLE SIGNAL: negative CLV (settled 1193, ROI -4.8%; CLV n 361 over 82 games, -2.7%)
- **sport = nba, stat/market = reb**: IN-SAMPLE SIGNAL: negative CLV (settled 950, ROI -0.4%; CLV n 454 over 83 games, -3.4%)
- **sport = nba, stat/market = stl**: IN-SAMPLE SIGNAL: negative CLV (settled 144, ROI +9.2%; CLV n 144 over 63 games, -5.8%)
- **sport = nba, stat/market = moneyline**: IN-SAMPLE SIGNAL: negative CLV (settled 64, ROI -9.8%; CLV n 64 over 40 games, -3.6%)
- **sport = nba, stat/market = blk**: IN-SAMPLE SIGNAL: negative CLV (settled 42, ROI +9.2%; CLV n 42 over 26 games, -5.5%)
- **sport = nba, stat/market = pra**: IN-SAMPLE SIGNAL: negative CLV (settled 752, ROI -3.4%; CLV n 211 over 74 games, -3.8%)
- **sport = nba, stat/market = ra**: IN-SAMPLE SIGNAL: negative CLV (settled 417, ROI -13.1%; CLV n 42 over 29 games, -6.6%)
- **sport = nfl, stat/market = anytime_td**: IN-SAMPLE SIGNAL: positive CLV (settled 0, ROI +0.0%; CLV n 74 over 15 games, +6.2%)
- **sport = nba, stat/market = pr**: IN-SAMPLE SIGNAL: negative ROI (settled 564, ROI -4.8%; CLV n 13 over 9 games, -19.7%)

## Every slice

| Slice | Logged | Settled (games) | Win rate | Chance given | ROI (90%) | CLV n (games) | CLV (90%) | Close move (90%) | Read |
|---|---|---|---|---|---|---|---|---|---|
| all | 6925 | 6373 (89) | 63% | 63% | -4.1% (-6.5% to -1.8%) | 2605 (102) | -4.1% (-4.4% to -3.8%) | -0.2% (-0.4% to -0.0%) |  |
| sport = nba | 6715 | 6373 (89) | 63% | 63% | -4.1% (-6.5% to -1.8%) | 2511 (87) | -4.4% (-4.7% to -4.1%) | -0.1% (-0.3% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = no | 6307 | 5781 (88) | 64% | 64% | -5.1% (-8.0% to -2.6%) | 2050 (102) | -4.6% (-5.1% to -4.2%) | -0.3% (-0.5% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = draftkings | 5623 | 5321 (89) | 66% | 65% | -3.4% (-6.1% to -0.8%) | 1500 (92) | -5.5% (-5.9% to -5.1%) | -0.2% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely | 5263 | 4943 (89) | 68% | 67% | -4.8% (-7.4% to -2.1%) | 1162 (96) | -8.5% (-8.9% to -8.0%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, sport = nba | 5233 | 4943 (89) | 68% | 67% | -4.8% (-7.4% to -2.1%) | 1146 (87) | -8.5% (-8.9% to -8.0%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = under 0% | 5254 | 4934 (89) | 68% | 67% | -4.8% (-7.4% to -2.2%) | 1153 (96) | -8.5% (-8.9% to -8.0%) | -0.8% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = over | 4964 | 4697 (88) | 66% | 66% | -4.9% (-8.2% to -1.5%) | 930 (90) | -6.0% (-6.7% to -5.3%) | -0.4% (-0.7% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = likely, side = over | 4523 | 4275 (82) | 68% | 68% | -5.1% (-8.2% to -2.0%) | 505 (81) | -11.2% (-11.9% to -10.5%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = yes | 4462 | 4238 (89) | 64% | 63% | -2.9% (-5.9% to -0.2%) | 1601 (87) | -4.3% (-4.8% to -4.0%) | +0.1% (-0.2% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -200 or shorter | 3841 | 3585 (85) | 70% | 69% | -4.9% (-7.7% to -2.1%) | 428 (92) | -9.2% (-9.9% to -8.6%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 6h+ before | 3712 | 3344 (71) | 66% | 65% | -3.7% (-6.9% to -0.7%) | 1035 (83) | -5.2% (-5.8% to -4.6%) | -0.2% (-0.5% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 60-70% | 3204 | 3007 (89) | 64% | 64% | -5.0% (-8.1% to -1.8%) | 1125 (95) | -8.5% (-8.9% to -8.0%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Best bet | 3031 | 2854 (76) | 72% | 71% | -4.7% (-7.7% to -1.7%) | 173 (67) | -9.4% (-10.5% to -8.3%) | -0.9% (-1.4% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| minutes moved = no | 2463 | 2135 (87) | 62% | 64% | -6.4% (-10.2% to -2.7%) | 1004 (101) | -3.8% (-4.2% to -3.2%) | -0.6% (-0.9% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Straight | 2232 | 2089 (89) | 63% | 62% | -4.9% (-8.2% to -1.5%) | 989 (96) | -8.3% (-8.7% to -7.8%) | -0.7% (-1.0% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = 2-6h before | 2212 | 2076 (88) | 62% | 62% | -4.5% (-8.0% to -1.3%) | 998 (95) | -3.6% (-4.0% to -3.2%) | -0.0% (-0.4% to +0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 70-80% | 2004 | 1886 (62) | 74% | 73% | -4.3% (-7.2% to -1.6%) | 37 (24) | -7.6% (-9.6% to -5.8%) | +0.1% (-0.6% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| side = under | 1704 | 1612 (89) | 55% | 55% | -1.7% (-6.3% to +3.2%) | 1529 (93) | -3.5% (-3.9% to -3.1%) | -0.1% (-0.4% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -199 to -130 | 1460 | 1396 (89) | 62% | 61% | -4.0% (-7.6% to -0.5%) | 771 (87) | -7.8% (-8.2% to -7.3%) | -0.7% (-1.1% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| tier = Value | 1579 | 1350 (88) | 48% | 49% | -2.0% (-8.2% to +4.0%) | 1368 (101) | -0.5% (-0.9% to -0.1%) | +0.2% (-0.1% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pts | 1250 | 1193 (88) | 62% | 63% | -4.8% (-8.9% to -0.8%) | 361 (82) | -2.7% (-3.1% to -2.3%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pts | 1250 | 1193 (88) | 62% | 63% | -4.8% (-8.9% to -0.8%) | 361 (82) | -2.7% (-3.1% to -2.3%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 0-3% | 1188 | 1146 (88) | 49% | 50% | -0.9% (-7.8% to +5.9%) | 1088 (86) | -1.7% (-2.1% to -1.4%) | +0.6% (+0.3% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early | 1181 | 1139 (88) | 49% | 50% | -1.1% (-8.1% to +5.8%) | 1081 (86) | -1.7% (-2.0% to -1.4%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, sport = nba | 1181 | 1139 (88) | 49% | 50% | -1.1% (-8.1% to +5.8%) | 1081 (86) | -1.7% (-2.0% to -1.4%) | +0.7% (+0.4% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = tpm | 1133 | 1080 (89) | 60% | 62% | -8.7% (-12.3% to -5.0%) | 771 (87) | -5.6% (-5.9% to -5.2%) | -0.4% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = tpm | 1133 | 1080 (89) | 60% | 62% | -8.7% (-12.3% to -5.0%) | 771 (87) | -5.6% (-5.9% to -5.2%) | -0.4% (-0.6% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| book = fanduel | 1302 | 1052 (89) | 50% | 53% | -7.5% (-13.0% to -2.1%) | 1105 (102) | -2.2% (-2.6% to -1.8%) | -0.2% (-0.5% to -0.0%) | IN-SAMPLE SIGNAL: negative CLV |
| flagged = under 2h before | 1001 | 953 (81) | 58% | 59% | -4.9% (-9.6% to +0.1%) | 572 (83) | -3.0% (-3.5% to -2.6%) | -0.5% (-0.7% to -0.3%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = reb | 984 | 950 (86) | 62% | 60% | -0.4% (-5.3% to +4.3%) | 454 (83) | -3.4% (-4.0% to -2.7%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = reb | 984 | 950 (86) | 62% | 60% | -0.4% (-5.3% to +4.3%) | 454 (83) | -3.4% (-4.0% to -2.7%) | +0.4% (-0.1% to +0.9%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = early, side = under | 912 | 880 (88) | 50% | 51% | -0.5% (-8.4% to +6.6%) | 822 (86) | -1.9% (-2.3% to -1.5%) | +0.6% (+0.3% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 50-60% | 899 | 863 (86) | 50% | 53% | -3.7% (-10.9% to +3.4%) | 801 (86) | -2.1% (-2.4% to -1.8%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| price = -129 to +100 | 783 | 754 (86) | 49% | 52% | -4.4% (-11.8% to +2.8%) | 690 (84) | -2.4% (-2.7% to -2.1%) | -0.1% (-0.4% to +0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pra | 796 | 752 (83) | 64% | 64% | -3.4% (-7.8% to +0.9%) | 211 (74) | -3.8% (-4.4% to -3.3%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = pra | 796 | 752 (83) | 64% | 64% | -3.4% (-7.8% to +0.9%) | 211 (74) | -3.8% (-4.4% to -3.3%) | +0.2% (-0.1% to +0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = ast | 766 | 716 (88) | 62% | 60% | +1.1% (-4.3% to +6.3%) | 404 (85) | -3.9% (-4.4% to -3.3%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ast | 766 | 716 (88) | 62% | 60% | +1.1% (-4.3% to +6.3%) | 404 (85) | -3.9% (-4.4% to -3.3%) | -0.3% (-0.8% to +0.2%) | IN-SAMPLE SIGNAL: negative CLV |
| price = +101 or longer | 841 | 638 (88) | 45% | 46% | +0.5% (-7.5% to +8.3%) | 716 (101) | +1.2% (+0.7% to +1.6%) | +0.4% (-0.0% to +0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = under | 655 | 604 (89) | 64% | 62% | -1.9% (-7.9% to +3.9%) | 585 (92) | -6.7% (-7.0% to -6.3%) | -0.8% (-1.1% to -0.5%) | IN-SAMPLE SIGNAL: negative CLV |
| status change = yes | 618 | 592 (53) | 56% | 53% | +5.9% (-1.5% to +12.7%) | 555 (51) | -2.2% (-2.6% to -1.8%) | -0.1% (-0.5% to +0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = pr | 595 | 564 (62) | 69% | 68% | -4.8% (-9.4% to -0.3%) | 13 (9) | -19.7% (9 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| stat/market = pr | 595 | 564 (62) | 69% | 68% | -4.8% (-9.4% to -0.3%) | 13 (9) | -19.7% (9 games) | -2.9% (2 games) | IN-SAMPLE SIGNAL: negative ROI |
| chance = 40-50% | 566 | 536 (87) | 45% | 46% | +0.2% (-7.7% to +8.4%) | 542 (89) | +0.2% (-0.2% to +0.7%) | +0.6% (+0.1% to +1.0%) | hypothesis (range includes zero) |
| sport = nba, stat/market = pa | 474 | 451 (62) | 70% | 69% | -4.2% (-9.0% to +0.4%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| stat/market = pa | 474 | 451 (62) | 70% | 69% | -4.2% (-9.0% to +0.4%) | 5 (5) | -17.5% (5 games) | -5.5% (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = ra | 442 | 417 (69) | 63% | 68% | -13.1% (-20.0% to -5.7%) | 42 (29) | -6.6% (-9.7% to -3.3%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = ra | 442 | 417 (69) | 63% | 68% | -13.1% (-20.0% to -5.7%) | 42 (29) | -6.6% (-9.7% to -3.3%) | -2.2% (-4.0% to -0.6%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value | 481 | 291 (82) | 44% | 48% | -4.6% (-15.0% to +5.5%) | 362 (94) | +2.6% (+2.0% to +3.3%) | -1.5% (-2.0% to -1.1%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nba | 301 | 291 (82) | 44% | 48% | -4.6% (-15.0% to +5.5%) | 284 (79) | +1.7% (+1.1% to +2.2%) | -1.4% (-1.8% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = early, side = over | 269 | 259 (68) | 47% | 49% | -3.4% (-18.3% to +11.2%) | 259 (68) | -1.2% (-1.7% to -0.6%) | +0.7% (+0.2% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 3-6% | 321 | 256 (81) | 44% | 48% | -5.1% (-15.9% to +5.8%) | 277 (89) | +1.7% (+1.1% to +2.2%) | -1.0% (-1.5% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, side = over | 172 | 163 (68) | 44% | 46% | -1.1% (-17.3% to +16.1%) | 166 (69) | +2.3% (+1.5% to +3.1%) | -1.6% (-2.4% to -0.9%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nba, stat/market = stl | 155 | 144 (63) | 72% | 63% | +9.2% (-3.4% to +20.8%) | 144 (63) | -5.8% (-6.3% to -5.2%) | -0.7% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = stl | 155 | 144 (63) | 72% | 63% | +9.2% (-3.4% to +20.8%) | 144 (63) | -5.8% (-6.3% to -5.2%) | -0.7% (-1.2% to -0.1%) | IN-SAMPLE SIGNAL: negative CLV |
| lane = value, side = under | 137 | 128 (60) | 44% | 50% | -9.2% (-26.8% to +7.6%) | 122 (61) | +0.9% (-0.1% to +1.8%) | -1.1% (-2.1% to -0.2%) | hypothesis (range includes zero) |
| tier = Lean | 83 | 80 (48) | 56% | 57% | +0.1% (-15.5% to +15.1%) | 75 (47) | -2.6% (-3.6% to -1.7%) | -1.2% (-2.0% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| sport = nba, stat/market = moneyline | 70 | 64 (40) | 62% | 67% | -9.8% (-29.1% to +9.1%) | 64 (40) | -3.6% (-4.6% to -2.4%) | -0.1% (-1.1% to +1.1%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = moneyline | 85 | 64 (40) | 62% | 67% | -9.8% (-29.1% to +9.1%) | 72 (46) | -3.7% (-4.6% to -2.6%) | -0.2% (-1.1% to +0.8%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 80-90% | 55 | 50 (10) | 80% | 81% | -7.3% (-17.7% to +3.7%) | 0 (0) | – (–) | – (–) | hypothesis (range includes zero) |
| sport = nba, stat/market = blk | 50 | 42 (26) | 71% | 61% | +9.2% (-13.4% to +29.0%) | 42 (26) | -5.5% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| stat/market = blk | 50 | 42 (26) | 71% | 61% | +9.2% (-13.4% to +29.0%) | 42 (26) | -5.5% (-6.3% to -4.7%) | -1.0% (-1.7% to -0.4%) | IN-SAMPLE SIGNAL: negative CLV |
| edge = 6%+ | 162 | 37 (20) | 43% | 48% | -0.8% (-37.6% to +37.9%) | 87 (34) | +5.5% (+3.9% to +7.2%) | -3.0% (-4.7% to -1.4%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = home | 40 | 35 (22) | 60% | 68% | -13.9% (-38.4% to +11.6%) | 37 (24) | -3.4% (-4.4% to -2.4%) | +0.1% (-0.8% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| side = home | 40 | 35 (22) | 60% | 68% | -13.9% (-38.4% to +11.6%) | 37 (24) | -3.4% (-4.4% to -2.4%) | +0.1% (-0.8% to +1.0%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 30-40% | 49 | 31 (24) | 42% | 38% | +14.2% (-27.1% to +59.7%) | 39 (30) | +4.9% (+3.4% to +6.4%) | +1.2% (-0.6% to +3.2%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = likely, side = away | 45 | 29 (18) | 66% | 67% | -4.8% (-33.8% to +23.5%) | 35 (22) | -3.9% (-5.6% to -1.9%) | -0.5% (-2.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| side = away | 45 | 29 (18) | 66% | 67% | -4.8% (-33.8% to +23.5%) | 35 (22) | -3.9% (-5.6% to -1.9%) | -0.5% (-2.2% to +1.5%) | IN-SAMPLE SIGNAL: negative CLV |
| chance = 10-20% | 95 | 0 (0) | – | – | – (–) | 35 (13) | +7.2% (+4.6% to +10.8%) | -1.3% (-3.4% to +1.2%) | IN-SAMPLE SIGNAL: positive CLV |
| chance = 20-30% | 53 | 0 (0) | – | – | – (–) | 26 (13) | +6.2% (+4.5% to +7.9%) | -1.5% (-2.5% to -0.6%) | hypothesis |
| lane = likely, sport = nfl | 29 | 0 (0) | – | – | – (–) | 16 (9) | -5.5% (9 games) | -0.7% (9 games) | hypothesis |
| lane = likely, sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| lane = value, side = yes | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| lane = value, sport = nfl | 180 | 0 (0) | – | – | – (–) | 78 (15) | +5.9% (+4.6% to +7.8%) | -2.2% (-3.5% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| side = yes | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl | 209 | 0 (0) | – | – | – (–) | 94 (15) | +4.0% (+2.5% to +5.8%) | -1.9% (-3.1% to -0.7%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = anytime_td | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| sport = nfl, stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| sport = nfl, stat/market = moneyline | 14 | 0 (0) | – | – | – (–) | 8 (6) | -4.4% (6 games) | -1.2% (6 games) | hypothesis |
| sport = nfl, stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| sport = nfl, stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| sport = nfl, stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
| sport = soccer | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| sport = soccer, stat/market = moneyline | 1 | 0 (0) | – | – | – (–) | 0 (0) | – (–) | – (–) | no data |
| stat/market = anytime_td | 172 | 0 (0) | – | – | – (–) | 74 (15) | +6.2% (+4.9% to +8.1%) | -2.1% (-3.6% to -0.6%) | IN-SAMPLE SIGNAL: positive CLV |
| stat/market = ints | 3 | 0 (0) | – | – | – (–) | 2 (2) | +2.4% (2 games) | -1.2% (2 games) | hypothesis |
| stat/market = pass_tds | 8 | 0 (0) | – | – | – (–) | 4 (4) | -6.2% (4 games) | -0.2% (4 games) | hypothesis |
| stat/market = receptions | 10 | 0 (0) | – | – | – (–) | 5 (4) | -5.9% (4 games) | -1.2% (4 games) | hypothesis |
| stat/market = rush_att | 2 | 0 (0) | – | – | – (–) | 1 (1) | -3.8% (–) | -10.5% (–) | hypothesis |
