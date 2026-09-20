# Dated proof bulletin — 20 September 2026

This bulletin records the new ES–Fable–weighted-conductor bridge with stable result IDs and proof locators. It is a mathematical index, not a programme chronology. The complete derivations are in [the crosswalk](research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex), and the exact symbolic receipt is [here](research/incoming/es-fable-zeta-bridge-20260920/verification_receipt.json).

## SZ-20260920-019 — normalized ES quartic and intrinsic prime

For every ordered positive solution `4/p=1/x+1/y+1/z`, the normalized binary quartic

```text
-(p+x+y+z)^{-1}(U-pV)(U-xV)(U-yV)(U-zV)
```

has fixed `U^3V` coefficient one, recovers `p=-5u4/u3`, and satisfies

```text
625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0.
```

On `u0u3u4 != 0` the converse holds algebraically: the recovered `p` is a root, and the other roots satisfy the ES reciprocal equation when nonzero.

- **Proof:** crosswalk, EZ6–EZ10.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.
- **Antecedent strengthened:** canonical corpus unit `PUBUNIT-1C9A160031EECC8F3F032D4D`, generic resultant-one ES quartic carrier.

## SZ-20260920-020 — complete eight-point signed fibre

When the four arithmetic roots are distinct, the target lies in `u0 Disc(H) != 0` and its complete Fable fibre consists of two explicitly displayed source points over each of `p,x,y,z`. The full discriminant is

```text
(p+x+y+z)^(-6) product_{j<k}(t_j-t_k)^2.
```

- **Proof:** crosswalk, EZ11–EZ14; upstream GF1–GF18.
- **Certificate:** new crosswalk checker plus `upstream/independent/verify_global_fibre.py`.

## SZ-20260920-021 — the prime-marked resultant-one pair

With `Delta_p=(p-x)(p-y)(p-z)`, the two choices `lambda^2=-(p+x+y+z)/Delta_p` give the exact prime-marked factor pairs. They satisfy `LC=H_ES`, `Res(L,C)=1`, `ad+bc=1` and `4af-be=0`. The remaining six states mark the denominators rather than the prime.

- **Proof:** crosswalk, EZ15–EZ17.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.

## SZ-20260920-022 — every Turn 7 exterior target is in the étale locus

For the retained exterior normalization, `x<p`, `x<y<z`, `z>p`, and `y!=p`. Thus every actual Turn 7 exterior state has four distinct roots and lands in the genuine degree-eight locus, not the nonproper boundary. On the strict real chamber, the intrinsic prime and sorted remaining roots reconstruct all exterior coordinates.

- **Proof:** crosswalk, EZ18–EZ23.
- **Strengthens:** `SZ-20260919-006`, by embedding its complete marked-cubic inverse in the global signed quartic cover without losing the arithmetic inverse.

## SZ-20260920-023 — separate seven-state reciprocal suspension

The reciprocal cubic with roots `p/x,p/y,p/z` has a canonical quartic suspension on `u0=0`. For distinct denominators it has exactly seven states: two over each finite root and one infinity-chart point. It lies on the nonproper hyperplane and is not identified with the eight-state arithmetic quartic.

- **Proof:** crosswalk, EZ24–EZ28.
- **Certificate:** `verify_es_fable_zeta_bridge.py` and upstream GF1–GF18.

## SZ-20260920-024 — fixed weighted-conductor transport

The invertible maps `Phi_*` and `Psi_*` transport the nonlinear Fable map and all of its fibres through the original conductor identity `T_A,* Phi_*=Psi_*`. Kernels are zero; fibres, deck action and exceptional loci are preserved. `Psi_*` is the receiving isomorphism and is not renamed as the conductor.

- **Proof:** crosswalk, EZ29–EZ35; upstream FC26–FC35.
- **Literature:** exact Meixner–Pollaczek formulas in DLMF 18.19.8–9, 18.22.8 and 18.23.7.
- **Nonclaim:** no ES root is thereby identified with a zeta zero.

## SZ-20260920-025 — root-algebra isomorphism and exact projective obstruction

A chosen bijection between the four ES roots and four fixed reference roots induces an explicit evaluation/Lagrange-interpolation algebra isomorphism with zero kernel. A single Möbius realization exists exactly when the corresponding cross ratios agree up to relabelling. Failure of that stronger map is an exact obstruction, not a claim of disconnection.

- **Proof:** crosswalk, EZ36.

## SZ-20260920-026 — exact symmetric quotient and smooth arithmetic chart

Let `s1=x+y+z`, `s2=xy+xz+yz`, `s3=xyz`, and `S=p+s1`.  On the nonzero chart, the scheme `p*s2=4*s3` modulo permutations of `x,y,z` is isomorphic—not merely mapped—to `V(G) intersect D(u0*u3*u4)`.  The complete inverse is

```text
p  = -5u4/u3,
s1 = -1/u0 + 5u4/u3,
s2 = 4u3^2/(25u0u4),
s3 = -u3/(5u0).
```

The polynomial `G` is irreducible. Its scheme-theoretic singular ideal is displayed in the proof, and its reduced singular support is exactly `u3=u4=0`; hence the entire arithmetic chart is smooth.  Denominator collisions and collisions of `p` with a denominator are different divisors inside this smooth chart.  They can occur for positive solutions—for example `(3;1,6,6)` and `(5;2,5,10)`—so the eight-point fibre statement is restricted to the distinct-root locus and, in particular, the proved Turn 7 exterior chamber.

- **Proof:** crosswalk, EZ9a–EZ9h.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.
- **Strengthens:** `SZ-20260920-019` from an algebraic converse to an exact quotient isomorphism.

