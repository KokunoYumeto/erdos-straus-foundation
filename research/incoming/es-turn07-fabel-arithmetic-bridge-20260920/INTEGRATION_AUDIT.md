# Integration audit and retained corrections

The 30 files listed in `MANIFEST.json` are a byte-preserved incoming packet.
This file is an integrating audit and is not an upstream manifest entry.

## Identity and replay

- Outer cumulative ZIP SHA-256:
  `f32b6e1c4d694fdbf2a925b20af67b112e1de188eddfcc1736534709db917858`.
- Incoming `core.tex` SHA-256:
  `ac1270fcdf747137ad74d6c2c6e3cabd406d1fd8cec878e5e38be248e890f853`.
- All 30 manifest entries were rehashed after a fresh extraction: zero
  mismatches.
- Fresh main replay through 3,000: 211 primes, 1,877,004 divisor vectors,
  5,700 E states, 5,268 oriented M states, 180,267 checks; passed.
- Fresh optimized replay produced identical totals and certificate hashes.
- Fresh independent implementation: 243,374 checks; passed.
- Whole-polynomial Gaussian-integer certificate: incidence, resultant, factor
  product, and constant Jacobian `-2`; passed.

Program replay is a certificate, not an independent proof.  Two independent
coordinate-level proof reviews were therefore requested for the local-algebra
and negative-square-transfer blocks.

## Correction A — M special-fibre wording

The sentence in `core.tex` beginning “For M, all three roots and all derivative
values are units or zero with distinct reductions” is too strong if “distinct
reductions” modifies the derivative values.  The correct statement is:

> For M, the three roots have distinct reductions; every derivative value is
> a unit.  The derivative residues need not be pairwise distinct.

Counterexample: at the original M state
`p=5`, `(a,u,R,h,r,s,lambda,H)=(2,1,3,1,1,2,1,2)`, the reduced roots are
`(0,3,1)` but the derivative residues are `(3,1,3)`.  This correction does not
alter the seven geometric special-fibre points or the count of three
`F_p`-rational points.

## Correction B — alpha inverse-fibre gate

The alpha-branch paragraph in `core.tex` does not list every test required for
its claimed “full fibre.”  Starting from

```text
N=(p+4c^2)/h,
s | N,
k=N/s,
r=(s+k)/4,
a=hrs,
u=hr^2,
R=4a-p=hs^2+4c^2,
```

divisibility, parity, coprimality, and first-half range are not sufficient.
One must also retain the original E gate

```text
R | 4u+1,
```

equivalently `R | pr+s`.  For `p=5209,h=95,c=2`, the uncorrected list admits
`s=5,k=11,r=4`, hence `(a,u,R)=(1900,1520,2391)`, but
`4u+1=6081` is not divisible by `2391`.  The supplied `verify.py` does apply
the missing gate at lines 270–276; the defect is in the written theorem, not
in the enumerated certificate.  The forward negative-four-square transfer
theorem is unaffected.

## Scope retained

- The local fibre theorem concerns the reciprocal-cubic seven-state boundary
  map, not the normalized four-finite-root eight-state map.
- The ramified/unramified comparison concerns two different arithmetic target
  cubics at the same prime; it is not an isomorphism of unchanged fibres.
- The integral root-order conductor is not the fixed complex weighted analytic
  conductor.
- The transfer theorem starts from an actual E state and does not supply the
  missing first state at every prescribed prime.
- No universal Erdős–Straus assertion, p-adic descent of the complex period
  matrix, or Lean completion is claimed.

## Correction C — branch-collision scope

The equation `c1*c2=j` classifies collisions of the selected alpha and beta
words only after the full targets are compared.  Equality of full targets first
recovers

```text
Q = 4*h_M*r_M*lambda_M - 1 = h.
```

Thus both branches have the same `h` and the same `j=(h+1)/4`; on that fixed
source cofactor, `U_alpha=c1^2` and `U_beta=(j/c2)^2` coincide exactly when
`c1*c2=j`.  Equality of the number `U` across unrelated values of `h` is not
the asserted collision.

## Correction D — meaning of “entire lines”

The transfer has no size cutoff when `c=1`.  Therefore every already-existing
original E state on `alpha=-4` or `beta=-4` has an original same-prime M
return.  This does not establish that either line contains infinitely many
source states, that the line is unboundedly occupied, or that every prescribed
prime supplies a source state on it.  The corrected sources use this exact
scope.

## Corrected public build

The received 30-file packet, including its PDFs, remains unchanged and
manifest-verifiable.  Corrected editable sources are in `corrected/`; they
repair A–D without rewriting the received objects.  The public reading path
must use the corrected PDFs generated from those sources.

## New theorem proved during integration

The two selected negative-square words are not the full return mechanism. If
an existing E state has (h\equiv3\pmod4) and (j=(h+1)/4), the complete set

```text
U_{p,h} = {U > 0 : U | j^2 and h | p+4U}
```

is in bijection with every original M state at the same prime whose normalized
cofactor is (Q=h). The forward map and its exact inverse, primitive
normalization, ordered denominators, negative-square residue slices, overlaps
and empty-fibre criterion are proved in `corrected/fixed_cofactor_atlas.tex`.
The new checker `verify_integration_extensions.py` compares the constructed set
with every recorded M state in the byte-preserved scan. It derives 1,293
eligible E-source incidences, 933 source-target incidences, and 511 distinct
fixed-(Q) targets; it also verifies the strict (p=41161) return and the
genuinely empty (p=3049) fibre with Lucas primality certificates.

Composed with the already proved diagonal and radius-eight returns, this shows
that every remaining occupied exterior source has shape radius at least nine.
It still starts from an occupied E state and is not a universal occupancy
theorem.
