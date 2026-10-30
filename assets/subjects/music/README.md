# GSET Music — Subject Code 30

Last reviewed: 30 October 2026

Branch: `add-music-subject-30`  
Pull request: [#18](https://github.com/dhavalkhant3-web/gset-test-series/pull/18) → `integration/combined-subject-banks`

## Source and answer-key audit

- 300 question records retained: 100 each for November 2023, December 2024, and November 2025.
- English/Gujarati stems, all four options, option order and matching-list notation visually proofread against original official bilingual GSET question-paper PDFs: **300/300**.
- Gujarati stem and four-option fields populated: **300/300**.
- Official final answer keys visually checked: **300/300**, 0 discrepancies recorded.
- No questions were removed or replaced.

## Syllabus mapping — not complete

GSET Subject Code 30 uses UGC-NET Music Code 16. The official UGC syllabus explicitly states that Units I–IV are common, while Units V–X are subject-specific. It contains separate streams: **Hindustani (Vocal, Instrumental & Musicology), Karnataka, Percussion, and Rabindra Sangeet**. Therefore, a unit number cannot be finalized from a broad topic label alone; the applicable stream must be established for each question.

Current question-level mapping status:
- Manually reviewed: **140/300** (November 2023: 88; December 2024: 52; November 2025: 0).
- Ambiguous: **14** (November 2023: 12; December 2024: 2).
- Provisional / stream-specific review pending: **146** (December 2024: 46; November 2025: 100).
- Review flags: **160/300** remain true until the mapping gate is complete.

The 146 provisional unit numbers are suggestions only, not final verified mappings. The 14 ambiguous records remain explicitly flagged. Do not promote either group to manually reviewed until the stream and the exact unit description are verified.

## Remaining work before merge

1. Determine the correct syllabus stream for each question using its content and the official paper context.
2. Re-check all 140 existing manual mappings against the same stream-specific rules; retain only evidence-backed assignments.
3. Resolve 14 ambiguous and 146 provisional mappings. Units I–IV use the common syllabus; Units V–X must follow the relevant stream.
4. Run the latest Music validator, unit tests and Android debug APK build. Inspect CI and final PR diff.

Official sources:
- [GSET Music syllabus, Subject Code 30](https://gujaratset.ac.in/assets/syllabus/30.pdf)
- [UGC-NET Music syllabus, Code 16](https://ugc-web-files.s3.ap-south-1.amazonaws.com/NTA_All_R_Syllabus/16/Music_English.pdf)

Official question papers and final keys:
- [November 2023 paper](https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2330.pdf) · [final key](https://www.gujaratset.ac.in/assets/anskey/paperII/nov23/nov2330.pdf)
- [December 2024 paper](https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2430.pdf) · [final key](https://www.gujaratset.ac.in/assets/anskey/paperII/dec2430.pdf)
- [November 2025 paper](https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2530.pdf) · [final key](https://www.gujaratset.ac.in/assets/anskey/paperII/nov25/nov2530.pdf)

**Merge rule:** Do not merge PR #18 without explicit user authorization.
