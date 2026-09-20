**The supplied family construction is integrated into a new continuation with four further derivations.** The main quantitative result is that, under the repository’s native spectral-transfer theorem, the canonical metric and the constructed jet metric require more than any fixed polynomial conditioning cost to compare. The other results calculate the complete division of the joint-source determinant cost, the covariance between ES sum centres and unequal primary lengths, and every collision exponent when the jet scale varies simultaneously.

[Download the integration package](sandbox:/mnt/data/ES_RH_Family_Integration_20260920_C.zip)

[Read the 18-page proofs](sandbox:/mnt/data/ES_RH_Family_Integration_20260920_C/MANUSCRIPT.pdf) · [Editable manuscript](sandbox:/mnt/data/ES_RH_Family_Integration_20260920_C/RESEARCH_CONTINUATION.md) · [Codex handoff](sandbox:/mnt/data/ES_RH_Family_Integration_20260920_C/CODEX_HANDOFF.md) · [Verification record](sandbox:/mnt/data/ES_RH_Family_Integration_20260920_C/results/VERIFICATION_SUMMARY.json)

The four new suites completed **1,275 exact checks and twenty negative-control executions per interpreter mode**, with byte-identical normal and optimized Python outputs. These check finite algebra, exact minors, complete quadratic minima, and explicitly labelled diagnostic examples. They are not evaluations of unknown native zeta moments or a Lean verification.

The uploaded note is preserved unchanged. I used its complete supplied text; I did not retrieve or count verification from the separate archive linked inside it. Its central distinction is retained throughout: its conditioning estimate compares two **constructed** metrics, not either one with the canonical scalar-source metric.

The RH snapshot checked is `b1f3e2e1879c40f411eb263dde171589cb5f9390`; the ES snapshot is `34e45e06694c66650ddb4550bbf48c60ce75d8f9`. The newer finite-theta certificate is recorded as a repository update, not used as an additional premise. Neither repository has been changed.

## 1. The constructed metric has a quantified cost of return to the canonical metric

The attachment gives actual finite tensor-source sections, not merely abstract positive forms. For a common quartet of multiplicity \(m\), retain

$$
D=k(m-1),\qquad q=(D+1)(k+1)^2,\qquad
M_k=\frac{M_S-kI/2}{i}.
$$

Let \(G_{k,N}\) be the original canonical metric at scalar-polynomial cutoff \(N\), and let

$$
\widetilde G_{k,\eta}
=\tau_\eta^kG_{k,\eta}
$$

be the **actual physical pullback metric** of the supplied constructed section. The factor \(\tau_\eta^k\) is retained. It cancels from an endomorphism’s adjoint by an exact scalar identity, but not from the section’s physical norm. The section realization and this scalar are part of the attachment’s equations (26)–(31).

For the stipulated off-line quartet, put

$$
R_0=\sqrt{\delta^2+\gamma^2},
\qquad \eta=\frac{\delta}{D+1}
$$

when \(D>0\). In the constructed orthonormal jet coordinates,

$$
M_k=Z_k+N_k,
\qquad
\|N_k\|\le\frac{\delta}{2},
$$

so

$$
\boxed{
\|M_k\|_{\widetilde G}\le kR_0+\frac{\delta}{2},
\qquad
\|M_k^{-1}\|_{\widetilde G}
\le\frac1{R_0-\delta/2}.
}
\tag{1}
$$

For \(D=0\), the nilpotent term is zero. The inverse bound follows because every diagonal block of \(Z_k\) has modulus at least \(R_0\), and its remaining part is nilpotent.

These are not estimates in \(G_{k,N}\).

### The exact exterior comparison

For positive metrics \(G_c,G_a\) on the same \(q\)-dimensional space, let

$$
\lambda_1\ge\cdots\ge\lambda_q
$$

be the logarithms of the eigenvalues of
\(G_c^{-1/2}G_aG_c^{-1/2}\). Define

$$
\mathfrak d(G_c,G_a)
=\min_{b\in\mathbb R}\sum_i|\lambda_i-b|,
\qquad
\operatorname{cond}(G_c,G_a)=e^{\lambda_1-\lambda_q}.
$$

The scalar minimization removes only the scalar metric factor that leaves endomorphism norms unchanged.

For the actual identity map

$$
L:(C,G_c)\longrightarrow(C,G_a),
$$

and \(h=\lfloor q/2\rfloor\),

