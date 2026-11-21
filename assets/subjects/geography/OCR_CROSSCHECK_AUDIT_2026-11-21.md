# Geography Code 24 — OCR Cross-check Audit (2026-11-21)

## Scope
This audit cross-checks the November 2023 and December 2024 question-bank text against OCR extracted from the corresponding uploaded official question-paper page scans.

**Important:** OCR corroboration is not human visual sign-off. It does not authorize setting `source_verified=true` or activating questions. The earlier correction remains in force: the prior signed-off checkpoint was 129/300, with 171 still requiring verified source-level sign-off.

## Results

| Paper | OCR pages | Question blocks found | High OCR corroboration | Manual visual check required |
|---|---:|---:|---:|---:|
| November 2023 | 30 | 100/100 | 93 | 7 |
| December 2024 | 30 | 98/100 | 67 | 33 |
| **Total** | **60** | **198/200** | **160** | **40** |

The high-corroboration threshold requires strong question-stem token coverage and option-text similarity. OCR errors, unusual formatting, and missing blocks are conservatively sent to manual visual review.

## Mandatory follow-up
1. Manually compare all 40 flagged questions with the corresponding original page images.
2. Independently inspect the 160 high-corroboration questions before changing any source-verification flag; OCR alone is insufficient.
3. Reconcile the canonical `questions.json` flags and `papers.json` counters against a question-level signed-off ledger.
4. Keep all 300 new questions review-only until official Code 24 syllabus mappings are independently reviewed.
5. Run the Geography validator and confirm the GitHub Actions run before reporting CI as PASS.

## Integrity rule
Do not treat OCR matches, page-image availability, answer-key parity, or four populated options as a substitute for question-by-question visual verification. Preserve the official final answer key as authoritative and do not infer missing text.
