# Exact Lean-ready dependency plan

This is a specification of declarations and proof dependencies, not compiled Lean code. Imported analytic theorems must be formalized or explicitly retained as named dependencies. Finite computation must prove propositions by kernel-checked reflection rather than treating a Python receipt as an axiom.

## 1. Finite projective geometry and group transport

Use `ZMod 23`, a two-dimensional vector space, its projectivization, and `SL(2, ZMod 23)`. Serialize infinity separately (the checker integer 23 is only a serialization label).

F01. Define C, J, T by the three displayed matrices and prove determinant one.
F02. Prove J^2=C^3=-I, (JC)^3=I, T^4=C, T^12=-I, T^24=I by exact normalization.
F03. Define fractional-linear action, including all zero-denominator and infinity cases; prove composition agrees with multiplication and +/-I act identically.
F04. Enumerate the two T cycles; prove each contains 12 distinct points and together they equal P1(F23).
F05. Construct the four projective g_u for u=1,5,7,11. Prove their multiplication is the actual unit-group multiplication modulo 12.
F06. Prove conjugation by C induces sigma=(5 7 11), fixing 1.
F07. Construct the 12 distinct g_u C^j and establish the semidirect-product group law; identify A4 via its Klein subgroup and cyclic quotient.
F08. Check the complete 2 x 4 x 3 table phi and inverse. Prove A4 equivariance and six/six T sheet transition counts.
F09. Finite-reflection certificate that <J,T> equals all determinant-one matrices modulo sign; cardinality 6072. This does not use an abstract classification from cardinality alone.
F10. Over Q, verify the original projective matrix M cycles infinity,+1/2,-1/2 and sends P(S,T) to -64 P(S,T). Specialize only the marked rational matrix/points, not analytic Mellin variables.

## 2. Golay code and Leech lattice

L01. Define code generators as the 23 translated quadratic-residue supports plus infinity in F2^24.
L02. Kernel-check rank 12, the complete 4096-word list, self-orthogonality, all-one word, and exact weight enumerator.
L03. Verify every matrix in F09 maps a code basis into the code; invertibility gives preservation of the whole code.
L04. Define the integral numerator module and its even submodule. Prove the bitwise carry identity and closure using code orthogonality.
L05. Prove the odd part is exactly the coset by (-3,1^23), and twice that vector belongs to the even part.
L06. Prove all lattice pairings are integral and all norms even after scale 1/sqrt8. Establish numerator index 2^36 and covolume one.
L07. Exclude squared norm two by exhaustive integer-square shapes. A nonzero lattice vector consequently has norm at least four.
L08. Establish coordinate-permutation preservation of the lattice from L03; T and all A4 elements act as lattice isometries.
L09. Define the 24 marked vectors v_i. Prove membership, norms 4, pairings 2 off diagonal, and differences of squared norm 4.
L10. Define the quotient module Lambda/12Lambda. Prove the 24 classes are distinct by the lower bound 576 for nonzero 12Lambda vectors. Prove equivariance and exact order-12 seed orbits.
L11. Derive the rational coordinate inverse a_i=(sum x-20x_i)/80 and Gram determinant; integral index is 5*2^12, not one.
L12. Optional finite reflection: complete membership/uniqueness enumeration of the 196560 minimal vectors. Minimal-shell completeness can alternatively use the three integer-square shapes plus the complete code.

The designation 'Leech' uses the stated classical construction or its uniqueness theorem with hypotheses even, positive definite, unimodular, rank 24, rootless. It is not inferred from a 196560-point count alone.

## 3. Residue operator kernel

