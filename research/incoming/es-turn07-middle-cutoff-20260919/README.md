# Turn 7: sharp square-root middle atlas

This tranche proves structural results for the original first-half middle
channel of the Erdős--Straus equation.  It does **not** prove universal
occupancy and does not claim an Erdős--Straus proof.

For an oriented middle state, retain

```
p/4 < a < p/2,  R = 4a-p,  u | a^2,  R | u+a,  u<a,
(h,r,s) = (gcd(a,u)^2/u, u/gcd(a,u), a/gcd(a,u)),
lambda = (r+s)/R,  j = h*r*lambda,  Q = 4j-1,  A = h*lambda^2.
```

The exact identity

```
p = R*Q - (Q+1)^2/(4A)
```

gives the following theorems.

- For every prime `p ≡ 1 (mod 8)`, with `t=min(R,Q)`,
  `4p >= 3t^2+6t-25`.  Equivalently
  `t <= 4 floor(sqrt((p+7)/12))-1`.  Equality is attained at `p=41`.
- On the six hard classes
  `{1,121,169,289,361,529} (mod 840)`,
  `4p >= 3t^2+14t-81`.  Equivalently
  `t <= B(p)=4 floor((sqrt(3p+73)-2)/6)-1`.  Equality forces the exact
  family in `core.tex` and is attained at `p=1801`.
- These bounds produce a complete disjoint two-chart atlas.  The direct chart
  enumerates the original residuals `R<=B(p)`.  The cofactor chart enumerates
  `j<=K(p)`, `u|j^2`, and `4j-1 | p+4u`, then reconstructs every original
  coordinate by the explicit inverse in equation (10).
- A fixed-grade obstruction proves that for every constant `B` there are
  infinitely many hard primes with no exterior state of grade `h<=B` and no
  oriented middle state of grade `j<=B`.  The same primes have explicit
  endpoint solutions, so this is an obstruction to that bounded inventory,
  not a proposed counterexample.

The example at `p=2521` proves why a small cofactor is not a small original
shell: its cofactor chart returns an original state although the original
residual-47 shell is empty in both channels.  The exact inverse, rather than a
shell identification, is the morphism between the two presentations.

## Read and reproduce

- `output/pdf/workbench.pdf`: readable paper.
- `workbench.tex`, `core.tex`, `references.tex`: complete TeX source.
- `MORPHISMS.md`: domains, codomains, inverses, fibres, exceptional loci and
  information retained by every map.
- `certificates/`: bounded scan, examples, fixed-grade prime certificate,
  execution summary and independent-check receipt.
- `source_reading.json` and `source_receipt.json`: literature and supplied-file
  identities.
- `ATTEMPTS.md` and `HANDOFF_TURN_7_REMAINDER.md`: what succeeded, what failed,
  and the exact remaining theorem.

From this directory:

```sh
python verify.py --bound 3000 --grade-budget 50 --out certificates
python -O verify.py --bound 3000 --grade-budget 50 --out reproduced_optimized
python check_independent.py --input certificates --out certificates/independent.json
python -O check_independent.py --input certificates --out reproduced_independent.json
pdflatex -halt-on-error -output-directory=output/pdf workbench.tex
pdflatex -halt-on-error -output-directory=output/pdf workbench.tex
```

The two Python implementations do not prove universal occupancy.  They replay
the declared bounded atlas and the supplied fixed-grade certificate.  No Lean
build or independent human review is claimed.
