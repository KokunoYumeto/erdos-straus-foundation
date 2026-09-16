# Typed maps and inverse data

## A1. Original exponent/divisor equivalence

Domain: (p,a,R,c,beta), beta in full [-e,e] box.

Codomain: same original labels with u|a^2.

Map: u=product q_i^(e_i+beta_i).

Inverse / full fibre / information loss: beta_i=v_q_i(u)-e_i; retain primes and channel.

Proof: core (1)-(2).

## A2. Rational and integral denominator reconstruction

Domain: canonical original leaf.

Codomain: same label with (h,r,s,quotient),(X,Y,Z).

Map: (4)-(5), D=R/gcd(R,g_c).

Inverse / full fibre / information loss: u=a^2/(RY-pa) E; u=pa^2/(RY-pa) M; gcd normalization returns every coordinate.

Proof: core (4)-(5).

## A3. Defect spectral observation

Domain: complete original leaf.

Codomain: x=1/D with label retained.

Map: D=R/gcd(R,g_c).

Inverse / full fibre / information loss: x alone identifies D but does not recover shell,u,channel; these remain in state.

Proof: core (2)-(3).

## I1. Full finite interpolation map

Domain: polynomials degree<=j+1.

Codomain: values at 0,1,1/3,...,1/(2j+1).

Map: evaluation.

Inverse / full fibre / information loss: inverse complete Lagrange basis, not only one selected value.

Proof: core (7)-(8).

## I2. Signed interpolation filter

Domain: original labelled eigenvalues.

Codomain: same support with coefficient Phi_j(1/D).

Map: Phi_j=x product (((2nu+1)x-1)/(2nu)).

Inverse / full fibre / information loss: not invertible: failures D=3,...,2j+1 are zeroed; original D/labels retained; zero coefficient not absence.

Proof: core (9)-(10).

## I3. Hybrid sharp error evaluation

Domain: j>=1,s>=1.

Codomain: finite set of possible integer maximizing k.

Map: window (11).

Inverse / full fibre / information loss: all maximizers and exact rational values are retained; j=0 or s=0 separate.

Proof: core (11).

## U1. Original moment observation

Domain: counting measure on original labels.

Codomain: M_k=sum D^(-k).

Map: original unit mass or declared masses.

Inverse / full fibre / information loss: moments forget which source labels supplied values; no claimed inverse from moments alone.

Proof: core Section3.

## U2. Uniform signed row certificate

Domain: p and original moments through j(p,n)+2.

Codomain: ell_pn,u_pn and unique integer H_p.

Map: (12)-(16).

Inverse / full fibre / information loss: ceil ell=floor u=H; a positive score gives a finite search for a positive original summand, not its identity without search.

Proof: core (12)-(16).

## U3. Certified interval input

Domain: absolute certified moment intervals.

Codomain: sign-directed lower/upper count interval.

Map: coefficient l1 norm <= j+2.

Inverse / full fibre / information loss: uncertainty retained; actual tolerance (16(j+2)3^n)^(-1), no row mass normalization.

Proof: core Section3 Absolute input error.

## U4. Infinite row operators

Domain: maximal counting number-operator domain sum H_p^2 |v_p|^2 finite.

Codomain: same domain.

Map: diagonals ell_pn,u_pn.

Inverse / full fibre / information loss: bounded differences from N, constants (15); relative traces only on stated convergent domain.

Proof: core Section3 Infinite operators.

## P1. Restriction to a common channel polynomial

Domain: one normalized coefficient vector P.

Codomain: two identical coefficient vectors (P,P).

Map: Delta P=(P,P).

Inverse / full fibre / information loss: inverse on diagonal reads one entry; full two-channel form retains off-diagonal-in-this-decomposition directions.

Proof: core Section4.

## P2. Partition-resolved lower count

Domain: genuine disjoint original subfamilies.

Codomain: integer lower bound sum max(0,ceil Ld).

Map: (19).

Inverse / full fibre / information loss: sums original mass, not split occurrences or duplicate branch labels; refined bound monotone.

Proof: core (19).

## S1. Split addition

Domain: B_f x B_b x {E,M}.

Codomain: B_e x {E,M}.

Map: (xi,eta,c)->(xi+eta,c).

Inverse / full fibre / information loss: full interval fibres and eta=beta-xi; cardinal n(beta) retained.

Proof: core Section4 Split arithmetic.

## S2. Isometric split duplication and average

Domain: counting l2 on original states.

Codomain: occurrence l2 weighted 1/n(beta).

Map: U duplicates values; U* averages.

Inverse / full fibre / information loss: U*U=I; kernel of average fibre sums zero; full inverse fibre Uv+kerU*.

Proof: core (20).

## S3. Polynomial functional calculus under split compression

Domain: original X and f.

Codomain: f(UXU*) on full occurrence space.

Map: Uf(X)U*+f(0)(I-UU*).

Inverse / full fibre / information loss: returns by U* on imU; Phi_j(0)=0, pure P_j has nonzero relation-sector term.

Proof: core (20).

## H1. Direct/residue finite histogram comparison

Domain: bounded actual prime exponents.

Codomain: group-algebra coefficient array followed by gate histogram.

Map: (23).

Inverse / full fibre / information loss: full fibres indexed by original exponents; neither group support nor histogram alone replaces labels.

Proof: core Section5.

## H2. Prime proof DAG

Domain: n,base,complete factorization n-1 with descending prime certificates.

Codomain: deterministic primality conclusion.

Map: order of base modulo every divisor must equal n-1.

Inverse / full fibre / information loss: all factor certificates and modular residues retained; no probable-prime step.

Proof: core Section5 and prime_proof.json.

## F1. All-integer progression map

Domain: j in nonnegative integers.

Codomain: n, a,u,raw h0,r0,s0,kappa0, ordered witness.

Map: (29).

Inverse / full fibre / information loss: j=(n-pstar)/255650653440 on image; no claim every hard n lies in image.

Proof: core Section6.

## F2. Primitive canonicalization

Domain: raw progression marking.

Codomain: coprime marking with same denominators.

Map: d=gcd(r0,s0); h=h0*d^2,r=r0/d,s=s0/d,kappa=kappa0/d.

Inverse / full fibre / information loss: retain d/raw frame if its inverse is requested; denominator order and u unchanged; gcd(d,135)=1.

Proof: core Section6.
