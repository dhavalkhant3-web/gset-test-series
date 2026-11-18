# GSET Paper-II — Seven-subject checkpoint (2026-11-17, refreshed)

Repository: https://github.com/dhavalkhant3-web/gset-test-series
Branch: `app/import-updated-subject-banks-2026-11-10`
Pull request: https://github.com/dhavalkhant3-web/gset-test-series/pull/22
Status: Open; NOT MERGED. Do not modify unrelated subjects, Paper-I UI, Mathematical Sciences Code 01, or Code 28.

## Historical counts snapshot — 2026-11-16 (superseded by dated per-file audits below)

| Code | Subject | Active | Review-only present in JSON | Staged / not integrated | Not yet transcribed |
|---|---|---:|---:|---:|---:|
| 06 | Gujarati | 356 | 44 | 0 | 0 |
| 07 | Sanskrit | 192 | 108 | 550 | 0 |
| 08 | History | 50 | 0 | 0 | 0 |
| 24 | Geography | 198 | 2 | 0 | 500 |
| 25 | Social Work | 0 | 0 | 0 | 600 |
| 26 | Environmental Sciences | 300 | 0 | 0 | 0 |
| 27 | Forensic Science | 292 | 8 | 0 | 0 |
| **Total** | | **1,388** | **162** | **550** | **1,100** |

Expected question records across these seven subjects: 3,200. Canonical JSON now contains 1,214 active + 336 review-only = 1,550 records. A further 550 Sanskrit staging questions are not yet integrated, while 500 Geography and 600 Social Work questions remain untranscribed. These categories sum to 3,200. Review-only records are not counted as active app questions. Sanskrit's review queue contains 108 records; its 550 staging records remain outside both canonical JSON files.

**Latest live audit notes:** Gujarati 296 active / 104 review-only after promoting 94 records that already passed source, official-final-key, and official-syllabus checks; the remaining review queue has 56 source-unverified and 33 final-key-unverified records. History 50 active; Q46 and Q48 remain syllabus-mapping holds. Geography 198 active / 2 review-only; five other papers (500 questions) remain untranscribed. Social Work has 600 key-only staged entries and no question text. Environmental Sciences now has 187 active / 113 review-only after verified December 2024 Q1–Q7, Q9–Q19, Q21–Q27, Q34–Q79 and Q80–Q88 source batches. Forensic Science has 291 active / 9 review-only; all 300 answer-key entries are recorded, and its November 2025 source questions Q47 and Q59 remain review-only for syllabus placement.



**Count integrity note (17 November 2026):** The table above is retained as a historical snapshot. Current canonical files and several older checkpoint/manifest counters disagree (notably Sanskrit staging, Geography review records, and earlier Social Work counts). Do not use the old aggregate row as a live total; use the dated per-file updates below until a full seven-subject reconciliation is completed.

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
- Sanskrit: live canonical JSON contains 153 active / 4 review-only present; 693 distinct staged records remain outside the canonical JSON and are not counted as present.
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


## 2026-11-15 — Gujarati Code 06 December 2019 active-bank promotion
- Promoted 99 December 2019 questions to active after confirming each has source_verified=true, answer_key_verified=true, verified Code 06 syllabus mapping, review_flag=false, and an answer matching the official FINAL key.
- December 2019 Q7 remains review-only because the official final key prints Z and the official note excludes it from evaluation.
- Gujarati bank is now 196 active / 204 review-only. This is a queue cleanup only; no question wording, options or answer letters were changed. The remaining 204 include 44 December 2002 and 50 December 2003 records whose available published keys are not explicitly labelled FINAL, plus source-review backlog in August 2017, December 2008 and December 2021.


## 2026-11-15 — Reconciled seven-subject totals after Gujarati promotion
- Gujarati Code 06: 99 December 2019 questions with completed source, official FINAL-key and syllabus checks moved from review queue to active. Q7 remains excluded as official Z/not evaluated. Gujarati now 196 active / 204 review-only.
- Seven-subject canonical totals now 968 active + 428 review-only + 704 Sanskrit staging records absent from canonical JSON + 1,100 not yet transcribed (Geography 500; Social Work 600) = 3,200 expected.
- Other current closures remain: Geography 198/2; Environmental Sciences all 300 mapped to official syllabus but 213 review-only source flags retained; Forensic Science 291/9 with 300/300 source verification and final-key reconciliation.


## 2026-11-15 — Sanskrit Code 07 staging recovery
- Restored 704 distinct records from the consolidated Library staging source into `questions_review_pending.json` using the canonical app schema. The 146 records already in the active bank were matched by ID and not duplicated.
- All 704 recovered records are explicitly review-only: `source_verified=false`, `review_flag=true`, and syllabus mapping pending. No recovered question was promoted to active.
- Answer-key verification is marked true only where the staging provenance explicitly identifies a final answer key and the letter is A–D; older published “KEY FOR PAPER-II” sources not labelled FINAL remain unverified.
- Sanskrit canonical totals now 146 active + 704 review-only = 850 records. Five keys-only sessions are still separate and were not invented/transcribed.


## 2026-11-15 — Sanskrit Code 07 staging recovery
- Restored 704 distinct records from consolidated staging into canonical `questions_review_pending.json`; the 146 records already active were matched by ID and not duplicated.
- All 704 recovered records remain review-only: `source_verified=false`, `review_flag=true`, and official syllabus mapping pending. No recovered question was promoted to active.
- Answer-key verification marked true only where staging provenance explicitly identifies a final answer key and the answer is A–D; older published keys not labelled FINAL remain unverified.
- Sanskrit totals: 146 active + 704 review-only = 850. Five key-only sessions remain separate and were not invented/transcribed.


## 2026-11-15 — Canonical Sanskrit queue validation
- Verified the Git blob for `questions_review_pending.json`: 704 records, 1,392,220 characters, valid JSON; 0 duplicate IDs and 0 overlaps with the 146 active records.
- All 704 records have exactly four options, `source_verified=false`, `review_flag=true`, and `syllabus_mapping_status=pending_official_syllabus_mapping`. 502 carry answer letters from staging sources explicitly labelled final; 202 remain unverified because their source key is not explicitly final or the answer is not an A–D letter.
- Seven-subject totals: 968 active + 1,132 review-only + 1,100 untranscribed = 3,200.


## 2026-11-15 — Final cross-subject checkpoint
- Geography Code 24: 198 active / 2 review-only. Q26 has a provisional Unit I (Geomorphology) fit pending expert confirmation; Q23 remains held because the official final-key letter conflicts with the apparent content answer. November 2025 source and final-key checks are 100/100.
- Sanskrit Code 07: 146 active / 704 review-only; 850 records present without duplication. All 704 recovered records remain source-unverified and syllabus-mapping pending. The 1.39 MB review queue was validated through its Git blob: valid JSON, 704 unique IDs, four options each, no overlap with active IDs.
- Forensic Science Code 27: 291 active / 9 review-only. All 300 source records visually verified and 300/300 final-key entries reconciled. The November 2025 paper metadata is corrected to 100 loaded / 100 source verified; 98 mappings verified, Q59 provisional and Q47 pending.
- Environmental Sciences Code 26: 300/300 syllabus mappings assigned to official units; 213 review-only source-verification flags remain untouched.
- Gujarati Code 06: 196 active / 204 review-only after moving 99 fully checked December 2019 records into active. Q7 (official Z/not evaluated) remains held.
- Seven-subject totals: 968 active + 1,132 review-only + 1,100 untranscribed = 3,200. The untranscribed backlog is Geography 500 + Social Work 600.
- History Q46/Q48 remain unmapped because the official Code 08 syllabus does not give a defensible direct unit fit; no guessed mapping was added.
- Social Work Code 25 remains 600 not transcribed. Official Code 25 syllabus located; the six official paper PDFs in the repository manifest have not yet been made available for source-based transcription in this workspace.
- PR #22 remains open and unmerged. Latest commit CI workflow runs and combined status checks are empty; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 November 2023 Q79–Q86 source verification
- Before this batch: 87 active / 213 review-only across 300 records; November 2023 had 79 source-verified questions and 21 review-only records. The already-verified Q87 was retained and not repeated.
- Official question-paper PDF pages 16–17 (zero-based indexes 15–16) visually checked. Q79–Q86 stems and all four options match the original scan; no figures or tables occur in this range.
- Official final-key answers: Q79 D, Q80 C, Q81 A, Q82 A, Q83 B, Q84 A, Q85 D, Q86 A. All 8/8 match the stored official answers and the GSET final-key table.
- Mappings: Q79–Q80 Unit VIII; Q81–Q86 Unit IX. Q84 was corrected from Unit III to Unit IX because official Code 26 Unit IX explicitly names the Leslie matrix and Lotka–Volterra models under models of population growth and interactions.
- After this batch: Environmental Sciences 95 active / 205 review-only; November 2023 is 87/100 source-verified with Q88–Q100 still pending. All 300 mappings remain verified (0 provisional, 0 pending). Official answer-key parity remains 300/300.
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov23/nov2326.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov23/nov2326.pdf ; https://gujaratset.ac.in/assets/syllabus/26.pdf.
- Seven-subject totals: 976 active + 1,124 review-only present + 1,100 untranscribed = 3,200. No other subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. PR #22 remains open/unmerged; no CI or Combined Debug APK pass is claimed.
- Next batch: Environmental Sciences Code 26, November 2023 Q88–Q95.


