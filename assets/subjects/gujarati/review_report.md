# GSET Gujarati (06) Paper-II - verification report

File: gset_gujarati_06_paper2_question_bank_staging.json (STAGING; not integrated into the repository). Same layout as the other staging files (a few passage-group records carry an extra "passage" field).

## Sessions (400 questions)
| Session | Q | Paper file | Paper code | Key |
|---|---|---|---|---|
| Dec 2002 (1 Dec) | 50 | dec0206.pdf | D-0602 | scanned "KEY FOR PAPER-II" (not labelled final) |
| Dec 2003 (7 Dec) | 50 | dec0306.pdf | D/03/6 | scanned, same |
| Dec 2008 (7 Dec) | 50 | dec0806.pdf | Dec-08/06 | scanned, same |
| Aug 2017 (27 Aug) | 50 | aug1706.pdf | AUG-17/06 | official final |
| Dec 2019 (29 Dec, 14th GSET) | 100 | dec1906.pdf | DEC-19/06 | official final (Q7 = Z) |
| Dec 2021 / Jan 2022 (15th GSET) | 100 | dec2106.pdf | DEC-21/06 | NONE SUPPLIED |

## Counts
| Status | Count |
|---|---|
| key_applied_pending_proofread | 276 |
| review_required | 24 |
| incomplete_answer_key_missing (Dec 2021, all 100) | 100 |
| verified against repository schema | 0 |

## Dec 2021: no answer key
No answer key for Dec 2021 was among the uploaded files. I tried to reach the official GSET website; this session blocked the request, and the only search results were third-party sites, which I did not use because you required official keys only. official_answer is null for all 100 questions. 28 of the 100 are also flagged for reading doubts (Q27, 35-40, 43, 47, 51, 60, 70, 72, 77, 78, 81, 83-86, 91, 93, 95-100); the doubts are in review_note (Q35-40/43/47/51/60 etc. are in the notes, not all in the status field, because the missing key overrides the status).

## Review-required (24, sessions with keys)
- Dec 2002: Q27, Q28. Dec 2003: Q18, 19, 43, 44, 47-50. Dec 2008: Q33, 34. Aug 2017: Q47 (conjunct in "પટ્ટણી": ટ્ટ vs ડ્ડ/ટ્ડ).
- Dec 2019: Q7 (key printed Z, not evaluated; official_answer null), Q22, 25, 42, 58, 64, 65, 78, 85, 86, 100 (Q100 option B printed "વિવંચકનું", possible printer's typo).

## Checks run
- JSON parses; 400 unique IDs (GSET-GUJ06-<SESSION>-Qnnn); four non-empty options A-D on every question; every non-null official_answer is one of A-D.
- Text keys (Aug 2017, Dec 2019) parsed programmatically (50 and 100); the three scanned keys were read by eye from full-page images.
- Four existing-key sessions were not re-checked by any OCR (see below).

## Important limits
- NO independent OCR cross-check: no Gujarati OCR was available. All Gujarati was read from images by a model, which can misread matras and conjuncts. A human proofread of ALL 400 records against the PDFs is essential.
- Second-pass verification: Aug 2017 Q1-45 were re-viewed once; the other sessions had only partial or no second pass because usage limits interrupted the work (Dec 2019 and Dec 2021: first pass only). Dec 2002/2003/2008 second passes are as reported by the transcribers, not independently confirmed.
- During the Dec 2019 work one file got the wrong question range; I moved the records by question number and re-validated that each file holds n=1-50 and n=51-100 once each.
- Printed typos and variant spellings (e.g. કઇ/કઈ) were kept as printed.
- Old keys (2002/2003/2008) are not titled "final".
- Whether a key letter is academically right was not assessed.
- syllabus_unit null everywhere; question_booklet_serial null (booklets print paper codes only; Dec 2021 serial could not be read reliably).
- Repo schema/validators were not accessible, so compatibility, path placement and build checks are NOT done. Do not treat this as integrated.
