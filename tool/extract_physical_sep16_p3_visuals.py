#!/usr/bin/env python3
from pathlib import Path
import urllib.request
import fitz
from PIL import Image
import io

URL="https://www.gujaratset.ac.in/assets/papers/paperIII/sept16/sept16p302.pdf"
OUT=Path("assets/images")
OUT.mkdir(parents=True,exist_ok=True)
pdf=Path("/tmp/sept16p302.pdf")
urllib.request.urlretrieve(URL,pdf)
doc=fitz.open(pdf)

# Crops retain the original source visual from the official scanned PDF.
crops={
  6:(250,350,2050,1550,"physical_sep16_p3_q6.png"),
  12:(70,520,1350,1600,"physical_sep16_p3_q12.png"),
  22:(180,650,2150,2850,"physical_sep16_p3_q64.png"),
  24:(180,300,2150,2050,"physical_sep16_p3_q69.png"),
}

for page_no,box in crops.items():
    page=doc[page_no-1]
    pix=page.get_pixmap(matrix=fitz.Matrix(300/72,300/72),alpha=False)
    png=pix.tobytes("png")
    im=Image.open(io.BytesIO(png))
    crop=tuple(int(v) for v in box[:4])
    im.crop(crop).save(OUT/box[4],format="PNG")
    print("generated",OUT/box[4])
