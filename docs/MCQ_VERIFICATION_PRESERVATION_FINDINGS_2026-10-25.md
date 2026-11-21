# MCQ & Verification Preservation Findings
Date: 2026-10-25

## User's required outcome
Preserve every existing subject bank and all legitimate question-level source-verification status. Physical Sciences target: 1,446 Paper-II questions. Chemical Sciences target: 1,300 Paper-II questions. Other integrated subjects and their question banks must remain present. Do not rebuild from scratch, blindly overwrite files, or erase source-review history.

## Verified current-main bank counts (read directly from Git blobs)
- Physical Sciences main `questions.json`: 1,300 parseable records, 1,300 unique IDs across 19 Paper-II sessions. Separate `questions_sep16_p2.json`: 50 IDs, but those IDs overlap the main bank's `physical_sep16_q01..q50`; **do not append** this supplement as new questions.
- Chemical Sciences main `questions.json`: 1,250 parseable records, 1,250 unique IDs across 18 sessions. Separate `questions_sep16_p2.json`: 50 IDs for `chemical_sep16`; they do not appear in main bank's parsed record IDs, so the loader should append this supplement to reach 1,300. Ensure the Paper-III 75-question file remains excluded from Paper-II.
- The counts in main `subjects.json` at the time of audit say Physical Sciences `questions_loaded: 225`, even though its data_status says 1,300 Paper-II archive records; this subject summary is stale/inconsistent. Chemical Sciences metadata says 1,300 including the September 2016 overlay.
- Physical `papers.json` has 19 Paper-II entries plus a 75-question Paper-III entry. Its Paper-II sum is 1,300, Paper-III separate = 75. Do not combine Paper-III into the Paper-II count.
- Chemical `papers.json` has 19 Paper-II entries including the September 2016 overlay (1,300 total) plus a separate 75-question Paper-III entry. Do not count Paper-III in Paper-II totals.

## Historical evidence and risk
- The integration PR #16 was merged with merge commit `bedd33e6536e4eb35823049d62e1889c3f75e7a7`.
- Compare merge commit against current `main`: current main has three commits on top. Two large bank files were modified:
  - Physical Sciences: 8,584 additions and 2,514 deletions in the aggregate comparison.
  - Chemical Sciences: 8,744 additions and 2,499 deletions in the aggregate comparison.
  These changes appear associated with subject data cleanup, language fields, and provisional syllabus mapping, but require record-level comparison to prove no question stems/options/answers or prior verification fields were lost.
- Commit `50b85a8f9a7e8cff2cb8be836d470cba50226912` is titled “Clear non-source Gujarati fields for English-only Subject 02”.
- Commit `55220b3243a4a2d712ca7ceae18054e980e2e2df` is titled “Clear non-source Gujarati fields for English-only Subject 03”.
- Later `b27abb7f156f279e47a4d97bd2e5cfde79cf481f` says “Restore previously populated Gujarati MCQ fields without changing question banks”.
- For Physical Sciences, 1,300 main-bank IDs match current Paper-II count, but the user's remembered target is 1,446. The known 1,300-record historical valid source also only has 1,300 records. The earlier historical file at commit `891ec10eeb8f12d555e4f792d2243d8b665886ac` was malformed around physical Oct 2011 Q18; do not restore it wholesale.
- The exact old APK uploaded in this task contained 1,300 Physics main-bank questions and 1,250 Chemistry main-bank questions, plus supplements/assets; it does not alone prove 1,446 Physics questions were in that APK.
- Earlier connector calls yielded empty contents for some large files, but raw Git blob reads later succeeded. Never interpret a connector's empty response as an actually empty file.

## Verification-preservation observations
- Current Physical Sciences `papers.json` tracks question-level `source_reviewed_question_count` and `review_flags_remaining_count`; there are many records with partial review. Preserve all existing review flags, answers, official source URLs, page provenance, and source-verified booleans. Do not bulk flip fields.
- Current Chemical Sciences `papers.json` also has per-paper source-review counts and outstanding review flags. Preserve these as well.
- The merged integration branch contains subject validators; current main should continue preserving those scripts/workflows.
- Metadata may have stale counts, but metadata must be corrected only after record-level source verification and actual loader behavior are established.

## Required recovery steps
1. Compare current-main question objects against merge commit `bedd33e...` for Physical Sciences and Chemical Sciences, field-by-field, including IDs, stems, options, answer, source URLs, `source_verified`, `review_flag`, `review_note`, and source-page fields. Summarize field loss by count; do not blindly restore any field without knowing whether it is source-based.
2. Search earlier repository history and all accessible legacy assets for the user's remaining 146 Physical Sciences Paper-II records. Do not count Paper-III, duplicates, or the already-overlapping September 2016 supplement.
3. For Chemical Sciences, validate the loader appends the 50-question September 2016 Paper-II supplement exactly once and excludes Paper-III. Preserve official-key reconciliation and the remaining Q4 review flag.
4. Audit the other merged subject banks; never replace them with a smaller staged copy merely because it has a convenient branch name.
5. Apply only minimal fixes on `recovery/mcq-bank-safety-audit`, add count and field-preservation tests, run Python subject validators and Flutter build; open a draft PR only. Do not merge automatically.
