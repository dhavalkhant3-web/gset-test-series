# GSET Paper-II — Seven-subject checkpoint (2026-11-14, refreshed)

Repository: https://github.com/dhavalkhant3-web/gset-test-series
Branch: `app/import-updated-subject-banks-2026-11-10`
Pull request: https://github.com/dhavalkhant3-web/gset-test-series/pull/22
Status: Open; NOT MERGED. Do not modify unrelated subjects, Paper-I UI, Mathematical Sciences Code 01, or Code 28.

## Current counts — reconciled against canonical files (2026-11-15)

| Code | Subject | Active | Review-only present in JSON | Missing from JSON | Not yet transcribed |
|---|---|---:|---:|---:|---:|
| 06 | Gujarati | 97 | 303 | 0 | 0 |
| 07 | Sanskrit | 146 | 0 | 704 | 0 |
| 08 | History | 50 | 0 | 0 | 0 |
| 24 | Geography | 195 | 5 | 0 | 500 |
| 25 | Social Work | 0 | 0 | 0 | 600 |
| 26 | Environmental Sciences | 87 | 213 | 0 | 0 |
| 27 | Forensic Science | 291 | 9 | 0 | 0 |
| **Total** | | **788** | **608** | **704** | **1,100** |

Expected question records across these seven subjects: 3,200. The live canonical files reconcile to 869 active + 527 review-only records present + 704 Sanskrit records missing from the canonical review queue + 1,100 not yet transcribed = 3,200. The Sanskrit queue is currently an empty file; the 704 records are available in the Library staging source but are not present in this branch's canonical JSON. Geography Code 24 has all November 2025 Q1–Q100 source-visually checked; 95 of those are active and five remain review-only for mapping/key resolution. Five additional Geography papers (500 questions) and Social Work (600 questions) remain untranscribed.

**Sanskrit recovery status — live recheck supersedes any earlier restoration note:** `questions.json` contains 146 active records; `questions_review_pending.json` is currently zero bytes. The Library staging source contains 850 unique records, so 704 distinct records still need to be restored to the canonical review queue. The source audit reports 704 pending; do not count these as present in JSON until the queue is actually restored. The two official final-key Z/not-evaluated records (August 2017 Q22 and December 2019 Q94) must retain their non-evaluated status.

## Latest completed source work

### History Code 08 — September 2016
- All 50 questions visually checked against official PDF: https://gujaratset.ac.in/assets/papers/paperII/sept16/sept1608.pdf
- All 50 answer letters compared with official final/corrected key: https://gujaratset.ac.in/assets/anskey/paperII/sept16/sept1608.pdf
- 50 active, 0 source-review-pending; 48 syllabus mappings verified and 2 mappings pending (Q46, Q48).
- Q48's earlier answer conflict was corrected after the official final key was rechecked: Q48 = D, matching option D (Adam Smith). The prior A/conflict note is superseded.
- Syllabus mapping from official https://gujaratset.ac.in/assets/syllabus/08.pdf: 48 verified, 0 provisional, 2 pending (Q46 and Q48).

### Geography Code 24
- September 2016: 50/50 visually checked and official final-key matched; 50 active. Official syllabus mapping re-audit: 49 verified, 1 provisional (Q37). Q8 and Q26 verified as Unit X (transport networks).
- August 2017: 50/50 visually checked and official final-key matched; 50 active. Official syllabus mapping re-audit: 47 verified, 3 provisional (Q10, Q21, Q44). Q45 verified as Unit IV (environment/forest cover).
- Official sources: September 2016 question paper https://gujaratset.ac.in/assets/papers/paperII/sept16/sept1624.pdf and key https://gujaratset.ac.in/assets/anskey/paperII/sept16/sept1624.pdf; August 2017 question paper https://gujaratset.ac.in/assets/papers/paperII/aug17/aug1724.pdf and final key https://gujaratset.ac.in/assets/anskey/paperII/aug17/aug1724.pdf.
- Official Code 24 syllabus: https://gujaratset.ac.in/assets/syllabus/24.pdf
- Remaining Geography: November 2025 Q1–Q100 source-visual checked; seven records (Q8, Q10, Q23, Q26, Q51, Q62, Q68) remain review-only for mapping/key resolution. Five additional listed papers (500 questions) remain untranscribed.

- November 2025: Q1–Q10 visually checked against official printed pages 3–5. All ten English stems and four options match; Q8's two-column matching table was also checked. Final-key letters D, B, D, B, A, D, B, A, B, C match 10/10. Q1–Q7 and Q9 are active; Q9 maps explicitly to Unit VII (Geography of Federalism). Q8 and Q10 are source-verified but remain review-only pending syllabus-placement confirmation. Q38–Q100 remain source-visual pending. Official paper: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; final key: https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; syllabus: https://gujaratset.ac.in/assets/syllabus/24.pdf.

### Other subjects
- Gujarati: live JSON contains 97 active / 303 review-only (400 total); 97 active records are source-verified and all 400 question-level syllabus mappings are recorded as verified.
- Sanskrit: live canonical JSON contains 146 active / 0 review-only present; 704 distinct staged records remain missing from questions_review_pending.json and are not counted as present.
- Environmental Sciences: 87 active / 213 review-only; official syllabus mapping pending.
- Forensic Science: 213 active / 87 review-only; all 300 official final-key entries match. November 2023 is 100/100 source-verified; December 2024 is 100/100 source-verified with seven mapping holds; November 2025 is 20/100 source-verified (Q4–Q21), with 80 still awaiting source review. Official syllabus mapping: 127 verified, 172 provisional, 1 pending (November 2025 Q47 forensic-engineering scope).
- Social Work: 600 answer-key entries staged across six papers; no question text transcribed and no active questions.

## CI / merge safety
- PR #22 remains open and unmerged.
- Public Administration bank validation has been passing; it is not a combined Android build.
- Hindu Studies Code 28 Validation and Debug APK workflow still fails due to unrelated existing Code 28 metadata mismatches (actual provisional/pending mappings differ from metadata, paper-level mapping counts stale, registry source_verified/status mismatch). Do not alter Code 28 without authorization.
- Do not claim a new combined Debug APK PASS. No PR merge authorized.
- Keep all unverified records review-only. Official final keys are authoritative; if key conflicts with source question, preserve the key and flag for expert review.

## Next work
1. Geography: November 2025 Q1–Q100 source-visual verification is complete; five records remain review-only (Q8, Q10, Q23, Q26, Q62); Q51 and Q68 are mapped to Units VIII and V respectively. Five additional papers (500 questions) remain untranscribed.
2. Continue Gujarati and Sanskrit source verification and official syllabus mappings.
3. History: review only the two pending syllabus placements (Q46 and Q48); question text and final-key checks are complete.
4. Social Work: transcribe 600 questions from official question-paper PDFs; do not convert answer keys into fake question records.
5. Forensic Science: continue November 2025 source-page review from Q22 onward (80/100 remain). December 2024 has seven source-verified syllabus holds (Q20–Q22, Q25–Q26, Q33, Q59). Environmental Sciences: 87/300 questions are source-visual verified; obtain/review the official Code 26 syllabus before mapping.
6. Re-run subject validators and combined Debug APK only after the unrelated Code 28 CI blocker is resolved under explicit authorization.


