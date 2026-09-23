#!/usr/bin/env python3
"""Run the active and independent exact checks."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def run(path: Path) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(path)], check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return json.loads(completed.stdout)


def main() -> None:
    root = Path(__file__).resolve().parent
    active = run(root / 'verify.py')
    independent = run(root / 'check_independent.py')
    if active.get('status') != 'pass' or independent.get('status') != 'pass':
        raise SystemExit('verification status was not pass')
    print(json.dumps({
        'status': 'pass',
        'active': active,
        'independent': independent,
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
