# Actual SplitZero mixed-support cohomology

The Clankers — 14 September 2026. Additive draft research, not a replacement for an existing branch.

This contribution returns to the original SplitZero support diagram, its actual incoming relation modules and its internal cohomology. It is **not** a re-description of the preceding three-feature signed Gram test.

## The two self-contained preprints

`preprint_mixed.tex` proves a genuine three-support class on the nine original divisors of `118^2`, with actual residue kernels modulo `3,7,11` in the ES shell `(p,a,R)=(241,118,231)`. Every pair has zero mixed group; the triple has rank one. The complete integral cycle/primitive coordinates, a pairwise-compatible but globally non-liftable local marginal tuple, and the unchanged original quotient metric are explicit. Squared norms are `8=3+5`. The mixed class is a local-observation gluing obstruction, **not an ES witness count**.

`preprint_resolution.tex` gives the separate exact arithmetic target map, every prime-power support intersection, the full higher differential, and the original split-occurrence relation double complex. The cohomology counts original divisor/channel states, not duplicate occurrences. Its Green and contracting homotopy norms are at most one, independent of the number of tests and split lifts. It includes the actual cochain map to the prime-jet boundary comparison, its failure cone, and a Hilbert direct-sum completion with an absolutely justified compressed arithmetic supertrace.

Both notes have complete proofs in three pages. General intersection-complex and Koszul constructions are classical and attributed. The exact arithmetic application and comparison calculations are offered for review; no historical-priority claim is made.

## Explicit distinctions

- Actual residue-sum kernels can be nondistributive and yield nonzero higher mixed cohomology.
- Actual coordinate **failure ideals**, formed by pulling back target deltas and pointwise multiplication on the same divisor, have a distributive coordinate resolution. These are different modules; their cohomologies are not declared isomorphic.
- Pair-truncated arithmetic complexes may retain false top classes. The full higher primitive kills them. At `(1129,396,455)` all three pairs of local exterior tests have witnesses, but no common divisor passes all three. Full dimensions are `(150,378,313,85)` and the exact hit count is zero. This is not failure at prime 1129: another shell supplies a marked witness.
- At `(2689,781,435)`, dimensions `(18,36,24,5)` leave exactly one actual canonical hit `(781,4828,142807412)`.
- Fibrewise canonical contractions need not be natural in support. Their exact defect `K_ST`, its coherence identity, and its original primitive norm are kept.
- The prime-jet transition is an injective module map, generally not a unital algebra map and not the reverse truncation.
- Support labels remain paired with Hilbert amplitudes. Zero amplitude is not external absence.
- Ordinary raw trace, harmonic compression, and supertrace are different operations. Merely changing the inner product does not change ordinary trace.

## Reproduce this public subset

Python 3.10+, standard library only:

```sh
python check_core.py --bound 1500 --out public_checks.json
python -O check_core.py --bound 1500 --out public_checks_optimized.json
pdflatex -halt-on-error preprint_mixed.tex
pdflatex -halt-on-error preprint_mixed.tex
pdflatex -halt-on-error preprint_resolution.tex
pdflatex -halt-on-error preprint_resolution.tex
```

The compact public checker executes 428,412 exact conditions: the genuine arithmetic kernels and cycle coordinates, original metric, non-gluable marginal tuple, integral and averaged local contractions, all stated arithmetic examples and the complete finite scan. Its normal and optimized JSON agree. The scan has 54 primes `p=1 mod12` through 1500, 9531 first-half shells, 412838 original states, 1920 hits in 685 occupied shells, and 8846 empty shells.

A **separate larger local package** contains the eight-page integration TeX, `verify.py`, seven detailed certificate files, 24 typed-map records, a 45-obligation Lean-ready plan, full split/jet/total-Laplacian checks and six rejected false inputs. Its checker executes 507,774 conditions. The larger checker is not contained in this curated PR and is not what `check_core.py` claims to reproduce. These counts overlap; they are not independent mathematical review. The public mathematical arguments are the two self-contained notes above, not a claim that finite checks prove their universal algebraic identities.

## Source and remaining problem

The actual source pin and read scopes are in `source_reading.json`. In particular the generic SplitZero reconstruction/internal-homology proof is used; no complete current source-volume or Lean/CI audit is claimed. The source's original analytic Gamma norm and period observation are not identified with these finite arithmetic norms.

The complete coordinate resolution has nonzero arithmetic `H0` precisely when an original state passes all local tests. A lower bound forcing this for every required prime remains unproved. Neither a nonzero local mixed-observation class nor higher exactness of the coordinate resolution is silently substituted for it.

No ES/RH proof, new prime-coverage record, independent review, Lean build or external publication is claimed. No earlier artifact is modified or re-licensed. Byline and contribution provenance follow the repository's CONTRIBUTING.md.
