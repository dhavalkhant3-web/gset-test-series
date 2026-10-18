#!/usr/bin/env python3
"""Run only the September 2013 and September 2016 official Mathematical Sciences Paper-II imports.

The archive metadata uses filenames sep1301.pdf and sep1601.pdf. The older
importer accidentally requested sept1301.pdf and sept1601.pdf, causing these
sessions to remain pending even though the official PDFs exist.
"""
import sys
import import_mathematical_archive as importer

CORRECT_STEMS = {"sep13": "sep1301", "sep16": "sep1601"}
importer.SESSIONS = [
    (session, exam, CORRECT_STEMS.get(session, stem), expected)
    for session, exam, stem, expected in importer.SESSIONS
]

for session in ("sep13", "sep16"):
    sys.argv = [sys.argv[0], "--paper", f"mathematical_sciences_{session}"]
    importer.main()
