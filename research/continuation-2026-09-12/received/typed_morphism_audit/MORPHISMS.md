# Typed morphism ledger



Eight locally available mathematical packages; no reconstruction of unavailable conversations or uninspected Git branches.



A many-to-one morphism is allowed. Claims of inverse transport explicitly retain its fibres or prove the target property descends.



## M01 — Divisor to primitive marked ray

**Source:** a>0,u|a^2. **Target:** (h,r,s), gcd(r,s)=1.

**Domain:** positive integers; all available prime exponents 0..2v_q(a).

**Map:** `d=gcd(a,u); r=u/d; s=a/d; h=d/r`.

**Inverse / reconstruction:** a=hrs, u=hr^2.

**Fibres:** singleton.

**Information boundary:** None. Do not replace the exponent box by the subgroup it generates.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:89 (`prop:divisor`)



## M02 — Exterior denominator reconstruction

**Source:** (p,R,u,h,r,s,E,kappa). **Target:** ordered (x,y,z) with retained p,R,E.

**Domain:** p odd prime; 0<R<p; R|pr+s; p+R=4hrs; kappa=(pr+s)/R.

**Map:** `(hrs,hs*kappa,p*h*r*kappa)`.

**Inverse / reconstruction:** u=x^2/(R*y-p*x), then M01; kappa from p,r,s,R.

**Fibres:** singleton on the marked image.

**Information boundary:** Sorting/permuting is not part of this arrow.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:75 (`eq:E`); `inputs/erdos_straus_research/paper.tex`:100 (`eq:Ediv`)



## M03 — Middle denominator reconstruction

**Source:** (p,R,u,h,r,s,M,lambda). **Target:** ordered (x,y,z) with retained p,R,M.

**Domain:** p odd prime; 0<R<p; R|r+s; p+R=4hrs; lambda=(r+s)/R.

**Map:** `(hrs,p*h*s*lambda,p*h*r*lambda)`.

**Inverse / reconstruction:** u=p*x^2/(R*y-p*x), then M01.

**Fibres:** singleton on the marked image.

**Information boundary:** lambda is not exterior kappa.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:83 (`eq:M`); `inputs/erdos_straus_research/paper.tex`:101 (`eq:Mdiv`)



## M04 — Middle orientation quotient

**Source:** oriented middle divisor states. **Target:** increasing denominator triples.

**Domain:** same bounded domain as M03; R odd >1.

**Map:** `u -> min-order of the last two denominators`.

**Inverse / reconstruction:** retain u or an orientation bit to invert.

**Fibres:** exactly two, u and a^2/u.

**Information boundary:** The two marked states must not be counted as two distinct sorted triples.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:128 (`prop:orientation`); `inputs/erdos_straus_research/paper.tex`:133 (`eq:middleinvolution`)



## M05 — Prime-incidence root blocks

**Source:** eligible finite auxiliary-prime set and rays. **Target:** finite joint incidence law.

**Domain:** auxiliary q does not divide coefficients; determinant-collision primes retained; all cutoffs fixed for PNT.

**Map:** `ray (r,s) -> -s/r mod q; group equal roots`.

**Inverse / reconstruction:** Retain ray labels and the entire root block.

**Fibres:** a block may contain several rays.

**Information boundary:** A density result is not an inverse returning a state at each prime.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:193 (`thm:pgf`); `inputs/erdos_straus_research/paper.tex`:533 (`prop:collisions`)



## M06 — Composite residual extraction

**Source:** actual prime-factor occurrences in a residual. **Target:** bounded Omega residual.

**Domain:** original bounded exponent multiset; quotient-group zero-sum bounds 2,3,5.

**Map:** `retain a minimal target-product submultiset`.

**Inverse / reconstruction:** No unique inverse: record deleted occurrences and the source residual.

**Fibres:** all extensions by discarded occurrences satisfying the divisor budget.

**Information boundary:** Existence of a residue in generated support is insufficient.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:259 (`lem:extract`); `inputs/erdos_straus_research/paper.tex`:266 (`thm:235`)



## M07 — Same-shell unimodular companion map

**Source:** state v=(r,s), companion w=(b,d). **Target:** all same-(p,R) exterior rays.

