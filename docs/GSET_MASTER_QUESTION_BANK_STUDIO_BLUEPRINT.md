# GSET Master Question Bank Studio — Implementation Blueprint

## Goal
Build a reusable PDF-to-validated-question-bank workflow for all 36 GSET Paper-II subjects, exporting into the existing Flutter app's canonical data layout without changing Paper-I or existing verified banks.

## Repository facts verified on 2026-11-19
- Repository: `dhavalkhant3-web/gset-test-series`
- Default branch: `main`
- Flutter application; question bank loader resolves `assets/subjects/<subjectId>/questions.json`.
- Subject registry: `assets/subjects/subjects.json`; it contains 36 subjects, codes 01–36.
- Shared syllabus registry: `assets/subjects/syllabus_units.json`.
- Existing question-bank validator: `tool/validate_questions.py`; legacy root-bank schema requires `id`, `paperId`, `question_en`, `question_gu`, `options_en`, `options_gu`, `answer`. Subject banks may have additional metadata and subject-specific validators; inspect each target file before export.
- Existing audit tools include `tool/audit_combined_subject_banks.py` and subject-specific validators under `tools/`.
- Existing PR #22 is open and targets `integration/combined-subject-banks`; this branch is independent and must not modify or merge PR #22.
- GitHub integration permission reports admin/push access.
- Important app integration constraint: `pubspec.yaml` bundles `assets/subjects/**`; the app loader reads the above path and has special merge logic for Physical Sciences and Chemical Sciences. Never assume all subject schemas/merge logic are identical.

## Branch
`feature/gset-master-question-bank-studio` created from `main`.

## Safety boundaries
1. Do not modify `main`, PR #22, other subject banks, Paper-I UI, release signing, or production Firebase configuration.
2. Do not auto-merge any PR.
3. Do not promote a record to verified solely from model confidence or OCR output.
4. Official GSET final answer keys are authoritative; preserve valid special answer codes already supported by the target bank.
5. Retain PDF file hash, source filename, printed page, PDF page index, question number and extraction method for traceability.
6. Separate `active/verified`, `provisional`, and `review` states; exports to production banks must be gated by explicit source/key/syllabus checks.
7. Do not require or commit API keys. Use environment variables and document required secrets.
8. No fabricated questions, answers, options, images, or syllabus mappings.

## Proposed system architecture
- Admin UI: browser-based subject/year/document upload and job dashboard.
- API: Python FastAPI backend.
- Processing workers: background task queue with per-document/job status and retry.
- PDF: PyMuPDF for native text/page metadata; OCR adapter interface for scanned pages (Google Document AI optional, Tesseract/PaddleOCR local fallback); multimodal review adapter optional.
- Data store: SQLite for local pilot, PostgreSQL for hosted multi-user deployment; original PDFs in private object storage/local media directory.
- AI adapters: provider-agnostic, configurable; secrets only server-side.
- Validation: deterministic Python validators and existing target subject validator.
- Export: generate preview/diff and create a feature-branch commit/PR; never write directly to main.
- Android compatibility: export exactly the target subject's existing schema and maintain `assets/subjects/<subjectId>/questions.json` plus associated `papers.json`/metadata as required.

## Common processing pipeline
1. Upload question paper, official final key, syllabus/version, optional tips/notes.
2. Compute SHA-256 and classify document; resolve subject code, year/session, paper and booklet.
3. Extract native text and page layout; OCR only pages that need it.
4. Parse candidate question blocks/options/figures and retain page/image source refs.
5. Normalize question IDs and paper IDs by the existing repository conventions.
6. Translate only when the target subject requires Gujarati; retain source-language text.
7. Reconcile every answer to the official final answer key with key version, booklet and question-number mapping.
8. Map syllabus unit/topic only when supported by official syllabus evidence; otherwise keep unresolved.
9. Attach user-provided tips and explanations by topic/question; AI-generated explanations must be labelled and must not affect official answer verification.
10. Run duplicate, missing-number, option-completeness, source, language, answer, syllabus and schema checks.
11. Produce review queue for uncertain pages/records, preview report, and verified-only export.
12. Commit to a dedicated feature branch and open a draft PR; run target validators and CI. Report build outcome honestly.

## MVP milestones
### M0 — Read-only audit and schema discovery
- Enumerate all 36 subject IDs/codes.
- Inspect representative question/paper files and every subject validator.
- Produce per-subject schema/loader compatibility map and current baseline counts.
- No bank edits.

### M1 — Upload and document inventory
- Subject/year/session selector with assisted classification.
- Multi-PDF upload, SHA-256 deduplication, file metadata, source retention.
- Job status and retry controls.

### M2 — Extraction and review
- Native PDF text extraction and OCR adapter.
- Question/option candidate extraction with per-field/page provenance.
- Human-review screen with original page image beside extracted output.
- Confidence is triage only, not verification.

### M3 — Key and syllabus verification
- Official-key parser and exact reconciliation.
- Versioned official syllabus parser and evidence-backed mapping.
- Fail-closed review queues.

### M4 — JSON generation
- Per-subject schema adapters based on actual existing JSON.
- Incremental merge with stable IDs and duplicate prevention.
- JSON schema validation, target-specific Python validator, diff preview and rollback.

### M5 — GitHub and Android CI
- Branch-only commit/PR integration.
- Existing workflows/tests and combined Debug APK build.
- Verify that the target subject loader can load the bank; do not modify Paper-I.

### M6 — Production hardening
- Auth, role-based permissions, upload limits, retention policy, backups, monitoring, cost controls, API secret management.
- Bulk enablement only after pilot acceptance.

## Pilot acceptance
Use one subject and one year supplied by the user:
- Extract all printed questions and options with source page refs.
- Compare against official final key.
- Use the official syllabus version supplied/verified.
- Generate target-compatible JSON.
- Run actual target validator and CI.
- Report counts: expected, extracted, duplicate, key matched, mapped, verified, review, exported.
- The pilot passes only if all expected questions are accounted for and every discrepancy is explicitly surfaced; otherwise it remains non-production/review-only.

## Required credentials/configuration (not yet supplied/verified)
- OCR provider credentials (optional if local OCR selected).
- AI model provider API key.
- Secure deployment/object storage configuration if hosted.
- GitHub integration is connected and has repository push permissions, but automation still needs secure server-side credential configuration for deployed service.

## Current implementation status
- Repository discovery: completed.
- Master registry: 36 subjects confirmed.
- Existing Flutter question loader and top-level schema pattern: inspected.
- Independent feature branch: created.
- Web application/API/OCR pipeline: not yet implemented.
- No source PDFs uploaded in this task; no extraction or answer verification performed.
- No PR created and no merge performed.
