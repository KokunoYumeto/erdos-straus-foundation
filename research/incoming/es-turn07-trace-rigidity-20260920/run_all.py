#!/usr/bin/env python3
"""Run the complete fixed default replay and record actual outcomes."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, time

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--directory',type=Path,default=Path('reproduced'))
    args=ap.parse_args();root=Path(__file__).resolve().parent
    base=args.directory.resolve();normal=base/'normal';optimized=base/'optimized'
    base.mkdir(parents=True,exist_ok=True)
    commands=[
      [sys.executable,str(root/'verify.py'),'--out',str(normal)],
      [sys.executable,'-O',str(root/'verify.py'),'--out',str(optimized)],
      [sys.executable,str(root/'check_independent.py'),'--input',str(normal),'--out',str(base/'independent.json')]
    ]
    receipt={'commands':[],'universal_ES_proved':False};start=time.monotonic()
    for i,cmd in enumerate(commands):
        t=time.monotonic();res=subprocess.run(cmd,cwd=root,text=True,capture_output=True,timeout=120)
        (base/f'command_{i}.log').write_text(res.stdout+res.stderr)
        receipt['commands'].append({'command':cmd,'returncode':res.returncode,'seconds':time.monotonic()-t})
        if res.returncode:
            (base/'execution.json').write_text(json.dumps(receipt,indent=2)+'\n')
            raise RuntimeError(f'Command {i} failed; inspect its log.')
    names=['scan.json','raw_trace.json','denominators.json','trace_relaxation.json',
           'algebraic_targets.json','examples.json','negative_controls.json']
    receipt['normal_optimized']={name:(normal/name).read_bytes()==(optimized/name).read_bytes() for name in names}
    if not all(receipt['normal_optimized'].values()):raise RuntimeError('Mathematical output mismatch')
    receipt['main']=json.loads((normal/'summary.json').read_text())
    receipt['independent']=json.loads((base/'independent.json').read_text())
    receipt['elapsed_seconds']=time.monotonic()-start;receipt['success']=True
    (base/'execution.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'success':True,'main_checks':receipt['main']['checks'],
                      'independent_checks':receipt['independent']['checks']},indent=2))
if __name__=='__main__':main()