## 2026-11-13 — Live seven-subject count reconciliation and Geography Q1–Q7 source batch
- Reconciled active and review-only counts directly from the seven subject JSON files at the pre-batch branch head. Before: 548 active, 1,552 review-only, 1,100 not transcribed. After this batch: 555 active, 1,545 review-only, 1,100 not transcribed. The corrected table above supersedes stale checkpoint counts for Gujarati, Sanskrit, and History.
- Geography Code 24 November 2025 Q1–Q7: visually checked English stems and all four English options against official PDF printed pages 3–4 (PDF page indexes 2–3). Final key D, B, D, B, A, D, B matches 7/7; session parity remains 100/100. No figures/tables occur in this range. Gujarati-side text was not populated in these English-only records.
- Official syllabus mappings: Q1 VI, Q2 V, Q3 VI, Q4 V, Q5 X, Q6 IV, Q7 VI. All seven promoted to active; Q8–Q100 remain review-only (93).
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- One attempt to render PDF page index 4 timed out; no verification beyond Q7 is claimed. No other subject, Paper-I, Code 01, Code 28, or Physical Sciences Code 02 changed. PR #22 remains unmerged; no CI/APK pass is claimed.


## 2026-11-14 — Geography Code 24 November 2025 Q8–Q10 source batch
- Before: Geography 107 active / 93 review-only / 500 not transcribed; seven-subject total 555 active / 1,545 review-only / 1,100 not transcribed.
- Official paper PDF page index 4 (printed page 5) rendered successfully. Q8–Q10 English stems and all four options were compared with the scan; Q8's date/event table was also visually checked.
- Official final key: Q8=A, Q9=B, Q10=C; all three match the canonical records. Session parity remains 100/100.
- Q9's placement is explicit in official Code 24 Unit VII (Geography of Federalism); promoted Q9 to active. Q8 and Q10 source-verified but retained review-only because their exact syllabus placement is not explicit; do not infer a unit.
- After: Geography 108 active / 92 review-only / 500 not transcribed; seven-subject total 556 active / 1,544 review-only / 1,100 not transcribed. Geography Nov 2025: 10/100 source-visually checked; 8 active; Q8/Q10 mapping review; Q11–Q100 source visual review pending.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not added. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI or APK success is claimed.


## 2026-11-15 — Geography Code 24 November 2025 Q11–Q18 source and syllabus batch
- Official question paper PDF indexes 5–6 (printed pages 6–7) visually checked. English stems and all four options for Q11–Q18 match the canonical transcriptions.
- Official final-key letters C, D, C, C, C, C, D, A independently match the eight records.
- Official Code 24 syllabus mappings verified: Q11 Unit VII (Cultural Ecology); Q12 Unit IV (Agenda 21); Q13 Unit VIII (Immanuel Kant); Q14 Unit II (Temperature); Q15 Unit VIII (Geographic Thought / man–environment traditions); Q16 Unit II (Thunderstorms); Q17 Unit VIII (regional vs. systematic dualism); Q18 Unit III (Warm and Cold Currents).
- Promoted Q11–Q18 from review-only to active. Geography now 116 transcribed records: 16 active and 84 review-only; 500 expected questions from five other papers remain not transcribed. In November 2025, Q1–Q18 are source-visually checked; Q1–Q7, Q9, Q11–Q18 active; Q8 and Q10 remain review-only pending mapping confirmation; Q38–Q100 remain source-visual pending.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q19–Q25 source batch
- Official PDF indexes 7–8 (printed pages 8–9) visually checked. English stems and all four options for Q19–Q25 match canonical transcriptions.
- Official final-key letters D, A, C, C, A, C, B match the canonical records and the registered November 2025 final-key table.
- Official syllabus mappings: Q19 Unit IX (remote sensing sensors); Q20 Unit III (ocean-floor relief); Q21 Unit IX (electromagnetic spectrum); Q22 Unit III (ocean salinity); Q23 Unit IX (GIS); Q24 Unit I (geomorphology/weathering); Q25 Unit IX (thematic maps and mapping organisations).
- Promoted Q19, Q20, Q21, Q22, Q24 and Q25 to active. Q23 is source-verified and mapped but remains review-only: official key A is preserved, although option B (Data acquisition) appears to fit digitization; expert review required. Geography now has 122 active and 78 review-only records; 500 expected questions remain untranscribed. November 2025 Q1–Q25 are visually checked; Q1–Q7, Q9, Q11–Q22 and Q24–Q25 active; Q8/Q10 remain mapping-review only; Q23 remains key-conflict review; Q38–Q100 remain source-visual pending.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q26–Q31 source batch
- Official PDF indexes 9–10 (printed pages 10–11) visually checked. English stems and all four options for Q26–Q31 match canonical transcriptions.
- Official final-key letters A, B, B, A, B, A match the registered official final-key table.
- Verified syllabus mappings: Q27 Unit X (Green Revolution/agriculture); Q28 Unit I (glacial geomorphology); Q29 Unit X (Indian physiographic regions); Q30 Unit I (geomorphic landforms); Q31 Unit X (Indian vegetation).
- Promoted Q27–Q31 to active. Q26 is source-verified and key-matched but remains review-only because the geological-period ordering is not explicitly scoped in the Code 24 syllabus. Geography now has 127 active and 73 review-only records; 500 expected questions remain untranscribed. November 2025 Q1–Q31 are visually checked; Q1–Q7, Q9, Q11–Q22, Q24–Q25 and Q27–Q31 active; Q8/Q10/Q26 mapping-review only; Q23 key-conflict review; Q38–Q100 source-visual pending.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q32–Q37 source batch
- Official PDF indexes 11–12 (printed pages 12–13) visually checked. English stems and all four options for Q32–Q37 match canonical transcriptions.
- Official final-key letters D, B, D, B, A, B match the registered official final-key table.
- Verified mappings: Q33 Unit V (fertility/mortality analysis); Q34 Unit V (rural settlements); Q35 Unit VI (agricultural systems of the world); Q36 Unit VII (social well-being and quality of life); Q37 Unit VI (A. Weber and industrial location theory).
- Promoted Q33–Q37 to active. Q32 is source-verified/key-matched but remains review-only pending a defensible syllabus placement for the coastal lagoon item. Geography now has 132 active and 68 review-only records; 500 expected questions remain untranscribed. November 2025 Q1–Q37 are visually checked; Q1–Q7, Q9, Q11–Q22, Q24–Q25, Q27–Q31 and Q33–Q37 active; Q8/Q10/Q26/Q32 mapping review; Q23 official-key/content conflict; Q38–Q100 visual review pending.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Canonical file and registry reconciliation
- Reconciled subject registry against current canonical JSON files for Codes 06, 07, 08, 24, 26 and 27. Corrected Code 08 and Code 24 loaded/review counts and refreshed their data_status descriptions.
- Sanskrit discrepancy found: questions.json has 130 records; questions_review_pending.json is empty; source_audit.json reports 720 pending and 33 review-required records, but none of the 130 question records has review_flag=true. The 720 records are not present in canonical JSON. Updated source audit and registry to make this a visible recovery blocker; did not fabricate or reconstruct missing question records.
- Current seven-subject totals: 580 active; 800 review-only records actually present in JSON; 720 Sanskrit review-only records reported but missing from JSON; 1,100 not transcribed (Geography 500, Social Work 600). PR #22 remains open/unmerged.


