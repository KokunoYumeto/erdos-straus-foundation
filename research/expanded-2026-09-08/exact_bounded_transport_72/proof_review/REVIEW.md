# Independent mathematical proof review

The current fifteen-source, 72-statement version has no unresolved error found in this bounded review. This record author independently read all ten final reverse statements and all four final boundary statements without editing their mathematics; precise authorship, separate reviewer scope, and repair provenance are recorded below. Earlier accepted review is carried forward only for unchanged proofs. The prior47-statement pass missed an exterior orientation and an incorrect pCD numerator; PR-006/007 preserve those failures. PR-008/009/010 record the completed distribution, coordinate-typing and full projection-fibre repairs; PR-011 records the lower integral hit precision repair.

Reviewed 72 labelled theorem statements in full, including all their proofs, in the fifteen files below. Exact SHA256 digests identify the reviewed versions.

- `bounded_transport.tex`: `4356f53962f2da9b418e066f2c2ca1ba9572e45dc398bb2ca4d37981301e5050`
- `connes_reading/connes_primitive_intersections.tex`: `77023419fd8d1dba895c7b4f765b294d86caacd748f13e6c16be4a07c211ea8c`
- `exact_audit/fixed_y_successor.tex`: `181e6b50dab2adb1b33de0cc9df0dafda97cb84ab37b5409fd778d41022c050f`
- `unary_boolean_transport.tex`: `6ee796fbc0a9ac286f9372e8f7345728dd8f785913dd79211e422ebdcf55af57`
- `shared_variable_crt.tex`: `5637c0026d294db133ba4c2d16eadd6c15d3a1f7fcf60c15e2d59f7b1b284c6b`
- `integral_cyclic_bridge.tex`: `49d4f511f86e5ca9429b0fb44b916ed0684241cd0f31181737bb04f29cdd1d85`
- `input_output_incidence.tex`: `e7b09ec144f78f7507cdf87df2022fbb8651e5f7d491a5f7895a000b21fe4861`
- `first_two_shell_sieve.tex`: `55b0653488fca8cd60c78b0d702d637a81f982e5f3ca797155777633fec96f7e`
- `raw_scale_hit_incidence.tex`: `fbc86a3f127448b797d51bb99441c209340278e1bcf942135c77b6ba49306442`
- `counterexample_sieve/all_shell_no_hit.tex`: `f440b496cf8298657b4bb17d2d97a12ce3392ca14ad09cb20859e97edbb608f2`
- `ns_operator_bridge/torus_cover_lemma.tex`: `4f4fae9611f87d10896b6019342370d11f9d35e8f9a5a90bde844cd7dfd66704`
- `ns_operator_bridge/sieve_character_cover.tex`: `916d7bc2a16d681c223de5f73330378f1babf70f7f4c0d657a93926deb5aae3c`
- `ns_operator_bridge/reverse_proof_transport.tex`: `cf42ea9475aecd08268d1af5795fcbec92ca62b67d3ec0f73ddb04e187c74d62`
- `ns_operator_bridge/reverse_smooth_inverse.tex`: `b9083db518d98550f2bd9928a0fbbc061d3a70ee846441774ce331be5288ad5b`
- `boundary_swap/boundary_swap_completion.tex`: `aa2af846808a077ce951d279da4249df742ab18c4e0d0f1880a47c3a675c60dc`

## NS operator and ordered-return verification

The repaired no-hit checker independently compares all original (pa)^2 passing residual divisors with the complete oriented chart; a fresh read-only replay through p<=5000 passed 16,815,504 divisors and 14,120 ordered witnesses with branch counts (5037,4046,5037). The torus checker uses exact rational points and cyclotomic remainder arithmetic; the character checker retains full monomials, all correction cosets and finite histories. Source and checker hashes are embedded in review.json and checked by validate_review.py.

The literal integer matrix J=((3,1),(1,5)), original eigenvectors/eigenvalues and unit-period torus operator from section6.1 equations6.1-6.7 and lemma6.2 equation6.19. All operator and finite arithmetic conclusions are proved in the local sources; no fluid existence or blowup theorem is used as a hypothesis.

Reviewer read both complete local bridge proofs, the repaired no-hit source, ORDERING_REPAIR.md, complete ATTRIBUTION.md, and SOURCES.json. Primary attribution/receipt checks belong to their named source-audit author; only the two delimited operator passages were compared across PDF revisions. Neither entire PDF is certified equivalent or independently proved.


## Resolved finding PR-001

The preamble originally imposed positive integer coordinates and positive determinant but did not expressly impose primitivity of both input vectors. The proof requires both.

V=(2,2), W=(1,2) has D=2, but det(V,E)=2(E_2-E_1) is even for every integer E, so it cannot equal1.

Parent added that all generators are primitive vectors and that primitivity is an explicit hypothesis of the subdivision lemma. Original norm endpoints and every recursively inserted generator are primitive. The correction makes the general lemma match every intended application.

## Resolved finding PR-002

The first extension gave the exact L affine map but ended with an implicit assertion that the J version follows by coordinate exchange. The required reciprocal-coordinate conjugation and its domain were not yet stated.

At p1753,a440,m20,c1 the J divisor return is u22 to v21. Raw Psi_{193600,194481,1}(1/22)=419/9261, which is not1/21. Thus the same uncomplemented affine formula would be false on the J-oriented divisor.

The parent added iota_N(x)=1/(Nx) on the positive reciprocal-divisor locus and computed iota_M Psi iota_N(x)=x/(1-cx), with exact domain u|N,u>c,u-c|M, label inverse v maps to v+c, and the mu-complement identity proving J=PLP. The final source fully specifies both L and J arithmetic maps and retains the correct original denominator ordering. The initially displayed L theorem itself was correct.

## Resolved finding PR-003

The initial raw-domain phrase called the entire tuple (A,B,C,D,epsilon) positive integer while also requiring epsilon in{0,1}. Literal positivity would remove the exterior tag0.

The actual p13 tuple(2,1,5,2,0) satisfies80=2+13+65 and a4 in the original range but has epsilon0.

The parent explicitly defined A,B,C,D in Z>0 and epsilon in{0,1}. Both original channels now belong to the typed domain exactly as used by the proof and fixtures.

## Resolved finding PR-004

The initial chi_H definition and generic radix statement referred to fixed seed coordinates, leaving their variable scope on an arbitrary decoded code implicit.

At p13 the fixed seed(2,1,5,2,0) passes, but the PCT code0 decodes(A,j,B,epsilon)=(1,0,1,0) and fails3|14. Fixed seed tests cannot define the total code bit.

The parent explicitly defined R(c)=4j(c)+3,a(c)=(q+R(c))/4, all three tests on A(c),B(c),epsilon(c), and the generic full-to-PCT map using its own decoded first denominator and four digits. The total indicator, least-hit selector, sentinels, layer bounds and radix correspondence now share the same fully defined code domain.

## Resolved finding PR-005

The parent identified that the raw ray source named d=Rz-S whereas the main original reconstruction names d=Ry-S. These orientations were initially assigned the same unqualified name.

At p13, a4,y20,z130, the original d_y is8 while d_z is338; these are distinct and multiply to52².

The parent retained d_y,d_z separately, identified original d=d_y and source(d,e)=(d_z,d_y), and proved the complement maps with productS² and the coordinate-swap involution. The exact typed exchange preserves both original ordered triples and both source conventions with singleton fibres.

## Resolved finding PR-006

The prior source claimed a unique d=p^epsilon*u representation with epsilon in {0,1} for every ordered witness. Original d_y has p-adic exponent 0, 1, or 2. The unswapped exterior chart therefore omits its opposite orientation. The prior 47-statement pass failed to detect this mathematical error.

At p=13,a=4, (4,130,20) has d_y=338=13^2*2, and (4,468,18) has d_y=1352=13^2*8. Both passing ordered witnesses were omitted by the unswapped exterior chart.

The source now retains exterior sigma in {0,1}; it gives the full inverse at each i=v_p(d_y): (0,a^2/d_y,0), (1,pa^2/d_y,0), (0,d_y/p^2,1). It proves both inverse compositions, every gate equivalence, the exact middle-complement swap, and all order-forgetting fibres. The all-shell emptiness criterion survives; the full ordered correspondence is now actually proved. The repaired checker independently enumerates every original S^2 divisor and compares the complete ordered image, detecting precisely the branch the old review missed. Historical reports remain preserved, not silently replaced.

## Resolved finding PR-007

The prior common-denominator identity printed (pABCD)/a=pCD although a=ABD forces the quotient pC. The prior pass accepted an incorrect displayed calculation.

At p=13,a=4,u=2, the exterior chart is (A,B,C,D)=(2,1,5,2). Then pABCD/a=65=pC whereas pCD=130.

The source explicitly computes pC+p^(1-epsilon)B+A=4ABCD from (4ABD-p)C=A+p^(1-epsilon)B with no suppressed factor. The intended 4/p reciprocal identity is now correct with its original denominators, constants and tags. PR-007 records an actual calculation repair separately from the orientation repair.

## Resolved finding PR-008

The incoming sharp inverse statement extended its coefficient argument to distributional solutions without the complete test-functional realization and uniqueness argument required for that type change.

This was a missing proof bridge, not a false numerical estimate: an array assertion alone does not define a continuous functional on the specified smooth test space or prove that zero coefficients force that functional to vanish.

The source now states the exact H^(s+q)_0 datum domain and complex-linear distribution convention, proves polynomial coefficient growth and an explicit C^M pairing bound, computes the differentiation sign, and proves uniqueness through convergence of smooth Fourier sums in every seminorm. The inverse conclusion now reaches actual distributions with its full equation and zero-mean uniqueness. The original analytical constants and Pell proof remain unchanged. The initial source is preserved in the 58-statement history.

## Resolved finding PR-009

The source update used one inverse symbol across the common chart and absolute auxiliary coordinate before proving the typed coordinate conversion and all of its scale factors.

For common character e_k(y), its absolute pullback has frequency (J^i)^T k and derivative multiplier T_g^i 2*pi*i(v_t dot k). Treating the two directional inverses as the identical coordinate operator omits the factor T_g^-i.