## SZ-20260920-027 — explicit receiver equation and prime-state selector

Forward substitution through `B_v^{-1}`, evaluation at the four fixed reference roots, and multiplication by the retained matrix `K` give four explicit receiver linear forms `U0,U2,U3,U4`.  In those coordinates the ES image is cut out by

```text
F_*(r)=625U0U4^3-125U3U4^2+25U2U3^2U4-4U3^4=0.
```

This polynomial is exactly `G(Psi_*^{-1}r)`, is nonzero and irreducible, and recovers `p,s1,s2,s3` by the formulas in `SZ-20260920-026` with `uj` replaced by `Uj`.  The factor pair over the distinguished prime is written in all six factor coordinates, and the polynomial equation

```text
5A(z)U4(r)-A(z)Y(z)U3(r)-iU3(r)=0
```

selects exactly the two prime-marked states among the eight receiver states on the distinct-root locus.  The conductor preserves all four recovered coefficient forms exactly.

- **Proof:** crosswalk, EZ34a–EZ34n.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.
- **Dependencies:** `SZ-20260920-021`, `SZ-20260920-024`, `SZ-20260920-026`.
- **Nonclaim:** the fixed reference roots and moments are not identified with the arithmetic roots or zeta zeros.

## SZ-20260920-028 — complete prime-local reciprocal Fable fibre

For every original \(p\equiv1\pmod4\) exterior or middle state, the suspended
reciprocal cubic has seven reduced geometric affine inverse points and exactly
three points over \(\mathbb Q_p\).  The complete algebras are
\[
E:\mathbb Q_p^3\times K_{\rm ram}^2,\qquad
M:\mathbb Q_p^3\times K_{\rm unr}^2.
\]
The two ramified fields of a fixed exterior state are isomorphic but
state-dependent; the two middle fields are copies of the unique unramified
quadratic extension.  The common count of three local points therefore does
not identify the two fibres.

- **Proof:** cumulative crosswalk, EZ28a–EZ28k; corrected Turn 7 Fabel source.
- **Certificates:** incoming main, independent, and whole-polynomial checks.
- **Literature:** Elsholtz–Tao, §2, Propositions 2.2 and 2.6; Hatcher,
  §6.4; Milne, Chapter 7.

## SZ-20260920-029 — root-order conductor and exact interpolation loss

For the ordered reciprocal roots,
\[
\mathcal O_E=\{(z_1,z_2,z_3)\in\mathbb Z_p^3:z_1\equiv z_2\pmod p\},
\qquad\mathcal O_M=\mathbb Z_p^3.
\]
The first order has normalization quotient \(\mathbb F_p\) and conductor
\(p\mathbb Z_p\times p\mathbb Z_p\times\mathbb Z_p\).  The unique labelled
exterior-to-middle quadratic interpolation has coefficient valuations
\((0,-1,-1)\) and \(pF(T)\equiv cT(T-4)\pmod p\), \(c\ne0\); the reverse
interpolation is integral.  The composition divisibilities hold in
\(\mathbb Q_p[T]\), not in general in \(\mathbb Z_p[T]\).

- **Proof:** cumulative crosswalk, EZ28l–EZ28q; corrected root-order source.
- **Correction retained:** middle roots have distinct reductions and all
  derivative values are units, but derivative residues need not be pairwise
  distinct.

## SZ-20260920-030 — corrected negative-four-square channel transfer

Let an existing exterior state have shape coordinate
\(\alpha=-4c^2\) or \(\beta=-4c^2\), and put \(j=(h+1)/4\).  On the exact
selected-word domain \(c\mid j\), set
\[
Q=h,\qquad
U=c^2\ \text{in alpha},\qquad
U=(j/c)^2\ \text{in beta},\qquad
R_M=(p+4U)/h,\qquad A_M=(p+R_M)/4.
\]
These formulas construct an original middle state at the same prime, with the
full primitive normalization and ordered denominators displayed in the proof.
Every already-existing state on \(\alpha=-4\) or \(\beta=-4\) therefore
returns, without a bound on the other coordinate.

The complete alpha inverse fibre must also impose the original exterior gate
\(R_s\mid4hr^2+1\), equivalently \(R_s\mid pr+s\).  Omitting it admits the
false candidate \(p=5209,h=95,c=2,s=5,r=4,R_s=2391\), for which
\(2391\nmid6081\).  The supplied executable verifier already imposed the gate;
the corrected source now does as well.

- **Proof:** cumulative crosswalk, EZ28r–EZ28z; corrected Turn 7 Fabel source.
- **Certificates:** incoming main and independent replays.
- **Scope:** the theorem transfers existing sources; it does not show that
  either line is infinitely occupied or that every prime supplies a source.

## SZ-20260920-031 — complete fixed-cofactor middle fibre

Let an existing exterior state have (h\equiv3\pmod4) and put
(j=(h+1)/4).  The complete finite set

\[
\mathcal U_{p,h}=\{U>0:U\mid j^2,\ h\mid p+4U\}
\]

is in bijection with all original middle states at the same prime whose
normalized cofactor is (Q=h).  The bijection retains every coordinate:

\[
R_U=(p+4U)/h,quad A_U=(p+R_U)/4,quad g_U=\gcd(j,U),
\]

\[
h_U=g_U^2/U,quad r_U=U/g_U,quad
\lambda_U=j/g_U,quad s_U=R_U\lambda_U-r_U.
\]

