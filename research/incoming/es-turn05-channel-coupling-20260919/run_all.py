#!/usr/bin/env python3
"""Reproduce the five scoped Turn 5 checks and record their exact source hashes."""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, time
from pathlib import Path

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',default='reproduced')
    ap.add_argument('--pair-bound',type=int,default=1000)
    ap.add_argument('--window-bound',type=int,default=2000)
    ap.add_argument('--optimized',action='store_true')
    ar=ap.parse_args(); root=Path(__file__).resolve().parent; out=Path(ar.out).resolve()
    out.mkdir(parents=True,exist_ok=True)
    if ar.pair_bound<97 or ar.window_bound<5:ap.error('pair bound >=97 and window bound >=5 required')
    python=[sys.executable]+(['-O'] if ar.optimized else [])
    commands=[['verify.py','--bound',str(ar.pair_bound),'--out',str(out)],
              ['verify_windows.py','--bound',str(ar.window_bound),'--out',str(out)],
              ['check_independent.py','--input',str(out),'--out',str(out/'independent.json')],
              ['check_windows.py','--input',str(out),'--out',str(out/'windows_independent.json')],
              ['verify_local.py']]
    runs=[]
    for command in commands:
        started=time.monotonic()
        result=subprocess.run(python+command,cwd=root,text=True,capture_output=True)
        row={'argv':python+command,'source_sha256':sha(root/command[0]),'returncode':result.returncode,
             'seconds':round(time.monotonic()-started,6),'stdout':result.stdout,'stderr':result.stderr}
        runs.append(row)
        if result.returncode:
            (out/'run_receipt.json').write_text(json.dumps({'success':False,'runs':runs},indent=2)+'\n')
            print(result.stderr or result.stdout,file=sys.stderr);raise SystemExit(result.returncode)
    shutil.copy2(root/'local_certificate.json',out/'local_certificate.json')
    hashes={p.name:sha(p) for p in sorted(out.glob('*.json')) if p.name!='run_receipt.json'}
    receipt={'success':True,'optimized':ar.optimized,'pair_bound':ar.pair_bound,'window_bound':ar.window_bound,
             'runs':runs,'mathematical_files':hashes,
             'scope':'Five scoped program executions, not independent mathematical review, a Lean build, or universal ES occupancy.'}
    (out/'run_receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'success':True,'mathematical_files':len(hashes),'optimized':ar.optimized},sort_keys=True))
if __name__=='__main__':main()