S17 now defines Y,y,P_i,D_v^Y,D_v^y,T_v^Y,T_v^y,Pi_Y and Pi_y; proves Haar, derivative and inverse covariance on every original character; and derives P_i Delta v=-Q^-1-h T_t^Y P_i E_theta^circ with its original minus sign. The desired and actual axial increments retain A1 and the slow derivatives. The stronger inverse estimate is now mapped exactly to the actual source mean-correction coordinates, without erasing the cutoff remainder or claiming the complete PDE theorem.

## Resolved finding PR-010

The initial transfer proof supplied the projection compositions and the complete P_m and L_m fibres, but did not expressly give every Q_m fibre despite claiming every operator fibre.

This was a completeness omission, not a counterexample to the compositions: arbitrary target h outside the fixed-point image has empty Q_m fibre, while a fixed target has an entire affine kernel coset.

The final theorem and proof explicitly establish ker Q_m=ker L_m and Q_m^-1(h)=h+ker L_m if Q_m h=h, with empty fibre otherwise, using P_m injectivity and subtraction. All three transfer operators now have the complete typed fibres promised by the statement. The read-only transfer reviewer requested and independently rechecked this addition.

## Resolved finding PR-011

The drafting review required the exterior code-decrease sentence to state that the returned lower record is an integral hit only on the calculated shell gate. The rational candidate code itself is lower whenever A0>B0.

At p=373,R=7 the exterior records with (A,B)=(19,1) and (5,1) have lower swapped candidate codes, while their forced swapped coefficients 7088/7 and1866/7 have exact denominator7 and hence do not give integral hits.

The theorem now says that the same-tag swap gives a lower integral hit exactly on R|p^2-1; outside it the exact rational companion and its nontrivial obstruction remain. The proof retains the complete code-difference formula and the independent integrality table. The orbit-minimum conclusion now explicitly compares actual hits. The complete failed integral fibres and rational relation survive; no occupancy or new witness is inferred from a smaller arithmetic code alone.

## Theorem-by-theorem reasoning

### `lem:units` — pass

Locator: `bounded_transport.tex`, line 49.

Primality and 0<a<p prove gcd(R,pa)=1. From Ryz=pa(y+z), the two positive integers d=Ry-pa and d*=Rz-pa have product (pa)^2. Reduction of d/(pa) gives valuations max(c-b,0) and max(b-c,0), each at most b, with exclusive support. Multiplication by n/(pa) is legitimate in the residue unit group and yields R|(m+n). Conversely the displayed denominators are integral and positive because n,m|pa and k=(m+n)/R>0. Both inverse compositions follow from d=pa*m/n and uniqueness of reduced positive fractions. Ordered coordinates are retained.

### `thm:glue` — pass

Locator: `bounded_transport.tex`, line 243.

The diagonal map has precisely the intersection kernel. The difference map is well defined modulo K_D+K_E and is onto via ([z],[0]). If x-y=k_D+k_E, e0=x-k_D=y+k_E gives both classes; all common lifts differ by K_D intersect K_E. This proves middle exactness and every fibre, not merely necessity. For negative exponents, clearing a denominator prime to D and E proves K_lcm=K_D intersect K_E. The original box remains an intersection with that coset. Local targets are explicitly restricted to the respective images, and finite-order enumeration below the theorem computes image membership and bounded lifts.

### `prop:crt` — pass

Locator: `bounded_transport.tex`, line 303.

For g=gcd(D,E), the formula w=r+D*(v*(s-r)/g modulo E/g) reduces to r and s exactly. D/g and E/g are coprime, including the vacuous modulus-one case. Two lifts differ by lcm(D,E), and a lift is a unit exactly when both residues are units. This establishes the stated ring and unit fibre products. No assertion makes their full residue image equal to the exponent image.

### `prop:nonzero-obstruction` — pass

Locator: `bounded_transport.tex`, line 379.

At p=241,a=64 the supplied prime and shell checks are correct. The exponent box is j=0,...,12. Both E/M targets are 11 modulo15, so modulo3 j is odd while modulo5 j is 0 modulo4. The image kernels are 2Z and 4Z. Local lifts 1 and0 give class1 in Z/2Z, while ordinary residues have the common class11 modulo15. This proves an actual integral-exponent obstruction before imposing the finite box.

### `prop:local-counterexample` — pass

Locator: `bounded_transport.tex`, line 411.

All fifteen divisors of324 and all four local E/M hit sets were recomputed exactly. Each same-channel intersection is empty. The integer exponent lift (5,1) has value96 and satisfies both exterior residue conditions, so its integral obstruction is zero; its bounded fibre is empty. The coordinate CRT lift (22,13) has the required two local primitive residues and is primitive, but its forbidden primes cannot supply a bounded lift because Section1 classifies the complete empty E/M shell. The stated full CRT fibre is a fibre of residue reduction, not a claim that every representative is primitive or positive.

### `thm:divisor-crt` — pass

Locator: `bounded_transport.tex`, line 515.

All upper divisor constraints intersect by gcd and all mandatory factors by lcm. Failure f|N is decisive; otherwise unique factorization gives exactly d_l<=j_l<=e_l. Dividing each affine congruence by gcd(c_i,M_i) is reversible exactly when that gcd divides b_i. The reduced coefficient is a unit; when c_i=0 the algorithm correctly keeps only M_i|b_i and a modulus-one condition. Successive CRT uses the full previous lcm, not merely pairwise choices. Multiplication in the full residue monoid retains zero and nonunits and counts labelled exponent choices without cancellation. Distinct prime exponent vectors give distinct positive integers. Thus coefficient extraction and stored choices solve the entire bounded fibre, including N=f=1, no congruences, negative coefficients, and arbitrary noncoprime moduli. The interval1<=u<=N is used only together with, and never instead of, the valuation box.

### `thm:ratio` — pass

Locator: `bounded_transport.tex`, line 694.

A positive ordered shell pair is uniquely determined by its ratio. The rational scaling b*R_a/(a*R_b) is positive and has the displayed inverse and composition law. Integrality at both ends is equivalent via lem:units to the same reduced pair dividing both supplies and satisfying both sum congruences. Their supply gcd is p*gcd(a,b), and their sum modulus is the lcm. Every budget is a coordinatewise minimum. For b=a+d, oddness of R_a proves gcd(R_a,4d)=gcd(R_a,d). The rational scaling factor itself need not be an integer; the proof correctly checks integrality through both reconstructed pairs.

### `cor:adjacent` — pass

Locator: `bounded_transport.tex`, line 740.

Consecutive a have gcd1 and their odd residuals differing by4 are coprime. Hence the entire common supply consists of the primitive pairs(1,1),(p,1),(1,p). The first is excluded by R>=3. The other two pass exactly when R(R+4)|p+1; this proves both directions, exact cardinality, denominator formulas and height bound. The p769 example and prime trial-division list are correct.

### `prop:no-shear` — pass

Locator: `bounded_transport.tex`, line 793.

For either unimodular positive shear the new coordinate is m+n, divisible by R. It cannot divide S because gcd(R,S)=1 and R>=3. The unchanged gcd remains1, so no cancellation can restore membership in the original primitive supply. This excludes precisely the specified maps.

### `thm:shear` — pass

Locator: `bounded_transport.tex`, line 806.

If both adjacent sheared pairs pass, their unchanged coordinate divides gcd(pa,p(a+1))=p. The possibility p is ruled out because the other new coordinate is prime to p and exceeds a+1. The same size argument excludes p|m. Thus n=1,m|a,m+1|a+1, with exactly the two stated residual conditions. Solving4k=1 moduloR+4 gives k=(R+5)/4+(R+4)t; positivity excludes negative t. Solving a=mr and m+1|a+1 gives r=1+c(m+1), with positivity excluding negative c. These steps are individually reversible; R and a recover t,c uniquely. Prime specialization and both shell bounds are explicitly retained. The J case follows by exact coordinate exchange.

### `cor:family` — pass

Locator: `bounded_transport.tex`, line 863.

The family takes R=7,m=20,t=0 in the classification, with a=20+420c and p=73+1680c. The stated h=6+140c and bounds contain both a and a+1 for every c>=0. Divisibility20|a and21|a+1 and sums21,22 prove both witness marks. The c0 triples are exact. The result retains primality and does not assert infinitude in this progression.

### `thm:no-two-shears` — pass

Locator: `bounded_transport.tex`, line 893.

The graph includes only forward adjacent L/J transitions with actual primitive witnesses at every vertex. An L edge ends at(m+1,1), whose first coordinate exceeds1, so it cannot start a J edge; coordinate exchange excludes J then L. Two L edges would have pairs(m+i,1) at(a+i),i=0,1,2. Divisibility m+i|a+i forces each m+i to divide K=a-m, hence3|K. Each residual R+4i divides m+i+1 and therefore divides the same integer C=4(m+1)-R=p+4-4K. One residual is divisible by3, so3|C, whereas p=1 modulo3 and3|K give C=2 modulo3. This contradiction excludes LL; conjugation excludes JJ. Simultaneous outgoing L/J would require the forbidden pair(1,1); incoming L/J require opposite strict coordinate inequalities, and each inverse is unique. Thus indegree and outdegree are at most1, and no vertex can have both, proving that every nontrivial component is exactly one directed edge. The existing p73 edge proves sharpness. This does not exclude matrix words whose intermediate coordinates leave the arithmetic vertex domain, or the separate fixed-y map.

### `lem:split` — pass_after_repair

Locator: `bounded_transport.tex`, line 1024.

The final preamble explicitly assumes both primitive positive integer generators. With that hypothesis, extend V to an integral oriented basis(V,E0); the coefficient of E0 in W is D. Reducing the V coefficient moduloD gives the unique r,E, and primitivity of W forces gcd(r,D)=1, so r is nonzero for D>1. The positive combination for Z proves interiority, determinant1 proves primitivity, and the right determinant is D-r. The coefficients of V,W in Z sum to at most1, proving the coordinate maximum invariant. Recursive determinants decrease and the induction1+(D-r)<=D proves the leaf bound. Without the repaired hypothesis the statement was false, as recorded in finding PR-001.

### `lem:marked-finite` — pass

Locator: `bounded_transport.tex`, line 1077.

The second column gives exactly the closed integer interval for t. Substitution of q=4bk-e into qt-pk=1 gives (4bt-p)k=et+1>0, so the finite positive divisor parameter and congruence follow necessarily. Conversely delta congruent to -p modulo4t gives positive integral b, and t(4bk-e)=pk+1 proves positive integral q as well as determinant and mark. Slope tests recover both columns in the cone. The inverse keeps e,t,k,b,q and is unique. Multiplying the reciprocal identities by pbkt gives pt+pk+1 for e=p and pk+t+1 for e=1, exactly the derived equations. The two reconstructed triples keep their stated denominator order.

