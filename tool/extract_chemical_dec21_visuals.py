#!/usr/bin/env python3
"""Render official December 2021 Chemical Sciences visual-question assets."""
from pathlib import Path
import subprocess
import fitz

URL = "https://gujaratset.ac.in/assets/papers/paperII/dec21/dec2103.pdf"
OUT = Path("assets/images")
PDF = Path("build/chemical_dec21/dec2103.pdf")
OUT.mkdir(parents=True, exist_ok=True)
PDF.parent.mkdir(parents=True, exist_ok=True)

# (question, 1-based PDF page, x0, y0, x1, y1) in PDF points.
BOXES = {
    18:(10,6.7,266.7,540,466.7), 43:(15,20,166.7,536.7,346.7),
    53:(17,13.3,200,540,556.7), 64:(19,16.7,460,536.7,710),
    71:(21,13.3,23.3,543.3,466.7), 72:(21,13.3,450,543.3,706.7),
    73:(22,13.3,23.3,546.7,213.3), 75:(22,13.3,300,546.7,473.3),
    76:(22,13.3,460,546.7,703.3), 77:(23,13.3,23.3,550,336.7),
    78:(23,13.3,326.7,550,696.7), 79:(24,13.3,23.3,550,333.3),
    80:(24,13.3,313.3,550,486.7), 81:(24,13.3,466.7,550,700),
    82:(25,13.3,23.3,550,333.3), 83:(25,13.3,326.7,550,536.7),
    84:(25,13.3,523.3,550,706.7), 85:(26,13.3,23.3,550,280),
    86:(26,13.3,263.3,550,503.3), 87:(26,13.3,490,550,710),
    88:(27,13.3,23.3,540,260), 89:(27,13.3,240,540,720),
    90:(28,13.3,23.3,543.3,280), 91:(28,13.3,270,543.3,493.3),
    93:(29,13.3,23.3,546.7,366.7),
}

def run(cmd):
    subprocess.run(cmd, check=True)

run(["curl","-L","--fail","--retry","3","--connect-timeout","20",
     "--insecure","-o",str(PDF),URL])

doc = fitz.open(PDF)
assert len(doc) == 32, f"Unexpected page count: {len(doc)}"

for q,(page_no,x0,y0,x1,y1) in BOXES.items():
    page = doc[page_no-1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0,2.0),
                           clip=fitz.Rect(x0,y0,x1,y1), alpha=False)
    out = OUT / f"chemical_dec21_q{q}.jpg"
    pix.save(out, jpg_quality=80)
    assert out.stat().st_size > 1000, f"Invalid image for Q{q}"

expected={f"chemical_dec21_q{q}.jpg" for q in BOXES}
actual={p.name for p in OUT.glob("chemical_dec21_q*.jpg")}
assert actual == expected, f"Unexpected visual assets: {sorted(actual ^ expected)}"
print(f"December 2021 Chemical Sciences visual assets: {len(expected)}")
print("Questions:", sorted(BOXES))