**Domain:** rd-sb=epsilon=+-1; A,RB primitive; new coordinates positive; r_prime*s_prime|a.

**Map:** `v_prime=A*v+R*B*w; kappa_prime=A*kappa+B*(bp+d)`.

**Inverse / reconstruction:** A=epsilon*(d*r_prime-b*s_prime); B=epsilon*(r*s_prime-s*r_prime)/R.

**Fibres:** singleton for chosen basis.

**Information boundary:** Retain p,R,basis and shell divisor test. The ordinary mediant does not preserve R>1.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:548 (`thm:lattice`); `inputs/erdos_straus_research/paper.tex`:555 (`eq:latticemap`)



## M08 — Exterior-to-middle cubic exchange

**Source:** exterior marking. **Target:** middle marking plus square-divisor index g.

**Domain:** g=gcd(h,r); necessary and sufficient R|4r^3-1.

**Map:** `(H,a1,b1)=(s*g^2,r/g,h/g)`.

**Inverse / reconstruction:** for each g: h=g*b1,r=g*a1,s=H/g^2; require g^2|H, coprimality, cubic congruence.

**Fibres:** exact finite g-indexed inverse fibre.

**Information boundary:** Forgetting g can identify two distinct exterior states.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/erdos_straus_research/paper.tex`:581 (`thm:cubic`); `inputs/erdos_straus_research/paper.tex`:600 (`eq:cubicfibre`)



## M09 — Angular anchor packet

**Source:** (p,R,A;t,n,d) from actual divisor boxes. **Target:** positive middle state.

**Domain:** t|a/A, nd|A, gcd(n,d)=1; tn+d=0 mod R; tn>8d; gcd(a,R)=1.

**Map:** `g=gcd(d,tn); (h,r,s)=(a*g^2/(dtn),d/g,tn/g); u=a*d/(tn)`.

**Inverse / reconstruction:** t=d*s/(n*r), with original anchor pair retained.

**Fibres:** all anchor pairs giving integral t; collisions t*n*d_prime=t_prime*n_prime*d.

**Information boundary:** No unbounded exponent lift or positivity surrogate.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/es_pointwise_tranche/tranche.tex`:127 (`eq:packetmap`); `inputs/es_pointwise_tranche/tranche.tex`:163 (`eq:packetinverse`)



## M10 — Exterior shell/hyperbola exchange

**Source:** (p,R,a,u,E). **Target:** (p,k,D,u).

**Domain:** k=(4u+1)/R; all entries positive; R<p; u|a^2.

**Map:** `k=(4u+1)/R; D=(kp+1)/4=k*a-u`.

**Inverse / reconstruction:** R=(4u+1)/k; a=(u+D)/k.

**Fibres:** singleton on the stated congruence/divisor locus.

**Information boundary:** k differs from kappa. Search termination does not imply a nonempty output.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/es_pointwise_tranche/tranche.tex`:464 (`prop:hyperbola`)



## M11 — Ordered Fourier coordinates

**Source:** ordered real triple q. **Target:** (t,zeta) in R direct-sum C.

**Domain:** omega=e^(2pi i/3); retain complex conjugation and slot order.

**Map:** `t=sum(q)/3; zeta=(q0+omega*q1+omega^2*q2)/3`.

**Inverse / reconstruction:** qj=t+omega^(-j)zeta+omega^j*conjugate(zeta).

**Fibres:** singleton.

**Information boundary:** Do not identify vector-space coordinates with componentwise direct-product multiplication.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/three_coordinate_jordan/note.tex`:30 (`eq:fourier`); `inputs/three_coordinate_jordan/note.tex`:35 (`eq:inverse-fourier`)



## M12 — Transported cubic algebra

**Source:** ordered componentwise multiplication. **Target:** star multiplication in Fourier coordinates.

**Domain:** same fields and normalization as M11.

**Map:** `(t,z)*(u,w)=(tu+2Re(z*bar(w)),t*w+u*z+bar(z)*bar(w))`.

**Inverse / reconstruction:** M11 transports multiplication both ways.

**Fibres:** isomorphism.