## 2026-11-16 — Sanskrit Code 07 recovery audit and one source-verified integration
- Audited the Library consolidated staging source (850 question records across December 2002, December 2003, December 2008, September 2013, August 2017, December 2019, December 2021, November 2022, November 2023, December 2024, and November 2025). Against the canonical bank before this batch, 146 records overlapped and 704 were absent; the review queue file itself was empty. After this batch, canonical active count is 147 and 703 staged records remain unintegrated.
- November 2025 final-answer-key parity: staging answers match the official final answer key 100/100. December 2024 final-answer-key parity: 100/100. This is answer-key reconciliation only; it does not mean every transcription has been visually verified.
- November 2025 Q38 was visually compared against official paper printed page 8 (Q38–Q45): stem and all four options match. Its answer B matches the official final key. Q38 was promoted to active in `questions.json`; it is not a blanket approval of the other staged records. Commit: `2fb731f43541c23868b2a22c10cfb613fb4cf855`.
- November 2025 Q53 remains review-required because option D is a Brahmi-script glyph that is not represented as ordinary text; official key B is retained. December 2024 staging still has three review-required items (Q5, Q28, Q63); November 2025 has one remaining review-required item (Q53) after Q38 resolution.
- The consolidated staging file also contains 300 answer-key-only rows across September 2016 (50), September 2018 (100), January 2002 (50), July 2004 (50), and July 2006 (50). These do not contain transcribed question records and are not included in the 850-question staging count.
- Official source PDFs: November 2025 question paper `https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2507.pdf`, final key `https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2507.pdf`; December 2024 question paper `https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2407.pdf`, final key `https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2407.pdf`.
- No other subject or Paper-I changed. PR #22 remains unmerged; no CI/APK pass is claimed.


## 2026-11-16 — Sanskrit Code 07 November 2025 Q1–Q6 source batch
- Official paper printed page 3 was visually inspected. Q1, Q2, Q4, Q5, and Q6 stems and all four options were checked against the page; source punctuation/Devanagari visarga and Q2 option A were normalized to match the printed page. Q3's matching-table structure is retained for separate layout review and was not promoted.
- Official final-key answers: Q1=C, Q2=D, Q4=D, Q5=C, Q6=C; all five match the official November 2025 final answer key.
- Promoted Q1, Q2, Q4, Q5, Q6 to active. Sanskrit canonical active count: 152; review queue remains empty; 698 of the 850 consolidated staging records remain outside the canonical bank. Combined seven-subject counts: 982 active, 420 review-only present, 698 staged-not-integrated, 1,100 not transcribed.
- Q3 remains held for matching-table layout fidelity; Q53 remains held because option D is a Brahmi glyph; December 2024 Q5/Q28/Q63 remain review-required. No blanket source-verification claim is made for the remaining staged records.
- Commit adding Q1, Q2, Q4–Q6: `74e8d9efcc44d7386eeb400b9be41cbef5b03cc5`.


## 2026-11-16 — Sanskrit Code 07: resolve Q3, Q53 and December 2024 proofreading batch
- November 2025 Q3: printed page 3 visually checked. The a–d metre names, i–iv gana patterns and A–D matching permutations were transcribed preserving the original two-column matching structure. Official final-key answer C matches the printed choice. Integrated into canonical `questions.json` as active. Source page: `https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2507.pdf` (printed page 3).
- November 2025 Q53: printed page 9 visually checked. Option D's Brahmi glyph was transcribed as Unicode Brahmi letter KA U+11013 (`𑀓`); option C is `><`. Official final key says B (+), although the question's semantic reading appears to point to the Brahmi KA glyph at D. Official key B is preserved; Q53 is retained in `questions_review_pending.json` for expert answer-key discrepancy review, not activated. Official key: `https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2507.pdf`.
- December 2024 Q5: printed page 1 visually checked. Option B reads `विण्टरनिट्झ–वेबर`; prior possible-nukta ambiguity is resolved. Stem and all four options match; official final-key answer D confirmed. Retained review-only pending the full December 2024 paper source pass.
- December 2024 Q28: printed page 5 visually checked. Corrected verse transcription to `कुसुमं कुमुद्वत्याः` and final double danda `॥`; stem and options match; official final-key answer A confirmed. Retained review-only pending the full December 2024 paper source pass.
- December 2024 Q63: printed page 10 visually checked. The scan appears to print option C as `कर्तरि कर्मण्यतिहारे`; this is preserved verbatim rather than silently normalizing to the familiar `कर्मव्यतिहारे`. Official final-key answer D confirmed. Retained review-only for expert review of possible source typographic discrepancy.
- Canonical changes: Q3 promoted active; Q53 + Dec 2024 Q5/Q28/Q63 added to the review queue. Sanskrit now 153 active / 4 review-only in canonical JSON; 693 of 850 staged records remain outside the canonical files. Seven-subject totals: 983 active, 424 review-only, 693 staged-not-integrated, 1,100 not transcribed = 3,200 expected.
- Official December 2024 sources: question paper `https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2407.pdf`; final key `https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2407.pdf`. Official November 2025 sources: question paper `https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2507.pdf`; final key `https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2507.pdf`.
- No other subject, Paper-I, Code 01, Code 02, or Code 28 changed. PR #22 remains unmerged. No CI/APK pass is claimed.


## 2026-11-16 — Sanskrit Code 07 November batch integration
- Integrated 45 additional November 2025 Paper-II Sanskrit questions (Q7–Q37, Q39–Q45, Q70, Q85, Q88, Q91, Q93, Q94, Q97) into canonical `questions.json` after checking the source paper transcription and matching every answer letter to the official final answer key.
- November 2025 now has 99 active records plus Q53 retained in the review queue. Q53's Brahmi glyph / official-key discrepancy remains review-only; it was not promoted or altered.
- November 2023 Q100 was checked for duplicate status and already existed in the canonical bank; no duplicate was added.
- Sanskrit canonical active count: 198; review-only count: 4; distinct staging records not yet integrated: 648. Seven-subject totals: 1,028 active, 424 review-only, 648 staged-not-integrated, 1,100 not transcribed = 3,200.
- Commit: 218a7c39654ee14792166936102a3f983d86a21f. No merge was performed. No CI/APK pass is claimed. Syllabus mappings for the new batch remain pending; source/key verification does not imply syllabus mapping completion.


## 2026-11-16 — Sanskrit November 2025 integration and review reconciliation
- Added 45 missing November 2025 records to canonical bank; Q100 from November 2023 was already present and was not duplicated.
- November 2025 canonical distribution: 93 active and 7 review-only (Q53, Q85, Q88, Q91, Q93, Q94, Q97). Q53 remains held for Brahmi glyph / official-key discrepancy. Q85, Q88, Q91, Q93, Q94 and Q97 remain review-only because the earlier source audit identified Devanagari transcription discrepancies requiring another exact proofread; official final-key letters were preserved.
- Sanskrit canonical totals: 192 active, 10 review-only, 648 staged records not yet integrated. Seven-subject totals: 1,022 active + 430 review-only + 648 staged-not-integrated + 1,100 not yet transcribed = 3,200.
- Source audit and review queue reconciled. No PR merge. No CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 November 2023 Q33 source verification
- User supplied the official November 2023 Sanskrit Paper-II scan and final answer key. Printed page 7 visually confirms Q33 stem `अधोदत्तेषु किं काण्डं रामायणे प्रक्षिप्तं मन्यते ?` and options A सुन्दरकाण्डम्, B युद्धकाण्डम्, C अयोध्याकाण्डम्, D किष्किन्धाकाण्डम्.
- Official final answer key gives Q33 = B. The stem/options and key were checked, but the item remains review-only because its content/key interpretation requires Sanskrit subject-expert review; official key B is preserved and no model-derived answer substituted.
- Added Q33 to `questions_review_pending.json`; no active-bank promotion. Sanskrit remains 192 active / 11 review-only; 647 of 850 staging records are outside both canonical files. Seven-subject totals: 1,022 active + 431 review-only + 647 staged-not-integrated + 1,100 not transcribed = 3,200.
- December 2024 official paper and final key were also supplied; existing Q5, Q28 and Q63 remain source-verified review-only. The remaining December 2024 records have not yet been integrated. No other subject changed; PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q1–Q7 source batch
- Visually checked printed page 3 of the user-supplied official December 2024 Paper-II scan. Q1–Q7 stems and all four options were compared with the consolidated staging transcription. Q5 was already present in the review queue; Q1–Q4 and Q6–Q7 were added as six new review-only records.
- Official final-key answers confirmed: Q1 D, Q2 A, Q3 D, Q4 A, Q5 D, Q6 A, Q7 D. All seven are retained review-only pending full December 2024 paper completion and official syllabus mapping; no automatic promotion to active.
- Sanskrit canonical totals: 192 active / 17 review-only; 641 of 850 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 437 review-only + 641 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q8–Q16 source batch
- Visually checked printed page 4 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q8–Q16 stems and all four options match the source; nine records added to the canonical review queue.
- Official final-key answers confirmed: Q8 A, Q9 B, Q10 C, Q11 A, Q12 A, Q13 C, Q14 D, Q15 B, Q16 C. All nine remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 26 review-only; 632 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 446 review-only + 632 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q17–Q23 source batch
- Visually checked printed page 5 of the user-supplied official December 2024 paper. Q17–Q23 stems and options match; Q23's a–d / i–iv matching-table structure was preserved.
- Official final-key answers confirmed: Q17 B, Q18 C, Q19 D, Q20 A, Q21 C, Q22 D, Q23 A. Seven records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 33 review-only; 625 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 453 review-only + 625 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q24–Q31 source batch
- Visually checked printed page 6 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q24–Q27 and Q29–Q31 stems/options match. Q28 was already in the review queue and was not duplicated.
- Official final-key answers confirmed: Q24 A, Q25 A, Q26 D, Q27 C, Q28 A (existing record), Q29 A, Q30 B, Q31 A. Seven new records added to review queue; Q28 remains held for its separate verse transcription review. All remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 40 review-only; 618 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 460 review-only + 618 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q32–Q39 source batch
- Visually checked printed page 7 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q32–Q39 stems and all four options match the scan.
- Official final-key answers confirmed: Q32 A, Q33 A, Q34 B, Q35 B, Q36 D, Q37 A, Q38 C, Q39 B. Eight records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 48 review-only; 610 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 468 review-only + 610 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q40–Q48 source batch
- Visually checked printed page 8 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q40–Q48 stems and all four options match.
- Official final-key answers confirmed: Q40 A, Q41 C, Q42 C, Q43 A, Q44 C, Q45 A, Q46 A, Q47 A, Q48 A. Nine records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 57 review-only; 601 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 477 review-only + 601 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q49–Q55 source batch
- Visually checked printed page 9 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q49–Q55 stems and all four options match.
- Official final-key answers confirmed: Q49 D, Q50 A, Q51 A, Q52 C, Q53 A, Q54 A, Q55 A. Seven records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 64 review-only; 594 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 484 review-only + 594 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q56–Q63 source batch
- Visually checked printed page 10 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q56–Q62 stems and all four options match. Existing Q63 review record was not duplicated.
- Official final-key answers confirmed: Q56 A, Q57 D, Q58 B, Q59 A, Q60 A, Q61 B, Q62 A, Q63 D. Seven new records added to review queue; Q63 remains separately held for its printed wording concern.
- Sanskrit canonical totals: 192 active / 71 review-only; 587 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 491 review-only + 587 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q64–Q70 source batch
- Visually checked printed page 11 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q64–Q70 stems and all four options match.
- Official final-key answers confirmed: Q64 D, Q65 A, Q66 C, Q67 B, Q68 C, Q69 C, Q70 A. Seven records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 78 review-only; 580 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 498 review-only + 580 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q71–Q78 source batch
- Visually checked printed page 12 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q71–Q78 stems and all four options match.
- Official final-key answers confirmed: Q71 D, Q72 C, Q73 B, Q74 D, Q75 C, Q76 C, Q77 D, Q78 A. Eight records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 86 review-only; 572 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 506 review-only + 572 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q79–Q86 source batch
- Visually checked printed page 13 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q79–Q86 stems and all four options match.
- Q85's printed notation `प(p)` is preserved verbatim rather than normalized. Official final-key answers confirmed: Q79 D, Q80 C, Q81 D, Q82 C, Q83 B, Q84 C, Q85 B, Q86 A. Eight records added to review queue; all remain review-only pending full-paper completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 94 review-only; 564 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 514 review-only + 564 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 Q87–Q95 source batch
- Visually checked printed page 14 of the user-supplied official December 2024 Sanskrit Paper-II scan. Q87–Q95 stems and all four options match.
- Q90 title preserved as printed. Official final-key answers confirmed: Q87 A, Q88 B, Q89 B, Q90 D, Q91 A, Q92 A, Q93 C, Q94 B, Q95 B. Nine records added to review queue; all remain review-only pending final-page completion and official syllabus mapping.
- Sanskrit canonical totals: 192 active / 103 review-only; 555 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 523 review-only + 555 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 complete source pass
- Completed visual source verification of all 100 questions in the user-supplied official December 2024 Sanskrit Paper-II scan, Q1–Q100, and reconciled every answer against the official final answer key (100/100).
- Final page Q96–Q100 checked; Q99's matching table preserved. Existing Q5, Q28 and Q63 were retained without duplicates; other missing records added to the review queue. All 100 December 2024 questions are represented in canonical active + review files.
- All 100 are source-verified and final-key reconciled, but remain review-only pending official Code 07 syllabus mapping and editorial sign-off; source verification alone does not authorize activation.
- Sanskrit canonical totals: 192 active / 108 review-only; 550 staging records remain outside both canonical files. Seven-subject totals: 1,022 active + 528 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200.
- No other subject changed. PR #22 remains unmerged; no CI/APK pass claimed.


