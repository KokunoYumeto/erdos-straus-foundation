#!/usr/bin/env python3
"""Build the deterministic source-and-certificate manifest for this module."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXCLUDED_PARTS = {"__pycache__", "build", "reproduced", "reproduced_local"}
EXCLUDED_NAMES = {"MANIFEST.json"}


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return (
        path.is_file()
        and path.name not in EXCLUDED_NAMES
        and not any(part in EXCLUDED_PARTS for part in rel.parts)
        and path.suffix.lower() not in {".aux", ".log", ".out", ".toc"}
        and not path.name.endswith(".synctex.gz")
    )


entries = {}
for path in sorted((p for p in ROOT.rglob("*") if included(p)), key=lambda p: p.as_posix()):
    data = path.read_bytes()
    entries[path.relative_to(ROOT).as_posix()] = {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }

(ROOT / "MANIFEST.json").write_bytes(
    (json.dumps(entries, indent=2, sort_keys=True) + "\n").encode("utf-8")
)
print(json.dumps({"entries": len(entries), "success": True}, sort_keys=True))
