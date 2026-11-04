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


## 2026-11-03 — Performing Arts provisional mapping batch
- Added 36 provisional syllabus-unit assignments to Code 31 Performing Arts December 2024 questions using the registered ten-unit syllabus catalog and question topics (Indian cultural history, folk/traditional forms, Natyashastra, aesthetics, international dance, pedagogy and drama/theatre theory). Stream-specific Unit 6 assignments remain provisional where stream identification is not established.
- Current mapping counts: 0 verified, 171 provisional, 129 pending. Source-review progress remains unchanged: 94 source pages visually verified, 200 text/transcription checks pending, 6 bilingual discrepancies flagged and 206 review flags retained.
- Updated `assets/subjects/subjects.json`, `MASTER_PROGRESS.md`, and `PROJECT_STATE.json`.
- Combined subject bank audit run `41584320487` and Public Administration validator run `41584320497` passed on metadata commit `b255ff5d0669cdd3a7191315a6b03b507f2a4a44`. Debug APK run `41584320491` was in progress (Flutter analyze step running) at last check.
- No question stems, options, answers, Gujarati transcription, source references, Paper-I or Code 01 files changed; no PR merged.


## 2026-11-03 — Visual Art mapping batch 2
- Added 83 provisional syllabus-unit assignments to Visual Art Code 33 records across December 2024 and November 2025 (Indian/Western art history, traditional media/printmaking, design/typography, East Asian art and digital photography/visual technology). All unit assignments remain provisional; source review and 14 content concerns are unchanged.
- Visual Art mapping counts now total 22 manually reviewed, 248 provisional, 30 pending. Across today's two Visual Art batches, 117 provisional assignments were added; source proofreading remains 256 pending.
- Updated `assets/subjects/subjects.json`, `MASTER_PROGRESS.md`, and `PROJECT_STATE.json`.
- Combined audit run `41584513117` and Public Administration validation run `41584513079` passed on manifest commit `270994d07386a694fce97efd8bb86dc546573dfd`. Debug APK run `41584513093` remained in progress at last check.
- No question text/options/answers/source references changed; no flags cleared; no PR merged.


## 2026-11-03 — Visual Art remaining mapping fields
- Assigned provisional syllabus units to the remaining 30 Code 33 Visual Art records (including figure-based sculpture/painting questions and broad sculpture-function items), bringing the bank to 22 manually reviewed, 278 provisional, and 0 unmapped/pending assignments.
- Figure-dependent mappings were inferred only from the visible question wording/options and linked figure asset metadata; the actual image bytes were not inspected. All 30 remain provisional, and no source text/option proofread status or review flag was changed. The 256 source proofreading checks and 14 content concerns remain open.
- Updated `assets/subjects/subjects.json`, `MASTER_PROGRESS.md`, and `PROJECT_STATE.json`.
- Combined bank audit run `41584664171` and Public Administration validation `41584664295` passed on subject-manifest commit `580dc4c703e1fbae1618aa9cbf67b5f20ab90fe5`. Debug APK run `41584664153` remained in progress at last check.
- No question text/options/answers/source refs changed; no PR merged.


## 2026-11-03 — Continued provisional syllabus field completion
- Public Administration Code 32: filled 28 previously null question-level unit fields using narrowly targeted explicit topic phrases matched against the registered official syllabus. Distribution: Unit I=7, Unit III=11, Unit V=1, Unit VIII=7, Unit X=2. Corrected Nov 2025 Q39 (73rd Constitutional Amendment/Panchayati Raj) to provisional Unit IV after inspecting the matched item. All mappings remain provisional; review flags, stems, options, answers, Gujarati fields and sources unchanged.
- Performing Arts Code 31: filled 21 previously null question-level unit fields using explicit subject terms. Distribution: Unit I=6, Unit II=5, Unit III=3, Unit VI=6, Unit VIII=1. Stream-specific unit scope and visual/source checks remain pending; all mappings provisional and flags retained.
- Commits: Public Administration mapping batch `e68195d5991cf9273111c99c8912f59ddd85a2f3`; Panchayati Raj mapping refinement `a9839ef83e7b05d6ef8ed25f4934832c07f3325c`; Performing Arts mapping batch `005e79ee91d9d059c890433340e860c0da9354ec`.
- Exact-head combined subject bank audit on `a9839ef83e7b05d6ef8ed25f4934832c07f3325c`: PASS. Public Administration bank validator on the same commit: PASS. Debug APK run `41590949177` had Flutter analyze and widget tests PASS; APK build was still running at this note.
- No PR merged; Code 01 and Paper-I untouched. No source text, options, answers, translations or verification flags were changed.


