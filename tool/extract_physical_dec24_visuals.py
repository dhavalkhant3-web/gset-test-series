#!/usr/bin/env python3
from pathlib import Path
import urllib.request
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2402.pdf"
OUT = Path("assets/images")
OUT.mkdir(parents=True, exist_ok=True)
pdf = Path("/tmp/dec2402_official.pdf")
urllib.request.urlretrieve(URL, pdf)

doc = fitz.open(pdf)
assert len(doc) == 32, f"Expected 32 pages, got {len(doc)}"

# Page 19 contains Q54-Q58; page 29 contains Q94-Q96.
# Keep generous crops around the original source visuals; do not redraw them.
jobs = {
    54: (18, fitz.Rect(70, 60, 2050, 1050)),
    94: (28, fitz.Rect(70, 50, 2050, 1050)),
}
for q, (page_no, rect) in jobs.items():
    pix = doc[page_no].get_pixmap(matrix=fitz.Matrix(1.8, 1.8), clip=rect, alpha=False)
    pix.save(OUT / f"physical_dec24_q{q}.png")

for q in jobs:
    assert (OUT / f"physical_dec24_q{q}.png").exists()
print("Generated", len(jobs), "official source crops.")
