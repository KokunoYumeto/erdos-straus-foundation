# Exact Lean-ready dependency plan (no build claimed)

A. Rational valuations and Newton integrality
- Define labelled xs : Fin n -> Rat, all nonzero, and powerSum k.
- Prove Newton's recurrence through coefficient comparison for
  product (1 + xs_i*T), including multiplicities.
- Inductively prove factorial(j)*elementarySymmetric(j) is an integer for j<n.
- Prove v_l(factorial j)<j for a prime l and j>0.
- In the elementary symmetric function of the number of minimal-valuation roots,
  prove the unique minimal term valuation, without an unjustified cancellation.
- Deduce all reduced denominators coincide and the exact numerator divisibility.
- Prove the odd-n parity exclusion and binary factorial bound for even n>=4.
- Deduce the numerator-four integrality theorem. No ES existence axiom is used.

B. Exact three-root classification
- Use the reduced polynomial X^3-ABC to obtain distinct roots and a cubic root of
  unity at l !=3. Handle the derivative-zero prime3 by the displayed valuation1
  identity. Keep reduced denominator exponents.
- Construct each permitted denominator type by finite unit Hensel steps and CRT;
  prove the precise reciprocal-numerator valuations after reduction.

C. Original raw gate and trace
- Define the integer raw source p,a,R,U with the complete source ranges.
- Prove its rational reciprocal identity and exact denominator formula.
- Split vp(U)=0/1; prove E/M normalization, primality-sensitive units, ordered
  inverses, and trace congruence tags.
- Prove the exact equality S(U)=S(V) iff U=V or U*V=a^2.
- Define the finite free modules and trace-label pushforward. Construct its
  integral kernel basis and the stated weighted Hilbert quotient separately.

D. Full first-trace tail relaxation
- Prove equal tail denominators from integer sum, then derive d^2=R/gcd(R,N).
- Prove the complete factor-pair map, square-divisibility kernel, second-trace
  denominator and independent source ranges. Verify the p1009 counterexample.

E. Literal root traces and the algebraic exception
- Compute rank-four Newton traces and the factor2 in the rank-eight free basis.
- Reconstruct the denominator cubic from the original p and two traces.
- Prove the character sum by the conic parameterization; choose the actual k0.
- Prove the adjacent-square discriminant inequality and irrationality.
- Verify the ES identity in the quadratic field and all integral moments via
  the monic polynomial recurrence, while retaining the nonrational field.
- Give both local embeddings by the explicit Hensel recurrence. Prove the local
  cluster valuations using actual nonzero residues and the height bounds.

F. Finite numerical validation
- Formalize only the explicit statements when adding native_decide evaluations;
  do not replace the general valuation proof by bounded checks.
- The current Python independent checker is not a Lean certificate or a separate
  mathematical review. No sorry, universal occupancy axiom, or conjectural prime
  distribution input is part of this proposed dependency graph.