## 2026-11-15 — Geography Code 24 November 2025 Q38–Q45 source batch
- Official PDF indexes 13–14 (printed pages 14–15) visually checked. English stems and all four options for Q38–Q45 match canonical transcriptions.
- Official final-key letters D, C, C, C, D, A, A, C match the registered November 2025 final-key table.
- Verified syllabus mappings: Q38 Unit V (rural settlement patterns); Q39 Unit X (regional planning in India); Q40 Unit IV (Paris Agreement); Q41 Unit VII (Rimland Theory); Q42 Unit IV (water pollution/eutrophication); Q43 Unit VII (quality of life); Q44 Unit IV (environmental hazards); Q45 Unit VII (frontiers).
- Promoted all eight to active. Geography now has 140 active / 60 review-only out of 200 transcribed. November 2025 Q1–Q45 are source-visually checked; 40 are active and five earlier review-only items remain (Q8, Q10, Q23, Q26, Q32); Q46–Q100 remain source-visual pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q46–Q51 source batch
- Official PDF indexes 15–16 (printed pages 16–17) visually checked. English stems and all options for Q46–Q51 match canonical transcriptions.
- Official final-key letters D, D, B, D, B, D match the registered November 2025 final-key table.
- Verified mappings: Q46 Unit IV (IPCC/international climate programmes); Q47 Unit VIII (Arab scholars); Q48 Unit II (atmospheric structure/temperature); Q49 Unit VIII (geographic thought and dualisms); Q50 Unit II (climatology/humidity).
- Promoted Q46–Q50 to active. Q51 is source-verified/key-matched but remains review-only pending an explicit syllabus placement for exploration/discovery. Geography now 145 active / 55 review-only; November 2025 Q1–Q51 visually checked, 45 active and six review-only items (Q8, Q10, Q23, Q26, Q32, Q51); Q52–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q52–Q59 source batch
- Official PDF indexes 17–18 (printed pages 18–19) visually checked. English stems/options and Q54's matching table/options match canonical transcriptions.
- Official final-key letters B, C, C, A, D, C, C, B match the registered November 2025 final-key table.
- Verified mappings: Q52 Unit II (Coriolis/pressure and winds); Q53 Unit IX (basin circularity ratio); Q55 Unit III (ocean circulation); Q56 Unit IX (GIS attribute data); Q57 Unit I (geomorphology/drainage); Q58 Unit IX (digital image processing); Q59 Unit I (slope development/Penck).
- Promoted Q52, Q53 and Q55–Q59 to active. Q54 is source-verified/key-matched but remains review-only because the island-origin classification has no unambiguous single-unit placement. Geography now 152 active / 48 review-only; November 2025 Q1–Q59 visually checked, 52 active and seven review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54); Q60–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q60–Q65 source batch
- Official PDF indexes 19–20 (printed pages 20–21) visually checked. English stems and all four options for Q60–Q65 match canonical transcriptions.
- Official final-key letters B, D, B, A, C, C match the registered November 2025 final-key table.
- Verified mappings: Q60 Unit X (India/Tropic of Cancer); Q61 Unit I (earthquakes); Q63 Unit V (demographic transition); Q64 Unit V (Harris–Ullman urban model); Q65 Unit VI (WTO/world trade).
- Promoted Q60, Q61 and Q63–Q65 to active. Q62 is source-verified/key-matched but remains review-only pending explicit syllabus placement for nuclear power-station location. Geography now 157 active / 43 review-only; November 2025 Q1–Q65 visually checked, 57 active and eight review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62); Q66–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q66–Q73 source batch
- Official PDF indexes 21–22 (printed pages 22–23) visually checked. English stems and all options for Q66–Q73 match canonical transcriptions.
- Official final-key letters D, D, D, D, A, D, D, C match the registered final-key table.
- Verified mappings: Q66 Unit IX (raster GIS data); Q67 Unit V (urban systems/population); Q69 Unit V (tribal distribution); Q70 Unit VI (primary economic activities); Q71 Unit II (climate change/greenhouse gases); Q72 Unit V (tribal population); Q73 Unit IV (ecosystem/trophic levels).
- Promoted Q66–Q67 and Q69–Q73 to active. Q68 is source-verified/key-matched but remains review-only pending explicit syllabus placement for Chandigarh's master plan. Geography now 164 active / 36 review-only; November 2025 Q1–Q73 visually checked, 64 active and nine review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62, Q68); Q74–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q74–Q79 source batch
- Official PDF indexes 23–24 (printed pages 24–25) visually checked. English stems and all options for Q74–Q79 match canonical transcriptions.
- Official final-key letters A, D, C, D, D, A match the registered final-key table.
- Verified mappings: Q74 Unit VII (organic theory of state); Q75 Unit IV (Kyoto Protocol); Q76 Unit V (Toda tribe); Q77 Unit II (Köppen classification); Q78 Unit VIII (nature/scope and geographic traditions); Q79 Unit II (westerlies/pressure and winds).
- Promoted all six to active. Geography now 170 active / 30 review-only; November 2025 Q1–Q79 visually checked, 70 active and nine review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62, Q68); Q80–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q80–Q85 source batch
- Official PDF indexes 25–26 (printed pages 26–27) visually checked. English stems/options and Q81's variable-gas matching table match canonical transcriptions.
- Official final-key letters D, A, A, C, B, B match the registered final-key table.
- Verified mappings: Q80 Unit VIII (scholarly contributions); Q81 Unit II (atmospheric composition); Q82 Unit IX (stream ordering/morphometry); Q83 Unit I (plate tectonics); Q84 Unit IX (PCA/cluster analysis); Q85 Unit III (ocean trenches).
- Promoted all six to active. Geography now 176 active / 24 review-only; November 2025 Q1–Q85 visually checked, 76 active and nine review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62, Q68); Q86–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q86–Q93 source batch
- Official PDF indexes 27–28 (printed pages 28–29) visually checked. English stems/options and Q92's mineral-producer matching table match canonical transcriptions.
- Official final-key letters B, B, C, C, D, C, A, C match the registered final-key table.
- Verified mappings: Q86 Unit IX (remote-sensing platform); Q87 Unit I (graded river/fluvial equilibrium); Q88 Unit IX (regression); Q89 Unit I (dynamic equilibrium); Q90 Unit IX (GPS); Q91 Unit I (weathering); Q92 Unit X (Indian mineral producers); Q93 Unit X (Vindhyan mineral resources).
- Promoted all eight to active. Geography now 184 active / 16 review-only; November 2025 Q1–Q93 visually checked, 84 active and nine review-only items (Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62, Q68); Q94–Q100 remain visual-review pending. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Geography Code 24 November 2025 Q94–Q100 source batch
- Official PDF indexes 29–30 (printed pages 30–31) visually checked. English stems/options and Q100's pass-to-state matching table match canonical transcriptions.
- Official final-key letters B, B, B, D, D, C, D match the registered final-key table.
- Verified mappings: Q94 Unit I (knickpoint/rejuvenation); Q95 Unit X (Gujarat Golden Corridor/industrial regions); Q96 Unit I (recumbent folding); Q97 Unit I (badland topography); Q98 Unit X (transport networks); Q99 Unit I (plate tectonics/vulcanicity); Q100 Unit X (Himalayan passes).
- Promoted all seven to active. Geography now 191 active / 9 review-only out of 200 transcribed; November 2025 Q1–Q100 source-visual review is complete. Nine review-only records remain for non-source gates: Q8, Q10, Q23, Q26, Q32, Q51, Q54, Q62 and Q68. Five other Geography papers (500 questions) remain untranscribed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- Gujarati-side text was not populated. No other subject, Code 01, Code 02, Code 28 or Paper-I changed. PR #22 remains open/unmerged. No CI/APK result is claimed for this PR branch.


