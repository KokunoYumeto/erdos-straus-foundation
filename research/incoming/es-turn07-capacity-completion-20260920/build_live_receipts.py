#!/usr/bin/env python3
"""Generate deterministic live-tree hashes after the repaired replay/build."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if path.name in {"MANIFEST.json", "verification.json"}:
        return True
    if any(
        part in {
            "__pycache__",
            "certificates_replay",
            "certificates_optimized_replay",
        }
        for part in rel.parts
    ):
        return True
    if path.suffix.lower() in {".aux", ".log", ".out"}:
        return True
    if "output" in rel.parts and path.name.endswith("-pass-1.txt"):
        return True
    if "output" in rel.parts and path.name.endswith("-pass-2.txt"):
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--visual-review", action="store_true")
    args = parser.parse_args()

    summary = json.loads((ROOT / "certificates_replay" / "summary.json").read_text())
    independent = json.loads(
        (ROOT / "certificates_replay" / "independent.json").read_text()
    )
    if not summary["success"] or not independent["success"]:
        raise SystemExit("arithmetic receipts do not report success")

    pdfs = {
        name: ROOT / "output" / name
        for name in ("workbench.pdf", "preprint.pdf")
    }
    pdf_receipt = {
        name: {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "pages": len(PdfReader(str(path)).pages),
        }
        for name, path in pdfs.items()
    }

    manifest = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or excluded(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        manifest[rel] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

    verification = {
        "schema_version": 1,
        "date": "2026-09-20",
        "status": "pass",
        "mathematics": {
            "main": summary,
            "independent_implementation": independent,
            "main_checks": 1161828,
            "independent_checks": 622997,
            "external_peer_review": False,
            "lean_proof": False,
        },
        "build": {
            "pdflatex_passes_per_pdf": 2,
            "pdfs": pdf_receipt,
            "visual_review_all_pages": args.visual_review,
        },
        "received_history": {
            "manifest": "received/received-inner-MANIFEST.json",
            "verification": "received/received-inner-verification.json",
            "note": "These two files describe the received package before the live TeX repair.",
        },
        "scope": {
            "universal_erdos_straus_proved": False,
            "same_grade_obstruction_only": True,
            "priority_claim": False,
        },
    }

    (ROOT / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (ROOT / "verification.json").write_text(
        json.dumps(verification, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"manifest_entries": len(manifest), **verification}, indent=2))


if __name__ == "__main__":
    main()
