#!/usr/bin/env python3
"""Replay the exact suites in normal and optimized Python, comparing receipts.

Each suite runs with an explicit timeout and checks that cannot be disabled by -O.
No network access, credentials, native arithmetic moment values, or Lean build is
required or claimed. The script must be launched from an intact package.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SUITES={
 'residue':'check_residue.py',
 'es_slice':'check_es_slice.py',
 'gram_floor':'check_gram_floor.py',
 'lowrank':'check_lowrank.py',
 'gauss_bridge':'check_gauss_bridge.py',
 'previous_bounds':'check_previous_bounds.py',
 'monodromy':'check_monodromy.py',
 'bernstein':'check_bernstein.py',
 'local_transport':'check_local_transport.py',
 'additional':'check_additional.py',
}

def run_one(name: str, timeout: float)->dict:
    script=SUITES[name]
    receipt=None
    first_stdout=None
    first_json=None
    modes=[]
    for flag in [[],['-O']]:
        proc=subprocess.run([sys.executable,*flag,str(HERE/script)],cwd=HERE,
                            capture_output=True,timeout=timeout)
        if proc.returncode:
            raise RuntimeError(f'{script} {flag}: failure\n'+proc.stderr.decode(errors='replace'))
        message=json.loads(proc.stdout.decode().strip().splitlines()[-1])
        if message.get('status')!='PASS': raise RuntimeError(f'{script}: missing PASS')
        path=ROOT/'results'/(message['suite']+'.json')
        data=path.read_bytes()
        parsed=json.loads(data)
        if first_stdout is None:
            first_stdout=proc.stdout;first_json=data;receipt=parsed
        elif proc.stdout!=first_stdout or data!=first_json:
            raise RuntimeError(f'{script}: optimization changed output or receipt')
        modes.append('optimized' if flag else 'normal')
    result={'suite':name,'script':script,'status':'PASS','modes':modes,
            'identical_stdout':True,'identical_json':True,
            'exact_checks_per_mode':receipt['exact_checks'],
            'negative_controls_per_mode':receipt['negative_controls'],
            'receipt_sha256':hashlib.sha256(first_json).hexdigest()}
    destination=ROOT/'results'/'replay';destination.mkdir(exist_ok=True)
    (destination/(name+'.json')).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)
    return result

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite',choices=list(SUITES))
    parser.add_argument('--timeout',type=float,default=120.0)
    args=parser.parse_args()
    names=[args.suite] if args.suite else list(SUITES)
    for name in names:run_one(name,args.timeout)
    if not args.suite:
        aggregate()

def aggregate()->dict:
    import sympy
    results=[json.loads((ROOT/'results'/'replay'/(name+'.json')).read_text()) for name in SUITES]
    report={'status':'PASS','python':platform.python_version(),'sympy':sympy.__version__,
            'suite_count':len(results),
            'exact_checks_per_mode':sum(x['exact_checks_per_mode'] for x in results),
            'negative_controls_per_mode':sum(x['negative_controls_per_mode'] for x in results),
            'all_normal_optimized_receipts_identical':all(x['identical_json'] and x['identical_stdout'] for x in results),
            'scope':'Exact symbolic identities and bounded rational diagnostics; no Lean verification or evaluated native arithmetic moments.',
            'suites':results}
    (ROOT/'results'/'VERIFICATION_SUMMARY.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    return report
if __name__=='__main__':main()