$$
\boxed{
\mathfrak d(G_c,G_a)
=
2\log\!\left(
\|\wedge^hL\|\,\|\wedge^hL^{-1}\|
\right).
}
\tag{2}
$$

This is the direct inverse-exterior relationship: a median minimizes the absolute deviations, and singular-value decomposition computes the exterior norms. The standard SVD conventions are those described by Higham (2020); the comparison below is proved explicitly in the package. ([Nick Higham][1])

Suppose \(M\) has at least \(r\) singular values in \(G_a\) not smaller than \(bq\), while \(\|M\|_{G_c}\le C\). With \(p=\min(r,q-r)>0\),

$$
\boxed{
\mathfrak d(G_c,G_a)\ge2r\log(bq/C),
\qquad
\log\operatorname{cond}(G_c,G_a)
\ge\frac{2r}{p}\log(bq/C).
}
\tag{3}
$$

Indeed,

$$
(bq)^r
\le\|\wedge^rM\|_{G_a}
\le
\|\wedge^rL\|\,C^r\,\|\wedge^rL^{-1}\|.
$$

The logarithms of the exterior factors are sums of the largest and smallest metric eigenvalue logarithms. Their overlapping terms cancel when \(r>q/2\), giving the factor \(p\).

### The canonical consequence

The repository’s NG20–NG21 theorem states that the canonical attained selfadjoint compression, scaled by \(q\), has a limiting positive spectral probability with no atom at zero, and differs from \(M_k\) by rank at most one. Thus, for every fixed \(\varepsilon>0\), eventually at least \((1-\varepsilon)q\) canonical singular values of \(M_k\) exceed \(bq\) for a suitable fixed \(b>0\). This is the inherited spectral input, not a theorem inferred from our finite tests.

Applying (3) and then letting \(\varepsilon\downarrow0\) gives

$$
\boxed{
\liminf_{k\to\infty}
\frac{\mathfrak d(\widetilde G_{k,\eta},G_{k,N})}
{q\log(q/k)}
\ge2,
}
\tag{4}
$$

and

$$
\boxed{
\frac{
\log\operatorname{cond}(\widetilde G_{k,\eta},G_{k,N})
}{
\log(q/k)
}
\longrightarrow+\infty.
}
\tag{5}
$$

These hold on the source’s stated canonical cutoff sequences and fixed-packet domain. They have no effective threshold in \(k\), because the consumed spectral law supplies none.

The attachment’s controlled constructed family is therefore useful, but **its canonical return cannot be treated as a polynomially conditioned change of metric**. This does not contradict the attachment’s own bound, whose comparison metrics are different.

### The two heat scales separate exactly

At the \(q\)-scale, canonical positive heat tends to the repository’s \(H_s(t)\), whereas constructed positive heat tends to one. At the \(k\)-scale, for every fixed \(t>0\),

$$
\boxed{
\frac1q\operatorname{Tr}
e^{-tM_k^{\dagger_{G_{k,N}}}M_k/k^2}
\longrightarrow0,
}
\tag{6}
$$

while the constructed metric gives

$$
\boxed{
\frac1q\operatorname{Tr}
e^{-tM_k^{\dagger_{\widetilde G}}M_k/k^2}
\longrightarrow
\frac{\pi}{4t\delta\gamma}
\operatorname{erf}(\delta\sqrt t)
\operatorname{erf}(\gamma\sqrt t)>0.
}
\tag{7}
$$

The constructed limit is the attachment’s evaluated heat integral. The new comparison establishes what happens to the same operator in the canonical metric.

There is also an explicit constructed error:

$$
\boxed{
\left|
\frac1q\operatorname{Tr}
e^{-tM_k^{\dagger_{\widetilde G}}M_k/k^2}
-\mathcal K_\infty(t)
\right|
\le
\frac{4tR_0^2}{k+1}
+t\left(\frac{R_0\delta}{k}+\frac{\delta^2}{4k^2}\right).
}
\tag{8}
$$

The two terms are, respectively, the rectangle-grid error and the Duhamel error from the retained nilpotent part.

## 2. The joint-source determinant cost splits into an exact kernel term and an exact observation term

The attachment already supplies the full mixed minimum. Let \(X\) embed the original scalar source, with Gram \(H_X=X^*X\), and let \(J\) be its onto cyclic value map:

$$
G=(JH_X^{-1}J^*)^{-1}.
$$

