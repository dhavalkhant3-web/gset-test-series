# Mathematical Sciences — year-by-year source verification ledger

Repository: `assets/subjects/mathematical_sciences/questions.json`  
Official question-paper archive: https://www.gujaratset.ac.in/oldpap  
Official final answer keys: https://www.gujaratset.ac.in/anskey

## Acceptance rule

A record may be marked `source_verified: true` and have `review_flag: false` only after checking it against the official question-paper PDF and the official final answer key. Answer-key agreement alone is insufficient. The reviewer must check question number, original wording, all four options, mathematical notation (including fractions, matrices, superscripts/subscripts, Greek symbols), figures/tables, and final answer. Do not recreate missing questions from memory. Preserve any source figure as an original asset or leave the record flagged with a clear note.

## Year-by-year ledger

Recovered counts below are from the recovered archive metadata, not from completed source verification.

| Paper / session | Expected | Recovered | Missing | Source-level status |
|---|---:|---:|---:|---|
| January 2002 | 50 | 42 | 8 | NOT VERIFIED |
| December 2002 | 50 | 50 | 0 | NOT VERIFIED |
| December 2003 | 50 | 44 | 6 | NOT VERIFIED |
| July 2004 | 50 | 43 | 7 | NOT VERIFIED |
| July 2006 | 50 | 44 | 6 | NOT VERIFIED |
| December 2008 | 50 | 32 | 18 | NOT VERIFIED |
| October 2010 | 50 | 26 | 24 | NOT VERIFIED |
| October 2011 | 50 | 42 | 8 | NOT VERIFIED |
| September 2013 | 50 | 50 | 0 | NOT VERIFIED |
| October 2014 | 50 | 43 | 7 | NOT VERIFIED |
| September 2016 | 50 | 50 | 0 | NOT VERIFIED |
| August 2017 | 50 | 36 | 14 | NOT VERIFIED |
| September 2018 | 100 | 87 | 13 | NOT VERIFIED |
| December 2019 | 100 | 74 | 26 | NOT VERIFIED |
| December 2021 / January 2022 | 100 | 92 | 8 | NOT VERIFIED |
| November 2022 | 100 | 90 | 10 | PARTIAL: answer-label comparison only; discrepancies require review |
| November 2023 | 100 | 88 | 12 | PARTIAL: recovered answer labels match key; wording/options/notation not verified |
| December 2024 | 100 | 89 | 11 | PARTIAL: answer-label discrepancies require review |
| November 2025 | 100 | 89 | 11 | PARTIAL: 89 recovered answer labels matched official final key; missing Q6, Q22, Q25, Q26, Q29, Q36, Q55, Q57, Q63, Q77, Q95 |

## Known answer-key checks (not full verification)

- November 2025 official question paper: https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2501.pdf
- November 2025 official final key: https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2501.pdf
- November 2022 official final key: https://gujaratset.ac.in/assets/anskey/paperII/nov22/nov2201.pdf
- November 2023 official final key: https://gujaratset.ac.in/assets/anskey/paperII/nov23/nov2301.pdf
- December 2024 official final key: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2401.pdf

November 2025 key labels matched for 89 recovered records. Official key labels Q16, Q41 and Q92 are `Z`, meaning those questions are not evaluated; do not replace `Z` with an A/B/C/D answer. This does not prove the recovered question statements/options are accurate.

## Next actions

1. Obtain the official source PDF for one session and compare each recovered question by its printed question number, not array position.
2. Log each check with a source page/region note and answer-key result.
3. Repair OCR only by transcribing the source; preserve figures and equations faithfully. If a figure cannot be represented safely, retain the source image reference and keep the record flagged.
4. Add genuinely missing questions only by source transcription, with all four options and the official key.
5. Run the fail-closed validator; it must reject any unverified or flagged record.
6. Do not merge this bank into `main` or alter Paper-I/other subject banks until the year is complete and reviewed.

**Current release decision: BLOCKED.** No year is fully source-verified yet. This ledger is a tracking document, not evidence that the listed records have been verified.
