# Confirmed MCQ Recovery Sources — 2026-10-25

## Critical correction
The earlier empty responses returned by the repository file reader for current `main` do not represent verified empty JSON content. Direct GitHub contents/blob access has confirmed recoverable historical source blobs.

## Physical Sciences (02)
- Target count confirmed from the user's prior working baseline: 1,446 expected/previously reported.
- Historical blob at commit `b851dfe4378b97948293cbfefd01835e7d5f6a55` contains a valid JSON array with **1,300 records**, 1,300 unique IDs, across 19 paper sessions. The last record ID is `physical_sep18_q99`.
- Blob SHA: `8acf3d4e6fe6a46f94892fff4b6bf26659f5c622` (as exposed by GitHub contents endpoint at that ref).
- This is a valid 1,300-record recovery source, but it is 146 records below the user's stated 1,446 baseline; it is not enough alone to assert full recovery.
- Another older source at `891ec10eeb8f12d555e4f792d2243d8b665886ac` returns only 777 identifiable records and malformed JSON (missing comma around Q18), so do not use that source as a whole-bank replacement.
- Current main content read failed with empty response. Do not overwrite it until current blob/tree content is inspected directly.
- A subsequent source file at `ad83aaab60c04885a7821ca55a2e8a6e524643c4` includes OCR damage in Physical Sciences Q18, where mathematical superscripts/options were split into extra array elements. Avoid blind replacement from this source too.

## Chemical Sciences (03)
- Valid historical bank at `891ec10eeb8f12d555e4f792d2243d8b665886ac` / `complete-chemical-sciences-03` parses as **1,250 records**, with 1,250 unique IDs across 18 sessions, ending at `chemical_oct14_q50`.
- Its blob SHA is `83e31bb2a936ef2cb02c1f4cc1d16b07c1afd9f0`.
- Separate `questions_sep16_p2.json` on main contains 50 additional records. Do not blindly append until IDs/session scope are checked against the main bank, loader, and subject metadata.
- The old integration branch is not ahead of current main; it is behind 4 commits. Do not reset main to integration.

## Confirmed next action
Recover actual Git blob contents and compare current main to historical blobs. Use narrow file-scoped updates only on this recovery branch. Preserve source flags and existing answer keys. Do not fabricate questions to satisfy target counts. Do not merge before count, duplicate-ID, option-schema, official-key, and Flutter checks.
