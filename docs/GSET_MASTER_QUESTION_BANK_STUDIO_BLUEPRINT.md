# GSET Master Question Bank Studio — Implementation Blueprint

## Verified repository facts (19 Nov 2026)
- Flutter application; default branch is `main`.
- There are 36 Paper-II subjects in `assets/subjects/subjects.json`, codes 01–36.
- The Flutter data loader resolves subject banks at `assets/subjects/<subjectId>/questions.json`.
- Shared syllabus registry: `assets/subjects/syllabus_units.json`.
- Legacy root-bank validator: `tool/validate_questions.py`; required fields include `id`, `paperId`, `question_en`, `question_gu`, `options_en`, `options_gu`, `answer`. Subject banks may have extensions; always inspect their actual schema and target-specific validator.
- Existing audit/validation tooling includes `tool/audit_combined_subject_banks.py` and validators in `tools/`.
- PR #22 is open and targets `integration/combined-subject-banks`. Leave it unchanged and unmerged.
- GitHub connection reports repository admin/push permission.
- App loader has special merge logic for Physical Sciences and Chemical Sciences; do not assume all subjects integrate identically.

## Branch and safety
- Dedicated branch: `feature/gset-master-question-bank-studio`, created from `main`.
- Do not modify main, PR #22, existing question banks, Paper-I UI, signing files, or production Firebase configuration.
- Do not merge any PR.
- No question/answer/option/syllabus mapping may be invented.
- AI/OCR confidence is only a review-prioritization signal, not proof of verification.
- Preserve official final answer-key authority and the target bank's supported answer values.
- Store source PDF hash, filename, PDF page index, printed page, question number, extraction method and key/syllabus provenance.
- Use separate verified, provisional and review states. Fail closed when evidence is insufficient.
- Never commit API keys. Configure them server-side through environment variables/secrets.

## Target architecture
- Web admin UI for subject/year/session/document upload and job monitoring.
- Python FastAPI backend.
- Background processing workers with retryable job states.
- PyMuPDF for PDF structure/native text; OCR adapter for scanned pages (Google Document AI optional, Tesseract/PaddleOCR fallback); optional multimodal review for difficult math/figures.
- SQLite pilot database; PostgreSQL for hosted multi-user production.
- Provider-neutral AI adapters; credentials server-side only.
- Deterministic validation and subject-specific schema adapters.
- Export previews and diffs, then create a feature branch and draft PR. Never write directly to main.
- Export to the existing Android data path: `assets/subjects/<subjectId>/questions.json`, plus `papers.json` and metadata only when needed.

## Automated workflow
1. Upload question paper, official final key, official syllabus/version and optional user tips/notes.
2. Hash/classify files; resolve code, year, session, paper and booklet; identify reused syllabus.
3. Extract native text/layout, OCR only pages requiring it.
4. Extract question stems, options, equations, tables and figure references with page provenance.
5. Preserve source wording/notation; translate to Gujarati only when target language requires it.
6. Match every question against the official final key with booklet/number mapping.
7. Map topics/units only with evidence from the official syllabus.
8. Attach existing user tips; label AI-generated explanations as unverified suggestions.
9. Check completeness, duplicate IDs, option counts, answer values, translations, source refs, syllabus validity and schema.
10. Put unresolved records into review; produce a count/reconciliation report.
11. Generate compatible JSON, preview diff, backup, validate and create a draft PR.
12. Run target validators, CI, Debug APK build and app-loader checks; report exact results.

## Milestones
- M0 Read-only audit: all 36 subjects, data schemas, paper metadata, loaders, validators, counts, baseline.
- M1 Upload/document inventory: multi-PDF upload, SHA-256 dedupe, metadata and job state.
- M2 Extraction/review: native extraction, OCR adapter, page-image comparison, field provenance.
- M3 Verification: final-key parser/reconciliation, versioned syllabus mapping and fail-closed review.
- M4 JSON generation: per-subject adapters, incremental merge, stable IDs, duplicate prevention, backups/rollback.
- M5 GitHub/Android: branch-only commit/PR, existing tests/validators and combined Debug APK.
- M6 Production: authentication, role permissions, secure storage, retention, monitoring, rate/cost limits, secrets and deployment.

## Pilot acceptance
Pilot must use one subject and one examination year from user-provided official PDFs. Report expected/extracted/missing/duplicate/key-matched/mapped/verified/review/exported counts. Pass only when the official expected question sequence is accounted for, answer-key reconciliation is evidenced, mappings have official syllabus support, JSON passes the target validator, and Android build/load checks pass. Otherwise keep the export staged/review-only.

## Credentials/configuration still needed
- AI provider API key.
- OCR provider credentials if managed cloud OCR is selected (local OCR can be used as fallback).
- Secure hosting/object storage settings for hosted upload.
- GitHub connector is connected with push permission, but a deployed service still needs its own secure GitHub App/PAT installation or approved OAuth flow.

## Status
- Repository audit: initial read-only inspection complete.
- 36 subject registry entries confirmed.
- Main Flutter loader and validator pattern inspected.
- Feature branch created.
- Blueprint recorded here; application code, upload API, OCR workers and UI are not yet implemented.
- No source PDFs were submitted in this turn; no question extraction or answer verification was performed.
- No PR created; no merges performed.