## 2026-11-03 — Mapping field-count synchronization
- Updated `assets/subjects/subjects.json` Code 31 and Code 32 data_status to distinguish filled `unit_number` fields from mapping status labels. Public Administration: 22 manually reviewed + 180 provisional unit values assigned; 98 unit fields null. Performing Arts: 156 provisional unit values assigned; 144 unit fields null (27 null fields still carry provisional status labels, 117 carry pending labels). Source flags are unchanged.
- Manifest commit: `9c425a8c85783c92faf83a15e40e23375a0918c5`. No question records or verification fields changed in this manifest update.


## 2026-11-03 — Structured syllabus unit field synchronization
- Public Administration Code 32: 98 null `unit_number`/`unit_id` fields filled from existing provisional `syllabus_unit` numeric values. Commit `5c70c23f90b441c370878d572ca8800bd7321a47`.
- Visual Art Code 33: 147 null unit fields filled from existing provisional `syllabus_unit` numeric values. Commit `4a6ec7deef5d630197a6c5403ceb0f58f7e193ab`.
- IKS Code 29: 189 null unit fields filled from existing provisional `syllabus_unit` numeric values; two pending values left null. Commit `63472b71a6e28028104a781a7ac43286f05df8e8`.
- Hindu Studies Code 28: all 300 structured `unit_number`/`unit_id` fields populated from existing `syllabus_unit` labels; status labels and review flags retained. Commit `3091e2f9fd60bf97cc44f6708a3032eb7df2e0be`.
- Subject registry reconciled in commit `3830783effb66cf62379be43f6119d7d62f1d0c1`; master progress entry appended in `35f92c5b245423fd809c6142447207dc7c20fd6d`.
- Changes synchronize already-present mapping labels only. They do not constitute source-PDF verification or mapping-status promotion.


## 2026-11-03 — Verification and progress-register refresh
- `PROJECT_STATE.json` refreshed with exact audit/validator/build run IDs, latest unit-field sync counts and APK artifact metadata (commit `35f2d9ccfadb21e7cbeb1e2a02caecceaf703eb1`).
- `VERIFICATION_LOG.json` records the combined audit PASS (`41594284815`), Public Administration validation PASS (`41594284715`), and APK workflow PASS (`41594322933`), including Flutter Analyze, widget tests, APK build and upload (commit `768f0347cacabf973a6fa5a66b370ec169b3fa9c`).
- `MASTER_PROGRESS.md` synchronized with these evidence-based results (commit `c6c4b285089d518f438aceceff4918629a0cbd38`).
- No original PDF visual proofreads completed in this documentation checkpoint. No source data changed, no review flag cleared, no PR merged; Code 01 and Paper-I remain untouched.


## 2026-11-03 — Music November 2025 source-page recheck (Q65–Q98)
- Commit `ebcc2a4fded8ab5fabb732f87470294bd506776c` visually proofread Q65–Q98 against the original official bilingual paper, printed pages 21–30.
- 34 question-text source_verified promotions; question review flags retained for mapping/content reconciliation. Corrections include Gujarati option transcription Q85, Q91, Q92 and Q97, plus source-based Gujarati passage text for Q87–Q90.
- Distinct November 2025 source-page comparison count is 53/100 (13 records overlap earlier source-page batch); 47 remain visual proofread. Music total 207/300 visual proofread, 93 pending. Official answer keys checked 300/300. No PR merge; Code 01/Paper-I untouched.


## 2026-11-03 — Music November 2025 Paper-II fully source-proofread
- Commit `be99ee33416ca6f105a80e1fae4fb4a044170286`: all 100 questions on printed pages 3–31 visually compared against the official bilingual source scan; English/Gujarati stems, option arrays/order and paragraph text proofread. Question-text source verification is 100/100 for Nov 2025; official answer-key verification remains 100/100.
- Music total visual proofread 254/300; 46 December 2024 questions remain. Mapping totals unchanged (162 manually reviewed, 14 ambiguous, 124 provisional); all review flags remain. No PR merged; Code 01/Paper-I unchanged.


## 2026-11-03 — Music Code 30 final December 2024 source-proofreading batch
- Commit `686aca9d2b442b36eaa1f17b7cc08b817067738a`: visually proofread GSET December 2024 Music Paper-II Q76–Q90 and Q96–Q100 against official source scan printed pages 23–28 and 30–31. Corrected OCR-damaged Gujarati in Q81, Q83, Q85, Q89 and Q90; normalized Q79 English wording. Set source_verified true for the 20 visually checked questions. No answer or official key values changed; review flags were retained for independent mapping/content review.
- Commit `adb249822521c9271d7cd991f1fbb7cb9727539b`: updated Music `verification_pending.json` to record 300/300 source visual proofreading complete, 0 text-proofreading questions remaining. Mapping backlog remains 14 ambiguous + 124 provisional, and 212 review flags stay active.
- Final Music question-bank integrity scan: 300/300 records, 300/300 source_verified, 0 blank Gujarati stems/options, 0 stored answer vs official_answer mismatches. No PR merge, Paper-I changes or Code 01 changes.


