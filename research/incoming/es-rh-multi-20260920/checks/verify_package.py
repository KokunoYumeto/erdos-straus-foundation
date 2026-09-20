#!/usr/bin/env python3
"""Verify every distributed payload file against MANIFEST.json."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

def main()->None:
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'MANIFEST.json').read_text())
    for record in manifest['files']:
        relative=Path(record['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise RuntimeError('Unsafe manifest path')
        path=root/relative
        data=path.read_bytes()
        if len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']:
            raise RuntimeError(f'Payload mismatch: {relative}')
    print(json.dumps({'status':'PASS','verified_files':len(manifest['files'])},sort_keys=True))

if __name__=='__main__':main()
