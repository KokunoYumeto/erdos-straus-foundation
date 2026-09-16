#!/usr/bin/env python3
"""Verify exact package bytes against manifest.json; standard library only."""
from pathlib import Path
from hashlib import sha256
import json

def main():
    root=Path(__file__).resolve().parent
    data=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
    for row in data['files']:
        p=(root/row['path']).resolve()
        if p.parent!=root:
            raise RuntimeError('Only direct bundle files are allowed')
        b=p.read_bytes()
        if len(b)!=row['bytes'] or sha256(b).hexdigest()!=row['sha256']:
            raise RuntimeError('File identity mismatch: '+row['path'])
    print(json.dumps({'files_verified':len(data['files']),'status':'passed','scope':'File identity only, not mathematical validation'},sort_keys=True))
if __name__=='__main__':main()