## 2026-11-15 — Sanskrit 720-record review queue restored
- Recovered the original Library source `gset_sanskrit_07_consolidated_staging.json` (850 records, 850 unique IDs).
- Compared IDs against canonical active `questions.json`: 130 overlaps; restored the other 720 unique records to `questions_review_pending.json`.
- Restored queue integrity: 720 unique records, 687 `key_applied_pending_proofread`, 33 `review_required`; every record remains `source_verified=false` and `review_flag=true`.
- Preserved two official final-key Z/not-evaluated records (August 2017 Q22 and December 2019 Q94) with `official_answer=null` and `answer=Z`; did not invent option letters.
- Reconciled per-paper `papers.json`, `source_audit.json` and subject registry. Sanskrit is 130 active / 720 review-only, with all 850 unique records accounted for. Five keys-only sessions remain answer-entry metadata, not extra question text.
- Updated seven-subject totals: 639 active, 1,461 review-only present, zero missing from JSON, 1,100 not transcribed; expected total 3,200.


## 2026-11-15 — Sanskrit Code 07 November 2025 Q71–Q76 visual verification
- Official GSET Sanskrit November 2025 Paper-II printed page 12 (PDF zero-based page 11) visually checked against canonical transcription for Q71–Q76. All six stems and four-option sets match the scan.
- Official final-key letters B, B, C, C, D, A match the registered official final-key table. Q71–Q76 promoted from review-only to active; syllabus mapping remains pending.
- Sanskrit now 136 active / 714 review-only. November 2025 source visual verification is 37/100; Q70 and Q85–Q100 remain source-visual pending (other flagged/remaining ranges are recorded in source_audit.json). Seven-subject totals: 645 active, 1,455 review-only, zero missing, 1,100 not transcribed.


## 2026-11-15 — Sanskrit Code 07 November 2025 Q85–Q90 visual verification
- Official GSET Sanskrit November 2025 Paper-II printed page 14 (PDF zero-based page 13) visually checked against Q85–Q90.
- Official final-key letters C, A, C, A, B, C match the registered key table. Q86, Q87, Q89 and Q90 promoted active.
- Q85 remains review-only: source appears to read “चरितं” while canonical text reads “चरति”. Q88 remains review-only: source begins “वेदत्रयीपदार्थ...” while canonical text reads “वेदप्रतिदित...”. Both are source-verified/key-matched but require transcription correction confirmation.
- Sanskrit now 140 active / 710 review-only; November 2025 visual verification 43/100 (41 active; Q85/Q88 source-verified but review-only; 57 still awaiting source-page review). Seven-subject totals: 649 active, 1,451 review-only, zero missing, 1,100 not transcribed.


## 2026-11-15 — Sanskrit Code 07 November 2025 Q91–Q100 visual verification
- Official GSET Sanskrit November 2025 Paper-II printed page 14 (Q91–Q92) and printed page 15 (Q93–Q100) visually checked against the canonical queue.
- Official final-key letters C, D, D, A, C, A, D, B, B, A match the registered key table. Q92, Q95, Q96, Q98, Q99 and Q100 promoted active.
- Q91, Q93, Q94 and Q97 remain source-verified/key-matched but review-only because their current Devanagari transcription differs from the printed source; exact wording is documented in source_audit.json.
- Sanskrit now 146 active / 704 review-only; November 2025 visual verification 53/100 (47 active, six source-verified transcription-review items, 47 not yet visually checked). Seven-subject totals: 655 active, 1,445 review-only, zero missing, 1,100 not transcribed.


## 2026-11-15 — Sanskrit Code 07 official syllabus registration and mapping batch
- Retrieved and visually inspected the official GSET Code 07 syllabus PDF (7 pages); registered its ten official units in `assets/subjects/syllabus_units.json`.
- Mapped 18 November 2025 Sanskrit questions to explicit syllabus topics/texts: Q72 Unit VIII, Q74 Unit I, Q75 Unit VIII, Q76 Unit IX, Q78 Unit IX, Q80 Unit II, Q86 Unit III, Q88 Unit I, Q89 Unit IX, Q90 Unit X, Q91 Unit II, Q92 Unit VIII, Q93 Unit II, Q96 Unit IV, Q97 Unit VII, Q98 Unit VIII, Q99 Unit I and Q100 Unit VII.
- Q88, Q91, Q93 and Q97 remain review-only for source transcription discrepancies even though their topic-level syllabus units are now identified. 832 of 850 Sanskrit records remain unmapped; no speculative mapping was forced.
- Sanskrit counts unchanged: 146 active / 704 review-only. Seven-subject totals remain 655 active, 1,445 review-only, zero missing, 1,100 not transcribed.


