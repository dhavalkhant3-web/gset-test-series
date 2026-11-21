# Geography Code 24 — verification correction (2026-11-21)

This correction supersedes any broader claim that all 300 new records have completed question-by-question visual sign-off.

Verified locally from the supplied staging JSON:
- 300 records; 300 unique IDs.
- Q1–Q100 present for December 2021/January 2022, November 2023 and December 2024.
- Four non-empty English option strings in all 300 records.
- 300/300 answer letters match the supplied official final-key JSON.
- JSON parses and the above structural/key checks return zero errors.

Visual source review:
- An earlier detailed checkpoint recorded 129/300 question-level visual verifications (2021: 100/100; November 2023: 29/100; December 2024: 0/100).
- The page images for the remaining 2023 and 2024 papers are now available and have been opened/reviewed as page images; however, the full question-by-question transcription-to-image sign-off has not yet been recorded for the remaining 171 records.
- The 32 previously incomplete option records now have four option slots and their relevant source pages have been inspected. Do not treat four-option completeness alone as proof of full stem transcription.

Safety:
- Keep all 300 new records review-only; do not promote them into active test use.
- The current canonical source_verified flags and papers.json counters need reconciliation against the 129 signed-off records before any release.
- Official syllabus-unit mapping remains pending for the 300 new records.
- September 2018 Q7–Q100 (94 questions) remain untranscribed.

Validation/CI:
- tool/validate_geography_bank.py and .github/workflows/geography-code24-validation.yml exist on this branch.
- A Geography-path commit was made to request a workflow trigger. The available GitHub connector returned no workflow run or commit status for that commit; therefore CI is NOT certified PASS.
- Full project schema validation has not yet been run locally because the GitHub connector returns an empty content payload for the large canonical questions.json file.
- Do not merge PR #22.