For the constructed physical section \(\mathcal R\), retain

$$
C_X=X^*\mathcal R,
$$

$$
H_Z=\mathcal R^*\mathcal R-C_X^*H_X^{-1}C_X,
\qquad
F=I-JH_X^{-1}C_X.
$$

The source compatibility

$$
\ker H_Z\subseteq\ker F
$$

allows the exact positive-range inverse:

$$
G_J=(G^{-1}+FH_Z^+F^*)^{-1}.
$$

These are the supplied equations (36)–(39), not new substitutions for their cross Gram.

Define

$$
T=G^{1/2}FH_Z^+F^*G^{1/2}\succeq0.
$$

Then

$$
G_J=G^{1/2}(I+T)^{-1}G^{1/2},
\qquad
\log\det G-\log\det G_J=\log\det(I+T).
\tag{9}
$$

### The complete allocation

Use the explicit \(G\)-orthonormal decomposition into the original kernel and its old-metric orthogonal complement. Write

$$
T=
\begin{pmatrix}
T_{11}&T_{12}\\
T_{12}^*&T_{22}
\end{pmatrix},
$$

and

$$
S_K=T_{11}-T_{12}(I+T_{22})^{-1}T_{12}^*\succeq0.
$$

The relative determinant decreases are

$$
\boxed{
\begin{aligned}
D_{\mathrm{obs}}&=\log\det(I+T_{22}),\\
D_{\mathrm{ker}}&=\log\det(I+S_K),\\
D_{\mathrm{total}}&=D_{\mathrm{obs}}+D_{\mathrm{ker}}
=\log\det(I+T).
\end{aligned}
}
\tag{10}
$$

The observed term comes from the lower-right block of the **inverse** metric. The kernel restriction comes from its full Schur complement. The term involving \(T_{12}\) cannot be discarded.

Invariantly, for the original observation \(\Lambda\),

$$
\boxed{
Q_J=
\left(
Q^{-1}+\Lambda FH_Z^+F^*\Lambda^*
\right)^{-1}.
}
\tag{11}
$$

For the original three columns \(V\), the entire observed and kernel forms are

$$
C_J=V^*\Lambda^*Q_J\Lambda V,
\qquad
R_J=V^*G_JV-C_J.
\tag{12}
$$

Thus all complex current factors are still computed from one common covariance, not independently selected scalar errors.

If \(t_1\ge\cdots\ge t_q\ge0\) are the eigenvalues of \(T\) and the observed dimension is \(r\),

$$
\boxed{
\sum_{i=q-r+1}^q\log(1+t_i)
\le D_{\mathrm{obs}}
\le\sum_{i=1}^r\log(1+t_i).
}
\tag{13}
$$

The actual observation orientation determines where it lies in this interval.

### Many new physical directions do not automatically give many new values

The constructed section has total degree at most \(k(2d-1)\). If its normal projection to the old scalar source vanishes on a class, that representative is a scalar polynomial in the total variable, of degree at most

$$
\min(N,k(2d-1)).
$$

Positivity of the original polynomial source makes physical equality here polynomial equality. Hence

$$
\boxed{
\operatorname{rank}H_Z
\ge
\max\{0,\ q-\min(N,k(2d-1))-1\}.
}
\tag{14}
$$

At fixed packet and \(N\asymp q\), this is \(q-O_h(k)\).

That is the rank of the **physical normal Gram**, not the rank of \(F\). A nonzero physical normal direction can still carry zero original cyclic value. Equation (14) therefore does not, by itself, force a large determinant improvement.

### The total canonical-return cost cannot disappear

Let

$$
G_S=\mathcal R^*\mathcal R
$$

retain the section’s entire physical scalar, and set

$$
D_C=\log\det G-\log\det G_J,
\qquad
D_S=\log\det G_S-\log\det G_J.
$$

Both are nonnegative because the joint source contains both original source systems.

The finite exterior inequality gives

$$
\boxed{\mathfrak d(G,G_S)\le D_C+D_S.}
\tag{15}
$$

Factor the identity map through \(G_J\): one factor is a contraction, and the other’s exterior norm is bounded by its full volume factor. Applying this in both directions proves (15).

Combining it with (4),

$$
\boxed{
\liminf_{k\to\infty}
\frac{D_C+D_S}{q\log(q/k)}\ge2.
}
\tag{16}
$$

