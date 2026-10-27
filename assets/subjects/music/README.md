# GSET Music — Subject Code 30

Existing branch: `add-music-subject-30`; PR #18 targets `integration/combined-subject-banks`. Existing subject banks were preserved.

## Question bank and answer key
- November 2023 Paper-II: 100 question records
- December 2024 Paper-II: 100 question records
- November 2025 Paper-II: 100 question records
- Total: 300 unique question records.
- All 300 answer choices are reconciled against the supplied official final answer-key PDFs; structural comparison currently reports 0 mismatches.

## Gujarati transcription status
- November 2023: 100/100 Gujarati stems + four options populated; visual proofreading pending.
- December 2024: 48/100 complete Gujarati stems + four options; 52 incomplete.
- November 2025: 58/100 complete Gujarati stems + four options; 42 incomplete.
- Total: 193/300 records have a Gujarati stem and four populated options; 107/300 still have at least one missing Gujarati field.
- Missing question ranges are recorded in `assets/subjects/music/verification_pending.json`.
- Multiple Gujarati-column OCR passes (layout modes 4, 6 and 11) were run against the original bilingual scans. OCR is not proof of exact transcription: all OCR-filled records remain review-flagged until visually checked against the original scan.
- Remaining records must be transcribed from the Gujarati column, not guessed or translated from English.

## English text, figures, and unit mapping
- English stems/options have not been visually proofread end-to-end against all 300 source questions.
- Figure/notation/diagram-bearing questions still need page-by-page review; no visual-content audit is claimed complete.
- All 300 records have a topic/wording-based first-pass mapping to the registered 10 Music units. Manual stream-specific review remains pending for borderline questions, especially Hindustani, Carnatic, percussion, and Rabindra Sangeet content.
- All 300 records remain review-flagged and `source_verified=false`.

## Merge gate
Do not merge or call this archive fully source-verified until the remaining 126 Gujarati transcriptions are completed, all 300 bilingual stems/options and visual content are proofread against the original scans, unit assignments are manually validated against the official stream syllabus, and Music-specific validation plus app build/CI pass.

## Official source locations
- GSET question-paper archive: https://www.gujaratset.ac.in/oldpap
- GSET final answer keys: https://www.gujaratset.ac.in/anskey
- GSET Music syllabus: https://gujaratset.ac.in/assets/syllabus/30.pdf
- UGC-NET Music syllabus code 16: https://ugcnetonline.in/syllabus-new.php

## Latest checkpoint — 27 October 2026
- Current bank: 300 records, 100 per session; 300 unique IDs.
- Gujarati stem plus four nonblank Gujarati options: 300/300 populated; 0 incomplete fields. This is transcription completeness, not source verification.
- All 300 records have four nonblank English options. Stored `answer` and `official_answer` fields currently agree in all 300 records; this structural comparison does not replace a fresh page-by-page comparison with the official final-key PDFs.
- All 300 still have `review_flag=true` and `source_verified=false`; fully source-verified count remains zero.
- Corrected the Music subject registry to report 3 papers and 300 question records, matching the existing bank. No question records or IDs were rewritten.
- Added `tools/validate_music_subject.py` to check IDs, record/session counts, English options, answer-field consistency, Gujarati completion counts, pending-number report synchronization, structural unit references, registry counts, and conservative review flags.
- Added `.github/workflows/music-subject-validation.yml` to run those checks and a Flutter debug APK build on subject-branch pushes / relevant PR changes. **Do not infer a passing CI result until GitHub Actions reports success on the current head.**
- These automated checks cannot visually verify scanned text, diagrams, notation, the official answer-key PDF itself, or the semantic correctness of unit assignments.

## Still required before merge
1. Complete the 126 missing Gujarati stems/options directly from the Gujarati columns of the original bilingual PDFs.
2. Visually proofread every English/Gujarati stem and all options/order against all three original PDFs; inspect diagrams, notation, symbols, and page layout where present.
3. Reconcile all answers directly against the official final answer-key PDFs; retain official answers if they differ from independent calculations.
4. Manually review all 300 unit assignments against the official Music syllabus, including Hindustani, Carnatic, percussion, and Rabindra Sangeet-specific content.
5. Obtain successful Music validator and Flutter build/CI checks. Do not set any source-verification flags or merge until the source-based gates are actually complete.



### Work completed in this continuation
- Added Gujarati transcription for November 2023 questions 22–26 and 40–43, 48–57 from the Gujarati columns of the original bilingual PDF. These 19 records are populated, but remain review-flagged and require visual proofreading for exact character/option fidelity.
- Recalculated and synchronized per-paper Gujarati completion counts and exact missing question lists from the current question bank; prior progress metadata was stale for November 2023.

### Latest transcription pass — 27 October 2026
- Filled all previously blank Gujarati stem/options fields across November 2023 (13 records), December 2024 (52 records), and November 2025 (42 records), bringing the field-completeness count to 300/300.
- Progress metadata and the verification-pending report were recalculated directly from the current bank.
- Important: many transcriptions were entered with OCR assistance and are **not yet visually proofread character-by-character** against the scanned bilingual originals. This does not satisfy the full source-verification requirement. All 300 remain `review_flag=true`, and `source_verified=true` remains 0.
- Official answer-key PDFs have not yet been fully reconciled independently against each question in this turn; do not infer that key review is complete from stored field agreement. The 300 syllabus-unit assignments still need manual topic-level and stream-specific review.
