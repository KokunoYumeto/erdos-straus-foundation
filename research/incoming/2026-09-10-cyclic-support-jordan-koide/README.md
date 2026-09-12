# One support, all cyclic degrees, and a reversible Koide–Jordan map

**Incoming research, 10 September 2026. Collective project: The Clankers.**

This note is an assistant-developed calculation prompted by the maintainer's research proposal. It keeps one external support scalar below a family of dimensional origins, retains the full-turn operator of a cyclic construction, and connects the original ES/Koide rational chart to an off-diagonal cubic Jordan matrix. The all-degree identities have written proofs below. The companion checker verifies finite exact instances and symbolic formulas. No proof of ES, RH/GRH, or a physical particle-mass relation is asserted. No existing accepted manuscript is changed.

## 1. One scalar support, not repeated split zeros

Let S=G(R)=R disjoint-union {tau}, with R=the real field. The old operations hold on R; tau is the new additive identity and multiplicative absorber. The supported old zero e=0_R satisfies e^2=e and e+1=1.

For any real vector space V, set V^tau=V disjoint-union {tau}. Its supported vectors retain ordinary vector addition and scalar multiplication; tau is the additive identity, and scalar tau annihilates every vector to tau. This is an S-semimodule. Scalar e sends supported vectors to the existing vector zero 0_V.

Every real-linear T:V->W extends by T^tau(tau)=tau. Direct substitution gives (QT)^tau=Q^tau T^tau and preservation of the semimodule operations. All the linear maps below therefore have an extension over the same support scalar S. The origin of R^3 is a three-coordinate vector zero, not a third externally adjoined scalar zero.

## 2. Full-turn holonomy for every degree

For finite-dimensional complex V and H in GL(V), define

```math
T_n(H)(v_0,\ldots,v_{n-1})=(Hv_{n-1},v_0,\ldots,v_{n-2}),\qquad n\ge1.
```

Then

```math
T_n(H)^n=\operatorname{diag}(H,\ldots,H),\qquad
\det(I-zT_n(H))=\det(I-z^nH).
```

Moreover, tr(T_n(H)^r)=0 when n does not divide r, and equals n tr(H^(r/n)) when it does.

**Proof.** After n shifts each component has crossed the wrap once, applying H once. Powers not divisible by n have no diagonal block. For a multiple nk the diagonal blocks are H^k. Thus, near z=0,

```math
-\log\det(I-zT_n(H))
=\sum_{r\ge1}\frac{z^r}{r}\operatorname{tr}(T_n(H)^r)
=\sum_{k\ge1}\frac{z^{nk}}k\operatorname{tr}(H^k)
=-\log\det(I-z^nH).
```

Exponentiation and polynomial identity extend the determinant equality to every z. The sign is fixed by differentiating -log(1-z).

For m,n>=1, index the nested direct sum by 0<=a<m, 0<=b<n. The permutation P_(m,n) sending index (a,b) to a+mb satisfies

```math
P_{m,n}T_m(T_n(H))P_{m,n}^{-1}=T_{mn}(H).
```

Indeed the outer shift increments a, its wrap increments b, and only the joint wrap applies H. This proves compatibility for all m,n. It is the linear-algebra realization of the cyclic direct-sum Verschiebung described by Connes–Consani [1, §3.4]. In particular H is not erased after n steps.

For H=I, S_n=T_n(I), zeta_n=exp(2*pi*i/n), the Fourier map is

```math
(\mathcal F_na)_k=\sum_{j=0}^{n-1}\zeta_n^{kj}a_j,\qquad
(\mathcal F_n^{-1}b)_j=\frac1n\sum_{k=0}^{n-1}\zeta_n^{-kj}b_k.
```

It intertwines S_n with diag(zeta_n^k). For n|m, q_(m,n)(e_j)=e_(j mod n) intertwines S_m and S_n. Its character pullback sends k mod n to (m/n)k mod m. The covering cyclic category in [2, printed p.586] retains integer translation before its cyclic quotient. These constructions explicitly record where a finite observation forgets winding.

The determinant-one lift is