It is the **sum** that is forced large. Either term may carry the cost. In particular, this does not convert the constructed metric estimate into a lower bound on the still-uncomputed canonical improvement alone.

### A certified range inverse

Suppose the actual kernel of \(H_Z\) is known and its positive spectrum has floor \(\lambda_+>0\). Then

$$
\boxed{
\frac{\lambda_+}{\lambda_++\epsilon}FH_Z^+F^*
\preceq
F(H_Z+\epsilon I)^{-1}F^*
\preceq FH_Z^+F^*.
}
\tag{17}
$$

For \(r_F=\operatorname{rank}(FH_Z^+F^*)\), the resulting joint determinant error is at most

$$
\boxed{r_F\log(1+\epsilon/\lambda_+).}
\tag{18}
$$

A fully algebraic floor is

$$
\lambda_+\ge
\frac{\operatorname{pdet}H_Z}
{(\operatorname{Tr}H_Z)^{\operatorname{rank}H_Z-1}}.
$$

This regularizes a **specified positive range**; it does not justify guessing the rank from a numerical midpoint.

## 3. Combining ES centres with unequal primary lengths produces a covariance, not just two variances

The attachment calculates the leakage caused by unequal chain lengths at a common RH sum centre. That result is retained. The new calculation lets the transported ES sum vary on the same labelled tuples.

For each factor, match the labelled root \(\rho\) with an ES root \(t_{i,\rho}\). The exact local algebra map sends

$$
t_{i,\rho}+z\longleftrightarrow\rho+z.
$$

Equivalently, a Hermite polynomial realizes this on the full local quotient. When multiplicities exceed one, the ES side is explicitly a **labelled jet thickening**; this is not a claim that the integer ES problem itself has acquired zeta-zero multiplicities.

On a tensor tuple, retain

$$
\kappa=\sum_i\rho_i,\qquad
\theta=\sum_i t_{i,\rho_i},\qquad
D=\sum_i(m_{i,\rho_i}-1),\qquad R=\sum_i z_i.
$$

The actions are

$$
\boxed{
A_R=\kappa I+R,\qquad
A_E=\theta I+R,\qquad
A_E-A_R=(\theta-\kappa)I.
}
\tag{19}
$$

### The minimal common reducing space

Group the actual positive tuple weights into \(W_{\kappa,\theta,D}\). The smallest subspace containing the original cyclic image and invariant under both actions and both adjoints is

$$
\boxed{
\mathscr W^{\mathrm{joint}}
=
\bigoplus_{\kappa,\theta,D}
\operatorname{span}\{R^j1_{\kappa,\theta,D}:0\le j\le D\}.
}
\tag{20}
$$

Each distinct triple is counted once.

The projectors are explicit: Hermite projectors select \(\kappa\); Lagrange polynomials in \(A_E-A_R\) select \(\theta\); and the attachment’s Casimir eigenvalues \(D(D+2)\) select the chain length. Powers of \(R\) then generate the whole chain. No uniform bound on inverse differences of distinct \(\theta\)'s is inferred through their collisions.

For

$$
S_j=\sum_{\theta,D}W_{\kappa,\theta,D}\binom Dj,
\qquad
g_j=(j!)^2\eta^{2j}S_j,
$$

the exact return is

$$
v_{\kappa,j}
=
\frac{\sum_{\theta,D}
W_{\kappa,\theta,D}\binom Dj\,u_{\kappa,\theta,D,j}}
{S_j}.
\tag{21}
$$

### The full mixed Gram

Define

$$
\pi_j(\theta,D)=\frac{W_{\kappa,\theta,D}\binom Dj}{S_j},
$$

and, in that probability,

$$
v_j=\mathbb E|\theta-\mathbb E\theta|^2,\qquad
d_j=\operatorname{Var}(D),\qquad
c_j=\mathbb E[(\theta-\mathbb E\theta)(D-\mathbb ED)].
$$

The covariance \(c_j\) can be complex.

For the adjoint ES leakage

$$
Z_E=(I-\Pi)A_E^\dagger\beta,
$$

the complete raw Gram in the original cyclic jet basis is

$$
\boxed{
\begin{aligned}
(Z_E^*G_{\mathrm{tensor}}Z_E)_{jj}
&=
g_j\left[
v_j+\eta^2\frac{S_{j-1}}{S_j}d_{j-1}
\right],\\
(Z_E^*G_{\mathrm{tensor}}Z_E)_{j,j+1}
&=g_j\eta^2(j+1)c_j.
\end{aligned}
}
\tag{22}
$$

