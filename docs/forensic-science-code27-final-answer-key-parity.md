# Forensic Science Code 27 — Official Final Answer-Key Parity Audit

**Audit scope:** Paper-II, GSET November 2023, December 2024, November 2025  
**Question-bank source:** conversation-uploaded `forensic_science_paper2_staging(1).json` (300 records)  
**Branch base:** `integration/combined-subject-banks` at audit branch creation  
**Status:** Answer-letter parity verified; source transcription and syllabus mapping are still pending.

## Results

| Session | Bank records | Final key entries | Mismatches |
|---|---:|---:|---:|
| November 2023 | 100 | 100 | 0 |
| December 2024 | 100 | 100 | 0 |
| November 2025 | 100 | 100 | 0 |
| **Total** | **300** | **300** | **0** |

Method: the official final-answer-key PDF uploads were text-extracted, each key was parsed into question number → choice (A/B/C/D/Z), and the staging record's `official_answer` was compared by session and official question number. All three keys contain question numbers 1–100. This validates answer-letter parity only; it does not validate the wording/options or booklet visual correspondence.

## Official answer-key references

- [November 2023 Forensic Science Paper-II final key](https://gujaratset.ac.in/assets/anskey/paperII/nov23/nov2327.pdf)
- December 2024 Forensic Science Paper-II final key: the user-uploaded final-key PDF was locally parsed; an official direct URL was not independently established in this audit.
- [November 2025 Forensic Science Paper-II final key](https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2527.pdf)

## Source-upload inventory reviewed

| File | Nature / session | Page count | Notes |
|---|---|---:|---|
| `nov2327 (1)(1).pdf` | Question paper, Nov 2023 | 16 | Scan/image PDF; text layer empty |
| `nov2327.pdf` | Final answer key, Nov 2023 | 1 | Text extractable; 100 key entries |
| `dec2427 (1).pdf` | Question paper, Dec 2024 | 16 | Scan/image PDF; text layer empty |
| `dec2427(1).pdf` | Final answer key, Dec 2024 | 1 | Text extractable; 100 key entries |
| `nov2527 (1).pdf` | Duplicate question paper, Nov 2025 | 16 | Larger duplicate upload |
| `nov2527.pdf` | Final answer key, Nov 2025 | 1 | Text extractable; 100 key entries |
| `forensic_science_paper2_staging(1).json` | Staging transcription | — | 300 records; still marked unproofread/unverified |
| `gset_forensic_science_paper2_staging(1).json` | Staging manifest | — | Notes 3 sessions, booklet IDs 270062/270054/270075; key fields null in manifest |

The corresponding question paper PDFs were each uploaded in duplicate form (large scan and smaller file). For this audit, the 16-page scans are treated as question-paper copies and the 1-page PDFs as final-key documents based on their extracted page text. This audit did not mark duplicate question records or file hashes as completed in the repository bank.

## Remaining work — do not imply completion

- Compare all 300 question stems and four options against each original scan page. Visual transcription remains unverified.
- Verify figure/table preservation and exact booklet mapping.
- Obtain and reconcile the official December 2024 final-key URL/source record.
- Official syllabus: no question-level unit mapping has been verified. A surfaced UGC NET Forensic Science syllabus uses Code 82, not GSET subject code 27; check repository syllabus schema and establish applicability before mapping.
- Complete duplicate-ID/question audit and app runtime checks against the latest integration branch.
- Run repository JSON/schema validators, Code 27-specific CI and combined Debug APK build. No PASS is claimed in this audit.
- PR #20 remains draft/unmerged; do not merge without authorization.

**Audit declaration:** This report records the completed 300/300 answer-letter comparison only. It does not certify the subject bank as source-verified or ready for merge.
