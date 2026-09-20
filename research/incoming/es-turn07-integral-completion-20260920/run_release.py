#!/usr/bin/env python3
"""Execute the mathematical certificate replays; optional TeX builds.
All mathematical checkers use the Python standard library. PDF compilation is
an optional external LaTeX toolchain step, recorded separately.
"""
from __future__ import annotations
import argparse, hashlib, json, os, platform, shutil, subprocess, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000)
    ap.add_argument('--build-pdfs',action='store_true');args=ap.parse_args()
    record={'date':'2026-09-20','python':platform.python_version(),
            'universal_ES_proved':False,'turn7_universal_milestone_completed':False,
            'commands':[],'source_hashes':{n:digest(ROOT/n) for n in
                ('verify.py','check_independent.py','core.tex','preprint.tex')}}
    start=time.monotonic()
    commands=[
      [sys.executable,'verify.py','--bound',str(args.bound),'--out','certificates'],
      [sys.executable,'-O','verify.py','--bound',str(args.bound),'--out','certificates_optimized'],
      [sys.executable,'check_independent.py','--input','certificates','--out','certificates/independent.json']]
    success=True
    for i,cmd in enumerate(commands):
        t=time.monotonic()
        try:
            p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=45)
            entry={'command':cmd,'returncode':p.returncode,'seconds':time.monotonic()-t}
            (ROOT/f'run_{i}.log').write_text(p.stdout+p.stderr)
            success=success and p.returncode==0
        except subprocess.TimeoutExpired:
            entry={'command':cmd,'status':'timeout','timeout_seconds':45};success=False
        record['commands'].append(entry)
        if not success:break
    comparison={}
    if success:
        for name in ('scan.json','examples.json','orders.json'):
            a=ROOT/'certificates'/name;b=ROOT/'certificates_optimized'/name
            comparison[name]={'identical':a.read_bytes()==b.read_bytes(),'sha256':digest(a)}
        success=all(x['identical'] for x in comparison.values())
        record['main']=json.loads((ROOT/'certificates/summary.json').read_text())
        record['independent']=json.loads((ROOT/'certificates/independent.json').read_text())
        success=success and record['main']['success'] and record['independent']['success']
    record['normal_optimized_comparison']=comparison
    record['mathematical_replay_success']=success
    record['pdf_builds']=[]
    if args.build_pdfs:
        if not shutil.which('pdflatex'):
            record['pdf_builds'].append({'status':'pdflatex unavailable'})
        else:
            for name in ('workbench','preprint'):
                runs=[]
                for pass_no in (1,2):
                    p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],
                                     cwd=ROOT,text=True,capture_output=True,timeout=45)
                    (ROOT/f'{name}_compile_{pass_no}.log').write_text(p.stdout+p.stderr)
                    runs.append(p.returncode)
                    if p.returncode:break
                record['pdf_builds'].append({'document':name,'returncodes':runs,
                    'success':runs==[0,0],
                    'sha256':digest(ROOT/(name+'.pdf')) if runs==[0,0] else None})
    record['elapsed_seconds']=time.monotonic()-start
    (ROOT/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record.get(k) for k in
         ('mathematical_replay_success','normal_optimized_comparison','pdf_builds')},indent=2))
    if not success:raise SystemExit(1)
if __name__=='__main__':main()