### `thm:orchard-partition` — pass

Locator: `bounded_transport.tex`, line 1124.

A determinant-one return has q/k>p/t. For a strict splitter between these slopes, the integral-basis coefficients A=ct-dp and B=qd-kc are positive integers. Then c=Aq+Bp>=q+p>p, contradicting the splitter bound c<=p. Therefore both columns lie in one closed child. They cannot belong to both children, since both would then lie on their common ray and have determinant0. The original positive norm coordinates satisfy u,x<p for p>2; the repaired subdivision preserves their coordinate maximum, so every actual splitter meets the bound. Repeated unique child assignment is a disjoint union over all leaves. Because all return tuple coordinates remain unchanged, every predicate on that tuple, including denominator-budget marks, restricts the same disjoint union. This establishes exact count-preserving localization, not new occupancy of every leaf.

### `prop:affine-point` — pass

Locator: `bounded_transport.tex`, line 1279.

On the actual embedded set H_N each x=e/N has image(e-c)/M; every f/M has the unique inverse(f+c)/N. Hence the full map is an affine bijection with the stated inverse and singleton fibres. Its zero fibre is exactly{c/N}, and its positive-image domain is exactly Nx>c. Since its zero image is-c/M, it is additive exactly for c=0; the zero fibre is correctly not described as a homomorphism kernel when c is nonzero. For a reciprocal divisor u=N/e, positivity and integral reciprocal return are exactly e>c and e-c|M, with e|N retained from the original box; this is precisely the finite index intersection Div(N) intersect(c+Div(M)). Direct affine composition adds c+d. After restriction to reciprocal divisors, the intermediate positive divisor e-c of M is an additional necessary and sufficient condition alongside the source and final budgets; endpoint composition never removes it.

### `thm:full-connes-shear` — pass

Locator: `bounded_transport.tex`, line 1339.

Every classified L edge has a=m+c*m*(m+1),b=a+1 with m|a and m+1|b. Thus u=am divides a^2 and v=b(m+1) divides b^2. Their gcd reductions give mu_a(u)=(m,1),mu_b(v)=(m+1,1); their middle marks become the original sums m+1 and m+2 using the retained unit factors a,b. The reciprocal indices are e=a/m=1+c(m+1),eprime=b/(m+1)=1+cm, so e-eprime=c and Psi(1/u)=1/v exactly. Positivity and both divisor budgets are established by these identities, not by an assumed lift. The uncorrected map has the intended return exactly at c=0. For c>0, e>1 divides a and gcd(a,b)=1, so e cannot divide b^2; therefore the uncorrected image has no positive reciprocal integer return at all. The subsequent fully explicit J conjugation is reviewed separately among the unlabelled calculations.

### `prop:connes-finite-return` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 43.

The union already includes1/N Z and every other summand lies in it. A reciprocal1/d belongs exactly when d divides N, recovering the full positive finite budget. Bezout applied to Nx,Mx establishes the intersection1/gcd(N,M) Z. The sum is generated by (M/g)/L and(N/g)/L, whose coprime integer coefficients generate1/L. The sum-map kernel is exactly(t,-t) with t in the intersection, and all fibres are translates. Inclusion is equivalent to N|M by testing1/N.

### `thm:connes-common-pairs` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 106.

The embedded intersection has supply gcd(pa,pb)=p*gcd(a,b). Taking coordinatewise reciprocals is injective and has the stated inverse on positive reciprocal integers; it preserves primitive integer labels exactly. The sum must be divisible by both residuals, equivalent prime by prime to their lcm. This proves precisely the same common-pair set as thm:ratio, now through the specified embedded additive groups.

### `prop:connes-pair-witness` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 148.

Primitivity and m,n|S give mn|S; the retained mark gives(m+n)/R positive integral. Therefore the scalar k=(S/mn)*(m+n)/R and both ordered denominators are positive integers. In the inverse, y=km,z=kn with k=gcd(y,z) gives R*k*m*n=S*(m+n). Since gcd(mn,m+n)=1, mn|S, and since gcd(R,S/mn)=1, R|(m+n). The same equation uniquely forces k. This matches the root reconstruction, where its different symbol k_root=(m+n)/R is not confused with the denominator gcd used here.

### `cor:connes-consecutive` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 198.

The embedded common supply is H_p. Its reciprocal labels1,p give exactly the three primitive ordered choices, with(1,1) excluded by R>=3. Coprime residuals force R(R+4)|p+1. The denominator formulas agree exactly with cor:adjacent and retain orientation.

### `prop:connes-abstract-loss` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 224.

A positive ordered-group isomorphism must send the least positive generator1/N to1/M, proving uniqueness of x maps to(N/M)x. For u=N/e, its reciprocal image e/M is an integer reciprocal exactly when e divides M; jointly e|N,M gives the complete returned subset and inverse. For primitive shell pairs write a=dk,b=dell with gcd(k,ell)=1. Integral labels(b/a)m,(b/a)n force k|m,n, hence k=1; primitive output then forces ell=1. Thus the coordinatewise isomorphism returns an integral primitive pair only for a=b. The isomorphism-class fibre is explicitly a relation on embedded finite objects, not misidentified as an additive kernel.

### `prop:connes-middle-return` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 285.

For u|a^2, subtracting min(j,e) from valuations gives the positive and negative parts within0,...,e and with exclusive support. Conversely u=am/n and a^2/u=an/m are integers for primitive m,n|a; writing a=gn gives gcd(u,a)=g. Thus the maps undo each other. The equality u+a=g(m+n), with gcd(g,R)=1, proves both directions of the middle mark. Substitution into the full primitive reconstruction gives the stated p(a+u)/R and p(a+a^2/u)/R and ratio u/a exactly.

### `thm:connes-marked-successor` — pass

Locator: `connes_reading/connes_primitive_intersections.tex`, line 325.

Consecutive a have coprime squares, so the reciprocal-divisor domain of the specified ordered-group isomorphism is only a^2 maps to(a+1)^2. An R=3 modulo4 has a prime divisor q=3 modulo4; a square root of-1 moduloq would create an order4 subgroup of the nonzero residues, impossible because4 does not divide q-1. Hence neither top divisor is E-marked. Their M marks reduce using gcd(a,R)=1 to R|a+1 and R+4|a+2, equivalently both residuals divide p+4. Coprimality gives exactly R(R+4)|p+4. The primitive maps send the top divisors to(a,1),(a+1,1), which are related by the original L shear. All denominator formulas agree with exact reconstruction. The quotient(p+4)/(R(R+4)) is positive and1 modulo4, giving unique t>=0; the displayed inequality proves both shell bounds. This is exactly c=0 in thm:shear, not the coordinatewise primitive isomorphism excluded in prop:connes-abstract-loss.

### `thm:exact-audit-fixed-y` — pass

Locator: `exact_audit/fixed_y_successor.tex`, line 19.

Subtracting the two original shell equations with y fixed forces1/zprime=1/z+1/[a(a+1)]. Thus the positive rational map is unique and satisfies0<zprime<min(z,A). The factorization(A+z)(A-zprime)=A^2 proves integrality exactly when A+z divides A^2 and gives the full reverse domain0<zprime<A, A-zprime|A^2. The two rational inverse formulas compose to identity. The original ratio identity y=pa(1+tau)/R gives tauprime=[a(R+4)tau+p]/[(a+1)R], so the raw pair and its gcd reduction are exact. If the divisor test passes, the target valuation argument supplies the whole primitive budget. Conversely the bounded primitive target reconstructs positive integers with the same ratio and reciprocal sum; uniqueness of that positive rational shell pair forces the exact computed(y,zprime), proving integrality and hence the divisor test. No integral-return condition is assumed without being computed.

### `thm:unary-box` — pass

Locator: `unary_boolean_transport.tex`, line 67.

The full rectangle has J=6h,M=9h, and mixed-radix division gives the exact inverse of c=(A-1)2JM+2Mj+2(B-1)+epsilon. The tagged component is correctly the singleton{(j,epsilon)}. For u|a^2, reducing a=gA,u=gB gives B|g, hence positive D=g/B and a=ABD,u=B^2D. Conversely the admissible rectangle conditions AB|a and gcd(A,B)=1 give exactly u=B^2D and gcd(a,u)=BD; this proves the full box/code bijection and all exponent inverse coordinates. Multiplying4u+p^epsilon by the unit A gives the original gate A+p^(1-epsilon)B. For epsilon1 the gate is exactly the middle one by4a=p moduloR. The stated positive integer triple has reciprocal sum4/p and reduced ratio A/[p^(1-epsilon)B]. A,B<p identify epsilon from divisibility of its denominator by p. Thus the ordered inverse is exact on the chart image. The explicit middle-chart exchange with mu_a and the exterior transposition preserve the source orientation without identifying it incorrectly.

### `thm:unary-truth-fibres` — pass

Locator: `unary_boolean_transport.tex`, line 166.

The truth-vector map on the actual passing code set has disjoint fibres partitioning that finite domain, so pulling them through the bijection preserves all simultaneous predicates on the same point. Any Boolean expression selects a disjoint union of whole truth fibres. Inverse images commute with union and intersection; for the stated r>=1 the fibre product over inclusions consists exactly of equal-code diagonal tuples. The tagged union projection has one preimage for each membership tag and its least-tag section gives a disjoint representation. The products of positive and complemented bits count each truth fibre exactly, and inclusion-exclusion counts each point with positive membership once. Partial coordinate predicates are evaluated only where chi=1, so arbitrary outside bits do not create witnesses. Exterior codes represent unordered pairs once with weight2; middle complement pairs each have weight1. Hence W1=2Q_p, and the middle invariance hypothesis is exactly what permits interpreting W_F/2 as an unordered integer count.

### `prop:unary-crt-fibre` — pass

Locator: `unary_boolean_transport.tex`, line 279.

Inside each fixed(j,epsilon) component the original divisor upper bound and gate remain mandatory. Every actual truth-cell point obeys all collected true affine/divisibility atoms, so the exact bounded-divisor CRT returns its unique u. The final test of all required true and false predicates at that same reconstructed code is necessary and sufficient for its entire truth vector. This proves both inclusions and no duplicates. Variable coefficients, arbitrary decidable predicates and false congruences are correctly postponed to the final exact test; they are never replaced by independent local choices or a conjunction of all local negations. The finite loops over components and disjoint truth vectors preserve complete lifts and cardinalities, including the actual ordered chart inverse.