## 2026-11-15 — Forensic Science Code 27 official syllabus mapping review
- Reviewed December 2024 Q50: “The study of insects in a forensic context to estimate the post-mortem interval is known as”. The official GSET Code 27 syllabus PDF, page 5, Unit X, explicitly includes “Forensic Entomology” and insects of forensic importance.
- Verified Q50's existing Unit 10 mapping. Stored answer B and official answer B were left unchanged. Changed only `syllabus_mapping_status` from provisional to `official_syllabus_content_reviewed`, with the official syllabus page/source recorded.
- Updated mapping audit: 1 verified, 298 provisional, 1 pending (November 2025 Q47 forensic-engineering scope). Q50 remains `source_verified=false` and `review_flag=true` because independent source-page visual verification is still pending; it remains review-only and is not activated.
- Official source: https://gujaratset.ac.in/assets/syllabus/27.pdf (page 5, Unit X). No other subject, Code 01, Code 02, Paper-I, or app UI changed. PR #22 remains open/unmerged; no CI/APK pass claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Unit X mapping batch
- Verified Q48 (forensic autopsy) and Q49 (rigor mortis) against the official Code 27 syllabus, page 5, Unit X: post-mortem examination and post-mortem changes are explicitly listed. Q50 (forensic entomology) was verified in the preceding batch against the same Unit X.
- Changed only the syllabus mapping status/evidence fields for Q48 and Q49; answers and all source-review/activation fields were preserved. Q48, Q49 and Q50 remain review-only because independent second-pass source-page visual verification is pending.
- Updated aggregate mapping count to 3 verified, 296 provisional, 1 pending; Unit X distribution now 47. The unresolved forensic-engineering Q47 remains pending because no direct official unit placement is supported.
- Official source: https://gujaratset.ac.in/assets/syllabus/27.pdf, page 5. No other subject, Code 01, Code 02, Paper-I or app UI changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q43–Q50 verified and activated
- Visually checked official GSET PDF printed page 7 (Q43–Q45), page 8 (Q46–Q49), and page 9 (Q50); independently matched final answer key: Q43 A, Q44 A, Q45 C, Q46 B, Q47 A, Q48 C, Q49 D, Q50 B.
- Official syllabus mapping checked against Code 27 syllabus PDF page 5: Q43–Q45 -> Unit IX (forensic documents/handwriting); Q46–Q50 -> Unit X (forensic medicine, post-mortem examination and entomology). Eight records are active/source_verified with review_flag=false.
- Forensic Science Code 27 live canonical count: 92 active, 208 review-only; December 2024 has 8 source-verified/loaded questions. Mapping total: 8 verified, 291 provisional, 1 pending (November 2025 Q47 forensic-engineering scope). Subject-level source_verified remains false because the other records/sessions are not fully verified.
- Sanskrit Code 07: live review queue remains empty; 704 distinct staged records still missing from canonical review JSON. Do not claim recovered.
- Seven-subject totals: 663 active, 733 review-only present, 704 missing from canonical JSON (Sanskrit), 1,100 not transcribed (Geography 500; Social Work 600) = 3,200 expected.
- No other subject, Code 01, Code 02, Code 28, Paper-I, or app UI changed. PR #22 remains open/unmerged; no CI/APK pass claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q35–Q50 verified
- Official GSET PDF printed page 7: Q35–Q42 visually checked; page 8: Q43–Q49; page 9: Q50. Official final-key answers matched: Q35 B, Q36 A, Q37 A, Q38 A, Q39 C, Q40 A, Q41 D, Q42 A, Q43 A, Q44 A, Q45 C, Q46 B, Q47 A, Q48 C, Q49 D, Q50 B.
- Source review now complete for December 2024 Q35–Q50 (16 questions); all 16 activated with source_verified=true and review_flag=false. Official syllabus content mapping verified for Q35–Q39 (Unit VIII), Q42–Q45 (Unit IX), Q46–Q50 (Unit X). Q40 and Q41 retain provisional mappings; they were source-verified, not mapped as verified.
- Forensic Science Code 27 live bank: 100 active, 200 review-only; all 100 December 2024 questions are now loaded, of which 16 have been visually verified. Subject remains source_verified=false because the other two sessions are not fully verified. Mapping totals: 14 verified, 285 provisional, 1 pending (November 2025 Q47 forensic-engineering scope).
- Sanskrit Code 07 queue is still empty; 704 distinct records from the 850-record Library staging source remain missing from canonical review JSON.
- Seven-subject totals: 671 active, 725 review-only present, 704 missing from canonical JSON (Sanskrit), 1,100 not transcribed (Geography 500; Social Work 600) = 3,200 expected.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI/APK pass claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q35–Q50 verified
- Official GSET PDF printed page 7: Q35–Q42 visually checked; page 8: Q43–Q49; page 9: Q50. Official final-key answers matched: Q35 B, Q36 A, Q37 A, Q38 A, Q39 C, Q40 A, Q41 D, Q42 A, Q43 A, Q44 A, Q45 C, Q46 B, Q47 A, Q48 C, Q49 D, Q50 B.
- Source review complete for December 2024 Q35–Q50 (16 questions); all 16 activated with source_verified=true and review_flag=false. Official syllabus mapping verified for Q35–Q39 (Unit VIII), Q42–Q45 (Unit IX), Q46–Q50 (Unit X). Q40 and Q41 remain provisional mappings.
- Forensic Science Code 27 live bank: 100 active, 200 review-only; December 2024 has 16 source-verified questions. Mapping totals: 14 verified, 285 provisional, 1 pending (November 2025 Q47 forensic-engineering scope).
- Sanskrit Code 07 queue remains empty; 704 distinct staged records are missing from canonical review JSON.
- Seven-subject totals: 671 active, 725 review-only present, 704 missing from canonical JSON, 1,100 not transcribed = 3,200 expected.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI/APK pass claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q51–Q57 source batch
- Before: Forensic Science 100 active / 200 review-only; December 2024 Q35–Q50 source-verified (16/100). Seven-subject totals: 671 active, 725 review-only present, 704 Sanskrit records missing from canonical JSON, 1,100 not transcribed.
- Official question paper: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf. Printed page 9 (PDF page index 8) visually checked for Q51–Q57. All seven stems and all four options match the canonical transcription; no figure or table occurs in this range.
- Official final answer key: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf. Q51–Q57 letters D, A, D, D, A, A, C match all seven stored answers. No answer values changed.
- Official Code 27 syllabus: https://gujaratset.ac.in/assets/syllabus/27.pdf, page 5. Verified mappings: Q51 Unit X; Q52 Unit V; Q53 Unit X; Q54 Unit I; Q55 Unit III; Q56 Unit X; Q57 Unit X.
- After: Forensic Science 107 active / 193 review-only; December 2024 Q35–Q57 source-verified (23/100), 77 remain review-only in that session. Mapping totals: 21 verified, 278 provisional, 1 pending. Seven-subject totals: 678 active, 718 review-only present, 704 Sanskrit records missing from canonical JSON, 1,100 not transcribed = 3,200 expected.
- Next batch: Forensic Science Code 27 December 2024 Q58–Q64 (printed page 10), subject to the same official-source/key/syllabus checks. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q58–Q64 source verification
- Official GSET question-paper printed page 10 (PDF page index 9) visually checked. All seven stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters A, A, C, D, D, D, C match Q58–Q64 exactly. No answer values changed.
- Official Code 27 syllabus checked: Q58 Unit X (human dentition/individual identification); Q60 Unit X (post-mortem and individual identification); Q61 Unit IV (toxicology); Q62 Unit VIII (fingerprints); Q63 Unit IX (questioned documents); Q64 Unit III (blood/body fluids/serology). Q59 source/key verified but retained review-only because the rape-kit topic overlaps sexual-offence evidence and medicolegal treatment in Units I and X.
- Forensic Science Code 27: 107 -> 113 active; 193 -> 187 review-only. December 2024 source-verified/activated count 23 -> 29; 71 remain review-only in that session. Mapping totals: 21 -> 27 verified, 278 -> 272 provisional, 1 pending.
- Seven-subject totals: 678 -> 684 active; 718 -> 712 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q65–Q71.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q65–Q71 source verification
- Official GSET question-paper printed page 11 (PDF page index 10) visually checked. All seven stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters A, C, C, D, C, A, A match Q65–Q71 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q65 Unit X (gunshot wounds); Q66–Q70 Unit IV (forensic toxicology); Q71 Unit V (ballistics/trajectory). All seven records moved from review-only to active.
- Forensic Science Code 27: 113 -> 120 active; 187 -> 180 review-only. December 2024 source-verified/activated count 29 -> 36; 64 remain review-only in that session. Mapping totals: 27 -> 34 verified, 272 provisional, 1 pending.
- Seven-subject totals: 684 -> 691 active; 712 -> 705 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q72–Q78.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q72–Q76 source verification
- Official GSET question-paper printed page 12 (PDF page index 11) visually checked. All five stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters B, C, A, D, C match Q72–Q76 exactly. No answer values changed.
- Official Code 27 syllabus page 3, Unit V, explicitly covers firearms, ammunition, ballistics and propellant concepts. All five records moved from review-only to active with Unit V mapping.
- Forensic Science Code 27: 120 -> 125 active; 180 -> 175 review-only. December 2024 source-verified/activated count 36 -> 41; 59 remain review-only in that session. Mapping totals: 34 -> 39 verified, 272 provisional, 1 pending.
- Seven-subject totals: 691 -> 696 active; 705 -> 700 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q77–Q83.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q77–Q85 source verification
- Official GSET question-paper printed page 13 (PDF page index 12) visually checked. All nine stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters B, A, C, A, B, B, A, A, D match Q77–Q85 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q77–Q78 Unit V (ballistics/firearms); Q79 Unit I (forensic laboratory organization); Q80 Unit X (human dentition); Q81–Q85 Unit VII (hair/fibres/pollens/diatoms). All nine records moved from review-only to active.
- Forensic Science Code 27: 125 -> 134 active; 175 -> 166 review-only. December 2024 source-verified/activated count 41 -> 50; 50 remain review-only in that session. Mapping totals: 39 -> 48 verified, 272 provisional, 1 pending.
- Seven-subject totals: 696 -> 705 active; 700 -> 691 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q86–Q92.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q86–Q92 source verification
- Official GSET question-paper printed page 14 (PDF page index 13) visually checked. All seven stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters B, D, C, C, B, A, D match Q86–Q92 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q86 Unit III (wildlife forensics); Q87–Q88 and Q90–Q92 Unit V (firearms/ballistics); Q89 Unit II (comparison microscopy). All seven records moved from review-only to active.
- Forensic Science Code 27: 134 -> 141 active; 166 -> 159 review-only. December 2024 source-verified/activated count 50 -> 57; 43 remain review-only in that session. Mapping totals: 48 -> 55 verified, 272 provisional, 1 pending.
- Seven-subject totals: 714 -> 721 active; 682 -> 675 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: November 2023 review or December 2024 Q93–Q100.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q93–Q100 source verification
- Official GSET question-paper printed page 15 (PDF page index 14) visually checked. All eight stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters D, B, B, B, B, D, B, B match Q93–Q100 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q93 Unit V (ballistics/air resistance); Q94–Q97 Unit VII (computer forensics/digital evidence); Q98–Q100 Unit IX (paper, fibres and questioned documents). All eight records moved from review-only to active.
- Forensic Science Code 27: 141 -> 149 active; 159 -> 151 review-only. December 2024 source-verified/activated count 57 -> 65; 35 remain review-only in that session. All Q35–Q100 are now source-page visually checked; Q59 remains review-only for syllabus-unit ambiguity. Mapping totals: 55 -> 63 verified, 272 provisional, 1 pending.
- Seven-subject totals: 721 -> 729 active; 675 -> 667 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next work: review December 2024 Q1–Q34 and continue the other two Forensic Science sessions.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q1–Q8 source verification
- Official GSET question-paper printed page 3 (PDF page index 2) visually checked. All eight stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters B, B, A, A, A, B, B, A match Q1–Q8 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q1–Q2 Unit V (firearms/ballistics); Q3 and Q5–Q8 Unit II (microscopy/instrumental methods); Q4 Unit I (brain fingerprinting/brain mapping). All eight records moved from review-only to active.
- Printed source wording “Ocular lance” (Q6) and “Abbey Condensers” (Q5) was retained exactly; no silent editorial correction.
- Forensic Science Code 27: 149 -> 157 active; 151 -> 143 review-only. December 2024 source-verified/activated count 65 -> 73; 27 remain review-only in that session (Q9–Q34 and Q59). Mapping totals: 63 -> 71 verified, 272 provisional, 1 pending.
- Seven-subject totals: 729 -> 737 active; 667 -> 659 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q9–Q16.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q9–Q16 source verification
- Official GSET question-paper printed page 4 (PDF page index 3) visually checked. All eight stems and all four options match the canonical transcription; no figure/table occurs in this range.
- Official final-key letters A, C, B, B, B, A, B, C match Q9–Q16 exactly. No answer values changed.
- Official Code 27 syllabus page 5 mappings verified: Q9 Unit VIII (fingerprint methods); Q10–Q11 Unit V (primer charge and rifled firearms); Q12 Unit I (lie detection/polygraphy); Q13–Q16 Unit III (DNA structure, profiling and extraction). Q16 was corrected from the earlier provisional Unit IV to Unit III based on the explicit DNA extraction coverage in Unit III.
- All eight records moved from review-only to active. Forensic Science Code 27: 157 -> 165 active; 143 -> 135 review-only. December 2024 source-verified count 74 -> 82; Q17–Q34 remain pending source review (18 questions), while Q59 remains review-only for syllabus ambiguity. Mapping totals: 71 -> 79 verified, 272 provisional, 1 pending.
- Seven-subject totals: 737 -> 745 active; 659 -> 651 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q17–Q24.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q17–Q24 source verification
- Official GSET question-paper printed pages 4–5 (PDF page indexes 3–4) visually checked. All eight stems and all four options match canonical transcription; no figures/tables in this range.
- Official final-key letters B, A, A, A, B, C, D, D match Q17–Q24 exactly. No answer values changed.
- Q17–Q19 and Q23–Q24 moved to active with explicit Unit III DNA/profiling mapping. Q20 (bacterial RNA polymerase sigma factor), Q21 (lac operon) and Q22 (purine metabolism) are source/key verified but remain review-only: these exact topics are not explicitly listed in the official Code 27 syllabus, so no forced mapping was applied.
- Forensic Science Code 27: 165 -> 170 active; 135 -> 130 review-only. December 2024 source-verified count 82 -> 90; Q20–Q22 and Q59 are source/key checked but retained review-only; Q25–Q34 (10 questions) remain source-review pending. Mapping totals: 79 -> 84 verified, 275 provisional, 1 pending.
- Seven-subject totals: 745 -> 750 active; 651 -> 646 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next Forensic Science batch: December 2024 Q25–Q34.