R01. Define R_n, including zero for nonunits, and prove multiplicativity. Prove operator norm <=1.
R02. Define four real unit characters with the exact table. Establish orthogonal projections P_chi, sum I, rank six; define phase projections Q_j and rank-two joint products.
R03. Prove periodic partial-sum discrepancy <=2, with component discrepancies 2/3,1,2,1, including noninteger x.
R04. Prove the literal Gaussian Mellin formula w(w-1) pi^(-w/2) Gamma(w/2)/8 using Gaussian integral and gamma recurrence. Specify complex powers on the positive real axis.
R05. Establish absolute convergence/interchange for Re w>1, and the operator Euler product excluding exactly 2 and 3.
R06. Diagonalize into four modulus-12 Dirichlet L-series, including imprimitive Euler factors. Do not assign identical parity factors to all characters.
R07. Prove unique 2^a 3^b m decomposition and the exact scalar restoration, including finite-lambda restrictions.
R08. Prove integral h=0, total variation e^(-1/2)+9e^(-3), and the explicit tail H(v)=(pi/2)v^3 e^(-pi v^2).
R09. Apply Abel summation and R03 to prove ||B(u)||<=8 V_h sqrt(u); prove Gaussian large-u bound.
R10. Define h_lambda with the explicitly imported sup-norm estimate C lambda^-2 on its input interval. Prove the four error terms independently: input approximation, truncated Gaussian sum, lower cutoff, upper cutoff. Sum to the displayed estimate uniformly on closed substrips and in the imaginary part.
R11. Establish Mellin holomorphy for Re s>-1/2 and continuation of R06 there. R10 is not a theorem about Weil ground-state eigenvectors.

Analytic input: Connes--Consani--Moscovici v1, Lemma 7.2(ii), with precisely its normalization and large-lambda scope. A formal proof of the prolate estimate is a separate import obligation.

## 4. Scalar theta completion

T01. For positive-definite integral unimodular L of rank 2*kappa, prove Poisson theta inversion. Treat the rank-one kappa=1/2 example separately where useful.
T02. Prove lattice-point growth bounds sufficient for normally convergent theta derivatives.
T03. Define Psi=sqrt(u) Theta(u^(1/kappa)); derive inversion and the exact termwise differential identity.
T04. Prove K=.5(D^2-.25)Psi kills the zero mode and is rapidly decreasing at both ends. Deduce entire even Mellin transform.
T05. In Re w>kappa, justify sum/integral interchange and compute the Mellin factor; then use analytic continuation.
T06. Derive the regularized theta integral with residues -1 at w=0 and +1 at w=kappa. Compute both s=+/-1/2 endpoint values 1/2.
T07. Specialize L=Z and prove K_Z=4 E h, including the +/-n multiplicity.
T08. Import the Leech theta identity with normalization q=e^(2*pi*i*tau). Prove the zeta-product minus Delta-L-series identity initially in Re w>12, then the completed entire formula with w=12s+6 and coefficient 393120/691.
T09. Optional exact finite check of first 40 coefficients; this is not a replacement for the general theta identity in T08.

## 5. Full congruence/Jacobi packet

P01. Identify the discriminant module of sqrt(12)*Lambda with Lambda/12Lambda, cardinality 12^24, pairing (a,b)/12 modulo integers.
P02. Prove character orthogonality, Fourier unitarity, and F^2(a)=-a. Fix the negative sign in the exponential convention.
P03. Derive vector theta Poisson inversion and commutation of lattice isometries with F.
P04. Derive centered vector kernel/Mellin inversion and endpoint vectors .5e_0, .5F e_0. This is an identity of vectors, not a scalar zero-location assertion.
P05. Define full Jacobi theta functions and prove covariance under (a,z)->(ga,gz), plus the modular Gaussian factor.
P06. Prove disjoint Fourier supports for distinct cosets and recovery by integration over the appropriate real torus. At z=0, equal theta values do not recover isometric marks.
P07. Prove each Fourier image of a basis vector has full support on 12^24 classes. The 24 named seed coordinates alone are not a Fourier-stable packet.

## 6. Evidence and nonclaims

The JSON certificates have exact integers, rational numerators/denominators, and permutation arrays. Python passes are evidence of the stated finite computation, not Lean theorems. No RH/GRH assertion, universal ES witness, historical-priority claim, full Weil-eigenfunction comparison, or enumeration of 12^24 cosets belongs to the asserted dependency graph.
