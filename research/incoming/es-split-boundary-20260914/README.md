# Prime-power SplitZero comparison and canonical ES moment bounds

**The Clankers — 14 September 2026.** Additive research continuation. No universal Erdős–Straus or RH claim.

## What changed

The last local integration used source `7ea0a49945390eae14d3160a5730858899768b5f`. This contribution reads current Zeta main `35b7aeaff0b63b0db71f26c5b921cdbbec2507fb` and the separate unmerged PR30 proof at `f57532b97c5c92a8c197e6cd4fef2b36b2d33e97`. It applies the support-changing quotient, original-metric secants, and explicit boundary-kernel comparison to the ES system. It does not claim a reading of all 821 pages or a new replay of the imported Lean/CI evidence.

**Sources:** `core.tex` is the complete integration module; `workbench.tex` builds it. `preprint.tex` is a self-contained three-page research note. `card.tex` is a one-page summary, not a proof. `source_reading.json` pins every source and its read scope. `morphisms.json` gives the maps, inverses and information-loss statements.

## Exact mathematical results

1. Each original labelled divisor state has a multivariate truncated-polynomial module with one variable for every relevant prime. Its joint socle always retains a supported line. The comparison of that line with the ordinary augmentation is exactly the original success projector. The prime-wise degree, not the mere existence of a socle line, distinguishes failure.
2. Modulus reduction and the reverse socle-preserving embedding are different maps. Both are explicit. Their coefficient-action defect is retained.
3. The old residue cohomology and the original-state projector have different dimensions. Their common pair-space span and a canonical mass-preserving comparison are calculated. At `(p,a,R)=(2521,636,23)` the dimensions are 5 matched pairs, 4 residue classes, 3 arithmetic states. The actual transported Gram has off-diagonal entries `3/8`; labels do not erase those pairings.
4. The original return-denominator measure has a proved gap `(0,1/3] union {1}`. Its canonical upper Christoffel bound and signed lower bound are computed with exact normal equations, including every singular correction kernel. They provide `L_d <= H <= U_d`, where H is the count of original canonical states, not split occurrences. Complete split-fibre weights commute with every moment and bound.
5. The exact relation-norm secants prove monotonicity. A Chebyshev competitor gives a finite stopping degree logarithmic in the original mass; it does not give a faster method for calculating the arithmetic moments. Four integer gcd moments give the exact first-degree positivity test.

The generic boundary comparison and upper Christoffel variational principle are inherited. The particular ES application, its comparison maps, signed lower counterpart, and certificates are derived here. A scoped content search did not establish an exact earlier application; that is not a historical-priority claim.

## Reproduce

Python 3.9 or later, standard library only:

```sh
python verify.py --bound 1500 --out generated
python -O verify.py --bound 1500 --out generated_optimized
python screen_degree_one.py --bound 50000 --out degree_one_screen.json
```

The first checker treats every actual prime exponent and both canonical channels. All checks remain active under `-O`. It also tests singular measures, the boundary module and reductions, split-fibre weights, the old/new cohomology comparison, and six deliberately false inputs.

The independently implemented integer screen tests a **finite converse**: whether a shell with an actual hit can nevertheless fail the degree-one sufficient test. This is not an ES coverage algorithm or a proof that degree one always suffices.

For TeX:

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error card.tex
pdftoppm -singlefile -png -r 180 card.pdf card
```

## Recorded finite outcomes

The main verifier executed 2,787,464 explicit conditions, including six rejected false controls. All 9,531 first-half shells of 54 primes `p=1 mod12`, `p<=1500`, contain 412,838 original canonical candidates and 1,920 hits in 685 shells. Four moments determine 9,530 exact counts. At `(1093,280,27)`, degree two gives the remaining exact count six.

The separate screen through `p<=50000` inspected 7,508,973 shells, 658,782,438 original candidates, and 56,756 occupied shells. No occupied shell failed the degree-one lower test in that finite range. Both Python modes produce identical output. The generic positive measure `delta_1+10000 delta_(1/5)+10000 delta_(1/7)` has lower bound `-8189/1811` despite positive endpoint mass: degree-one adequacy is not a consequence of the gap alone. A universal arithmetic theorem about these actual divisor measures remains unproved.

`verification.json` and the JSON certificates record actual execution scopes. Counts of tests are not counts of theorems. Several runs of one implementation are not independent mathematical review. The extra screen is a separate implementation of its limited integer criterion, not a reviewer.

## Preserved distinctions

- Supported zero versus external absence.
- Original ES states versus split occurrences versus residue-cohomology classes.
- Individual prime-power defects versus their product D.
- Joint socle versus ordinary augmentation and their comparison.
- Counting norm versus transported quotient norm; all cross terms retained.
- Exact rational normal equations versus an assumed inverse of a singular Gram.
- Arithmetic moments computed here versus analytic theta integrals in the source programme.
- A fixed finite count certificate versus uniform positive occupancy for all primes.

No earlier source, publication, branch, workflow or dependency pin needs modification. Source-module licensing remains unchanged; new text/metadata use CC0 and the new standalone software uses MIT (see LICENSE.md). The byline is the collective `The Clankers`, with attribution to the existing bounded-divisor programme and the source SplitZero contributions in the proof.
