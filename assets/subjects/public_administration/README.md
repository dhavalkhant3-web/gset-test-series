# Public Administration Paper-II integration

Subject code: 32. The subject registry records 3 staged sessions and 300 loaded records. The bank is **not source-verified as a whole** yet: the supplied staging dataset has 3 records marked for review, and the question text/options/official final answers still require a source-by-source audit against the linked official PDFs.

## Data files

- `questions.json`: 300 questions, 100 each for November 2023, December 2024, and November 2025.
- `papers.json`: per-session paper metadata and official GSET archive URLs.
- `tools/import_public_administration.py`: strict converter from the supplied staging schema to the app's existing question schema.

## Rebuild the question bank

```bash
python tools/import_public_administration.py gset_paper2_public_administration_staging.json
```

The importer checks the 300-record total, 100 questions per session, unique session/question-number pairs, and exactly four A-D options. It carries through the official answer and provenance and flags records whose staging status is not verified or whose answer does not map to A-D.

## Validation status

The app's generic Paper-II loader expects `assets/subjects/<subject_id>/questions.json`, so this bank follows the existing path convention. This branch does not claim the Flutter build or CI has passed. Keep `source_verified: false` and `answer_key_verified: false` until every question, option, and answer has been checked against the official question booklet and final answer key. Do not merge as fully verified before that audit and CI/build checks.