## 2026-11-15 — Forensic Science Code 27 December 2024 Q25–Q34 source verification
- Official GSET question-paper printed pages 5–6 (PDF page indexes 4–5) visually checked. All ten stems and all four options match canonical transcription; no figures/tables in this range.
- Official final-key letters D, B, A, B, D, D, A, D, A, D match Q25–Q34 exactly. No answer values changed.
- Q27–Q32 activated with official Unit III DNA/genetic-marker/profiling mapping; Q34 activated with Unit VIII fingerprint-development mapping (vacuum metal deposition). Q25 (epistasis), Q26 (protein tertiary structure) and Q33 (DMORT) source/key verified but remain review-only because exact topics are not explicitly listed in the official syllabus.
- Forensic Science Code 27: 170 -> 177 active; 130 -> 123 review-only. December 2024: all 100 questions now source-page checked; 93 active and seven retained review-only for syllabus resolution (Q20–Q22, Q25–Q26, Q33, Q59). Mapping totals: 84 -> 91 verified, 278 provisional, 1 pending.
- Seven-subject totals: 750 -> 757 active; 646 -> 639 review-only present; 704 Sanskrit records remain missing from canonical review JSON; 1,100 questions remain untranscribed (Geography 500; Social Work 600). Expected total 3,200.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2427.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.
- No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed. Next work: resolve seven December 2024 syllabus holds and visually review November 2023 / November 2025 sessions.


