"""Replay only this integration's exact checks in normal and optimized Python.

No predecessor counts are inherited. Native asymptotic statements are proved
conditionally in the manuscript; these tests concern their finite interfaces.
"""
from __future__ import annotations
import hashlib, json, platform, subprocess, sys
from pathlib import Path
import sympy

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=['check_family.py','check_joint_minimum.py','check_collision.py','check_metric.py']

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def main()->None:
    collect_only='--collect-only' in sys.argv
    result=ROOT/'results'; result.mkdir(exist_ok=True)
    logs=result/'logs';logs.mkdir(exist_ok=True)
    suites=[]
    for script in SCRIPTS:
        outputs=[]; receipts=[]
        for mode in ['normal','optimized']:
            out=result/mode;out.mkdir(exist_ok=True)
            cmd=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(ROOT/'checks'/script),str(out)]
            if collect_only:
                stdout=(logs/f'{script}.{mode}.stdout').read_text()
                stderr=(logs/f'{script}.{mode}.stderr').read_text()
                if stderr:raise RuntimeError(f'Stderr present for {script} ({mode}): {stderr}')
            else:
                proc=subprocess.run(cmd,cwd=ROOT/'checks',capture_output=True,text=True,timeout=300)
                stdout,stderr=proc.stdout,proc.stderr
                (logs/f'{script}.{mode}.stdout').write_text(stdout)
                (logs/f'{script}.{mode}.stderr').write_text(stderr)
                if proc.returncode:
                    raise RuntimeError(f'{script} ({mode}) failed: {stderr[-3000:]}')
            data=json.loads(stdout)
            receipt=out/f"{data['suite']}.json"
            if data['status']!='PASS' or not receipt.exists():
                raise RuntimeError(f'Incomplete receipt for {script} ({mode})')
            outputs.append(stdout);receipts.append(receipt)
        if outputs[0]!=outputs[1] or receipts[0].read_bytes()!=receipts[1].read_bytes():
            raise RuntimeError(f'Normal/optimized mismatch in {script}')
        data=json.loads(outputs[0])
        suites.append({'script':script,'suite':data['suite'],'exact_checks_per_mode':data['exact_checks'],
                       'negative_control_executions_per_mode':data['negative_controls'],
                       'receipt_sha256':sha(receipts[0]),'normal_optimized_identical':True})
        print(f"PASS {script}: {data['exact_checks']} exact, {data['negative_controls']} negative-control executions per mode",flush=True)
    summary={'status':'PASS','suite_count':len(suites),
             'exact_checks_per_mode':sum(x['exact_checks_per_mode'] for x in suites),
             'negative_control_executions_per_mode':sum(x['negative_control_executions_per_mode'] for x in suites),
             'normal_optimized_identical':True,'python':platform.python_version(),'sympy':sympy.__version__,
             'scope':'Fresh finite exact algebra and bounded synthetic checks only. Not a Lean build, numerical evaluation of native zeta moments, or replay of unavailable source archives.',
             'source_input_sha256':sha(ROOT/'sources'/'GENERAL_FAMILY_INPUT.md'),
             'checks_sha256':{p.name:sha(p) for p in sorted((ROOT/'checks').glob('*.py'))},'suites':suites}
    (result/'VERIFICATION_SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','suite_count','exact_checks_per_mode','negative_control_executions_per_mode','normal_optimized_identical']},indent=2))

if __name__=='__main__': main()
