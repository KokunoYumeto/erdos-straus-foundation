#!/usr/bin/env python3
"""Build a source-complete release and record only actual execution outcomes."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,tempfile,time,zipfile
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'certificates'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(cmd,cwd=ROOT,log=None,timeout=45):
    t=time.monotonic()
    try:
        z=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True,timeout=timeout)
        text=z.stdout+z.stderr
        if log:(ROOT/log).write_text(text)
        return dict(command=cmd,returncode=z.returncode,elapsed_seconds=time.monotonic()-t,
                    output_tail=text[-2000:])
    except subprocess.TimeoutExpired as e:
        return dict(command=cmd,status='timeout',timeout_seconds=timeout)
def read(p):return json.loads(Path(p).read_text())
record={'date':'2026-09-20','universal_ES_proved':False,'universal_TypeII_proved':False,
        'Turn7_universal_milestone_completed':False,'commands':[]}
for cmd,log in [
    ([sys.executable,'verify.py','--bound','3000','--target-bound','120','--j-bound','5000','--out','certificates'],'main.log'),
    ([sys.executable,'-O','verify.py','--bound','3000','--target-bound','120','--j-bound','5000','--out','certificates_optimized'],'optimized.log'),
    ([sys.executable,'check_independent.py','--input','certificates','--out','certificates/independent.json'],'independent.log')]:
    rec=run(cmd,log=log);record['commands'].append(rec)
    if rec.get('returncode')!=0:
        (ROOT/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
        raise RuntimeError('A required arithmetic replay failed; no successful release asserted.')
main=read(OUT/'summary.json');ind=read(OUT/'independent.json')
if not(main['success'] and ind['success']):raise RuntimeError('Missing success receipt')
# The full original census is cross-checked, not silently inherited.
if main['primes']!=211 or any(main['totals'].get(k)!=v for k,v in
 {'E':5700,'M':5268,'original_divisor_vectors':1877004}.items()):
    raise RuntimeError('Full-source census mismatch')
mathnames=['capacity.json','character_classes.json','scan.json','examples.json']
agreement={n:(OUT/n).read_bytes()==(ROOT/'certificates_optimized'/n).read_bytes() for n in mathnames}
if not all(agreement.values()):raise RuntimeError('Optimized replay changed mathematical output')
record.update(success=True,main=main,independent=ind,normal_optimized_identical=agreement,
              tests_are_not_independent_review=True)
record['latex']=[]
for name in ['workbench','preprint']:
    for passno in range(2):
        z=run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],log=f'latex-{name}-{passno}.log')
        record['latex'].append(z)
        if z.get('returncode')!=0:
            (ROOT/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
            raise RuntimeError('LaTeX build failed')
    run(['pdftotext','-layout',name+'.pdf',name+'.txt'],log=f'pdftext-{name}.log')
# Exact source hashes; no fonts or credentials are distributed.
record['source_sha256']={n:sha(ROOT/n) for n in
 ['core.tex','workbench.tex','preprint.tex','verify.py','check_independent.py']}
record['pdf_sha256']={n:sha(ROOT/(n+'.pdf')) for n in ['workbench','preprint']}
# Rendering is recorded independently of whether the image was manually inspected.
render=ROOT/'rendered';render.mkdir(exist_ok=True)
record['rendering']=[]
for name in ['workbench','preprint']:
    z=run(['pdftoppm','-r','105','-png',str(ROOT/(name+'.pdf')),str(render/name)],log=f'render-{name}.log')
    record['rendering'].append(z)
record['visual_review_claim']=False
record['pdf_pages']={}
try:
    from pypdf import PdfReader
    record['pdf_pages']={n:len(PdfReader(str(ROOT/(n+'.pdf'))).pages) for n in ['workbench','preprint']}
except ImportError:pass
(ROOT/'verification.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
# Source-only git history: explicitly not an upstream clone or remote branch.
repo=ROOT/'git_record';scope='research/incoming/es-turn07-capacity-completion-20260920'
if repo.exists():shutil.rmtree(repo)
(repo/scope).mkdir(parents=True)
source_names=['README.md','core.tex','workbench.tex','preprint.tex','verify.py','check_independent.py',
 'MORPHISMS.md','CORRECTION.md','HANDOFF_TURN_7_REMAINDER.md','lean_plan.md','source_reading.json']
for n in source_names:shutil.copy2(ROOT/n,repo/scope/n)
(repo/scope/'certificates').mkdir()
for n in ['capacity.json','character_classes.json','examples.json']:
    shutil.copy2(OUT/n,repo/scope/'certificates'/n)
for cmd in [['git','init','-q'],['git','config','user.name','The Clankers'],
 ['git','config','user.email','research@users.noreply.github.com'],['git','add','.'],
 ['git','commit','-q','-m','research(es): complete original negative-shape cofactor capacity']]:
    z=run(cmd,cwd=repo)
    if z.get('returncode')!=0:raise RuntimeError('Local source history failed')
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
patch=subprocess.check_output(['git','format-patch','--root','--stdout'],cwd=repo)
(ROOT/'integration.patch').write_bytes(patch)
z=run(['git','bundle','create',str(ROOT/'source_history.bundle'),'--all'],cwd=repo)
if z.get('returncode')!=0:raise RuntimeError('Local Git bundle failed')
fsck=run(['git','fsck','--full'],cwd=repo)
# Do not infer a remote PR from a local commit or from account permission.
publication=dict(remote_pr_created=False,status='No remote write action was confirmed for this continuation.',
    local_commit=head,history_kind='new source-only repository; not a clone of upstream main',
    additive_paths=len(source_names)+3,base_last_observed='2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3',
    local_git_fsck_returncode=fsck.get('returncode'))
(ROOT/'publication_receipt.json').write_text(json.dumps(publication,indent=2)+'\n')
# Hash an immutable byte snapshot. Exclude scratch replays and local .git objects.
include={}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT)
    if any(x in {'git_record','__pycache__','test','certificates_optimized','rendered','fresh_extract'} for x in rel.parts):continue
    if p.suffix in {'.aux','.out','.toc','.pyc','.log'} or p.name in {'MANIFEST.json','debug_receipt.png'}:continue
    include[str(rel)]=p.read_bytes()
manifest={n:dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest()) for n,b in include.items()}
include['MANIFEST.json']=(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode()
(ROOT/'MANIFEST.json').write_bytes(include['MANIFEST.json'])
archive=Path('/mnt/data/ES_Turn7_Capacity_Completion_20260920.zip')
fd,tmp=tempfile.mkstemp(dir='/mnt/data',suffix='.zip');os.close(fd);tmp=Path(tmp)
with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
    for n,b in include.items():z.writestr(n,b)
with zipfile.ZipFile(tmp) as z:
    if z.testzip() is not None:raise RuntimeError('ZIP integrity failure')
    for n,r in manifest.items():
        if hashlib.sha256(z.read(n)).hexdigest()!=r['sha256']:raise RuntimeError('Manifest mismatch')
os.replace(tmp,archive)
# Fresh extraction full arithmetic replay, not just an archive checksum.
fresh=Path(tempfile.mkdtemp(prefix='es-capacity-fresh-',dir='/mnt/data'))
with zipfile.ZipFile(archive) as z:z.extractall(fresh)
fresh_cmds=[]
for cmd in [[sys.executable,'verify.py','--bound','3000','--target-bound','120','--j-bound','5000','--out','fresh_normal'],
 [sys.executable,'-O','verify.py','--bound','3000','--target-bound','120','--j-bound','5000','--out','fresh_optimized'],
 [sys.executable,'check_independent.py','--input','fresh_normal','--out','fresh_independent.json']]:
    z=run(cmd,cwd=fresh);fresh_cmds.append(z)
    if z.get('returncode')!=0:raise RuntimeError('Fresh extraction replay failed')
fresh_equal={n:all((fresh/path/n).read_bytes()==(OUT/n).read_bytes() for path in ['fresh_normal','fresh_optimized']) for n in mathnames}
if not all(fresh_equal.values()):raise RuntimeError('Fresh output mismatch')
parent=Path('/mnt/data/ES_Turns6_7_With_Fabel_Bridge_20260920.zip')
cumulative=Path('/mnt/data/ES_Turns6_7_With_Capacity_Completion_20260920.zip')
fd,tmp=tempfile.mkstemp(dir='/mnt/data',suffix='.zip');os.close(fd);tmp=Path(tmp)
with zipfile.ZipFile(tmp,'w',zipfile.ZIP_STORED) as z:
    if parent.is_file():z.write(parent,'preserved/'+parent.name)
    z.write(archive,'current/'+archive.name)
    z.writestr('00_START_HERE.txt','The preceding cumulative archive is preserved byte-for-byte when present. The current tranche completes a fixed-target capacity problem and original branch transfers, not the universal ES existence step. Open current/ first. Execution receipts and source history have their exact scopes; old mathematics was not freshly audited.\n')
os.replace(tmp,cumulative)
receipt=dict(archive=str(archive),bytes=archive.stat().st_size,sha256=sha(archive),
    cumulative_archive=str(cumulative),cumulative_sha256=sha(cumulative),
    predecessor_preserved=parent.is_file(),predecessor_sha256=sha(parent) if parent.is_file() else None,
    manifest_entries_verified=len(manifest),main=main,independent=ind,
    normal_optimized_identical=agreement,fresh_commands=fresh_cmds,fresh_mathematical_files_identical=fresh_equal,
    pdf_pages=record['pdf_pages'],publication=publication,universal_ES_proved=False,
    Turn7_universal_milestone_completed=False,priority_claim=False,visual_review_claim=False)
Path('/mnt/data/ES_Turn7_Capacity_Completion_Receipt_20260920.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:receipt[k] for k in ['archive','bytes','manifest_entries_verified','pdf_pages','publication']},indent=2))
print('MAIN',main['checks'],main['totals']);print('INDEPENDENT',ind['checks'])