**Information boundary:** Norm is cubic product; spin-factor c=0 is a different product.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/three_coordinate_jordan/note.tex`:40 (`prop:product`); `inputs/three_coordinate_jordan/note.tex`:84 (`eq:family`)



## M13 — Rational spin inverse

**Source:** Q direct-sum Q(omega), spin product. **Target:** nonzero elements with Jordan inverse.

**Domain:** q=t^2-2Norm(z) is anisotropic over Q; not over R.

**Map:** `(t,z) -> (t,-z)/q`.

**Inverse / reconstruction:** involution on Jordan-invertible elements.

**Fibres:** singleton.

**Information boundary:** Jordan invertibility is not division-algebra cancellation.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/three_coordinate_jordan/note.tex`:127 (`thm:rational`)



## M14 — Full three-input associator

**Source:** source algebra (a,u)(b,v)=(ab+B(u,v),av+bu). **Target:** vector-valued trilinear tensor.

**Domain:** B fixed; output vector space retained.

**Map:** `[a,u;b,v;c,w]=(0,B(u,v)w-B(v,w)u)`.

**Inverse / reconstruction:** retain every output component, or full family ell composed with associator.

**Fibres:** scalar contraction alone has a kernel.

**Information boundary:** 27 input cells for a 3D algebra carry 3 output coordinates: 81 scalar coefficients, not one scalar 27-cube.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:81 (`prop:recovery`)



## M15 — Three marked-face gluing

**Source:** three bilinear faces with compatible shared edges. **Target:** scalar 3x3x3 tensor.

**Domain:** chosen marks e_i and splittings; incompatible shared edges have no lift.

**Map:** `inclusion-exclusion lift T0 plus Q0 tensor Q1 tensor Q2`.

**Inverse / reconstruction:** read faces and subtract T0.

**Fibres:** affine space of dimension eight.

**Information boundary:** Three marked faces do not determine the full cube.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:173 (`thm:glue`)



## M16 — Cube kernel-incidence transport

**Source:** nondegenerate cube plus three typed planes. **Target:** three genus-one curves and maps phi_ij.

**Domain:** rank exactly two along smooth determinant curves; left/right kernels per slot.

**Map:** `phi_ij given by tensor(v_i,v_j,-)=0`.

**Inverse / reconstruction:** phi_ji; retain tensor and all basis changes.

**Fibres:** forgetting tensor or line bundle is not injective.

**Information boundary:** Identical cubic equations do not identify incidence maps or full-turn translation.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:234 (`lem:kernel`); `inputs/cube_unification/note.tex`:271 (`thm:infinite`)



## M17 — Arithmetic-face attachment to cube

**Source:** existing ordered ES witness plus Moore cube. **Target:** integral cube, three basis changes, clearing scale.

**Domain:** rank-two arithmetic face; distinct lattice/arithmetic scale conventions.

**Map:** `Gaussian normalize faces; L A R=M; change all tensor slots and clear denominators`.

**Inverse / reconstruction:** undo each basis change and divide the retained clearing scale.

**Fibres:** singleton with all marks; many cubes without marks.

**Information boundary:** This attaches a known witness, not produces an unknown one.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:716 (`thm:attachment`)



## M18 — Tensor to graded Lie operator

**Source:** T in V0 tensor V1 tensor V2. **Target:** linear D_T on three Hom blocks.

**Domain:** oriented 3D spaces; first-Tits coefficient field fixed.

**Map:** `for pure a*b*c: D(A,B,C)=(b(a cross Cc)^T,c(b cross Aa)^T,a(c cross Bb)^T)`.

**Inverse / reconstruction:** read tensor coefficients from operator entries using epsilon_ijk.

**Fibres:** injective.

**Information boundary:** D_u^2=0 and I+tD_u apply to pure u; not arbitrary sums.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:361 (`eq:Du`); `inputs/cube_unification/note.tex`:371 (`eq:Dinverse`); `inputs/cube_unification/note.tex`:380 (`thm:move`)



## M19 — First Tits to Zorn-Albert coordinates

**Source:** (A,B,C) in three typed Hom blocks. **Target:** H3(split O).

**Domain:** complexification and orientations; fixed multiplication association.

**Map:** `x1=(A23,col1 B,-row1 C,A32), cyclic for x2,x3; xi_i=Aii`.

**Inverse / reconstruction:** read all matrix entries back.

**Fibres:** linear isomorphism of dimension27.

