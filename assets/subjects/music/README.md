# GSET Music — Subject Code 30

Last reviewed: 30 October 2026

Branch: `add-music-subject-30`  
Pull request: [#18](https://github.com/dhavalkhant3-web/gset-test-series/pull/18) → `integration/combined-subject-banks`

## Current question-bank status

- 300 question records are retained: 100 each for November 2023, December 2024, and November 2025.
- Gujarati stem and four-option fields are populated in 300/300 records. Populated fields alone do not prove accuracy.
- English/Gujarati stems, four options and their order have been visually proofread against the original official question-paper PDFs in 298/300 records: November 2023 100/100, December 2024 100/100, November 2025 98/100. November 2025 Q52–Q53 remain pending because their matching-list notation needs a careful visual transcription.
- Official final answer keys are recorded as visually checked for 300/300 questions, with 0 discrepancies recorded. This is a separate gate from question-paper proofreading.
- Syllabus mappings manually reviewed: 140/300 (November 2023: 88; December 2024: 52; November 2025: 0). Fourteen mappings are explicitly ambiguous (12 November 2023; 2 December 2024); 146 mappings remain provisional/pending (46 December 2024; 100 November 2025).
- 160/300 records remain review-flagged because one or more verification gates are incomplete. 140 records currently satisfy all three gates: source visual proofread, answer-key visual check, and manually reviewed syllabus mapping.
- The Music subject registry remains `source_verified: false` until every required question-level gate is complete.

## Remaining work before merge

1. Visually proofread November 2025 Q52–Q53 against the original bilingual question paper, including every swara/list item and all four matching options.
2. Adjudicate 14 ambiguous mappings (November 2023: Q61–66, Q71–74, Q91–92; December 2024: Q26 and Q36).
3. Complete 146 provisional mappings (December 2024: Q55–Q100; November 2025: Q1–Q100) against the official Music syllabus and the correct stream-specific content. Do not infer Units V–X without confirming the relevant Music stream.
4. Run the evidence-sensitive Music validator, its unit tests, and the Android debug APK build on the latest PR head. Verify CI and inspect the final PR diff.

## Official source PDFs

| Session | Question paper | Final answer key |
|---|---|---|
| November 2023 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2330.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov23/nov2330.pdf) |
| December 2024 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2430.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/dec24/dec2430.pdf) |
| November 2025 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2530.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov25/nov2530.pdf) |

Official syllabus: [GSET Music syllabus, Code 30](https://gujaratset.ac.in/assets/syllabus/30.pdf). The syllabus configuration identifies UGC-NET Music code 16 and notes that Units V–X are stream-specific; verify stream applicability before final mapping.

**Verification rule:** OCR and populated fields are not proof of source fidelity. Do not set `source_verified=true`, remove review flags, or merge until each source and mapping gate is evidenced. Do not merge PR #18 without explicit user authorization.
