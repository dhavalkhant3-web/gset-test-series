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

## 2026-10-30 — Combined validator scope and metric corrections
- Commit `4e7c6b5fe12bcbdbbd0f8d638994c902c702ff2f`: expanded `tool/audit_combined_subject_banks.py` to include Codes 28 and 30, fixed bilingual session detection and Gujarati option checks, and counted `source_verified` independently from review flags.
- Adjusted `tool/validate_syllabus_mapping.py` to keep provisional/ambiguous/manual-review statuses unverified.
- Combined bank audit run #278 succeeded with zero errors. The integration Debug APK run #25 for the same commit was still in progress at the last check.
- No question-bank records, answer keys, Paper-I files or Code 01 files changed.

## 2026-10-30 — Physical/Chemical source-option audit
- Updated the combined validator to accept both `options_en` arrays and valid `options: {A,B,C,D}` dictionaries. Physical Sciences had 85 valid dictionary-format records that were previously false-positive invalids.
- Physical Sciences now has 213 genuinely incomplete option records; every one was already source_unverified and review_flagged. No question record was modified for Code 02.
- Chemical Sciences base has one malformed record: July 2006 Q42 has `options_en` as a single string. Added `review_flag=true` and a source-review note only; retained the original text and answer C. Official PDF source URL: `https://gujaratset.ac.in/assets/papers/paperII/jy06/jy0603.pdf`.
- Verified the Sep 2016 Paper-II overlay has 50 unique IDs, no overlap with the 1,250 base IDs, and all 50 carry source_verified=true; Q4 remains flagged with official key B. The 75 Paper-III questions remain in a separate file.

## 2026-10-30 — IKS/Public Administration syllabus repair and latest build checkpoint
- Commit `6534a6a682ceefe58034cc81a4d78d1653f53d5e`: fixed IKS Code 29 to the official ten units and Public Administration Code 32 to the correct ten-unit order, without changing question records or mapping statuses.
- Code 33's ten-unit catalogue remained unchanged. Code 31's UGC-NET Code65 syllabus PDF could not be retrieved fully; its unit list remains pending independent validation.
- Audit #279 and Debug APK #27 succeeded on commit `57198996bb867ade25684aee2a70a4f1c311118e`; artifact ID `12959312490`.
- CI status for the following syllabus-only commit `6534a6a682ceefe58034cc81a4d78d1653f53d5e` was not available from the status endpoint at the time of this checkpoint.


## 2026-10-31 — Exact-head audit/build recheck and register synchronization
- Rechecked the live integration head `62490790e5ef39a395f0034d4b351a673d52a9ab` and its parent `69ef1d3d7c0bbff250b42f902bde24d5ba594360`.
- Exact-head Combined subject bank audit run `41088721295`: PASS with `errors=[]`; paper-manifest mapping-status warnings remain for Codes 28–33 and are explicitly retained as unresolved.
- Exact-head Integration Debug APK run `41088721107`: PASS; Flutter analyze and Debug APK build passed. Artifact ID `12992539292`; SHA-256 `57e92302134618394a57415b77429c4844c00d31c5925374697f7f49a773ab1e`.
- Refreshed `MASTER_PROGRESS.md`, `PROJECT_STATE.json`, and `VERIFICATION_LOG.json` from the exact-head audit and workflow logs.
- No question-bank records, answer text, options, translations, source references, Paper-I code, or Code 01 files changed. No PR was merged. Flutter tests were not run because the current integration workflow has no `flutter test` step.


## 2026-10-31 — Paper-level mapping status synchronization
- Commit `99545b7f7923ad56afd752ed22961390823ffa8d` updated 55 paper entries across Codes 02, 03 and 28–33 so `unit_mapping_status` consistently reflects the still-pending question-level mapping state.
- Added a note clarifying that the paper remains pending while any question mapping is provisional, ambiguous or unmapped.
- No question-level mapping, question text, options, answers, Gujarati transcription, source URL, Paper-I code or Code 01 file was changed.
- Combined audit run #41163322599 passed with zero errors and all eight paper-metadata warning arrays empty. Public Administration validator #41163322559 passed.
- APK build #41163322554: Flutter analyze passed; Debug APK build was still in progress at this register update.