**Information boundary:** Compact real points satisfy A=A*, C=B*. Split transformations need not preserve that real form or the chosen lattice.

**Status:** retained. **Evidence:** original formal-polynomial replay plus new exact Q(i) determining-grid check.

Sources: `inputs/cube_unification/note.tex`:495 (`eq:phi`)



## M20 — Cayley encoding

**Source:** ordered ES state (p;x,y,z). **Target:** (-p,4x,4y,4z) with affine scale.

**Domain:** p positive; denominators positive; e3=0 iff ES.

**Map:** `(-p,4x,4y,4z)`.

**Inverse / reconstruction:** p=-a0, denominators=a_i/4.

**Fibres:** singleton in affine marked coordinates.

**Information boundary:** Projectivization forgets a common scale; retain it.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:784 (`eq:cayleyes`)



## M21 — Reciprocal Cremona map

**Source:** Cayley coordinate torus e3=0. **Target:** projective plane sum ell_i=0.

**Domain:** every coordinate nonzero.

**Map:** `ell_i=product_{j!=i}a_j, equivalently [1/a_i]`.

**Inverse / reconstruction:** same product formula; second application scales by (product a)^2.

**Fibres:** singleton projectively, nontrivial scale affinely.

**Information boundary:** Coordinate hyperplanes are excluded; exceptional divisors not hidden.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cayley_fable_bridge/note.tex`:223 (`eq:cremona`)



## M22 — Four normalized Cayley charts

**Source:** marked Cayley a and face i. **Target:** three roots t_ij plus normalization h_i.

**Domain:** all a_i nonzero, pairwise distinct; h_i=-1/(4a_i).

**Map:** `t_ij=-4a_i/a_j; normalized a_i=-1/4`.

**Inverse / reconstruction:** a_i=(-1/4)/h_i, a_j=1/(h_i*t_ij).

**Fibres:** singleton with face, companion order and scale.

**Information boundary:** Changing face can change positivity. Twelve A4 flags, twenty-four S4 flags.

**Status:** retained. **Evidence:** 72 all-oriented arithmetic flags independently replayed, 432 local factor returns.

Sources: `inputs/tetrahedral_markings/note.tex`:193 (`eq:roots`); `inputs/tetrahedral_markings/note.tex`:204 (`eq:coeffs`)



## M23 — Oriented face exchange

**Source:** oriented roots (r,s,t), sum4. **Target:** new oriented roots.

**Domain:** r*s*t nonzero; none=-4; all distinct inherited from full torus.

**Map:** `J(r,s,t)=(16/r,-4t/r,-4s/r)`.

**Inverse / reconstruction:** J^2=identity.

**Fibres:** singleton.

**Information boundary:** Companion swap is necessary for preserved tetrahedral orientation.

**Status:** retained. **Evidence:** general rational identities and all72 arithmetic flags.

Sources: `inputs/tetrahedral_markings/note.tex`:225 (`eq:J`); `inputs/tetrahedral_markings/note.tex`:231 (`eq:relations`)



## M24 — Derivative/companion coordinates

**Source:** ordered r,s,t. **Target:** (r,d,eta), d=f_prime(r), eta=s-t.

**Domain:** simple root d!=0; eta^2=(3r-4)^2+16d.

**Map:** `r fixed; d=-3r^2/4+2r+beta/2; eta=s-t`.

**Inverse / reconstruction:** s=(4-r+eta)/2; t=(4-r-eta)/2.

**Fibres:** singleton; forgetting eta leaves two companion orders.

**Information boundary:** eta maps to4eta/r under J; its square is insufficient for orientation.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/tetrahedral_markings/note.tex`:254 (`eq:rd`)



## M25 — Ordered roots to cubic coefficients

**Source:** ordered triple of distinct roots sum4. **Target:** (alpha,beta,gamma).

**Domain:** characteristic zero; gamma=-1/2; cubic splits over stated field if rational branches requested.

**Map:** `alpha=product/4, beta=-pair_sum/2, gamma=-1/2`.

**Inverse / reconstruction:** recover unordered roots; retain selected factor and companion eta for ordered inverse.

**Fibres:** 6-to-1 geometrically.

