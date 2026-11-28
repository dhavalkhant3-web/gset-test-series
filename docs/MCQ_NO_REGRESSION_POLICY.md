# MCQ Bank Preservation and No-Regression Policy

## Purpose
Protect all existing GSET Paper-II question banks and prevent completed transcription, answer verification, source verification, language preservation, and unit mapping from being lost or repeated.

## Non-negotiable rules
1. Never rebuild a subject bank from scratch when a bank already exists.
2. Never replace a complete `questions.json` with OCR output, a partial paper, or a newly generated list.
3. Make small, targeted, reviewable changes. Preserve all existing question IDs unless a documented correction requires otherwise.
4. Never infer or fabricate missing question wording, options, diagrams, equations, or official answers.
5. The official GSET final answer key is authoritative. If a calculation appears to disagree, preserve the official key and mark the record for review with a clear note.
6. Keep Paper-II and Paper-III records separate. Do not load the same IDs through both a base bank and an overlay.
7. Keep uncertain OCR/transcription flagged for visual review; do not mark it source-verified without checking the official source.
8. Do not merge a recovery or content PR until all relevant automated checks pass and the diff has been reviewed.

## Required pre-change snapshot
Before editing a subject bank, record:
- base branch and commit SHA;
- subject code/name and relevant file paths;
- record count and unique-ID count;
- question IDs by paper/session/year where available;
- counts of `source_verified`, `review_flag`, and missing/uncertain options;
- answer-key and unit-mapping coverage;
- official paper and final-answer-key source references.

Store/update the snapshot and audit report in version control. Never silently replace an earlier snapshot; keep history.

## Required post-change no-regression checks
Compare the changed branch with its base commit and fail the check if:
- an existing question ID disappears without an explicitly approved removal;
- duplicate IDs are introduced or the app loads the same IDs twice;
- an existing official answer, original-language stem, options, figure reference, source-verification status, review flag, or unit mapping changes unexpectedly;
- counts drop for any existing paper/session without a documented explanation;
- a Paper-III file is included in the Paper-II loader;
- a new question lacks source provenance or has an unreviewed answer represented as verified.

New records must be additive unless a change is explicitly described as a correction. Any intentional correction must list affected IDs, old/new values, source evidence, and reason in the PR.

## PR checklist
- [ ] Scope is limited to the named subject/task.
- [ ] Baseline and before/after counts are included.
- [ ] Changed/added/removed IDs are listed.
- [ ] Original paper and official final answer key are cited for imported/changed records.
- [ ] All relevant subject validators pass.
- [ ] No-regression checks pass.
- [ ] Flutter app validation/build passes when app loading or rendering changes.
- [ ] Diff reviewed for Gujarati/English source wording, options, scientific notation, figures, and answer keys as applicable.
- [ ] Remaining visual-review items are explicitly listed.
- [ ] PR remains unmerged if any required check fails.

## Recovery procedure
If a regression is detected:
1. Stop further edits and do not merge.
2. Identify the last known-good commit and compare file history/diffs.
3. Restore only missing or damaged records from the known-good version and official sources; do not overwrite unrelated newer work.
4. Run the same validators and compare all protected fields again.
5. Document the incident and the fix before continuing.

## Completion reporting
For each subject, report separate counts for total records, unique IDs, source-verified records, records awaiting visual/source review, answer-key coverage, and unit mapping. A passing structural test is not proof that every question has been visually/source verified.