### `prop:input-crt` — pass

Locator: `shared_variable_crt.tex`, line 15.

Dividing lambda_i X=beta_i modulo m_i by the full gcd is reversible exactly when that gcd divides beta_i, including lambda_i0 and reduced modulus1. Pairwise compatibility is sufficient because for each prime a prior modulus achieving the maximum valuation gives exactly the common prime-power constraint between the prior lcm and the new modulus. Thus the merged residue remains compatible at every stage. The explicit merge representative remains in0,...,M-1 because its step is the least nonnegative remainder, with the stipulated zero step for modulus1. All integer fibres are a+MZ; positive t>=floor(-a/M)+1 and bounded ceil/floor t intervals are exact and have the stated inverse. The source F=p! product|E| is positive with every supplied nonzero E retained; no prime-output claim is inferred from these input congruences.

### `prop:output-crt` — pass

Locator: `shared_variable_crt.tex`, line 96.

The retained integer seed gives D_q=D_p+(q-p)Theta/K0. Dividing K0 and Theta by their gcd leaves coprime m,w, so integrality is exactly q=p modulo m, for every integer q. CRT with q=1 modulo the chosen positive D gives the exact gcd(D,m)|(p-1) obstruction, complete representative and lcm fibre, including reduced modulus1. At q1 the rational(A+B+C)/(4ABC) equals D_p-(p-1)w/m, so its reduced denominator is m/gcd(m,p-1). Positivity and A,B,C<=ABC place that rational strictly between0 and1, proving the denominator exceeds1 and all stated incompatibilities. D12 is compatible because p-1 is divisible by12. No condition is dropped to assert that a cyclotomic prime divisor belongs to the prescribed class.

### `lem:canonical-auxiliary` — pass

Locator: `shared_variable_crt.tex`, line 217.

The coefficient-sum bound controls each polynomial on the original closed integer box, with zero-to-the-zero convention1. The one-hot sign bits and inactive-slack zero equations give exactly one extension for each sign: positive slack f-1, negative slack-f-1, or both zero. The bound max(F_f-1,0) correctly includes F_f0 and1. For a divisor positive on the retained admissible domain, G=max(1,F_d) gives a valid nonempty bound even if the admissible domain is empty. Euclidean division gives q=floor(f/d) in[-F_f,F_f] and remainders r,s in[0,G-1]. Conversely the second residual and nonnegative r,s force0<=r<d, uniquely identifying quotient, remainder and s. Encoding the sign of r gives exactly the divisibility bit. Separate auxiliary blocks all attach uniquely to the same tuple; Boolean node equations then give a unique bit extension by finite expression induction.

### `thm:shared-variable-crt` — pass

Locator: `shared_variable_crt.tex`, line 321.

Coordinatewise scalar CRT yields precisely the pairwise-compatible residue tuples, kernel LZ^k, unique standard representative and full fibres r+LZ^k. Dividing every original augmented interval by positive L gives exactly the displayed integer ceil/floor bounds, including empty fibres and L1. All auxiliary coordinate bounds are proved before computing H by absolute coefficient sums. Any specified common multiple D_fixed is retained, and L=D_fixed(H+1)>H. Polynomial congruence preservation makes every bounded common lift of a locally zero residual tuple satisfy L|f_a(z); the global bound |f_a(z)|<=H<L forces f_a(z)=0 as an integer. Conversely every exact residual solution reduces to such a tuple. On retained admissible lifts the canonical auxiliary lemma identifies the bits uniquely, so Phi is evaluated once globally on the original common variables. Projection is a bijection because original solutions have unique auxiliary extensions and every augmented vector has one residue tuple and lift parameter. The explicit count therefore has no duplicate projection. Multiple coordinate lifts, variable positive divisors, negated predicates, original admissibility and positive ES reconstruction remain attached; no local-witness choice is substituted for a common integral lift.

### `cor:actual-prime-truth-system` — pass

Locator: `shared_variable_crt.tex`, line 472.

The actual full primewise instance retains the rectangle j0,...,6h-1, A,B1,...,9h and epsilon0,1. The polynomial p+(1-p)epsilon equals p^(1-epsilon), so the gate numerator is unchanged. The conjunction excluding common divisors d2,...,9h is exactly gcd(A,B)=1 because any nontrivial gcd lies in that range. Together with AB|a and R|T this is precisely the full chi hit set; every tested divisor is positive on the rectangle. At hits canonical Euclidean remainders vanish, giving unique positive D=a/(AB),C=T/R. Bounds D<=9h and C<=floor((p+1)9h/3) follow from a<=9h,T<=A+pB and R>=3. The exact quotient A^2D proves u=B^2D|a^2, and the displayed bounds on A,B,C,D and p^epsilon prove the y,z bound. The positive ordered reconstruction is the earlier exact chart formula; appending predicates on those same polynomial coordinates uses the proved finite auxiliary construction. Thus this is a concrete all-bounded ES instance of the shared-variable theorem, preserving the code inverse and exact weighted/unweighted counts.

### `lem:integral-augmentation` — pass

Locator: `integral_cyclic_bridge.tex`, line 6.

In the integral group algebra Z[G], the augmentation ideal is additively generated by u_g-u_0; its square is generated by u_(g+h)-u_g-u_h+u_0. The coefficient map to G kills every such relation, and the same relation proves additivity of g maps to[u_g-u_0]. These maps are inverse on I/I², with finite-support sums and negative integer coefficients retained. Since the algebra is commutative, the degree-zero cyclic boundary consists of zero commutators, giving HC_0^Z(A_G)=A_G. The full coefficient-map kernel is Z*u_0+I², and every fibre is the displayed translate; restriction to I has precisely its I² coset. Every group homomorphism induces the stated integral unital algebra map and preserves augmentation and its square, giving exact naturality. No rational tensor product erases finite torsion.

### `thm:cyclic-character-bridge` — pass

Locator: `integral_cyclic_bridge.tex`, line 67.

The explicitly defined Hom_Z(cyclic-chain-complex,Q/Z) convention has degree-zero cocycles exactly the additive traces and no incoming boundary. The subgroup with tau(u0)=0 and tau(I²)=0, rather than full HC^0, is exactly Hom(G,Q/Z), by the written coefficient-sum formula and inverse g maps to tau(u_g-u0). The extension proof uses the least m>0 with mx in H, lists all m solutions beta=(r+j)/m moduloZ, and proves well-definedness on H+Zx through its exact relation k-kprime divisible by m. All extensions are obtained, and their full restriction fibre is one extension plus characters pulled back from G/H. Finite iteration extends to G; applying it to the character g maps to1/order(g) on its cyclic subgroup proves exact separation, retaining every torsion order.

### `thm:cyclic-lattice-gluing` — pass

Locator: `integral_cyclic_bridge.tex`, line 142.

Each exponent quotient embeds in a finite residue unit group, and O is its quotient, proving finiteness. The integral augmentation isomorphisms conjugate the previously exact lattice i,delta sequence to the displayed augmentation-quotient maps; explicit generators, kernels, inverse coordinates and fibres are given. In the Q/Z trace subgroups, pullbacks are exactly character restriction/composition. Delta-surjectivity gives injective delta-star; characters killing ker(delta) factor uniquely through O, proving its middle image, and the proved character-extension construction gives surjective i-star with full affine fibres tau0+delta-star T_O. Character separation therefore tests precisely the original obstruction o, and its vanishing returns the same e0+K_L and original bounded B intersection. No trace vanishing is substituted for finite-box occupancy.

### `thm:input-output-incidence` — pass

Locator: `input_output_incidence.tex`, line 66.

The original fixed seed, prime, full source shell, all input affine congruences and bounds remain in the labelled datum. Input CRT failure yields the empty incidence. Candidate q labels retain primality, q>p, both prescribed residue-one classes and q=p modulo m; their finite bound N(V) is proved by the exact positive difference N(n+1)-N(n). Fixed-q fibres are the disjoint union of every polynomial root rho modulo q that passes gcd(M,q)|(rho-a_in), with the explicit noncoprime CRT representative, Lq kernel and all original ceil/floor interval lifts. Reduction X moduloq and t=(X-x_qrho)/Lq give both inverse coordinates; different roots cannot duplicate X. Counting by either projection counts each prime label once. The retained output class gives Dq integral and Omega+qTheta>0 gives positivity; the exact original ordered denominators sum to4/q. The source full shell bound and q>p imply a_q/q<=a_p/p<=3/4-3/(4p)<=3/4-3/(4q), while Theta>=C,Omega>0 give a_q/q>1/4. Thus the entire target shell interval, Rq,Sq and ordering survive. Adjoining coordinates is a graph bijection retaining seed,X,q; forgetting X has exactly the computed root fibres. The p13/q73 fixture proves nonreturn of the selected factor only and does not assert the whole filtered incidence fibre empty.

### `thm:r3-factor-sieve` — pass

Locator: `first_two_shell_sieve.tex`, line 18.

The original a=3h+1 is one modulo3, so both gates are exactly u=2mod3. The full prime-labelled exponent box maps bijectively to divisors with valuation inverse, and the passing fibre is precisely odd total exponent on the residue2 primes. The even-minus-odd alternating product is1 on those coordinates; all residue1 choices contribute P1, giving P1(P2-1)/2 for each channel. Complement a²/u preserves the middle fibre with no positive fixed point, so its count is even and the original weighted count is3P1(P2-1)/4. A residue2 factor gives u=a*ell with A1,Bell,D=a/ell in both tags; C0=(1+p*ell)/3,C1=(1+ell)/3 are positive integers, and the common-denominator calculation proves both ordered triples. All exponent budgets and the original first-half bound survive.

### `thm:r7-factor-sieve` — pass

Locator: `first_two_shell_sieve.tex`, line 95.

