# Typed morphisms and retained fibres



All entries refer to the numbered formulas of `core.tex`. This is a mathematical register, not a claim of formal compilation.



## A1. Original fixed-seed cofactor

Domain: p,k,N=factorized p+4u; Q|N, Q=-1 mod2^k.

Codomain: original middle state.

Map: `R=N/Q; a=(p+R)/4; A3 normalization`.

Inverse/fibre: u=pa^2/(Ry-pa), Q=N/R; retain p,R,M and ordered denominators.

Boundary: No prime assumption for identity; require p=1mod8,p>2u. N and a factorizations differ..

Proof: A1-A4.



## A2. Affine prime-exponent source

Domain: disjoint original prime blocks and bounded parameters t.

Codomain: original physical divisors W|N.

Map: `v_q(W)=offset_q+step_q*t_block`.

Inverse/fibre: read any nonzero step; all other coordinates checked.

Boundary: Image is a specified subset of original divisor box; unused complement is not absent from the full source..

Proof: C1.



## B1. Cyclic/Pascal coefficient coordinates

Domain: F2[X]/(X^o-1).

Codomain: F2[T]/T^o.

Map: `T=X+1`.

Inverse/fibre: X=T+1.

Boundary: Ordinary coefficient algebra isomorphism, not a global sparse-semiring inverse..

Proof: B1.



## B2. Ordinary cyclic quotient

Domain: A_o.

Codomain: A_d.

Map: `sum coefficients with equal residues modulo d`.

Inverse/fibre: kernel consists of coefficient vectors with each coset sum zero.

Boundary: Need d|o; support masks travel even when amplitudes cancel..

Proof: B2-B3.



## B3. Relative boundary inclusion

Domain: A_d as an F2[X]-module via quotient.

Codomain: ker(T^d) in A_o.

Map: `X^r -> X^r*N_d`.

Inverse/fibre: test each coset constant; then read coefficient at r=0..d-1.

Boundary: Not a unital algebra map; image is square-zero for proper d. Ordinary quotient is not its inverse..

Proof: B2-B3.



## B4. Relative norm multiplication

Domain: A_o.

Codomain: ker(T^d).

Map: `F -> N_d F = iota_d pi_d F`.

Inverse/fibre: retain coset-sum kernel of pi_d for full source reconstruction.

Boundary: Integer projection/repetition gives L times identity; mod2 it is zero when L even..

Proof: B3.



## B5. Subgroup-tower comparison

Domain: A_dprime, dprime|d|o.

Codomain: A_o.

Map: `iota_o,d iota_d,dprime = iota_o,dprime`.

Inverse/fibre: unique subgroup exponent decomposition.

Boundary: Not multiplication of overlapping norm elements; their intersection multiplicity remains..

Proof: B4.



## B6. Supported coefficient reduction

Domain: sparse integer coefficients with declared presence keys.

Codomain: sparse F2 coefficients with same image support.

Map: `reduce values modulo2 without deleting zero keys`.

Inverse/fibre: integer coefficient and preimage labels retained as decoration.

Boundary: A zero coefficient at an existing key is supported e, not tau. Reduction alone is not injective..

Proof: B3 and examples.



## C1. Disjoint lower/high exponent decomposition

Domain: 0<=t_i<=E_i.

Codomain: r_i,z_i with stride delta_i.

Map: `delta_i=d/gcd(d,a_i); t_i=r_i+delta_i*z_i`.

Inverse/fibre: Euclidean division gives unique r_i,z_i.

Boundary: No fractional mass introduced; includes phase parameter but phase is not an integer prime..

Proof: C3-C4.



## C2. Lower quotient target

Domain: actual lower-digit vector.

Codomain: target class in C_d.

Map: `t0-sum a_i*r_i mod d`.

Inverse/fibre: full lower vector and capacities retained.

Boundary: Zero lower gate does not assert a high lift..

Proof: C5.



## C3. Actual high-capacity packet

Domain: bounded high box with explicit C6 prefixes.

