#!/usr/bin/env python3
"""Mutation regression test: old acceptance versus corrected rejection."""
from pathlib import Path
import json,tempfile,shutil,subprocess,sys,hashlib
from verify_audit import LIFTS9,views,norm
R=Path(__file__).resolve().parent
source=R/'inputs'/'leech_trace_inverse'
rows=[]
def run(cmd):
    p=subprocess.run(cmd,text=True,capture_output=True,timeout=30)
    return {'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
with tempfile.TemporaryDirectory(prefix='leech_inverse_mutation_') as tmp:
    tmp=Path(tmp);copy=tmp/'old';shutil.copytree(source,copy)
    cert=copy/'certificates'
    for kind in ('four_view_column','nonminimal_representative'):
        shutil.rmtree(cert);shutil.copytree(source/'certificates',cert)
        if kind=='four_view_column':
            f=cert/'twelve_views.json';d=json.loads(f.read_text());d['right_inverse_numerators'][3]=[2*x for x in d['right_inverse_numerators'][3]];f.write_text(json.dumps(d))
            argv=['--four','1','2','3','2','3','1','3','2','1','1','4','1']
        else:
            f=cert/'shortest_lifts.json';d=json.loads(f.read_text());c=next(c for c in d['classes'] if c['residue_mod4']==[1,0,0]);c['representative_numerator']=[x+2*y for x,y in zip(c['representative_numerator'],LIFTS9[3])];f.write_text(json.dumps(d));argv=['--trace','1','0','0']
        old=run([sys.executable,str(copy/'reconstruct.py')]+argv)
        new=run([sys.executable,str(R/'reconstruct_checked.py'),'--cert-dir',str(cert)]+argv)
        if old['exit']!=0 or new['exit']==0:raise ArithmeticError('Regression behaviour not demonstrated')
        olddata=json.loads(old['stdout']);x=olddata['numerator']
        rows.append({'mutation':kind,'old_accepted_output':olddata,'actual_first_four_triples':views(x),'actual_norm':str(norm(x)),'patched_rejection':new['stderr'].splitlines()[-1]})
    clean=[]
    for mode in ('normal','optimized'):
        for argv in (['--trace','306','16218','1082101','--p','1201'],['--four','1','2','3','2','3','1','3','2','1','1','4','1']):
            c=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(R/'reconstruct_checked.py')]+argv
            r=run(c)
            if r['exit']!=0:raise ArithmeticError(r['stderr'])
            clean.append({'mode':mode,'args':argv,'output':json.loads(r['stdout'])})
    if clean[0]['output']!=clean[2]['output'] or clean[1]['output']!=clean[3]['output']:raise ArithmeticError('Optimization mismatch')
out={'status':'PASS','interpretation':'Two output-validation gaps, not counterexamples to the unmodified mathematical certificates.','mutations':rows,'clean_runs':clean,'patched_source_sha256':hashlib.sha256((R/'reconstruct_checked.py').read_bytes()).hexdigest()}
(R/'certificates'/'validation_regressions.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':'PASS','rejected_mutations':2,'clean_runs':4,'normals_equal_optimized':True}))
