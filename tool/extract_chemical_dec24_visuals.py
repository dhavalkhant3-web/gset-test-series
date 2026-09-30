#!/usr/bin/env python3
from pathlib import Path
import hashlib, urllib.request
import fitz
from PIL import Image

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2403.pdf"
EXPECTED_SHA256 = "3ec71d0edd24a716fb33f99378b5f5e3deac6a458ea9dff9823d80016c31c537"
PDF = Path("/tmp/chemical_dec24_p2.pdf")
OUT = Path("assets/images")
OUT.mkdir(parents=True, exist_ok=True)

urllib.request.urlretrieve(URL, PDF)
sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
if sha != EXPECTED_SHA256:
    raise SystemExit(f"SHA256 mismatch: {sha} != {EXPECTED_SHA256}")

# Crops are expressed in source-PDF points (converted from the audited 250-DPI
# page crops). They intentionally preserve the original printed visual.
crops = {
17:(90,80,1950,720,10), 20:(90,1080,1950,1650,10), 26:(100,850,1940,1850,11),
61:(90,1750,1950,2450,15), 64:(90,1450,1950,2450,16), 65:(80,80,1950,2250,17),
67:(80,80,1950,2700,18), 68:(80,80,1950,2700,19), 70:(80,850,1950,1750,20),
71:(80,1450,1950,2700,20), 72:(80,80,1950,2700,21), 73:(80,80,1950,2700,22),
74:(80,80,1950,1300,23), 76:(80,1500,1950,2700,23), 80:(80,1800,1950,2700,24),
81:(80,80,1950,1650,25), 83:(80,1700,1950,2550,25), 84:(80,80,1950,850,26),
86:(80,1150,1950,2700,26), 87:(80,80,1950,2700,27), 88:(80,1500,1950,2700,27),
89:(80,80,1950,1350,28), 90:(80,1250,1950,2700,28), 91:(80,80,1950,1200,29),
96:(80,80,1950,900,30)
}
scale = 72.0/250.0
doc = fitz.open(PDF)
for q,(x1,y1,x2,y2,page) in crops.items():
    p = doc[page-1]
    rect = fitz.Rect(x1*scale,y1*scale,x2*scale,y2*scale) & p.rect
    pix = p.get_pixmap(matrix=fitz.Matrix(250/72,250/72), clip=rect, alpha=False)
    pix.save(OUT / f"chemical_dec24_q{q}.png")
print(f"Generated {len(crops)} Chemical Sciences December 2024 visual assets.")
