#!/usr/bin/env python3
"""Run only the September 2013 and September 2016 official Mathematical Sciences Paper-II imports.

Use the filenames linked by the official GSET archive. In
tool/import_mathematical_archive.py these are already configured as
sept1301.pdf and sept1601.pdf under the official sept13/sept16 folders.
Do not rewrite them to sep1301.pdf / sep1601.pdf: those URLs return 404.
"""
import sys
import import_mathematical_archive as importer

# Keep the archive's official filename mapping unchanged. The previous wrapper
# rewrote the stems to non-existent filenames and caused both downloads to fail.
for session in ("sep13", "sep16"):
    sys.argv = [sys.argv[0], "--paper", f"mathematical_sciences_{session}"]
    importer.main()
