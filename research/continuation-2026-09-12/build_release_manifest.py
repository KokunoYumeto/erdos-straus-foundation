#!/usr/bin/env python3
"""Generate the exact new-continuation file manifest; no network or source edits."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
original=json.loads((ROOT/'received/ARTIFACT_PROVENANCE.json').read_text(encoding='utf-8'))
paths=[]
for folder in [ROOT,ROOT/'reconstructed',ROOT/'output/pdf']:
    paths.extend(p for p in folder.iterdir() if p.is_file()
                 and (p.suffix in {'.md','.json','.tex','.py','.pdf'} or p.name=='.gitignore')
                 and p.name!='RELEASE_FILES.json')
paths.extend(p for p in (ROOT/'checks').rglob('*') if p.is_file()
             and p.name.endswith(('.json','.json.gz')))
entries=[]
for p in sorted(set(paths)):
    data=p.read_bytes()
    entries.append({'path':p.relative_to(ROOT).as_posix(),'bytes':len(data),
                    'sha256':hashlib.sha256(data).hexdigest()})
result={'scope':'Exact files of the new reader, proofs, records and actual replay outputs; original source hashes are separate.',
        'original_manifest':'received/ARTIFACT_PROVENANCE.json',
        'original_files':len(original['members']),
        'original_manifest_sha256':hashlib.sha256((ROOT/'received/ARTIFACT_PROVENANCE.json').read_bytes()).hexdigest(),
        'new_files':entries}
(ROOT/'RELEASE_FILES.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'new_file_records':len(entries),'original_file_records':len(original['members'])}))