It is onto, not merely a construction: an arbitrary original M state with
(Q=h) recovers (U=u_M) and satisfies
(\gcd(j,U)=h_Mr_M).  In the negative-square alpha and beta slices, the
congruences are respectively (U\equiv c^2\pmod h) and
(c^2U\equiv j^2\pmod h).  Hence (c\mid j) is exact for the two earlier
selected words, but is not necessary for another fixed-(Q) word to return.

At the prime (p=41161), the existing E state with
((h,\alpha,c,j)=(11,-100,5,3)) has (5\nmid3), yet (U=3) gives

\[
\frac4{41161}=\frac1{11226}+\frac1{462073386}+\frac1{123483}.
\]

Conversely, the certified (p=3049,h=31,j=8,c=6) exterior state has an empty
fixed-(Q) divisor fibre.  Composed with the earlier diagonal and
radius-eight theorems, the proved residual exterior source has shape radius at
least nine.

- **Proof:** cumulative crosswalk, EZ28P–EZ28X; corrected
  `fixed_cofactor_atlas.tex`.
- **Certificate:** `verify_integration_extensions.py`; exact comparison with
  every recorded M state for the preserved scan gives 1,293 eligible E-source
  incidences, 933 source-target incidences and 511 distinct targets.
- **Nonclaim:** the map starts from an existing E source and does not force
  occupancy at a prescribed unoccupied prime.

## SZ-20260920-032 — exact elementary transform between the two Fable quartics

On the distinct-root arithmetic chart, the normalized literal-root quartic
(H_{\rm ES}) and the reciprocal suspension are related by

\[
\boxed{H_{\rm rec}(U,V)=\frac1{u_4}\frac{V}{U-V}H_{\rm ES}(pV,U)
=V\prod_{i=1}^3\left(U-\frac p{x_i}V\right).}
\]

This is inversion (T\mapsto p/T), deletion of the marked root (1),
insertion of infinity, and retained normalization.  It is not a single
projective linear transformation.  The reciprocal coefficient target forgets
exactly the common scale (p), and the inverse formulas recover
(u_0,u_2,u_3,u_4) once (p) is retained.  The projective degree-four root
schemes are explicitly isomorphic by

\[
T\mapsto\frac p{s_3}(X^2-s_1X+s_2),\qquad
X\mapsto\frac p{e_3}(T^2-4T+e_2).
\]

The collision and discriminant divisors transport exactly.  The signed covers
meet in a 14-point fibre product.  A direct generic rational signed-cover map
is obstructed by the derivative-twist square class; after adjoining its three
square roots, the projective covers correspond 8-to-8.  Passing to the affine
reciprocal chart loses exactly the second sign above the marked prime, giving
the observed 8-to-7 count.

- **Proof:** cumulative crosswalk, EZ28A–EZ28O.
- **Certificate:** `verify_es_fable_zeta_bridge.py`, schema 4, including the
  exact polynomial transform, coefficient inverse, root-scheme remainders,
  discriminant transport and derivative twist.
- **Nonclaim:** the obstruction to a direct signed map is not a claim that the
  two constructions are unrelated; the fibre product and quadratic
  trivialization are the exact relation.

## SZ-20260920-033 — exact three-dimensional raw-cell transport

The canonical project reader's retained raw-cell map is

\[
\Phi_\triangle=
\begin{pmatrix}
5/8&0&3/4&5/8\\
0&1&0&0\\
3/8&0&5/4&3/8\\
1/2&0&0&-1/2
\end{pmatrix},
\qquad \det\Phi_\triangle=-1/2.
\]

It sends the four stated raw vertices to one Lorentz-norm-one vector and
three null vectors.  Their spatial projection has face edges \(2\sqrt3\),
apex edges \(\sqrt{65}/4\), Euclidean volume \(\sqrt3/4\), and exact
face-centroid displacement

\[
\bar p_{\rm face}-p_\ast=(0,1/4,0).
\]

- **Proof:** cumulative crosswalk, EZ35A–EZ35D.
- **Certificate:** verify_fable_es_raw_tetrahedron.py.
- **Human-source locator:** Erdős–Straus Project Reader, Zenodo record
  21845035, theorem thm:Fable-ES-raw-tetrahedron-quarter-altitude.

## SZ-20260920-034 — exact odd receiving divisor on the ES locus

For the odd half-difference matrix \(O\), direct reduction of all four
component polynomials gives

\[
\det O=\varepsilon_{\rm br}\frac{4\mathfrak D_{\rm odd}(A,B,C,D)}{A^3}.
\]

On the normalized ES coefficient map, with
\(T=s_1/p\) and \(Z=s_3/p^3\),

\[
\mathfrak D_{\rm odd}\circ\Theta
=\frac{p^2\Phi(T,Z)}{(1+T)^6},
\]

where the degree-six polynomial \(\Phi\) is printed in EZ45 and is primitive
and irreducible over \(\mathbb Q\).  The supplied regular target
\((1,0,-60/431,0)\) is not on the ES hypersurface:

\[
G(1,0,-60/431,0)=-\frac{51840000}{34507149121}.
\]

- **Proof:** ODD_RECEIVER_ES_PULLBACK.tex, EZ37–EZ46.
- **Certificate:** verify_odd_receiver_es_pullback.py, with independent
  SymPy, python-flint, and mod-\(11\) irreducibility checks.

## SZ-20260920-035 — positive-real intersection and arithmetic residue

On the exact positive-real family

\[
\frac px=\frac14-\delta,\qquad
\frac py=\frac14+\delta,\qquad
\frac pz=\frac72,\qquad p=1,\quad w=\delta^2,
\]

the pulled-back odd divisor is

\[
-\frac{8Q(w)}{(144w-65)^6},
\]

