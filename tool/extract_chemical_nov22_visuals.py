from pathlib import Path
import requests
import fitz
from PIL import Image

OFFICIAL_URL = "https://gujaratset.ac.in/assets/papers/paperII/nov22/nov2203.pdf"
MIRROR_URL = "https://drive.usercontent.google.com/download?id=1nea-Knh79W9utYqENQxiJpyrN9WZ0gXp&export=download&confirm=t"
OUT = Path("assets/images")
OUT.mkdir(parents=True, exist_ok=True)
PDF = Path("/tmp/chemical_nov22.pdf")

# Coordinates are from the official November 2022 Chemical Sciences Paper-II
# uploaded source. Pages are 1-based; y coordinates are at 2x render scale.
CROPS = {
    28:(12,334,617), 32:(13,166,637), 43:(15,161,515), 63:(18,883,1500),
    71:(20,938,1490), 72:(21,158,763), 73:(21,763,1045), 74:(21,1045,1500),
    75:(22,169,705), 76:(22,705,1124), 77:(22,1124,1500),
    79:(23,314,551), 80:(23,551,974), 81:(23,974,1500),
    84:(24,712,1490), 86:(25,429,748), 87:(25,748,1500),
    88:(26,168,789), 91:(27,152,740), 93:(27,1053,1500),
    94:(28,169,763), 95:(28,763,1500),
    96:(29,145,683), 98:(29,976,1500),
    99:(30,158,670), 100:(30,670,1490),
}

def download(url):
    response = requests.get(url, timeout=(20, 120), headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=True)
    response.raise_for_status()
    data = response.content
    if not data.startswith(b"%PDF"):
        raise RuntimeError(f"Downloaded content is not a PDF from {url} (content-type={response.headers.get(chr(39)+chr(99)+chr(111)+chr(110)+chr(116)+chr(101)+chr(110)+chr(116)+chr(45)+chr(116)+chr(121)+chr(112)+chr(101)+chr(39))})")
    PDF.write_bytes(data)

try:
    download(OFFICIAL_URL)
    print("Downloaded official GSET question paper")
except Exception as official_error:
    print(f"Official GSET download unavailable: {official_error}")
    print("Using the public mirror of the same official question-paper PDF as fallback")
    download(MIRROR_URL)

doc = fitz.open(PDF)
assert len(doc) >= 30, f"Unexpected PDF page count: {len(doc)}"

for q, (page, y0, y1) in CROPS.items():
    pix = doc[page - 1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    page_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    x0, x1 = 45, page_image.width - 45
    crop = page_image.crop((x0, max(0, y0 - 18), x1, min(page_image.height, y1 - 12)))
    crop.save(str(OUT / f"chemical_nov22_q{q}.png"), optimize=True)

files = sorted(OUT.glob("chemical_nov22_q*.png"), key=lambda p: int(p.stem.split("q")[-1]))
assert len(files) == 26, f"Expected 26 Nov 2022 visual assets, found {len(files)}"
assert [int(p.stem.split("q")[-1]) for p in files] == sorted(CROPS), "Unexpected question asset set"
print(f"Generated {len(files)} official Nov 2022 Chemical Sciences visual assets")