## 2026-11-04 — Public Administration Code 32 source verification tranche 2
- Added source verification for 34 questions: Dec 2024 Q8–Q23 (16 items) and Nov 2025 Q7–Q16 plus Q18–Q25 (18 items), visually compared against original official GSET Paper-II PDF pages and final keys.
- Stems/options matched; stored answers equal final key letters. No question content or answer values were modified. Review flags and syllabus mapping statuses retained.
- Running source verification total: 37/300; pending 263; provisional mapping count unchanged at 278.


## 2026-11-04 — Public Administration Code 32 source verification tranche 3
- Commit batch updates source verification for Dec 2024 Q36–Q40 and Nov 2025 Q36–Q40, ten items. Original official PDF pages visually matched; final answer key letters match JSON answers.
- Running source-verified count 47/300; 253 pending. Provisional mappings 278 unchanged; active flags retained. No source question or answer rewritten.


## 2026-11-04 — Public Administration Code 32 source verification tranche 4
- Source-verified Dec 2024 Q41–Q46 and Nov 2025 Q41–Q46 against official PDF page images and official final answer keys (12 records).
- All stems/options and stored answer letters matched; no source content edited. Running source verified 59/300, 241 pending; provisional mappings 278 unchanged, review flags retained.


## 2026-11-04 — Public Administration Code 32 source verification tranche 5
- Source-verified Dec 2024 Q47–Q50 and Nov 2025 Q47–Q50 (8 items) using official page images and final answer keys; stems/options and answer letters match.
- Running count 67/300 source verified, 233 pending; 278 provisional mappings unchanged. Review flags retained; no PR merge or Code 01/Paper-I edits.


## 2026-11-04 — Public Administration Code 32 source verification tranche 6
- Verified Dec 2024 Q51–Q54 and Nov 2025 Q51–Q54 (8 records) against official source PDF page images and final answer keys. Stem/options and key letters matched.
- Running source verified 75/300, pending 225; 278 provisional mappings unchanged. Flags retained; no PR merge, Code 01/Paper-I untouched.


## 2026-11-04 — Public Administration Code 32 source verification tranche 7
- Source-verified Dec 2024 Q55–Q60 and Nov 2025 Q55–Q60 (12 records) against official source PDF page images and final answer keys. Stems/options and stored answer letters matched.
- Running source-verified total: 87/300; pending 213. Provisional mappings 278 unchanged; review flags retained. No PR merge; Code 01/Paper-I untouched.


## 2026-11-04 — Public Administration Code 32 source verification tranche 8
- Source-verified Dec 2024 Q61–Q65 and Nov 2025 Q61–Q65 (10 records) against official PDF page images and final answer keys; stems/options and stored answer letters matched.
- Running source-verified total: 97/300; pending 203. Provisional mappings 278 unchanged; review flags retained. No PR merge; Code 01/Paper-I untouched.


## 2026-11-04 — Public Administration Code 32 source verification tranche 9
- Source-verified Dec 2024 Q66–Q70 and Nov 2025 Q66–Q70 (10 records) against official PDF page images and final answer keys; stems/options and stored answer letters matched.
- Running source-verified total: 107/300; pending 193. Provisional mappings 278 unchanged; review flags retained. No PR merge; Code 01/Paper-I untouched.


## 2026-11-04 — Public Administration Code 32 source verification tranche 10
- Source-verified Dec 2024 Q71–Q75 and Nov 2025 Q71–Q75 (10 records) using official question-paper page images and official final answer keys; stems/options and answer letters match.
- Running total: 117/300 source verified; 183 pending. Provisional mappings 278 unchanged; review flags retained.
- No PR merge, Paper-I change or Code 01 change.


## 2026-11-04 — Public Administration Code 32 answer-key reconciliation batch 11 (visual review pending)
- Reconciled Dec 2024 Q76–Q80 and Nov 2025 Q76–Q80 against official final answer keys; all 10 answer letters match existing bank records.
- Original question-paper visual check pending, so source_verified remains 117/300; 183 pending. Review flags retained; no Paper-I/Code 01 change and no PR merge.