with the integer polynomial \(Q\) printed in the proof.  The exact endpoint
values satisfy \(Q(10^{-6})<0<Q(10^{-4})\), proving an intersection with the
positive-real, pairwise-distinct ES locus.  A positive rational point on this
divisor is prime-integral exactly when

\[
\Phi(T,Z)=0,\qquad X^3-TX^2+4ZX-Z
\]

splits into three distinct positive rational roots, none equal to \(1\), and
their least common denominator is \(1\) or a prime.

- **Proof:** ODD_RECEIVER_ES_PULLBACK.tex, EZ47–EZ48.
- **Nonclaim:** the real sign change does not supply a rational divisor point.

## SZ-20260920-036 — every hard-prime witness enters the eight-sheet domain

If \(p\equiv1\pmod {12}\) is prime and
\(4/p=1/x+1/y+1/z\) with positive integral denominators, then
\(p,x,y,z\) are pairwise distinct.  After ordering \(x<y<z\), put

\[
R=4x-p,\qquad s_p=\frac{p(p+3)}4,\qquad
B_p=p+s_p(s_p+1).
\]

Then \(3\le R\le2p-3\), \(S=p+x+y+z\le B_p\), and

\[
\Disc(h_u)\ge\frac{144}{B_p^6},\qquad
\frac2S\le|h_u'(t_j)|\le S^2,\qquad
\frac1S\le|\xi_j|\le\sqrt{S/2}.
\]

The full inverse coordinates obey

\[
|y_j|\le2S,\qquad |z_j|\le6S^2,\qquad |w_j|\le41S^3.
\]

- **Proof:** FIXED_INPUT_BOUNDARY_MONODROMY.tex, EZ49–EZ56.
- **Certificate:** verify_fixed_input_boundary.py.
- **Scope:** the theorem controls every witness at a fixed hard prime; it
  does not prove occupancy.

## SZ-20260920-037 — fixed-input order-\(48\) signed cover

For fixed \(p\ne0\), the coefficient relations give

\[
h_u(r)=(r-p)g_p(r),\qquad
g_p(r)=Ar^3+(1+Ap)r^2-\frac{4C}{5p}r+\frac C5.
\]

On \(A C g_p(p)\Disc(g_p)\ne0\), the signed algebra splits into a
rank-two marked-prime factor and a rank-six denominator factor.  Its
monodromy is

\[
G_p=\{(\sigma,\pi):\pi(p)=p,\ \prod_j\sigma_j=\operatorname{sgn}\pi\},
\qquad |G_p|=48,
\]

and its deck group is \(C_2\times C_2\).  In even/odd coordinates the
representation is

\[
\mathbf1^{\oplus2}\oplus V_2\oplus\chi_{\det}\oplus V_3.
\]

The averaged Gram form therefore retains a full \(2\times2\) block on the two
trivial summands, plus the displayed scalar blocks on the other three
summands.

- **Proof:** FIXED_INPUT_BOUNDARY_MONODROMY.tex, EZ57–EZ66.
- **Certificate:** verify_fixed_input_boundary.py enumerates group order
  \(48\), sheet orbits \(2,6\), and deck centralizer order \(4\).

## SZ-20260920-038 — finite rank-eight collision completion

With \(\eta=\xi^{-1}\),

\[
\widehat{\mathcal S}
=\mathcal R_0[r,\eta]/(h_u(r),\eta^2-h_u'(r))
\]

is finite flat of rank eight and agrees with the original inverse after
inverting \(\eta\).  At an \(m\)-fold root,

\[
\widehat{\mathcal S}_{r_0}
=\mathbb C[\varepsilon,\eta]/
(\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1}).
\]

A double root gives \(\mathbb C[\eta]/(\eta^4)\).  The rational ES boundary
family \((p;p,2p/5,2p)\) has
\(\eta_{\rm ES}^2=(3p/11)\varepsilon_{\rm ES}\); the auxiliary paired-root
fibre has
\(\eta_{\rm pair}^2=4\gamma^2\varepsilon_{\rm pair}\).  The map

\[
\varepsilon_{\rm ES}\mapsto\varepsilon_{\rm pair},\qquad
\eta_{\rm ES}\mapsto c\eta_{\rm pair},\qquad
c^2=\frac{3p}{44\gamma^2}
\]

is an exact length-four local-algebra isomorphism.  The original inverse
still has its \(\eta^{-1}\) pole.

- **Proof:** FIXED_INPUT_BOUNDARY_MONODROMY.tex, EZ67–EZ76.
- **Scope:** this is a local algebra/action map, not a global ES–zeta
  identification.

## SZ-20260920-039 — invertible marked odd-moment frame

On the ordered signed-root cover, let

\[
U=(r_j^{\,k})_{0\le k\le3,\,1\le j\le4}
\operatorname{diag}(\xi_1,\xi_2,\xi_3,\xi_4).
\]

Then

\[
\det U=\frac{\chi}{A^2},\qquad \chi\in\{1,-1\}.
\]

If \(V_h\) is the ascending coefficient matrix of the four reduced odd
component polynomials, the original odd evaluation factors exactly as
\(O=V_hU\).  The complete inverse is

\[
\begin{aligned}
\beta_j=\xi_j\bigl[&
(C+Br_j+r_j^2+Ar_j^3)m_0\\
&+(B+r_j+Ar_j^2)m_1+(1+Ar_j)m_2+Am_3\bigr].
\end{aligned}
\]

Thus the extra odd receiving divisor is in \(V_h\), not in the marked moment
carrier.

- **Proof:** FIXED_INPUT_BOUNDARY_MONODROMY.tex, EZ77–EZ80.
- **Certificate:** verify_fixed_input_boundary.py.

