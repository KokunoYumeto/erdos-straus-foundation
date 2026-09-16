# Typed map register

## A1. Fixed-seed arithmetic
Domain: (p,k,Q), Q|p+4u, Q=-1 mod2^k. Codomain: original positive M state.
Map: R=N/Q; a=(p+R)/4; gcd normalization.
Inverse/fibres/information loss: u=pa^2/(Ry-pa), retain k, channel and ordered denominators.
Proof: A1--A3.

## A2. Available affine coordinates
Domain: bounded parameter tuple on disjoint prime blocks. Codomain: actual divisor W|N.
Map: v_q(W)=a_q+sigma_q t_i, endpoint checks.
Inverse/fibres/information loss: read one nonzero step per block, then verify all coordinates.
Proof: A4.

## A3. Role return
Domain: available W and epsilon=0/1. Codomain: cofactor Q.
Map: Q=W or Q=N/W.
Inverse/fibres/information loss: retain role; forgetting it has at most two preimages Q,R.
Proof: A5.

## B1. Cyclic coordinate change
Domain: F2[C_o]. Codomain: F2[T]/T^o.
Map: T=X+1, full binomial coefficients.
Inverse/fibres/information loss: same binomial substitution, not a scalar readout.
Proof: B1.

## B2. Relative readout
Domain: nonzero parity P of order nu>=o-D. Codomain: q in F2[C_D].
Map: divide by T^(o-D), keep all coefficients; substitute T=X+1.
Inverse/fibres/information loss: norm_D*q returns exact parity P.
Proof: B2.

## B3. Integer source partition
Domain: actual labelled positive packet. Codomain: selected norm words and paired even remainder.
Map: P=norm_D*q_hat+2E; canonical suffix representative at odd sites.
Inverse/fibres/information loss: selected word or (even pair, side), retaining residue and original tuple.
Proof: B3 and following proof.

## B4. Positive complement observation
Domain: two independently available coordinate packets P,G. Codomain: integer target lower bound.
Map: norm_D*q_hat*pi_D(G)+2EG.
Inverse/fibres/information loss: choose actual coarse G-word and odd fine P-word; not an inverse of total counts alone.
Proof: B4.

## B5. Unit-corrected comparison
Domain: A_D with nu=o-D. Codomain: ker(T^D) in A_o.
Map: h -> norm_D*q*h.
Inverse/fibres/information loss: constant-on-coset image test, read representative coefficients, multiply by q^-1.
Proof: B5.

## B6. Singular exception
Domain: A_D with z=nu-o+D>0. Codomain: T^nu A_o.
Map: same multiplication.
Inverse/fibres/information loss: kernel T^(D-z)A_D; readout divisible by T^z; invert U modulo T^(D-z).
Proof: Theorem1.

## B7. Ordinary quotient
Domain: A_o. Codomain: A_D.
Map: sum coordinates per D-coset.
Inverse/fibres/information loss: kernel the coset-sum-zero module; pi iota=0 mod2, not identity.
Proof: B5.

## B8. Actual SplitZero BR1
Domain: M=F2[[T]], v=T^D, f=T^(o-D)U. Codomain: quotient and its v-annihilator.
Map: [x] -> [f(x)].
Inverse/fibres/information loss: prequotient cancellation; U is a power-series unit; polynomial ideal not falsely replaced.
Proof: BR1 instance after Theorem1.

## B9. Supported-zero observation
Domain: original integer coefficient with presence label. Codomain: same support in G(F2).
Map: reduce amplitude modulo2.
Inverse/fibres/information loss: full integer count and original word fibre retained; e is not tau.
Proof: section2.

## C1. Bounded submask packet
Domain: c_i<=E_i, actual log a_i. Codomain: integer packet and its reduced binomial product.
Map: sum over t_i submasks; nu=sum c_i lowbit(a_i).
Inverse/fibres/information loss: retain bits and original prime indices; no coloured occurrence duplication.
Proof: C1--C3.

## C2. Odd suffix inverse
Domain: odd fine high-packet coefficient. Codomain: one original bounded tuple.
Map: follow the unique odd suffix branch.
Inverse/fibres/information loss: full remaining fibres retained; target terminates at zero.
Proof: section3.

## C3. Classical weight observation
Domain: nonzero exact T-order nu. Codomain: lower bound on Hamming weight.
Map: weight>=2^popcount(nu).
Inverse/fibres/information loss: does not locate the target or invert support cardinality.
Proof: C4.

## D1. Rational geometric inverse
Domain: q=X^r S_h, h odd<D. Codomain: inverse in Q[C_D].
Map: X^-r(S_a(X^h)-(b/h)norm_D), ha-Db=1.
Inverse/fibres/information loss: full exact convolution inverse; signs and denominator h retained.
Proof: D1.

## D2. Integral coefficient image
Domain: Z^D under C_q. Codomain: sum-divisible-by-h sublattice.
Map: cyclic convolution.
Inverse/fibres/information loss: cokernel Z/h; determinant magnitude h, not unimodular merely because mod2 invertible.
Proof: D2.

## D3. Coefficient Gram
Domain: formal cyclic coefficient input. Codomain: repeated coefficient output.
Map: norm_D C_q.
Inverse/fibres/information loss: Gram (o/D)C_q^T C_q; no identity-metric replacement.
Proof: D3.

## D4. Original word quotient
Domain: orthonormal word coordinates. Codomain: occupied residue sums.
Map: sum within each fibre.
Inverse/fibres/information loss: canonical section y_r/P_r; star kernel, primitive and norm splitting.
Proof: section4 original word paragraph.

## D5. Available formal amplitude
Domain: D_P defined by all original zero-fibre constraints. Codomain: actual word space.
Map: (C_qh)_(r modD)/P_r on every actual word.
Inverse/fibres/information loss: formal image and integral image kept separate; no words supplied where P_r=0.
Proof: D4--D5.

## E1. Explicit factor family
Domain: k>=6 and prime residues E1. Codomain: unique original cofactor.
Map: Q=3^(d/2-1)q s, R=3^(d/2)r.
Inverse/fibres/information loss: factorization and fixed p retained; prime p only when independently certified.
Proof: E1--E4.

## E2. Family normalized unit
Domain: integer high packet P_d. Codomain: Q_d and even remainder.
Map: E2 coefficient identity.
Inverse/fibres/information loss: unit has d+1 terms and integer index d+1; deleting it changes targets.
Proof: E2.

## E3. Preceding canonical comparison
Domain: all old singleton/same-coset-pair patterns and strides. Codomain: explicit maximum weighted capacity.
Map: E5 envelope below required o/stride-1.
Inverse/fibres/information loss: not a no-go theorem for arbitrary affine packets.
Proof: E5.

## E4. Surviving three-prime shear
Domain: 0<=a<=d-3, t=0/1. Codomain: original exponents (a+2t,t,1-t).
Map: step 3^2 r/s is a half turn.
Inverse/fibres/information loss: t=v_r, a=v_3-2v_r; actual endpoints retain compensating powers.
Proof: E6.