Primality and a<p imply gcd(a,7)=1. The complete power table of3mod7 gives the exact logarithm coordinates and all original exponent fibres: exterior log5 and middle log(b+3), where b is the retained log ofa. Expanding the integral group-ring product counts every labelled exponent vector, including repeated residues and all finite caps. Each constructive branch is an actual divisor ofa²: ell5, a*ell6, a*d with three available residue3 copies, a*ell3*t2, and a*ell3/t4. In the quotient branch the two distinct affected exponents are b_ell+1 and b_t-1. If all predicates fail, n3=0 leaves only the residue subgroup{1,2,4}, disjoint from both targets. Otherwise n3=1 or2 and n24=0, so every divisor log is in0,...,2n3 and every signed log in[-n3,n3]; these miss5 and3mod6 respectively. This exhausts the original box, proving the full equivalence without substituting unrestricted group closure.

### `cor:two-shell-sieve-return` — pass

Locator: `first_two_shell_sieve.tex`, line 214.

The stated rejection set is precisely the conjunction of the two proved empty-fibre conditions. It makes no inference about remaining shells or survivor infinitude. For every retained passing tag and original divisor, the valuation exponent ofD=gcd(a,u)²/u is2min(v,e)-e, nonnegative throughout0<=e<=2v. Thus a=ABD,u=B²D and gcd(A,B)=1 hold integrally. Multiplication by the retained units gives each original C gate, so C>0. The common denominator pABCD gives exactly the ordered triple in the statement. The graph retains p,a,epsilon,u and hence has its stated unique valuation inverse; both shells satisfy a<=6h. The subsequent p373 example exhausts all nine original divisor exponents of95² and gives E={5,19},M empty, with A19 and5, so the same-shell A<=2 implication fails by an actual computed counterexample.

### `thm:raw-scale-fibre` — pass_after_repair

Locator: `raw_scale_hit_incidence.tex`, line 14.

The final domain explicitly makes A,B,C,D positive and permits both tags0,1. Since k=gcd(A,B)<p, the raw equation modulo k gives k|C. The exact residual is k times the coprime residual under (A,B,C,D)=(kA0,kB0,kC0,D0/k²). The original first denominator remains A0B0D0, and both inverse compositions recover all coordinates and k. Forgetting k has precisely the square-divisor fibre ofD0 and its primewise count. Direct substitution preserves a,R,S,u and ordered x,y,z, the actual gcd, each factor quotient and each scaled affine numerator. The reduced pair is(A0,p^(1-epsilon)B0), with gate quotientC0=C/k. The final orientation repair identifies original d=d_y, source(d,e)=(d_z,d_y), and proves d_yd_z=S² with the explicit complement and coordinate-swap involutions. No raw scale or original orientation is discarded.

### `thm:raw-scale-period` — pass

Locator: `raw_scale_hit_incidence.tex`, line 130.

The seed identity supplies D0(q)=D0p+(q-p)Theta0/K0 for every signed integerq. Dividing by the exact gcd gives primitive periodm0; the retained condition k²|D0p similarly gives raw periodmk=k²K0/gcd(k²K0,Theta0). Since gcd(m0,w)=1, the complete gcd calculation yields mk/m0=k²/gcd(k²,w), including all cancellations and inverse divisibility statements. Intersection with q>=p and q=1mod12 is precisely p+lcm(12,mk)t,t>=0. All returned denominators and rational coefficients remain positive there. The original shell inequality is proved for prime returnedq using a_q/q<=a_p/p and the lower strict bound>1/4. At a fixed primitive return the scales are exactly square divisors ofgcd(D0p,D0q), with their full count and inverseDk=D0/k²; a fixed k>1 is not extended to all primitive returns.

### `thm:raw-first-half-code` — pass_after_repair

Locator: `raw_scale_hit_incidence.tex`, line 241.

The first-half inequality is obtained by multiplying the exact a_q formula by positive2C0. The sign of2C0-Theta0 is handled completely; positive coefficient gives the exact ceiling and a first-half seed implies every later return passes. The PCT radix is the original first-half rectangle, and successive Euclidean divisions recover every digit. The repaired total chi_H explicitly computes a(c),R(c) from each arbitrary decoded code and applies the three original tests on that same tuple. The prefix product is proved to equal the least hit, including the failure sentinelN_H, and the A-layer inequalities preserve the distinction between a selected witness and another possible hit. On full hits with first-half shell the divisor condition bounds A,B byM_H, so recoding is defined; the converse PCT-to-full map retains the same digits, exact C,D,u and ordered triple. Both maps are inverse with singleton fibres. Subtracting the two complete radices gives c_F-c_H=2(A-1)Lambda_H+(q-1)j/2. Scales remain separate fibre coordinates.

### `thm:raw-scale-hit-incidence` — pass

Locator: `raw_scale_hit_incidence.tex`, line 411.

Each retained scale is a genuine raw seed, whose exact output integrality period is mk after the full k³ numerator/k denominator gcd calculation. Applying the already proved input-output incidence to that seed leaves all original input constraints, bounds and polynomial roots unchanged, and then applies the exact first-half gate on the same q. Thus fixed-scale and fixed-input fibres are the stated complete root branches and filtered prime lists, including empty fibres. The graph adjoins only uniquely determined raw tuple, original ordered witness, shell data and both distinct codes while retaining k,X,q and fixed source labels, proving its inverse. Forgetting k lands in the primitive incidence because m0|mk and is onto with section1; its full fibre is exactly the square divisors ofgcd(D0p,D0q). Counting either by these fibres or by scale/prime/root branches gives the two finite counts. Every predicate and Boolean truth vector is evaluated on the same retained graph element; projection intersects its full fibre with those tests rather than replacing occurrences by separate witnesses.

### `thm:shellwise-no-hit` — pass_after_repair

Locator: `counterexample_sieve/all_shell_no_hit.tex`, line 79.

The prime-labelled valuation box and residue packet give exactly the original E and M fibres. The repaired tagged domain consists of both exterior orientations (0,u,sigma) and a single middle tag (1,u,0). The valuation formula proves A,B,D positive integral, a=ABD, u=B^2D and gcd(A,B)=1. Multiplication by units A,p converts each gate exactly to integrality of positive C. The corrected common-denominator numerator is pC+p^(1-epsilon)B+A=4ABCD. The original residuals are d_y=p^epsilon*a^2/u and d_z=p^(2-epsilon)*u before swapping. Independently the residual divisor d_y maps bijectively to every ordered witness via ((S+d)/R,(S+S^2/d)/R). Its unique p-adic exponent i=0,1,2 gives inverse tags (0,a^2/d,0), (1,pa^2/d,0), (0,d/p^2,1), with all three reversible unit gate calculations proved. Hence both inverse compositions and singleton fibres hold on the entire ordered domain. The exterior swap toggles sigma; middle complement u->a^2/u swaps A,B and the last denominators with C,D unchanged. The two typed order-forgetting maps have exactly two-point fibres, since a fixed middle point would force R|2. Ordered and unordered counts are therefore 2|E|+|M| and |E|+|M|/2. The old review missed the omitted exterior orientation and pCD typo; PR-006/007 preserve that failure.

### `thm:global-no-hit` — pass_after_repair

Locator: `counterexample_sieve/all_shell_no_hit.tex`, line 295.

The indicator product is one exactly when both coefficient targets vanish in every retained shell. Each nonnegative integer shell count counts the proved order-forgetting fibres, so the finite sum is zero under exactly this same condition. The preceding original primewise biconditional uses the minimum denominator permutation to place some first denominator in the entire shell interval; the repaired shellwise inverse then reconstructs all original ordered solutions at each shell. Negation proves the asserted global equivalence. This does not claim occupancy, prime density, or any ES solution for a previously empty all-shell system.

### `cor:global-r3-r7` — pass

Locator: `counterexample_sieve/all_shell_no_hit.tex`, line 330.

The first two original shell residuals are 3 and 7. Substituting their exact earlier factor criteria into the coefficient-zero condition gives precisely the stated local rejection predicates. Their conjunction with the coefficient conditions for every remaining shell is equivalent to the full obstruction; the first two alone are only necessary. Every shell label and factor exponent remains attached.

### `thm:ns-directional-intertwining` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 33.

The literal eigenvectors satisfy the two displayed eigenvalue equations component by component. The Fourier map n -> (J^m)^T n is injective over Z^2 since det J^m=14^m; its full image and coefficient inverse are exact and retain the 2*pi*i convention. The chain rule yields D_v P_m=lambda^m P_m D_v. Irrationality of sqrt(2), proved by the parity contradiction, makes v dot n nonzero for every nonzero integer frequency, so D_v maps precisely onto the zero-constant finite polynomials with constant kernel. Reciprocating the exact nonzero multiplier proves D_v^-1 P_m=lambda^-m P_m D_v^-1 on that specified domain. No assertion of an inverse on arbitrary smooth functions or an analytic small-divisor estimate is needed.

### `thm:ns-torus-fibres` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 92.

Solving the first equation gives y=a-3x; the second becomes 14x=5a-b. On R/Z the fourteen listed lifts have distinct first coordinates and exhaust the root equation; changing real representatives leaves the root set unchanged. On N-torsion the exact obstruction is gcd(N,14)|(5a-b), and division by that gcd yields the invertible coefficient 14/g modulo N/g. The n=1 branch is explicitly included. All g lifts, the full kernel, N^2/g image cardinality, and the torsion coordinate identification with j/N have their stated inverses and preserve every target coordinate.

### `thm:ns-torus-average` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 150.

Summing by the exact finite fibres proves g/N^2 times the image sum; the zero-target indicator proves that equality for all functions fails when g>1. The literal transpose-frequency calculation and geometric sums give precisely the listed kernel frequencies. The full inverse image H of any finite subgroup D has 14 points per target. Thus P is injective, LP=1, PL averages exactly each deck orbit, and the stated normalized inner products obey the adjoint identity with |H|=14|D|. The kernel and all affine L fibres and singleton-or-empty P fibres follow directly from these formulas. The unlabelled Fejer argument proves only the continuous Haar identity on the unchanged torus: positivity, mass one, geometric-series tail bound, and uniform continuity supply the uniform approximation and integral limit.

### `prop:ns-torus-powers` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 236.

The quotient parametrization [k] -> J^-m(dtilde+k) has inverse [J^m htilde-dtilde]. Changes in either lift give exactly J^m Z^2, proving every fibre and both inverse compositions. Fourteen-fold one-step surjectivity iterated m times gives 14^m distinct points, proving the quotient cardinality without an assumed determinant-index theorem. Products use independent coordinates. On fixed N-torsion the backward recursion has disjoint predecessor sets because every candidate has its unique next point; image failure can stop branches. At N=2 the original matrix squares to zero, so kernel cardinalities 2,4,4 are correctly distinguished from an invalid 2^m rule.

