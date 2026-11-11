# GSET Paper-II — Seven-subject checkpoint (2026-11-11)

Branch: `app/import-updated-subject-banks-2026-11-10`
Pull request: https://github.com/dhavalkhant3-web/gset-test-series/pull/22
Status: Open; NOT MERGED. Do not modify unrelated subjects, Paper-I UI, or Mathematical Sciences Code 01.

| Code | Subject | Active records | Review-only records | Outstanding work |
|---|---|---:|---:|---|
| 06 | Gujarati | 29 | 371 | Independent PDF/final-key re-audit of active records; review 371; syllabus mapping |
| 07 | Sanskrit | 114 | 736 | Restored 736-record staging file; source review and syllabus mapping |
| 08 | History | 0 | 50 | Official PDF proofreading of 50, including two review-required; syllabus mapping |
| 24 | Geography | 0 | 200 | Official PDF proofreading of 200; syllabus mapping |
| 25 | Social Work | 0 | 0 | 600 staged answer-key entries are NOT question records; transcribe official question papers |
| 26 | Environmental Sciences | 87 | 213 | Source review of 213; official syllabus mapping |
| 27 | Forensic Science | 84 | 216 | Source review of 216; official syllabus mapping |

## Checks and cautions
- Gujarati JSON lists 29 active + 371 review-only, with no duplicate IDs within either file; registry and source audit reconciled. No new independent PDF verification was performed in that reconciliation.
- Sanskrit `questions_review_pending.json` was restored from the consolidated 850-record staging file, excluding the 114 IDs already active. Its Git blob exists on this branch (1,144,178 bytes). The GitHub connector may fail to fetch the large file in one response; do not infer it is empty.
- Environment and Forensic subject counts reflect earlier source-review batches committed to this branch. Final release still requires independently reproducible official-source verification and official syllabus mapping.
- PR #22's Hindu Studies Code 28 validation/Debug APK workflow failed before Android build due to **existing unrelated** metadata mismatches: 8 provisional and 16 pending mappings in actual records versus 24 provisional and 0 pending in metadata; three paper-level count mismatches; source_verified and status text mismatches. Do not modify Code 28 without authorization; do not claim a new APK PASS.
- No PR merge authorized. Review-only content must not be activated to satisfy numeric targets.

## Next subject-wise steps
1. Gujarati: check official PDF/final key for remaining December 2021 Q30–Q100, preserve original spellings/figures, and activate only fully evidenced records.
2. Sanskrit: audit 736 restored records and review-required items, including official non-evaluated keys.
3. History and Geography: compare source PDF page-by-page, then final key, then syllabus mapping.
4. Social Work: transcribe question papers; do not convert answer keys into fake questions.
5. Environmental Sciences and Forensic Science: finish November 2023 paper, then other years, with visual source evidence and key parity.
6. Run subject-level validation and combined APK CI when existing unrelated Code 28 blocker is addressed separately with authorization.