## 2026-11-15 — Forensic Science Code 27 November 2023 Q82–Q100 source verification
- Official GSET November 2023 question paper printed pages 13–15 (PDF page indexes 12–14) visually checked. All 19 stems and all four options match the canonical transcription; no figures/tables in this range.
- Official November 2023 final-key letters Q82–Q100: B, D, D, B, A, A, C, B, B, B, C, D, C, B, C, B, A, A, A; all 19 match stored answers. No answer values changed.
- Official Code 27 syllabus checked: Q82 Unit II; Q83 Unit V; Q84 Unit VII; Q85 Unit VIII; Q86–Q88 Unit VII; Q89–Q90 Unit X; Q91 Unit VII; Q92 Unit I; Q93 Unit VI; Q94 Unit III; Q95 Unit VII; Q96 Unit V; Q97 Unit IV; Q98 Unit III; Q99 Unit VI; Q100 Unit IV. All 19 moved from review-only to active.
- November 2023 now 100/100 source-page verified and final-key matched; 100 active, zero pending. Forensic Science total: 196 active / 104 review-only. Remaining review-only: December 2024 Q20–Q22, Q25–Q26, Q33, Q59 (7); November 2025 Q4–Q100 except the three already active (97).
- Question-level syllabus mapping: 110 reviewed, 189 provisional, 1 pending. PR #22 remains open/unmerged. No CI or Combined APK pass claimed. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed.


## 2026-11-15 — Forensic Science Code 27 November 2025 Q4–Q7 and Q9–Q10 source verification
- Official GSET November 2025 question paper printed page 3 (PDF page index 2) visually checked. All six stems and all four options match canonical transcription. Q8 was already active and visually checked in an earlier batch.
- Official November 2025 final-key letters Q4 A, Q5 B, Q6 A, Q7 B, Q9 C, Q10 C match all six stored answers. No answer values changed.
- Official Code 27 syllabus mappings: Q4 Unit IV (chemical examination of tissues/viscera); Q5 Unit VI (fire/arson and accelerants); Q6–Q7 Unit IV (pesticides and metallic poisons); Q9–Q10 Unit IV (trap-case chemicals and drugs of abuse). All six moved to active.
- November 2025 now 9 active / 91 awaiting source review. Forensic Science total: 202 active / 98 review-only. December 2024 holds remain seven (Q20–Q22, Q25–Q26, Q33, Q59); November 2025 remaining review queue 91.
- Question-level syllabus mapping: 116 reviewed, 183 provisional, 1 pending. PR #22 remains open/unmerged. No CI or Combined APK pass claimed. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed.


## 2026-11-15 — Geography Code 24 November 2025 Q32 official syllabus mapping closure
- Rechecked the already source-verified Q32 record against official GSET Code 24 syllabus PDF. The question identifies Pulicat Lake as a lagoon enclosed by a spit; official Unit I is Geomorphology and explicitly includes landform occurrence. This is a direct geomorphic landform match, so Q32 is mapped to Unit I.
- Official question-paper printed page 12 and official November 2025 final answer key independently confirm the stem/options and answer D. No answer or source wording changed.
- Promoted Q32 from review-only to active. Geography now 192 active / 8 review-only across 200 transcribed questions; November 2025 has 92 active / 8 review-only, 100/100 source visual checks, 100/100 final-key parity, and 93 verified / 7 provisional syllabus mappings. The eight review-only records are Q8, Q10, Q23, Q26, Q51, Q54, Q62 and Q68.
- Updated canonical questions, review queue, source audits, paper manifest and subject registry. Five additional Geography papers (500 questions) and Social Work (600 questions) remain untranscribed. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf.


## 2026-11-15 — Geography Code 24 November 2025 Q54 official syllabus mapping closure
- Rechecked the source-verified Q54 island-origin matching item against official GSET Code 24 syllabus. It tests geomorphic origin/classification (offshore, coral and volcanic islands), which falls directly under Unit I Geomorphology and landform occurrence.
- Official question-paper printed page 18 and final answer key confirm the matching set and answer C. No stem, option or answer was changed.
- Promoted Q54 from review-only to active. Geography now 193 active / 7 review-only across 200 transcribed questions; November 2025 has 93 active / 7 review-only, 100/100 source visual checks, 100/100 final-key parity, and 94 verified / 6 provisional syllabus mappings. Remaining review-only: Q8, Q10, Q23, Q26, Q51, Q62 and Q68.
- Updated canonical questions, review queue, source audits, paper manifest and subject registry. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf.


