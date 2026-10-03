#!/usr/bin/env python3
"""Render source pages from the official GSET Nov 2022 Chemical Sciences Paper-II."""
from pathlib import Path
import urllib.request
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/nov22/nov2203.pdf"
OUT = Path("assets/images")
PAGES = list(range(20, 31))

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = Path("/tmp/nov2203.pdf")
    urllib.request.urlretrieve(URL, pdf)
    doc = fitz.open(pdf)
    assert len(doc) == 32, f"Unexpected page count: {len(doc)}"
    for page_no in PAGES:
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        pix.save(OUT / f"chemical_nov22_page{page_no}.png")
    print(f"Generated {len(PAGES)} Nov 2022 source-page images.")

if __name__ == "__main__":
    main()
