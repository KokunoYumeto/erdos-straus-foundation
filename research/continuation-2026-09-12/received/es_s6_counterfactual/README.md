# ES denominator defects and the actual (3,4,infinity) period monodromy

This package constructs a complete **decorated affine-torsion cover** from every
candidate in the full Erdős–Straus divisor atlas. It uses the actual four-by-four
period monodromies of the manuscript circulated by Levent Alpöge and identifies
the arithmetic cyclic denominator obstruction with a cohomology class of exact
order D. It proves the full orbit and genus classification for every odd D.

Start with `preprint.pdf` (three pages) for the new finite-system theorems and
`workbench.pdf` for the detailed source reconstruction, ordered atlas, comparison
maps, restricted failure example, filling presentation and limitations.
`card.png` is a one-page posting summary, not a proof substitute.

## Reproduction

Python 3.10 or later, standard library only:

```console
python verify.py --out regenerated
python -O verify.py --out regenerated_optimized
python verify.py --prime 241 --shell 64 --out one_shell
python verify.py --prime 1201 --out full_prime
python verify.py --validate-negative purported_full_negative.json.gz
```

The validator recomputes the complete input atlas and rejects a restricted scope,
any missing or modified row, and any successful candidate. There is no known
full negative certificate in this package. The `241,64` example is a negative
**shell**, while the full atlas at 241 has successful states.

Every finite permutation is specified by three affine formulas. Explicit point
and cycle enumeration was run for D=1,3,5,7,9,15,21,25,27,35,45. Full ordered
arithmetic atlases were generated for p=5,37,241,1201 (50,832 rows in total).
Full permutations are supplied for D<=9. The large covering degrees attached to
all arithmetic rows are derived from the all-level theorem; their individual
sheets are not falsely claimed to have been expanded.

Normal and optimized runs produced byte-identical mathematical certificates.
Exact counts and timings are in `execution_receipt.json`. No Lean build or
independent mathematical review was performed.

## Type and source boundaries

- The rank-four period lattice is `mathbb L`, not the rank-24 Leech lattice.
- The affine residue system is a restriction of **linear** period monodromy to
  gamma=1 modulo D. It is not the affine central-fibre quotient generator.
- A loop permutation is invertible at every D. The older diagonal arithmetic
  operator is invertible only when its retained atlas has no successful row.
- A cover of the punctured base is a complex curve after compactification,
  not the source's compact complex threefold. The specific pullback threefold
  has positive first Betti number when the base component has positive genus.
- The gamma-torsor cocycle is locally trivial on the finite order-3 and order-4
  groups, but has a primitive cusp obstruction. This is proved directly from
  matrices, independently of the global claim that the source is a six-sphere.
- The source's original smooth-sphere conclusion, all analytic period existence
  and all attachment proofs were not independently audited in this turn.
- The complete 174-MB frozen source archive was located but not downloaded.
  Source PDFs were inspected through the web; local downloads failed DNS.
- No GitHub files were changed or merged; no external preprint deposit was made.

The candidate-labelled construction is lossless at the stated fields. Forgetting
its arithmetic labels keeps only the level D; it does not retain the prime,
shell or factor budget. Those forgetful maps are explicitly listed in
`morphisms.json`.

## Build the documents

```console
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
pdflatex -interaction=nonstopmode -halt-on-error preprint.tex
pdflatex -interaction=nonstopmode -halt-on-error card.tex
pdftoppm -singlefile -r 175 -png card.pdf card
```

`src/*.tex` are integration-ready components. `lean_ready_plan.md` is an exact
formalization dependency plan, not a compiled Lean development. Primary-source
roles and the scoped novelty search appear in `source_reading.json` and
`novelty_review.json`.
