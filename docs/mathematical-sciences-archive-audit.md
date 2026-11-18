# Mathematical Sciences archive — source audit

## Scope
This report summarizes the recovered GitHub Actions artifact `mathematical-sciences-archive` (artifact ID `12282244264`, run `39456150487`). It is an archive-quality audit, not a claim that questions have been verified against official source PDFs.

## Structural findings
- Recovered question records: **1,111**
- Paper metadata records: **19**
- Expected questions from metadata: **1,300**
- Missing records relative to metadata: **189**
- Records with `review_flag: true`: **1,111 / 1,111**
- Records with `source_verified: false`: **1,055**
- Gujarati question text identical to English: **1,105**
- Gujarati options identical to English options: **1,111**
- Answers outside A/B/C/D: **11** (label Z appears; do not replace without the official final key)
- Duplicate IDs: **0**

## Recovered questions by paper

| Exam | Expected | Recovered | Missing |
|---|---:|---:|---:|
| January 2002 | 50 | 42 | 8 |
| December 2002 | 50 | 50 | 0 |
| December 2003 | 50 | 44 | 6 |
| July 2004 | 50 | 43 | 7 |
| July 2006 | 50 | 44 | 6 |
| December 2008 | 50 | 32 | 18 |
| October 2010 | 50 | 26 | 24 |
| October 2011 | 50 | 42 | 8 |
| September 2013 | 50 | 50 | 0 |
| October 2014 | 50 | 43 | 7 |
| September 2016 | 50 | 50 | 0 |
| August 2017 | 50 | 36 | 14 |
| September 2018 | 100 | 87 | 13 |
| December 2019 | 100 | 74 | 26 |
| December 2021 (January 2022) | 100 | 92 | 8 |
| November 2022 | 100 | 90 | 10 |
| November 2023 | 100 | 88 | 12 |
| December 2024 | 100 | 89 | 11 |
| November 2025 | 100 | 89 | 11 |

## Known quality risks
- OCR corruption and merged question text occur in recovered records.
- Gujarati question and option fields are not reliably translated.
- The archive is incomplete for every paper except December 2002, September 2013, and September 2016.
- Some records have answer label `Z`; treat this as a value to verify against the official key, not an invalid value to silently convert.
- A previous `source_verified` flag is not sufficient evidence by itself; verification must be traceable to the official PDF/key.

## Safe next steps
1. Use only the official GSET question paper and final answer key: https://www.gujaratset.ac.in/oldpap and https://www.gujaratset.ac.in/anskey.
2. Verify one paper at a time, preserving question numbering, four options, mathematical notation, and figures.
3. Record unresolved or image-dependent items as `review_flag: true` and `source_verified: false`.
4. Do not promote the recovered archive to the production path until all expected questions and source checks pass.
5. Preserve the existing Paper-I UI and all other subject banks.

**Status: NOT VERIFIED / NOT READY FOR PRODUCTION.** This audit is based on the recovered archive and its metadata. It does not claim independent source verification of the question text or answers.