The frozen cumulative packet also contains the previously numbered global Fable/conductor results `SZ-20260920-009` through `SZ-20260920-014`, `SZ-20260920-017`, and `SZ-20260920-018`. [Audit notes](research/incoming/es-fable-zeta-bridge-20260920/AUDIT_NOTES.md) record the endpoint-label, fixed-frame and signed-evaluation qualifications discovered on independent replay.

## SZ-20260920-040 — complete fixed-target capacity trichotomy

For \(h=4j-1>t>0\), put

\[
\mathcal A_t(j)=\{W>0:W\mid j^2,\ W\equiv t\pmod h\}.
\]

Every word is uniquely one of: the canonical word \(W=t\), present exactly
when \(t\mid j^2\); the companion \(W=4tj\), present exactly when
\(4t\mid j\); or a finite word with unique data

\[
1\le\ell\le\left\lfloor\frac{t-2}{4}\right\rfloor,
\quad w\mid\ell^2,
\quad n=\frac{t-w}{4\ell+1}>0,
\quad V=\frac{\ell^2}{w},
\quad j=\ell+4nV,
\]

and \(W=j^2/V=t+nh\). The inverse is

\[
n=\frac{W-t}{h},\qquad V=\frac{j^2}{W},\qquad
\ell=j-4nV,qquad w=\frac{\ell^2}{V}.
\]

- **Proof:** `research/incoming/es-turn07-capacity-completion-20260920/core.tex`,
  Theorem `thm:capacity`, equations (7)--(10).
- **Strengthens:** SZ-20260920-031 by solving every fixed-target divisor word.

## SZ-20260920-041 — sharp finite boundary and returned-grade reduction

Every finite word satisfies

\[
h\le t^2-3t+1.
\]

Equality holds exactly for

\[
w=n=1,\qquad t=4\ell+2,\qquad
j=\ell(4\ell+1),qquad W=(4\ell+1)^2.
\]

Beyond the strict boundary, the exact count is

\[
|\mathcal A_t(j)|=\mathbf1_{t\mid j^2}+\mathbf1_{4t\mid j}.
\]

For every finite word the reconstructed middle grade obeys
\(h_M\le\ell<t/4\).

- **Proof:** same source, Theorem `thm:bound`, equations (11)--(15).
- **Depends on:** SZ-20260920-040.

## SZ-20260920-042 — automatic alpha and beta returns

For every original exterior state with shape coordinate \(\alpha=-4t\), the
canonical word is forced for \(t=1,2,3\). For every original exterior state
with \(\beta=-4t\), it is forced for every \(t\mid36\). These statements
include nonsquare coefficients. Each word is converted by the exact return
map into a positive integral original middle state at the same prime.

- **Proof:** same source, Theorem `thm:auto`, equation (16), with the complete
  same-grade return in equations (5)--(6).
- **Antecedents:** the \(t=1\) and square special cases of SZ-20260920-030.

## SZ-20260920-043 — prime-realized sharpness

For every \(t\equiv6\pmod{420}\), the equality data of SZ-20260920-041 occurs
on original exterior states at infinitely many primes \(p\equiv1\pmod{840}\).
The construction uses

\[
h=t^2-3t+1,\qquad R=t^2+t+1,\qquad
r_0=\frac{t+2R}{4},qquad p=4hr-R,
\]

with an explicit reduced CRT progression for \(r\). The displayed prime
\(p=825241\) gives the exact nonsquare return \(W=25\) at \(t=6\).

- **Proof:** same source, Theorem `thm:sharp`, equations (17)--(18).
- **Literature dependency:** Dirichlet's theorem on primes in reduced linear
  progressions, with the modulus and coprimality proved in the source.

## SZ-20260920-044 — infinite fixed-coefficient same-grade obstruction

For each fixed \(t\ge4\), there are infinitely many hard primes carrying an
original exterior state with \(\alpha=-4t\) for which
\(\mathcal A_t(j)=\varnothing\). The construction chooses a unit class
\(A\not\equiv-1\pmod{4K(t)}\) with the exact quadratic character, then uses
two reduced Dirichlet progressions to construct \(R\) and \(p\). Since
\(h>t^2-3t+1\), the finite branch is absent; the chosen class removes the
canonical branch, and therefore also the companion.

- **Proof:** same source, Theorem `thm:obstruct`, equations (19)--(21).
- **Nonclaim:** every constructed prime already has its displayed exterior
  solution. This is an obstruction only to the complete middle box at the
  retained cofactor \(Q=h\), not a counterexample to Erdős--Straus.

## SZ-20260920-045 — positive-real rank-three crossing and integral dichotomy

The exact positive-real solution family

\[
(p;x,y,z)=p\left(1,\frac{t}{4t-402},\frac{t}{202},\frac{t}{200}\right),
\qquad t>202,
\]

has \(0<x<p<y<z\). Its odd receiving determinant has a unique simple zero
\(t_*\) in

\[
\frac{3520743}{6176}<t_*<\frac{3562358}{6249},
\]

and at this parameter \(\operatorname{rank}O(t_*)=3\) while
\(A\operatorname{Disc}(h)\ne0\). For distinct positive integral roots,
\(N=S^6F\in\mathbb Z\); either \(N=0\), or

\[
|\det O|\ge\frac4{S^3},\qquad
\|O^{-1}\|_2\le\frac{41^3}{4}S^{12}.
\]

