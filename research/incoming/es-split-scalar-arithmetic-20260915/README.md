# Split-zero inversion and exact arithmetic capacity control

**The Clankers — 15 September 2026.** Research continuation. No universal ES or RH claim.

## What changed

The intended scalar is `G(A) = {tau} disjoint-union A^bullet`, with supported zero `e = 0_A^bullet` distinct from absence. The previous observation-Gram and prime-indexed Koszul constructions were additional constructions, not definitions of that distinction. Their useful exact maps remain valid at their stated scopes; their generic formal properties alone do not force ES occupancy.

This continuation works with the actual positive prime-factor contribution before computing target occupancy. It proves an explicit obstruction to lifting an ordinary group-algebra inverse to the sparse split carrier, then obtains exact all-multiplicity divisor arithmetic and a complete local capacity classification at residual 27.

## Main proved results

- A split coefficient vector is the pair `(presence mask, amplitude vector)`. Its convolution support is the product of the presence masks even when amplitudes cancel. Its global convolution units are exactly unit monomials. Ordinary fixed-fibre linear inverses are a different construction and are not prohibited.
- The old ordinary six-cycle target `[3]+2[1]` and its ordinary inverse multiply in the split carrier to `1[0]+e[2]+e[4]`, not the global identity. The exact saturated identity and all changed masks are retained.
- The positive divisor factors have explicit rational formal generating series and coefficient bijections. For a generator of order `o` and `e = r+ok`, the complete count vector is `P_e=P_r+2k sum_H[h]`. This handles arbitrary integer multiplicities without enumerating the original exponent interval.
- Target availability has a finite cap `floor(o/2)` in each residue class. Actual counts still retain every original prime and every grouped-composition fibre.
- At residual 27 there are exactly **174 coordinatewise minimal profiles**: 9 with one nonidentity residue class, 99 with two, and 66 with three. Every hit has a witness using a reserved capacity of at most nine actual prime occurrences from at most three residue classes. Original surplus factors are retained. The three-class bound is necessary at the prime 19489. The nine-capacity optimum is claimed for the stated local residue-profile model, not for an unspecified least prime.
- A separate hand proof gives the exact two-class thresholds for all multiplicities of primes in residues 1, 7 and 11 modulo 27.
- Fixed-residual Dirichlet series for the actual coefficients have absolutely convergent Euler products on `Re(s)>1`, exact character/L-function factors, and a uniform-in-modulus absolute tail bound. Nonzero global series are not substituted for positive individual coefficients.

## Files and reproduction

`workbench.pdf` / `workbench.tex` / `core.tex` contain the complete proofs, including all domains and nonclaims. `preprint.pdf` / `preprint.tex` give a three-page standalone note. The complete 174-entry list and its actual target words are `certificates/catalogue27.json`.

Python 3.9+, standard library only:

```sh
python verify.py --out reproduced
python -O verify.py --out reproduced_optimized
python check_catalogue.py --catalogue reproduced/catalogue27.json --out frontier.json
python check_dirichlet.py --bound 120 --out dirichlet.json
```

`verify.py` creates the catalogue using cyclic exponent masks, then checks exact counts and reconstructs every selected original witness. `check_catalogue.py` does not import that implementation: it independently uses original unit residues and explores every unoccupied capped profile and its upward frontier. Together with the proved monotonicity and cap, that is the finite certificate for the all-exponent classification. No experimental prime extrapolation is used in that theorem.

`check_dirichlet.py` separately reconstructs the positive formal Euler factors and compares every finite coefficient with direct divisor enumeration. Analytic convergence and tails have written proofs, not a finite numerical substitute.

Build:

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

## Exact finite scopes

The catalogue builder uses all 131,072 squarefree supports plus 14,040 positive capped profiles on the remaining mixed-parity supports. The independent checker visits 62,812 unoccupied capped profiles and 629,841 frontier edges; each of the 567,030 occupied boundary edges is covered by a verified minimal pattern.

The R=27 application covers all 4,519 primes up to 2,000,000 in residues `{1,121,169,289,361,529}` modulo 840. It finds 1,214 occupied residual-27 shells, 1,880 exterior states and 1,800 middle states. This is not new prime coverage, and a miss at this residual is not an ES counterexample.

The independent small-shell count comparison includes all first-half shells at the 44 primes `1 mod4` through 500: 2,480 shells, 80,032 canonical candidates, and 1,043 hits. No Koide chamber restriction is used in this tranche.

Examples retain both the inherited empty shell at `(p,a,R)=(3361,847,27)` and the positive shell at `(23689,5929,27)`. Multiplying `a` by 7 changes the prime from 3361 to 23689. It is not described as a fixed-prime descent.

## What remains open in this route

For a false ES prime, every actual shell must miss. This contribution classifies residual 27 completely, including all possible multiplicities, but does not prove that every prime occupies that residual or one of a universally bounded collection of residuals. Cross-shell arithmetic at the same prime is still required. No new Lean build, independent review, or historical-priority determination is claimed. The prior code and papers are not overwritten; this package is published only as an additive research branch.

## Publication status and licenses

This is an additive research contribution based on repository revision
`63f52c3d7162d2ba0c0d8187e4b1d5369f223ed9`. Publishing its branch does not
assert that it has been merged, independently reviewed, or accepted as a
universal Erdős--Straus theorem. `publication_replay.json` records the fresh
reproduction performed for this public package, while `MANIFEST.json` pins the
published bytes.

The mathematical prose, TeX, data, certificates, rendered documents, and
images are dedicated under CC0 1.0. The three Python verification programs are
licensed under the MIT License. See `LICENSES.md`, `LICENSE-CC0.txt`, and
`LICENSE-MIT.txt`.