## 2026-11-15 — Forensic Science Code 27 November 2025 Q11–Q21 source and syllabus verification
- Official GSET November 2025 Forensic Science Paper-II printed page 4 (PDF page index 3) visually checked. All 11 question stems and four-option sets match the canonical transcriptions.
- Official final-key letters Q11–Q21: A, D, C, B, C, C, B, B, A, A, C. All 11 match the stored official answers; no answer values changed.
- Official Code 27 syllabus mappings: Q11 Unit II (immunoassays/ELISA); Q12–Q14 Unit IV (ethyl alcohol and toxicology); Q15 Unit I (criminal investigation/corpus delicti); Q16–Q17 Unit IV (poison/pesticide toxicity); Q18 Unit X (human dentition and age estimation); Q19–Q20 Unit IV (metallic poison and ethyl alcohol analysis); Q21 Unit III (DNA/Y-STR profiling). All 11 promoted to active.
- Forensic Science now 213 active / 87 review-only. November 2025: 20/100 source-page verified, 20/100 final-key matched, 80 remain source-review pending. Overall subject mapping audit: 127 verified, 172 provisional, 1 pending.
- Updated canonical questions, review queue, source audit, paper manifest and subject registry. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2527.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2527.pdf ; https://gujaratset.ac.in/assets/syllabus/27.pdf.


## 2026-11-15 — Forensic Science Code 27 mapping-audit reconciliation
- Recomputed the verified unit distribution from canonical active `questions.json` records whose `syllabus_mapping_status` is `official_syllabus_content_reviewed`; verified count remains 127.
- Reconciled aggregate mapping totals across active and review-only banks (300 records): 127 verified, 172 provisional, 1 pending. The pending record is November 2025 Q47; no mapping was forced.
- Reconciled session totals across both banks: November 2023 100, December 2024 100, November 2025 100.
- Updated `source_audit.json` and the Code 27 entry in `assets/subjects/subjects.json`. Question content, answers, review flags, and activation status were not changed.
- PR #22 remains open/unmerged. No CI or Combined APK pass is claimed.


## 2026-11-15 — Geography Code 24 November 2025 Q51 and Q68 syllabus mapping
- Reviewed the official Code 24 syllabus: Q51's exploration/discovery and cartography content maps to Unit VIII (Geographic Thought, scholars and cartographic contributions); Q68's Chandigarh master-plan question maps to Unit V (Population and Settlement Geography, urban planning/settlement).
- Both questions had already been visually checked against the official November 2025 paper and matched the official final answer key. Only syllabus mapping and review status were updated; stems, options and official answer letters were preserved.
- Geography now 195 active / 5 review-only across 200 transcribed questions. Remaining November 2025 review-only: Q8, Q10, Q23, Q26 and Q62. Q23 remains held due official-key/content concern.
- Five additional Geography papers (500 questions) remain untranscribed. No other subject, Code 01, Code 02, Code 28 or Paper-I changed; PR #22 remains open/unmerged; no CI/APK pass claimed.


## 2026-11-15 — Geography Code 24 Q8, Q10 and Q62 mapping decisions
- Q8 mapped to Unit IV (Geography of Environment): the official syllabus explicitly lists environmental policy, international treaties, international programmes and policies; this question tests international environmental observance days.
- Q10 mapped to Unit III (Oceanography): sea-to-land offshore/shore/backshore zonation under relief of oceans.
- Q62 mapped to Unit X (Geography of India): Indian nuclear power station location under India’s natural-resource/industrial geography.
- All three were already visually checked against the official paper and official final-key matched; question wording, options and answer letters were preserved.
- November 2025 Geography now 98 active / 2 review-only. Q23 remains held for an apparent official-key/content conflict; Q26 remains held because the geological-period chronology is not explicit in the Code 24 syllabus. Five other Geography papers (500 questions) remain untranscribed.
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/24.pdf. No other subject changed; PR #22 remains unmerged.


## 2026-11-15 — Forensic Science Code 27 November 2025 Q22–Q45 visual source verification
- Visually compared Q22–Q45 and all four options with official PDF printed pages 4–7 (PDF zero-based pages 3–6). Stored stems, option order and official answer letters were retained; no corrections were needed.
- Q35 option A remains as printed in the scan: “Pentathol sodium”.
- November 2025 source-verified coverage increased from 20 to 44/100; Q46–Q100 remain pending (55 questions). Across all sessions, the 87 review-only records remain review-only where syllabus mapping is provisional; source verification does not automatically activate them.
- Official source: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2527.pdf. PR #22 remains open/unmerged.


## 2026-11-15 — Environmental Sciences Code 26 official syllabus mapping
- Re-read the official ten-unit Code 26 syllabus: https://gujaratset.ac.in/assets/syllabus/26.pdf.
- Assigned question-level units to all 300 canonical records (87 active + 213 review-only): 300 verified mappings, 0 provisional, 0 pending. Unit distribution: {"Unit I":22,"Unit X":28,"Unit IV":32,"Unit VI":38,"Unit II":42,"Unit III":28,"Unit V":35,"Unit VII":23,"Unit VIII":25,"Unit IX":27}.
- Mapped both active and review-only records. Review-only flags and source-verification fields were preserved; mapping completion does NOT mark the 213 source pages visually checked or activate them.
- November 2023 / December 2024 / November 2025 papers remain source-review pending as per paper metadata; no answer or question text changed.


## 2026-11-15 — Forensic Science Code 27 source and syllabus review closure
- Official Code 27 syllabus reviewed: https://gujaratset.ac.in/assets/syllabus/27.pdf. All 300 question stems/options are source-verified (November 2023 100/100, December 2024 100/100, November 2025 100/100); official final-key parity is 300/300.
- Reviewed the 87 review-only records against the ten official units. Promoted 78 records with direct syllabus matches to the active bank; retained 9 review-only records where the syllabus does not directly name the topic or a unique unit cannot be justified. No source text, options or official answers changed.
- Current bank: 291 active / 9 review-only. Mapping totals: 205 verified, 94 provisional, 1 pending. Verified unit distribution: {"Unit 2":8,"Unit 5":21,"Unit 7":15,"Unit 8":9,"Unit 10":16,"Unit 1":6,"Unit 6":3,"Unit 3":21,"Unit 4":20,"Unit 9":8,"Unit NaN":78}.
- PR #22 remains open/unmerged; no CI or Combined APK pass claimed.


## 2026-11-15 — Latest verified completion updates
- Geography Code 24: 198 active / 2 review-only. Remaining Q23 (official-key/content conflict) and Q26 (geological chronology not explicitly stated in syllabus); November 2025 Q1–Q100 source and final-key checks 100/100.
- Environmental Sciences Code 26: all 300 records (87 active + 213 review-only) mapped to official ten-unit syllabus; 213 review-only source flags intentionally remain because page-level proofreading has not been completed.
- Forensic Science Code 27: all 300 questions visually source-verified and 300/300 official final-key reconciled. After reviewing the 87 review-only records against the official syllabus, 78 directly mapped records promoted; current 291 active / 9 review-only. Mapping totals 205 verified, 94 provisional, 1 pending. Nine held records: December 2024 Q20, Q21, Q22, Q25, Q26, Q33, Q59; November 2025 Q47, Q59.
- Repository totals for seven subjects now 869 active + 527 review-only + 704 Sanskrit staging records not in canonical queue + 1,100 untranscribed (Geography 500; Social Work 600) = 3,200 expected.
- No PR merge. CI/Combined APK remains unverified.