- **Proof:** research/incoming/es-rh-multi-20260920/proofs/01_ES_FRAME_AND_ARITHMETIC.md, Sections 3--4.
- **Certificate:** research/incoming/es-rh-multi-20260920/checks/check_es_slice.py.
- **Depends on:** SZ-20260920-034, SZ-20260920-035 and SZ-20260920-039.
- **Scope:** interface theorem; the crossing is not an integral witness and
  arithmetic nonvanishing of \(N\) remains open.

## SZ-20260920-046 — perfect residue pairing and exact trace-degenerating map

On the rank-eight collision completion, the residue Gram is perfect with
\(\det\mathcal J=A^{-8}\), and

\[
\operatorname{Tr}(M_f)=\Lambda(2\eta^3f),\qquad
\det(\operatorname{TraceGram})=
\frac{256\operatorname{Disc}(h)^3}{A^{14}}.
\]

At an \(m\)-fold root the local algebra has length \(2m\), while
multiplication by \(2\eta^3\) and the trace pairing have rank one. The exact
local ES/RH algebra isomorphism changes the residue functional by the unit

\[
u_E=c^3\left[1+\left(\frac{2}{3p}+\frac{s i}{\gamma}\right)
\varepsilon_E\right].
\]

The original metric pole remains, with the unconditional lower bound
\(|\eta|\|Fq\|_Q\ge\sqrt{\lambda_{\min}(F^*QF)}\).

- **Proof:** research/incoming/es-rh-multi-20260920/proofs/02_RESIDUE_TRACE_AND_BOUNDARY.md, Sections 1--5.
- **Certificates:** research/incoming/es-rh-multi-20260920/checks/check_residue.py and checks/check_local_transport.py.
- **Depends on:** SZ-20260920-024 and SZ-20260920-038.
- **Scope:** exact local boundary interface, not a global ES--zeta identification.

## SZ-20260920-047 — residue-to-native Gram multiplier with retained defect

For the native monic orthogonal polynomial \(p_n\), the original moment Gram
is exactly

\[
H_{n-1}=J_pq_{n-1}(C_p),
\]

where the second-kind multiplier \(q_{n-1}\) retains the original mass. For
an arbitrary monic root polynomial \(h\), including an ES quartic,

\[
H_{ij}=[J_hk(C_h)]_{ij}
+\int h(x)\operatorname{quo}_h(x^{i+j})\,d\rho(x).
\]

Thus the relation defect is an explicit original-moment term and cannot be
dropped merely because the two algebras have the same finite dimension.

- **Proof:** research/incoming/es-rh-multi-20260920/proofs/03_NATIVE_GAUSS_PAIRING.md, Sections 1--4.
- **Certificate:** research/incoming/es-rh-multi-20260920/checks/check_gauss_bridge.py.
- **Depends on:** SZ-20260920-019 and SZ-20260920-046.
- **Scope:** cross-programme typed bridge; it does not make ES roots native
  Gauss nodes or establish occupancy.

## SZ-20260920-048 — inverse-trace native moment margin

For the unmodified monomial Gram on \([1,2]\), the shifted-Legendre
coefficient matrix gives an exact inverse and

\[
J_t\succeq\tau_t^{-1}I,\qquad
\tau_t^{-1}\le\lambda_{\min}(J_t)\le(t+1)\tau_t^{-1},
\]

with \(\tau_t=\operatorname{tr}J_t^{-1}\) and
\(\tau_t^{-1}\ge g_t\) in every degree. Moreover

\[
\tau_t\le(t+1)(2t+1)100^t.
\]

The resulting native moment tolerance is explicit, and a degree-\(L\) weight
requires moments through degree \(2t+L\).

- **Proof:** research/incoming/es-rh-multi-20260920/proofs/04_NATIVE_INVERSE_MARGINS.md, Sections 2--6.
- **Certificates:** research/incoming/es-rh-multi-20260920/checks/check_gram_floor.py and checks/check_previous_bounds.py.
- **Scope:** RH-facing conditioning result; outside the ES occupancy chain.

## SZ-20260920-049 — common-parameter quotient and Bernstein procedure

For one common diagonal uncertainty matrix \(\Theta\), every onto observation
map has the exact attained quotient

\[
G(\theta)=G_0+Z\Theta(I+K\Theta)^{-1}Z^*,
\qquad
\frac{\det G(\theta)}{\det G_0}
=\frac{\det(I+L\Theta)}{\det(I+K\Theta)}.
\]

The minimizing lift stays in the complete original source fibre. Fixed-column
current numerators have the proved coordinatewise degree bounds, exact
Bernstein subdivision gives a finite positivity procedure under a strict
margin, and native monic columns acquire the displayed rational correction
from the same parameters.

- **Proof:** research/incoming/es-rh-multi-20260920/proofs/05_MULTIPARAMETER_CURRENT_CERTIFICATES.md, Sections 1--6.
- **Certificates:** research/incoming/es-rh-multi-20260920/checks/check_lowrank.py, checks/check_bernstein.py and checks/check_additional.py.
- **Scope:** RH-facing propagation interface. The diagnostics are synthetic;
  no actual native-current sign certificate, RH theorem or ES occupancy result
  is claimed.

## SZ-20260920-050 — defining-prime integral normalization and complete Smith classification

For every positive integral witness at a prime (p\equiv1\pmod {12}), the
literal-root signed quartic order has the displayed normalization matrix

\[
\mathsf C_p=\operatorname{diag}
\bigl(V,\operatorname{diag}(p^{m_i})V\bigr),
\]

with every unit factor and closer-pair valuation retained.  On the separated
exterior and middle strata its Smith exponents are respectively

\[
(0,0,0,0,0,0,1,1),\qquad (0,0,0,1,1,2,2,3),
\]

