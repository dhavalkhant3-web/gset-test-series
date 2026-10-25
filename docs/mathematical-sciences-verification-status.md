# Mathematical Sciences archive verification status

## Safety rule
Do not merge the recovered OCR archive into the app's production question bank until each question and all four options have been compared with the official GSET Paper-II question paper, and each answer has been compared with the official final answer key.

Official sources:
- Question papers: https://www.gujaratset.ac.in/oldpap
- Final answer keys: https://www.gujaratset.ac.in/anskey

## Recovered archive baseline
The recovered archive contains 1,111 records across 19 exam papers; the expected total based on the archive plan is 1,300, so 189 records are missing. All recovered records still require source verification; the archive's own audit found OCR corruption and incomplete/merged options in some records.

## Required per-question checks
- Match exact question number and wording to the official PDF.
- Match all four options, including mathematical notation, figures, matrices, superscripts and subscripts.
- Match answer to the official final answer key. A key value of Z means the question is not considered for evaluation and must not be converted to A-D.
- Never reconstruct missing content from memory or guess an answer.
- Keep `review_flag: true` and `source_verified: false` until all source checks pass.
- Record source URL and a concise review note for unresolved image/notation cases.
- Preserve the existing app UI and all other subject banks.

## Current status
NOT VERIFIED / NOT READY TO MERGE. This document is a tracking guard, not a claim that the archive has been checked. Use `scripts/validate_mathematical_sciences_bank.py` to fail closed if the app bank is absent, structurally invalid, or still contains unverified/review-flagged records.