Codomain: positive integer packet on subgroup C_L.

Map: `choose total weighted degree L-1; use binary submask parameters`.

Inverse/fibre: suffix-parity inverse and every bounded source tuple retained.

Boundary: Requires high logs divisible by d; exact total degree alone is insufficient. d=o excluded..

Proof: C6-C7.



## C4. High target reconstruction

Domain: subgroup target, selected packet and lower digits.

Codomain: full original parameter vector.

Map: `z_i from packet; t_i=r_i+delta_i*z_i`.

Inverse/fibre: read affine parameters, divmod stride, check retained digits and submasks.

Boundary: Source coordinates not replaced by their modular residues..

Proof: Theorem actual relative packet forcing.



## C5. Formal orientation return

Domain: physical word W and epsilon in{0,1}.

Codomain: original cofactor Q.

Map: `Q=W for epsilon0; Q=N/W for epsilon1`.

Inverse/fibre: W=Q or R according to retained role.

Boundary: Forgetting role identifies at most complementary words; do not count them as new states..

Proof: C2 and A2.



## C6. Uniform lower-fibre capacity

Domain: E_i+1=C_i*delta_i+B_i.

Codomain: actual capacity function.

Map: `F_i(r)=C_i-1+1_(r<B_i)`.

Inverse/fibre: retain E_i,delta_i and admissible r_i.

Boundary: Minimum capacity may be insufficient even when some particular fibre works; not necessary for all witnesses..

Proof: C8.



## D1. Exact principal-unit logarithm

Domain: t|M, t=-1 mod2^ell, v2(b-1)=ell.

Codomain: r_t in[0,L), L=2^(k-ell).

Map: `b^r_t=-t^-1 mod2^k`.

Inverse/fibre: binary lift chooses one of two exponents at each precision.

Boundary: Actual b-factor capacity is independently required..

Proof: D1-D2.



## D2. All original cofactors at one high prime

Domain: t and i=r_t+jL within0..e.

Codomain: Q=b^i t.

Map: `multiply actual factors`.

Inverse/fibre: i=v_b(Q); t=Q/b^i.

Boundary: Complete bijection because gcd(b,M)=1..

Proof: D2-D3.



## D3. All-exponent generating series

Domain: fixed b,M,k and all nonnegative e.

Codomain: positive integer count series.

Map: `sum C(e)z^e=(sum_t z^r_t)/((1-z)(1-z^L))`.

Inverse/fibre: coefficient tracks actual bounded i<=e.

Boundary: Varying e varies p; remove invalid finite prefix; not a prime-filtered rationality theorem..

Proof: D3a.



## D4. Minimal coarse target reduction

Domain: actual t=-1mod2^ell of minimum occurrence length.

Codomain: coarse word of length<=2^(ell-2).

Map: `remove a proper quotient-zero subword if its full sign is+1, keep if-1`.

Inverse/fibre: retain removed prime occurrences and original t.

Boundary: Not an arbitrary subgroup-membership replacement; uses an existing bounded coarse target..

Proof: D4.



## E1. Separation-family parameter construction

Domain: k>=6, actual q,r in stated reduced classes.

Codomain: actual N,p and exactly two target cofactors.

Map: `N=3*17^L*q*r; p=N-4u; Q1=17^(L/2)r,Q2=3*17^(L/2)q`.

Inverse/fibre: retain k,q,r,L and role; complete enumeration by coarse residues.

Boundary: Dirichlet supplies auxiliary primes, not primality of derived p. Individually certified example separate..

Proof: E6-E8.



## F1. Canonical relative search

Domain: actual factorization and preceding maximal singleton/pair lines.

Codomain: first certified relative packet or no certificate in declared class.

Map: `test every proper relative level and all actual lower digits after capacity pruning`.

Inverse/fibre: certificate records pattern, offsets,strides,digits,selected capacities and inverse word.

Boundary: Not exhaustive over every possible affine line or every ES state. Stronger three-word baseline retained..

Proof: Section finite comparison.