### `lem:ns-finite-dual` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 278.

Extending from B to <B,g> retains the unique b*g^j presentation with 0<=j<r and all r roots of z^r=chi(g^r). The carry relation at r proves multiplicativity, and restriction/value-at-g recover both extension coordinates. Successive subgroup index products therefore prove |dual G|=|G| and enumerate every character. Starting at the cyclic subgroup of any nonidentity element and extending proves separation; translation of the character sum proves exact orthogonality. The retained generator tuple embeds the dual in the original unit-period torus; every relation is necessary and sufficient for the inverse word formula to be well-defined. Fibres are singleton on that precisely described image.

### `thm:ns-es-packet` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 341.

Finite orthogonality gives an orthonormal basis of |G|^2 functions and therefore the stated Fourier inversion. Pulling back a mode gives chi(u^3 v)*psi(u v^5); both averages survive exactly when v=u^-3 and u^14=1. Directly solving the two target equations proves the kernel, image and all fourteenth-root fibres. Each single marginal is uniform by varying the other input bijectively. Literal packet expansion retains every prime label and exponent cap, and unique factorization supplies its full divisor inverse. The two-packet sum retains exactly the displayed exponent pairs with uniquely recovered torsion index. For the original row (A_m,B_m), the conditions u^A_m=u^B_m=1 are equivalent by Bezout to u^gcd(A_m,B_m)=1, including row (1,0) at m=0. No subgroup closure replaces the bounded valuation box.

### `cor:ns-es-cover-repair` — pass

Locator: `ns_operator_bridge/torus_cover_lemma.tex`, line 454.

The retained coordinate embedding identifies D with the full finite dual square, and the product of the quotient lift maps gives exactly 14^(m*s) points over every target. This proves the displayed mean and every lift coordinate on the specified H_m domain. Independent target means recover the one and two packet counts without aliases. At p=13,a=4,R=3 the five original exponents give counts (3,2), and both targets equal 2. The two torsion contributions are 4 and 9, so the uncorrected joint mean is 13 while the independent target product is 4. The actual row of J^2 is (10,8), whose gcd 2 retains both units and gives the uncorrected one-packet count 5, while the cover returns 2. These are exact discrepancies, not proof of empty original fibres.

### `lem:ns-labelled-character-packet` — pass

Locator: `ns_operator_bridge/sieve_character_cover.tex`, line 52.

The additive dual is explicitly constructed on the actual unit multiplication table, with exponent values in (1/n)Z/Z. The exponential correspondence with the preceding multiplicative convention is a proved isomorphism with singleton fibres. The explicit subgroup extension proves separation; translating the finite character sum gives orthogonality with denominator |dual G|. Expanding the formal packet retains a distinct monomial for each original valuation vector. Its coefficient is exactly one for the target equation and zero otherwise. Unique factorization recovers every positive divisor and inverse valuation, and the two unit targets are exactly the original exterior and middle gates.

### `thm:ns-character-coset-correction` — pass

Locator: `ns_operator_bridge/sieve_character_cover.tex`, line 119.

The first output fixes beta=gamma-3alpha; the second is the exact root equation 14alpha=5gamma-eta. Thus the displayed kernel, image, quotient map q and exact sequence are proved in both directions. Each nonempty root fibre is a translate of dual G[14], with cardinality delta; counting gives exactly delta quotient cosets. For T the unique recorded representative of [eta-5gamma] is rho, and all delta roots of 14alpha=5gamma-eta+rho give the full fibre. Hence T is onto and counting its constant delta fibres proves the averaging identity for arbitrary functions and coefficient by coefficient for polynomials.

### `thm:ns-sieve-alias-removal` — pass

Locator: `ns_operator_bridge/sieve_character_cover.tex`, line 185.

For each retained pair of original exponent vectors, the uncorrected complex factor is <alpha,g^3 k><beta,g k^5>. Orthogonality keeps precisely k=g^-3 and g^14=1, giving the exact nonnegative alias packet sum. With correction the extra factor is <rho,k>. For k^14=1 it factors through the quotient dual G/14 dual G; character separation and quotient translation make its representative sum vanish unless k=1. Then g^3=g^14=1 implies g=1 through 1=5*3-14. Thus the corrected sum keeps exactly both original targets with their full two formal monomials, and not merely their aggregate counts.

### `cor:ns-finite-history-sieve` — pass

Locator: `ns_operator_bridge/sieve_character_cover.tex`, line 242.

Successive substitution gives the exact matrix-power expansion, including the empty sum at k=0. For each terminal point the last coset coordinate is uniquely determined and there are delta predecessor states. Repeating the full inverse step produces precisely delta^k distinct histories, retaining each state and coset coordinate. Fibre counting proves the mean for arbitrary polynomial functions. The specified single-packet function removes only the independent eta summation factor and recovers the original target polynomial. Returning each monomial through the repaired oriented no-hit map retains the exterior swap bit and both middle divisors; Q_p and O_p consequently remain the original tests at every finite history length.

### `thm:ns-continuous-transfer` — pass_after_repair

Locator: `ns_operator_bridge/reverse_proof_transport.tex`, line 17.

Every target fibre is the proved 14^m-point deck coset. Its finite sum gives L_m P_m=1 and P_m L_m=Q_m; local affine inverse branches prove smoothness. Injectivity of P_m proves the complete L and Q kernels and all affine fibres, while deck invariance characterizes the singleton-or-empty P fibre. The annihilator calculation evaluates the retained character on J^-m Z^2/Z^2, giving exactly n in (J^m)^T Z^2 and its unique original k. Haar preservation follows from polynomial Fourier calculation and the existing uniform Fejer approximation; fibre projection gives the product identity and conjugation gives adjunction. The exact surviving multiplier v dot n=lambda^m(v dot k) proves D_v L_m=lambda^-m L_m D_v and D_v^-1 L_m=lambda^m L_m D_v^-1. Smooth Fourier convergence and the proved finite derivative loss justify both extensions. Translation averaging commutes with the original multipliers. The previously implicit full Q_m fibre is now expressly proved, not inferred from a verbal distinction.

### `thm:ns-reverse-mean-correction` — pass

Locator: `ns_operator_bridge/reverse_proof_transport.tex`, line 108.

At every retained slow coordinate the original Haar subtraction removes precisely the zero Fourier coefficient. The proved smooth inverse gives c_i D_t C_i(E)=-E^circ. A zero correction forces E to be an arbitrary torus-independent slow function; solving for E gives the complete fibre -c_i D_t V+b and every zero-mean V is attained. Haar commutation and D_t^-1 P_delta=T_g^-delta P_delta D_t^-1 combine with c_j=T_g^-delta c_i to give the written covariance with its minus sign. Deck invariance is the full descent test and L_delta its inverse. Powers compose, so the common sum and absolute representative agree exactly. Injectivity of the smaller pullback proves every overlap equation and its returned correction; sums and products use the actual coefficient algebra. Fixed Q and all band indices remain, and the exponent calculation Q^A Q^-(2A+1/2) T_g^-i=Q^-1-h T_g^-i=c_i^-1 retains the original physical factors.

### `thm:ns-physical-evaluation-fibre` — pass

Locator: `ns_operator_bridge/reverse_proof_transport.tex`, line 188.

The evaluation graph is smooth on the expressly retained r>0 domain. Constant-in-torus extension is a right inverse, subtraction gives the graph-vanishing kernel and every affine evaluation fibre, and power composition proves E_i=E_j P_(i-j). The chain rule retains both slow derivatives and J^i v eigenvalues. The original chart changes produce exactly -Q^h partial_T+c_i D_t, partial_R+Lambda^i Q^(d_r/2) d_r R^(d_r-1) D_r, and Q^h partial_Z, including the negative time sign and the radial domain. For nonzero n the nowhere-zero a=e_n(J^i phi) gives H=e_n-a with zero evaluation and mean -a, proving failure of mean descent. The explicit F_(f,b)=b+(f-b)e_n/a attains every desired pair of evaluation and mean, with complete fibre F_(f,b)+(ker E_i intersect ker Pi); taking its real part retains real pairs. The conclusion states this proved structural freedom, without attributing an unproved motivation to source authors.

### `thm:ns-reverse-sampling-fibres` — pass

Locator: `ns_operator_bridge/reverse_proof_transport.tex`, line 266.

Two finite geometric sums give the exact residue-sum DFT and its full kernel. Orthogonality supplies the basis and surjectivity. For a retained finite original spectrum, occupied residue classes give exactly the image; one retained representative per class and all remaining free coefficients give every inverse fibre. Thus restriction is injective precisely on distinct residues. If n and nprime collide, irrationality makes v dot(n-nprime) nonzero, so the zero-sample character difference has a nonzero derivative sample. For the inverse both original modes must be nonzero; their distinct nonzero multipliers have distinct reciprocals. This proves necessity on exactly Omega minus original zero. Conversely the restriction bijection conjugates each actual operator and forces its unique image operator; the empty-domain case is included. The separate e_(Nk)-1 and e_(Nk)-e_(2Nk) fixtures retain 2*pi*i and prove both unrestricted obstructions. Neither grid mean nor a choice of reduced frequency replaces original Haar zero or the full frequency labels.

### `thm:ns-reverse-lifted-inverse` — pass

Locator: `ns_operator_bridge/reverse_proof_transport.tex`, line 377.

Distinct original residue labels make I_Omega read each exact coefficient, proving both inverse compositions on the stated image. Conjugation then gives the actual derivative and zero-Haar inverse; the single original mode (N,0) proves why constant grid values need not have a zero-frequency source. Every target grid point has 14^m preimages, so the lifted Gram sum equals the original grid DFT of f e_-n and recovers each coefficient. The inverse frequency is (J^-m)^T on its exact image, and the original multiplier denominator is 2*pi*i lambda^m(v dot n). For smooth data, integration by parts and the full 8j shell count prove absolute summability with every displayed weight. Uniform reconstruction permits the finite-fibre average term by term; precisely N Z^2 frequencies survive. Subtracting the actual zero mode gives the exact error series. Every surviving nonzero mode has length at least N, giving the displayed weighted bound independently of m. Original spectral collisions are not repaired by silently changing the spectrum.

### `thm:ns-sharp-denominator` — pass

Locator: `ns_operator_bridge/reverse_smooth_inverse.tex`, line 20.

