# Lean formalization plan for Turn 7

Status: no Lean build is claimed for this tranche.  This file is a dependency
plan; it contains no `sorry` certificate and no theorem is counted as formalized.

1. Define an `OrientedMiddleState p` structure retaining `a,R,u,g,h,r,s,lambda`
   and all positivity, divisibility, gcd and ordering hypotheses.
2. Prove the prime-valuation normalization equivalence
   `(a,u) <-> (h,r,s)` including divisor complementation and orientation.
3. Prove the ordered denominator identity and its rational inverse after
   clearing every denominator.
4. Define `j,Q,A` and prove all four equations in (2)--(3), including strict
   `Q+1<2A*R` and the ranges `0<R,Q<p`.
5. Formalize the `A>=2` branch of the general bound as integer polynomial
   inequalities, preserving the `Q=t` and `R=t` cases.
6. Formalize `A=1`, exclude the tie, parameterize `Q=t+4k`, and prove the
   concave endpoint comparison without a real-analysis black box.
7. Derive the exact integer cutoff equivalence for `t=4k-1` and certify both
   equality states at `p=41`.
8. Define the six hard residue classes modulo 840, prove the minimum-prime
   lemma, exclude `k=1`, and formalize the refined endpoint comparison.
9. Prove the equality classification and the full integer family; keep the
   statement separate from any prime-value assertion.
10. Define direct-chart data and prove its equivalence with oriented states
    satisfying `R<=Q`.
11. Define cofactor-chart data and prove `u|j^2` in the forward direction.
12. For the inverse, prove primewise that `u|j^2` implies `u|gcd(j,u)^2`;
    then prove every returned identity, range and gcd condition.
13. Assemble the charts as a sum type and prove bijectivity and disjointness,
    assigning `R=Q` only to the direct constructor.
14. Verify the `p=2521` original residual-47 residue table and the cofactor
    return as two nonidentical objects connected by the exact inverse.
15. Prove the divisor-candidate bound in (11), including the divisor-triple
    injection and harmonic estimate.
16. Formalize CRT existence for the two congruences and import or prove the
    required Dirichlet theorem only if available; until then separate the
    elementary conditional progression lemma from the analytic infinitude step.
17. Prove the quadratic-residue statements by exact reciprocity and the
    supplementary law, then the E and M grade lower bounds.
18. Prove the endpoint solution map for the progression by a cleared rational
    identity.
19. Formalize the partial-factor order lemma: orders modulo each prime divisor,
    full prime-power divisibility, and the least-prime-factor contradiction.
20. Reflect `scan.json`, `examples.json` and `grade_certificate.json` only after
    the structural theorems compile.  Bounded reflection is not a replacement
    for the universal occupancy theorem.

Unavailable theorem: every hard prime occupies one of the two M charts.
Unavailable theorem: every hard prime has a bounded E or M grade independent
of `p`; the latter statement is disproved in `core.tex`.