## 2026-11-03 — Public Administration and IKS mapping execution
- Public Administration Code 32: added provisional unit mappings to 128 records across the November 2023, December 2024 and November 2025 Paper-II banks. Current mapping status: 22 manually reviewed, 278 provisional, 0 pending. Source stem/options proofreading remains unverified for all 300; review flags were retained.
- IKS Code 29: added provisional unit mappings to 189 records across all three sessions. Current mapping status: 0 manually verified, 298 provisional, 2 pending (Dec 2024 Q20 and Nov 2025 Q15). All source-review flags remain active.
- Updated `assets/subjects/subjects.json`, Public Administration `papers.json`, and `MASTER_PROGRESS.md` to reflect current mapping counts.
- Relevant question-bank commits: PA `f39b9889e3f044348c31d74c869000d8bbd5fa4c`, `8af91e8653d9a076749016da154cc68d445401a4`, `e0246e4dfa0bbf59c496972503a94a126ad0e82b`, `a89475cbd6049b26b82316aee65716fa1d2ac953`; IKS `1f1e6d60517c22f60f8d11742dae579d4c158953`, `3e69faba612ff65ff7bab197e644c0a21af04a62`, `3afafdae07d97a5763a488dbfd0b73e76a042c53`, `cfb21c35849e1c670f445dcd0a0c89ec435a6eca`.
- Combined bank audit run `41583643015` passed on exact bank commit `7df69a43b64739b615caea1e7838bee259144085`; Public Administration validator `41583643030` was queued and Debug APK run `41583643012` remained in progress at the last check.
- No question stems, answer letters, options, Gujarati text, source references, Paper-I UI or Code 01 records changed; no PR was merged.


## 2026-11-03 — Music common-unit mapping review
- Manually reviewed 22 provisional syllabus assignments in Music Code 30 across December 2024 and November 2025 using the question topic and the official GSET Music syllabus: Units I–IV are common to all four streams. Unit mapping status now totals 162 manually reviewed, 14 ambiguous, and 124 provisional stream-specific assignments.
- Kept `review_flag=true` on all 22 records because this was mapping-only review; the 146 original-paper stem/options visual proofreading backlog remains unchanged (Dec 2024: 46; Nov 2025: 100). No answer, stem, option, Gujarati field or source URL was edited.
- Updated `assets/subjects/music/verification_pending.json`, `assets/subjects/subjects.json`, and `MASTER_PROGRESS.md` with the mapping counts. Updated `PROJECT_STATE.json` rollups for IKS, Music and Public Administration.
- Combined subject bank audit run `41583928078`: SUCCESS. Public Administration validator `41583928058`: SUCCESS. Debug APK run `41583928048`: Flutter analyze and widget tests passed; combined APK build was still in progress at the last check.
- No PR merged; Code 01 and Paper-I remain untouched.


## 2026-11-03 — Visual Art provisional mapping batch
- Added 34 provisional syllabus-unit assignments to Code 33 Visual Art November 2023 records using the official GSET Code 33 unit headings and question topic (fundamentals/color, traditional materials/techniques, Indian/Western art history, design/visual communication, cinema/animation, and contemporary Indian art).
- Mapping counts from the integrated bank now: 22 manually reviewed, 165 provisional, 113 pending. Original question visual-proofreading count and 14 content concerns are unchanged; provisional assignments are not source-verified.
- Updated `assets/subjects/subjects.json`, `MASTER_PROGRESS.md`, and `PROJECT_STATE.json` to synchronize counts. Combined bank audit run `41584155940` passed on metadata commit `9590778364d0d6fcf081e2cbbf0f094f87a09002`; Debug APK run `41584155869` was in progress and Visual Art validation `41584155887` was queued at last check.
- No question text, options, answer, Gujarati translation, source references, Paper-I or Code 01 files changed; no PR merged.