so the normalization indices are (p^2) and (p^9).  The two independently
received derivations are proved to use the same signed orders and the same
ordered bases.

- **Proofs:** `research/incoming/es-defining-prime-continuation-20260920/DEFINING_PRIME_CONTINUATION.md`, Sections 1--4;
  `INTEGRAL_NORMALIZATION_CROSSWALK.md`;
  `research/incoming/es-turn07-integral-completion-20260920/core.tex`, Sections 2--4.
- **Certificates:** `verify_defining_prime.py` (80 exact checks), plus the
  integral module's main and independent replays (104,538 and 27,154 checks).

## SZ-20260920-051 — translated-chart twist and fixed-prime collision gluing

When (p\mid S), the translated chart is not silently identified with the
original chart.  If

\[
c_\lambda=\frac{S}{S-4\lambda},\qquad q^2=c_\lambda,
\]

then the exact base-change isomorphism is

\[
T_\lambda\longmapsto T_0-\lambda,
\qquad \sigma_\lambda\longmapsto q\sigma_0.
\]

It descends over (\mathbb Q_p) exactly when the retained square class is
trivial.  On the fixed-prime base the signed algebra is the exact rank-(2+6)
fibre product over (B/(R)[\sigma]/(\sigma^2)).  Its collision model
(B[\zeta]/(\zeta^4-t^2)) has normalization exponents ((0,0,1,1)) and
specialization kernel generated by (\zeta^2,\zeta^3).

- **Proof:** defining-prime source, Sections 3 and 5--6.
- **Depends on:** SZ-20260920-037, SZ-20260920-038 and SZ-20260920-050.

## SZ-20260920-052 — local signed-label representation and conductor-index identity

For a residue cluster (C) of (m) labels, the signed-label defect
representation is

\[
W_C\cong\mathbf1^{\oplus(m-1)}\oplus\bigoplus_{i\in C}\chi_i.
\]

It is tame, its Artin conductor is (a(W_C)=\sum_{i\in C}\epsilon_i), and

\[
2\,\operatorname{length}
(\widetilde{\mathscr E}_p/\mathscr E_p)+a(W)
=6\sum_{i<j}\nu_p(t_i-t_j).
\]

For the (p=1201) middle witness the Frobenius polynomial is
((1-T)^3(1+T)^2), with trace (1), while the integral defect length remains
(9).

- **Proof:** `research/incoming/es-defining-prime-continuation-20260920/LOCAL_GALOIS_REPRESENTATION.md`.
- **Depends on:** SZ-20260920-050.

## SZ-20260920-053 — arithmetic nonsingularity on 3,456 CRT classes

If (p\equiv1\pmod {12}) is prime and

\[
\left(\frac{-511}{p}\right)=
\left(\frac{1241}{p}\right)=
\left(\frac{-15}{p}\right)=-1,
\]

then every positive integral ES witness at (p) has nonzero receiving
numerator (N=S^6F\), hence an invertible original odd receiving frame.  The
proof exhausts the one-(p)-divisible and two-(p)-divisible denominator
patterns and retains the Type-I diagonal (x\equiv y\pmod p).  Quadratic
reciprocity gives exactly (3456) reduced classes modulo (521220).

- **Proof:** `research/incoming/es-rh-continuation-b-20260920/RESEARCH_CONTINUATION.md`, Track I, E1--E8.
- **Certificate:** `check_es_arithmetic_descent.py`, 923 exact checks jointly
  with SZ-20260920-056, including all 163 witnesses at the five diagnostic
  primes.
- **Nonclaim:** the character conditions are sufficient, not necessary.

## SZ-20260920-054 — sharp paired determinant return

For consecutive native Gram determinant ratios (r_L), the exact identity

\[
\epsilon_L^2=a_L^2\frac{(1-r_{L-1})(1-r_L)}{r_L}
\]

and (\Theta\le\epsilon_L) imply

\[
-\log(r_{L-1}r_L)\ge
2\operatorname{arsinh}(\Theta/a_L).
\]

Summing from (L=q) to (2q-1) gives the four-endpoint determinant return
printed as D10.

- **Proof:** continuation B, Track II, D1--D13.
- **Verification boundary:** the complete proof is present, but the four
  scripts behind the received Track-II/III executable receipt were not in the
  supplied evidence packet.

## SZ-20260920-055 — finite heat actions with exact remainders

For (T(t)=A-tQ) with (Q^2=0), the holomorphic heat action has the entire
outgoing-parameter expansion and dimension-independent remainder H7.  The
holomorphic and positive heat actions remain distinct and satisfy the proved
small-time comparison H13 and rational finite-stopping certificate H15.

- **Proof:** continuation B, Track III, H1--H16.
- **Depends on:** SZ-20260920-054.
- **Nonclaim:** this is a finite-dimensional constraint, not the assembled
  arithmetic action or a global endpoint theorem.

## SZ-20260920-056 — exact signed-cover descent and nonsquare twist at (q=61)

For the actual witness ((13;4,18,468)), the reduced normalized quartic has
roots (4,13,18,41) modulo (61) and derivative values (18,38,26,30), all
nonsquares.  The original signed cover has no (\mathbb F_{61})-point and
eight (\mathbb F_{61^2})-points.  The twist

\[
\eta^2=2h'(r)
\]

has eight (\mathbb F_{61})-points.  Over (w^2=2), the exact isomorphism is
(\eta_2=w\eta_1).  Frobenius is four disjoint transpositions and the finite
fibre has zeta function ((1-T^2)^{-4}).

