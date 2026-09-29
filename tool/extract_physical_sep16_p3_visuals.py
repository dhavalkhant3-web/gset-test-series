#!/usr/bin/env python3
from pathlib import Path
import urllib.request
import fitz

URL="https://www.gujaratset.ac.in/assets/papers/paperIII/sept16/sept16p302.pdf"
OUT=Path("assets/images")
OUT.mkdir(parents=True,exist_ok=True)
pdf=Path("/tmp/sept16p302.pdf")
urllib.request.urlretrieve(URL,pdf)
doc=fitz.open(pdf)
# Official scanned pages: printed page 6 is PDF page 6, page 22 is PDF page 22, page 24 is PDF page 24.
# Crops retain the original source visual; no OCR/redrawing is used.
crops={
  6:(250,350,2050,1550,"physical_sep16_p3_q6.png"),
  22:(180,650,2150,2850,"physical_sep16_p3_q64.png"),
  24:(180,300,2150,2050,"physical_sep16_p3_q69.png"),
}
for page_no,box in crops.items():
    page=doc[page_no-1]
    pix=page.get_pixmap(matrix=fitz.Matrix(300/72,300/72),alpha=False)
    img=fitz.Pixmap(fitz.csRGB,pix)
    # crop coordinates are based on 300dpi rendering dimensions (72pt -> 300dpi scale ~4.1667);
    # use the same fixed source-region proportions by converting from rendered pixels.
    scale=300/72
    # Instead of reusing OCR, render and crop with PIL for exact pixel output.
    from PIL import Image
    import io
    png=pix.tobytes("png")
    im=Image.open(io.BytesIO(png))
    sx=300/72
    crop=tuple(int(v*sx) for v in box)
    im.crop(crop).save(OUT/box[4],format="PNG")
    print("generated",OUT/box[4])
