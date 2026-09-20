"""Build the deterministic file manifest for the Family C continuation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    files = []
    for path in sorted(ROOT.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file() or path == OUTPUT or "__pycache__" in path.parts:
            continue
        files.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    manifest = {
        "schema": "es-family-integration-file-manifest-v1",
        "module": "research/incoming/es-rh-family-integration-c-20260920",
        "file_count": len(files),
        "files": files,
    }
    OUTPUT.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