The length term is absent at \(j=0\); the lower entry is the conjugate of the upper.

The neighbouring term arises because the centre residual from input \(j\) and the length residual from input \(j+1\) both land at degree \(j\). Their inner product is exactly the covariance in (22). Adding only the two diagonal variance matrices would miss it.

For the attachment’s length example \((2,2,0)\), unit weights, \(\eta=1/3\), and added centre labels \((1,4,2)\), the unchanged cyclic Gram is

$$
\operatorname{diag}(3,4/9,8/81),
$$

and the new raw leakage Gram is

$$
\boxed{
\begin{pmatrix}
14/3&2/27&0\\
2/27&251/243&0\\
0&0&2/9
\end{pmatrix}.
}
\tag{23}
$$

The \(2/27\) entry is the mixed covariance. This is a checked finite diagnostic model, not a native moment evaluation.

### The common-multiplicity ES return is now complete at every nilpotent level

For a sorted hard-prime witness \((p;x,y,z)\), set

$$
\mathfrak d=p-x-y+z>0.
$$

At fixed RH grid coordinates \((u,v)\), the ES centre depends on the remaining occupation \(j\) by

$$
\theta=kt_4+(t_2-t_4)u+(t_3-t_4)v+\mathfrak d\,j.
$$

With common \(D=k(m-1)\),

$$
\boxed{
\dim\mathscr W^{\mathrm{joint}}
=(D+1)\binom{k+3}{3},
\qquad
\dim\mathscr W^{\mathrm{joint}}-q
=(D+1)\binom{k+1}{3}.
}
\tag{24}
$$

For the explicitly chosen unit root weights, the forward leakage eigenvalue at every nilpotent level is

$$
\boxed{
\mathfrak d^2\frac{uv(k-u)(k-v)}{k^2(k-1)}.
}
\tag{25}
$$

The multinomial weights and their binomial generating identities are retained exactly; standard coefficient conventions agree with DLMF §26.3. ([DLMF][2])

Therefore

$$
\boxed{
\operatorname{rank}L_E=(D+1)(k-1)^2,
\qquad
\dim\ker L_E=4k(D+1).
}
\tag{26}
$$

The same one-factor sections realize this enlarged space in the supplied total-degree bound. But its physical value space is larger than the original cyclic image. Returning it through (21) introduces an actual additional quotient; it is not the original jet map unchanged.

## 4. Every simultaneous collision/jet-scale exponent is now explicit

The attachment supplies the exact two-centre divided-jet matrix and expresses simultaneous scaling through a minimum over minors. That minimum can be evaluated for **every pair of lengths and every nonnegative power-law scale**.

Let \(e\ge f\ge1\), \(n=e+f\), and retain

$$
\mathbb C[u]/(u^e(u-z)^f).
$$

The output is the full divided jets at \(0,z\). Weight the derivative of order \(j\) by

$$
\eta^j,\qquad \eta=|z|^a,\quad a\ge0.
$$

Fixed positive jet factors are retained. A residual output metric must remain uniformly positive and bounded after these powers for the following exponents to apply.

Write the singular values in decreasing order as

$$
\sigma_j\asymp |z|^{\nu_j},
\qquad \nu_1\le\cdots\le\nu_n.
$$

For \(0\le a\le1\),

$$
\boxed{
0,a,\ldots,(e-1)a;\qquad
e-f+2j-1+a(f-j),\quad j=1,\ldots,f.
}
\tag{27}
$$

For \(a\ge1\),

$$
\boxed{
(a+1)j,\ (a+1)j+1,\quad j=0,\ldots,f-1;
\qquad
aj+f,\quad j=f,\ldots,e-1.
}
\tag{28}
$$

The only transition is \(a=1\), where both lists become

$$
\boxed{0,1,\ldots,e+f-1.}
\tag{29}
$$

For example, \((e,f)=(3,2)\) gives

$$
\begin{cases}
(0,a,2a,2+a,4),&0\le a\le1,\\
(0,1,a+1,a+2,2a+2),&a\ge1.
\end{cases}
$$

For the first regime, bounded Taylor row elimination leaves the residual block

$$
C_{j,c}=\eta^j\binom{e+c}{j}z^{e+c-j}.
$$