Both original vector/conjugate products expand to the stated nonzero integral quadratic forms, and their zero cases force the zero integer vector by irrationality. Their absolute values are at least one. Cauchy-Schwarz with the retained conjugate norm c gives the bound; equality is impossible because a nonzero integer vector cannot have the irrational conjugate slope. The explicit integral Pell recurrence gives alpha^j and beta^j with beta=-alpha^-1, including the signs for both original directions. Perpendicular decomposition in the unchanged vectors proves K_j^2=alpha^(2j)/c^2+alpha^(-2j)/d^2 exactly. Hence the product tends to 1/c with every integer coordinate retained, proving the strict bound, sharp infimum and nonattainment. Neither original direction is rescaled to unit length.

### `lem:ns-fourier-analytic-bridge` — pass

Locator: `ns_operator_bridge/reverse_smooth_inverse.tex`, line 119.

Original period-one characters are orthonormal. Expanding a finite projection error proves Bessel directly; periodic integration by parts retains every 2*pi factor. The multinomial expansion of W^r and total coefficient sum 3^r establish the coordinate C^r to H^r estimate. Integration along a coordinate at least |k|/sqrt2 gives exact decay, while the complete 8j shell count supplies summability. All differentiated series converge uniformly; the earlier proved Fejer approximate identity identifies their sum with the original function, so no rapid-array surrogate is assumed. Bounding S by (1/(2*pi^4)) sum j^-3 and the displayed integral gives 3/(4*pi^4). Cauchy-Schwarz applied to W^-1 and W^((m+2)/2)|b| gives the exact reconstruction inequality. The original nonzero-frequency condition ensures 2*pi|k|>=1 for every derivative of lower order, proving the full C^m assertion.

### `thm:ns-sharp-smooth-inverse` — pass_after_repair

Locator: `ns_operator_bridge/reverse_smooth_inverse.tex`, line 206.

For every original nonzero frequency the sharp denominator bound yields the exact multiplier ratio below (c/(4*pi^2))^q in the stated W-weighted Sobolev norms. Summing and coefficient truncation extend the map to the specified completion. The two retained Pell sequences make this ratio tend to that constant; for any smaller derivative loss delta<q the same single-character ratio grows as alpha^((q-delta)j), proving the exact norm and optimal Sobolev loss. Smooth coefficient decay proves every differentiated inverse series converges, and the nonzero symbols force the full smooth kernel, image and constant fibres. The previously incomplete distributional bridge is now proved: H^s coefficients have polynomial growth, their pairing with test-function coefficients has the displayed continuous C^M bound, and distributional differentiation gives the correct positive Fourier multiplier after its definition by a minus sign on tests. Smooth Fourier sums converge in every seminorm, so zero distributional coefficients imply the zero functional. Thus both the equation and zero-mean uniqueness hold for precisely the stated H^(s+q) data.

### `thm:ns-cm-improvement` — pass

Locator: `ns_operator_bridge/reverse_smooth_inverse.tex`, line 306.

Apply the proved reconstruction inequality to inverse coefficients and the exact Sobolev multiplier estimate at output order m+2. This gives the first inequality with the original lattice sum S. The multinomial C^r bound at r=m+q+2 gives C_(m,q)=(c/(4*pi^2))^q 3^((m+q+2)/2)sqrt(S), and its explicit upper bound follows from S<=3/(4*pi^4). The Bessel/integration-by-parts proof uses only the displayed finite differentiability, so the result directly covers C^(m+q+2) data. The one-inverse temporal step therefore needs m+3 and the repeated radial inverse m+q+2 in these coordinate norms; increasing the input order yields the source m+4 and m+q+3 inequalities. Only the Sobolev loss is called optimal: no optimality of this C^m count is asserted.

### `prop:ns-inverse-parameters` — pass_after_repair

Locator: `ns_operator_bridge/reverse_smooth_inverse.tex`, line 347.

On each compact parameter neighborhood, coefficient differentiation and integration by parts have uniform bounds of every required order. The 8j shell majorant makes all mixed inverse series and derivatives locally uniformly convergent; integrating each derivative series along a segment justifies termwise differentiation. This proves joint smoothness, exact parameter commutation and the uniform estimate. Vanishing parameter slices have every coefficient zero, and conjugate opposite frequencies prove the support and reality claims. The final source mapping expressly distinguishes absolute Y and common y=J^iY, both means and both inverses. Pulling back e_k(y) gives exactly e_((J^i)^T k)(Y), with T_g^i derivative factor and reciprocal inverse factor; multiplication by -c_i^-1 gives P_i Delta v=-Q^-1-h T_t^Y P_i E_theta^circ. The source A1 integral keeps its radial shift, cutoff and r>0 shell-supported domain, so local smoothness follows by differentiation over a fixed compact radial interval. The actual axial increment gamma_d-A1 gamma_d retains its fast remainder and both slow-time terms. No axial flatness or complete PDE estimate is supplied by assumption.

### `thm:boundary-four-rational` — pass

Locator: `boundary_swap/boundary_swap_completion.tex`, line 40.

The complete raw rational record keeps ABD=a, both bits, all shell data and the uniquely forced positive C. Swapping A,B and toggling epsilon commute and each squares to the identity, proving the full four-element action, singleton map fibres and all stabilizers; A=B gives exactly the stated stabilizer. The central equation yields the original common-denominator numerator pC+p^(1-eta)beta+alpha and all three ordered rational reciprocals. Direct multiplication gives d_y=p^eta alpha^2 D,d_z=p^(2-eta)beta^2 D and their product S^2 even before witness integrality. The original divisor u=B^2D is complemented exactly on swapping, with the tag retained. The graph inverse keeps source and bits, including coincident orbit members. The gcd-scale map and its displayed inverse retain k and D0, so its full forgotten-scale fibre is precisely k^2|D0. Since k is a unit modulo R, integral C forces k|C, proving integral equivalence with C0; direct substitution proves every ordered witness coordinate is unchanged. No rational companion or raw scale is discarded.

### `thm:boundary-obstruction-fibres` — pass

Locator: `boundary_swap/boundary_swap_completion.tex`, line 148.

The two original source congruences A=-pB and A=-B give each of the six table rows separately, with signs retained. For N/R the least d with dN/R integral is R/gcd(R,N), proved through Bezout after keeping the gcd and both quotients. Every multiplier B,p,alpha,beta,D is a unit modulo R, so the same gcd remains for C,y,z; this proves every exact denominator and both directions of all four integrality tests. The rational involution restricts to a self-bijection precisely on records whose source and target are integral. The map psi_R([n])=n/R+Z is a proved additive isomorphism onto the R-torsion of Q/Z. Factoring m by gcd(R,m) proves the exact image, kernel and every affine fibre of psi_R composed with multiplication by m, including m=0. Since the retained B is a unit, its obstruction has the full stated additive order. Failed integral candidates retain their exact positive rational witnesses and inverse, rather than being declared unrelated.

### `thm:boundary-orbit-code` — pass_after_repair

Locator: `boundary_swap/boundary_swap_completion.tex`, line 257.

The original half and full shell ranges give A0,B0<=a<=M_rho, so swaps retain the exact radix rectangle. Successive Euclidean division proves the complete code inverse, including both encode-decode compositions; on hits C0,D0 and the retained scale reconstruct the full raw record. Subtraction gives s(B0-A0)(Lambda_rho-2)+(eta-epsilon) with every original digit retained. The preceding complete integrality table gives all four orbit rows; the unit contradiction excludes A=B for every middle hit and for R|p-1, giving exactly their stated distinct cardinalities. Lambda_rho-2>1 makes a coordinate drop dominate either tag change, proving every unique minimum. Two records share a minimum exactly when they belong to the same integral orbit; forgetting k adds precisely the disjoint square-divisor scale fibres. Global least hits must be orbit minima by the proved lower integral hit. The final wording expressly requires integrality for the exterior lower hit, preserving its rational companion when the obstruction is nonzero.

### `thm:boundary-r3-global-minimum` — pass

Locator: `boundary_swap/boundary_swap_completion.tex`, line 383.

The original R3 gate gives A0+B0=0 modulo3 with both units, so a hit forces a divisor congruent2 modulo3 and hence a retained prime factor in that residue. Conversely each such prime supplies A0=1,B0=ell,D0=a3/ell and the positive integral C0=(1+p ell)/3, proving occupation exactly before selecting its minimum. The constructed ell_star code is below 2M_rho and Lambda_rho, which excludes every A0>=2 and every later j>=1 in both original radices. The remaining A0=1,j=0 hits have B0 congruent2 dividing a3; a prime factor yields B0>=ell_star, and tag zero precedes tag one. This proves the actual global first code, full ordered denominators, both residuals and every raw scale. A boundary source m+1 has the same divisor/gate, so its involutive swap has exact code2m and the global code is at most2m with equality exactly m+1=ell_star. Failed R3 occupation is confined to j=0 and is not promoted to later-shell emptiness.

## Additional arithmetic coverage

### eq:signed-box and the E/M comparison

Signed exponent vectors are injective because the bases are distinct primes. The complement d maps to S^2/d swaps p-exponents0 and2; exponent1 has no fixed passing divisor because R cannot divide2a. Therefore the ordered witness count is2|E|+|M| and the unordered count is|E|+|M|/2. The signed channel targets are exactly-1/p and-1 moduloR.

### The full primewise biconditional and the two unary layers

Permuting an existing positive solution so a is its minimum gives p/4<a<=3p/4, whose integer range is precisely3h+1,...,9h; keeping the permutation permits return to the original order. This proves the necessity of Q_p>0, while the original reconstruction proves sufficiency. For u/a=B/A in lowest terms, the finite signed box gives A,B|a and their coprimality gives AB|a. Thus s=a/(AB), a=ABs,u=B^2s and s=gcd(a,u)^2/u are positive integer inverse formulas. Multiplying4u+1 by A gives the exact exterior mark A+pB, and the middle mark reduces to A+B by the retained units. The full divisor list at p37,a12 has only exterior u8, with(A,B,s)=(3,2,2), and no middle hit; the actual triple(12,42,1036) therefore does not produce an A<=2 hit at that shell. The p37,a10,u5 example has(A,B,s)=(2,1,5) and exact complementary residual divisors6845,20, giving(10,2405,130). Thus the text correctly refutes per-shell completeness without inferring a global cutoff counterexample.

### Finite-order kernel enumeration and two-term complex