```math
\widetilde S_n=e^{-i\pi(n-1)/n}S_n\in\mathrm{SU}(n),\qquad
\widetilde S_n^n=(-1)^{n-1}I.
```

The scalar factor and the even-degree central sign are retained. This action on a frame is not the scalar-center action: conjugation by zeta I is the identity, whereas conjugation by the displayed lift permutes diagonal entries.

## 3. Rank three and the three octonionic components

Let J=H_3(O), for the real octonions, with Jordan product X circle Y=(XY+YX)/2. Fix coordinates

```math
X=\begin{pmatrix}a&z&\bar y\\\bar z&b&x\\y&\bar x&c\end{pmatrix}.
```

The coordinate map R^3 direct-sum O^3 -> J is a real-linear isomorphism; its inverse reads (X_11,X_22,X_33;X_23,X_31,X_12). The full dimension is 27. The ordered diagonal frame e_1,e_2,e_3 has three primitive idempotents, and the three off-diagonal Peirce spaces each have real dimension eight [3, §§2.1, 2.7].

With L_e(X)=e circle X, the exact projection/reconstruction maps are

```math
P_{ii}=2L_{e_i}^2-L_{e_i},\quad P_{ij}=4L_{e_i}L_{e_j},\quad
X=\sum_iP_{ii}X+\sum_{i<j}P_{ij}X.
```

The cyclic real permutation P acts as a Jordan automorphism C(X)=PXP^T and gives

```math
(a,b,c;x,y,z)\longmapsto(c,a,b;z,x,y).
```

The pointwise frame stabilizer is Spin(8); triality relates its three eight-dimensional representations [3]. This imports the precise Lie-group result. It does not identify a 24-dimensional space with R^3 merely by dividing dimensions.

Retain the invariants

```math
\operatorname{tr}(X)=a+b+c,
```

```math
\operatorname{tr}(X^2)=a^2+b^2+c^2+2(N(x)+N(y)+N(z)),
```

```math
N_J(X)=abc-aN(x)-bN(y)-cN(z)+2\operatorname{Re}((xy)z).
```

The last displayed association is fixed. The real associator vanishes. All the coordinate and projection maps extend to the single supported vector space J^tau from §1.

## 4. The original rational ES/Koide chart

The source section `19_rational_koide_chart.tex` supplied in the maintainer's ES archive uses

```math
\Delta(q)=4(q_1q_2+q_1q_3+q_2q_3)-\sum_iq_i^2
=2(q_1+q_2+q_3)^2-3\sum_iq_i^2.
```

For fixed delta>0 rational, take the rational symmetric matrix M=[[a,b],[b,c]] with ac-b^2=-delta. Put

```math
D=-1-6a^2+6ab-b^2+4b,\qquad L=2-4b,
```

and retain the source open locus aLD nonzero. The map is

```math
q=D^{-1}(-D-L,-La,-L(b-a)),\qquad\Delta(q)=-1.
```

The target excludes (q_1+1)q_2(q_1+1-2q_2-2q_3)=0. Its inverse, with delta retained, is

```math
a=\frac{q_2}{q_1+1},\quad b=\frac{q_2+q_3}{q_1+1},\quad
c=\frac{b^2-\delta}{a}.
```

For completeness, write r=a, s=b-a and v=(1,r,s). Then Delta((1,0,0)+t v)=-1-tL+t^2D. Taking t=L/D and negating proves the source map. The inverse reads r,s back from q and reconstructs c from the original determinant. This repeats the source's proof so the incoming note is independently readable; no authorship of that chart is claimed.

## 5. Exact character coordinates and the lifted angle

Put omega=exp(2*pi*i/3), T=q_1+q_2+q_3, Z=q_1+omega q_2+omega^2 q_3. Then

```math
q_j=\frac{T+\omega^{-(j-1)}Z+\omega^{j-1}\bar Z}{3},\qquad
\Delta(q)=T^2-2|Z|^2.
```

The identity follows by expansion using 1+omega+omega^2=0. Thus the exact ES surface is 2|Z|^2=T^2+1. The homogeneous physical Koide cone instead has 2|Z|^2=T^2; it is not substituted for the ES surface.

Retain Z=R exp(i theta), theta real without quotienting by 2*pi. Then

