# Typed maps and precisely retained information

1. **Split coefficient encoding.** `G(A)[Gamma] <-> {(S,f): nz(f) subset S}`. Inverse puts supported `f(g)` at every `g in S`, including zero, and tau elsewhere. Equations S2-S3. No loss.
2. **Amplitude observation.** `(S,f) -> f` into `A[Gamma]`. Fibre is every mask containing `nz(f)`. A zero output coordinate need not have been absent. Ordinary inversion does not by itself invert this observation.
3. **Idempotent completion.** `(S,f) -> (HS,f)` for a subgroup H, by multiplication by `(H,[1])`. Original mask gives the decorated inverse; without it support activation is not reversible. S4-S5 give the explicit C6 case.
4. **Positive count lift.** `N[Gamma] -> G(Q)[Gamma]`, zero coefficient to tau, positive integer coefficient to its supported amplitude. This is a semiring embedding because no nontrivial cancellation occurs. It is not the full-supported-fibre lift of an ordinary signed vector.
5. **Original ES exponent coordinates.** E uses raw exponents `0<=f_i<=2e_i`; M uses centered exponents `-e_i<=beta_i<=e_i`. The divisor is `prod q_i^f_i` or `a prod q_i^beta_i`. Channel and full prime list remain. A3-A4 give the positive ordered denominators and inverse.
6. **Positive geometric-series indices.** `(j,k,epsilon) -> (e,f)` or `(e,beta)` by P1. The exact parity formulas in its proof invert every coefficient term. No original term is duplicated.
7. **Periodic arithmetic.** `(g,e) -> (g,r,k)`, `e=r+ord(g)k`, retains e exactly. P2 computes the entire amplitude vector. This is not the capacity cap.
8. **Capacity reduction.** `e -> min(e,floor(ord(g)/2))` preserves coefficient support only. Counts and the removed original occurrences remain in the source record; it is not called a coefficient isomorphism.
9. **Grouping equal residues.** Per-prime exponent vector -> aggregate exponent for each residue. Complete fibre consists of all bounded integer compositions. P3 retains their exact count polynomial. No regrouped uniform count is substituted.
10. **Catalogue witness selection.** Actual factorization -> a dominated minimal residual-27 profile -> reserved actual occurrences -> one bounded target word -> original witness. The selected profile, allocations, full a, and surplus prime factors are retained. This is a constructive existence reduction, not a bijection on all witnesses. Its inverse fibres are exactly the reservation and bounded-composition choices stated in the proof.
11. **Arithmetic source extension.** `(n,a,R,u,c,t)` with `gcd(t,R)=1` -> `(t(n+R)-R,ta,R,u,E)` or `(t(n+R)-R,ta,R,tu,M)`. Inverse divides the retained data by t on this image. Original defects are unchanged. The parameter n changes; new states are not confused with embedded old states.
12. **Dirichlet and character observations.** All actual finite prime factors -> locally finite Dirichlet coefficient. Uniqueness of integer factorization supplies the inverse original prime list. Finite character evaluation is an amplitude observation with the usual character-inversion matrix, not a sparse split identity; all Euler factors at primes dividing R are retained. Selecting prime values of `4a-R` is an additional restriction and is not assumed to preserve the Euler product.

## Exact three-state distinctions

- An omitted coordinate has value tau.
- A retained source coordinate that evaluates to amplitude zero has value e.
- A positive target-count coefficient is a positive supported integer.
- Evaluation of an existing candidate's gate at zero is supported e, whereas selecting that candidate into a positive counting measure contributes one. These are different maps, not inconsistent conventions.
- Nonzero arithmetic target coefficients are produced by actual bounded prime exponents, not by idempotent activation alone.