## 2026-11-16 — Environmental Sciences Code 26 November 2023 Q88–Q100 source verification
- Visually checked Q88–Q100 against the official GSET November 2023 Environmental Sciences Paper-II scan (PDF zero-based pages 16–18). Q91 and Q94 matching-column structures were checked and retained.
- Independently reconciled all 13 stored answer letters against the official final answer key: Q88 A, Q89 B, Q90 D, Q91 A, Q92 A, Q93 B, Q94 A, Q95 C, Q96 A, Q97 D, Q98 A, Q99 A, Q100 D — 13/13 match.
- All 13 already had a recorded official Code 26 syllabus unit; after source verification they were promoted from review-only to active.
- Environmental Sciences changed from 95 active / 205 review-only to 108 active / 192 review-only. No other subject was modified in this batch.
- Official question paper: https://gujaratset.ac.in/assets/papers/paperII/nov23/nov2326.pdf ; official final answer key: https://gujaratset.ac.in/assets/anskey/paperII/nov23/nov2326.pdf ; official syllabus: https://gujaratset.ac.in/assets/syllabus/26.pdf
- PR #22 remains open and unmerged. No combined Debug APK or CI PASS is claimed.


## 2026-11-16 — Gujarati Code 06 August 2017 Q7–Q12 source verification
- Rechecked the official August 2017 Gujarati Paper-II scan, printed page 4 (PDF zero-based page 2), for Q7–Q12. Stems and all four Gujarati options match the source; Q11's chronological-order list was preserved.
- Official final-key answers: Q7 C, Q8 D, Q9 A, Q10 B, Q11 C, Q12 B. All six match the official final key.
- All six records have verified Code 06 syllabus-unit placements. Q8's previously pending visual source check was completed; Q7 and Q9–Q12 were already source-checked but were held in the review queue. All six passed the active-bank gates and were promoted.
- Gujarati changed from 196 active / 204 review-only to 202 active / 198 review-only. The remaining Gujarati review queue still contains 51 source-unverified records and 33 records without final-key verification.
- Official question paper: https://gujaratset.ac.in/assets/papers/paperII/aug17/aug1706.pdf ; official final answer key: https://gujaratset.ac.in/assets/anskey/paperII/aug17/aug1706.pdf ; official syllabus: https://gujaratset.ac.in/assets/syllabus/06.pdf
- PR #22 remains open and unmerged. No combined Debug APK or CI PASS is claimed.


## 2026-11-16 — Sanskrit Code 07 December 2024 official syllabus mapping
- Reopened the official GSET Sanskrit Code 07 syllabus PDF (7 pages) and mapped the December 2024 question batch Q1–Q100 at question level.
- 98/100 questions now have an explicit official syllabus unit assignment in `questions_review_pending.json`; Q14 (specific vāyu / vital-air classification) and Q27 (fourfold body classification) remain unmapped because that exact subject matter is not expressly named in the official syllabus. They remain review-only; no forced unit assignment.
- Mapping covers Units I–X: Vedic literature; specific Vedic literature; general and specific Indian philosophy; grammar and linguistics; detailed grammar; Sanskrit literature/poetics/chandas; prescribed literary works; Puranic history/Dharmashastra/inscriptions; and Arthashastra/Smriti.
- All 100 December 2024 records remain review-only pending editorial sign-off. No question was promoted to active solely because mapping was completed. Existing Q5/Q28/Q63 concerns remain preserved; official final-key letters remain unchanged.
- Sanskrit canonical count remains 192 active / 108 review-only; staging records not integrated remain 550. Seven-subject totals remain 1,041 active + 509 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200.
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. PR #22 remains open and unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Sanskrit Code 07 remaining review-record syllabus pass
- Added official syllabus mappings for the eight previously pending Sanskrit review records: November 2023 Q33 (Ramayana / Unit IX) and November 2025 Q53 (Brahmi script / Unit IX), Q85 (Samkhya / Unit IV), Q88, Q91, Q93, Q94 (Vedic literature / Unit I), and Q97 (Sanskrit poetry / Unit VII).
- These eight records remain review-only: Q33 retains the official-key/content expert-review hold; Q53 retains the official-key discrepancy; Q85/Q88/Q91/Q93/Q94 retain transcription-proofreading holds; Q97 is mapped but awaits editorial sign-off. No official answer letter or source text was changed.
- Across the December 2024 batch, 98/100 are syllabus-mapped; Q14 and Q27 remain the only December 2024 mapping holds. No review-only record was promoted.
- Official source: https://gujaratset.ac.in/assets/syllabus/07.pdf. PR #22 remains open and unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Gujarati Code 06 safe promotion batch
- Audited all 198 records in the Gujarati review queue against the promotion gates already recorded in the JSON: source_verified=true, answer_key_verified=true, syllabus_mapping_status=verified, and review_flag not true.
- Promoted 94 records satisfying every gate into the active bank. Checked for ID collisions against the existing 202 active records; duplicates found: 0. No question text, options, answer letter or syllabus unit was changed.
- Gujarati is now 296 active / 104 review-only. The remaining queue contains 48 source-verified and 71 final-key-verified records; 56 still need source-page verification and 33 still need final-key verification (some records may overlap these categories).
- Seven-subject totals: 1,135 active + 415 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open and unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q1–Q7 and Q9–Q13
- Visually checked the official December 2024 Environmental Sciences Paper-II scan: Q1–Q4 on printed page 3 (PDF index 2), Q5–Q8 on printed page 4 (PDF index 3), and Q9–Q13 on printed page 5 (PDF index 4). All stems and four options for Q1–Q7 and Q9–Q13 match the canonical records.
- Independently checked the official final answer key: Q1 A, Q2 B, Q3 B, Q4 A, Q5 A, Q6 D, Q7 B, Q9 D, Q10 A, Q11 B, Q12 D, Q13 A. All 12 match. Q8 was not changed because it was already outside this review batch.
- All 12 records already had verified Code 26 syllabus mappings. Promoted them to active after checking there were no duplicate IDs. Environmental Sciences is now 120 active / 180 review-only; 12 records were moved, with no changes to question wording or answer letters.
- Seven-subject totals: 1,147 active + 403 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open and unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q14–Q19 and Q21–Q22
- Visually checked the official December 2024 paper scan: Q14–Q18 on printed page 6 (PDF index 5) and Q19–Q22 on printed page 7 (PDF index 6). The English stems and all four options for Q14–Q19 and Q21–Q22 match the canonical records.
- Official final-key answers independently matched: Q14 D, Q15 A, Q16 A, Q17 B, Q18 D, Q19 A, Q21 B, Q22 D. Q20 was not part of this review-only batch and was left unchanged.
- All eight records already had verified syllabus mappings. Promoted all eight after duplicate-ID checks; no question wording or answer letters were altered. Environmental Sciences now stands at 128 active / 172 review-only.
- Seven-subject totals: 1,155 active + 395 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q23–Q27
- Visually checked the official December 2024 scan, printed page 8 (PDF index 7), for Q23–Q27. Stems and all four options match; Q26's two-column classification table and all answer combinations were checked against the scan.
- Official final-key answers independently matched: Q23 B, Q24 D, Q25 A, Q26 A, Q27 A. All five already had verified official Code 26 syllabus mappings.
- Promoted five records after checking for duplicate IDs; no question wording or official answer letters changed. Environmental Sciences now stands at 133 active / 167 review-only.
- Seven-subject totals: 1,160 active + 390 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q34–Q40
- Visually checked the official December 2024 Environmental Sciences scan, printed page 10 (PDF index 9), for Q34–Q40. Stems and all four options match the canonical records.
- Official final-key answers are D for each of Q34–Q40; all seven stored letters match. All seven already had verified official syllabus mappings.
- Promoted seven records after duplicate-ID checks; no text or answer changes. Environmental Sciences now stands at 140 active / 160 review-only. PDF page index 8 (Q28–Q33) returned 403 and was not claimed as verified in this batch.
- Seven-subject totals: 1,167 active + 383 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q41–Q46
- Visually checked the official December 2024 scan, printed page 11 (PDF index 10), for Q41–Q46. All stems and four options match; Q45's matching table and answer combinations were checked.
- Official final-key answers matched: Q41 D, Q42 A, Q43 D, Q44 C, Q45 A, Q46 C. All six already had verified syllabus mappings.
- Promoted six records after duplicate-ID checks; no text or official answer letters changed. Environmental Sciences now stands at 146 active / 154 review-only.
- Seven-subject totals: 1,173 active + 377 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q47–Q50 and Q52–Q53
- Visually checked the official December 2024 scan, printed page 12 (PDF index 11), for Q47–Q53. Q47–Q50 and Q52–Q53 stems and all four options match; Q51 was already active and was not modified.
- Official final-key answers matched: Q47 D, Q48 D, Q49 C, Q50 A, Q52 A, Q53 C. All six already had verified syllabus mappings.
- Promoted six records after duplicate-ID checks; no wording or official answer letters changed. Environmental Sciences now stands at 152 active / 148 review-only.
- Seven-subject totals: 1,179 active + 371 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q54–Q62
- Visually checked the official December 2024 scan, printed page 13 (PDF index 12), for Q54–Q62. All stems and four options match the scan.
- Official final-key answers matched: Q54 C, Q55 A, Q56 C, Q57 C, Q58 B, Q59 D, Q60 C, Q61 D, Q62 A. All nine had verified syllabus mappings.
- Corrected one source-transcription typo in Q61: canonical “combution” was changed to the printed “combustion”. Promoted all nine after duplicate-ID checks; no official answer letters changed. Environmental Sciences now stands at 161 active / 139 review-only.
- Seven-subject totals: 1,188 active + 362 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q63–Q71
- Visually checked the official December 2024 scan, printed page 14 (PDF index 13), for Q63–Q71. All stems and four options match the canonical records.
- Official final-key answers matched: Q63 D, Q64 C, Q65 B, Q66 D, Q67 C, Q68 C, Q69 B, Q70 A, Q71 B. All nine already had verified syllabus mappings.
- Promoted nine records after duplicate-ID checks; no text or answer letters changed. Environmental Sciences now stands at 170 active / 130 review-only.
- Seven-subject totals: 1,197 active + 353 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q72–Q79
- Visually checked the official December 2024 scan: Q72–Q75 on printed page 15 (PDF index 14) and Q76–Q79 on printed page 16 (PDF index 15). Stems and all four options match; matching and statement-selection structures were preserved.
- Official final-key answers matched: Q72 D, Q73 C, Q74 B, Q75 C, Q76 B, Q77 D, Q78 D, Q79 B. All eight already had verified syllabus mappings.
- Promoted eight records after duplicate-ID checks. Environmental Sciences now stands at 178 active / 122 review-only.
- Seven-subject totals: 1,205 active + 345 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Environmental Sciences Code 26 December 2024 Q80–Q88
- Visually checked the official December 2024 scan, printed page 17 (PDF index 16), for Q80–Q88. All stems and options match; mathematical notation in Q84 and statistical expressions in Q82–Q87 were checked.
- Official final-key answers matched: Q80 A, Q81 A, Q82 A, Q83 A, Q84 A, Q85 B, Q86 B, Q87 B, Q88 C. All nine already had verified syllabus mappings.
- Promoted nine records after duplicate-ID checks. Environmental Sciences now stands at 187 active / 113 review-only.
- Seven-subject totals: 1,214 active + 336 review-only + 550 staged-not-integrated + 1,100 not transcribed = 3,200. PR #22 remains open/unmerged; no CI/APK PASS is claimed.


