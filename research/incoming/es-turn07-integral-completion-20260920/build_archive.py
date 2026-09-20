#!/usr/bin/env python3
"""Local immutable snapshot, fresh arithmetic/PDF replay, cumulative handoff.
The mathematical verifiers are standard-library-only. This release check uses
PyMuPDF for PDF text/pixel comparison and an external pdflatex executable.
"""
from __future__ import annotations
import hashlib,json,os,shutil,subprocess,sys,tempfile,time,zipfile
from pathlib import Path
import fitz
R=Path(__file__).resolve().parent
OUT=R.parent
CURRENT=OUT/'ES_Turn7_Integral_Completion_20260920.zip'
PREVIOUS=OUT/'ES_Turns6_7_With_Capacity_Completion_20260920.zip'
CUMULATIVE=OUT/'ES_Turns6_7_With_Integral_Completion_20260920.zip'
RECEIPT=OUT/'ES_Turn7_Integral_Completion_Receipt_20260920.json'

def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def filehash(p:Path)->str:return sha(p.read_bytes())
def pdf_record(path:Path):
 d=fitz.open(path)
 return {'pages':len(d),'text_sha256':sha(''.join(p.get_text() for p in d).encode()),
         'pixels':[sha(p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples) for p in d]}
def run(cmd,cwd,log):
 p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True,timeout=45)
 log.append({'command':cmd,'returncode':p.returncode})
 if p.returncode:raise RuntimeError(p.stdout+'\n'+p.stderr)
 return p

