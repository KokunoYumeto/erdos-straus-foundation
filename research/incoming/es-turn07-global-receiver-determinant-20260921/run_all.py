#!/usr/bin/env python3
"""Reproduce exact proofs and bounded checks; failed commands stop the release.
Run from any directory. No external Python packages are needed.
PDF rendering is a separate optional release step, not a mathematical premise.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys, time
from pathlib import Path


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--directory',type=Path,default=Path('certificates'))
    args=ap.parse_args()
    root=Path(__file__).resolve().parent
    out=args.directory if args.directory.is_absolute() else root/args.directory
    opt=out.with_name(out.name+'_optimized')
    logs=root/'execution_logs';logs.mkdir(exist_ok=True)
    commands=[
      [sys.executable,str(root/'verify.py'),'--bound',str(args.bound),'--out',str(out)],
      [sys.executable,'-O',str(root/'verify.py'),'--bound',str(args.bound),'--out',str(opt)],
      [sys.executable,str(root/'check_independent.py'),'--input',str(out),'--out',str(out/'independent.json')],
      [sys.executable,'-O',str(root/'check_independent.py'),'--input',str(opt),'--out',str(opt/'independent.json')],
    ]
    records=[]
    for i,cmd in enumerate(commands):
        start=time.monotonic()
        p=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
        (logs/f'command_{i}.log').write_text(p.stdout+p.stderr,encoding='utf-8')
        records.append({'arguments':cmd,'returncode':p.returncode,
                        'elapsed_seconds':round(time.monotonic()-start,6),
                        'log':f'execution_logs/command_{i}.log'})
        if p.returncode:
            (root/'verification.json').write_text(json.dumps({'success':False,'commands':records},indent=2)+'\n')
            raise SystemExit(p.returncode)
    files=['polynomial_certificates.json','states.json','scan.json','examples.json',
           'negative_controls.json','summary.json']
    comparison={name:(out/name).read_bytes()==(opt/name).read_bytes() for name in files}
    comparison['independent.json']=(out/'independent.json').read_bytes()==(opt/'independent.json').read_bytes()
    if not all(comparison.values()):raise RuntimeError('Normal and optimized mathematical outputs differ.')
    receipt={'success':True,'commands':records,'normal_optimized_identical':comparison,
       'source_hashes':{name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                        for name in ['verify.py','check_independent.py','run_all.py']},
       'main':json.loads((out/'summary.json').read_text()),
       'independent':json.loads((out/'independent.json').read_text()),
       'universal_ES_proved':False,'independent_mathematical_review':False,'lean_build':False}
    (root/'verification.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'success':True,'main_checks':receipt['main']['checks'],
       'independent_checks':receipt['independent']['checks'],
       'normal_optimized_identical':all(comparison.values()),
       'elapsed_seconds':[r['elapsed_seconds'] for r in records]},indent=2))

if __name__=='__main__':main()
