# Sanskrit Code 07 — Official Source Retrieval Checkpoint

## Repository status (2026-11-21)

The latest head of [PR #22](https://github.com/dhavalkhant3-web/gset-test-series/pull/22), `bc439768d494719a3669613d70d05cdc62807fbe`, contains the Sanskrit Code 07 work. It has not yet been merged into `integration/combined-subject-banks`.

- 192 active and 658 review-only questions: 850 unique IDs, no overlap.
- All 850 records have a stem and four options.
- Active: 192 source verified, 192 answer-key verified; 184 syllabus mappings verified and 8 pending.
- Review-only: 108 source verified and 550 not source verified; 456 answer-key verified and 202 pending; 106 mappings verified and 552 pending. All 658 remain review flagged.
- Separate answer-key staging has 300 key-only entries; these are not question records.
- The source-audit mapping totals are 290 verified and 560 pending.

## Official October session PDFs retrieved

The earlier audit said October 2010, October 2011, and October 2014 materials were missing. Direct retrieval from the official GSET host (without `www`) now succeeds for all six PDFs. No upload is needed for these sessions.

| Session | Paper-II question paper | Official answer key |
|---|---|---|
| October 2010 | [oct1007.pdf — 10 pages](https://gujaratset.ac.in/assets/papers/paperII/oct10/oct1007.pdf) | [oct1007.pdf — 1 page](https://gujaratset.ac.in/assets/anskey/paperII/oct10/oct1007.pdf) |
| October 2011 | [oct1107.pdf — 10 pages](https://gujaratset.ac.in/assets/papers/paperII/oct11/oct1107.pdf) | [oct1107.pdf — 1 page](https://gujaratset.ac.in/assets/anskey/paperII/oct11/oct1107.pdf) |
| October 2014 | [oct1407.pdf — 16 pages](https://gujaratset.ac.in/assets/papers/paperII/oct14/oct1407.pdf) | [oct1407.pdf — 1 page, final/corrected key](https://gujaratset.ac.in/assets/anskey/paperII/oct14/oct1407.pdf) |

The official old-paper archive was also retrieved at https://gujaratset.ac.in/oldpap. The `www.gujaratset.ac.in` host failed automated retrieval for some URLs, while the same official `gujaratset.ac.in` URLs succeeded.

## Remaining checkpoint

These six sources still need to be reconciled into the question-bank workflow. OCR retrieval alone does not count as Sanskrit transcription or visual verification. Continue the existing review queue without promoting recovered records until source, answer-key, and syllabus evidence is checked.

## Correction history

Earlier versions of this checkpoint first overlooked PR #22 and then listed these three sessions as missing. Both claims are superseded: PR #22 contains the existing subject bank, and all six October-session PDFs above are now retrievable from the official GSET host.
