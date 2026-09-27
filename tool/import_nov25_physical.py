import json, re, subprocess, urllib.request
from pathlib import Path

URL='https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2502.pdf'
ANS='''D D A A B C B C D B
C D C D D A C D A C
A B C D A A B B D B
B C C B A C A B A B
B D C A D A B C A B
B D C A B B A B D A
B D D B B A C A D B
B B C B D A B C A B
D B A B A B C B D B
C B D A A C B C B B'''.split()
assert len(ANS)==100

def clean(s):
    s=re.sub(r'\|+',' ',s)
    s=re.sub(r'\s+',' ',s).strip()
    return s

def main():
    work=Path('build/nov25')
    work.mkdir(parents=True,exist_ok=True)
    pdf=work/'nov2502.pdf'
    urllib.request.urlretrieve(URL,pdf)
    subprocess.run(['pdftoppm','-f','7','-l','22','-png','-r','220',str(pdf),str(work/'p')],check=True)
    texts=[]
    for p in sorted(work.glob('p-*.png')):
        out=p.with_suffix('.txt')
        subprocess.run(['tesseract',str(p),str(out.with_suffix('')),'--psm','6'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        texts.append(out.read_text(errors='ignore'))
    alltxt='\n'.join(texts)
    matches=list(re.finditer(r'(?m)^\s*\|?\s*(\d{1,3})\.\s*',alltxt))
    blocks={}
    for i,m in enumerate(matches):
        q=int(m.group(1))
        e=matches[i+1].start() if i+1<len(matches) else len(alltxt)
        blocks[q]=alltxt[m.end():e]
    manual={
      1:("Let A=[[2,1],[0,2]], then A^5 is",["32I","2^5 A","16A−80I","80A−128I"]),
      2:("Let M=[[4,1,−1],[2,1,1],[0,0,3]] and v=[1,2,0]^T, then",["v is the eigenvector of M with eigenvalue 2","v is the eigenvector of M with eigenvalue 3","v is the eigenvector of M with eigenvalue 5","v is not an eigenvector of M"]),
      3:("The determinant of a metric tensor corresponds to ds²=4(dx¹)²+3(dx²)²+6dx¹dx²−4dx²dx³+2dx¹dx³",["−31","6","0","19"]),
      4:("For f(x)=4x(1−x), −1≤x≤0, and f(x)=4x(1+x), 0≤x≤1, the Fourier coefficient b_n is",["32/(π²n³) for odd n and 0 for even n","32/(π³n³) for even n and 0 for odd n","32/(π²n²) for odd n and 0 for even n","32/(π²n²) for even n and 0 for odd n"]),
      5:("For f(z)=(z+1)/(z³−1), the residue at z=1 is",["0","2/3","3/2","2"]),
      6:("The Laplace transform of t e^(−2t) cos(3t) is",["(s+2)/((s+2)²+9)","2(s+2)/((s+2)²+9)","((s+2)−9)/((s+2)²+9)","((s+2)+9)/((s+2)²+9)"]),
      7:("The coefficient of x^8 in the Taylor series of cos(x²) about x=2π is",["1/8","1/24","−1/8","−1/24"])
    }
    records=[]
    for q in range(1,101):
        if q in manual:
            qt,opts=manual[q]; review=True
        else:
            b=blocks.get(q,'')
            om=list(re.finditer(r'\(([A-D])\)\s*',b))
            opts=[]
            for j,o in enumerate(om):
                e=om[j+1].start() if j+1<len(om) else len(b)
                opts.append(clean(b[o.end():e]))
            opts=(opts+['','','',''])[:4]
            first=om[0].start() if om else len(b)
            qt=clean(b[:first])
            review=(len(om)!=4 or '?' in qt or any('?' in x for x in opts))
        topic=('Mathematical Physics' if q<=12 else
               'Classical Mechanics & Relativity' if q<=20 else
               'Electromagnetism & Relativity' if q<=34 else
               'Quantum Mechanics' if q<=48 else
               'Thermodynamics & Statistical Physics' if q<=59 else
               'Experimental Methods & Electronics' if q<=68 else
               'Atomic & Molecular Physics' if q<=75 else
               'Laser Physics' if q<=78 else
               'Nuclear Physics' if q<=87 else
               'Condensed Matter & Nuclear/Particle Physics')
        records.append({
          'id':f'physical_nov25_q{q:02d}',
          'paper_id':'physical_nov25',
          'exam':'November 2025',
          'question_en':qt,
          'options_en':opts,
          'answer':ANS[q-1],
          'topic':topic,
          'difficulty':'Medium',
          'explanation_en':f'Official final answer key: {ANS[q-1]}. Verify the printed mathematical notation when using this item.',
          'explanation_gu':f'Official final answer key મુજબ જવાબ {ANS[q-1]} છે. Mathematical notation માટે original paper જુઓ.',
          'review_flag':review,
          'review_note':'OCR/notation requires manual review.' if review else '',
          'source_verified':True,
          'source':'GSET official November 2025 Physical Sciences question paper and final answer key'
        })
    Path('assets/subjects/physical_sciences/nov25_questions.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':
    main()
