# GSET Test Series — MCQ Recovery Audit Baseline
Date: 2026-10-25

## Safety status
- This branch is a recovery/audit branch created from the current `main` commit.
- No subject question-bank file or app source file has been changed by this commit.
- Do not merge this branch until the bank recovery plan and validators have been reviewed.

## Repository state observed
- Default branch: `main`
- `main` HEAD: `6bbf0d6aca621edef849ded92fe8109b4c6f88da` — “Restore Mathematical Sciences questions into app assets”
- PR #16 (integration/combined-subject-banks) is merged. Its head branch remains available at `fd272394dbbd24b506f1de023872ed24f0035ec4`; it is behind current `main` by 4 commits. Do not copy the old integration tree over `main`.
- `assets/subjects/subjects.json` is identical on `main` and the old integration branch.

## Content observations
GitHub's file-content connector returned zero-byte content for these files on both `main` and the relevant audit/completion branches. Treat this as a confirmed retrieval/inspection limitation, **not by itself proof** that the Git blobs contain empty files:
- `assets/subjects/physical_sciences/questions.json`
- `assets/subjects/chemical_sciences/questions.json`
- `assets/subjects/mathematical_sciences/questions.json`

The main branch commit's own diff confirms a recent “Restore Mathematical Sciences questions into app assets” change in the Mathematical Sciences bank (large-file patch ending at approximately 34k lines). Do not overwrite that restored file.

Independent branches provide parseable 300-record banks for:
- Performing Arts: `add-performing-arts-31` (300 questions)
- Indian Knowledge System: `add-indian-knowledge-system-29` (300 questions)
- Public Administration: `integrate/public-administration-subject` (300 questions)
- Visual Art: `complete-visual-arts-33` (300 questions)

Current `main` and older integration branch both have parseable 300-record copies for Performing Arts and IKS. Current `main` also has 300-record Public Administration and Visual Art files, and those file blobs differ from the integration branch versions. Prefer `main` as the baseline unless a verified comparison proves a bank is missing or degraded; do not blindly replace one with the other.

Chemical Sciences supplementary file `assets/subjects/chemical_sciences/questions_sep16_p2.json` is parseable and contains 50 records, Q1–Q50, with one review flag. The app loader on `main` includes the September 2016 supplement.

Physical Sciences supplement `assets/subjects/physical_sciences/sept18_source_review.json` contains two review records (Q32 and Q86). The loader source currently contains no obvious reference to this overlay in its inspected text, so verify loader paths and assets before claiming that overlay is active.

## Required next steps
1. Obtain actual Git blob bytes for the three large question JSON files through a Git-data/raw-file path that supports large blobs; do not infer emptiness from a connector response that returned no content.
2. Compute record counts and IDs for every subject bank from the actual blob data.
3. Compare `main` against independent branches per file and select the highest-quality source by provenance, schema, count, and validator results — not just file size.
4. Preserve `main`'s 4 newer commits. Apply only narrow, file-scoped recovery commits on this branch.
5. Run JSON parse, duplicate-ID, expected question-number, subject loader/metadata, official answer-key, and Flutter validation checks.
6. Do not mark source verification complete unless question wording/options are checked against official GSET scans. Keep all legitimate review flags.
7. Open a draft PR with an audit summary; do not merge automatically.