## 2026-11-16 — Forensic Science Code 27 Q59 mapping resolution
- Reviewed the official Code 27 syllabus. December 2024 Q59 (rape-kit purpose) is supported by Unit I, which explicitly includes sexual offences under Criminal Investigations and collection/preservation of physical evidence.
- Promoted `GSET-FS27-DEC2024-Q059` from review-only to active without changing its source wording, options, or official final-key answer.
- Current Forensic Science count after live verification: 292 active / 8 review-only. The remaining eight are retained for explicit syllabus-scope uncertainty; no forced mapping.


## 2026-11-16 — History Code 08 syllabus-hold clarification
- Rechecked official Code 08 syllabus against September 2016 Q46 and Q48. Q46 asks about South African apartheid/racial segregation; the syllabus scope is Indian history and does not explicitly include South Africa/Apartheid. Q48 asks for the author of *The Wealth of Nations*; the syllabus does not explicitly list Adam Smith or European political economy. Neither question has been assigned an inferred unit.
- Updated both canonical records with `review_flag=true` and explicit `review_note`; their final-key answers and source-verification status were not changed. Both remain pending official syllabus mapping / expert review.
- Official syllabus: https://www.gujaratset.ac.in/assets/syllabus/08.pdf (GSET History Code 08).
- No unrelated subject, Paper-I, Code 01, Code 02, or Code 28 was modified. PR #22 remains open and unmerged; no combined APK PASS is claimed.


## 2026-11-16 — Canonical JSON count correction (live branch audit)
- Re-fetched all seven canonical `questions.json` files and the applicable review queues on branch `app/import-updated-subject-banks-2026-11-10`. Counts in the PR body and top checkpoint table had drifted from the live JSON.
- Gujarati: 356 records in `questions.json` + 44 in `questions_review_pending.json` = 400; all 356 canonical active records have `review_flag=false`. This supersedes stale 296/104 counts.
- Environmental Sciences: 300 records in `questions.json`, 0 in `questions_review_pending.json`; all 300 canonical records have `source_verified=true`, `answer_key_verified=true`, `review_flag=false`, and `syllabus_mapping_status=verified`. This supersedes stale 187/113 counts and confirms the subject bank is complete at the canonical-file level.
- Forensic Science: 292 active + 8 review-only. Geography: 198 active + 2 review-only + 500 not transcribed. Sanskrit: 192 active + 108 review-only + 550 staging not integrated. History: 50 active; Q46 and Q48 remain syllabus holds. Social Work: 600 official key entries but question text remains untranscribed.
- Corrected seven-subject aggregate: 1,388 active + 162 review-only + 550 Sanskrit staging + 1,100 not transcribed = 3,200 expected records.
- Updated PR #22 body to reflect these canonical counts. No question content was changed in this audit; no unrelated subject/Paper-I/Code 01/Code 02/Code 28 was modified. PR #22 remains open and unmerged; no combined APK PASS is claimed.


## 2026-11-16 — Gujarati Code 06 source-verification batch
- Official GSET August 2017 Gujarati Paper-II printed page 12 (PDF page index 11) visually checked for Q40 and Q41, including both matching tables and all four answer options.
- Official GSET final answer key independently confirms Q40=B and Q41=D.
- Promoted only these two records from review-only to canonical active questions. Canonical Gujarati count: 358 active / 42 review-only (400 total).
- Review queue reduced from 44 to 42. Q40/Q41 source verification notes record the official paper page and final-key parity.
- No other subject, Paper-I, Code 01, Code 02, or Code 28 changed. PR #22 remains open and unmerged. No CI/APK pass is claimed.


## 2026-11-16 — Gujarati Code 06 source-verification batch 2
- Official GSET August 2017 Gujarati Paper-II PDF page index 3 (printed page 3; scan rotated 180 degrees) visually checked for Q1–Q6, including stems and all four Gujarati options.
- All six stored answers already matched the official answer-key records; answer letters were not changed.
- Promoted Q1–Q6 from review-only into canonical `questions.json`; the review queue was reduced by six.
- Gujarati now has 364 active + 36 review-only = 400 records. Seven-subject aggregate is 1,396 active + 154 review-only + 550 Sanskrit keys-only staging + 1,100 Geography/Social Work untranscribed = 3,200 expected.
- PR #22 remains open and unmerged. No CI or Combined APK pass is claimed; no other subject was changed.


## 2026-11-16 — Social Work Code 25 transcription batch 1
- Transcribed official November 2022 Paper-II questions Q1–Q23 from the official question booklet PDF (booklet serial 250512). English stems and all four English options were captured; the booklet states English prevails in case of language discrepancy.
- Reconciled all 23 answer letters against the official GSET FINAL ANSWER KEY for November 2022. No answer-key mismatch was found.
- Added 23 canonical Social Work records with source PDF URL, official final-key source, exam date (6 November 2022), and question-level syllabus-unit mapping for Units I, II, III, V, VI and VII. No figure/table was present in this batch.
- Social Work now has 23 active records; 577 of the 600 target questions remain untranscribed. This is a first partial batch, not a completed subject.
- Seven-subject totals now: 1,419 active + 154 review-only + 550 Sanskrit keys-only staging + 1,077 not transcribed = 3,200 expected.
- PR #22 remains open and unmerged. No combined APK/CI PASS is claimed. No other subject or unrelated bank was modified in this batch.


## 16 November 2026 — Social Work transcription continuation

- Nov 2023: 100/100 questions transcribed; official final-key parity complete. All 100 retain review flags pending official syllabus mapping.
- Dec 2019: Q1–Q25 transcribed and visually checked against official source PDF; all 25 answers match the official final key. Q26–Q100 remain.
- Nov 2022: 100/100 questions transcribed and reconciled; 77 syllabus mapping flags remain.
- Canonical Social Work total: 225 question records. Remaining transcription: 375 (Dec 2019: 75; Dec 2021: 100; Dec 2024: 100; Nov 2025: 100).
- No unsupported syllabus mappings assigned; these Social Work records remain review-only pending mapping review.
- Latest branch head at this checkpoint: 68b875abb6769207939e44527de14d8f0de06907. PR #22 open/unmerged. No CI workflow run or combined APK PASS observed.


