# Ternary mixed-support ES certificate

The Clankers — 14 September 2026. Additive research continuation; no universal ES or RH claim.

## Result

On the original 9702-state shell at the previously certified prime
`2671180768668258904496300170662649`, `R=135`, use the three functions
`1`, `x*1_E`, `x*1_(beta_457>0)` with `x=1/D` and the actual return denominator
`D=R/gcd(R,g)`. All three two-coordinate signed forms are negative definite.
The full three-coordinate form has inertia `(1,2,0)`. The explicit combination
`(-1+36*x*1_E+36*x*1_(beta_457>0))/71` has signed value
`607462/1890375 > 0` and hence forces an original integral witness.

The third component is an overlapping support on the original divisor states;
there are still only the two original arithmetic channels E and M. The comparison
is with pairs of these specified components, not every possible reparametrization
by two freely designed functions. This is a new certificate in an inherited shell,
not a newly discovered prime or new numerical prime coverage.

## Exact interfaces

`core.tex` is the seven-page workbench's integration body; `preprint.tex` is the
three-page standalone proof note; `card.tex` is a one-page summary.

The general signed-form theorem gives `n_+(J) <= H` and a numerical count lower
bound from a pointwise successful-pattern amplitude bound. Its Schur coordinate
change and inverse retain the complete cross term and ordinary source metric.

The finite dictionaries extend to arbitrary growing mixed spaces with the
factorial filter error measured against their actual source Gram. Filtering
before compression is essential. Two actual failed states at `(37,18,35)`
give `A*Phi_3(X)A=0` but `Phi_3(A*XA)=17/343000>0` on their normalized constant
line. The exact missing squared-norm correction is supplied.

A budget split is a finite-fibre map of the original exponent vectors, not a
new independent source. Both mixed Grams return exactly with inverse-fibre
weights. The checked split has 44550 occurrences, original mass 9702, seven
raw hit occurrences and three original hits. Its support condition is evaluated
on the full returned beta, never on one partial summand.

## Reproduce

Python 3.9 or later; standard library only, no network:

```sh
python verify.py --bound 1500 --out generated
python -O verify.py --bound 1500 --out generated_optimized
```

Keep `prime_certificate.json` beside the script. The inherited complete-order
primality certificate is replayed by new code (eight internal nodes, fifteen
trial-division primes). No probabilistic primality result is relied upon.

`certificates/original_states.json.gz` retains the common factorization and all
9702 full original rational reconstructions, including beta, u, E/M, R, D,
h,r,s, quotient and ordered denominators. Fractions are exact numerator/denominator
objects. `hard_ternary.json` includes all three integer witnesses, the mixed
matrices, every principal determinant, a signed Schur inverse and the full
compression-defect matrix.

The small scan covers 54 primes p=1 mod12 through 1500, 9531 first-half shells,
412838 original states and 20177 support choices. It certifies the 685 occupied
shells and has no false positives. No ternary-only choice occurs in that small
range; the fixed large example is the strict one. It is not claimed least.

Additional exact fixtures check 729 symmetric integer forms, 256 overlapping
source dictionaries at five filter degrees, and six deliberately false inputs.
Checks remain active under `python -O`. Repeated modes are implementation
replays, not independent mathematical review.

## Exact bridge to the native support complex

This scalar theorem is not an identification with the native mixed-support
cohomology of PR #7.  Its typed comparison is

```text
R^3 --A--> R^Omega --Pi--> H^0_arithmetic,
```

followed by the already defined top insertion `s` and augmentation `epsilon`,
for which `epsilon s A = Pi A`.  Thus the receiving comparison is through the
arithmetic successful-state space.  Neither `J`, its positive
eigenspace, nor the three-support phenomenon is identified with the `H^-1`
local-gluing class in PR #7.

TeX builds:

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error card.tex
pdftoppm -singlefile -r 170 -png card.pdf card
```

## Sources and publication state

The Zeta source is pinned at `d1191f9c2c47d4317c87262eca9e75c8de9ca7ff`.
Actual proof equations JSA12–JSA20 were read, not just their summary.
The source's Gamma measure, analytic bounds and global endpoint claims are not
assumed for the finite ES form. The prior discrete-positivity archive supplies
the hard prime, its factorization and primality proof, and the scalar filters.
Their hashes and read scopes are in `source_reading.json`.

The general localizing-matrix method and Schur algebra are classical, with
primary references in the proof. The scoped search did not establish an earlier
exact ES application; no historical-priority claim is made.

This directory is an additive source tranche under
`research/incoming/es-mixed-support-20260914/`; it does not change earlier
files.  The TeX sources, readable PDF/PNG previews, nine exact certificates,
licence, and publication replay receipt are retained together.  No merge, new
Lean build, or external preprint deposit is recorded here.
