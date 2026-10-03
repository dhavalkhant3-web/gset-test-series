#!/usr/bin/env python3
"""Generate source-page images for GSET Chemical Sciences Nov 2025 Paper-II.

The question paper is downloaded only from the official GSET URL. Rendered
source pages are used for structure/figure/equation-based questions so the app
does not need invented redraws.
"""
from pathlib import Path
import urllib.request
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2503.pdf"
OUT = Path("assets/images")
PAGES = [12, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = Path("/tmp/nov2503.pdf")
    urllib.request.urlretrieve(URL, pdf)
    doc = fitz.open(pdf)
    assert len(doc) == 32, f"Unexpected page count: {len(doc)}"
    for page_no in PAGES:
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        pix.save(OUT / f"chemical_nov25_page{page_no}.png")
    print(f"Generated {len(PAGES)} source-page images.")

if __name__ == "__main__":
    main()
