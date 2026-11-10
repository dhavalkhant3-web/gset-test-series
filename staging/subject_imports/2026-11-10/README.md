# Uploaded GSET Subject Import — Audit Staging (2026-11-10)

**Repository:** dhavalkhant3-web/gset-test-series  
**Base branch:** integration/combined-subject-banks  
**Working branch:** staging/uploaded-subject-banks-2026-11-10  
**Status:** SOURCE STAGING ONLY — NOT APP-INTEGRATED; DO NOT MERGE OR MARK COMPLETE.

This folder preserves the uploaded source JSONs and the accompanying Geography audit report so they can be reconciled against the repository schema and original official PDFs. Duplicate byte-identical uploads were deduplicated. The source JSONs are preserved without changing their question or answer content.

## Imported material and findings

| Subject | Uploaded material | Records represented | Current finding |
|---|---|---:|---|
| Geography (24) | 2016/2017 mapped staging, Nov 2025 mapped staging, official final-key index, audit report | 200 question records; 700 key entries across 8 sessions | Staging files explicitly say proofreading/source visual review is pending. Audit report says 600 questions from Sep 2018, Dec 2021, Nov 2022, Nov 2023 and Dec 2024 remain untranscribed. The Nov 2025 file has 2 review-required records and Q81 visual check pending. The uploaded question files contain 0 source_verified=true records. |
| Gujarati (06) | Paper-II staging bank and official syllabus unit-title file | 400 question records | 399 answers populated; one answer missing. 52 review_required records. Syllabus units are only titles; per-question mapping is not done. The source notice says transcription still needs human proofread and older 2002/2003/2008 keys are not labelled final. |
| Environmental Sciences (26) | Paper-II staging bank | 300 question records across Nov 2023, Dec 2024 and Nov 2025 | 292 records marked key_verified_pending_proofread and 8 key_verified_visual_checked. All syllabus_unit values are null because the official syllabus was not supplied. |
| Social Work (25) | Answer-key staging file only | 600 answer-key entries across 6 sessions | No question text/options bank was uploaded; this is not ready for app question-bank integration. |

## Exact source data locations

- `geography/geography_nov2025_mapped.json`
- `geography/geography_sep2016_aug2017_mapped.json`
- `geography/geography_official_final_keys.json`
- `geography/geography_audit_report.md`
- `gujarati/gset_gujarati_paper2_staging.json`
- `gujarati/gset_gujarati_syllabus_units.json`
- `environmental_sciences/gset_env_sci_26_paper2_staging.json`
- `social_work/gset_sw25_answer_keys_only.json`

## Why these files are not yet active in the app

The repository's active Paper-II loader expects question records in its established schema (e.g. `id`, `paper_id`, `question_no`, `question_en`, `options_en`, `answer`, `topic`, source/review fields). The uploaded staging files use different field names and explicitly carry incomplete proofread, visual-review or syllabus-mapping states. Social Work has keys only. The original question-paper PDFs and final-key PDFs themselves were not included in this upload batch, so source-page re-verification cannot be performed from these files alone.

No live `assets/subjects/<subject>/questions.json`, `papers.json`, subject registry, Flutter loader, Paper-I UI, or other subject was modified in this staging commit series. This is intentional: do not expose unproofread/unreconciled staging records as completed app content.

## Next steps before app activation

1. Obtain the original official question-paper PDFs and answer-key PDFs for the relevant sessions.
2. Resolve the flagged/missing items and visually proofread every question and option.
3. Map each question to the official syllabus; do not treat provisional unit suggestions as verified.
4. Convert to the repository's canonical question-bank schema and run duplicate, coverage, option, answer and source-provenance audits.
5. Only then update the live subject assets and registry on a reviewed integration branch.
6. Run the subject validator, combined CI and Debug APK build.
7. Keep the PR unmerged until explicit user approval.

**No answer, source-verification flag, syllabus mapping, CI result or APK result has been fabricated or promoted to verified.**
