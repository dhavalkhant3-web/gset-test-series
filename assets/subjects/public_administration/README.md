# Public Administration Paper-II integration

Subject code: 32. The subject already exists in `assets/subjects/subjects.json`; its counts remain at zero until the staging bank is imported and validated.

## Import

Place the supplied `gset_paper2_public_administration_staging.json` file somewhere accessible, then run:

```bash
python tools/import_public_administration.py gset_paper2_public_administration_staging.json
```

The importer writes `assets/subjects/public_administration/questions.json` in the app's existing question schema. It checks that there are exactly 300 records, 100 per session across November 2025, December 2024, and November 2023, unique session/question-number pairs, and four options per question. It carries through the official answer and provenance, preserves original English text, and flags non-verified records or answers that do not map to A-D.

## Important validation status

The importer does not claim that the source PDFs were independently re-audited. The three staging records marked `review_required` remain flagged. It intentionally does not mark the subject's registry entry as loaded or source-verified. Those metadata must be updated only after the generated JSON has been committed and checked against the official booklets and final answer keys.

## Current app behavior

The app loads the base bank at `assets/subjects/<subject_id>/questions.json`. Therefore, the generated file's path follows the existing subject loader convention. Paper-specific session metadata and subject registry counts should be updated in the same integration once the bank is available in the repository.
