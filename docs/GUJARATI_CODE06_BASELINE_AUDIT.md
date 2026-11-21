# Gujarati Code 06 — baseline audit

**Branch:** `feature/gujarati-code06-completion`  
**Base:** `integration/combined-subject-banks` at `6898dfa9a14a0527b55b5f8765ff8fe958848c10`  
**Audit date:** 2026-11-21  
**Scope:** Paper-II, Gujarati subject code 06 only.

## Repository baseline

The integration branch's `assets/subjects/subjects.json` registers `gujarati` (code `06`) with `papers_loaded: 0` and `questions_loaded: 0`. The recursive Git tree contains no `assets/subjects/gujarati/` directory or Gujarati question bank, paper manifest, answer-key files, syllabus mapping, or source PDFs. Accordingly:

- Existing papers: **0**
- Existing question records / IDs: **0**
- Duplicate records in bank: **0** (no bank exists to contain duplicates)
- Missing listed examinations: **18**
- Expected question numbers absent: **1,300 total expected questions across all sessions; 1,300 absent from the repository baseline**
- Transcription / source verification: **not started**
- Repository answer-key reconciliation: **0**
- Gujarati syllabus question mappings: **0**
- Historical “42 review records” checkpoint: **not applicable to this branch baseline**

No other subject files were changed. This is a baseline, not a completion claim. The archive inventory is based on links returned under Gujarati (Code 06) from the official GSET old-paper page. Question counts vary by exam era: the 12 sessions from January 2002 through August 2017 use the legacy 50-question format (600 questions); the seven sessions from September 2018 through November 2025 use 100 questions (700 questions). This yields 1,300 expected questions. The direct source PDFs and covers still need visual review during transcription.

## Official Paper-II inventory

The staging files supplied in this turn contain 600 unique question records across nine sessions. Exact duplicate file copies were counted once. The repository itself still has no imported bank at this point.

| Session | Official question paper | Expected Q | Staged Q | Repository Q | Missing from staging | Stage status |
|---|---|---:|---:|---:|---|---|
| January 2002 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/jan02/jan0206.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| December 2002 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec02/dec0206.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| December 2003 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec03/dec0306.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| July 2004 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/jy04/jy0406.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| July 2006 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/jy06/jy0606.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| December 2008 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec08/dec0806.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| October 2010 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/oct10/oct1006.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| October 2011 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/oct11/oct1106.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| September 2013 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/sept13/sept1306.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| October 2014 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/oct14/oct1406.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| September 2016 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/sept16/sept1606.pdf) | 50 | 0 | 0 | Q1–Q50 | Not yet transcribed |
| August 2017 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/aug17/aug1706.pdf) | 50 | 50 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| September 2018 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/sept18/sept1806.pdf) | 100 | 100 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| December 2019 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec19/dec1906.pdf) | 100 | 100 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| December 2021 (January 2022) | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec21/dec2106.pdf) | 100 | 100 | 0 | None | Transcribed in staging; proofreading/reconciliation pending |
| November 2022 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/nov22/nov2206.pdf) | 100 | 0 | 0 | Q1–Q100 | Not yet transcribed |
| November 2023 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/nov23/nov2306.pdf) | 100 | 0 | 0 | Q1–Q100 | Not yet transcribed |
| December 2024 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2406.pdf) | 100 | 0 | 0 | Q1–Q100 | Not yet transcribed |
| November 2025 | [PDF](https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2506.pdf) | 100 | 0 | 0 | Q1–Q100 | Not yet transcribed |

**Staging coverage:** January 2002 (50), December 2002 (50), December 2003 (50), July 2004 (50), December 2008 (50), August 2017 (50), September 2018 (100), December 2019 (100), December 2021 / January 2022 (100). **Total: 600/1,300 staged; 700 questions across 10 sessions remain untranscribed.**

## Final answer-key inventory

The official GSET answer-key page lists Code 06 Paper-II key PDFs for all 19 sessions. All are absent from the repository. Question-level reconciliation in the repository baseline remains **0/1,300**. The answer-key PDFs for January 2002, December 2002, December 2003 and December 2008 are labelled simply “Key for Paper-II” in the scans; their final-key status must be confirmed from the official archive context before marking reconciled.

| Session | Official final answer key |
|---|---|
| January 2002 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/jan02/jan0206.pdf) |
| December 2002 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec02/dec0206.pdf) |
| December 2003 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec03/dec0306.pdf) |
| July 2004 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/jy04/jy0406.pdf) |
| July 2006 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/jy06/jy0606.pdf) |
| December 2008 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec08/dec0806.pdf) |
| October 2010 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/oct10/oct1006.pdf) |
| October 2011 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/oct11/oct1106.pdf) |
| September 2013 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/sept13/sept1306.pdf) |
| October 2014 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/oct14/oct1406.pdf) |
| September 2016 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/sept16/sept1606.pdf) |
| August 2017 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/aug17/aug1706.pdf) |
| September 2018 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/sept18/sept1806.pdf) |
| December 2019 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec19/dec1906.pdf) |
| December 2021 (January 2022) | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec21/dec2106.pdf) |
| November 2022 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/nov22/nov2206.pdf) |
| November 2023 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/nov23/nov2306.pdf) |
| December 2024 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2406.pdf) |
| November 2025 | [PDF](https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2506.pdf) |

## Official syllabus

The GSET Gujarati syllabus is available at [Code 06 syllabus PDF](https://gujaratset.ac.in/assets/syllabus/06.pdf). Question-level unit/topic mapping has not started.

## Validation and CI baseline

The integration branch includes `tool/audit_combined_subject_banks.py`, `tool/validate_questions.py`, and `tool/validate_syllabus_mapping.py`, plus combined-bank GitHub Actions. The combined audit's current `IN_SCOPE` list does not include Code 06, and no Gujarati bank exists for the validator to inspect. The validation workflow must be extended only when the Gujarati files and schema are implemented; no validation was run in this remote audit.
