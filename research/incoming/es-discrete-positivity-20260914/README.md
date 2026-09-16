# Discrete-spectrum positivity after uniform ES-array control

**The Clankers — 14 September 2026.** This is a complete current research tranche, not a copy of the whole historical workbench. All new code is standard-library Python. No universal Erdős–Straus or RH result is asserted.

## What is proved

The original return denominator is an odd positive integer. Keeping its exact reciprocal spectrum gives explicit one-sided Lagrange filters

`Phi_j(x) = x product_(nu=1..j) (((2nu+1)x-1)/(2nu))`.

Odd j bounds the success indicator below; even j bounds it above. The error is at most `1/(2^j j! (2j+3))`, while the absolute coefficient sum is only `j+1`. A finite rational window gives the sharp error. Combining this with the proved original row-mass bound gives simultaneous unscaled lower and upper counts for every canonical row defined here, for primes `p = 1 mod 4`, with maximum moment degree asymptotic to `log p / log log p`. All infinite operators retain their maximal domains and all relative traces their convergence domains. This is a certificate-degree improvement, not a faster moment-computation theorem or proof of positive occupancy for every such prime.

The lower inequalities are applied to an actual prime `p=19748674681=1 mod840`. Its shell `R=135`, `a=4937168704=2^6*13^4*37*73` contains exactly one original hit, but its optimal aggregate first-degree signed moment form is negative definite. This disproves a possible universal converse suggested by the old finite screen; the earlier sufficient theorem remains valid. Keeping the E channel restores a positive first-degree certificate. Alternatively, the fixed discrete quartic gives a positive sum on the full original shell and, with its degree-five upper partner, certifies the exact count one.

A second certified hard prime, `2671180768668258904496300170662649=289 mod840`, has a shell with three hits but negative first-degree maxima even on each channel separately. The same quartic is positive there. Neither example is claimed least. Neither is a counterexample to ES. No universal adequacy of the quartic is inferred.

The first witness also yields an explicit all-integer progression `n=19748674681+255650653440 j`, j>=0, entirely in class 1 mod840. All its denominators and the nonprimitive-to-canonical inverse are given. Coprimality and Dirichlet's theorem imply infinitely many prime members, without requiring a second auxiliary prime. This is an explicit specialization of the inherited selector, not a new general progression method.

## Read and reproduce

- `workbench.pdf` / `workbench.tex` / `core.tex`: complete seven-page proof and integration.
- `preprint_filters.pdf` / `.tex`: standalone three-page filter proof.
- `preprint_hard_shell.pdf` / `.tex`: standalone three-page arithmetic obstruction and positive repair.
- `card.pdf`, `card.png`: one-page summary, not a substitute for either proof.
- `verify.py`, `prime_proof.json`: complete executable certificate sources.
- `certificates/`: exact regenerated outputs.
- `morphisms.json`, `MORPHISMS.md`: domains, inverses, fibres and explicit information loss.
- `lean_plan.md`: proposed dependency obligations; not a Lean build.
- `source_reading.json`, `novelty_review.json`: source pins, actual reading scopes and attribution boundaries.

Run from this directory with Python 3.9 or later:

```sh
python verify.py --bound 1500 --out generated
python -O verify.py --bound 1500 --out generated_optimized
```

The supplied JSON prime-proof DAG must remain beside the script. No network, SymPy, numerical eigensolver, primality library, or unprovided prior implementation is imported. Python big integers and exact `Fraction` arithmetic are used. JSON integers can exceed JavaScript's exact-number range.

Build the documents with a standard TeX installation:

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint_filters.tex
pdflatex -halt-on-error preprint_filters.tex
pdflatex -halt-on-error preprint_hard_shell.tex
pdflatex -halt-on-error preprint_hard_shell.tex
pdflatex -halt-on-error card.tex
pdftoppm -singlefile -png -r 180 card.pdf card
```

## Finite scopes

The verifier checks 54 primes p=1 mod12 through 1500, all 9,531 first-half shells, 412,838 original E/M candidates, and all 1,920 hits and row-count brackets. These repeat a prior finite domain; they are not new prime coverage.

Both large-example shells are exhausted by direct integer divisors and independently by finite group-algebra multiplication. The first shell's 2,106 labels and inverse denominators are serialized. The second shell has 9,702 candidates; its histogram, residue-product certificate, and all three hits are serialized. The entire prime rows at these large primes are **not** enumerated.

Primality of the first example is checked by a full p-1 order certificate and independent complete trial division through 140529. The second uses an eight-node recursive full-order certificate reducing to trial-prime leaves below 10000. Neither test is probabilistic. General interpolation signs and infinite error bounds have written proofs; bounded scalar tests are corroboration of those formulas.

The progression is proved symbolically for all j>=0. Executed examples include nonprimitive cases and j=10^12. Filters, source-resolved forms, exact split fibres, moment-error intervals, and seven deliberately incorrect inputs are checked. See `verification.json` for actual executions rather than inferring success from these instructions.

## Integration and nonclaims

The mathematical target is unchanged: force a positive one-sided moment sum in at least one complete original row for every relevant prime. The current proof gives a uniform way to recover the integer count and explicit positive examples, not that final universal lower bound.

Support labels, both E/M channels, all prime-exponent multiplicities, source weights, ordered denominator inverses, and the polynomial functional-calculus kernel term are retained. Since `Phi_j(0)=0`, the new filters commute with the actual split isometric compression without adding a relation-sector identity. Raw repeated diagonal traces still have the wrong multiplicities and are not used.

ES PR6 remains the direct open-draft antecedent at `f234ed0c34100c39e52c6a4645793823e830a983`. The corrected source, complete certificates and readable documents are published additively on branch `research/es-discrete-positivity-20260914`; `main`, PR6 and every other research branch remain unchanged.

The generic interpolation and variational principles are classical and cited. A scoped content search did not establish an exact antecedent for the combined application; that is not a historical-priority determination. Several executions of this implementation are not independent mathematical review. No Lean compilation is claimed.
