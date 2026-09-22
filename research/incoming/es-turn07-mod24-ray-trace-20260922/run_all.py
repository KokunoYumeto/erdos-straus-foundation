#!/usr/bin/env python3
"""Replay the main, optimized and separate arithmetic implementations."""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys, time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bound',type=int,default=10000)
    ap.add_argument('--directory',type=Path,default=Path('reproduced'))
    ar=ap.parse_args();root=Path(__file__).resolve().parent
    out=ar.directory.resolve();opt=Path(str(out)+'_optimized');out.mkdir(parents=True,exist_ok=True)
    commands=[[sys.executable,str(root/'verify.py'),'--bound',str(ar.bound),'--out',str(out)],
      [sys.executable,'-O',str(root/'verify.py'),'--bound',str(ar.bound),'--out',str(opt)],
      [sys.executable,str(root/'check_independent.py'),'--input',str(out),'--out',str(out/'independent.json')],
      [sys.executable,str(root/'repair.py'),'--p','1129','--a','417','--y','6116/7','--z','20714892/7','--out',str(out/'repair_example.json')],
      [sys.executable,'-O',str(root/'repair.py'),'--p','1129','--a','417','--y','6116/7','--z','20714892/7','--out',str(opt/'repair_example.json')],
      [sys.executable,str(root/'check_interface.py'),'--input',str(out),'--out',str(out/'interface.json')]]
    records=[]
    for i,cmd in enumerate(commands):
        start=time.monotonic();res=subprocess.run(cmd,text=True,capture_output=True,cwd=root)
        (out/f'command_{i}.log').write_text(res.stdout+res.stderr)
        records.append(dict(command=cmd,returncode=res.returncode,elapsed_seconds=round(time.monotonic()-start,3)))
        if res.returncode:raise RuntimeError(f'failed command {i}; see its original log')
    equal={}
    for name in ('scan.json','ray_fibres.json','examples.json','progressions.json','repair_example.json'):
        equal[name]=(out/name).read_bytes()==(opt/name).read_bytes()
    a=json.loads((out/'summary.json').read_text());b=json.loads((opt/'summary.json').read_text())
    a.pop('elapsed_seconds',None);b.pop('elapsed_seconds',None);equal['summary_except_elapsed']=a==b
    if not all(equal.values()):raise ArithmeticError('normal/optimized mismatch')
    receipt=dict(success=True,commands=records,normal_optimized_comparison=equal,
                 main=json.loads((out/'summary.json').read_text()),
                 independent=json.loads((out/'independent.json').read_text()),
                 interface=json.loads((out/'interface.json').read_text()),
                 universal_ES_proved=False,universal_existence_milestone_completed=False)
    (out/'REPLAY.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
