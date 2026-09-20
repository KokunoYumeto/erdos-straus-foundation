**The combined continuation produces three substantive additions:** an exact order-`48` monodromy group on the fixed-input ES coefficient family; a finite rank-eight extension of the signed inverse correspondence, with explicit nilpotent fibres connecting the ES and RH degeneration calculations; and an explicit auxiliary-degree bound for the original native resolvent errors. Those errors can then be carried through the full source and observation minima without losing their complex phases.

I used the updated `erdos-straus-foundation` at commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3` and `zeta-function-research-reader` at commit `f8b73284d2e669e981bf2c7609e99f4d2b3a50be`. The ES foundation’s new literal-root quartic is the starting point—not the older mod-`107` workbench or an alternative quartic with a substituted root.

The repository results used below are identified as such. The propositions and calculations developed from them are the continuation obtained here; they are not being attributed to the repositories’ authors as already published results.

## 1. The actual ES family: a stronger domain theorem and quantitative separation

The new ES source associates to

```math
\frac4p=\frac1x+\frac1y+\frac1z
```

the quartic

```math
H_{\mathrm{ES}}(U,V) =-\frac{(U-pV)(U-xV)(U-yV)(U-zV)}{S}, \qquad S=p+x+y+z.
```

Writing

```math
h_u(r)=Ar^4+r^3+Br^2+Cr+D,
```

its exact coefficients are

```math
A=-\frac1S,\qquad B=-\frac{p(x+y+z)+xy+xz+yz}{S},
```

```math
C=\frac{5xyz}{S},\qquad D=-\frac{pxyz}{S}.
```

In particular,

```math
p=-\frac{5D}{C},
```

and

```math
625AD^3-125CD^2+25BC^2D-4C^4=0. \tag{1}
```

These are the published EZ6–EZ10 identities. Their converse is algebraic: positivity, integrality, primality and the original channel conditions remain additional requirements.

The source proves that its Turn 7 exterior states have four distinct literal roots and therefore enter the eight-sheet Fable domain. The following extends that statement to **every positive integral ES witness at a prime** **`p\equiv1\pmod{12}`**, including any middle-channel witness. This includes the remaining `p\equiv1\pmod{24}` class in the foundation’s elementary reduction.

### 1.1 Every hard-prime witness has four distinct literal roots

**Proposition.** Let `p\equiv1\pmod{12}` be prime. If `x,y,z` are positive integers satisfying ES, then `p,x,y,z` are pairwise distinct.

Suppose first that `x=p`. Then

```math
\frac3p=\frac1y+\frac1z, \qquad (3y-p)(3z-p)=p^2.
```

Both factors are positive. Each must belong to `\{1,p,p^2\}`, whose elements are all `1\pmod3`. But

```math
3y-p\equiv-p\equiv2\pmod3,
```

a contradiction.

Next suppose two denominators coincide, say `x=y=a`. Put

```math
d=2a-p>0.
```

The reciprocal equation becomes

```math
4dz=p(d+p),
```

so `d\mid p^2`. The three possibilities `d=1,p,p^2` give, respectively,

```math
z=\frac{p(p+1)}4,\qquad z=\frac p2,\qquad z=\frac{p+1}4.
```

None is integral when `p\equiv1\pmod4`. Thus repeated denominators are also impossible.

Consequently every such witness lies in

```math
A\,\operatorname{Disc}(h_u)\ne0,
```

and has all eight distinct signed Fable lifts. No exterior-channel hypothesis is needed for this conclusion.

### 1.2 A uniform finite bound at each prescribed hard prime

Sort the denominators as `x<y<z`. Then

```math
\frac p4<x\le\frac{3p}4.
```

Set

```math
R=4x-p,\qquad S_R=px=\frac{p(p+R)}4.
```

Because `p\equiv1\pmod4`,

```math
3\le R\le2p-3.
```

The remaining reciprocal equation has the exact factorization

```math
(Ry-S_R)(Rz-S_R)=S_R^2.
```

Both factors are positive integers. Hence

```math
z\le \frac{S_R(S_R+1)}R.
```

Let

```math
s_p=\frac{p(p+3)}4.
```

A direct subtraction gives

```math
\frac{S_R(S_R+1)}R-\frac{s_p(s_p+1)}3 = \frac{p^2(R-3)}{16} \left(1-\frac{p^2+4}{3R}\right).
```

The right side is nonpositive throughout the allowed range, because

```math
p^2+4-3(2p-3)=(p-3)^2+4>0.
```

Therefore

```math
\boxed{ z\le\frac{s_p(s_p+1)}3,\qquad S\le B_p:=p+s_p(s_p+1). } \tag{2}
```

This yields explicit separation in the normalized Fable target. For four distinct integers `t_1,\ldots,t_4`,

```math
\left|\prod_{j<k}(t_k-t_j)\right|\ge12.
```

Thus

```math
\boxed{ \operatorname{Disc}(h_u) =S^{-6}\prod_{j<k}(t_j-t_k)^2 \ge\frac{144}{B_p^6}. } \tag{3}
```

At any selected root `t_j`,

```math
h_u'(t_j)=-S^{-1}\prod_{\ell\ne j}(t_j-t_\ell).
```

The three differences are distinct nonzero integers, so their absolute product is at least `2`; each difference is smaller than `S`. Consequently

```math
\boxed{ \frac2S\le |h_u'(t_j)|\le S^2. } \tag{4}
```

The original signed coordinate, denoted here by `\xi_j`, satisfies

```math
\xi_j^2h_u'(t_j)=1,
```

and hence

```math
\boxed{ \frac1S\le|\xi_j|\le\sqrt{\frac S2}. } \tag{5}
```

The source’s full inverse is

```math
y_F=-t_j-\frac{i}{\xi_j},
```

```math
z_F=\frac A{\xi_j^3}+\frac{2t_j}{\xi_j} +\frac{3i}{\xi_j^2},
```

```math
w_F=\frac{7it_j^2}{\xi_j} +\frac{B-17t_j+At_j^2}{\xi_j^2} -\frac{13i}{\xi_j^3}-\frac{2A}{\xi_j^4}.
```

These are the literal GF7/EZ13 coordinates, not a new inverse model.

Using `|A|=S^{-1}`, `|B|\le S` and `|t_j|\le S`, they give

```math
|y_F|\le2S,\qquad |z_F|\le6S^2,\qquad |w_F|\le41S^3. \tag{6}
```

Thus, in any specified fixed receiving Gram `G>0`,

```math
\boxed{ \|q_{j,\pm}\|_G^2 \le \|G\|_2 \left(\frac S2+4S^2+36S^4+1681S^6\right). } \tag{7}
```

**Interpretation.** At a fixed hard prime, actual integral ES witnesses cannot escape through either the quartic discriminant or infinity. The bounds grow with `p`, so this is not a uniform compactness theorem over all primes and does not establish occupancy. It also does not bound away from zero the separate odd-receiving determinant studied in the preceding response.

## 2. The ES restriction changes the signed cover: degree `2+6`, monodromy `48`

The generic Fable cover has the source’s order-`192` signed permutation group. But the ES coefficient family has an intrinsic distinguished root, `p=-5D/C`. The generic group therefore cannot be carried unchanged into this restricted family. The source records the generic group but does not assign it to the ES restriction.

### 2.1 Exact fixed-`p` coefficient coordinates

For a fixed `p\ne0`, equation (1) is equivalent, on `ACD\ne0`, to

```math
\boxed{ D=-\frac{pC}{5},\qquad B=-Ap^2-p-\frac{4C}{5p}. } \tag{8}
```

Substitution gives the exact factorization

```math
h_u(r)=(r-p)g_p(r),
```

where

```math
\boxed{ g_p(r) =Ar^3+(1+Ap)r^2-\frac{4C}{5p}r+\frac C5. } \tag{9}
```

Define

```math
d_p=g_p(p)=2Ap^3+p^2-\frac{3C}{5}.
```

Then

```math
\boxed{ \operatorname{Disc}(h_u)=d_p^2\operatorname{Disc}(g_p). } \tag{10}
```

This follows either from the resultant product identity or directly by separating the three differences involving the distinguished root.

On

```math
\mathcal B_p =\{(A,C):ACd_p\operatorname{Disc}(g_p)\ne0\},
```

the root algebra splits through the explicit idempotent

```math
e_p(r)=\frac{g_p(r)}{d_p}.
```

It is one at `r=p` and zero at the three denominator roots. Accordingly, the signed inverse algebra splits into a rank-two prime part and a rank-six denominator part:

```math
\boxed{ \begin{aligned} \mathcal S_p &\simeq \mathcal R[\xi]/(\xi^2d_p-1)\\ &\quad\times \left(\mathcal R[r]/(g_p)\right)[\xi]\big/ \left(\xi^2(r-p)g_p'(r)-1\right), \end{aligned} } \tag{11}
```

where `\mathcal R` is the coordinate ring of `\mathcal B_p`.

The factor `d_p` is now a precise non-unit boundary: when it vanishes, the prime root meets a denominator root and this idempotent decomposition ceases to exist. That is not a failure of the fixed weighted conductor.

### 2.2 Full monodromy of the complex fixed-input ES family

**Proposition.** For each fixed `p\ne0`, the monodromy of the eight signed states over `\mathcal B_p` is

```math
\boxed{ G_p= \left\{(\sigma,\pi)\in\{\pm1\}^4\rtimes S_4: \pi(p)=p,\quad \prod_j\sigma_j=\operatorname{sgn}\pi \right\}, } \tag{12}
```

and

```math
|G_p|=48.
```

The upper bound follows from the distinguished root and the retained product invariant

```math
A^2\!\prod_{j<k}(t_k-t_j)\prod_j\xi_j\in\{1,-1\}.
```

It remains to realize the whole group.

The ordered denominator family has the rational presentation

```math
z=\frac{pxy}{4xy-p(x+y)}. \tag{13}
```

Removing zero denominators, coincident roots and `S=0` leaves a nonempty open subset of `\mathbb C^2`, hence a path-connected ordered-root cover. Its six orderings therefore realize the full denominator permutation group `S_3`.

The required sign changes can be exhibited without assuming a braid presentation. First take

```math
x=p(2+w),\qquad y=p(2-w),\qquad z=p\frac{4-w^2}{12-4w^2}. \tag{14}
```

For `0<|w|\le1/10`, only the collision `x=y` lies inside the puncture. A half-circle exchanges `x,y` and returns the coefficient target. Its square makes `h'(x)` and `h'(y)` wind once around zero, changing those two inverse square-root signs and leaving the other two signs fixed.

For a prime–denominator sign change, take

```math
x=p(1+w),\qquad y=\frac{2p}{5},\qquad z=\frac{2p(1+w)}{1+3w}, \qquad 0<|w|\le1/100. \tag{15}
```

A full circle around `w=0` leaves every root label fixed. The derivatives at `p` and `x` each have one simple zero inside, so their signs flip; the other signs do not.

The denominator pair flips generate the two-dimensional even-sign subgroup on three denominator labels. Adding a prime–denominator flip generates all eight even sign patterns on four labels. Together with the six denominator permutations, this gives `8\cdot6=48`, attaining the upper bound.

These paths preserve the **algebraic ES relation at fixed** **`p`**. They do not preserve positive integral denominators.

There is also a change in the deck group. The rank-two and rank-six components in (11) have independent sign reversals:

```math
\xi\longmapsto(1-2e_p)\xi, \qquad \xi\longmapsto-\xi.
```

Their generated deck group is

```math
\boxed{\operatorname{Deck}(\mathcal S_p/\mathcal B_p)\simeq C_2\times C_2.} \tag{16}
```

On the six denominator states, the centralizer of the full signed permutation action is just the identity and simultaneous sign reversal; on the prime pair it is `C_2`. This also proves that there are no additional deck transformations.

### 2.3 Consequence for the earlier orbit-metric reconstruction

The order-`192` averaging formula from the preceding continuation cannot simply be reused on this ES family. The restricted eight-dimensional representation decomposes as

```math
1\oplus1\oplus2\oplus1\oplus3.
```

The two trivial components are the prime-even state and the sum of the three denominator-even states. Their **mutual Gram term survives**.

For the original mean and odd columns `E=[e_p,E_d]`, `O=[o_p,O_d]`, and any specified receiving form `G`, the order-`48` averaged form, in the corresponding orthonormal decomposition of label coordinates, is

```math
\boxed{ H_{\mathrm{triv}} \oplus\lambda_2I_2 \oplus\lambda_p \oplus\lambda_3I_3, } \tag{17}
```

where

```math
H_{\mathrm{triv}} = \begin{bmatrix}e_p&E_d\mathbf1/\sqrt3\end{bmatrix}^{\!*} G \begin{bmatrix}e_p&E_d\mathbf1/\sqrt3\end{bmatrix},
```

```math
\lambda_2=\frac12\operatorname{tr}(P_2E_d^*GE_d), \quad P_2=I_3-\frac13\mathbf1\mathbf1^*,
```

```math
\lambda_p=o_p^*Go_p,\qquad \lambda_3=\frac13\operatorname{tr}(O_d^*GO_d).
```

Even-sign averaging eliminates the other mixed terms; permutation averaging gives the displayed scalar blocks. The `2\times2` block must remain. For an actual observation, `G` is replaced by its exact semidefinite pullback, and positivity of that block must be checked rather than assumed.

## 3. Completing the non-invertible boundary while retaining the pole

The original signed inverse correspondence uses

```math
\xi^2h_u'(r)=1.
```

Its missing multiple-root states are therefore caused by the inversion of `h_u'(r)`. A finite extension is obtained by retaining the reciprocal coordinate instead.

### 3.1 A finite flat rank-eight extension

Work over

```math
\mathcal R_0=\mathbb C[A,A^{-1},B,C,D], \qquad \mathcal E=\mathcal R_0[r]/(h_u).
```

Introduce

```math
\eta=\xi^{-1}
```

and define

```math
\boxed{ \widehat{\mathcal S} =\mathcal E[\eta]/(\eta^2-h_u'(r)). } \tag{18}
```

It is free of rank eight over `\mathcal R_0`, with basis

```math
1,r,r^2,r^3,\eta,\eta r,\eta r^2,\eta r^3.
```

Indeed `A^{-1}h_u` is monic of degree four, and the second relation is monic of degree two.

The original inverse is recovered exactly on `\eta\ne0`:

```math
\boxed{ \mathcal E[\xi]/(\xi^2h_u'-1) \simeq \widehat{\mathcal S}[\eta^{-1}], \qquad \eta=\xi h_u',\quad \xi=\eta^{-1}. } \tag{19}
```

Both compositions follow immediately from the two defining equations.

Thus `\operatorname{Spec}\widehat{\mathcal S}\to\operatorname{Spec}\mathcal R_0` is a finite flat degree-eight morphism and is proper. The finite/proper implication is the standard algebraic-geometric result; the explicit free algebra and open immersion above identify the actual extension being used. It is an extension over `A\ne0`, not a claim to repair the separate infinity-chart boundary `A=0`. ([The Stacks Project](https://stacks.math.columbia.edu/tag/03ZN?utm_source=chatgpt.com "Section 67.45 (03ZN): Integral and finite morphisms—The Stacks project"))

The added boundary is ramified. The Jacobian of the two relations with respect to `(r,\eta)` has determinant

```math
2\eta h_u'(r)=2\eta^3. \tag{20}
```

Away from `\eta=0` it is invertible, in agreement with the source’s étale inverse domain and the standard derivative-unit criterion. ([The Stacks Project](https://stacks.math.columbia.edu/tag/0G1A "Section 10.144 (0G1A): Local structure of étale ring maps—The Stacks project"))

### 3.2 The original physical pole has not been cancelled

In these coordinates the original Fable point is

```math
\boxed{ q= \begin{pmatrix} \eta^{-1}\\ -r-i\eta\\ A\eta^3+2r\eta+3i\eta^2\\ 7ir^2\eta+(B-17r+Ar^2)\eta^2-13i\eta^3-2A\eta^4 \end{pmatrix}. } \tag{21}
```

All coordinates except the first extend regularly across `\eta=0`.

For any fixed injective receiving map `F`, carrying its actual positive target metric back to `G=F^*QF`,

```math
\eta q\longrightarrow e_1
```

along a bounded-root approach to that boundary. Therefore

```math
\boxed{ |\eta|\,\|Fq\|_Q\longrightarrow\sqrt{G_{11}}>0. } \tag{22}
```

The finite algebraic extension adds the missing state. It does **not** identify an unbounded original norm with a bounded one. The exact pole is retained in the meromorphic map (21).

### 3.3 Multiple roots give explicit nilpotent fibres

Suppose a target has an `m`-fold root `r_0`:

```math
h_u(r)=(r-r_0)^m g(r),\qquad g(r_0)=g_0\ne0.
```

With `\varepsilon=r-r_0`, its local root algebra is

```math
\mathbb C[\varepsilon]/(\varepsilon^m),
```

and

```math
h_u'(r)=mg_0\varepsilon^{m-1}
```

in that algebra. The completed local signed fibre is exactly

```math
\boxed{ \widehat{\mathcal S}_{r_0} = \mathbb C[\varepsilon,\eta]\big/ \left(\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1}\right), \qquad \dim_{\mathbb C}\widehat{\mathcal S}_{r_0}=2m. } \tag{23}
```

For a double root,

```math
\varepsilon=\frac{\eta^2}{2g_0}, \qquad \boxed{\widehat{\mathcal S}_{r_0}\simeq\mathbb C[\eta]/(\eta^4).} \tag{24}
```

Four nearby signed states become a single length-four nonreduced fibre, not four finite distinct points.

Multiplication by `\varepsilon` has two Jordan blocks of size `m`. This follows directly from the free basis `1,\eta` over `\mathbb C[\varepsilon]/(\varepsilon^m)`.

### 3.4 A literal ES boundary and an exact local RH map

There is an actual positive integral ES boundary example:

```math
\frac45=\frac15+\frac12+\frac1{10}.
```

Its quartic is

```math
h_{\mathrm{ES}}(r) =-\frac1{22}(r-5)^2(r-2)(r-10).
```

At `r=5`, `g_0=15/22`, so

```math
\eta_{\mathrm{ES}}^2=\frac{15}{11}\varepsilon_{\mathrm{ES}}.
```

Its completed fibre consists of a length-four local algebra at `5`, plus four reduced signed points above `2` and `10`.

More generally, the rational ES family

```math
(p;x,y,z)=\left(p;p,\frac{2p}{5},2p\right)
```

has

```math
\eta_{\mathrm{ES}}^2=\frac{3p}{11}\varepsilon_{\mathrm{ES}} \tag{25}
```

at its double root `p`.

The RH programme’s auxiliary quartet degeneration is

```math
h_{\mathrm{RH},0}(r) =-\frac12\left((r-\tfrac12)^2+\gamma^2\right)^2.
```

At either `r_\pm=\tfrac12\pm i\gamma`, `g_0=2\gamma^2`, hence

```math
\eta_{\mathrm{RH}}^2=4\gamma^2\varepsilon_{\mathrm{RH}}.
```

This is the source’s auxiliary paired-root degeneration, not an assertion that a varying family of actual zeta zeros exists.

Choose either square root

```math
c^2=\frac{3p}{44\gamma^2}.
```

Then

```math
\boxed{ \eta_{\mathrm{ES}}\longmapsto c\,\eta_{\mathrm{RH}}, \qquad \varepsilon_{\mathrm{ES}}\longmapsto\varepsilon_{\mathrm{RH}} } \tag{26}
```

is an explicit isomorphism of the two length-four local algebras. It intertwines **centred** multiplication:

```math
M_{r-p}\longmapsto M_{r-r_\pm}.
```

For uncentred multiplication, the exact correction is

```math
r_{\mathrm{ES}}\longmapsto r_{\mathrm{RH}}+(p-r_\pm). \tag{27}
```

This is a genuine local algebra/action morphism between the two constructions. It does not identify the full fibres, original global actions or native metrics. In the bases `1,\eta,\eta^2,\eta^3`, its matrix is

```math
\operatorname{diag}(1,c,c^2,c^3),
```

so any specified metric is transported by that full congruence, including determinant factor `|c|^{12}`.

There is also a useful obstruction. For the nonzero nilpotent `N` in (24), `N^2=0`, and for every positive Hermitian form `G`, the defect

```math
N^*G+GN
```

has both signs. Choose `Nv=w\ne0`, `Nw=0`. Its compression to `(w,v)` has determinant

```math
-\|w\|_G^4<0.
```

Thus the nilpotent completion does not itself produce an isometric action or arithmetic purity.

## 4. A receiving frame without the extra odd determinant divisor

The previous continuation identified a regular quartic where the original odd receiving matrix `O` has rank three. The new ES audit independently records another such regular target and explicitly warns that squarefreeness does not imply `\det O\ne0`.

There is a global replacement on the squarefree `A\ne0` domain that makes the information loss explicit.

For the four roots `r_j` and their chosen signs `\xi_j`, define the odd moment matrix

```math
\boxed{ U= \begin{pmatrix} 1&1&1&1\\ r_1&r_2&r_3&r_4\\ r_1^2&r_2^2&r_3^2&r_4^2\\ r_1^3&r_2^3&r_3^3&r_4^3 \end{pmatrix} \operatorname{diag}(\xi_1,\xi_2,\xi_3,\xi_4). } \tag{28}
```

The retained product invariant gives

```math
\boxed{\det U=\frac{\chi}{A^2},\qquad \chi\in\{1,-1\}.} \tag{29}
```

Thus this frame has no additional receiving-divisor zero.

Let `V_h` be the coefficient matrix obtained by reducing

```math
1,\quad -ih_u',\quad A(h_u')^2+2rh_u', \quad i\bigl(7r^2h_u'-13(h_u')^2\bigr)
```

modulo `h_u`, in the basis `1,r,r^2,r^3`. Then the original odd evaluation is exactly

```math
\boxed{O=V_hU.} \tag{30}
```

A singularity of `O` away from the discriminant is therefore located in `V_h`, not in the signed moment carrier `U`.

The full inverse is explicit. For `m=U\beta`,

```math
\boxed{ \begin{aligned} \beta_j=\xi_j\bigl[& (C+Br_j+r_j^2+Ar_j^3)m_0\\ &+(B+r_j+Ar_j^2)m_1 +(1+Ar_j)m_2+Am_3\bigr]. \end{aligned} } \tag{31}
```

This is Lagrange interpolation, using

```math
\frac1{\xi_jh_u'(r_j)}=\xi_j.
```

At `\det V_h=0`, (31) does not reconstruct moments from the already-collapsed data `O\beta`. Those moments must actually be retained or measured. The relation (30) identifies exactly what the original evaluation forgets.

### Passage into the updated, actual RH observation

The latest RH source goes beyond the older cubic Gamma receiver. It constructs

```math
F_+=J_+K^{-1},\qquad F_B=\Lambda_kJ_+K^{-1},\qquad F_-=J_-D_\partial K^{-1},
```

with

```math
\boxed{\Lambda_kF_+=F_B,\qquad \bar C F_B=F_-.} \tag{32}
```

Here `J_\pm` are the original corner cardinal-class maps, `K` is the literal four-point Fable marking, and `D_\partial` contains the four original conductor corner coefficients. These are MO1–MO10, not freely chosen lifts.

On the source’s nonzero-corner domain, `F_B` is injective. Therefore every ES target `u` and signed inverse `q` with `P(q)=u` satisfies

```math
\boxed{ (F_BPF_B^{-1})(F_Bq)=F_Bu, } \tag{33}
```

on the stated four-dimensional image. Equation (32) gives its exact source and conductor partners.

The metric here is the original arithmetic observation metric

```math
\widehat G_N=K^{-*}O_+^*Q_NO_+K^{-1}.
```

It retains the two source residuals

```math
O_+^*Q_NO_+ = D_\partial^*J_-^*T_NJ_-D_\partial +\Delta_N^*Q_N\Delta_N,
```

```math
J_+^*G_NJ_+ = O_+^*Q_NO_+ +Z_N^*G_NZ_N. \tag{34}
```

Neither term is set to zero by transporting an ES point.

The arithmetic generator remains

```math
\widehat B_k=K\operatorname{diag}(k\rho_l)K^{-1}.
```

It is not replaced by multiplication by `p,x,y,z`. This gives a combined ES–Fable–original-observation construction while retaining the distinction between its coefficient geometry and its arithmetic dynamics.

## 5. An explicit auxiliary-degree bound for the native resolvents

This is the main analytic advance in the continuation.

The newest native-moment proof already gives exact Gauss/Radau brackets, rank-one error directions and convergence at fixed poles. It explicitly does **not** give an a priori rate in the auxiliary polynomial degree. Its displayed elementary rate is instead a rate in the pole, and can worsen as higher moments grow.

The following closes that specific degree-selection gap using the original Gamma comparison.

### 5.1 Original measures and the exact error scalar

Retain

```math
m_k=w_{h_\zeta}^{*k},\qquad m_k(y)\le\overline a_k\,\sigma(y),
```

where

```math
\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}, \qquad M_\Gamma:=\int_{\mathbb R}\sigma(y)\,dy=\sqrt{2\pi}.
```

The source’s actual upper constant is

```math
\overline a_k =\frac{C_{h_\zeta}^{\mathrm{tilt}}}{c_\Gamma} k^{p_h+1}M_{h_\zeta}(\pi/2)^{k-1}, \qquad p_h=8m_0-\frac92,\quad c_\Gamma=\sqrt2e^{-7/6}.
```

No probability normalization is made.

Use the source’s parity and tilted measures

```math
d\nu_0(x)=m_k(\sqrt x)x^{-1/2}dx,\qquad d\nu_1=x\,d\nu_0,
```

```math
s(x)=\frac{\tanh(\pi\sqrt x/2)}{\sqrt x}, \qquad d\rho_b=s\,d\nu_b,\quad b=0,1.
```

For the native resolvent matrix, RR8 states

```math
F_n(a)-F^-_{n,r}(a) =\lambda_r^{(b)}(a)\,z_n(a)z_n(a)^*, \qquad z_n(a)=(1,-a,\ldots,(-a)^n)^T.
```

Its scalar has the exact variational expression

```math
\boxed{ \lambda_r^{(b)}(a) = \min_{\substack{\deg R\le r\\R(-a)=1}} \int_0^\infty\frac{|R(x)|^2}{x+a}\,d\rho_b(x). } \tag{35}
```

Indeed variations preserving `R(-a)=1` are multiples of `x+a`; orthogonality makes the minimizer the native monic polynomial `p_r(x)/p_r(-a)`. This is the same scalar as RR6–RR11.

### 5.2 The bound at every original pole `a_j=4j^2`

**Proposition.** For `j\ge1`, both original parity measures satisfy

```math
\boxed{ \lambda_r^{(b)}(4j^2) \le \frac{\mathcal K_{k,j}}{(r+1)^{2j}}, \qquad b=0,1, } \tag{36}
```

where

```math
\boxed{ \mathcal K_{k,j} = \frac{\pi\sqrt{2\pi}}{4j}\, \overline a_k\, \bigl((5/4)_{j-1}\bigr)^2. } \tag{37}
```

**Proof.** Let `p_n^\Gamma` be the original monic Gamma polynomials:

```math
\|p_n^\Gamma\|_\sigma^2=M_\Gamma n!(1/2)_n,
```

```math
\sum_{n\ge0}\frac{p_n^\Gamma(y)}{n!}t^n =(1+t^2)^{-1/4}e^{y\arctan t}.
```

This is the precise Meixner–Pollaczek specialization used in WCF and RR; the generating identity is DLMF 18.23.7. ([DLMF](https://dlmf.nist.gov/18.23.E7 "DLMF: §18.23 Hahn Class: Generating Functions ‣ Askey Scheme ‣ Chapter 18 Orthogonal Polynomials"))

Set `R_n(Y)=i^{-n}p_n^\Gamma(iY)`. At `Y=2j`,

```math
\boxed{ \sum_{n\ge0}\frac{R_n(2j)}{n!}t^n =(1+t)^{2j}(1-t^2)^{-(j+1/4)}. } \tag{38}
```

Every coefficient on the right is nonnegative. Hence

```math
\frac{R_{2m}(2j)}{(2m)!}\ge\frac{(j+1/4)_m}{m!},
```

```math
\frac{R_{2m+1}(2j)}{(2m+1)!} \ge2j\,\frac{(j+1/4)_m}{m!}.
```

The elementary product inequalities

```math
\frac{n!}{(1/2)_n}\ge\sqrt{n+1}, \qquad \frac{(5/4)_m}{m!}\ge(m+1)^{1/4}
```

follow by induction, the latter using concavity of `x^{1/4}`. Also

```math
\frac{(j+1/4)_m}{m!} \ge \frac{(m+1)^{j-3/4}}{(5/4)_{j-1}}.
```

Summing the resulting squared evaluation terms gives the Gamma even and odd kernels

```math
\boxed{ K_r^{\mathrm{ev}}(2ij) \ge \frac{(r+1)^{2j}} {2jM_\Gamma((5/4)_{j-1})^2}, } \tag{39}
```

```math
\boxed{ K_r^{\mathrm{odd}}(2ij) \ge \frac{2j(r+1)^{2j}} {M_\Gamma((5/4)_{j-1})^2}. } \tag{40}
```

The sum estimate used here is simply

```math
\sum_{m=0}^r(m+1)^{2j-1} \ge\frac{(r+1)^{2j}}{2j}.
```

For `b=0`, use `s\le\pi/2`, `x+a\ge a`, and the exact even lift `R(x)\mapsto R(y^2)` in (35):

```math
\lambda_r^{(0)}(a) \le \frac{(\pi/2)\overline a_k}{aK_r^{\mathrm{ev}}(i\sqrt a)}.
```

For `b=1`, the lift is `yR(y^2)`, whose value at `i\sqrt a` is `i\sqrt a`. Thus

```math
\lambda_r^{(1)}(a) \le \frac{(\pi/2)\overline a_k}{K_r^{\mathrm{odd}}(i\sqrt a)}.
```

Substituting `a=4j^2` and (39)–(40) gives precisely (36)–(37).

This proof uses the native measures throughout the error minimum. The Gamma measure enters only through the stated dominating inequality and explicit trial-space evaluation.

### 5.3 A closed auxiliary-degree choice for the existing endpoint certificate

Let `\gamma_r(a_j)` be the finite-moment upper scalar from RR9. Replace it by

```math
\widehat\gamma_{r,j} = \min\left\{\gamma_r(a_j), \frac{\mathcal K_{k,j}}{(r+1)^{2j}}\right\}. \tag{41}
```

This is a scalar minimum along the **same known rank-one direction**, not an unsupported minimum of two matrices.

For

```math
B_n(a)=H_{n+1}-aF_n(a),
```

the refined lower bound is

```math
B^{\mathrm{new},-}_{n,r} = H_{n+1}-aF^-_{n,r} -a\widehat\gamma_{r,j}zz^*.
```

It is positive semidefinite because it is at least the already proved Radau lower matrix.

At a fixed original cutoff, write

```math
H_{\mathrm{base}} =\frac2\pi\operatorname{diag}(H_{\rho_0},H_{\rho_1})>0.
```

Let `z_{b,j}` denote the evaluation vector padded into the appropriate parity block, and define

```math
\chi_{b,j}=z_{b,j}^*H_{\mathrm{base}}^{-1}z_{b,j}.
```

Allocate positive tolerances `\varepsilon_{b,j}` with

```math
\sum_{b,j}\varepsilon_{b,j}\le\delta_{\mathrm{inner}}.
```

Then the explicit integer choice

```math
\boxed{ r_{b,j} = \max\left\{ n_b+1,\ \left\lceil \left( \frac{4a_j\mathcal K_{k,j}\chi_{b,j}} {\pi\varepsilon_{b,j}} \right)^{1/(2j)} \right\rceil-1 \right\} } \tag{42}
```

guarantees

```math
\frac4\pi\sum_{b,j} a_j\widehat\gamma_{r_{b,j},j}z_{b,j}z_{b,j}^* \preceq \delta_{\mathrm{inner}}H_{\mathrm{base}} \preceq \delta_{\mathrm{inner}}G^-. \tag{43}
```

The first inequality uses

```math
zz^*\preceq(z^*H_{\mathrm{base}}^{-1}z)H_{\mathrm{base}}.
```

Thus the source’s qualitative instruction “refine until the inner test holds” has an explicit sufficient degree. Its original outer truncation and signed four-endpoint bounds remain unchanged.

Even `\chi_{b,j}` has an a priori comparison when needed. From

```math
s(y^2)\ge \frac{\tanh(\pi/2)}{\sqrt2}(1+y^2)^{-1/2}
```

and the original lower envelope, define

```math
c_{k,N} = \frac{\tanh(\pi/2)}{\sqrt2}\, \underline a_k [1+4(N+1)^2]^{-(M+1/2)}.
```

Jensen’s inequality and the Gamma multiplication bound give

```math
\boxed{ \chi_{b,j} \le \frac{\pi}{2c_{k,N}a_j^b} K_{n_b}^{(b)}(2ij), } \tag{44}
```

where the kernel on the right is a finite, explicitly evaluable Gamma-polynomial sum.

This does **not** evaluate the original moments or imply economical computational complexity. It supplies a rigorous degree bound, with the original constants, for a step the current source previously justified only by convergence. The finite-matrix Gauss/Radau literature supplies context, but its finite-dimensional hypotheses are not being substituted for this native-measure proof (Zimmerling et al., 2025). ([arXiv](https://arxiv.org/abs/2407.21505?utm_source=chatgpt.com "Monotonicity, bounds and extrapolation of Block-Gauss and Gauss-Radau quadrature for computing $B^T φ(A) B$"))

## 6. Carrying the scalar errors through the actual minima and currents

The rank-one structure survives the full minimization. This is stronger than replacing it by independent entrywise error discs.

### 6.1 Exact source-to-quotient update

Let

```math
H_\theta=H_0+\theta vv^*>0
```

and let `\mathsf A` be the original onto map—remainder, observation, or the composite conductor observation. Put

```math
P=H_0^{-1},\qquad G_0=(\mathsf A P\mathsf A^*)^{-1},
```

```math
z=G_0\mathsf A Pv,\qquad \chi=v^*Pv,
```

```math
\kappa =v^*\left(P-P\mathsf A^*G_0\mathsf A P\right)v.
```

The middle matrix is positive semidefinite, so `0\le\kappa\le\chi`.

Two applications of the rank-one inverse formula give

```math
\boxed{ G_\theta =(\mathsf A H_\theta^{-1}\mathsf A^*)^{-1} = G_0+\frac{\theta}{1+\kappa\theta}zz^*, } \tag{45}
```

and

```math
\boxed{ \frac{\det G_\theta}{\det G_0} =\frac{1+\chi\theta}{1+\kappa\theta}. } \tag{46}
```

The exact minimum representative also follows. If

```math
x_0=P\mathsf A^*G_0u,\qquad k_v=Pv-P\mathsf A^*G_0\mathsf A Pv\in\ker\mathsf A,
```

then

```math
\boxed{ x_\theta=x_0-\frac{\theta}{1+\kappa\theta}k_v\,z^*u. } \tag{47}
```

The correction lies in the full original kernel. No coordinate or source term has been omitted.

### 6.2 The second minimum retains the same scalar

Now work in the original quotient `E`, let `I` be a full-column frame for `\ker\Lambda`, and retain the actual three columns

```math
W=[b_N,b_{N+1},v_\lambda].
```

Define

```math
M=I^*G_0I,\qquad F_0=W^*G_0W,
```

```math
R_0=W^*G_0I\,M^{-1}I^*G_0W,\qquad C_0=F_0-R_0.
```

Here `R_0` is the kernel contribution and `C_0` the observed contribution, as in the programme’s HG6–HG7 decomposition.

Set

```math
u=W^*z,\qquad \beta=z^*I M^{-1}I^*z,
```

```math
w=u-W^*G_0I M^{-1}I^*z.
```

Then, exactly,

```math
\boxed{ \begin{aligned} F_\theta&=F_0+t\,uu^*,\\ C_\theta&=C_0+s\,ww^*,\\ R_\theta&=R_0+t\,uu^*-s\,ww^*, \end{aligned} \qquad t=\frac{\theta}{1+\kappa\theta},\quad s=\frac{\theta}{1+(\kappa+\beta)\theta}. } \tag{48}
```

The proof is the Schur-complement expansion of the full Gram on `[I,W]`. Also

```math
0\le\beta\le\chi-\kappa.
```

Therefore the positivity condition on `H_\theta` makes both denominators positive.

The scalar `\kappa+\beta` is exactly the `\kappa` obtained by applying (45) directly to the composite map `\Lambda\mathsf A`. This is the algebraic expression of associativity of the two complete minima—not a second independent uncertainty.

### 6.3 Phase-sensitive current intervals become polynomial tests

For the observed current, write

```math
(C_\theta)_{13}=a_0+s a_1,\qquad (C_\theta)_{23}=b_0+s b_1,
```

where

```math
a_1=w_1\overline{w_3},\qquad b_1=w_2\overline{w_3}.
```

Its undivided numerator is exactly

```math
\boxed{ 2\operatorname{Re} \left(\overline{(C_\theta)_{13}}(C_\theta)_{23}\right) =A_0+A_1s+A_2s^2, } \tag{49}
```

with

```math
A_0=2\operatorname{Re}(\overline{a_0}b_0),
```

```math
A_1=2\operatorname{Re}(\overline{a_0}b_1+\overline{a_1}b_0), \qquad A_2=2\operatorname{Re}(\overline{a_1}b_1).
```

Since `s(\theta)` is increasing on the positive-definite interval, its exact range is found from the two endpoints and, when it belongs to the interval,

```math
s_*=-\frac{A_1}{2A_2}.
```

For the kernel and mixed currents, clearing the positive denominator

```math
[(1+\kappa\theta)(1+(\kappa+\beta)\theta)]^2
```

gives real polynomials of degree at most four. Both source mixed products

```math
\overline{K_1}B_2+\overline{B_1}K_2
```

remain present. The current identities themselves are the original HG7 formulas; the polynomial dependence here is the new propagation calculation.

Endpoint testing alone is insufficient, even in a positive rank-one family. For example,

```math
C_0= \begin{pmatrix} 2&0&-1/4\\ 0&2&-3/4\\ -1/4&-3/4&2 \end{pmatrix}>0, \qquad w=(1,1,1)^T,
```

gives `C(s)=C_0+sww^*>0` for `0\le s\le1`, but

```math
2\operatorname{Re}(\overline{C_{13}(s)}C_{23}(s)) =2(s-\tfrac14)(s-\tfrac34).
```

It is `3/8` at both endpoints and `-1/8` at `s=1/2`. This is an exact test of the inference rule, not a purported arithmetic example.

### 6.4 When the native boundary polynomials move

The fixed-column degree bounds above must not silently freeze a polynomial that is being recomputed from the same uncertain moments.

For completeness, let `q_0` be the original monic degree-`n` minimizer, let `I` insert the lower-degree coefficients, and put

```math
M=I^*H_0I,\qquad a=I^*v,\qquad \beta_0=a^*M^{-1}a.
```

Then the moving monic polynomial and its squared norm are

```math
\boxed{ q_\theta =q_0-\frac{\theta}{1+\beta_0\theta} IM^{-1}a\,(v^*q_0), } \tag{50}
```

```math
\boxed{ h_\theta =h_0+\frac{\theta}{1+\beta_0\theta}|v^*q_0|^2. } \tag{51}
```

Orthogonality against every lower-degree polynomial verifies (50); completing the square gives (51). Any orthonormal column must retain the factor `h_\theta^{-1/2}`.

Thus the same scalar can be propagated through the native polynomials, source quotient, observation quotient, and current. What is not justified is assigning unrelated errors to these quantities or retaining the fixed-column quartic degree bound after changing the columns without substitution.

## 7. What has advanced, and what remains

The ES foundation’s literal-root map now has a stronger receiving domain: **all positive integral witnesses at the hard primes**, with explicit discriminant, derivative and lift bounds. Its fixed-input complex family has a calculated order-`48` monodromy group and a rank-`2+6` decomposition, rather than an unqualified reuse of the generic order-`192` result.

The non-unit inverse derivative has an explicit finite extension. Its double-root fibre is `\mathbb C[\eta]/(\eta^4)`, and the local ES–RH map (26) preserves centred multiplication while displaying the uncentred correction. The original norm pole remains visible in (21)–(22).

On the RH analytic side, equation (36) supplies an a priori auxiliary-degree rate at every original pole `4j^2`. Equation (42) converts it into a finite sufficient degree for the existing native endpoint certificate. Equations (45)–(51) then carry each scalar uncertainty through the original minima and phase-sensitive currents.

The unresolved conclusions are still the substantive ones: positivity of the complete original ES witness count at every prescribed hard prime; evaluation of the original RH projected-current asymptotics and proper-source target Schur quantities; and the independent same-class inequality or comparison needed for programme closure. The current sources explicitly retain those requirements.

The derivations above are written proofs and explicit identities. The Python/SymPy execution attempt failed with a runtime transport error, so **no successful computer-algebra or Lean verification is being reported**, and neither repository has been modified.

### References

The Clankers. (2026, September 20). *The normalized Erdős–Straus quartic and its exact passage through the signed Fable cover to a fixed weighted conductor* [Research manuscript, commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`]. *Erdős–Straus Foundation*.

National Institute of Standards and Technology. (2026). *NIST Digital Library of Mathematical Functions* (Version 1.2.6), §18.23, equation 18.23.7. ([DLMF](https://dlmf.nist.gov/18.23.E7 "DLMF: §18.23 Hahn Class: Generating Functions ‣ Askey Scheme ‣ Chapter 18 Orthogonal Polynomials"))

Split-Zero programme. (2026a, September 20). *Finite native moments and the original arithmetic observation* [Research manuscript, commit `f8b73284d2e669e981bf2c7609e99f4d2b3a50be`]. *Zeta-function research reader*.

Split-Zero programme. (2026b, September 20). *The actual marked observation and its complete inverse branches* [Cumulative source edition, same commit]. *Zeta-function research reader*.

The Stacks Project Authors. (n.d.). *Local structure of étale ring maps* (Tag 0G1A); *Integral and finite morphisms* (Tag 03ZN). ([The Stacks Project](https://stacks.math.columbia.edu/tag/0G1A "Section 10.144 (0G1A): Local structure of étale ring maps—The Stacks project"))

Zimmerling, J., Druskin, V., & Simoncini, V. (2025). *Monotonicity, bounds and extrapolation of Block-Gauss and Gauss-Radau quadrature for computing* *`B^T\phi(A)B`* (Version 3) [Preprint]. arXiv:2407.21505. ([arXiv](https://arxiv.org/abs/2407.21505?utm_source=chatgpt.com "Monotonicity, bounds and extrapolation of Block-Gauss and Gauss-Radau quadrature for computing $B^T φ(A) B$"))