- **Proof:** continuation B, Track IV, F1--F9.
- **Certificate:** the same 923-check independent reconstruction used for
  SZ-20260920-053.
- **Nonclaim:** this finite-fibre zeta function is not the Riemann zeta
  function.

## SZ-20260920-057 — sharp Type-I boundary lift obstruction

The added Type-I nilpotent boundary point has exactly (p) lifts modulo
(p^2) and no lift modulo (p^3).  The obstruction is the explicit nonzero
third digit.  Thus finite flat rank eight does not create an original integral
section.

- **Proof:** `research/incoming/es-turn07-integral-completion-20260920/core.tex`,
  boundary-lifting section.
- **Depends on:** SZ-20260920-050.

## SZ-20260920-058 — one-way literal-root interpolation and exact order loss

The labelled literal-root exterior-to-middle interpolation and its reverse are
written in the original bases.  One direction is integral; the other has exact
(p^2) denominator loss.  The prime-only deck sign has exact (p)-order one
in the exterior channel and two in the middle channel, so the generic deck map
need not preserve the original integral order.

- **Proof:** integral-completion `core.tex`, interpolation and conductor
  sections, with `MORPHISMS.md`.
- **Depends on:** SZ-20260920-050.

## SZ-20260920-059 — finite-place control family exposes the omitted divisor coordinate

For every prescribed finite set of primes, an explicit CRT progression gives
rational exterior and middle targets satisfying both numerical gates, the
original height bounds and the stated local signatures, while one specified
prime occurrence violates the original divisor box.  The same primes have
separately exhibited genuine integer solutions.

- **Proof:** integral-completion `core.tex` and `crt_control_note.tex`.
- **Certificates:** the integral module's main and independent replays.
- **Nonclaim:** this disproves sufficiency of those finite-place tests alone;
  it is not an all-place obstruction or an ES counterexample.

## SZ-20260920-060 — common-denominator rigidity from global traces

Let $x_1,\ldots,x_n\in\mathbb Q^\times$, $n\ge2$, have integral power
sums $s_k=\sum_i x_i^k$ for $1\le k<n$, and let
$\sum_i x_i^{-1}=m/b\ne0$ be reduced.  All $x_i$ have one common reduced
denominator $d$, and

\[
\gcd(d,b)=1,\qquad d^n\mid(n-1)!m.
\]

If $n$ is odd, $d$ is odd.  The proof uses Newton identities and the
unique least-valuation term of the first elementary symmetric function whose
minimum-valuation roots do not yet exhaust the tuple.  For reciprocal sum
$4/p$ and $n\ge3$, the divisibility excludes every denominator prime.
Consequently, for the three-denominator Erdős--Straus equation, integrality of
the first two power traces is equivalent to integrality of all denominators.

- **Proof:** `research/incoming/es-turn07-trace-rigidity-20260920/core.tex`,
  TR1--TR4; compact proof in `preprint.tex`.
- **Human antecedents:** Euler's Newton identities, cited at exact source
  locators in `references.tex`; the ES source coordinates inherited from
  Elsholtz--Tao are cited there separately.
- **Boundary:** the $n=2$ statement fails at $(p/2,p/2)$ for odd $p$.

## SZ-20260920-061 — one trace recovers the raw divisor budget and exact fibres

For the complete raw gate

\[
x=a,\qquad y=\frac{pa(U+a)}{RU},\qquad
z=\frac{p(a+U)}R,\qquad R=4a-p,
\]

the literal trace $S=p+x+y+z$ has reduced denominator

\[
\operatorname{den}S=\frac{U}{\gcd(U,pa^2)}.
\]

Thus $S\in\mathbb Z$ exactly when $U\mid pa^2$.  Its $p$-valuation
then recovers the original M or E channel, and the tag is also read from
$S\bmod p$.  Two raw words have equal trace exactly when $UV=a^2$.
Every such pair is the pair of original middle orientations; exterior and
nonintegral traces are singleton fibres.  Therefore

\[
\operatorname{rank}\ker\Phi=M_a/2,\qquad
|\Theta_{p,a}\cap\mathbb Z|=E_a+M_a/2,
\]

with basis $e_U-e_{a^2/U}$ for $U<a$ in the middle channel.

- **Proof:** trace-rigidity `core.tex`, TR7--TR16.
- **Illustration:** `figures/trace_integrality_fibres.pdf`; its $p=13$,
  $a=4$, $R=3$ sample retains every raw word and displays the unique
  two-point fibre $U=2\leftrightarrow8$.
- **Certificates:** normal and optimized runs agree on seven mathematical
  JSON tables; the integration replay passed 2,655,782 main checks and the
  separate implementation passed 331,544 checks.
- **Nonclaim:** no lower bound proved here forces an integral trace at every
  hard prime.

## SZ-20260920-062 — exact rationality boundary of the trace test

Without the complete raw gate, integer first trace leaves the exact
square-part residual

\[
d^2=\frac{R}{\gcd(R,N)},\qquad
\operatorname{den}(a^2+y^2+z^2)=d^2,
\]

for $N=y+z\in\mathbb Z$.  The package gives the full factor presentation,
the explicit $p=1009$ failure of the attempted $R=135\to15$ shell change,
and, for every hard prime, positive irrational algebraic-integer denominators
with all power traces integral and the retained middle prime-local signature.
This proves that the rationality hypothesis in SZ-20260920-060 is essential;
the algebraic targets are not Erdős--Straus counterexamples.

- **Proof:** trace-rigidity `core.tex`, TR17--TR25.
- **Certificates:** `certificates/negative_controls.json` and
  `certificates/algebraic_targets.json`, regenerated by `run_all.py`.
