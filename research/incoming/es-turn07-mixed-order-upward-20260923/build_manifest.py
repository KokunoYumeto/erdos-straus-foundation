from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXCLUDED_DIRECTORIES = {"__pycache__", "rendered"}
EXCLUDED_SUFFIXES = {
    ".aux",
    ".fls",
    ".fdb_latexmk",
    ".out",
    ".synctex.gz",
    ".toc",
}
EXCLUDED_FILES = {"MANIFEST.json"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def retained(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if path.name in EXCLUDED_FILES:
        return False
    if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
        return False
    if any(path.name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return False
    if path.name in {"preprint.log", "workbench.log"}:
        return False
    return True


def main() -> None:
    manifest: dict[str, dict[str, int | str]] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or not retained(path):
            continue
        relative = path.relative_to(ROOT).as_posix()
        manifest[relative] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
    target = ROOT / "MANIFEST.json"
    target.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