Its least \(r\)-minor exponent is

$$
r(e-f+r)+\frac{ar(2f-r-1)}2,
$$

attained by the lowest columns and highest rows. Its coefficient is a nonzero falling-factorial Vandermonde. Consecutive minor orders yield (27).

For the second regime, factor the column powers \(z^m\) and row powers \(|z|^{(a-1)j}\). The smallest available derivative orders at the two centres, paired with the first columns, give a nonzero confluent Vandermonde. This yields (28).

### Every inverse exterior rank, including constants at the transition

For inverse exterior rank \(r\), the divergence exponent is the sum of the largest \(r\) entries in the displayed exponent list. When \(0\le a\le1\), it is

$$
\boxed{
\mathfrak e_r(a)=
\begin{cases}
r(e+f-r)+ar(r-1)/2,&r\le f,\\[2mm]
ef+\dfrac a2\{f(f-1)+(r-f)(2e-r+f-1)\},&r>f.
\end{cases}
}
\tag{30}
$$

At \(a=1\),

$$
\boxed{\mathfrak e_r(1)=\frac{r(2n-r-1)}2.}
\tag{31}
$$

There are finite explicit constants at that transition. Let \(B\) be the fixed weighted Hermite matrix at \(0,1\), and put

$$
\beta_B=\operatorname{Tr}(B^*B),\qquad
\alpha_B=\frac{\det(B^*B)}{\beta_B^{n-1}}>0.
$$

Then

$$
\boxed{
\beta_B^{-r/2}|z|^{-r(2n-r-1)/2}
\le
\|\wedge^rE_{z,|z|}^{-1}\|
\le
\alpha_B^{-r/2}|z|^{-r(2n-r-1)/2}.
}
\tag{32}
$$

A physical section scalar \(T(z)\) multiplying the output Gram multiplies this inverse-exterior norm by \(T(z)^{-r/2}\). In particular, the attachment’s product of \(\tau_{i,\eta}\) cannot be omitted. If \(T(z)\asymp |z|^{-b}\), all absolute singular exponents shift by \(-b/2\); the relative condition number does not.

## 5. What the integration makes actionable

The attachment’s family construction now connects to the continuing programme through explicit quantities rather than a general assertion that another metric is controlled.

The **canonical comparison** has the lower bounds (4)–(5). The **complete mixed minimum** has the allocation (10), the range certificate (17)–(18), and the two-cost lower bound (16). The **joint ES/RH action** has the minimal enlarged value space (20) and the complete phase-sensitive covariance (22). The **collision calculation** now has closed exponents and constants, not an unevaluated minor minimization.

What is still required for the native signed conclusion is the actual cross Gram \(C_X\), its full value map \(F\), and their orientation relative to the original observation kernel. The new section’s degree and conditioning bounds do not assign those entries. The source itself identifies precisely that remaining return, and the new formulas preserve it.

The package includes the supplied text unchanged, the four complete proof notes, the fresh test receipts, a claim register separating finite results from consequences conditional on NG20–NG21, and the Codex handoff. The PDF was rendered and inspected; the archive’s CRC and every manifest hash were verified.

### References

*General-family control: Multiplicities, collisions, source sections, and all mixed minima*. (2026, September 20). [User-supplied research continuation; author unspecified in supplied text]. The complete supplied text and its original equation numbering are preserved in the package.

Higham, N. J. (2020, October 13). *What is the singular value decomposition?* Author’s mathematical exposition. Used for standard singular-value and norm conventions; the exterior comparison inequalities above are derived independently. ([Nick Higham][1])

National Institute of Standards and Technology. (n.d.). *NIST Digital Library of Mathematical Functions*, §26.3, Lattice paths: Binomial coefficients. ([DLMF][2])

Split-Zero research programme. (2026, September 20). *Gaussian spectral actions through the original arithmetic quotient* [Research manuscript, NG1–NG27]. *Zeta-function research reader*, commit `b1f3e2e1879c40f411eb263dde171589cb5f9390`. The directly consumed passage is NG16–NG22, including the original compression law and rank-one relation.

[1]: https://nhigham.com/2020/10/13/what-is-the-singular-value-decomposition/ "https://nhigham.com/2020/10/13/what-is-the-singular-value-decomposition/"
[2]: https://dlmf.nist.gov/26.3 "https://dlmf.nist.gov/26.3"
