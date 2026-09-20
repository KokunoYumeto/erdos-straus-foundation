# Erdős–Straus: objects, connections and present questions

The goal is to resolve whether $4/n$ is a sum of three positive integer
reciprocals for every integer $n\ge2$, while developing the mathematical
connections that arise in trying. This is an ongoing research programme, not
a completed proof of the conjecture. Its full arguments remain in the
[readers and source archives](README.md#start-reading).

## From the original problem to the current coordinates

A witness $(x,y,z)$ is checked exactly by positivity and
$4xyz=n(xy+xz+yz)$: multiply the reciprocal equation by the positive product
$nxyz$, or divide this integer identity by it, to obtain either direction.
If $n=mp$ with $m\ge1$ and $(x,y,z)$ solves the equation for $p$, then
$(mx,my,mz)$ solves it for $n$, since each reciprocal is divided by $m$.
Every $n\ge2$ has a prime divisor, so solving all prime inputs suffices.

Why the remaining prime classes? For a prime $p\equiv2\pmod3$, the positive
integer triple $(p,(p+1)/3,p(p+1)/3)$ works, because
$1/p+3/(p+1)+3/[p(p+1)]=4/p$.
For $p\equiv3\pmod4$, the triple
$((p+1)/4,p(p+1)/2,p(p+1)/2)$ works, because
$4/(p+1)+4/[p(p+1)]=4/p$.
These include $p=2,3$. Every prime greater than three has residue
$1,5,7$ or $11\pmod{12}$; the latter three classes are covered by the
two identities. It therefore suffices to consider $p=12h+1$, $h\ge1$.

There is a further elementary reduction: if $p=24j+13$ with $j\ge0$, then
$a=(p+3)/4=6j+4$ is a positive even integer and
$(a,pa/2,pa)$ is an integer witness, since
$1/a+2/(pa)+1/(pa)=(p+3)/(pa)=4/p$.
Thus **primes $p\equiv1\pmod{24}$ are the remaining target of this reduction**.
These identities explain the scope; they are not advertised as new results.
The supplement uses the larger $p=12h+1$ domain to state its shell maps;
working on that domain must not be confused with settling its remaining
$1\pmod{24}$ subclass.

For one such prime, a **shell** fixes the first denominator $a$ in
$A_p=\{3h+1,\ldots,9h\}$. It retains the residual $R_a=4a-p$ and
product $S_a=pa$. The remaining equation is

$$\frac1y+\frac1z=\frac{R_a}{S_a}.$$

The source constructs the finite set

$$\mathcal W_a=\{(m,n)\in\mathbb Z_{>0}^2:
m\mid S_a,\ n\mid S_a,\ \gcd(m,n)=1,\ R_a\mid m+n\}.$$

Here $n$ is a local pair coordinate, not the original conjecture's input.
For $k=(m+n)/R_a$, its ordered witness map is
$(m,n)\mapsto(a,(S_a/n)k,(S_a/m)k)$.
The reverse map, its integrality and all domain conditions are proved in
[Lemma `lem:units`](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L49).
Coordinates are not discarded merely because another description exists.

Two divisor channels encode the same full shell:

$$E_a=\{u>0:u\mid a^2,\ R_a\mid4u+1\},\qquad
M_a=\{u>0:u\mid a^2,\ R_a\mid u+a\}.$$

The full count is

$$Q_p=\sum_{a=3h+1}^{9h}\left(|E_a|+\tfrac12|M_a|\right).$$

The source proves $\operatorname{ES}(p)\iff Q_p>0$, including the full
denominator range and reconstruction in both directions. A shell is
**occupied** when its count is positive. Neither an empty single shell nor a
failed restricted search is an ES counterexample. See
[the full biconditional](research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex#L146)
and [all-shell failure criterion](research/expanded-2026-09-08/exact_bounded_transport_72/counterexample_sieve/all_shell_no_hit.tex).

## How the approaches meet

These approaches work on connected data, not five independent substitutes for
the original problem. The same divisors can be represented by their finite
vectors of prime exponents. A **bounded fibre** is the set of those vectors
satisfying specified conditions within the original exponent limits. A
**character** is a multiplicative map from an abelian group to complex numbers
of modulus one; the finite characters here encode congruence conditions.
A **witness transport** is a map whose proved domain carries actual integer
solutions, including their retained order and scale.

| Approach | Established scope in the published supplement | Research question it leaves |
| --- | --- | --- |
| Factor tests for shells | At residual $R_a=3$, occupancy is equivalent to a prime divisor of $a=(p+3)/4$ being $2\pmod3$. There is also an exact residual-seven test. [Proofs](research/expanded-2026-09-08/exact_bounded_transport_72/first_two_shell_sieve.tex). | How can the simultaneous failures of these and all later shells be excluded or realized? |
| Simultaneous congruences | The Chinese remainder and lattice calculations retain shared variables and finite exponent limits; they describe the complete bounded solution sets. [Proofs](research/expanded-2026-09-08/exact_bounded_transport_72/shared_variable_crt.tex). | What structure forces one of the actual bounded sets to be nonempty, beyond compatibility without bounds? |
| Transport of witnesses and codes | Exact successor domains, inverse fibres and swap maps are calculated. A **code** is the source's integer encoding of a candidate in its specified search order; the occupied residual-three case has an exact first code. [Proofs](research/expanded-2026-09-08/exact_bounded_transport_72/boundary_swap/boundary_swap_completion.tex). | How far can the proved maps propagate existence when their first-shell domain is empty? |
| Divisor and cyclic constructions | Connes–Consani's ordered-group constructions and cyclic coordinates represent the retained arithmetic data and its gluing obstruction. [Ordered groups](research/expanded-2026-09-08/exact_bounded_transport_72/connes_reading/connes_primitive_intersections.tex); [cyclic map](research/expanded-2026-09-08/exact_bounded_transport_72/integral_cyclic_bridge.tex). | Which consequences of these exact correspondences control bounded occupancy? |
| Torus and directional operators | A torus is the quotient $\mathbb R^2/\mathbb Z^2$ here. The integer matrix $J=((3,1),(1,5))$ gives a degree-14 cover. Complete covering fibres and corrected character sums retain arithmetic counts; directional inverse estimates have full constants. [Cover](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/torus_cover_lemma.tex); [inverse](research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/reverse_smooth_inverse.tex). | Can those operator results establish a further arithmetic implication? No full fluid theorem or ES resolution follows merely from the cover. |
| Literal-root quartic and weighted conductor | Every actual Turn 7 exterior witness gives a normalized quartic with roots $p,x,y,z$, intrinsic $p=-5u_4/u_3$, complete eight-point signed fibre, and an exact fixed-conductor square. [Proof and checks](research/incoming/es-fable-zeta-bridge-20260920/README.md). | Can the coefficient geometry force an arithmetic target to exist at an unoccupied prescribed prime? The proved map begins with a witness and does not yet supply that implication. |
| Reciprocal prime-local fibre and root order | Every original E/M state gives a seven-state reciprocal-cubic fibre. E has $\mathbb Q_p^3\times K_{\rm ram}^2$ and a root order of index $p$; M has $\mathbb Q_p^3\times K_{\rm unr}^2$ and the maximal order. A labelled rational comparison exists and loses exactly one power of $p$. [Corrected proof and audit](research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/INTEGRATION_AUDIT.md). | Which exact source-changing returns can cross this integral obstruction, and can their union force occupancy? The local classification alone starts from an existing state. |
| Negative-four-square source change | If an existing exterior shape has $\alpha=-4c^2$ or $\beta=-4c^2$ and the selected word is available, the complete formulas construct an original middle state at the same prime. Every existing state on $\alpha=-4$ or $\beta=-4$ returns, with no cutoff on the other coordinate. [Corrected proof](research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/corrected/workbench.tex). | The result does not supply a first state at a prescribed prime or prove that the two lines are infinitely occupied. The complete fixed-cofactor divisor atlas is the stronger next structural object. |
| Complete fixed-cofactor fibre | For any existing E state with $h\equiv3\pmod4$, the divisors $U\mid((h+1)/4)^2$ satisfying $h\mid p+4U$ are in exact bijection with all original M states whose normalized cofactor is $Q=h$. The formulas retain every primitive coordinate and denominator; the theorem strictly extends the selected negative-square words. [Proof and exact replay](research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/corrected/fixed_cofactor_atlas.tex). | This completes the target fibre once an exterior source supplies $h$, and removes every occupied shape of radius at most eight. It still does not construct that first exterior source at an arbitrary prime. |
| Literal/reciprocal quartic morphism | Inversion $T\mapsto p/T$, deletion of the marked root, insertion of infinity and normalization give an exact elementary transform. The coefficient map forgets precisely one common scale; the projective root schemes are explicitly isomorphic, while the signed covers meet in a 14-point fibre product and require a quadratic trivialization for an 8-to-8 correspondence. [Proof](research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex). | Can the new receiving-frame divisors or other coefficient loci constrain arithmetic occupancy? The morphism itself starts from an existing witness. |
| Three-dimensional transport and odd receiving divisor | The archived raw-cell coordinates map invertibly to a Lorentz chart by an explicit matrix and inverse. Separately, the odd receiving determinant pulls back to $p^2\Phi(T,Z)/(1+T)^6$, with primitive irreducible $\Phi$; an exact sign-changing family proves a positive-real pairwise-distinct ES intersection. A rational intersection lifts to an integral prime-numerator solution exactly under the stated splitting and common-denominator criterion. [Proofs](research/incoming/es-fable-zeta-bridge-20260920/FABLE_ES_TETRAHEDRON.tex) and [pullback](research/incoming/es-fable-zeta-bridge-20260920/ODD_RECEIVER_ES_PULLBACK.tex). | No positive rational divisor point satisfying the full prime-integral lift criterion has yet been proved. The coefficient point checked in the proof lies outside the ES hypersurface and carries no further semantic identification. |
| Fixed-input signed cover | Every positive integral witness at a prime $p\equiv1\pmod {12}$ has four distinct literal roots and explicit fixed-$p$ discriminant, derivative and inverse-coordinate bounds. At fixed nonzero complex $p$, over $\mathcal B_p=\{(A,C):ACd_p\operatorname{Disc}(g_p)\ne0\}$, the signed algebra splits into ranks $2+6$, its monodromy has order $48$, its deck group is $C_2\times C_2$, and the exact averaged metric retains a full $2\times2$ trivial block. [Proof and audit](research/incoming/es-fable-zeta-bridge-20260920/INTEGRATION_AUDIT_20260920.md). | These bounds are not uniform over $p$ and do not supply a witness at an unoccupied prime. Can the fixed-input coefficient divisors force occupancy or a further arithmetic transfer? |
| Finite collision completion and odd-moment frame | The reciprocal coordinate $\eta=\xi^{-1}$ gives a finite flat rank-eight completion. An $m$-fold root gives a length-$2m$ local algebra, a double root gives $\mathbb C[\eta]/(\eta^4)$, and the original inverse pole remains explicit. A separate marked moment frame $U$ has determinant $\pm A^{-2}$ and factors the original odd evaluation as $O=V_hU$. [Proof](research/incoming/es-fable-zeta-bridge-20260920/FIXED_INPUT_BOUNDARY_MONODROMY.tex). | The local ES--paired-root map is not a global zeta identification. Does the explicit divisor $\det V_h=0$ contain a positive rational point with prime-integral lift, or does arithmetic exclude it? |
| Fixed-target cofactor capacity | For $h=4j-1>t$, every $W\mid j^2$ with $W\equiv t\pmod h$ is uniquely canonical, companion, or an explicit finite template. The finite templates satisfy the sharp bound $h\le t^2-3t+1$, with complete equality and inverse formulas. The bound occurs at infinitely many hard-prime exterior states; for every fixed $t\ge4$, another infinite hard-prime family has an empty complete same-grade middle box. [Proof and replay](research/incoming/es-turn07-capacity-completion-20260920/INTEGRATION_AUDIT_20260920.md). | These empty boxes obstruct only the original cofactor $Q=h$; each constructed prime already has an exterior solution. Can the complete capacity classification interact with another grade or channel to force a global descent? |
| Odd-frame crossing, residue trace and native Gram | The explicit positive-real family $p(1,t/(4t-402),t/202,t/200)$ has one exactly isolated rank-three odd receiver while the quartic remains squarefree. On the collision completion, residue duality stays perfect and trace degeneration is exactly multiplication by $2\eta^3$. For a native orthogonal polynomial, $H=J_pq(C_p)$; for an arbitrary ES polynomial the complete relation defect remains. [Proof, audit and reader](research/incoming/es-rh-multi-20260920/INTEGRATION_AUDIT_20260920.md). | The real crossing is not an integral witness, and $N=S^6F$ may still vanish arithmetically. The local algebra map is not global ES--zeta transport. Actual native moments and a sign margin are still required for the RH-facing certificate. |
| Original integral signed order | In the literal-root basis, every original exterior state has normalization exponents $(0,0,0,0,0,0,1,1)$ and index $p^2$, while every middle state has $(0,0,0,1,1,2,2,3)$ and index $p^9$. Conductors, inverse lattices, reduction kernels and the Type-I boundary lift are explicit. [Proof and independent replays](research/incoming/es-turn07-integral-completion-20260920/README.md). | Finite flat rank eight and the added nilpotent boundary point do not create an original positive integral source. The remaining problem is still occupancy before normalization. |
| Defining-prime collisions and local signed characters | The complete closer-pair formula extends the E/M cases, the $p\mid S$ chart is an exact quadratic twist, and the fixed-prime algebra is a rank-$2+6$ fibre product. The signed-label representation is tame and satisfies $2\,\mathrm{length}(\widetilde{\mathscr E}_p/\mathscr E_p)+a(W)=6\sum_{i<j}v_p(t_i-t_j)$. [Proof and crosswalk](research/incoming/es-defining-prime-continuation-20260920/README.md). | The twist descends only under its retained square-class condition. Local Frobenius and conductor data are not a complex zeta operator or a universal source theorem. |
| Arithmetic receiving-frame sieve and signed descent | Three exact Legendre-symbol conditions force odd-frame nonsingularity for every witness in $3456$ reduced classes modulo $521220$. For $(13;4,18,468)$ at $q=61$, the original signed fibre has $0$ rational points and $8$ quadratic-extension points, while its specified nonsquare twist has $8$ rational points. [Proof and independent replay](research/incoming/es-rh-continuation-b-20260920/README.md). | The character conditions are sufficient, not necessary. Their failure does not certify singularity, and the finite-fibre zeta function is not the Riemann zeta function. |

The [attempt accounts](ATTEMPTS.md) explain why these directions were pursued,
what failed and what survived. The [research map](WORKBENCH.md) locates complete
proofs of the connections, including corrections and inverse fibres. The current
programme is not limited to these five routes; earlier books contain further
investigations whose history is being recovered.

## What the present record does and does not include

The [12 September continuation](research/continuation-2026-09-12/README.md)
adds JT's Boolean/cyclotomic investigation, the exact character-resolved
collision minimum and its refinement theorem, and a common-modulus affine
return map with integral hexagonal coordinates. Its full proofs and fresh
computational receipts are separate from the older indexed edition below.
At `p=1201,a=310`, character-cell energy `30<32` forces the middle target
where the unpartitioned bound is an equality and does not certify it. The
common quartic/hexagonal norm and its complete positive-square returns are
proved; norm-preserving rotation is not a norm-decreasing descent. Read its
explicit corrections together with the unchanged received papers.

The indexed edition is the 86-page supplement, version
[10.5281/zenodo.22678971](https://doi.org/10.5281/zenodo.22678971):
85 source/check files, 15 canonical TeX modules and 72 named statements.
These counts describe coverage, not novelty, significance or a truth score.
The earlier 488-page and 619-page archives remain separate source editions.
A later date does not imply that every branch has been integrated.

The current supplement has written proofs and recorded finite computational
checks. It is **not** represented as a whole-supplement Lean formalization.
Earlier Lean packages retain their own propositions, dependencies and run
receipts. [Check records](polyclank/checks.json) distinguish a mathematical
replay from file-identity and source-locator tests. Those methods support the
specific objects they check, not unexamined downstream claims.

The mathematical lineage includes Elsholtz–Tao's parametrization work,
Connes–Consani's divisor and cyclic constructions, the exact auxiliary-operator
source, and the arithmetic contributions of **u/UmbrellaCorp_HR** and
**u/CommonCareful3149**. [Literature and attribution](LITERATURE.md) give the
source roles. [Six original human directions](MOTIVATIONS.md) have been recovered
from the earlier web conversations. Recovery remains incomplete: route
motivations labelled editorial inferences are not being passed off as quotations
or as established historical derivations from those original directions.

## An independently usable research node

[workbench.json](workbench.json) exposes the problem, goal, dated edition,
source directory, inventories and cooperation links. Its records contain exact
statement locations and source hashes; complete definitions and proofs are in
the linked files. No special model, prompt script, credential test or central
registrar is required to read this research node.

An independent workbench may pursue a different route, publish an idea, check a
result through use, or challenge a step. The existing
[issue discussion](https://github.com/KokunoYumeto/erdos-straus-foundation/issues)
accepts short contributions as well as links to substantial work. The
[contribution guide](CONTRIBUTING.md) explains how source lineage, corrections,
credit and independently maintained versions remain visible. It does not assign
the next researcher's mathematics.
