# Reproduce this continuation

Use Python 3.10 or newer. The commands below use only its standard library;
they neither install dependencies nor contact services. Run them from this
directory. Each `--out` is a new output location, so the supplied certificates
remain unchanged.

```sh
python reconstructed/character_energy_check.py --out replay/energy --scan-bound 1500
python received/es_dual_frontier/dual_es.py --self-test --out replay/dual
python received/es_s6_counterfactual/verify.py --out replay/s6
python reconstructed/boolean_exact_checks.py
python verify_continuation.py
```

For assertion-removal checks, repeat the first three commands with `python -O`
and a different output directory. Those checkers use explicit exceptions for
their mathematical tests. The independent Boolean regression script uses
ordinary assertions and is intended to run without `-O`.

The committed `checks/energy`, `checks/dual`, and `checks/s6` were generated
from this repository copy. Their totals respectively are 4,194,527,
1,033,275, and 2,232,577 checks at the scopes stated in those receipts.
Counts are individual program checks, not counts of independent theorems,
reviewers or new discoveries. The character scan is exactly 54 primes
congruent to one modulo 12 up to 1,500, with 9,531 first-half shells.
It certifies 214/231/240 shells under the unpartitioned/Jacobi/all-local-
quadratic tests. These are not counts of exceptional primes.

The geometry intake receipt records separate independent sorted-denominator
enumeration at primes 5, 13, 37 and 97, ten malformed-certificate rejections,
and comparisons of 28 supplied mathematical certificates in ordinary and
optimized execution. The original compatibility helper is supported by a
byte-identical alignment-file copy described in PROVENANCE.md.

Build the new reader from its source directory, with a standard LaTeX
installation:

```sh
cd reconstructed
pdflatex -interaction=nonstopmode -halt-on-error continuation.tex
pdflatex -interaction=nonstopmode -halt-on-error continuation.tex
```

The committed readable version is `output/pdf/continuation.pdf`. LaTeX build
logs and rendered inspection pages are not public mathematical sources.
The original package PDFs remain under `received/` at their original names.

The complete written proofs, finite exact calculations and formal proofs
have different scopes. No new Lean run or whole-programme formalization is
claimed. A successful finite checker does not validate an untested analytic
step; the branch-cover correction is an explicit example of why both the
proof and the computation matter.
