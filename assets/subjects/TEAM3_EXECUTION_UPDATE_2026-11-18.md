# Team 3 execution update — 2026-11-18

Scope: Sanskrit (Code 07), Environmental Sciences (Code 26), and validation evidence only. This report reflects PR #22 head after the three metadata reconciliation commits.

## Sanskrit Code 07 — canonical ID reconciliation

Directly parsed:
- `questions.json`: 192 records, 192 unique IDs.
- `questions_review_pending.json`: 658 records, 658 unique IDs.
- Active/review overlap: 0 IDs; duplicate IDs in review queue: 0.
- Union: 850 unique question records.
- Review queue: 108 `source_verified=true`, 550 `source_verified=false`; all 658 retain `review_flag=true`.
- Review queue answer-key status: 456 verified, 202 unverified.
- English option arrays: all 658 review records have four options; no empty stems found.
- Recovered set: 550 records, all remain review-only and source-unverified. No source-verification promotion was made.
- Five answer-key-only sessions contain 300 key entries. These are not question records and remain separate.

The earlier 704 review-queue counter is stale. The live canonical queue is 658.

## Sanskrit syllabus mappings

Live canonical totals:
- Verified: 290 (184 active + 106 review-only).
- Pending official syllabus mapping: 560 (8 active + 552 review-only).
- The 8 active unresolved IDs are:
  - GSET-SAN07-NOV2023-Q080
  - GSET-SAN07-NOV2023-Q092
  - GSET-SAN07-NOV2025-Q015
  - GSET-SAN07-NOV2025-Q029
  - GSET-SAN07-NOV2025-Q040
  - GSET-SAN07-NOV2025-Q071
  - GSET-SAN07-NOV2025-Q079
  - GSET-SAN07-NOV2025-Q087

No unit was guessed or assigned: the official Code 07 syllabus PDF was reachable as a PDF but its page text could not be extracted in this execution, so those 8 mappings remain pending.

## Environmental Sciences Code 26 — second-pass register

Direct canonical parse:
- `questions.json`: 300 records, 300 unique IDs.
- `questions_review_pending.json`: empty array.
- All 300 canonical records currently have `source_verified=true`, `answer_key_verified=true`, `review_flag=false`, and verified syllabus mapping.
- The supplied v3 staging register identifies 291 records as `key_verified_proofread_pass1` and 9 as `key_verified_visual_checked`.
- Therefore 291 is an independent second-pass proofreading backlog, not a review-queue count. No second-pass completion is claimed in this update.

The old registry statement of 95 active / 205 review-only and the old note of 213 review-only records did not match the live canonical files. Registry counters were corrected to 300 loaded / 0 review-queue, while retaining a separate 291 second-pass pending counter and subject-level `source_verified=false` gate.

## Registry and audit counter reconciliation

Updated only:
- `assets/subjects/sanskrit/source_audit.json`
- `assets/subjects/environmental_sciences/source_audit.json`
- The Code 07 and Code 26 entries in `assets/subjects/subjects.json`

No question text, answer, option, syllabus unit, or review flag was changed. No other subject entry was edited.

## Validation / CI / APK

- All 9 non-empty JSON files fetched for the two in-scope subjects and registry parsed successfully; the Sanskrit review queue was parsed via its Git blob because the contents endpoint returned an empty payload for this large file.
- Rechecked canonical counts and ID uniqueness after the updates.
- Push-triggered workflow run #1043 (`Public Administration bank validation`) completed successfully, but it validates Public Administration only and is **not** evidence for Sanskrit/Environmental Sciences or the Android APK.
- No target subject-specific validation or Debug APK run is recorded for this commit. Debug APK validation remains pending.

## Remaining evidence-gated work

1. Independently verify all 550 recovered Sanskrit questions against their original official paper pages.
2. Resolve the 8 active Sanskrit syllabus mappings against readable official Code 07 syllabus text.
3. Complete the independent second proofreading pass for the 291 Environmental Sciences records using the official question-paper scans.
4. Run the relevant Sanskrit/Environmental Sciences bank validators and the combined Debug APK workflow.
5. Do not merge PR #22 without explicit authorization.
