#!/usr/bin/env python3
"""Rebuild the Markdown and typeset PDF; no mathematical input is changed."""
from pathlib import Path
import argparse
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-dir', type=Path)
    args = parser.parse_args()
    for executable in ('pandoc', 'pdflatex'):
        if not shutil.which(executable):
            raise SystemExit(f'Required executable not found: {executable}')
    inputs = [ROOT / 'INTRODUCTION.md', *sorted((ROOT / 'proofs').glob('*.md')), ROOT / 'REFERENCES.md']
    text = '\n\n\\newpage\n\n'.join(p.read_text(encoding='utf-8').strip().removesuffix('\\newpage').strip() for p in inputs) + '\n'
    (ROOT / 'RESEARCH_CONTINUATION.md').write_text(text, encoding='utf-8')
    subprocess.run([
        'pandoc', str(ROOT / 'RESEARCH_CONTINUATION.md'),
        '-f', 'markdown+tex_math_single_backslash+tex_math_dollars',
        '-s', '-t', 'latex', '--toc', '--toc-depth=2',
        '-V', 'geometry:margin=24mm', '-V', 'fontsize=11pt',
        '-V', 'title=General-family integration for the ES--RH programme',
        '-V', 'subtitle=Canonical metrics, complete mixed minima, ES tensor actions, and collision scales',
        '-V', 'date=20 September 2026',
        '-H', str(ROOT / 'header.tex'), '-o', str(ROOT / 'MANUSCRIPT.tex')
    ], check=True, cwd=ROOT)
    tex = (ROOT / 'MANUSCRIPT.tex').read_text(encoding='utf-8')
    # Pandoc's inline-code rendering does not break long repository paths.
    # Render only those literal paths using xurl's line-breakable \path.
    def wrap_path(match: re.Match[str]) -> str:
        literal = match.group(1)
        if '/' in literal and len(literal) > 65:
            return r'\path{' + literal.replace('\\_', '_').replace('\n', '') + '}'
        return match.group(0)
    tex = re.sub(r'\\texttt\{([^{}]+)\}', wrap_path, tex, flags=re.DOTALL)
    if '\ufffd' in tex:
        raise RuntimeError('Unexpected replacement character in generated TeX')
    (ROOT / 'MANUSCRIPT.tex').write_text(tex, encoding='utf-8')
    build_dir = args.build_dir or Path(tempfile.mkdtemp(prefix='es_rh_family_pdf_'))
    build_dir.mkdir(parents=True, exist_ok=True)
    for run in range(1, 4):
        with (build_dir / f'latex_run_{run}.log').open('w', encoding='utf-8') as log:
            subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            f'-output-directory={build_dir}', str(ROOT / 'MANUSCRIPT.tex')],
                           stdout=log, stderr=subprocess.STDOUT, check=True, cwd=ROOT)
    shutil.copy2(build_dir / 'MANUSCRIPT.pdf', ROOT / 'MANUSCRIPT.pdf')
    (ROOT / 'results').mkdir(exist_ok=True)
    shutil.copy2(build_dir / 'latex_run_3.log', ROOT / 'results' / 'latex_final.log')
    print(ROOT / 'MANUSCRIPT.pdf')
    print(f'Build logs: {build_dir}')

if __name__ == '__main__':
    main()
