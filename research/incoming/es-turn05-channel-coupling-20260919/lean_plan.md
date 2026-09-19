# Lean-ready dependency plan (no build claimed)

Base: Nat prime factorization/divisibility/gcd, Finite/Pi bounded integer products, Rat reciprocal arithmetic, ZMod for unit residue characters, finite sums.

A. Source identity: R=4a-p>0, p prime, gcd(pa,R)=1. Prove valuation gcd normalization and both ordered reciprocal identities; retain channel enum.
B. Character lemma: primewise quadratic reciprocity plus the supplementary law for 2, extended to original square divisors. Derive E/M sign conditions. Formalizing (4) requires no analytic machinery.
C. Define PrimitivePair with channel, positive r,s, gcd=1, rs|N, and actual congruence. Define PairSource with b,c|pN, R|b+c. Construct an Equiv to the disjoint union of primitive states × (divisors h) × Bool, where Bool means p-common or p-side according to channel. Prove all inverse branches by p-valuations. Cardinality gives 2*tau(h).
D. Define F,T on divisors of N. Prove T/2=sum F by the equivalence rather than division over Nat. Use integers for Möbius inversion. Auxiliary source N does not carry a false shell witness.
E. Reciprocal source equivalence: coprime r,s, 4hrs=pD+1, r+s=Dlambda. Prove gcd(r,lambda)=1, min denominator in first half, original E residual and inverse. Handle equal-r-s impossibility and factor-2 orientation fibre explicitly.
F. Common-source gcd identity. Derive the nonresidue overlap classification and bounded converse under p=1 mod8.
G. Finite certificate theorem: enumerate all 22 t values by the strict sigma*q*t²<3p bound; factor products, prime trial certificates, all square divisors and all gates. Separate certified reconstruction for the R31 witness pair. This certifies the local obstruction only.
H. Optional: group algebra/finite character identity with Möbius differences. This is not required to check the finite reciprocal obstruction or the original solutions.

No axioms of uniform graph occupancy, favourable factor inventory, positive Gram, or ES are permitted in these lemmas. The universal H_p>0 remains a separate unproved target.


## Added channel-window dependency chain (not compiled)

Define tagged original E/M records with divisibility and source-bound fields.
1. `quarter_domain`: Nat integrality a/(4u) iff4u|a; define on Div(a/4).
2. `quarter_involutive` and `quarter_exchanges_channels`: clear unit denominators
   in the actual integer gates; no division in a nonunit ring.
3. `window_E_equiv`, `window_M_equiv`: use prime2valuation plus odd divisors.
4. `interval_residue_count`: floor-difference identity over Int, including negative
   endpoints; prove separately before reducing mod a finite cyclic order.
5. `paired_interval_extrema` and `union_length`: e>=1; preserve e0exception.
6. `simple_NR_parity`: use quadratic reciprocity and exponent bound0..2, then exact
   original fibres for E and the two M orientations.
7. `power_channel_counts` and `count_difference_le_one`: equality of interval lengths.
8. `six_cycle_certificate`: decidable trial primality, exhaustive square-divisor
   generation, all17strict t-bound lists, and reconstruction of the exit witness.
The executable Python certificates are not Lean proofs. No `sorry`-based file or
unverified imported universal existence assertion is represented as a build.
