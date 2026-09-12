# Two-sided ES morphism delta

This register supplements, rather than overwrites, the preceding typed-morphism workbench. All failed candidates remain positive rational solutions; integrality is recorded by D.

## D01_full_box

**Domain**: p prime=1 mod4; p/4<a<3p/4; exponent f_q in [0,2v_q(a)]

**Codomain**: u positive dividing a^2 with p,a retained

**Map**: u=product(q^f_q)

**Inverse**: f_q=v_q(u)

**Fibres**: singletons

**Exceptional Locus**: No angle or R<p cutoff permitted for global failure.

**Scope**: Inherited complete divisor coordinates; exact enumerated domain.

## D02_primitive

**Domain**: (p,a,u,E/M)

**Codomain**: (p,R,u,h,r,s,E/M,kappa/lambda)

**Map**: g=gcd(a,u); R=4a-p; r=u/g; s=a/g; h=g^2/u; kappa=(pr+s)/R or lambda=(r+s)/R

**Inverse**: a=hrs; u=hr^2

**Fibres**: singletons

**Exceptional Locus**: Quotient is allowed to be rational on failed candidates.

**Scope**: Extension keeps unsuccessful rational candidates.

## D03_rational_E

**Domain**: canonical exterior candidates

**Codomain**: positive rational ordered ES triple at p

**Map**: (a,(pa+a^2/u)/R,(pa+p^2u)/R)

**Inverse**: u=a^2/(RY-pa)

**Fibres**: singletons in canonical order

**Exceptional Locus**: For arbitrary ordered integral witnesses with v_p(RY-pa)=2, retain the exterior swap.

**Scope**: Inherited channel formula, extended before divisibility gate.

## D04_rational_M

**Domain**: canonical middle candidates

**Codomain**: positive rational ordered ES triple at p

**Map**: (a,p(a+a^2/u)/R,p(a+u)/R)

**Inverse**: u=pa^2/(RY-pa)

**Fibres**: singletons in canonical order

**Exceptional Locus**: Y=Z exactly u=a; no extra middle swap bit.

**Scope**: Inherited channel formula; full rational collision stratum retained.

## D05_return_defect

**Domain**: full candidate with original p

**Codomain**: minimal common reduced denominator D

**Map**: D_E=R/gcd(R,4u+1); D_M=R/gcd(R,u+a)

**Inverse**: With cleared X and p: D=4product(X)/(p*S(X))

**Fibres**: Forgetting candidate loses fibres; no claim D alone is injective.

**Exceptional Locus**: D=1 success; otherwise odd D in [3,2p-3], gcd(D,p)=1.

**Scope**: Proved exact common-denominator theorem.

## D06_clearing

**Domain**: (p,candidate,D)

**Codomain**: (original p, scaled parameter pD, integral ordered X)

**Map**: X=D*q; F_p(X)=p(D-1)S(X)

**Inverse**: D=4product(X)/(pS(X)); q=X/D; candidate inverse D03/D04

**Fibres**: singletons with p and canonical order retained

**Exceptional Locus**: Forgetting p permits distinct integral models of the same projective point.

**Scope**: Failed states map to genuine integral ES solutions at pD, not p.

## D07_same_shell

**Domain**: (p,a,u_E,u_M) with u_E,u_M|a^2 and u_M=p*u_E modR

**Codomain**: exterior-middle correspondence at fixed p,R

**Map**: retains both actual divisors; D_E(u_E)=D_M(u_M)

**Inverse**: reverse the ordered pair of divisors

**Fibres**: complete finite relation; not an everywhere-defined map

**Exceptional Locus**: Some exterior states have no middle partner.

**Scope**: Defect preserved, including when D>1.

## D08_complement

**Domain**: (p,a,u,M)

**Codomain**: (p,a,a^2/u,M)

**Map**: reverses Y,Z and preserves D

**Inverse**: itself

**Fibres**: singletons

**Exceptional Locus**: Fixed rational point u=a is a failed, repeated-root state.

**Scope**: Full rational complement, unlike integral-only fixed-point-free locus.

## D09_prime_obstruction

**Domain**: failed canonical candidates

**Codomain**: prime-labelled valuation deficits

**Map**: choose least ell|D; v_ell(R)>v_ell(g_c(u))

**Inverse**: Recompute each full box leaf and all deficits; not from ell alone.

**Fibres**: Each leaf may have several obstruction primes; chosen minimum canonical.

**Exceptional Locus**: A union of obstructions on different leaves is not one common local obstruction.

**Scope**: Constructive negative certificate; scope must be full to imply ES failure.

## D10_diagonal_algebra

**Domain**: complete finite labelled candidate set

**Codomain**: A_p=Q^candidates, H multiplication by (D-1)/2

**Map**: ker H gives successes; when all D>1 inverse is pointwise 2/(D-1)

**Inverse**: Read coordinate label of any zero, or multiply by the displayed inverse

**Fibres**: No arithmetic labels forgotten.

**Exceptional Locus**: Operator invertibility is equivalent to failure, not independently proved for a prime.

**Scope**: Exact two-sided certificate encoding.

## D11_energy_packet

**Domain**: actual signed exponent box

**Codomain**: multiplicity function mu on units moduloR

**Map**: beta->product q^beta; retain full fibre table

**Inverse**: actual beta in target yields u=product q^(e+beta); negate beta for target -p when needed

**Fibres**: residue fibres retain multiplicity; reduction alone is not injective

**Exceptional Locus**: Target set {-1,-p,-p^-1} uses distinct elements only.

