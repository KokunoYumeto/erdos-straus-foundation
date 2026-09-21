# Proposed additive contribution: global arithmetic odd-receiver nonvanishing

This tranche extends `es-rh-continuation-b-20260920`, Track I, equations E1–E6.
It uses exactly the same literal quartic and receiving determinant polynomial.
No predecessor source is modified.

For every positive integral ES witness at every prime p=1 mod12, it proves
N=S^6F < -(125873811/262144)p^8. On p=1 mod24, the constant is
327448292668/47045881. The original inverse bound is
||O^-1|| < 360 S^9/(c p^8), with the actual label/receiving metric factors.

The all-witness theorem removes the former three-character restriction; it
neither supplies a first ES witness nor contradicts the real or p-adic singular
loci. A raw, gate-failing original divisor example already has a nonsingular
frame. Integral normalization indices and p-adic valuations remain separate.

Proof components: complete first-half Type I/II reduction; three positive
221-coefficient exterior polynomials; one positive 191-coefficient middle
comparison; exact determinant reduction and Lagrange inverse. The separate
checker uses full unisolvent grids and primitive state enumeration.

Observed replay: 48,542 main checks, 30,245 separate checks; all 99 primes
p=1 mod12 through 3000; 868,359 original divisor vectors; 2,451 E states and 2,054
oriented M states. Ordinary/optimized mathematical files agree. This is not an
independent mathematical review or Lean build.

The local patch is additive under
`research/incoming/es-turn07-global-receiver-determinant-20260921/`.
The integration may be published by a direct commit rather than a pull request.
The explicit coefficient certificates, their inequality domains and the final
publication receipt remain part of the module. The original
coefficient-occupancy obligation remains at Turn 7.
