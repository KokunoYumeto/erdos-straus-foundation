#!/usr/bin/env python3
"""Reproduce all declared arithmetic checks in normal and optimized Python."""
from __future__ import annotations
import argparse,hashlib,json,subprocess,sys,time
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('--bound',type=int,default=10000);p.add_argument('--directory',type=Path,default=Path('reproduced'));a=p.parse_args()
    root=Path(__file__).resolve().parent;out=a.directory.resolve();out.mkdir(parents=True,exist_ok=True)
    normal=out/'normal';opt=out/'optimized';commands=[]
    for flag,dest in [([],normal),(['-O'],opt)]:
        dest.mkdir(parents=True,exist_ok=True)
        jobs=[['verify_fibres.py','--bound',str(a.bound),'--out',str(dest)],
              ['verify_spectrum.py','--out',str(dest)],
              ['check_independent.py','--input',str(dest),'--out',str(dest/'independent.json')]]
        for job in jobs:
            cmd=[sys.executable,*flag,*job];start=time.monotonic()
            r=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
            (dest/(job[0]+'.log')).write_bytes((r.stdout+r.stderr).encode('utf-8'))
            def portable(value):
                path=Path(value)
                if not path.is_absolute():
                    return str(value).replace('\\','/')
                for base,label in ((root,'.'),(out,'<output>')):
                    try:
                        rel=path.relative_to(base).as_posix()
                        return rel if label=='.' else f'{label}/{rel}'
                    except ValueError:
                        pass
                return f'<absolute>/{path.name}'
            recorded=['python',*flag,*[portable(value) for value in job]]
            commands.append(dict(command=recorded,returncode=r.returncode,seconds=round(time.monotonic()-start,3)))
            if r.returncode:raise RuntimeError(f'Failed command: {cmd}\n{r.stdout}\n{r.stderr}')
    matches={}
    for name in ('fibres.json','examples.json','fibre_summary.json','spectrum.json','spectrum_summary.json','independent.json'):
        L=(normal/name).read_bytes();R=(opt/name).read_bytes();matches[name]=L==R
        if L!=R:raise ArithmeticError('normal/optimized disagreement: '+name)
    source_hashes={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in root.glob('*.py')}
    report=dict(success=True,commands=commands,normal_optimized_identical=matches,source_sha256=source_hashes,
                main=json.loads((normal/'fibre_summary.json').read_text()),spectrum=json.loads((normal/'spectrum_summary.json').read_text()),
                independent=json.loads((normal/'independent.json').read_text()),universal_ES_proved=False,
                independent_human_mathematical_review=False,lean_build=False)
    (out/'execution.json').write_bytes((json.dumps(report,indent=2,sort_keys=True)+'\n').encode('utf-8'))
    print(json.dumps(dict(success=True,normal_optimized_identical=all(matches.values()),arithmetic_main_checks=report['main']['checks'],
                         spectrum_checks=report['spectrum']['checks'],independent_checks=report['independent']['checks']),sort_keys=True))
if __name__=='__main__':main()
