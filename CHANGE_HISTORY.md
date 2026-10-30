# Change History

## 2026-10-30 — Initial durable repository audit
- Recorded branch heads, PR #16 merge and subject PR statuses.
- Created the project state, progress, verification and change-history registers.
- No question bank, loader, Paper-I or Code 01 source files changed.

## 2026-10-30 — Official syllabus and metadata reconciliation
- Commit `b76df8c65e191b558ed82841f098626a23194c3e`: added official GSET Code 28 Hindu Studies and Code 30 Music syllabus-unit records to `assets/subjects/syllabus_units.json`.
- Commit `4235ac24301e8be12053a011405a7a9863e0994f`: corrected Music `verification_pending.json`; reflected 146 remaining visual question-text reviews, 14 ambiguous plus 146 provisional mappings, and the recorded 300/300 answer-key visual checks.
- Commit `4aa9cdb2c2488e7ca052674b53c9e4fd9700a66f`: synchronized current integrated source/mapping/review counts in six subject descriptions in `assets/subjects/subjects.json`.
- Current integration run #18 completed Flutter analyze and combined Debug APK build successfully on commit `025dcce8a90ecfff3dd0ee14a256e8eca7b82131`; artifact ID `12957748495`.
- Metadata follow-up workflow runs #19–#21 were still in progress at the last check.
- No question text, option, answer, image, source URL, question ID, Paper-I code or Code 01 file was changed. No PR was merged and no branch history was force-pushed.

## 2026-10-30 — Integrated data structure and build verification
- Parsed and structurally checked the integrated 300-question banks for Codes 28–33: all six passed record-count, unique-ID, 100-per-session, question-number, English stem/options, answer-token, stored-key-parity and paper-manifest checks.
- Commit `4aa9cdb2c2488e7ca052674b53c9e4fd9700a66f` passed Integration Debug APK workflow run #21; Flutter analyze reported no issues and the combined Debug APK artifact was uploaded as ID `12958701650`.
- Current integration head before this register refresh: `4cef120441bdb8be9a525edea933b6a4d6926132`; run #22 is a docs-only push and was in progress at the last check.
- These structural checks do not replace original-paper visual proofreading or independent final-answer-key checking.
