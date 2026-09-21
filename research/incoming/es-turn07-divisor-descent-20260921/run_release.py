#!/usr/bin/env python3
"""Run the two standard-library verifiers; optionally compile/render the papers."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,subprocess,sys,time

ROOT=Path(__file__).resolve().parent
MATH=('sources.json','scan.json','examples.json','progressions.json','abstract.json','summary.json','independent.json')
def run(cmd,cwd=ROOT):
    start=time.monotonic()
    r=subprocess.run(cmd,cwd=cwd,text=True,encoding='utf-8',capture_output=True,timeout=600)
    report=dict(command=cmd,returncode=r.returncode,elapsed_seconds=time.monotonic()-start,
                stdout=r.stdout,stderr=r.stderr)
    if r.returncode:raise RuntimeError(json.dumps(report,indent=2))
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,default=ROOT/'reproduced');p.add_argument('--pdf',action='store_true');p.add_argument('--render',action='store_true')
    a=p.parse_args();a.directory=a.directory.resolve();a.directory.mkdir(parents=True,exist_ok=True)
    normal=a.directory/'normal';opt=a.directory/'optimized'
    with ThreadPoolExecutor(max_workers=2) as pool:
        records=list(pool.map(run,[
            [sys.executable,'verify.py','--bound','3000','--seed-bound','100','--out',str(normal)],
            [sys.executable,'-O','verify.py','--bound','3000','--seed-bound','100','--out',str(opt)],
        ]))
    with ThreadPoolExecutor(max_workers=2) as pool:
        records.extend(pool.map(run,[
            [sys.executable,'check_independent.py','--input',str(normal),'--out',str(normal/'independent.json')],
            [sys.executable,'-O','check_independent.py','--input',str(opt),'--out',str(opt/'independent.json')],
        ]))
    agreement={n:(normal/n).read_bytes()==(opt/n).read_bytes() for n in MATH}
    if not all(agreement.values()):raise RuntimeError('normal/optimized mathematical outputs differ')
    pdf={}
    if a.pdf or a.render:
        for name in ('workbench','preprint'):
            for _ in range(2):records.append(run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex']))
            text=run(['pdftotext','-layout',name+'.pdf','-'])['stdout']
            info=run(['pdfinfo',name+'.pdf'])['stdout']
            pages=int(next(line.split(':')[1] for line in info.splitlines() if line.startswith('Pages:')))
            pdf[name]=dict(pages=pages,text_sha256=hashlib.sha256(text.encode()).hexdigest())
            if a.render:
                folder=a.directory/'rendered'/name;folder.mkdir(parents=True,exist_ok=True)
                records.append(run(['pdftoppm','-r','110','-png',name+'.pdf',str(folder/'page')]))
                pdf[name]['PNG_sha256']={q.name:hashlib.sha256(q.read_bytes()).hexdigest() for q in sorted(folder.glob('*.png'))}
    report=dict(success=True,main=json.loads((normal/'summary.json').read_text()),
                independent=json.loads((normal/'independent.json').read_text()),normal_optimized_identical=agreement,
                pdf=pdf,commands=records,universal_ES_proved=False,
                independent_machine_review=True,independent_human_review=False,Lean_build=False)
    (a.directory/'REPLAY.json').write_bytes(
        (json.dumps(report,sort_keys=True,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({k:v for k,v in report.items() if k!='commands'},sort_keys=True,indent=2))
if __name__=='__main__':main()
