# GSET Paper-II — Seven-subject checkpoint (2026-11-13, refreshed)

Repository: https://github.com/dhavalkhant3-web/gset-test-series
Branch: `app/import-updated-subject-banks-2026-11-10`
Pull request: https://github.com/dhavalkhant3-web/gset-test-series/pull/22
Status: Open; NOT MERGED. Do not modify unrelated subjects, Paper-I UI, Mathematical Sciences Code 01, or Code 28.

## Current counts

| Code | Subject | Active | Staged review-only | Not yet transcribed |
|---|---|---:|---:|---:|
| 06 | Gujarati | 97 | 303 | 0 |
| 07 | Sanskrit | 130 | 720 | 0 |
| 08 | History | 50 | 0 | 0 |
| 24 | Geography | 107 | 93 | 500 |
| 25 | Social Work | 0 | 0 | 600 |
| 26 | Environmental Sciences | 87 | 213 | 0 |
| 27 | Forensic Science | 84 | 216 | 0 |
| **Total** | | **555** | **1,545** | **1,100** |

Expected question records across these seven subjects: 3,200. Active: 555. Remaining work: 2,645 records, consisting of 1,545 transcribed but review-only and 1,100 not yet transcribed. Social Work's 600 official answer-key entries are source material only, not question records.

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
- Remaining Geography: 100 staged questions (November 2025; all 100 final-key letters reconciled, source visual review pending); 500 expected questions across five other listed papers not yet transcribed.

- November 2025: Q1–Q7 visually checked against the official question-paper PDF (Q1–Q3 printed page 3; Q4–Q7 printed page 4). All seven English stems and four options match; final-key letters D, B, D, B, A, D, B match 7/7; syllabus mappings verified to Units VI, V, VI, V, X, IV, VI respectively. Seven records promoted to active; Q8–Q100 remain review-only (93). Official paper: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; final key: https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; syllabus: https://gujaratset.ac.in/assets/syllabus/24.pdf.

### Other subjects
- Gujarati: live JSON contains 97 active / 303 review-only (400 total); 97 active records are source-verified and all 400 question-level syllabus mappings are recorded as verified.
- Sanskrit: live JSON contains 130 active / 720 review-only (850 total); the 720 pending records remain review-only.
- Environmental Sciences: 87 active / 213 review-only; official syllabus mapping pending.
- Forensic Science: 84 active / 216 review-only; 300/300 official final-key entries match. The official Code 27 syllabus is now registered; 299 question records have provisional unit matches and one item (November 2025 Q47, forensic engineering scope) remains pending subject-expert review. Source-review and activation statuses are unchanged.
- Social Work: 600 answer-key entries staged across six papers; no question text transcribed and no active questions.

## CI / merge safety
- PR #22 remains open and unmerged.
- Public Administration bank validation has been passing; it is not a combined Android build.
- Hindu Studies Code 28 Validation and Debug APK workflow still fails due to unrelated existing Code 28 metadata mismatches (actual provisional/pending mappings differ from metadata, paper-level mapping counts stale, registry source_verified/status mismatch). Do not alter Code 28 without authorization.
- Do not claim a new combined Debug APK PASS. No PR merge authorized.
- Keep all unverified records review-only. Official final keys are authoritative; if key conflicts with source question, preserve the key and flag for expert review.

## Next work
1. Geography: continue November 2025 visual verification from Q8 onward (Q1–Q7 complete; 93 remain review-only). PDF page indexes 2–3 rendered; page index 4 timed out once and should be retried page-by-page. Five additional papers (500 questions) remain untranscribed.
2. Continue Gujarati and Sanskrit source verification and official syllabus mappings.
3. History: review only the two pending syllabus placements (Q46 and Q48); question text and final-key checks are complete.
4. Social Work: transcribe 600 questions from official question-paper PDFs; do not convert answer keys into fake question records.
5. Environmental Sciences and Forensic Science: complete remaining source reviews and official syllabus mapping.
6. Re-run subject validators and combined Debug APK only after the unrelated Code 28 CI blocker is resolved under explicit authorization.


## 2026-11-13 — Live seven-subject count reconciliation and Geography Q1–Q7 source batch
- Reconciled active and review-only counts directly from the seven subject JSON files at the pre-batch branch head. Before: 548 active, 1,552 review-only, 1,100 not transcribed. After this batch: 555 active, 1,545 review-only, 1,100 not transcribed. The corrected table above supersedes stale checkpoint counts for Gujarati, Sanskrit, and History.
- Geography Code 24 November 2025 Q1–Q7: visually checked English stems and all four English options against official PDF printed pages 3–4 (PDF page indexes 2–3). Final key D, B, D, B, A, D, B matches 7/7; session parity remains 100/100. No figures/tables occur in this range. Gujarati-side text was not populated in these English-only records.
- Official syllabus mappings: Q1 VI, Q2 V, Q3 VI, Q4 V, Q5 X, Q6 IV, Q7 VI. All seven promoted to active; Q8–Q100 remain review-only (93).
- Official sources: https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2524.pdf ; https://gujaratset.ac.in/assets/syllabus/24.pdf
- One attempt to render PDF page index 4 timed out; no verification beyond Q7 is claimed. No other subject, Paper-I, Code 01, Code 28, or Physical Sciences Code 02 changed. PR #22 remains unmerged; no CI/APK pass is claimed.