## 16 November 2026 — latest verified continuation

### Social Work (Code 25)
- December 2019 Q1–Q100 is now complete: all 100 question stems/options were transcribed from the official paper and all 100 stored answers match the official final answer key. Syllabus mapping remains pending for all 100, so they remain review-only.
- December 2021 / January 2022 Q1–Q12 are transcribed and visually checked against the official paper; all 12 answers match the official final key. Q13–Q100 remain untranscribed.
- Current canonical Social Work records: 312. Per-paper counts: social_work_dec2019=100, social_work_dec2021=12, social_work_nov2022=100, social_work_nov2023=100.
- Social Work transcription remaining: 288 (Dec 2021 Q13–Q100 = 88; Dec 2024 = 100; Nov 2025 = 100). Nov 2022 and Nov 2023 remain 100/100 each.

### Sanskrit (Code 07)
- Restored 550 unique question records from the consolidated staging Library source into questions_review_pending.json after confirming they were absent from both canonical files.
- Review queue now contains 658 unique records (108 existing + 550 restored). All 550 recovered records remain review-only, source_verified=false, with official syllabus mapping pending. No record was promoted active by this recovery.
- The five separate answer-key-only sessions (300 key entries) remain distinct and are not treated as transcribed question text.
- Updated source_audit.json; it now records zero missing staging IDs across active + review-only stores.

### Outstanding work
- Geography: 500 questions remain untranscribed across five papers. Two Nov 2025 records remain review-only (one official-key/content discrepancy; one provisional syllabus mapping).
- Sanskrit: visual proofreading, final-key reconciliation where applicable, and syllabus mapping remain for the restored queue.
- History: Q46 and Q48 remain intentionally unmapped because the official syllabus does not explicitly cover their concepts.
- Gujarati: 36 review-only records remain; only source-backed records may be promoted.
- Forensic Science: eight source/key-verified review-only records remain due to syllabus-scope uncertainty; do not force mappings.
- Social Work: all newly transcribed records remain review-only pending official syllabus mapping.
- No CI workflow run/status check or combined APK PASS has been observed for the current head.
- PR #22 remains open and unmerged; no merge authorized.


## 16 November 2026 — Social Work follow-up and parity audit
- Social Work Dec 2019: 100/100 complete; all 100 answers match the official final key. Q17 was corrected from C to official key B after an independent question-level parity check.
- Social Work Dec 2021/Jan 2022: Q1–Q31 transcribed from official source pages and all 31 answers match the official final answer key. Q32–Q100 remain untranscribed.
- Social Work canonical total is now 331/600: Nov 2022 100, Nov 2023 100, Dec 2019 100, Dec 2021 31. Remaining transcription: 269 (Dec 2021 69 + Dec 2024 100 + Nov 2025 100).
- Independent key parity audit: zero mismatches across all 331 transcribed Social Work records. All 331 records have four complete English options. All 308 current Social Work review flags remain due to pending official syllabus mapping; no unsupported units were assigned.
- Sanskrit 550 missing staged questions have been restored to review-only queue; 658 total review-only records. No activation occurred.
- CI/APK: current feature-branch head has no associated Actions run or status checks. Combined subject audit and integration Debug APK workflows are configured for the integration branch / workflow_dispatch, not this feature branch. No APK PASS is claimed.


## 16 November 2026 — latest checkpoint after Dec 2021 Q31
- Social Work canonical questions: 331/600 (Nov 2022 100, Nov 2023 100, Dec 2019 100, Dec 2021 31). Remaining transcription: 269 (Dec 2021 Q32–Q100: 69; Dec 2024: 100; Nov 2025: 100).
- Social Work answer-key parity rechecked against the staging key table: 331/331 transcribed questions match the official final key. Dec 2019 Q17 was corrected to official key B; no mismatch remains. All 331 records have four English options.
- Seven-subject canonical structural audit: 1,727 records; zero duplicate IDs, zero missing four-option arrays, zero invalid answer letters, and zero unknown paper IDs. This is a JSON/schema audit, not a CI or APK build.
- Current subject state (active / review-only): Gujarati 364/36; Sanskrit 192/658; History 48/2; Geography 198/2; Social Work 23/308; Environmental Sciences 300/0; Forensic Science 292/8. Totals: 1,417 active and 1,014 review-only.
- Not yet transcribed: Geography 500 and Social Work 269 = 769 questions. Sanskrit's 550 recovered staging records are now counted in the review-only queue, not as active questions. Five separate Sanskrit keys-only sessions (300 answer entries) remain separate from question text.
- Official syllabus mapping and source review remain open for review-only records; no unsupported mapping or automatic promotion was made.
- Current feature branch has no Actions run or status checks. Combined subject audit and Integration Debug APK workflows support workflow_dispatch; no APK PASS is claimed.
- PR #22 remains open and unmerged.


## 16 November 2026 — Social Work transcription continuation (latest)

- December 2019: 100/100 questions now transcribed from the official GSET Paper-II PDF. All 100 answers match the official final answer key; source and key parity complete. All 100 remain review-only pending official syllabus mapping.
- December 2021 / January 2022: 96/100 questions transcribed and visually checked. All 96 answers match the official final answer key. Q32–Q35 are still not transcribed because the corresponding official PDF page could not be reliably retrieved; do not infer them. Paper remains incomplete and not eligible as a full practice test.
- November 2022: 100/100 transcribed and key-reconciled; 77 syllabus mapping flags remain.
- November 2023: 100/100 transcribed and key-reconciled; 100 syllabus mapping flags remain.
- Canonical Social Work total: 396 unique records: Dec 2019 (100), Dec 2021/Jan 2022 (96), Nov 2022 (100), Nov 2023 (100). Remaining Social Work transcription: 204 questions (Dec 2021 Q32–Q35; Dec 2024 100; Nov 2025 100).
- An integrity audit confirmed unique IDs, four English options per record, and exact official final-key parity for every loaded question in Dec 2019 and Dec 2021. No unsupported syllabus mappings were added; review flags retained.
- PR #22 remains open and unmerged. No CI run or combined APK PASS observed.


## 16 November 2026 — Cross-subject review-queue and Sanskrit staging audit

- Gujarati: 36 records in questions_review_pending.json; these include source-page proofreading, ambiguous glyphs, and historical key/numbering conflicts. They remain held.
- History: 2 mapping holds; both remain review-only.
- Geography: 2 explicit review-queue records (Nov 2025 Q23 key/content concern; Q26 provisional Unit I mapping). The live questions bank has 207 unique IDs, so the older PR summary of 200 total is stale; 500 questions across five papers remain untranscribed.
- Forensic Science: 8 review-queue records remain; the 86 provisional-unit matches are not being promoted automatically. Existing official-source/key checks are retained.
- Environmental Sciences: review queue empty; 300 unique records.
- Social Work: 396 unique records; review_flag=true on 373, all pending syllabus mapping; Dec 2019 100/100, Dec 2021/Jan 2022 96/100, Nov 2022 100/100, Nov 2023 100/100. Remaining transcription 204.
- Sanskrit staging discrepancy: canonical questions.json has 192 records (unique), while source_audit.json claims 850 transcribed questions and 108 pending review. The review queue file is empty and all 192 canonical records currently have review_flag=false; only 14 have syllabus_mapping_status=verified. answer_keys_staging.json explicitly contains 300 keys-only entries across five sessions, including SEP2018 Q44 marked Z/not evaluated, and mentions three further 50-question sessions (Oct 2010, Oct 2011, Oct 2014) whose question/key files were not available. The reported 550 staging count cannot be reconciled to the present files: do not invent missing question text or promote key-only entries.
- No flags were cleared automatically where source, official key, or syllabus evidence remained unresolved. Data discrepancies are recorded for reconciliation.


## 16 November 2026 — execution continuation (latest verified snapshot)

### Social Work (Code 25)
- Canonical question bank: 419 unique records; no duplicate IDs; every loaded record has four English options.
- December 2019: 100/100 transcribed and final-key parity complete.
- December 2021 / January 2022: 96/100 transcribed; Q32–Q35 remain untranscribed. No full-paper parity claim until the missing four are recovered.
- November 2022: 100/100 transcribed and final-key reconciled; 77 syllabus mapping review flags remain.
- November 2023: 100/100 transcribed and final-key reconciled; 100 syllabus mapping review flags remain.
- December 2024: Q1–Q23 transcribed from official PDF; all 23 match the official final key. Q24–Q100 remain.
- November 2025: 0/100 transcribed.
- Remaining Social Work transcription: 181 questions (Dec 2021 Q32–Q35 = 4; Dec 2024 Q24–Q100 = 77; Nov 2025 = 100). 396 of 419 records are review-only pending mapping/source gates.

### Geography (Code 24)
- Canonical question bank: 304 unique records; no duplicate IDs; all loaded records have four English options.
- November 2022: 100/100 questions now transcribed and visually checked; all 100 answers match the official final key. All 100 remain review-only pending official syllabus mapping.
- September 2018: Q1–Q6 transcribed and final-key matched; Q7–Q100 remain.
- November 2022 Q1–Q100 complete; remaining 396 geography questions are September 2018 Q7–Q100 (94), December 2021 (100), November 2023 (100), December 2024 (100), and two untranscribed November 2025 records.
- Existing September 2016 and August 2017 papers remain 50/50 each; November 2025 canonical bank has 98 records, with two review-only records separately queued.

### Environmental Sciences (Code 26)
- Canonical audit confirms 300/300 records across November 2023, December 2024 and November 2025; all 300 have source_verified=true, answer_key_verified=true, review_flag=false and syllabus_mapping_status=verified.
- Reconciled stale papers.json counters: each paper now records 100 loaded/source-verified questions and zero review flags. This was a manifest correction against canonical question-level records, not a new transcription claim.

