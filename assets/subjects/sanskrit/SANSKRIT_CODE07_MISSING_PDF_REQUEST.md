# Sanskrit Code 07 — Current Work and Remaining Source Request

## Corrected repository audit (2026-11-21)

I rechecked the open [PR #22](https://github.com/dhavalkhant3-web/gset-test-series/pull/22), head `bc439768d494719a3669613d70d05cdc62807fbe`. Sanskrit Code 07 work is already present there. It has not yet been merged into `integration/combined-subject-banks`; that integration branch still reports zero Sanskrit questions.

PR #22 contains:

- `questions.json`: 192 active records.
- `questions_review_pending.json`: 658 review-only records.
- 850 total unique question IDs across active and review-only records; no overlap or duplicate IDs.
- All 850 have a question stem and four English options.
- Active records: 192 source verified, 192 final-answer-key verified, 184 syllabus mappings verified, 8 mappings pending.
- Review-only records: 108 source verified and 550 not source verified; 456 final-answer-key verified and 202 not verified; 106 syllabus mappings verified and 552 pending. All 658 remain review flagged.
- `answer_keys_staging.json`: 300 answer-key-only entries across five sessions. They are not question records and must remain separate.
- `papers.json`: 11 paper sessions represented.

The queue reconciliation in `source_audit.json` agrees on 850 unique questions and 658 review-only records. Its recorded mapping totals are 290 verified and 560 pending (184+106 verified; 8+552 pending).

## Please provide only these missing sessions

The PR #22 staging note says these question papers and answer keys were not included in the materials received. Each paper is expected to contain questions 1–50. Please upload both PDFs for each session if available:

| Session | Official Paper-II question paper | Official final answer key |
|---|---|---|
| October 2010 | [oct1007.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct10/oct1007.pdf) | [oct1007.pdf](https://www.gujaratset.ac.in/assets/anskey/paperII/oct10/oct1007.pdf) |
| October 2011 | [oct1107.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct11/oct1107.pdf) | [oct1107.pdf](https://www.gujaratset.ac.in/assets/anskey/paperII/oct11/oct1107.pdf) |
| October 2014 | [oct1407.pdf](https://www.gujaratset.ac.in/assets/papers/paperII/oct14/oct1407.pdf) | [oct1407.pdf](https://www.gujaratset.ac.in/assets/anskey/paperII/oct14/oct1407.pdf) |

Do not re-upload the other 16 sessions on the basis of this request. The current PR contains question records, source references, or separate answer-key staging for those sessions; their review flags and pending counts are recorded above.

## Remaining checkpoint

After the three missing sessions are available, add/reconcile their question records and final keys if the official PDFs support them. Continue visual Sanskrit proofreading, key reconciliation for the 202 unverified review-only records, and official syllabus mapping for the 560 pending records. Keep recovered records review-only until their evidence supports promotion.

## Correction note

An earlier version of this file incorrectly said the repository had no Sanskrit bank and requested 18 PDFs. That statement came from checking only the integration branch and missing the existing open PR #22. This corrected version supersedes it.
