# Exact Lean-ready dependency plan (no build performed or claimed)

1. Define an original E/M state over Nat with p prime, p=1 mod12 and the ordered
   denominator formulas. Prove both reciprocal identities in Rat and the gcd
   normalization / inverse from u|a². Retain an orientation bit for M.
2. Prove every positive integral ES witness has distinct literal roots and a
   unique smallest denominator in (p/4,p/2), using the explicit argument in
   core.tex. This is not assumed from a completeness label.
3. Define elementary symmetric polynomial N in four variables over Int and F
   over Rat[A,A^-1,B,C,D]. Prove the displayed N=S^6 F identity by ring_nf.
4. Construct quotient reduction in basis 1,T,T²,T³. Prove A det(C_H)=4 F;
   include the Gaussian row factors and oriented Vandermonde/sign relation.
5. Define P_E through the explicit scaled-root polynomial. Certify its exact
   division and the three translated coefficient arrays by integer computation.
   Use native_decide only to check the explicit finite equality/positivity data,
   not an unbounded positivity axiom.
6. Prove nonnegative-variable evaluation of a polynomial with nonnegative
   coefficients. The positive constant term yields strict positivity. Apply
   the two actual derivative numerators to Q_E=P_E/(2^26 u^6 w^8).
7. Certify the exact boundary constants. Apply u>=2; prove u>=5 for p=1 mod24
   by the original quadratic-character identity, or as a separate modular
   small-word lemma for u=1,2,3,4.
8. Define H_M from the normalized source (L,bc,bL,cL). Certify
   47045881 H_M-327448292668 L_M^6 and its full coefficient list. Show equality
   only X=Y=0 and exclude that rational cone endpoint in the prime domain.
9. Combine the E/M classifications and two cones to prove N<-c p^8 for every
   original state and therefore every positive integral witness.
10. Prove the rational Lagrange inverse of C_H U on four distinct roots,
    with xi_j² d_j=1. Sign/permutation labels are explicit parameters.
11. Derive the cofactor entry bound, adjugate Frobenius estimate and original
    metric factors. The analytic norms require separate matrix norm lemmas;
    they are not established by native_decide on a finite scan.
12. Verify the fixed examples and five negative controls with rational/natural
    arithmetic. The bounded census is an auxiliary decidable proposition.

No axiom asserting ES existence, original-source occupancy, nonzero receiver
on all positive real quartics, or unchanged analytic conductor metrics is used.