### Sanskrit (Code 07) — reconciliation warning
- Canonical questions.json currently contains 192 records (99 November 2023, 93 November 2025). The separate answer_keys_staging.json contains 300 answer-key-only entries across five sessions; these are not question-text records and must not be counted as transcribed questions.
- The earlier audit/source_audit references 550 recovered staging questions, but the current questions_review_pending.json fetch is empty (0 bytes). The claimed 550-record review queue is therefore not confirmed in the actual file. Do not promote or count those 550 until the missing content is physically present and validated.

### Other review-only queues
- Gujarati: 36 separate review-only records; no duplicate IDs in canonical bank.
- History: 2 explicit syllabus-mapping holds (Q46 and Q48); keep them unmapped.
- Forensic Science: 8 separate review-only records remain; retain the syllabus-scope holds rather than forcing units.
- Geography: 2 separate November 2025 review-only records plus 100 November 2022 mapping holds and six September 2018 source/mapping review flags.
- Social Work: mapping/source review flags remain as listed above; no unsupported unit assignments made.

### CI / integration
- Latest PR #22 head checked: no associated commit status checks and no PR-triggered workflow runs returned. No Combined APK PASS is claimed.
- PR #22 remains open and unmerged. No merge authorization received.


## 17 November 2026 — Social Work Code 25 December 2021 Q32–Q35 recovered

