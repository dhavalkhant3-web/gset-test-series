# GSET Music — Subject Code 30

Last reviewed: 30 October 2026

Branch: `add-music-subject-30`  
Pull request: [#18](https://github.com/dhavalkhant3-web/gset-test-series/pull/18) → `integration/combined-subject-banks`

## Current question-bank status

- 300 question records retained: 100 each for November 2023, December 2024, and November 2025.
- English/Gujarati stems, all four options, option order and matching-list notation have been visually proofread against the original official bilingual GSET question-paper PDFs: **300/300**.
- Gujarati stem and four-option fields are populated in 300/300 records.
- Official final answer keys are recorded as visually checked for 300/300 questions, with 0 discrepancies recorded.
- Syllabus mappings manually reviewed: **140/300** (November 2023: 88; December 2024: 52; November 2025: 0).
- Fourteen mappings remain ambiguous (November 2023: 12; December 2024: 2); 146 remain provisional/pending (December 2024: 46; November 2025: 100).
- 160/300 records remain review-flagged because syllabus mapping is incomplete or ambiguous. 140 records currently satisfy all three gates: source visual proofread, answer-key visual check, and manually reviewed syllabus mapping.
- Music registry remains `source_verified: false` until all question-level gates are complete.

## Remaining work before merge

1. Adjudicate 14 ambiguous mappings (November 2023: Q61–66, Q71–74, Q91–92; December 2024: Q26 and Q36).
2. Complete 146 provisional mappings (December 2024: Q55–Q100; November 2025: Q1–Q100) against official Music syllabus code 16.
3. Confirm the relevant Music stream before finalizing stream-specific Units V–X. Do not guess stream-dependent mappings.
4. Run/verify the latest Music validator, unit tests and Android debug APK build. Inspect CI and final PR diff.

## Official source PDFs

| Session | Question paper | Final answer key |
|---|---|---|
| November 2023 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2330.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov23/nov2330.pdf) |
| December 2024 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2430.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/dec24/dec2430.pdf) |
| November 2025 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2530.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov25/nov2530.pdf) |

Official syllabus: [GSET Music syllabus, Code 30](https://gujaratset.ac.in/assets/syllabus/30.pdf). Repository configuration identifies UGC-NET Music code 16 and notes that Units V–X are stream-specific; verify stream applicability before final mapping.

**Verification rule:** OCR and populated fields are not proof of source fidelity. Do not remove review flags or merge until each mapping gate is evidenced. Do not merge PR #18 without explicit user authorization.
