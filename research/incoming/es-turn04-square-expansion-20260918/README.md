# Turn 4: finite reduction of mixed square-source closed sets

**Collective byline:** The Clankers. **Status:** proved structural theorems, including an explicitly finite computer-assisted proof; Erdős–Straus remains unresolved by this work.

For every hard prime p and every set of at most five external nonresidue prime vertices, a valid original source `(p+sigma(q) q t^2)/4`, with `t in {1,3,5,7,9}`, has an actual nonresidue prime factor outside that set. Starting at any vertex, at most 25 source factorizations therefore produce at least six distinct reachable vertices. Both vertex types and every stabilizer quotient are allowed. The conclusion is factor supply, not selector occupancy.

For a square-source-closed set of arbitrary fixed cardinality m, the proved root-prefix bound gives `p < (4H)^m < 16^(m^2)` and an exact finite cycle-cofactor domain. The at-most-five theorem exhausts that domain: 1,381,117,764 rooted profiles before proved pruning, 5,922,259 range-compatible profiles, 1,915 typed integer models, and exactly three surviving prime cycles. Each has a directly verified multiplier-nine exit. No prime-census extrapolation or probable-prime input is used.

An exact integer carry retains the full residual `sigma(q) q t^2`, including overlap of its base and square factors. At p=12889 the canonical mixed pair `43 <-> 61` has both original E/M gates empty at all 22 valid same-vertex square sources, comprising 246 divisor vectors. The factor graph still escapes and a checked path reaches the ordered witness `(3225,1357856150,3789366)`.

## Source and complete portable proof

`preprint.tex` is a standalone four-page proof. Run:

```sh
python cofactor_check.py --out certificates/cofactor_certificate.json
python check_independent.py --input certificates
python verify_examples.py
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

The first enumerator derives affine interval bounds from the exact monotonicity formula. The second independently reconstructs the affine numerators, uses binary-search pruning, exhaustive trial division and literal quadratic residue sets; it imports none of the first implementation. The small example checker independently enumerates every divisor and verifies the ordered positive return. Python optimization is supported; all arithmetic is exact. The hash is a replay identifier, not a substitute for the proved pruning theorem.

The [`full/`](full/README.md) directory now preserves the broader source
tranche: the seven-page workbench proof source, prime-power root counts, mixed
reciprocity tables, exact coefficient fibres, the complete square-source scan
through hard `p<=5000`, both full replay implementations, deterministic
certificates, the 21-map register, attempt ledger, and Turn 5 handoff. The
`discovery/` scan through one million is retained there as exploratory evidence
only. Those additional replay lanes are not falsely attributed to the smaller
portable checker above.

The canonical source and reciprocity antecedents are Bryan's pinned CENTL notes; original Type I/II coordinates are attributed to Elsholtz–Tao; Turn 3 is PR #18. This contribution adds new files only. No least-example assertion, whole-conjecture result, new ES verification range, independent mathematical review, Lean build or historical-priority determination is claimed.
