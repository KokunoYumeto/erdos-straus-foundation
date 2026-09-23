#!/usr/bin/env python3
"""Replay the complete declared arithmetic and coefficient domains.
Standard library only. Failing tests raise also under optimized Python.
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, time


def run(command: list[str], cwd: Path, log: Path) -> dict:
    started=time.monotonic()
    result=subprocess.run(command,cwd=cwd,text=True,capture_output=True)
    log.parent.mkdir(parents=True,exist_ok=True)
    log.write_bytes((result.stdout+result.stderr).encode('utf-8'))
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}); see {log}: {command}')
    return dict(command=command,returncode=result.returncode,
                elapsed_seconds=round(time.monotonic()-started,3))


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--bound',type=int,default=10000)
    ap.add_argument('--directory',default='certificates')
    args=ap.parse_args()
    root=Path(__file__).resolve().parent
    out=Path(args.directory)
    if not out.is_absolute():out=root/out
    opt=out.with_name(out.name+'_optimized')
    runs=[]
    runs.append(run([sys.executable,'verify.py','--bound',str(args.bound),'--out',str(out)],root,out/'main.log'))
    runs.append(run([sys.executable,'-O','verify.py','--bound',str(args.bound),'--out',str(opt)],root,out/'optimized.log'))
    runs.append(run([sys.executable,'check_independent.py','--input',str(out),'--out',str(out/'independent.json')],root,out/'independent.log'))
    summary=json.loads((out/'summary.json').read_bytes())
    independent=json.loads((out/'independent.json').read_bytes())
    names=sorted(summary['tables'])
    comparisons={name:(out/name).read_bytes()==(opt/name).read_bytes() for name in names}
    comparisons['summary.json']=(out/'summary.json').read_bytes()==(opt/'summary.json').read_bytes()
    if not all(comparisons.values()):raise RuntimeError('Normal and optimized bytes differ')
    if independent['tables']!=summary['tables']:raise RuntimeError('Independent table digest mismatch')
    receipt=dict(success=True,runs=runs,main=summary,independent=independent,
                 normal_optimized_identical=comparisons,
                 source_sha256={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                    for name in ['arithmetic.py','verify.py','check_independent.py','run_all.py']},
                 universal_ES_proved=False,turn7_universal_existence_complete=False,
                 evidence_scope='Two implementations of finite exact checks; not independent human review or Lean.')
    dest=out/'execution.json'
    dest.write_bytes((json.dumps(receipt,indent=2,sort_keys=True)+'\n').encode('utf-8'))
    print(json.dumps(dict(success=True,receipt=str(dest),main_checks=summary['checks'],
                    independent_checks=independent['checks'],counts=summary['source_counts']),indent=2))

if __name__=='__main__':main()
