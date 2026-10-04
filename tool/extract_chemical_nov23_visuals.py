#!/usr/bin/env python3
"""Render source-preserving crops from the official GSET Nov-2023 Chemical Sciences PDF."""
from pathlib import Path
import re, subprocess, fitz

URL="https://www.gujaratset.ac.in/assets/papers/paperII/nov23/nov2303.pdf"
PDF=Path("build/chemical_nov23/nov2303.pdf")
OUT=Path("assets/images")
SOURCE_PAGES={13:9,16:10,31:13,58:18,59:18,64:19,69:20,72:21,76:22,77:22,82:23,84:24,85:24,91:27,93:27,96:28,97:29,98:29,99:30}
OUT.mkdir(parents=True,exist_ok=True); PDF.parent.mkdir(parents=True,exist_ok=True)
subprocess.run(["curl","-L","--fail","--retry","5","--retry-delay","5","--connect-timeout","30","--max-time","300","--insecure","-o",str(PDF),URL],check=True)

def qy(page,n):
    p=re.compile(rf"^\s*{n}\s*[\.\)]\s*")
    ys=[]
    for x0,y0,x1,y1,t,*_ in page.get_text("blocks"):
        if p.search(t.replace("\n"," ").strip()): ys.append(y0)
    return min(ys) if ys else 0

def next_y(page,n):
    for k in range(n+1,101):
        y=qy(page,k)
        if y>0:return y
    return page.rect.height

doc=fitz.open(PDF)
for n,page_no in SOURCE_PAGES.items():
    page=doc[page_no-1]; top=qy(page,n); bottom=next_y(page,n)
    if top<=0: top,bottom=0,page.rect.height
    clip=fitz.Rect(6,max(0,top-8),page.rect.width-6,min(page.rect.height,bottom+8))
    out=OUT/f"chemical_nov23_q{n}.png"
    page.get_pixmap(matrix=fitz.Matrix(2.4,2.4),clip=clip,alpha=False).save(out)
    assert out.stat().st_size>1000
print("Created 19 official Nov-2023 Chemical visual crops.")
