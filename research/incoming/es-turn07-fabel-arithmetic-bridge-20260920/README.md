# Turn 7 continuation: the Zeta/Fabel inverse at an original ES prime

Start with `preprint.pdf` (short proof) or `workbench.pdf` (full proof and fibres).
Both have complete editable LaTeX. The source of the original four-dimensional
polynomial is pinned below, not replaced by a similarly shaped map.

## Established

For every original first-half ES state at a prime p = 1 mod 4, its ordered
reciprocal roots p/x_i define the literal Fabel target (0,-4,sigma2,-sigma3).
The complete fibre has seven geometric affine points and exactly three Q_p
rational points. E gives Q_p^3 times two copies of a ramified quadratic field;
M gives Q_p^3 times two copies of the unramified quadratic field. The original
M factor relation forces chi_p(rs)=-1, excluding a fully split local fibre.

The integral E root order has index p in Z_p^3 and consists exactly of tuples
whose first two coordinates agree mod p. Its conductor is (p,p,1). The M order
is Z_p^3. A labelled quadratic root map E -> M requires exactly one p-adic
power in its denominator; its reverse is integral. These are literal formulas,
not an assertion that the seven-point field algebras are isomorphic.

An original negative-four-square shape alpha=-4c^2 or beta=-4c^2 supplies an
original same-prime M state on the exact domain c | (h+1)/4. Both full lines
alpha=-4 and beta=-4 are therefore removed from the residual E-only problem,
with no bound on their other shape coordinate. Source and target factors,
colliding branch labels, and complete inverse fibres remain recorded.

## Source and status

Zeta source:
`KokunoYumeto/zeta-function-research-reader`, revision
`369f6ea9e0312bdf348ca9efd294735efc99c51d`,
`workbenches/splitzero-tandem/continuations/20260920-fable-conductor/FABLE_TO_ORIGINAL_CONDUCTOR.tex`,
blob `f777bb9f1434fa90f2f8bc762860048cc1d32bb4`, GF1-GF11 and FC32-FC35.
The four-dimensional construction is the ES extension. Do not attribute its
four labels to the original three-dimensional Alpöge-Fabel example.

**The universal Turn 7 existence task remains unresolved.** This tranche does
not claim that an initial ES state exists, that every negative-square word is
available, or that the original complex period matrix has a Q_p-model. It does
not advance to Turn 8 under an assumed occupancy statement.

## Reproduction

```
python verify.py --bound 3000 --out certificates
python -O verify.py --bound 3000 --out certificates_optimized
python check_independent.py --input certificates --out certificates/independent.json
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
```

The verifier uses only the Python standard library. It checks all original E/M
states, not only the new successful branch. The separate implementation imports
none of it or any predecessor, enumerates primitive h,r,s directly, and checks
the factor-incidence equations rather than the expanded Fabel polynomial.
See `verification.json` for actual execution outcomes and hashes. Repeated runs
are not independent mathematical reviews. No Lean build is asserted.

The supplied patch adds a new directory; it does not rewrite predecessor claims.
The previous archive is preserved separately in the cumulative handoff when its
exact mounted bytes are available. That preservation is not a renewed audit of
all earlier work.
