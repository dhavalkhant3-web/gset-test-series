#!/usr/bin/env python3
"""Render source-preserving visual crops from the official GSET Dec-2021 Chemical Sciences paper.

No OCR is used to reconstruct scientific content. Each image is a direct crop of the
official PDF page, preserving printed structures, reactions, equations, graphs, tables,
symbols and answer options.
"""
from pathlib import Path
import subprocess
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/dec21/dec2103.pdf"
OUT = Path("assets/images")
PDF = Path("build/chemical_dec21/dec2103.pdf")
OUT.mkdir(parents=True, exist_ok=True)
PDF.parent.mkdir(parents=True, exist_ok=True)

# (question, zero-based PDF page index, top fraction, bottom fraction)
# Fractions are based on an audited 300-DPI render of the same official PDF.
CROPS = {
    18:(9,0.355514,0.635551), 19:(9,0.621688,1.0), 20:(10,0.082512,1.0),
    28:(11,0.695813,1.0), 31:(12,0.361308,1.0), 40:(13,0.581302,1.0),
    43:(14,0.235710,1.0), 47:(15,0.090546,0.414979), 49:(15,0.401166,1.0),
    52:(16,0.075200,0.311541), 53:(16,0.297729,1.0),
    60:(18,0.083385,0.703692), 64:(18,0.689846,1.0),
    71:(20,0.082335,0.641782), 72:(20,0.627957,1.0),
    75:(21,0.441140,0.629368), 76:(21,0.615573,1.0),
    77:(22,0.089543,0.456915), 78:(22,0.443116,1.0),
    79:(23,0.080012,0.419068), 80:(23,0.405273,0.625690), 81:(23,0.611895,1.0),
    82:(24,0.103860,0.432598), 83:(24,0.418811,0.703125), 84:(24,0.689338,1.0),
    85:(25,0.089483,0.382841), 86:(25,0.369004,0.680812), 87:(25,0.666974,1.0),
    88:(26,0.103565,0.358943), 89:(26,0.345114,1.0),
    90:(27,0.092194,0.411801), 91:(27,0.397972,0.659496), 93:(28,0.104199,0.461538),
}

def run(cmd):
    subprocess.run(cmd, check=True)

run(["curl","-L","--fail","--retry","5","--retry-delay","5",
     "--connect-timeout","30","--max-time","300","--insecure","-o",str(PDF),URL])

doc = fitz.open(PDF)
assert len(doc) == 32, f"Unexpected page count: {len(doc)}"

for q,(page_index,top,bottom) in CROPS.items():
    page = doc[page_index]
    r = page.rect
    clip = fitz.Rect(8, r.height*top, r.width-8, r.height*bottom)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.2,2.2), clip=clip, alpha=False)
    out = OUT / f"chemical_dec21_q{q}.png"
    pix.save(out)
    assert out.stat().st_size > 1000, f"Invalid image for Q{q}"

expected={f"chemical_dec21_q{q}.png" for q in CROPS}
actual={p.name for p in OUT.glob("chemical_dec21_q*.png")}
assert actual == expected, f"Unexpected visual assets: {sorted(actual ^ expected)}"
print(f"December 2021 Chemical Sciences visual assets: {len(expected)}")
print("Questions:", sorted(CROPS))
