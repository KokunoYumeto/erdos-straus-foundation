# Actual-factor socle certificates for Erdős–Straus

The Clankers — 15 September 2026. Additive research contribution, not a universal ES proof.

## Mathematical change

The preceding fixed-p analysis proves prime-factor escape and a sharp capacity theorem using available powers of3. Those factors may still miss the target residue. Here the actual bounded prime contributions form a product in F2[(Z/2^hZ)^*]. An explicit coordinate map identifies this algebra with F2[S,T]/(S^2,T^L); the top element ST^(L-1) has every group coefficient one. A proved binary-prefix criterion constructs an actual bounded product equal to that top element.

The original positive integer divisor polynomial remains present. Mod2 reduction is an observation, not a deletion of used coefficients: an even positive coefficient becomes supported zero, not absence. The selected binary-submask divisor family has a complete inverse and no hidden binomial multiplicities. A residue coefficient one returns an original integer divisor and the full marked middle ES solution. The optional half-turn quotient retains which full-modulus lift is residual and which is cofactor.

The three-page `preprint.tex` contains the complete general proof, the finite capacity criterion, original cofactor and denominator inverses, disjoint-packing count lower bound, and three explicit examples. The general group-algebra strategy is classical (Olson/Petrov), not claimed as a new principle. The application and exact selection criterion are derived in this continuation; priority has not been established.

At p=1794769 the seed32 factorization has exactly one original state, R=207,Q=8671. Both factors require three prime occurrences. The predecessor 3-power capacity test and the two inside-subgroup-only tests fail; the mixed actual-factor product succeeds. The positive polynomial (1+[9])(1+[13])(1+[23]) has each unit modulo16 exactly once.

## Published replay entrypoints

Python3.9 or newer, standard library only. Explicit checks survive optimized execution.

```
python check_examples.py --out examples.json
python -O check_examples.py --out examples_optimized.json
python check_independent.py --bound 2000000 --out comparison.json
python -O check_independent.py --bound 2000000 --out comparison_optimized.json
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

`check_examples.py` performs complete trial primality tests, lists every selected integer divisor word, verifies all parity coefficients and full-modulus factor roles, reconstructs the ordered ES identities, and exhausts the three original seed branches. It is not a universal search.

`check_independent.py` is a separate implementation of the finite comparison: actual unit-group logarithms and parity-aware bounded knapsack, not the first implementation's valuation and prefix test. It enumerates all original cofactor divisors for soundness and the half-turn fibre count. This is a second implementation, not independent mathematical review.

The full local research handoff additionally contains a six-page workbench derivation, the larger `verify.py` structural suite, all generated certificates, rendered PDFs and posting image. Those additional local artifacts are not misrepresented as files in this nine-file public intake. The published preprint is self-contained and the two published scripts reproduce the displayed examples and full comparison.

## Finite scope and nonclaims

All4519 hard-class primes through two million, all37289 valid dyadic branches:4583 original states in3097 occupied branches. The previous capacity criterion certifies964 primes; the new prefix test certifies1194; their union certifies1196. The232 additions concern this sufficient test, not new overall ES coverage. Two predecessor-certified primes remain outside the new test. There is no universal domination or universal capacity theorem.

The unproved arithmetic step is to force a successful capacity in at least one branch of every prescribed prime, or use another actual-factor mechanism for the remaining rows. A nonzero top line assigned after the fact would not prove this. All nilpotents used here come from the original prime residue operators.

No old file, other research branch, workflow or source publication is changed. No new Lean build, historical-priority determination, analytic theta norm identification, fast factoring guarantee, or independent mathematical review is claimed. See SOURCES.md, MORPHISMS.md, results.json and lean_plan.md. New text/metadata use CC0; the new standalone code uses MIT. Cited sources retain their own licences.
