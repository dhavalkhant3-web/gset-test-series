# GSET Paper-II — Seven-subject checkpoint (2026-11-11, refreshed)

Repository: https://github.com/dhavalkhant3-web/gset-test-series
Branch: `app/import-updated-subject-banks-2026-11-10`
Pull request: https://github.com/dhavalkhant3-web/gset-test-series/pull/22
Latest inspected PR head: `c0f680fe2ce3f409f4160ed03f4ec92daea1d866`
Status: Open; NOT MERGED. Do not modify unrelated subjects, Paper-I UI, Mathematical Sciences Code 01, or Code 28.

## Current counts

| Code | Subject | Active | Staged review-only | Not yet transcribed |
|---|---|---:|---:|---:|
| 06 | Gujarati | 29 | 371 | 0 |
| 07 | Sanskrit | 114 | 736 | 0 |
| 08 | History | 49 | 1 | 0 |
| 24 | Geography | 50 | 150 | 500 |
| 25 | Social Work | 0 | 0 | 600 |
| 26 | Environmental Sciences | 87 | 213 | 0 |
| 27 | Forensic Science | 84 | 216 | 0 |
| **Total** | | **413** | **1,687** | **1,100** |

Expected question records across these seven subjects: 3,200. Active: 413. Remaining work: 2,787 records, consisting of 1,687 already transcribed but review-only and 1,100 not yet transcribed. Social Work's 600 official answer-key entries are source material only, not question records.

## Latest completed source work

### History Code 08 — September 2016
- All 50 questions visually checked against official PDF: https://gujaratset.ac.in/assets/papers/paperII/sept16/sept1608.pdf
- All 50 answer letters compared with official final/corrected key: https://gujaratset.ac.in/assets/anskey/paperII/sept16/sept1608.pdf
- 49 active, 1 pending (Q48).
- Q48 conflict: official key A, but printed question asks author of The Wealth of Nations and option D is Adam Smith. Official A preserved; Q48 stays review-only.
- Syllabus mapping from official https://gujaratset.ac.in/assets/syllabus/08.pdf: 43 verified, 5 provisional, 1 pending (Q46).

### Geography Code 24 — September 2016
- All 50 questions visually checked against official PDF: https://gujaratset.ac.in/assets/papers/paperII/sept16/sept1624.pdf
- All 50 answer letters compared with official final/corrected key: https://gujaratset.ac.in/assets/anskey/paperII/sept16/sept1624.pdf
- 50 active; no review flags for this paper.
- Syllabus mapping from official https://gujaratset.ac.in/assets/syllabus/24.pdf: 47 verified, 3 provisional, 0 pending.
- OCR corrections recorded: Q2 Carbon Dioxide, Q33 Purvanchal, Q41 Datum plane.
- Other Geography backlog: 150 staged questions remain review-only; 500 expected questions across five papers are not yet transcribed.

### Other subjects
- Gujarati: 29 active / 371 review-only; registry reconciled with JSON. Active records still require independent source-provenance re-audit.
- Sanskrit: 114 active / 736 review-only; 736 records restored from consolidated staging. Connector may fail fetching the large pending file in one response; Git blob exists.
- Environmental Sciences: 87 active / 213 review-only; official syllabus mapping pending.
- Forensic Science: 84 active / 216 review-only; official syllabus mapping pending.
- Social Work: 600 answer-key entries staged across six papers; no question text transcribed and no active questions.

## CI / merge safety
- PR #22 remains open and unmerged.
- Latest Public Administration bank validation run was successful; it is not a combined Android build.
- Hindu Studies Code 28 Validation and Debug APK workflow still fails due to unrelated existing Code 28 metadata mismatches (actual provisional/pending mappings differ from metadata, paper-level mapping counts stale, registry source_verified/status mismatch). Do not alter Code 28 without authorization.
- Do not claim a new combined Debug APK PASS. No PR merge authorized.
- Keep all unverified records review-only. Official final keys are authoritative; if key conflicts with source question, preserve the key and flag for expert review.

## Next work
1. Continue Geography: source-review remaining 150 staged questions, then transcribe the remaining 500 questions from the five listed papers.
2. Continue Gujarati and Sanskrit source verification and official syllabus mappings.
3. History: resolve Q48 with subject expert; map Q46 and review provisional mappings.
4. Social Work: transcribe 600 questions from official question-paper PDFs; do not convert answer keys into fake question records.
5. Environmental Sciences and Forensic Science: complete remaining source reviews and official syllabus mapping.
6. Re-run subject validators and combined Debug APK only after the unrelated Code 28 CI blocker is resolved under explicit authorization.
