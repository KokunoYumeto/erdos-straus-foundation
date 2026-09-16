# Relative boundary packets and actual divisor lifting

**The Clankers — 16 September 2026.** Additive research continuation of the actual-factor/SplitZero programme. The conjecture is not claimed solved.

## Mathematical contribution

The preceding affine-factor construction sought a packet filling an entire cyclic chart. This continuation uses an actual packet filling a **proper subgroup**, with the correct coset selected in the original lower-exponent coordinates. The lower quotient is not presumed to lift: the high-capacity inequalities and the original word return are proved.

`core.tex` supplies the complete proof. `workbench.tex` builds the seven-page integration note. `preprint.tex` is a self-contained three-page note. `card.tex` is a one-page summary, not a replacement for the proof.

The source boundary map is the actual BR1 comparison from the Zeta workbench, pinned in `source_reading.json`. In characteristic two,

```
A_o = F2[T]/T^o,
N_d = T^(o-d) = sum_(j=0)^(o/d-1) X^(dj),
iota_d : A_d -> ker(T^d),
pi_d iota_d = 0, although iota_d is nonzero.
```

The map is an `F2[X]`-module isomorphism onto its stated image, not a unital algebra isomorphism. Its inverse reads a coefficient in every coset **after checking invariance**. The ordinary quotient adds those coefficients and can kill them. A supported zero retains its presence mask and original integer multiplicity.

The new results are:

1. Complete relative norm maps, inverse fibres, integer multiplicity identities and their subgroup-tower composition.
2. A disjoint mixed-radix decomposition of the actual bounded affine parameter box, followed by exact prefix inequalities forcing a positive original witness. There is no unbounded factor availability or hypothetical subgroup-saturation assumption.
3. A sharp all-multiplicity count when an actual prime `b` with `v2(b-1)=ell` supplies the principal-unit subgroup. The threshold is `2^(k-ell)-1`; the corresponding witness has at most `2^(k-ell)-1+2^(ell-2)` prime occurrences.
4. An explicit family with exactly two target cofactors and minimum occurrence length `2^(k-5)+1`, unbounded in k. The relative criterion succeeds while the preceding full-chart canonical tests and every fixed short-word cutoff eventually fail. General derived p are integers; the supplied 17-digit prime is separately certified.

The generic norm, cyclic-cover and quotient-kernel ingredients are inherited. No historical-priority determination is asserted for their particular combination here.

## Concrete original states

At `(p,k,u)=(8060861761,6,128)`,

```
p+512 = 3 * 17^4 * 53 * 607.
```

The two lower targets modulo16 are 607 and159. Both require two available factors17 modulo64. The complete original cofactor set is `{45951,175423}`. Its two labels cannot be merged merely because their reduced residue observations coincide.

The larger certified prime

```
p=16689143913960961, k=7, u=512,
p+2048 = 3 * 17^8 * 277 * 2879
```

has only the complementary cofactors 240456959 and69405951, with five and six prime occurrences. Thus even a four-occurrence search in either role misses this branch. The relative order-eight certificate supplies it. The prime proof uses a complete factorization of p-1 and exact modular order tests; no trial division of this p to its square root is claimed.

The negative prime example `(p,k,u)=(9331009,6,128)` has lower targets but insufficient high capacity, and that entire branch is empty. A separate explicit middle witness at `(R,u)=(7,857)` is supplied, so this is not a counterexample to ES.

## Fair finite comparison

The complete stated universe has 4519 hard-class primes through2000000, 37289 valid dyadic branches, and4583 original middle states. The new relative class certifies1723 branches on1595 primes. Added to the previous union of canonical affine packets, two-occurrence words, and the3,11 capacity test, it gives3073 branches on2402 primes instead of3071 on2401.

**The stronger baseline matters:** direct words of at most three occurrences already certify3095 branches on2409 primes; their union with the earlier tests certifies all3097 occupied branches on2411 primes in this small range. There is therefore **no coverage gain beyond that stronger union**. The unbounded separation theorem and separately certified large prime establish a different structural advantage. No overall ES coverage or efficient factorization theorem is claimed.

## Reproduce

Python3.9+; standard library only. Keep the `antecedent` directory beside the new verifier.

```sh
python verify.py --bound 2000000 --out regenerated
python -O verify.py --bound 2000000 --out regenerated_optimized
python check_independent.py --input regenerated --out regenerated/independent.json
```

The main script imports the exact predecessor module for the existing arithmetic normalization and baseline definitions. Its checks are counted separately: 203654 new checks and 876325 invocations of antecedent checks. The separate implementation imports neither and performs 167547 checks. Seven deliberately false transformations are rejected. Both scripts test the actual complete rows, not merely the aggregate totals. A separately implemented checker is not independent mathematical review.

Build documents with two `pdflatex -halt-on-error` passes each for `workbench.tex`, `preprint.tex`, and `card.tex`; render with `pdftoppm` or the supplied environment's PDF renderer.

`verification.json` records execution, hashes, render inspection and exact scopes. `morphisms.json` and `MORPHISMS.md` retain the maps. `lean_plan.md` is a dependency plan, not compiled Lean. The final-archive replay receipt is supplied separately to avoid a self-hash cycle.

## Limits

A coarser target alone need not lift. Ordinary projection is not the inverse of the boundary inclusion. Mixing parameter boxes by overlapping convolution changes multiplicities unless the source fibres are retained. The finite search is complete only for the **declared canonical lines and relative strata**, not for all possible affine offsets or all ES solutions.

The remaining pointwise problem is to force a qualifying original lower fibre and its high-layer capacity somewhere among the seeds of each prescribed prime. That cross-seed arithmetic implication is not proved here. No source-wide analytic Gamma identification, new Lean build, independent mathematical review, or conjecture solution is asserted.

## Publication status

The recovered package was first committed byte-for-byte as commit `119dfa6`; this publication revision changes only status prose and adds a replay receipt. It is published additively on branch `research/es-relative-boundary-20260916` under `research/incoming/es-relative-boundary-20260916/`. It does not modify `main`, PR10, or another research branch.
