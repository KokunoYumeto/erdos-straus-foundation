# Integration audit

Date: 20 September 2026.

## Identity

- Received SHA-256:
  F97EC18809279C10CAF20A0FFA59ABAA9CF54EC5C5C0AB21761C2840B426D886.
- The received file is preserved without edits under received/.
- The corrected public derivation is separate from that evidence copy.

## Mathematical corrections

1. The chart change at \(p\mid S\) is a quadratic twist. With
   \(c_\lambda=S/(S-4\lambda)\), the map
   \(T_\lambda\mapsto T_0-\lambda\),
   \(\sigma_\lambda\mapsto q\sigma_0\) is defined after adjoining
   \(q^2=c_\lambda\). It descends over \(\mathbb Q_p\) only when the retained
   square class is trivial. Original-algebra Smith conclusions therefore
   keep \(p\nmid S\); the translated chart is not silently substituted.
2. The coefficient-ring quotient in equation (7) is stated as an
   \(R_0\)-module isomorphism.
3. The nilpotent Jordan list in equation (29) is restricted to \(m\ge2\).
   At \(m=1\), \(\sigma^2=u(0)\) is a unit and multiplication by \(\sigma\)
   is invertible.
4. The exterior cofactor is defined before use:
   \(D_E=(4u+1)/R=(r+\kappa)/s\).
5. The supplied sentence saying that execution had timed out is historical.
   The live tree now contains an 80-check exact replay and receipt.

## Direct proof audit

- The normalization map, rank-three inclusion, cokernel and conductor were
  re-derived from the monic equation for \(P\).
- The positive-witness valuation split was checked without reducing by an
  unproved unit: there are one or two \(p\)-divisible denominators and every
  such valuation is exactly one.
- The general Smith formulas were re-derived cluster by cluster. Their
  separated instances agree exactly with the independent integral-completion
  packet: E has index \(p^2\), M has index \(p^9\).
- Both \(p=1201\) witnesses, coefficient reductions, local algebras, Smith
  factors, nilpotent actions and the exterior local square class were checked.
- The rank-\(2+6\) fibre-product sequence follows from
  \((T-P)\cap(g)=((T-P)g)\) after retaining that \(R=g(P)\) is a
  non-zero-divisor on the working base. Its trace determinants and local
  normalization matrix were recalculated.
- The reproducing-kernel minimum, CRT excess, determinant ratio and four
  covariance scales were re-derived in the fixed original metric. No
  \(p\)-adic norm was assigned to that complex metric.
- The supplied local Galois formula was recast as a typed signed-label defect
  representation. Its tame conductor and \(p=1201\) Frobenius polynomial were
  proved from the actual normalized quadratic factors.

## Executable and visual receipts

- verify_defining_prime.py: 80 exact checks, PASS.
- results/verification.json: machine-readable replay.
- tools/generate_20260920_illustrations.py: reproducible figure source.
- figures/integral-normalization-smith.pdf and
  figures/defining-prime-twist-gluing.pdf were inspected against the formulas.
- The readable PDF is built from the corrected source, not the received copy.

## Scope retained

No universal ES occupancy, ES counterexample, zeta zero, RH theorem, or
identity between a finite integral conductor and the fixed complex weighted
conductor is asserted.
