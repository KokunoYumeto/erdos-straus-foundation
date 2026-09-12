from pathlib import Path
import subprocess,time,json,sys,hashlib,concurrent.futures,platform
R=Path(__file__).resolve().parent
jobs=[
('selectors','erdos_straus_research','verifier.py',['--bound','2000000','--families','--out','OUT'],False),
('pointwise','es_pointwise_tranche','verifier.py',['--self-test','--anchors','--cover-bound','10000000000','--out','OUT'],False),
('jordan','three_coordinate_jordan','verify.py',['--output','FILE'],True),
('cube','cube_unification','verify.py',['--out','FILE'],True),
('graded_lie','cube_unification','graded_lie.py',[],True),
('wilson_leech','cube_unification','leech_ternary.py',[],True),
('cayley','cayley_fable_bridge','verify.py',['--out','OUT'],True),
('tetrahedral','tetrahedral_markings','verify.py',['--out','OUT'],True),
('mellin','mellin_leech_research','verify.py',['--out','OUT'],True),
('trace_inverse','leech_trace_inverse','verify.py',['--out','OUT'],True)]
def run(job):
 name,folder,script,args,opt=job; receipts=[]
 for flag in (['normal','optimized'] if opt else ['normal']):
  out=R/'replays'/name/flag;out.mkdir(parents=True,exist_ok=True)
  a=[str(out) if s=='OUT' else str(out/'certificate.json') if s=='FILE' else s for s in args]
  cmd=[sys.executable]+(['-O'] if flag=='optimized' else [])+[str(R/'inputs'/folder/script)]+a
  now=time.monotonic()
  with (out/'stdout.txt').open('wb') as so,(out/'stderr.txt').open('wb') as se:
   try:
    cp=subprocess.run(cmd,cwd=out,stdout=so,stderr=se,timeout=720);rc=cp.returncode
   except subprocess.TimeoutExpired:rc='TIMEOUT'
  receipt={'name':name,'mode':flag,'command':cmd,'exit_code':rc,'elapsed_seconds':time.monotonic()-now,'source_sha256':hashlib.sha256((R/'inputs'/folder/script).read_bytes()).hexdigest()}
  receipts.append(receipt)
  (out/'execution.json').write_text(json.dumps(receipt,indent=2)+'\n')
  print(name,flag,rc,round(receipt['elapsed_seconds'],2),flush=True)
  if rc!=0:break
 if opt and len(receipts)==2 and all(r['exit_code']==0 for r in receipts):
  n,o=[R/'replays'/name/k for k in ['normal','optimized']]
  nf={p.relative_to(n).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in n.rglob('*') if p.is_file() and p.name!='execution.json'}
  of={p.relative_to(o).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in o.rglob('*') if p.is_file() and p.name!='execution.json'}
  receipts.append({'name':name,'normal_optimized_file_identity':nf==of,'normal_files':nf,'optimized_files':of})
 return receipts
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 results=[]
 for rs in pool.map(run,jobs):
  results+=rs
  (R/'replay_receipts.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'runs':results},indent=2)+'\n')
