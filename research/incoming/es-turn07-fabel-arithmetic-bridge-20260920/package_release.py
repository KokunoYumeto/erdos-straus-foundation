#!/usr/bin/env python3
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile,ZIP_DEFLATED,ZIP_STORED
from collections import Counter
import subprocess,json,hashlib,sys,shutil,os,time
r=Path(__file__).resolve().parent
# A fresh completed execution is a precondition for publication of the archive.
subprocess.run([sys.executable,str(r/'check_polynomial.py')],check=True,cwd=r,capture_output=True,text=True,errors="replace",timeout=180)
poly=json.loads((r/'polynomial_certificate.json').read_text());assert poly['success']
subprocess.run([sys.executable,str(r/'run_release.py')],check=True,cwd=r,capture_output=True,text=True,errors="replace",timeout=180)
report=json.loads((r/'verification.json').read_text());assert report['success']
assert report['main']['primes']==211
for k,n in [('E',5700),('M',5268),('divisor_vectors',1877004)]:assert report['main']['totals'][k]==n
assert all(report['normal_optimized_agreement'].values())
# Record scope changes without falsely presenting them as additional ES prime coverage.
sc=json.loads((r/'certificates/scan.json').read_text());ct=Counter();new=[]
for row in sc['rows']:
 seen=set();hard_seen=set()
 for z in row['crosses']:
  if not z['available']:continue
  src=tuple(z['source']);seen.add(src)
  if row['hard']:
   hard_seen.add(src);_,a,u,R,h,rr,s,k,*_=src;v=a*a//u;D=(4*u+1)//R
   if R!=D and max(abs(v-R),abs(v-D))>8:new.append(dict(p=row['p'],source=list(src),side=z['side'],c=z['c']))
 ct['distinct_E_states_with_new_middle_return']+=len(seen)
 ct['hard_E_states_with_new_return']+=len(hard_seen)
 ct['hard_primes_with_return']+=bool(hard_seen)
