# GSET Music — Subject Code 30

Existing branch: `add-music-subject-30`; PR #18 targets `integration/combined-subject-banks`. Existing subject banks were not replaced.

## Question bank and answer key
- November 2023 Paper-II: 100 question records
- December 2024 Paper-II: 100 question records
- November 2025 Paper-II: 100 question records
- Total: 300 unique question records.
- The 300 answer choices are reconciled against the supplied official final answer-key PDFs; structural comparison currently reports 0 mismatches.

## Gujarati transcription status
- Gujarati stem + four options populated: 131/300
- Still missing at least one Gujarati field/option: 169/300
- New OCR passes were run against the original bilingual scans using Gujarati-column layout extraction. Every OCR-filled record remains review-flagged until the original scan is visually checked.
- Do not treat OCR as final proofreading. Remaining records must be transcribed from the scan, not translated from English or guessed.

## English text, figures, and unit mapping
- English stems/options have not yet been visually proofread end-to-end against all 300 source questions.
- Figure/notation/diagram-bearing questions still need page-by-page review; no visual-content audit is claimed complete.
- All 300 records have been topic/wording-based mapped to the registered 10 Music units as a first-pass review. Stream-specific/manual review remains pending for borderline questions, particularly Hindustani, Carnatic, percussion, and Rabindra Sangeet material.
- All records remain review-flagged and `source_verified=false`.

## Merge gate
Do not merge or call this archive fully source-verified until the remaining 169 Gujarati transcriptions are completed, all 300 bilingual stems/options and visual content are proofread against the original scans, unit assignments are manually validated against the official stream syllabus, and app CI/build validation passes.

## Official source locations
- GSET question-paper archive: https://www.gujaratset.ac.in/oldpap
- GSET final answer keys: https://www.gujaratset.ac.in/anskey
- GSET Music syllabus: https://gujaratset.ac.in/assets/syllabus/30.pdf
- UGC-NET Music syllabus code 16: https://ugcnetonline.in/syllabus-new.php
