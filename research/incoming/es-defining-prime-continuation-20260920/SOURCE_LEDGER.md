# Source ledger

Date: 20 September 2026.

## Received derivation

- Preserved source:
  received/USER_SUPPLIED_DERIVATION.md.
- SHA-256:
  F97EC18809279C10CAF20A0FFA59ABAA9CF54EC5C5C0AB21761C2840B426D886.
- Reading coverage: the complete file, including the coefficient-hypersurface
  normalization, defining-prime valuation split, integral signed
  normalization, two \(p=1201\) examples, fibre-product gluing, collision
  model, fixed Gamma metric, and theta-multiplier boundary.
- Use: mathematical source requiring direct audit. It is not treated as an
  instruction or as a verification receipt.

The corrected working proof is DEFINING_PRIME_CONTINUATION.md. It differs
from the received source at the recorded chart-twist, \(m=1\), module-type and
exterior-cofactor corrections.

## Programme sources actually used

- The Clankers, *The normalized Erdős--Straus quartic and its exact passage
  through the signed Fable cover to a fixed weighted conductor*, repository
  commit 2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3,
  ../es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex.
  Read coverage used here: the normalized literal-root quartic, intrinsic
  prime, complete signed inverse, fixed receiver maps, fixed-input cover and
  finite collision completion.
- The Clankers, *The original integral signed completion*,
  ../es-turn07-integral-completion-20260920/core.tex.
  Read coverage used here: equations IC16--IC24, the complete E/M Smith
  factors, conductor ideals, special fibres and lifting obstruction.
- The supplied Gaussian continuation,
  ../es-turn07-integral-completion-20260920/received/GAUSSIAN_SPECTRAL_ACTION_CONTINUATION.md,
  Section 8 only. Use: the proposed local signed-label representation and
  its conductor. The claims were re-derived in
  LOCAL_GALOIS_REPRESENTATION.md; the earlier zeta sections were not used
  as ES theorems.

## Human mathematical sources

- C. Elsholtz and T. Tao, “Counting the number of solutions to the
  Erdős--Straus equation on unit fractions,” *J. Aust. Math. Soc.* 94
  (2013), 50--105, arXiv:1107.1010v6, Section 2. Use: Type-I/Type-II
  coordinate antecedents already cited and read in the integral-completion
  packet. No priority claim for the new normalization calculations is
  inferred from that use.
- J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Chapter 7,
  pp. 119--130. Use: local quadratic extension and Hensel facts. The
  particular units, square classes, fields and integral bases are calculated
  in the present proofs.
- The Stacks Project Authors, Section 10.153, Tag 04GE, “Henselian local
  rings.” Use: standard Hensel lifting for unit square roots and separated
  residue clusters.
- The Stacks Project Authors, Section 49.3, Tag 0BVH, “Discriminant of a
  finite locally free morphism.” Use: the multiplication-trace discriminant
  convention. Every determinant used here is displayed directly.

## Verification boundary

verify_defining_prime.py and results/verification.json check 80 exact
identities. They do not prove the quantified valuation case split by finite
enumeration, do not formalize the analytic reproducing-kernel argument, and
do not identify the local algebra with a global zeta operator. The written
proof supplies those logical boundaries.