```math
q_j=\frac{T+2R\cos(\theta-2\pi(j-1)/3)}3,
```

```math
q_1q_2q_3=\frac{T^3-3TR^2+2R^3\cos(3\theta)}{27}.
```

An advance 2*pi/3 permutes the ordered triple; 2*pi returns the triple but changes the retained lift. These are two explicit observation maps, not a claim that the triple alone remembers the integer.

## 6. A reversible off-diagonal extension

For t real define

```math
c_t=\frac{1-t^2}{1+t^2},\quad s_t=\frac{2t}{1+t^2},\quad
R_t=\begin{pmatrix}c_t&-s_t&0\\s_t&c_t&0\\0&0&1\end{pmatrix},
\quad X(q,t)=R_t\operatorname{diag}(q)R_t^T.
```

Direct multiplication gives R_t^T R_t=I, det R_t=1 and

```math
X_{11}=c_t^2q_1+s_t^2q_2,\quad X_{22}=s_t^2q_1+c_t^2q_2,
\quad X_{12}=c_ts_t(q_1-q_2),\quad X_{33}=q_3.
```

The remaining off-diagonal entries vanish. Since this is a real symmetric matrix inside J, its trace, quadratic trace, and cubic Jordan determinant are preserved:

```math
\operatorname{tr}X=T,\quad\operatorname{tr}X^2=\sum_iq_i^2,
\quad N_J(X)=q_1q_2q_3,
\quad 2(\operatorname{tr}X)^2-3\operatorname{tr}X^2=-1.
```

The inverse is diag(q)=R_t^T X R_t when t is retained, followed by the preceding rational inverse with delta retained. This supplies a concrete non-diagonal Jordan family with exact arithmetic return. It does not exhaust the Albert algebra or establish positivity of q as mass roots.

Example: a=1, b=3, c=8, delta=1 gives q=(-2/7,5/7,10/7). At t=1/2,

```math
X=\begin{pmatrix}62/175&-12/25&0\\-12/25&13/175&0\\0&0&10/7\end{pmatrix}.
```

It has the same exact defect -1. For arbitrary octonionic entries with fixed diagonal q, the defect instead equals Delta(q)-6(N(x)+N(y)+N(z)). Our construction compensates by moving the diagonal as well; it does not erase that term.

## 7. Scope and reproducibility

The motivation is to replace an informal rank/winding/support identification by a composable family of maps. The outcome is an all-degree holonomy identity, its compatibility with cyclic Fourier coordinates, a marked rank-three Jordan realization, and an explicit extension of the original ES rational chart. The claim that such an extension enforces arithmetic zero locations is not proved here. The full-turn H in §2 remains an input, not a modulus forced to one by support alone.

Run `python check_exact.py` and `python -O check_exact.py`. Both runs must print the same receipt. The written all-degree proof is separate from the finite test range. No Lean replay is claimed. The full uploaded source archives and copyrighted external papers are not redistributed in this PR.

## References and attribution

[1] Connes, A., & Consani, C. (2023). BC-system, absolute cyclotomy and the quantized calculus. EMS Surveys in Mathematical Sciences 9, 447–475. DOI:10.4171/EMSS/64. §3.4 supplies Frobenius/Verschiebung; the present note spells out the block maps and their invariant.

[2] Connes, A., & Marcolli, M. (2008). Noncommutative Geometry, Quantum Fields and Motives. AMS. Printed pp.586–587: cyclic covering, integer lifts and cyclic modules. Propositions 4.97 and 4.133 concern character idempotents and the separate arithmetic positivity criterion.

[3] Yokota, I. (2009). Exceptional Lie groups. arXiv:0902.0431. §§1.16, 2.1, 2.7. https://arxiv.org/abs/0902.0431

[4] Maintainer-supplied ES source: `19_rational_koide_chart.tex`, section “A rational chart bridge beyond the orthogonal obstruction,” theorem `ratkoide:birational`; inherited source attributions to Koide and Kocik remain in that manuscript. The rational-chart proof is not claimed as new here. The present off-diagonal extension is an assistant-derived continuation prompted by the maintainer; the map has no priority or physical-validation claim.
