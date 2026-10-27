# GSET Music — Subject Code 30

Branch: `add-music-subject-30`  
Pull request: [#18](https://github.com/dhavalkhant3-web/gset-test-series/pull/18) → `integration/combined-subject-banks`

## Current verified inventory (27 October 2026)

- 300 question records total: 100 each for November 2023, December 2024, and November 2025.
- Gujarati stems and all four Gujarati options are populated in 300/300 records. This confirms field completeness only; it does **not** certify exact transcription.
- Four English options are populated in 300/300 records.
- Stored answer letters were compared with extracted official final-key text: 300 matches, 0 reported mismatches. A fresh visual check against the original answer-key PDFs remains a separate verification gate.
- All 300 records remain `review_flag=true` and `source_verified=false`. Fully source-verified count: **0/300**.
- No end-to-end visual proofreading of all bilingual question text, option order, diagrams, notation, symbols, or tables is claimed complete.
- Unit mappings are provisional topic-based classifications. Manual semantic and stream-specific review remains incomplete.

## Official source PDFs

| Session | Question paper | Final answer key |
|---|---|---|
| November 2023 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2330.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov23/nov2330.pdf) |
| December 2024 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2430.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/dec24/dec2430.pdf) |
| November 2025 | [Paper-II PDF](https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2530.pdf) | [Final key PDF](https://www.gujaratset.ac.in/assets/anskey/paperII/nov25/nov2530.pdf) |

Official syllabus: [GSET Music syllabus, Code 30](https://gujaratset.ac.in/assets/syllabus/30.pdf). Units I–IV are common; Units V–X are stream-specific.

## Remaining merge gates

1. Visually compare every English and Gujarati stem and all four options/order against each original paper PDF.
2. Inspect all figures, tables, notation, musical symbols, and page-specific content.
3. Compare answer letters directly with the official final-key PDFs and record any source discrepancies.
4. Manually validate all 300 unit assignments against the official syllabus, paying particular attention to Hindustani, Karnataka/Carnatic, percussion, and Rabindra Sangeet stream-specific topics.
5. Run the Music validator and Flutter build/CI on the current PR head; only then consider merging.

**Important:** OCR and populated fields are not proof of source fidelity. Do not set `source_verified=true`, remove review flags, or merge until the source-based checks above are actually complete.
