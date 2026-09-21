#!/usr/bin/env python3
"""Write a deterministic SHA-256 manifest for the integrated module."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "MANIFEST.json"
EXCLUDED_SUFFIXES = {".aux", ".log", ".out", ".toc"}


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return (
        path.is_file()
        and path != OUT
        and "__pycache__" not in rel.parts
        and path.suffix not in EXCLUDED_SUFFIXES
    )


def main() -> None:
    entries = []
    for path in sorted((p for p in ROOT.rglob("*") if included(p)),
                       key=lambda p: p.relative_to(ROOT).as_posix()):
        data = path.read_bytes()
        entries.append({
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": len(data),
            "sha256": sha256(data).hexdigest(),
        })
    manifest = {
        "schema": "sha256-file-manifest-v1",
        "root": "research/incoming/es-turn07-global-receiver-determinant-20260921",
        "self_excluded": "MANIFEST.json",
        "excluded_suffixes": sorted(EXCLUDED_SUFFIXES),
        "entries": entries,
    }
    OUT.write_bytes((json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    print(f"wrote {OUT.name} with {len(entries)} entries")


if __name__ == "__main__":
    main()
