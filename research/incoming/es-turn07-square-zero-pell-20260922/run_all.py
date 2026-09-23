#!/usr/bin/env python3
"""Run both exact implementations, with ordinary/optimized byte comparisons.
No network or third-party Python dependency. The default finite scopes are
recorded in core.tex; they are not a universal ES verification range.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

FILES = ['box_tiles.json', 'prime_squares.json', 'prefix_certificate.json',
         'worked_examples.json', 'local_certificates.json', 'sharp_packets.json',
         'negative_controls.json', 'fixed_tail_sum.json',
         'prime_square_fixed_sum.json', 'summary.json', 'independent.json']

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', default='reproduced')
    parser.add_argument('--bound', type=int, default=10000)
    parser.add_argument('--square-bound', type=int, default=2000000)
    parser.add_argument('--prefix-bound', type=int, default=67369)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    out = Path(args.directory).resolve()
    out.mkdir(parents=True, exist_ok=True)
    ordinary, optimized = out/'normal', out/'optimized'
    ordinary.mkdir(exist_ok=True); optimized.mkdir(exist_ok=True)
    commands = []
    def run(command: list[str], name: str) -> None:
        start = time.monotonic()
        result = subprocess.run(command, cwd=root, text=True, encoding='utf-8',
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out/(name+'.log')).write_bytes(result.stdout.encode('utf-8'))
        commands.append({'name': name, 'command': command, 'returncode': result.returncode,
                         'elapsed_seconds': time.monotonic()-start})
        if result.returncode:
            raise RuntimeError(f'{name} failed; read {out/(name+".log")}')
    for target, flags, name in [(ordinary, [], 'normal'), (optimized, ['-O'], 'optimized')]:
        run([sys.executable, *flags, str(root/'verify.py'), '--out', str(target),
             '--bound', str(args.bound), '--square-bound', str(args.square_bound),
             '--prefix-bound', str(args.prefix_bound)], name+'_main')
        run([sys.executable, *flags, str(root/'check_prime_square_fixed_sum.py'),
             '--input', str(target/'prime_squares.json'),
             '--out', str(target/'prime_square_fixed_sum.json')],
            name+'_prime_square_fixed_sum')
        run([sys.executable, *flags, str(root/'check_independent.py'), '--input', str(target),
             '--out', str(target/'independent.json')], name+'_separate')
    hashes = {}
    for name in FILES:
        a, b = (ordinary/name).read_bytes(), (optimized/name).read_bytes()
        if a != b:
            raise RuntimeError(f'ordinary/optimized mathematical output differs: {name}')
        hashes[name] = hashlib.sha256(a).hexdigest()
    receipt = {'python': sys.version, 'platform': platform.platform(), 'commands': commands,
               'mathematical_files': hashes, 'normal_optimized_identical': True,
               'main': json.loads((ordinary/'summary.json').read_bytes()),
               'separate': json.loads((ordinary/'independent.json').read_bytes()),
               'universal_ES_proved': False, 'independent_human_review': False}
    (out/'execution_receipt.json').write_bytes((json.dumps(receipt, indent=2, sort_keys=True)+'\n').encode('utf-8'))
    print(json.dumps({'main_checks': receipt['main']['checks'],
                      'separate_checks': receipt['separate']['checks'],
                      'mathematical_files_compared': len(FILES),
                      'normal_optimized_identical': True}, indent=2))

if __name__ == '__main__':
    main()