**Information boundary:** Rational coefficients do not imply rational roots.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cayley_fable_bridge/note.tex`:131 (`eq:esbase`)



## M26 — Fable chart to normalized factor pair

**Source:** (u,v,w) in affine3. **Target:** (L,Q), Res(L,Q)=1 and U2V coefficient1.

**Domain:** characteristic zero; factor coefficients retained.

**Map:** `L=uU+(1+uv)V; Q as explicit polynomial chart`.

**Inverse / reconstruction:** u=L_U; v=2 L_V Q_UV-L_U Q_VV; w=-4Q_UV^2-2Q_UU Q_VV-12L_V Q_UV^2-6L_V Q_UU Q_VV+9Q_VV.

**Fibres:** polynomial isomorphism to normalized factor variety.

**Information boundary:** Fable u is not ES divisor u.

**Status:** retained. **Evidence:** polynomial source replay plus432 factor-chart inversions.

Sources: `inputs/cayley_fable_bridge/note.tex`:50 (`eq:factor`)



## M27 — Factor multiplication

**Source:** normalized (L,Q). **Target:** binary cubic coefficients.

**Domain:** Res(L,Q)=1; generic separable cubic has three simple projective roots.

**Map:** `(L,Q)->LQ`.

**Inverse / reconstruction:** choose one simple root; finite root r gives u=1/d,v=-r-d,w=5d^2+3rd-gamma*d^3.

**Fibres:** 3 geometric points off discriminant, 1 over double+simple, 0 at triple root in this chart.

**Information boundary:** Constant nonzero Jacobian is local: it does not supply a global single-valued inverse.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cayley_fable_bridge/note.tex`:56 (`thm:fibres`); `inputs/cayley_fable_bridge/note.tex`:58 (`eq:inverse`)



## M28 — Quarter cubic to arbitrary ES reciprocal cubic

**Source:** three base normalized factors plus ordered roots. **Target:** three transported normalized factors.

**Domain:** roots distinct; matrix M determinant D=4(t2-t3)(t1-t2)(t1-t3)!=0.

**Map:** `L=(8/D)L_star composed adj M; Q=(1/64)Q_star composed adj M`.

**Inverse / reconstruction:** undo both scalars and adj M.

**Fibres:** singleton with M and selected factor.

**Information boundary:** M and two different scale factors must remain; resultant transforms by D^2.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cayley_fable_bridge/note.tex`:171 (`thm:mobius`); `inputs/cayley_fable_bridge/note.tex`:193 (`eq:transportpair`)



## M29 — Tetrahedral pencil states

**Source:** 12 oriented pairs (H,K). **Target:** 3 normalized factors of fixed C_star.

**Domain:** H half-sign tetrahedron; simultaneous A4 action on numerator and denominator.

**Map:** `pick component L and complementary Q, then normalize resultant`.

**Inverse / reconstruction:** retain tetrahedral numerator frame to choose the preimage.

**Fibres:** 4-to-1; 24 states if orientation reversals included.

**Information boundary:** Four frames above each factor are not four geometric preimages of the cubic.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/tetrahedral_markings/note.tex`:130 (`thm:twelve`)



## M30 — Rational projective reduction

**Source:** marked rational projective coordinates. **Target:** P1(F23).

**Domain:** choose primitive integral pair, not both divisible23; denominators treated projectively.

**Map:** `[a:b]->[a mod23:b mod23]`.

**Inverse / reconstruction:** no arithmetic inverse unless original rational lift retained.

**Fibres:** infinite fibres.

**Information boundary:** The three named marks reduce to infinity,12,11. Do not reduce arbitrary complex Mellin values.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:62 (`eq:projective`); `inputs/mellin_leech_research/note.tex`:67 (`eq:cycle`)



## M31 — Abstract flag to projective Leech coordinate

**Source:** oriented A4 flag plus orbit bit. **Target:** 24 named coordinates.

**Domain:** explicit generator matching C,J and base coordinate; order fixed.

**Map:** `branch_table(orbit,u,j)`.

**Inverse / reconstruction:** read table inverse.

**Fibres:** singleton finite label map.

**Information boundary:** This only transports labels. p, denominators, scales and factors are separate retained fields.

**Status:** retained. **Evidence:** original fullfinitechecks and newgenerator-equivariancecomputation.

Sources: `inputs/mellin_leech_research/note.tex`:119 (`eq:labels`)