def main():
 t=time.monotonic();log=[]
 required=['core.tex','preprint.tex','verify.py','check_independent.py','verification.json',
           'workbench.pdf','preprint.pdf','crt_control.pdf','publication_receipt.json']
 for n in required:
  if not (R/n).is_file():raise FileNotFoundError(n)
 old=json.loads((R/'verification.json').read_text())
 if not old['mathematical_replay_success']:raise ArithmeticError('Main replay not successful')
 # Keep the two-page auxiliary proof as well, but give readers the main preprint first.
 for n in ('workbench','preprint','crt_control'):
  if 'Overfull' in (R/(n+'.log')).read_text():raise ArithmeticError('Unresolved overfull box: '+n)
 d=fitz.open(R/'preprint.pdf')
 (R/'preprint_pages').mkdir(exist_ok=True)
 for i,p in enumerate(d):
  p.get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(R/'preprint_pages'/f'page-{i+1:02d}.png')
 snapshot={}
 allowed_suffix={'.md','.tex','.py','.json','.pdf','.patch','.bundle','.sh'}
 for p in sorted(R.iterdir()):
  if p.is_file() and p.suffix in allowed_suffix and p.name!='MANIFEST.json':snapshot[p.name]=p.read_bytes()
 for sub in ('certificates','antecedent','preprint_pages'):
  for p in sorted((R/sub).rglob('*')):
   if p.is_file():snapshot[str(p.relative_to(R))]=p.read_bytes()
 manifest={n:{'bytes':len(b),'sha256':sha(b)} for n,b in snapshot.items()}
 snapshot['MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
 (R/'MANIFEST.json').write_bytes(snapshot['MANIFEST.json'])
 with tempfile.NamedTemporaryFile(dir=OUT,suffix='.zip',delete=False) as tmp:tmpname=Path(tmp.name)
 try:
  with zipfile.ZipFile(tmpname,'w',zipfile.ZIP_DEFLATED) as z:
   for n,b in snapshot.items():z.writestr(n,b)
  with zipfile.ZipFile(tmpname) as z:
   if z.testzip() is not None:raise ArithmeticError('zip CRC failure')
   for n,e in manifest.items():
    if sha(z.read(n))!=e['sha256']:raise ArithmeticError('manifest mismatch: '+n)
  os.replace(tmpname,CURRENT)
 finally:
  if tmpname.exists():tmpname.unlink()
 fresh=OUT/'_es_integral_completion_fresh'
 if fresh.exists():shutil.rmtree(fresh)
 fresh.mkdir()
 with zipfile.ZipFile(CURRENT) as z:z.extractall(fresh)
 for mode,directory in (([], 'fresh_normal'),(['-O'],'fresh_optimized')):
  run([sys.executable]+mode+['verify.py','--bound','3000','--out',directory],fresh,log)
 for name in ('scan.json','examples.json','orders.json'):
  expect=(R/'certificates'/name).read_bytes()
  for output in ('fresh_normal','fresh_optimized'):
   if (fresh/output/name).read_bytes()!=expect:raise ArithmeticError('Fresh table mismatch: '+name)
 run([sys.executable,'check_independent.py','--input','fresh_normal','--out','fresh_independent.json'],fresh,log)
 independent=json.loads((fresh/'fresh_independent.json').read_text())
 expected=json.loads((R/'certificates/independent.json').read_text())
 for key in ('success','bound','primes','checks','counts','original_vectors','source_sha256'):
  if independent[key]!=expected[key]:raise ArithmeticError('Independent mismatch: '+key)
 pdfs={}
 for n in ('workbench','preprint','crt_control'):
  for _ in range(2):run(['pdflatex','-interaction=nonstopmode','-halt-on-error',n+'.tex'],fresh,log)
  a=pdf_record(R/(n+'.pdf'));b=pdf_record(fresh/(n+'.pdf'))
  if a!=b:raise ArithmeticError('Fresh PDF difference: '+n)
  pdfs[n]=a
 # A small certificate-only ZIP and a preprint-source bundle are convenience copies.
 CERTS=OUT/'ES_Turn7_Integral_Completion_Certificates_20260920.zip'
 with zipfile.ZipFile(CERTS,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in snapshot.items():
   if n.startswith('certificates/') or n in ('verify.py','check_independent.py','verification.json','source_reading.json'):
    z.writestr(n,b)
 PREPRINT=OUT/'ES_Turn7_Integral_Completion_Preprint_20260920.zip'
 with zipfile.ZipFile(PREPRINT,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in snapshot.items():
   if n.startswith('preprint_pages/') or n in ('preprint.tex','preprint.pdf','preamble.tex'):
    z.writestr(n,b)
 if not PREVIOUS.is_file():raise FileNotFoundError('Predecessor cumulative archive missing')
 previous_hash=filehash(PREVIOUS)
 with zipfile.ZipFile(PREVIOUS) as z:
  if z.testzip() is not None:raise ArithmeticError('Predecessor CRC failure')
 with tempfile.NamedTemporaryFile(dir=OUT,suffix='.zip',delete=False) as tmp:tmpname=Path(tmp.name)
 try:
  with zipfile.ZipFile(tmpname,'w',zipfile.ZIP_STORED) as z:
   z.write(PREVIOUS,'preserved/'+PREVIOUS.name)
   z.write(CURRENT,'current/'+CURRENT.name)
   z.writestr('00_START_HERE.md','# Turn 7 continuation\n\nThe predecessor is preserved byte-for-byte. '
     'The current package contains original integral completion proofs and a joint source-domain '
     'obstruction, not universal ES existence. Read its README and verification.json. '
     'Historical preservation is not a whole-programme audit.\n')
  with zipfile.ZipFile(tmpname) as z:
   if z.testzip() is not None:raise ArithmeticError('Cumulative CRC failure')
   if sha(z.read('preserved/'+PREVIOUS.name))!=previous_hash:raise ArithmeticError('Predecessor altered')
   if sha(z.read('current/'+CURRENT.name))!=filehash(CURRENT):raise ArithmeticError('Current altered')
  os.replace(tmpname,CUMULATIVE)
 finally:
  if tmpname.exists():tmpname.unlink()
 receipt={'date':'2026-09-20','current_archive':str(CURRENT),'cumulative_archive':str(CUMULATIVE),
          'current_bytes':CURRENT.stat().st_size,'current_sha256':filehash(CURRENT),
          'cumulative_bytes':CUMULATIVE.stat().st_size,'cumulative_sha256':filehash(CUMULATIVE),
          'predecessor':{'path':str(PREVIOUS),'sha256':previous_hash,'preserved_byte_for_byte':True},
          'manifest_entries_verified':len(manifest),'fresh_commands':log,
          'fresh_arithmetic_success':True,'normal_optimized_tables_identical':True,
          'main':json.loads((R/'certificates/summary.json').read_text()),
          'independent':expected,'fresh_PDF_text_and_pixels_identical':True,
          'PDFs':pdfs,'render_scale':1.5,'rendered_pages':sum(x['pages'] for x in pdfs.values()),
          'publication':json.loads((R/'publication_receipt.json').read_text()),
          'universal_ES_proved':False,'turn7_universal_milestone_completed':False,
          'elapsed_seconds':time.monotonic()-t}
 RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n')
 for p in (CURRENT,CUMULATIVE,CERTS,PREPRINT,RECEIPT):p.chmod(0o644)
 print(json.dumps({k:receipt[k] for k in ('current_archive','cumulative_archive','manifest_entries_verified',
       'fresh_arithmetic_success','fresh_PDF_text_and_pixels_identical','rendered_pages')},indent=2))
if __name__=='__main__':main()
