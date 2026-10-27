# GSET Music — Subject Code 30

Existing branch: `add-music-subject-30`; PR #18 targets `integration/combined-subject-banks`. Existing subject banks were preserved.

## Question bank and answer key
- November 2023 Paper-II: 100 question records
- December 2024 Paper-II: 100 question records
- November 2025 Paper-II: 100 question records
- Total: 300 unique question records.
- All 300 answer choices are reconciled against the supplied official final answer-key PDFs; structural comparison currently reports 0 mismatches.

## Gujarati transcription status
- November 2023: 68/100 complete Gujarati stems + four options; 32 incomplete.
- December 2024: 48/100 complete Gujarati stems + four options; 52 incomplete.
- November 2025: 58/100 complete Gujarati stems + four options; 42 incomplete.
- Total: 174/300 records have a Gujarati stem and four populated options; 126/300 still have at least one missing Gujarati field.
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
- Gujarati stem plus four nonblank Gujarati options: 174/300; pending: 126 (Nov 2023: 32, Dec 2024: 52, Nov 2025: 42).
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