**Scope**: Integer energy lower bound on every failed shell; strict reverse extracts witness.

## D12_anchor_packet

**Domain**: R,H,A|a and actual t|a/A outsideH; nd|A,gcd(n,d)=1,n/d=-t^-1 modR

**Codomain**: middle candidate with full p,R,u,h,r,s,lambda

**Map**: g=gcd(d,tn); r=d/g; s=tn/g; h=ag^2/(dtn); u=ad/(tn); lambda=(d+tn)/(gR)

**Inverse**: for each anchor pair t=ds/(nr); require integer t|a/A; g=d/r

**Fibres**: finite fibres over retained anchor pairs

**Exceptional Locus**: Positive chamber sufficient test is tn>8d; not assumed for an arbitrary p.

**Scope**: Improved using exact greatest outside divisor, not subgroup-generated availability.

## D13_cayley

**Domain**: (p,q,D) positive rational candidate

**Codomain**: raw and cleared affine Cayley vectors

**Map**: a=(-p,4q_0,4q_1,4q_2); a_clear=D*a

**Inverse**: q_j=a_(j+1)/4; recover p=-a_0 and D from scales or D05

**Fibres**: projective quotient identifies the pair; raw scale retained

**Exceptional Locus**: All coordinates nonzero; a repeated middle pair remains labelled.

**Scope**: Both lie on e3=0; clearing changes the arithmetic parameter.

## D14_four_faces

**Domain**: ordered raw Cayley coordinates plus one of24 flags (i,j,k,l)

**Codomain**: three ordered face roots plus raw face scale a_i

**Map**: t_iq=-4a_i/a_q; sum roots=4

**Inverse**: a_q=-4a_i/t_iq; same for cleared scales

**Fibres**: singletons with labels, orientation and affine scale retained

**Exceptional Locus**: Labels remain distinct even when numerical roots coincide.

**Scope**: All24flags checked for seven rational/integral candidates.

## D15_factor_normalization

**Domain**: face roots r,s,t with derivative d=-(r-s)(r-t)/4

**Codomain**: linear/quadratic factor pair and Fable coordinates

**Map**: raw L=U-rV, raw Q=-(U-sV)(U-tV)/4; if d!=0, L/d,dQ

**Inverse**: Retain d and companion difference s-t; multiply and read marked roots.

**Fibres**: Selects a typed factor, not an unlabelled cubic root.

**Exceptional Locus**: d=0: retain raw factors and record that normalized chart is unavailable; no division by zero.

**Scope**: Fable chart formulas replayed only on their actual simple-root locus.

## D16_resolvent

**Domain**: raw Cayley vector and companion matching labels

**Codomain**: b=(a0a1+a2a3,a0a2+a1a3,a0a3+a1a2)

**Map**: clearing D scales b by D^2

**Inverse**: Use retained raw coordinates/face maps; b alone not asserted injective.

**Fibres**: resolvent is an observation with retained upstream fibre

**Exceptional Locus**: Coincident b retained on repeated-root strata.

**Scope**: Degree-two scaling checked on all examples.

## D17_trace_lift

**Domain**: integral cleared trace X in Z^3 and k in kerP

**Codomain**: full Leech lambda

**Map**: sigma(X)+k with explicit b0,Cb0,C^2b0

**Inverse**: X=P(lambda), k=lambda-sigma(P(lambda))

**Fibres**: rank21 fibre over X; tested section k=0

**Exceptional Locus**: Do not discard k for subsequent actions by J,T.

**Scope**: Inherited integral inverse; basis membership and right inverse replayed.

## D18_all_octads

**Domain**: full Leech numerator x

**Codomain**: 759 octad traces a_B=sum_B x_i/4

**Map**: S=sum_B a_B, S_i=sum_(B contains i)a_B

**Inverse**: x_i=(23S_i-7S)/1012

**Fibres**: singletons on exact image

**Exceptional Locus**: Linear compatibility and delta=(11S-23S_0)/506=0 mod4 required.

**Scope**: Complete trace inverse/syndrome tested; theorem inherited.

## D19_octonions

**Domain**: full Leech numerator

**Codomain**: three ordered Wilson octonions

**Map**: pinned signed permutation y_i=eps_i x_pi(i), then z_j=(y_(8j+r))/2

**Inverse**: signed inverse numerator permutation

**Fibres**: singletons on image lattice

**Exceptional Locus**: Joint pair/triple lattice congruences checked, not merely norm.

**Scope**: Dictionary pinned; infinite-lattice isometry theorem inherited.

## D20_Albert

**Domain**: Leech state with trace X and ordered z_i

**Codomain**: compact marked Albert matrix

**Map**: diagonal X; off-diagonal z; keep nu=2Re((z0*z1)*z2)

**Inverse**: read off-diagonal entries and signed inverse, then confirm diagonal=P(lambda)

**Fibres**: singletons on specified image

**Exceptional Locus**: Full defect is F_p(X)+sum(p-4X_i)N(z_i)+4nu, not just F_p(X).

**Scope**: All seven numerical cubic correction identities checked.

## D21_operator_transport

**Domain**: bijection f between fully retained state spaces

**Codomain**: labelled multiplication operators

**Map**: H_new=f_* H_old f_*^-1 with multiplier delta o f^-1

**Inverse**: use f^-1

**Fibres**: same success kernels/inverse certificates

**Exceptional Locus**: A noninjective observation needs its fibre; a state-changing operation recomputesD.

**Scope**: Abstract conjugacy proved coordinatewise; not a new existence theorem.
