# Team 3 Sanskrit & Environmental Sciences Integrity Audit

Date: 2026-11-18
Audit source: Open PR #22 head `eaed58933107b6a2bb51dff0358381a23db2716a`
Target branch for this report: `warroom/team-3-sanskrit-integration`
Base integration HEAD at branch creation: `6898dfa9a14a0527b55b5f8765ff8fe958848c10`

## Scope and safety
- This report only; no subject question-bank files, manifests, registry entries, Paper-I UI, or other teams' data were changed.
- No PR was merged.
- The PR #22 head was inspected as an evidence source only. It is not the integration base.

## Sanskrit (Code 07)

### Observed canonical data
- `questions.json`: 192 records; 192 unique IDs.
- All 192 have `source_verified=true`, `answer_key_verified=true`, `review_flag=false`.
- 184 records have `syllabus_mapping_status=verified`; 8 do not have that verified status.
- All 192 have a non-empty stem, an answer, and exactly four English options.

### Staging sidecar
- `answer_keys_staging.json` contains five answer-key-only sessions: SEP2016 (50), SEP2018 (100), JAN2002 (50), JUL2004 (50), JUL2006 (50).
- Total answer-key-only entries: 300. These are not question transcriptions and must not be promoted to question records.
- This sidecar is distinct from the reported 550 recovered question records.

### Conflicting audit/registry claims
- `source_audit.json` reports `transcribed_questions=850`, `active_questions=192`, and `pending_review=108`.
- The same audit reports a 550-record recovery and a review queue count of 658 in one field, but its integrity narrative says 704 unique review records; it also says 665 key-applied records plus 39 review-required records.
- Its `canonical_file_reconciliation` instead claims 192 active + 658 review-only = 850, with no missing IDs.
- The subject registry at the PR head says 146 active + 704 review-only = 850.
- The retrieved canonical `questions.json` has 192 records, not 146 or 850.
- `questions_review_pending.json` could not be reliably read by the GitHub file-content connector in this audit, despite PR #22's diff reporting a large added file. Its record count must therefore be treated as unverified until read via an alternate reliable path.

### Conclusion
The claimed 550 recovered question records are described in the audit as review-only records sourced from a consolidated staging file, but the canonical JSON and registry/audit counters are not mutually consistent. Do not mark 550 recovered records as confirmed present until the actual review queue bytes are fetched and IDs are reconciled. Do not confuse the 300 answer-key-only entries with question records.

## Environmental Sciences (Code 26)

### Observed canonical data
- `questions.json`: 300 records, 300 unique IDs.
- All 300 have `source_verified=true`, `answer_key_verified=true`, `review_flag=false`, and `syllabus_mapping_status=verified`.
- All have a non-empty stem, answer, and exactly four English options.
- `papers.json` contains three papers with 100 records each: November 2023, December 2024, November 2025. Each paper entry reports source, final-key, and syllabus mapping verification complete.

### Conflicting audit/registry claims
- The registry at the PR head reports 95 active + 205 review-only and states only 95/300 source-page visually verified.
- The same registry reports 300/300 syllabus mappings verified.
- `source_audit.json` reports 300 transcribed, 300 official-key matches, 300 visually checked, 300 active, and zero pending review, but also says 291 are pending a second proofreading pass.
- These counters describe different review dimensions but are not clearly reconciled in the registry. Canonical per-question flags are all green, whereas the registry's active/review split is not.

### Conclusion
The 300 canonical records are structurally complete and carry verified flags at question level. However, registry/source-audit disagreement must be resolved before declaring the subject fully verified. The reported second proofreading pass of 291 records should remain a separate quality-control status; it should not be silently equated with source verification or final-key parity.

## Validation and next actions
1. Retrieve the full Sanskrit review queue from PR #22 through a reliable raw/blob path; compare IDs against all 192 active IDs and the 850 staging source IDs.
2. Reconcile Sanskrit totals across `questions.json`, `questions_review_pending.json`, `source_audit.json`, `papers.json`, and `subjects.json`.
3. Confirm the exact 550 recovered question IDs; retain all as review-only until Devanagari visual proofreading, official final-key reconciliation, and explicit syllabus mapping are evidenced.
4. Reconcile Environmental Sciences' 95/205 registry split against the 300 per-record flags and the 291 second-proofreading count.
5. Run the repository's existing validation and CI after any justified data correction. A prior integration audit and Debug APK passed on 2026-11-14, but those runs do not validate PR #22's unmerged content.

## Status
- Audit report committed on the Team 3 war-room branch only.
- No canonical subject data modified.
- No merge performed.
- No new APK PASS claimed.