ct['hard_E_states_outside_previous_diagonal_or_radius8']=len({(z['p'],tuple(z['source'])) for z in new})
(r/'certificates/transfer_scope.json').write_text(json.dumps(dict(counts=dict(ct),strict_examples=new,scope='Original state reductions, not additional overall ES prime coverage.'),indent=2)+'\n')
# Verify the PDFs really exist, extract all page bounds, then render them.
import fitz
from PIL import Image,ImageDraw
rend=r/'render';rend.mkdir(exist_ok=True)
for p in rend.glob('*.png'):p.unlink()
render_receipt={}
for name in ('workbench','preprint'):
 doc=fitz.open(r/(name+'.pdf'));bounds=[];pages=[]
 for i,page in enumerate(doc):
  for block in page.get_text('blocks'):
   x0,y0,x1,y1=block[:4]
   if not (0<=x0<=x1<=page.rect.width+1 and 0<=y0<=y1<=page.rect.height+1):bounds.append(dict(page=i+1,box=[x0,y0,x1,y1]))
  pix=page.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False);pp=rend/f'{name}-{i+1:02d}.png';pix.save(pp);pages.append(pp)
 assert not bounds,(name,bounds)
 for start in range(0,len(pages),6):
  batch=pages[start:start+6];sheet=Image.new('RGB',(1710,810*((len(batch)+2)//3)),(225,225,225))
  for i,pp in enumerate(batch):
   im=Image.open(pp).convert('RGB');im.thumbnail((550,770));tile=Image.new('RGB',(570,810),'white');tile.paste(im,((570-im.width)//2,15));ImageDraw.Draw(tile).text((10,788),pp.name,fill='black');sheet.paste(tile,((i%3)*570,(i//3)*810))
  sheet.save(rend/f'{name}_contact_{start//6+1}.png')
 render_receipt[name]=dict(pages=len(doc),out_of_page_text_blocks=bounds)
(r/'render_receipt.json').write_text(json.dumps(render_receipt,indent=2)+'\n')
# Build a portable source-only Git record; this is not an upstream clone.
source_names=['README.md','core.tex','root_orders.tex','workbench.tex','preprint.tex','verify.py','check_independent.py','check_polynomial.py','MORPHISMS.md','HANDOFF_TURN_7_REMAINDER.md','lean_plan.md','source_reading.json','ATTEMPT.md']
with TemporaryDirectory(prefix='es_fabel_git_') as td:
 g=Path(td);subprocess.run(['git','init','-q'],cwd=g,check=True)
 subprocess.run(['git','config','user.name','The Clankers'],cwd=g,check=True)
 subprocess.run(['git','config','user.email','research@localhost'],cwd=g,check=True)
 subprocess.run(['git','commit','--allow-empty','-qm','Local source-only base; not an upstream snapshot'],cwd=g,check=True)
 dest=g/'research/incoming/es-turn07-fabel-bridge-20260920';dest.mkdir(parents=True)
 for n in source_names:shutil.copy2(r/n,dest/n)
 subprocess.run(['git','add','.'],cwd=g,check=True)
 subprocess.run(['git','commit','-qm','Original-prime Fabel fibres and exact negative-square channel returns'],cwd=g,check=True)
 commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=g,text=True).strip()
 patch=subprocess.check_output(['git','diff','HEAD^','HEAD','--binary'],cwd=g)
 (r/'integration.patch').write_bytes(patch)
 subprocess.run(['git','bundle','create',str(r/'source_history.bundle'),'--all'],cwd=g,check=True,capture_output=True)
 subprocess.run(['git','bundle','verify',str(r/'source_history.bundle')],cwd=g,check=True,capture_output=True)
 tree=subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=g,text=True).strip()
 with TemporaryDirectory(prefix='es_fabel_apply_') as tt:
  a=Path(tt);subprocess.run(['git','init','-q'],cwd=a,check=True)
  subprocess.run(['git','apply','--check',str(r/'integration.patch')],cwd=a,check=True)
  subprocess.run(['git','apply',str(r/'integration.patch')],cwd=a,check=True)
  subprocess.run(['git','add','.'],cwd=a,check=True)
  assert subprocess.check_output(['git','write-tree'],cwd=a,text=True).strip()==tree
pub=dict(remote_pr_created=False,status='No remote write was executed; no create/push action was exposed in this session.',local_source_only_commit=commit,local_tree=tree,upstream_clone=False,additive_patch_replayed=True)
(r/'publication_receipt.json').write_text(json.dumps(pub,indent=2)+'\n')
# Only distributable source and actual proof/certificate outputs enter this release.
names=source_names+['run_release.py','package_release.py','workbench.pdf','preprint.pdf','verification.json','render_receipt.json','polynomial_certificate.json','publication_receipt.json','integration.patch','source_history.bundle','publish_pr.sh','PR_BODY.md']
for p in sorted((r/'certificates').glob('*.json')):names.append(str(p.relative_to(r)))
manifest={n:dict(bytes=(r/n).stat().st_size,sha256=hashlib.sha256((r/n).read_bytes()).hexdigest()) for n in names}
(r/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n');names.append('MANIFEST.json')
archive=Path('/mnt/data/ES_Turn7_Fabel_Arithmetic_Bridge_20260920.zip')
with ZipFile(archive,'w',ZIP_DEFLATED) as z:
 for n in names:z.write(r/n,'es_turn7_fabel_bridge_20260920/'+n)
with ZipFile(archive) as z:
 assert z.testzip() is None
 for n,item in manifest.items():assert hashlib.sha256(z.read('es_turn7_fabel_bridge_20260920/'+n)).hexdigest()==item['sha256']
# Replay the exact packaged bytes in a fresh directory.
fresh=[]
with TemporaryDirectory(prefix='es_fabel_release_') as td:
 with ZipFile(archive) as z:z.extractall(td)
 rr=Path(td)/'es_turn7_fabel_bridge_20260920'
 commands=[[sys.executable,'verify.py','--bound','3000','--out','reproduced'],[sys.executable,'-O','verify.py','--bound','3000','--out','reproduced_O'],[sys.executable,'check_independent.py','--input','reproduced','--out','independent_fresh.json'],[sys.executable,'check_polynomial.py']]
 for c in commands:
  result=subprocess.run(c,cwd=rr,capture_output=True,text=True,errors="replace",timeout=180);assert result.returncode==0,(c,result.stderr[-2000:]);fresh.append(dict(command=c,returncode=result.returncode))
 for n in ('scan.json','examples.json'):
  assert (rr/'reproduced'/n).read_bytes()==(r/'certificates'/n).read_bytes()
  assert (rr/'reproduced_O'/n).read_bytes()==(r/'certificates'/n).read_bytes()
 for name in ('workbench','preprint'):
  subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=rr,capture_output=True,check=True,timeout=60)
  subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=rr,capture_output=True,check=True,timeout=60)
  a=fitz.open(rr/(name+'.pdf'));b=fitz.open(r/(name+'.pdf'))
  assert len(a)==len(b)
  assert all(a[i].get_text()==b[i].get_text() for i in range(len(a)))
  assert all(a[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).samples==b[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).samples for i in range(len(a)))
# Preserve only actually mounted predecessor bytes, never infer a historical ZIP.
predecessor=Path('/mnt/data/ES_Turns6_7_With_Shape_Rigidity_20260919.zip')
if not predecessor.is_file():predecessor=Path('/mnt/data/ES_Turn7_Shape_Rigidity_20260919.zip')
combined=Path('/mnt/data/ES_Turns6_7_With_Fabel_Bridge_20260920.zip')
with ZipFile(combined,'w',ZIP_STORED) as z:
 if predecessor.is_file():z.write(predecessor,'preserved/'+predecessor.name)
 z.write(archive,'current/'+archive.name)
 z.writestr('00_START_HERE.txt','Current proof, TeX, code and certificates are in current/. The supplied predecessor archive is preserved byte-for-byte under preserved/. This is preservation, not a fresh audit of all historical results. Turn7 universal ES occupancy remains unproved.\n')
receipt=dict(current_archive=str(archive),bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),manifest_entries_verified=len(manifest),fresh_replay=fresh,normal_optimized_identical=True,fresh_PDF_text_and_pixels_identical=True,rendered=render_receipt,main=dict(checks=report['main']['checks'],primes=report['main']['primes'],totals=report['main']['totals']),independent_checks=report['independent']['checks'],polynomial_identity_certificate=poly,transfer_scope=dict(ct),publication=pub,cumulative_archive=str(combined),cumulative_bytes=combined.stat().st_size,predecessor=None if not predecessor.is_file() else dict(path=str(predecessor),sha256=hashlib.sha256(predecessor.read_bytes()).hexdigest()),universal_ES_proved=False,turn7_existence_milestone_completed=False)
Path('/mnt/data/ES_Turn7_Fabel_Arithmetic_Bridge_Receipt_20260920.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(receipt,indent=2))