Coordinate reduction modulo the respective multiplicative orders gives a finite union of full rectangular lattice cosets, including negative original exponents. Intersecting each coset with the original box is exact. Repeated gluing uses the entire prior kernel intersection. The complex has H0 equal to the diagonal image and H1=0 because delta is onto; the text correctly requires a specified local pair to be a cocycle and separately to have a bounded preimage.

### Primitive monoid product

Each labelled prime contributes exactly the zero exponent choice, a numerator-only positive exponent, or a denominator-only positive exponent. This is a bijection with coprime positive divisors of the supply. Residue multiplication and the final sum test are consequently exact; a common stored choice, not unrelated local choices, determines a lift.

### Original norm equations and p1201 exhibits

The expanded identity T^2+2Delta^2=p(p+2) has the correct orientation-independent square. Positive primitive collinear endpoints would coincide, contradicting their norms. For |Delta|=1 the positive factors(p+1-T),(p+1+T) of3 have sum4, forcing p=1, excluded here. The p1201 endpoints, Delta=-667,T=745, supplied return coordinates, denominator triple, contained empty cone coefficients and all four empty-return rows were checked. The alternate empty cone is not asserted to be a leaf of the coordinate-bounded canonical chain.

### Finite category-of-divisors specialization

The covariant functor is the representable Hom_R(N,-): it has a point at n precisely when n|N. The category of elements has common source lcm(n,m), with no unequal parallel arrows. Its cofiltering/flatness condition and associated finite embedded group are coherent with the stated arrow orientation. No cyclic-cohomology or abstract topos-point result is used as an unproved arithmetic lifting assertion.

### eq:conjugate-affine and the full J correspondence

The specified iota_N(x)=1/(Nx) is an involution on positive reciprocal divisors, where it exactly complements u to N/u. It is not claimed to be a total self-map of H_N. Conjugating Psi by these involutions gives x/(1-cx) on the complete partial domain u|N,u>c,u-c|M. The label map u maps to v=u-c has inverse v maps to v+c with v|M,v+c>0,v+c|N, proving singleton fibres and both directions of positivity and return. For a classified J shear the actual divisors are u=a/m=1+c(m+1),v=b/(m+1)=1+cm=u-c. The identity mu_a(a^2/w)=P*mu_a(w) follows from the inverse reduced ratio and proves J=PLP on these exact divisor maps. Both marks and all valuations survive, with the last two denominators exchanged. At p1753,a440,c1 the L reciprocal map is1/8800 to1/9261 and the complemented J map is1/22 to1/21. Applying raw Psi to1/22 instead gives419/9261; the final source explicitly avoids that incorrect map.

## Independent computations

The new `review_checks.py` passed 7,840 single affine cases with signed coefficients and modulus-one cases, and 160 mixed upper-divisor, mandatory-factor and simultaneous-congruence cases. Its residue-monoid reconstruction was compared with direct testing of all positive integers in the original bound. It also recomputed the two actual local-obstruction examples, all four empty-cone determinant rows, the quoted integer witness triples and the failed fixed-y example. Its output is `review_checks.json`.

The extension independently enumerated all 26,439 adjacent shell pairs for the 63 eligible primes through1753, including all3,956 passing ordered source pairs. Its eight directly checked L/J edges form a matching, with no length-two path. It also passed7,200 affine/complemented reciprocal cases,9,261 signed affine composition cases, the exact zero-fibre and full positive-image tests, and the p1753 corrected/noncorrected orientation tests. Prime1613, outside the specified class, has a valid two-edge L chain at shells404,405,406; this confirms that the prime congruence restriction must remain attached.

The independent `boolean_shared_checks.py` additionally passed all856,332 full rectangular codes for p13,37,61,73,97, with3,048 admissible tagged codes,53 hits and weighted ordered count82. It checked exact code/box inverses, original denominator orientation and direct S-squared divisor counts; all eight truth cells per prime were compared against bounded CRT on the same u, followed by union/intersection, biconditional and negation tests. It exhausted25 bounded sign cases including F0 and all21,600 augmented quotient/remainder/sign tuples for a variable positive divisor, comparing exact residual zeros with overlapping CRT tests at moduli6,22,33 and L66. All15 original tuples had unique auxiliaries, and global Boolean projection matched direct testing. It checked525 affine input cases,848 prescribed output/seed cases, the three lifts[-2,0,2] of residue0mod2, and the p13 mixed-local-negation example. Output is `boolean_shared_checks.json`.

The independent `cyclic_incidence_checks.py` computes integral Smith forms of augmentation-square relation lattices for eight finite groups, retaining their exact torsion orders and checking all character relations and separation. It verifies64 lattice/character dual exact sequences and the actual p241/p37 obstruction cases. Five finite incidence fixtures retain every prime divisor of each tested input and compare full input fibres with all root-CRT branches, including a noncoprime modulus-one branch and all ordered witness/shell returns. Complete roots are computed through two exact modular square-root stages and checked against direct root enumeration for small primes. The p13/q73 nonreturn fixture is verified exactly. Output is `cyclic_incidence_checks.json`.

Run the check scripts from the assigned research directory using `python`. This is the existing Python 3.13.9 runtime with SymPy 1.13.1 needed by the cyclic/incidence checker; the bundled Codex dependency Python lacks SymPy. No package was installed.

The continuation checker `sieve_checks.py` exhausts 300 eligible primes through 10,000, all 10,480 original divisors of the first two shell supplies, and all 6,003 passing tagged divisors with both radix inverses and original ordered triples. It also checks 2,187 labelled residue-budget patterns and complete group-ring fibre counts. Fourteen primes have both tested shells empty; no conclusion about their other shells follows. Twenty-two occupied residual-seven shells lack A1 hits; the complete p373 fibre even has no A<=2 hit. The extra primes153877 and226789 explicitly test three residue3 factors, including repeated multiplicity, beyond the stated main finite interval.

The independent `raw_scale_checks.py` and its certificate check all recorded raw-scale fibres, signed integer-q period equivalences, positive returned witnesses, first-half gates, total decoded bits, PCT/full radix inverses and the original oriented divisors. Its complete finite scaled prime-incidence fixture retains all factors and all scale lifts, checking both projection counts and same-tuple Boolean selections. Exact sizes and input ranges are recorded in its JSON certificate.

These computations check bounded instances; the general conclusions above rely on the reviewed proofs. The peer subreview files supply another independent check of the arithmetic maps. The separate `THREE_REQUIREMENT_AUDIT.md` and JSON cover 85 changes of presentation, retaining the initial TR-001/TR-002 failures and the continuation domain/orientation findings with their exact accepted repairs. The previous 37-statement reports are preserved under `history/37_statement_review/`; the inaccurate pre-orientation 47-statement pass is preserved under `history/47_statement_pre_orientation_repair/` with PR-006/007 explicitly superseding its no-hit verdict.

## Limits of the verdict

- This is a deductive mathematical review, supplemented by finite exact computations; it is not Lean or another proof-assistant verification.
- Coverage is exactly the fifteen source hashes recorded here, plus the identified unlabelled arithmetic paragraphs. Later changes require checking their effect on this review.
- This review does not independently certify the full reading history, bibliographic novelty, source crosswalk completeness, or all claims in the supplied original notes; those are separate parent tasks.
- No universal shell occupancy, total monotone propagation, infinitude of prime specializations, or global Erdős–Straus conclusion follows from these partial successor domains.
- The exact bounded CRT algorithm is finite and may have exponential cost; the proof makes no polynomial-time or nonempty-output guarantee.
- The canonical localization theorem starts with the stated existing positive primitive norm endpoints. It does not construct such endpoints for every prime.
- The affine corrections act on the underlying embedded sets/torsors. For nonzero correction they are not additive homomorphisms and are not asserted to be morphisms of the Connes divisor category or topos points.
- Source receipts distinguish the 165-page and 166-page NS PDFs. The recorded operator and mean-correction passages and pinned static source locators were compared by the identified source/repair reviewers; neither complete NS proof or full-PDF equivalence is independently certified, and no Lean process was launched.

This review tranche edits proof_review records/scripts and SOURCE_CLAIM_MORPHISMS.json only. Root owns manuscript integration and PDF QA. No Lean runs, remote changes, or publication.

## Current reverse and boundary review provenance

Read both complete frozen reverse proof files and rechecked all ten statements, their typed maps, constants, inverse domains, kernels, full fibres, analytical convergence and unlabelled source-return calculations. This record author made no mathematical source edits.

This record is an independent read of all ten final statements relative to their mathematical authors and repair author. The separate read-only transfer_audit reviewed the first three statements and the later changed passages; its smooth-file follow-up covers S17 only. Earlier analytic review is historical evidence. No broader second-review scope is claimed.

The current repair author compared the retained 166-page source equations (6.1)-(6.7), (6.17)-(6.20), (8.4)-(8.10), (8.14), and (8.19)-(8.23), and the explicitly cited pinned Lean source lines. The record author inspected the resulting exact mathematical maps; complete source-PDF or Lean kernel verification is not claimed.

Read the complete final four-statement boundary source, every proof and both unlabelled R7 companions, without editing its mathematics. Checked original raw-scale inverses, all six obstruction table rows, every group action and orbit fibre, code decoder and comparisons against the full original radices.

boundary_swap/CHECKER_REVIEW.md records a separate read-only reviewer and exact finite checker. The final source edit was a layout-only gathered display split, which that reviewer inverted to reconstruct its previously reviewed source hash before rechecking the final hash.

The reverse exact checker binds both final proof hashes and checks5100 DFT/sample identities,64 obstructions,16 spectra,13293 full-preimage points,84 Gram checks,60 cover-direction checks,4800 derivative and4416 inverse frequency pairs,204 affine-fibre DFTs,80 Pell identities and864 typed inverse identities. The boundary checker binds its final proof hash and checks70 eligible primes,33012 complete shells,2141138 raw tagged candidates,57056 rational compositions,28020 original code differences,33012 full shell hit-set comparisons and140 global minima;102 occupied-R3 comparisons verify the exact first-code formula. The previous finite checks are carried forward with unchanged source/script hashes; they were not needlessly re-executed for these new records.

The current complete transformation audit has85 entries in15 proof files. The historical58-statement reports remain under history/58_statement_before_reverse_map. The current proof-review checkpoint does not certify PDF rendering or DOI publication; root retains those separate receipts.
