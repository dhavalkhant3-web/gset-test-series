# Sanskrit Code 07 — Missing Official Paper PDFs

## Repository checkpoint

Audited `integration/combined-subject-banks` at commit `6898dfa9a14a0527b55b5f8765ff8fe958848c10` (2026-11-21).

- The subject registry contains Sanskrit (Code 07), but reports `papers_loaded: 0` and `questions_loaded: 0`.
- There is no Sanskrit question bank, Sanskrit staging/review file, or Sanskrit entry in the verification backlog.
- The archive manifest has 19 expected Sanskrit Paper-II sessions. Eighteen paper URLs listed below could not be retrieved during this audit; automated official-site reads failed. Their exact question ranges below follow the manifest's expected counts and still need confirmation against the PDFs.
- November 2025's official PDF URL returned a 16-page paper, but OCR is too noisy for transcription or visual verification. It is not requested again here; it remains an outstanding source-verification item.
- Official final answer keys for August 2017, November 2023, and December 2024 were discoverable on GSET's site. They do not replace the question-paper PDFs.

## Please upload these exact files

| Examination session | Expected question range | Official PDF required |
|---|---:|---|
| January 2002 | 1–50 | [jan0207.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/jan02/jan0207.pdf) |
| December 2002 | 1–50 | [dec0207.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec02/dec0207.pdf) |
| December 2003 | 1–50 | [dec0307.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec03/dec0307.pdf) |
| July 2004 | 1–50 | [jul0407.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/jy04/jul0407.pdf) |
| July 2006 | 1–50 | [jul0607.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/jul06/jul0607.pdf) |
| December 2008 | 1–50 | [dec0807.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec08/dec0807.pdf) |
| October 2010 | 1–50 | [oct1007.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct10/oct1007.pdf) |
| October 2011 | 1–50 | [oct1107.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct11/oct1107.pdf) |
| September 2013 | 1–50 | [sep1307.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/sep13/sep1307.pdf) |
| October 2014 | 1–50 | [oct1407.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct14/oct1407.pdf) |
| September 2016 | 1–50 | [sep1607.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/sep16/sep1607.pdf) |
| August 2017 | 1–50 | [aug1707.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/aug17/aug1707.pdf) |
| September 2018 | 1–100 | [sept1807.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/sep18/sept1807.pdf) |
| December 2019 | 1–100 | [dec1907.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec19/dec1907.pdf) |
| December 2021 (January 2022) | 1–100 | [dec2107.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec21/dec2107.pdf) |
| November 2022 | 1–100 | [nov2207.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/nov22/nov2207.pdf) |
| November 2023 | 1–100 | [nov2307.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2307.pdf) |
| December 2024 | 1–100 | [dec2407.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2407.pdf) |

Upload the original PDFs, including all pages and any figures. They are needed to recover and visually verify question text and all four options. No question or answer records will be invented from OCR or answer keys alone.

## Official archive references

- Question papers: https://www.gujaratset.ac.in/oldpap
- Final answer keys: https://www.gujaratset.ac.in/anskey
- Inventory basis: `assets/subjects/archive_manifest.json` on the audited integration branch.

## Remaining checkpoint

After these source PDFs are available, reconcile the questions against the canonical bank, recover staging records, compare final answer keys, and verify syllabus mappings. The November 2025 paper also needs page-by-page Devanagari proofreading because OCR alone is not reliable.