## M32 — Minimal-vector congruence marking

**Source:** 24 named coordinates. **Target:** 24 classes in Lambda/12Lambda.

**Domain:** v_i=(ones-4e_i)/sqrt8; minimum norm4.

**Map:** `i->[v_i]`.

**Inverse / reconstruction:** read one of the24 marked classes.

**Fibres:** singleton on these24 marks only.

**Information boundary:** The full lattice quotient has kernel12Lambda and size12^24, not24.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:175 (`thm:mod12`)



## M33 — Three integral lattice traces

**Source:** Lambda_G. **Target:** Z3.

**Domain:** three specified octads; no extra congruence condition.

**Map:** `P_j(x/sqrt8)=sum_Bj x_i/4`.

**Inverse / reconstruction:** sigma(t)=sum t_i b_i plus arbitrary k in K21.

**Fibres:** affine rank21 lattice, det64.

**Information boundary:** P alone loses the kernel; the full (t,k) representation is bijective.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/leech_trace_inverse/note.tex`:92 (`thm:inverse`)



## M34 — Shortest integral trace lift

**Source:** t in Z3. **Target:** chosen minimum vector lambda_star(t).

**Domain:** r=t mod4, reduced a_i in{-1,0,1,2};64 classes.

**Map:** `nu_r+sum((t_i-a_i)/4)w_i`.

**Inverse / reconstruction:** P(lambda_star)=t; inverse fibre has all minimizers or fullK21 as selected target dictates.

**Fibres:** section, not a bijection onto Lambda.

**Information boundary:** Tie-break choice need not be symmetry-equivariant. New8-seedproof replaces fullshell enumeration for attainment.

**Status:** retained with shorter standalone proof and strengthened output validation. **Evidence:** old full196560 replay; new8-seed/64classproof; mutation tests.

Sources: `inputs/leech_trace_inverse/note.tex`:126 (`thm:shortest`)



## M35 — Tetrahedral kernel cocycle

**Source:** (t,k) in Z3 direct-sum K21. **Target:** same full-coordinate object.

**Domain:** g in A4, rho_g its induced phase action.

**Map:** `(rho_g t, gk+g sigma(t)-sigma(rho_g t))`.

**Inverse / reconstruction:** apply g inverse and corresponding cocycle.

**Fibres:** singleton.

**Information boundary:** No invariant integral section outside4Z3. Dropping the correction changes the action.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/leech_trace_inverse/note.tex`:201 (`eq:cocycle`); `inputs/leech_trace_inverse/note.tex`:180 (`thm:invariants`)



## M36 — Four-view integral inverse

**Source:** four ordered triples of common sum. **Target:** Lambda_G plus rank15 fibre.

**Domain:** only common sum constraints; original 9-column section fixed.

**Map:** `a=pack first triple plus first2 of other3; lambda=sigma9(a)+k9`.

**Inverse / reconstruction:** all four P(T^n lambda), residual lambda-sigma9(a).

**Fibres:** affine rank15, det5292.

**Information boundary:** All12 T-readings determined; J does NOT descend to this quotient.

**Status:** retained; J-composition boundary added. **Evidence:** fullreplay andnewexplicitK9/Jcounterexample; repairedCLIchecksallviews.

Sources: `inputs/leech_trace_inverse/note.tex`:222 (`thm:nine`); `inputs/leech_trace_inverse/note.tex`:217 (`eq:Tphase`)



## M37 — Golay to Wilson model

**Source:** Lambda_G raw24. **Target:** Lambda_W in O3.

**Domain:** explicit aligned pi,signs; z_j=half rawblock; Wilson normhalf.

**Map:** `y_i=epsilon_i x_pi(i)`.

**Inverse / reconstruction:** x_pi(i)=epsilon_i y_i.

**Fibres:** singleton entirelattice.

**Information boundary:** Previously absent coordinate arrow now supplied. Existing Wilson-MOG isometry is primary antecedent.

**Status:** new coordinate completion. **Evidence:** 37 generating vectors, signed metric identity, unimodularity; allbasis inverse checks.

Sources: `inputs/cube_unification/note.tex`:554 (`eq:wilson`); `inputs/leech_trace_inverse/note.tex`:36 (`eq:leech`)



## M38 — Off-diagonal Albert embedding