- Pre-batch canonical audit: Social Work had 419 records; December 2021 / January 2022 had 96/100 questions, with only Q32–Q35 absent. The earlier manifest note also listed Q51–Q57 as missing, but the canonical question-number audit found those questions present; that stale note is corrected.
- Visually inspected the official GSET question-paper PDF, zero-based PDF page index 12. Transcribed English stems and all four options for Q32–Q35; no figures or tables occur in this range.
- Official FINAL answer-key parity: Q32 B, Q33 B, Q34 B, Q35 D — 4/4 exact matches.
- Official Code 25 syllabus mapping: Q32 and Q33 → Unit V (Research in Social Work); Q34 and Q35 → Unit VI (Administration, Welfare and Development Services). All four new records have source_verified=true, answer_key_verified=true, syllabus_mapping_status=verified, review_flag=false.
- After batch: Social Work canonical records 423 (before 419, +4); active 27 (before 23, +4); review-only 396 (unchanged); December 2021 is 100/100 transcribed. Remaining Social Work transcription is 177: December 2024 Q24–Q100 (77) and November 2025 Q1–Q100 (100). The other 96 December 2021 records remain review-only pending syllabus mapping, so the paper is not yet fully cleared for practice use.
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec21/dec2125.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec21/dec2125.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Next batch: Social Work Code 25, December 2024 Q24–Q31 (official question paper and final-key URLs resolve).
- The earlier planned Environmental Sciences November 2023 Q88–Q95 batch was not repeated: those canonical records already carry source_verified=true, answer_key_verified=true, review_flag=false and visual-source notes.
- PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q24–Q31 verified
- Pre-batch live canonical audit: Social Work had 423 records, 27 active and 396 review-only. December 2024 had Q1–Q23 transcribed; Q24–Q31 were absent. Total Social Work transcription remaining was 177 (December 2024 Q24–Q100: 77; November 2025 Q1–Q100: 100).
- Visually checked the official GSET December 2024 Social Work Paper-II scan on zero-based PDF page indexes 10 and 11. Q24–Q31 stems and all four English options match the scan; no figures or tables occur in this range. Gujarati-side text was not added.
- Official FINAL answer-key parity: Q24 C, Q25 A, Q26 B, Q27 D, Q28 A, Q29 D, Q30 C, Q31 B — 8/8 exact matches.
- Official Code 25 syllabus mapping: Q24 Unit II (Theories of Personality); Q25 Unit II (Human Behavior and Life Span Development); Q26–Q29 Unit III (Social Group Work); Q30 Unit II (Sociological Concepts / Social Groups); Q31 Unit IV (Community Organization). All eight records have source_verified=true, answer_key_verified=true, syllabus_mapping_status=verified and review_flag=false.
- After batch: Social Work canonical records 431 (before 423, +8); active 35 (before 27, +8); review-only 396 (unchanged). December 2024 is 31/100 transcribed, with Q1–Q23 still review-only pending mapping and Q32–Q100 untranscribed. Remaining Social Work transcription is 169: December 2024 Q32–Q100 (69) and November 2025 Q1–Q100 (100).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Next batch: Social Work Code 25, December 2024 Q32–Q39. No previously completed question was repeated.
- PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q32–Q39
- Pre-batch live canonical audit: 431 Social Work records; 35 active and 396 review-only. December 2024 Q1–Q31 were present; Q32–Q39 were absent. Previously committed December 2021 Q32–Q35 and December 2024 Q24–Q31 were not repeated.
- Visually inspected the official GSET December 2024 Social Work Paper-II scan: zero-based PDF page index 12 (Q32–Q35) and 13 (Q36–Q39). English stems and all four options were checked. No figures or tables occur in this range. Gujarati-side transcription was not added.
- Official FINAL answer-key parity: Q32 C, Q33 B, Q34 C, Q35 B, Q36 A, Q37 D, Q38 C, Q39 A — 8/8 exact matches.
- Syllabus review: Q33–Q39 mapped to official Code 25 Unit IV (community organization / development). Q32 (Elizabethan Poor Law) has source and key verification but the official syllabus does not explicitly name the Poor Law; Unit I is provisional only, so Q32 remains review-only with review_flag=true. No unsupported promotion.
- After batch: Social Work canonical records 439 (before 431, +8); active 42 (before 35, +7); review-only 397 (before 396, +1). December 2024 is 39/100 transcribed. Remaining Social Work transcription: 161 (December 2024 Q40–Q100 = 61; November 2025 Q1–Q100 = 100). December 2024 mapping state: 15 verified, 1 provisional, 24 pending/review-only.
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q32–Q39 b6bda72fb98f467b4920dcfa2b99f59c5c9d4f1b; retain Q32 review-only f642ddc46f338f16d64c3f8cd65cdc5d8263558f; paper metadata c68d867b28af777fa0dba37d614b44129da7466c and 743bcea86dd8249216e88ae017bff7cd0d6dc731. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q40–Q47. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q40–Q47
- Pre-batch canonical audit: 439 Social Work records (42 active / 397 review-only); December 2024 Q1–Q39 were present. Q40–Q47 were missing. No completed question was repeated.
- Retrieved the exact English stems and four options for Q40–Q47 from the official GSET December 2024 Social Work Paper-II PDF using targeted PDF extraction. No unreadable text was returned; Gujarati-side transcription was not added.
- Official FINAL answer-key parity: Q40 B, Q41 B, Q42 A, Q43 D, Q44 C, Q45 C, Q46 B, Q47 B — 8/8 exact matches.
- Official Code 25 syllabus mapping: Q40 → Unit IV (Social Work with Communities and Social Action / community practice); Q41–Q47 → Unit V (Research in Social Work: research problem, hypothesis, design, descriptive statistics, statistical tests, citing and paraphrasing). All eight records marked source_verified=true, answer_key_verified=true, syllabus_mapping_status=verified, review_flag=false.
- After batch: Social Work canonical records 447 (before 439, +8); active 50 (before 42, +8); review-only 397 (unchanged). December 2024 is 47/100 transcribed. Remaining Social Work transcription: 153 (December 2024 Q48–Q100 = 53; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 23 verified, 1 provisional (Q32), 24 pending (Q1–Q23 and Q32).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q40–Q47 cebb4c359f3eec28cc3f258c3efedf971fbeda16; paper manifest 046002642de75d882db4f6b017f6c3b28ed68d8d. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q48–Q55. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q48–Q55
- Pre-batch canonical audit: 447 Social Work records (50 active / 397 review-only); December 2024 Q1–Q47 were present. Q48–Q55 were missing. No completed question was repeated.
- Visually checked official GSET December 2024 Social Work Paper-II PDF pages: zero-based page index 16 (Q48), 17 (Q49–Q51), and 18 (Q52–Q55). English stems and all four options checked against the scan.
- Official FINAL answer-key parity: Q48 C, Q49 B, Q50 D, Q51 A, Q52 C, Q53 D, Q54 B, Q55 B — 8/8 exact matches.
- Official Code 25 syllabus mapping: Q48–Q50 → Unit V (Research in Social Work / statistical tests); Q51–Q53 and Q55 → Unit VI (Administration, Welfare and Development Services). Q54 (NITI Aayog chairperson) remains review-only: the official Code 25 syllabus does not explicitly mention NITI Aayog, so no forced mapping was assigned. All eight source and final-key checks are complete.
- After batch: Social Work canonical records 455 (before 447, +8); active 57 (before 50, +7); review-only 398 (before 397, +1). December 2024 is 55/100 transcribed. Remaining Social Work transcription: 145 (December 2024 Q56–Q100 = 45; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 30 verified, 1 provisional (Q32), 25 pending/review-only (Q1–Q23, Q32 and Q54).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q48–Q55 cee11019257ba03e1f18db4428037ce6b55b9382; paper manifest 8588f363619154c5360eda8a5344481d124bbf41. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q56–Q63. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q56–Q63
- Pre-batch canonical audit: 455 Social Work records (57 active / 398 review-only); December 2024 Q1–Q55 were present. Q56–Q63 were missing. No completed question was repeated.
- Visually checked official GSET December 2024 Social Work Paper-II PDF pages: zero-based page index 18 (Q56), 19 (Q57–Q60), and 20 (Q61–Q63). English stems and all four options checked against the scan.
- Official FINAL answer-key parity: Q56 D, Q57 A, Q58 C, Q59 D, Q60 C, Q61 A, Q62 C, Q63 A — 8/8 exact matches.
- Official Code 25 syllabus mapping: Q57–Q59 and Q62 → Unit VI (Administration, Welfare and Development Services). Q56 (productivity), Q60 (co-operative movement), Q61 (Problems of Social Policy / Richard Titmuss) and Q63 (T. H. Marshall / citizenship in social policy) remain review-only because the official syllabus does not explicitly cover these specific topics. No forced units.
- After batch: Social Work canonical records 463 (before 455, +8); active 61 (before 57, +4); review-only 402 (before 398, +4). December 2024 is 63/100 transcribed. Remaining Social Work transcription: 137 (December 2024 Q64–Q100 = 37; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 34 verified, 1 provisional (Q32), 29 pending/review-only (Q1–Q23, Q32, Q54, Q56, Q60, Q61 and Q63).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q56–Q63 722b84cf7bed41af59ba0b7549b8ecafa37a4410; paper manifest d9210bfc09a1362555b3191a521b35cdad3cc249. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q64–Q71. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q64–Q71
- Pre-batch canonical audit: 463 Social Work records (61 active / 402 review-only); December 2024 Q1–Q63 were present. Q64–Q71 were missing. No completed question was repeated.
- Visually checked official GSET December 2024 Social Work Paper-II PDF pages: zero-based page index 20 (Q64–Q65), 21 (Q66–Q69), and 22 (Q70–Q71). English stems and all four options checked against the scan.
- Official FINAL answer-key parity: Q64 C, Q65 A, Q66 B, Q67 D, Q68 B, Q69 C, Q70 C, Q71 B — 8/8 exact matches.
- Official Code 25 syllabus mapping: Q66, Q68 and Q69 → Unit VI (Administration, Welfare and Development Services / history, coordination, development services). Q64, Q65, Q67, Q70 and Q71 remain review-only because the official syllabus does not explicitly identify the institutional-redistributive model, social-policy analysis, policy statements, democratic sources of social policy or Article 38. No forced units.
- After batch: Social Work canonical records 471 (before 463, +8); active 64 (before 61, +3); review-only 407 (before 402, +5). December 2024 is 71/100 transcribed. Remaining Social Work transcription: 129 (December 2024 Q72–Q100 = 29; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 37 verified, 1 provisional (Q32), 34 pending/review-only (Q1–Q23, Q32, Q54, Q56, Q60, Q61, Q63–Q65, Q67, Q70 and Q71).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q64–Q71 cd9110893991245411779329ee78ae14e1be102a; paper manifest 61b19e8b997ec2fb09013895deb1f4bb00c61dab. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q72–Q79. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q72–Q79
- Pre-batch canonical audit: 471 Social Work records (64 active / 407 review-only); December 2024 Q1–Q71 were present. Q72–Q79 were missing. No completed question was repeated.
- Visually checked official GSET December 2024 Social Work Paper-II PDF pages: zero-based page index 22 (Q72–Q73), 23 (Q74–Q76), and 24 (Q77–Q79). English stems and all four options checked against the scan.
- Official FINAL answer-key parity: Q72 B, Q73 B, Q74 C, Q75 C, Q76 C, Q77 B, Q78 B, Q79 C — 8/8 exact matches.
- Source transcription and answer-key verification are complete for all eight. All eight remain review-only because exact mapping to an explicit official Code 25 syllabus topic has not been established. No unsupported syllabus units assigned.
- After batch: Social Work canonical records 479 (before 471, +8); active 64 (unchanged); review-only 415 (before 407, +8). December 2024 is 79/100 transcribed. Remaining Social Work transcription: 121 (December 2024 Q80–Q100 = 21; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 37 verified, 1 provisional (Q32), 42 pending/review-only (including Q1–Q23, Q32, Q54, Q56, Q60, Q61, Q64–Q65, Q67, Q70–Q79).
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q72–Q79 1398aad994a127a9b67b4d90765ccc5abf3f90a6; paper manifest 0f01585987b933da7307ea7e03d96bb32fbb29c0. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q80–Q87. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 Q80–Q85
- Pre-batch canonical audit: 479 Social Work records (64 active / 415 review-only); December 2024 Q1–Q79 were present. Q80–Q85 were missing. No completed question was repeated.
- Visually checked official GSET December 2024 Social Work Paper-II PDF: Q80 on zero-based page index 24 and Q81–Q85 on index 25. English stems and all four options checked against the scan.
- Official FINAL answer-key parity: Q80 B, Q81 B, Q82 C, Q83 B, Q84 B, Q85 C — 6/6 exact matches.
- Source transcription and final-key verification are complete for all six. All six remain review-only pending exact mapping to explicit Code 25 syllabus topics; no unsupported units assigned.
- After batch: Social Work canonical records 485 (before 479, +6); active 64 (unchanged); review-only 421 (before 415, +6). December 2024 is 85/100 transcribed. Remaining Social Work transcription: 115 (December 2024 Q86–Q100 = 15; November 2025 Q1–Q100 = 100). December 2024 mapping counters: 37 verified, 1 provisional (Q32), 48 pending/review-only.
- Official sources: question paper https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf; FINAL answer key https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf; syllabus https://gujaratset.ac.in/assets/syllabus/25.pdf.
- Data commits: questions Q80–Q85 759fa0a2deec286e9bb3ed588aef881b431d0b80; paper manifest 98539a2cc12afad3d45c814dd72df0e129fef1c1. Checkpoint commit recorded separately after this note.
- Next batch: Social Work Code 25, December 2024 Q86–Q93. PR #22 remains open and unmerged. No unrelated subject, Code 01, Code 02, Code 28, Paper-I or app UI changed. No CI or Combined Debug APK PASS is claimed.


## 2026-11-18 — Social Work Code 25 December 2024 syllabus-mapping batch
- Re-audited the existing December 2024 Q64–Q85 records against the official GSET Code 25 syllabus: https://gujaratset.ac.in/assets/syllabus/25.pdf
- Promoted 18 already source-verified and final-key-verified records to active using explicit syllabus matches: Q64, Q65, Q67, Q70 → Unit VII; Q71–Q75 and Q77–Q80 → Unit VIII; Q81–Q85 → Unit IX.
- Q76 (Panchayati Raj Institutions) remains review-only because the syllabus does not name this topic explicitly; no unit was forced. All other unresolved questions remain review-only.
- December 2024 Social Work now has 85/100 question stems transcribed, 55 active, and 30 review-only for syllabus mapping. Q86–Q100 remain untranscribed. The official final answer-key parity remains verified for the 85 transcribed records; full 100-question parity is not claimed.
- No Gujarati-side transcription was added in this batch. No other subject, Paper-I, Code 01, Code 02 or Code 28 was modified. PR #22 remains unmerged; no CI or APK pass is claimed.


## Social Work Code 25 — November 2022 syllabus mapping batch (18 November 2026)
- Official source: https://gujaratset.ac.in/assets/syllabus/25.pdf
- 59 of 77 previously unmapped questions (Q27, Q29–Q64 except Q65, Q66–Q76, Q88–Q92, Q94–Q97, Q99–Q100) were assigned only where the official syllabus text gave a direct topic match.
- Unit distribution: Unit II: 2; Unit V: 1; Unit VI: 2; Unit VII: 3; Unit VIII: 26; Unit IX: 11; Unit X: 14.
- These 59 records already had source_verified=true, answer_key_verified=true, and four English options; those values and answers were not changed. Each mapped record now has syllabus_mapping_status=verified, official syllabus source, unit fields, and review_flag=false.
- 18 remain review-only: Q24–Q26, Q28, Q65, Q77–Q87, Q93, Q98. No unsupported mappings were assigned.
- Commits: questions `18d3d27bbeda2983b55bc2ca12bae05426deff71`; manifest `5e059d957bb23e19ee406089f8fb7f0aa623cd55`; manifest note correction `5e531efd855c9be21d6a94da69803519779df8e1`.


## Social Work Code 25 — December 2021 syllabus mapping batch (18 November 2026)
- Official syllabus used: https://gujaratset.ac.in/assets/syllabus/25.pdf
- 95 additional questions were mapped in this batch: 94 first-pass mappings plus Q56 (Article 24 / child labour) after a final explicit constitutional check. Together with the earlier Q32–Q35, 99/100 questions now have verified unit mappings.
- Unit distribution of the 95 new mappings: Unit I: 10; Unit II: 7; Unit III: 6; Unit IV: 3; Unit V: 9; Unit VI: 1; Unit VII: 11; Unit VIII: 32; Unit IX: 9; Unit X: 13.
- Q31 (a general search-engine question) remains review-only because the official Code 25 syllabus provides no defensible unit match.
- Existing source and official final-key checks were preserved; answer letters and question text were not changed. All mapped records were already source_verified and answer_key_verified with four English options.
- Commits: questions `0484b00cdd1b2d8b12bb76878eb0d26ff129244a`, `ee79d05e7076ab431dae34a111bf9a346889337c`; manifest `2761592ce66aef3a25852168bd595620333536d7`, `18473a8f647b944d58b3dcbf89665133f55bb217`.


## Social Work Code 25 — November 2023 syllabus mapping batch (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/25.pdf
- 99/100 questions received verified mappings across Units I–X. Unit distribution: I: 9; II: 14; III: 5; IV: 10; V: 10; VI: 9; VII: 10; VIII: 8; IX: 13; X: 11.
- Q21 (“bug in the ear” / field-work supervision) remains review-only because the Code 25 syllabus does not explicitly identify field-work supervision as a separate topic. No unsupported mapping was assigned.
- Existing source-page checks, official final-key checks, question text, options and answer letters were preserved; all 99 mapped records were already source_verified and answer_key_verified with four English options.
- Commits: questions `217c9a9f558fe241e82f291a06ffbc2f5c8719b6`; manifest `b8244c3d72903af9049c91933c93e137064ca373`.


## Social Work Code 25 — December 2019 syllabus mapping completed (18 November 2026)
- Official Code 25 syllabus: https://gujaratset.ac.in/assets/syllabus/25.pdf
- 100/100 December 2019 questions now have explicit mappings across Units I–X; 100 Active, 0 review-only for syllabus mapping.
- All 100 records already had source_verified=true, answer_key_verified=true and four English options. Question stems, options and answer letters were not modified.
- Manifest: unit_mapping_verified_count=100; unit_mapping_pending_count=0; review_flags_remaining_count=0; status=source_verified_final_key_reconciled_syllabus_mapped.
- Questions file SHA after update: `0ae5e460fbc5fa76bd9b988d3e05cd45a849668f`; manifest SHA: `e715e677f756cab6d046165d738ec145c562d1aa`.


## Social Work Code 25 — November 2022 mapping review continued (18 November 2026)
- 16 additional questions mapped to explicit topics in the official Code 25 syllabus: Q25, Q28, Q65, Q77–Q87, Q93 and Q98.
- November 2022 now has 98/100 verified mappings. Q24 (MOOC) and Q26 (image-file extensions) remain review-only because these are not explicitly identified as Social Work syllabus topics.
- Source and official final-key flags were already verified for all mapped records; answer letters, stems and options were not changed.
- Commits: questions `c1868a3cdff92941824c28eaf51e26acf5d0f9ba`; manifest `f6f32d10d9a610463f0984d4f4fd7c28cc8c824d`.


## Social Work Code 25 — December 2024 syllabus mapping review (18 November 2026)
- 29 additional questions mapped to the official Code 25 syllabus: Q1–Q23, Q32, Q54, Q60, Q61, Q63 and Q76.
- December 2024 now has 84/85 verified mappings. Q56 (productivity as a mathematical input-output relationship) remains review-only because no exact syllabus topic is explicit.
- Q1–Q85 source verification and official FINAL answer-key parity remain unchanged; no question text, options or answer letters were modified. Q86–Q100 are still not transcribed.
- Commits: questions `910f4817af60ed06472eb3453f8742e282ac95da`; manifest `24e67f555d1090b5eef6408cf7c803d3bd4e280d`.


## Social Work Code 25 — December 2024 Q86–Q93 source transcription (18 November 2026)
- Official question paper: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf. Visually checked all English stems and four options: Q86–Q90 on zero-based PDF page index 26, Q91–Q92 on index 27, and Q93 on index 28. No figures/tables in this range; Gujarati text was not transcribed.
- Official FINAL answer key: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf. Exact stored-key matches: Q86 A, Q87 B, Q88 B, Q89 C, Q90 B, Q91 A, Q92 C, Q93 A (8/8). The official key was retained as authoritative.
- Official Code 25 syllabus: https://gujaratset.ac.in/assets/syllabus/25.pdf. Mappings: Q86–Q87 Unit II; Q88–Q91 Unit VIII; Q92–Q93 Unit X. All eight received explicit unit mappings. Q91 remains review-only because option A appears to describe the SC/ST (Prevention of Atrocities) Act more closely than the Protection of Civil Rights Act. Q92 remains review-only because both options B and C describe important purposes of the Juvenile Justice Act and the wording/key needs expert interpretation. Q56 remains review-only for mapping uncertainty.
- After batch: Social Work canonical question file 493 records total; December 2024 is 93/100 transcribed, with 92/93 mapped and three review flags in that paper (Q56, Q91, Q92). December 2024 Q94–Q100 and November 2025 Q1–Q100 remain untranscribed (107 questions total).
- Commits: questions `bfea560d530cdaf478bea27a61459e1cd8bf2ac7`; paper manifest `67d8f5895c3225a0109c6989595d8bd10c3fe622`.
- No other subject, Paper-I, Code 01, Code 02, Code 28, or app UI changed. PR #22 remains open and unmerged. CI/Combined APK status must be checked separately; no APK PASS is claimed.
- Next batch: Social Work Code 25, December 2024 Q94–Q100.


## Social Work Code 25 — December 2024 Q94 (18 November 2026)
- Official GSET December 2024 Social Work paper: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2425.pdf. Q94 stem and all four options visually checked on zero-based PDF page index 28; no figure/table. Gujarati-side text not transcribed.
- Official FINAL key: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2425.pdf. Q94 = C; stored answer matches exactly.
- Official Code 25 syllabus: https://gujaratset.ac.in/assets/syllabus/25.pdf. Q94 mapped to Unit X (Social Work with Families; family dynamics and interventions).
- December 2024 now 94/100 transcribed; 93 mapped. Review-only: Q56 (mapping), Q91 and Q92 (official-key/question wording requires subject-expert review). Q95–Q100 remain untranscribed: attempts to render official PDF page indexes 29–31 timed out, and direct PDF retrieval failed. No transcription or visual verification is claimed for Q95–Q100.
- Commits: questions `7d9ac14059180b0ee7480a2134d0572abd9deaa1`; paper manifest `910a49a882300fbcae0895fe2ca718ee24ba4dbd`.
- PR #22 remains open and unmerged. No other subject, Paper-I, Code 01, Code 02, Code 28 or app UI changed. No CI/Combined APK PASS is claimed.
- Next: continue Q95–Q100 only after official PDF pages are retrievable; otherwise switch to another independently verifiable subject batch.


## Sanskrit Code 07 — November 2023 Q1–Q8 official syllabus mapping (18 November 2026)
- Official syllabus reviewed: https://gujaratset.ac.in/assets/syllabus/07.pdf (printed pages 4–5; PDF indexes 3–4).
- Mapped eight already source-verified and final-key-verified questions without changing stems, options or answers: Q1 Unit VIII (Kavyashastra / Kavyalakshana / Alankara); Q2 Unit VI (Bhartrihari / Vakyapadiya); Q3–Q8 Unit VI (Paninian grammar, case usage, Anga-sanjna, Agama, Sandhi and Samasa).
- Sanskrit canonical file: 192 records. Verified syllabus mappings increased from 14 to 22; pending official mappings decreased from 178 to 170. No question was promoted or marked source-verified by this mapping-only batch; no answer or transcription changed.
- Questions commit: `41ac81955e5bcb4881c7d3666e95daa020d89904`. PR #22 remains open and unmerged. Other subjects and protected areas remain untouched.
- Next mapping batch: Sanskrit November 2023 Q9–Q16, subject to exact fit in the official syllabus.


## Sanskrit Code 07 — November 2023 Q9–Q16 official syllabus mapping (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. Mapped eight existing source/key-verified records without changing question text, options or answers: Q9–Q10 Unit VI (Paninian grammar); Q11 Unit VIII (Chhanda); Q12 Unit IV (Patanjali Yoga Sutra); Q13 Unit I (Vedic literature); Q14 Unit IV (Sankhya); Q15 Unit IX (epigraphy/Brahmi/Ashoka); Q16 Unit VIII (Kavyaprakasha and Kavyaprayojana).
- Sanskrit mappings: 22 → 30 verified; pending official syllabus mappings: 170 → 162 (192 canonical records). No source verification or question promotion was claimed.
- Questions commit: `de587314821beb4dd1596db52f60f841565b8ee5`. PR #22 remains open and unmerged; other subjects and protected areas untouched.
- Next mapping batch: Sanskrit November 2023 Q17–Q24, only where an explicit official syllabus fit exists.


## Sanskrit Code 07 — November 2023 Q17–Q24 official syllabus mapping (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. Mapped eight source/key-verified records without changing text/options/answers: Q17 Unit VIII (Buddhacharita); Q18–Q19 Unit II (Vedic/Rigvedic literature); Q20 Unit I (Vedanga Shiksha); Q21 Unit II (Rkpratishakhya); Q22 Unit VI (Karaka/Paninian grammar); Q23 Unit II (Brihadaranyaka Upanishad); Q24 Unit VIII (Bharata Natyashastra/Rasa).
- Sanskrit verified syllabus mappings: 30 → 38; pending: 162 → 154 (192 canonical records). No source verification or activation was claimed.
- Questions commit: `9a0b3e002e7780b3a3c6b541084cfa357d4a61fc`. PR #22 remains open and unmerged; all other subjects and protected areas untouched.
- Next mapping batch: Sanskrit November 2023 Q25–Q32, only where explicit syllabus coverage is present.


## Sanskrit Code 07 — November 2023 Q25–Q32 official syllabus mapping (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. Mapped eight source/key-verified records without modifying question text/options/answers: Q25 Unit I (Vedanga Shiksha); Q26 Unit VIII (Sanskrit drama); Q27 Unit IX (Puranic literature); Q28 Unit VI (grammar); Q29 Unit VIII (Chhanda); Q30 Unit IV (Nyaya philosophy); Q31 Unit VIII (Nalachampu); Q32 Unit VIII (Vakroktijivita/Kuntaka).
- Sanskrit verified syllabus mappings: 38 → 46; pending: 154 → 146 (192 canonical records). No source verification or activation was claimed.
- Questions commit: `35f28c46007c305c9686eaaf5bac8caf54ed94d9`. PR #22 remains open and unmerged; other subjects and protected areas untouched.
- Next mapping batch: Sanskrit November 2023 Q33–Q40, only where explicit syllabus coverage exists.


## Sanskrit Code 07 — November 2023 Q34–Q40 official syllabus mapping (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. Mapped seven existing source/key-verified records without changing text/options/answers: Q34–Q37 Unit IV (Vedanta and Sankhya); Q38–Q40 Unit VIII (Kavyashastra, Alankara and Rasa theory).
- Q33 is absent from the current canonical Sanskrit JSON for this session; it was not created or inferred. It remains a separate data-completeness check.
- Sanskrit verified mappings: 46 → 53; pending: 146 → 139 (192 canonical records). No source verification or activation was claimed.
- Questions commit: `5825f2e4b8ff650f8540a9229221d554cb8b1f78`. PR #22 remains open and unmerged; all other subjects and protected areas untouched.
- Next mapping batch: Sanskrit November 2023 Q41–Q48, only where exact syllabus coverage exists.


## Sanskrit Code 07 — November 2023 Q41–Q48 official syllabus mapping (18 November 2026)
- Official syllabus: https://gujaratset.ac.in/assets/syllabus/07.pdf. Mapped eight source/key-verified records without modifying question text/options/answers: Q41 Unit VIII (Venisamhara); Q42 Unit X (Yajnavalkya Smriti, Vyavahara); Q43–Q45 Unit X (historical epigraphy); Q46 Unit VIII (dramatic theory); Q47 Unit VIII (Uttararamacharita); Q48 Unit VIII (Ratnavali).
- Sanskrit verified mappings: 53 → 61; pending: 139 → 131 (192 canonical records). Q33 remains absent from the current canonical JSON; it was not fabricated.
- Questions commit: `01ca95d8e02286210103c89b3c7ad51e2b003e57`. PR #22 remains open and unmerged; all other subjects and protected areas untouched.
- Next mapping batch: Sanskrit November 2023 Q49–Q56, subject to exact syllabus coverage.
