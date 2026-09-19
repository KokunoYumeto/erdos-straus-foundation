#!/usr/bin/env python3
"""Run exact checks; retain timeouts and failures without upgrading them to success."""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys, time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bound',type=int,default=3000);ap.add_argument('--timeout',type=int,default=90)
    ar=ap.parse_args();root=Path(__file__).resolve().parent
    commands=[
       [sys.executable,'verify.py','--bound',str(ar.bound),'--out','certificates'],
       [sys.executable,'-O','verify.py','--bound',str(ar.bound),'--out','certificates_optimized'],
       [sys.executable,'check_independent.py','--input','certificates','--out','independent.json']]
    record=dict(bound=ar.bound,commands=[],normal_optimized_agreement={},new_replay_success=False,
                universal_ES_proved=False,turn7_existence_milestone_completed=False)
    for i,cmd in enumerate(commands):
        start=time.monotonic();row={'command':['python',*cmd[1:]]}
        try:
            z=subprocess.run(cmd,cwd=root,text=True,capture_output=True,timeout=ar.timeout)
            row.update(returncode=z.returncode,status='completed',elapsed_seconds=time.monotonic()-start)
            (root/f'run_{i}.log').write_text(z.stdout+z.stderr)
        except subprocess.TimeoutExpired as exc:
            row.update(status='timeout',timeout_seconds=ar.timeout,elapsed_seconds=time.monotonic()-start)
            data=(exc.stdout or b'')+(exc.stderr or b'')
            (root/f'run_{i}.log').write_bytes(data if isinstance(data,bytes) else data.encode())
        record['commands'].append(row)
        (root/'RELEASE_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
    for name in ('scan.json','profiles.json','examples.json','radius8.json'):
        a=root/'certificates'/name;b=root/'certificates_optimized'/name
        record['normal_optimized_agreement'][name]=a.is_file() and b.is_file() and a.read_bytes()==b.read_bytes()
    for key,path in [('main_report',root/'certificates/verification.json'),('independent_report',root/'independent.json')]:
        if path.is_file():
            try:record[key]=json.loads(path.read_text())
            except ValueError:record[key]={'parse_error':True}
    record['source_sha256']={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in ('core.tex','preprint.tex','verify.py','check_independent.py')}
    record['new_replay_success']=(all(x.get('returncode')==0 for x in record['commands']) and all(record['normal_optimized_agreement'].values()))
    (root/'RELEASE_EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
if __name__=='__main__':main()