**Source:** Wilson Leech O3. **Target:** H3(O_R) with zero diagonal.

**Domain:** three octonionic entries and conjugates in fixed positions.

**Map:** `iota(z)=[[0,z2,bar z1],[bar z2,0,z0],[z1,bar z0,0]]`.

**Inverse / reconstruction:** read ordered off-diagonal entries.

**Fibres:** singleton on image.

**Information boundary:** Preserves quadratic norm with factor4; cubic nu is not trace product.

**Status:** retained with concrete Golay source and norm correction. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:569 (`eq:leechinvariants`)



## M39 — Faithful combined trace-Albert graph

**Source:** lambda in Lambda_G. **Target:** Xhat=diag(P lambda)+iota(Pi lambda).

**Domain:** full graph membership: compact octonions,lattice and3diagonalconstraints.

**Map:** `augment the aligned off-diagonal embedding by its three traces`.

**Inverse / reconstruction:** read all z, invert signed permutation, recompute traces.

**Fibres:** singleton.

**Information boundary:** 4N-pS = F_p(t)+sum(p-4t_i)N(z_i)+4nu. Every correction retained.

**Status:** new corrected interface. **Evidence:** written cubic formulas, exactQ(i) checks, full2600-node determining check.

Sources: `inputs/leech_trace_inverse/note.tex`:262 (`eq:defect`); `inputs/cube_unification/note.tex`:333 (`eq:titsnorm`)



## M40 — Albert coordinates to27linevariables

**Source:** three3x3typedblocks. **Target:** 27independent labeled scalar variables.

**Domain:** specific ordered bijection in source; char0.

**Map:** `dictionary gives45signed normmonomials matching45tritangent triples`.

**Inverse / reconstruction:** read matrix entries by labels.

**Fibres:** singleton coordinate map.

**Information boundary:** Not an isomorphism of the cubic surface with27-dimensional affine space. Weyl lifts may retain signs after permutations return.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cayley_fable_bridge/note.tex`:261 (`eq:blocks`); `inputs/cayley_fable_bridge/note.tex`:272 (`thm:dictionary`)



## M41 — Full orbit trace completion

**Source:** lambda in Lambda_G. **Target:** a_B for all759octads.

**Domain:** explicit linear imageequations and exactmod4syndrome.

**Map:** `a_B=sum_B x/4`.

**Inverse / reconstruction:** x_i=(23 S_i-7S)/1012; latticeimage iff(11S-23S0)/506=0 mod4.

**Fibres:** singleton.

**Information boundary:** Smallest real stable span under<J,T> has rank24; no9-dimensional fullgroupquotient.

**Status:** new integral reconstruction theorem. **Evidence:** 759orbit,Gram576,24minor det2^14, allintegerdualquotientproof.

Sources: `inputs/leech_trace_inverse/note.tex`:222 (`thm:nine`); `inputs/mellin_leech_research/note.tex`:88 (`thm:groups`)



## M42 — Vector theta Fourier return

**Source:** Lambda/12Lambda theta packet. **Target:** same packet after tau or t inversion.

**Domain:** fullfinite module size12^24, bilinear pairing mod12; preserve Jacobi variable z for classidentification.

**Map:** `F_ab=12^-12 exp(-2pi i(a,b)/12)`.

**Inverse / reconstruction:** F^2 sends a to -a.

**Fibres:** invertible on fullpacket; selected24marks notclosed.

**Information boundary:** Setting z=0 canidentifyisometriccosets; selecting24classes losesFouriersupport.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:384 (`eq:vectorTheta`)



## M43 — Mellin transform of literal source kernel

**Source:** E h with h=(pi²x4-3pi x²/2)e^-pi x². **Target:** xi(s+1/2)/4.

**Domain:** sourceconvention u^(s-1); finitekernels and centeredstrip asstated.

**Map:** `M(Eh)=xi/4; normalizedsource is4Eh`.

**Inverse / reconstruction:** Mellin inversion requires analyticdomain/growthandalltransformdata; no pointwise inverseclaimedhere.

**Fibres:** not a finiteprojectiverootmap.

**Information boundary:** Completion marks +-1/2 are not xi zeros; infinity is chartmark notintegralsubstitution.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:42 (`prop:normalization`)



## M44 — Residue-valued arithmetic kernel

**Source:** all positive integers n and residueoperators. **Target:** matrix Mellin Dirichlet packet.

**Domain:** R_n=0 for gcd(n,12)>1; actualn retained.

**Map:** `B(u)=4sqrt(u) sum R_n h(nu)`.

**Inverse / reconstruction:** retainall4characterprojections andphases; restore2,3 factors byfull2^a3^b sum.

**Fibres:** discardingcharacters losescomponents.

**Information boundary:** Finite projective labels are not arithmeticvalues; imprimitivefactors and conductorsretained.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:231 (`thm:dirichlet`); `inputs/mellin_leech_research/note.tex`:250 (`eq:restore`)



## M45 — Leech theta centeredkernel

**Source:** selfdual positive definite lattice rank2kappa. **Target:** entire even Mellin function.

**Domain:** Psi=u^1/2 Theta(u^1/kappa); zero-modekilled; Leechkappa12.

**Map:** `K=1/2(D²-1/4)Psi; w=kappa(s+1/2)`.

**Inverse / reconstruction:** retainfulltheta coefficients/analyticdata, notjustendpointvalues.

**Fibres:** spectral scalar observations canlose vectorcosetlabels.

**Information boundary:** Leech transform has zeta(w)zeta(w-11)-L(Delta,w), not Riemannxi.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:316 (`thm:theta`); `inputs/mellin_leech_research/note.tex`:361 (`eq:LeechM`)



## M46 — Finitekernel approximation

**Source:** h_lambda compact approximation with explicitC. **Target:** Mellin B_lambda converging on closed substrips.

**Domain:** epsilon>0, stated herror; retaintailandendpointestimates.

**Map:** `sourcefinitekernelconstruction`.

**Inverse / reconstruction:** no spectral inverse toWeillowesteigenfunctionproved.

**Fibres:** N/A analyticestimate.

**Information boundary:** Kernelapproximation is not eigenfunctioncomparison or RHproof.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/mellin_leech_research/note.tex`:257 (`thm:error`)



