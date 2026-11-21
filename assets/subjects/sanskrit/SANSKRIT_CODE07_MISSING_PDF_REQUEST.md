# Sanskrit Code 07 — Official Source Retrieval Checkpoint

## Repository status (2026-11-21)

The latest head of [PR #22](https://github.com/dhavalkhant3-web/gset-test-series/pull/22) is `52e46c1a6e0c505906bc7765d6934a59994f0284`. It contains Sanskrit Code 07 data and source-retrieval updates, but remains unmerged into `integration/combined-subject-banks`.

- 192 active + 658 review-only question records = 850 unique IDs, with no active/queue overlap.
- All 850 records have question stems and four options.
- Active: 192 source verified and answer-key verified; 184 syllabus mappings verified, 8 pending.
- Review-only: 108 source verified, 550 not source verified; 456 answer-key verified, 202 pending; 106 syllabus mappings verified, 552 pending. All 658 remain review flagged.
- Separate answer-key staging now contains 450 entries across eight sessions; these are not question records.

## Official October session PDFs retrieved

Direct official GSET URLs (host without `www`) return the question papers and answer keys:

| Session | Paper-II question paper | Official answer key |
|---|---|---|
| October 2010 | [oct1007.pdf — 10 pages](https://gujaratset.ac.in/assets/papers/paperII/oct10/oct1007.pdf) | [oct1007.pdf — 1 page](https://gujaratset.ac.in/assets/anskey/paperII/oct10/oct1007.pdf) |
| October 2011 | [oct1107.pdf — 10 pages](https://gujaratset.ac.in/assets/papers/paperII/oct11/oct1107.pdf) | [oct1107.pdf — 1 page](https://gujaratset.ac.in/assets/anskey/paperII/oct11/oct1107.pdf) |
| October 2014 | [oct1407.pdf — 16 pages](https://gujaratset.ac.in/assets/papers/paperII/oct14/oct1407.pdf) | [oct1407.pdf — 1 page, final/corrected key](https://gujaratset.ac.in/assets/anskey/paperII/oct14/oct1407.pdf) |

The 150 official answer choices were added to `answer_keys_staging.json` on PR #22. The 2010 and 2011 PDFs are headed “KEY FOR PAPER-II”; final-key status is not explicit there. The 2014 PDF is explicitly a final/corrected key. They remain separate from the question bank because the corresponding question text has not been transcribed into records yet.

## Remaining checkpoint

Transcribe and visually proofread the three question papers, establish final-key status for October 2010 and October 2011 where possible, reconcile their 150 questions, then continue the existing review queue. Do not promote OCR-only text or unconfirmed keys as verified.

## Correction history

An earlier checkpoint overlooked PR #22 and asked for 18 papers. That request was incorrect. The three October source pairs were then found on the official GSET host, and their answer choices were staged in the PR #22 branch.
