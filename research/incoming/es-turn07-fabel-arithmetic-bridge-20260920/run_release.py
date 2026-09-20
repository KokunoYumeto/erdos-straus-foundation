#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,json,hashlib,time,os
root=Path(__file__).resolve().parent
runs=[]
commands=[
 [sys.executable,'verify.py','--bound','3000','--out','certificates'],
 [sys.executable,'-O','verify.py','--bound','3000','--out','certificates_optimized'],
 [sys.executable,'check_independent.py','--input','certificates','--out','certificates/independent.json'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','workbench.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','workbench.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','preprint.tex'],
 ['pdflatex','-interaction=nonstopmode','-halt-on-error','preprint.tex']]
for i,c in enumerate(commands):
 t=time.monotonic();r=subprocess.run(c,cwd=root,text=True,errors="replace",capture_output=True,timeout=180)
 (root/f'run_{i}.log').write_text(r.stdout+r.stderr)
 runs.append(dict(command=c,returncode=r.returncode,seconds=time.monotonic()-t,log=f'run_{i}.log'))
 if r.returncode:
  (root/'verification.json').write_text(json.dumps(dict(success=False,runs=runs),indent=2))
  raise RuntimeError(str(c)+' failed:\n'+(r.stdout+r.stderr)[-2000:])
comparison={n:(root/'certificates'/n).read_bytes()==(root/'certificates_optimized'/n).read_bytes() for n in ('scan.json','examples.json')}
if not all(comparison.values()):raise ArithmeticError('optimized replay mismatch')
main=json.loads((root/'certificates/report.json').read_text());ind=json.loads((root/'certificates/independent.json').read_text())
if not main['success'] or not ind['success']:raise ArithmeticError('receipt failure')
if main['output_sha256']['scan.json']!=ind['scan_sha256']:raise ArithmeticError('independent source mismatch')
pdfs={}
for name in ('workbench','preprint'):
 s=subprocess.check_output(['pdfinfo',str(root/(name+'.pdf'))],text=True)
 pages=int(next(line.split(':')[1] for line in s.splitlines() if line.startswith('Pages:')))
 subprocess.run(['pdftotext','-layout',str(root/(name+'.pdf')),str(root/(name+'_rendered.txt'))],check=True)
 warnings=[line for line in (root/(name+'.log')).read_text(errors="replace").splitlines() if 'Overfull' in line or 'undefined' in line]
 pdfs[name]=dict(pages=pages,warnings=warnings,sha256=hashlib.sha256((root/(name+'.pdf')).read_bytes()).hexdigest())
files=['verify.py','check_independent.py','core.tex','root_orders.tex','workbench.tex','preprint.tex']
report=dict(success=True,runs=runs,normal_optimized_agreement=comparison,main=main,independent=ind,pdfs=pdfs,
            source_sha256={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in files},
            universal_ES_proved=False,turn7_universal_existence_completed=False,independent_mathematical_review=False,lean_build=False)
(root/'verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:report[k] for k in ['success','normal_optimized_agreement','pdfs']},indent=2))
print('MAIN',main['checks'],main['primes'],main['totals'])
print('SEPARATE',ind['checks'])