## M47 — Terzo exponential evaluation

**Source:** free exponential-ring quotient A. **Target:** complexnumbers.

**Domain:** specified relations; injection requiresSchanuel, notusedunconditionally.

**Map:** `evaluate(X,Y)=(pi,i)`.

**Inverse / reconstruction:** kernelJ; cube evaluation kernelJ^27.

**Fibres:** unknown unconditionalkernel.

**Information boundary:** Period subgroupZ varpi injects byordinaryevaluation, but fullringfaithfulnessconditional.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/cube_unification/note.tex`:882 (`eq:periodmap`)



## M48 — Arithmetic cubic selection

**Source:** complete positiveintegraltracefibres. **Target:** ESsolution locus.

**Domain:** p prescribed prime; Fp=0 actualequation; allmarks inherited.

**Map:** `select t>0 with 4t0t1t2=p pair_sum`.

**Inverse / reconstruction:** selector reconstructionwhenboundedmarkexists; no universal producerproved.

**Fibres:** each t hasfull latticekernel-fibre.

**Information boundary:** Surjectivity ofP doesnotestablish existenceoft withFp=0.

**Status:** explicit unresolved existence arrow. **Evidence:** written source and bounded original replay.

Sources: `inputs/leech_trace_inverse/note.tex`:262 (`eq:defect`); `inputs/cube_unification/note.tex`:804 (`prop:prime-return`)



## M49 — Fixedmodulus Selberg conclusion

**Source:** fixedrayfamily andactualprimefactoroccurrences. **Target:** explicit exceptional-count theorem.

**Domain:** allowedprime restriction applies to every prime/divisor sum; square majorant before CRT; fixedfamily constants.

**Map:** `count exceptions to existence of bounded residual`.

**Inverse / reconstruction:** notapointwise inverse; no movingmodulusPNT silentlyused.

**Fibres:** N/A countingtheorem.

**Information boundary:** No finitecomputation or densityone leap to universal selector.

**Status:** retained. **Evidence:** written source and bounded original replay.

Sources: `inputs/es_pointwise_tranche/tranche.tex`:556 (`app:sieve`); `inputs/erdos_straus_research/paper.tex`:456 (`thm:small`)


