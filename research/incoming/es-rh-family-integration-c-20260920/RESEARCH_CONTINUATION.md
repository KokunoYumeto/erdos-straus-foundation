# Integration record and scope

This continuation integrates the supplied **General-family control: multiplicities, collisions, source sections, and all mixed minima** rather than replacing it with a canonical-metric assertion. Its complete supplied text is preserved byte-for-byte in `sources/GENERAL_FAMILY_INPUT.md`. The standalone package and full proof files linked inside that text were not retrieved; their execution reports are not counted here.

The main results are the quantitative canonical/constructed metric separation derived from the pinned NG20–NG21 theorem (MR7–MR8), the complete two-minimum allocation and its corrected positive-range certificate (JS6–JS15), the combined ES-centre/primary-length covariance and minimal reducing enlargement on the generated top-chain sector (ER5–ER14), and the complete collision/jet-scale phase diagram (CP2–CP11). The inherited native spectral law is explicitly identified; no native moment has been assigned a numerical value. Neither global conjecture is asserted to be resolved.

**Fresh verification.** 4 suites completed in ordinary and optimized Python, with 1284 exact checks and 22 negative-control executions per mode. All paired standard outputs and JSON receipts are byte-identical. The code checks exact finite interfaces and bounded synthetic models, not unknown native moment values or the asymptotic theorem by finite samples. This is not a Lean build. The full record is `results/VERIFICATION_SUMMARY.json`.

The RH source snapshot was checked at commit `b1f3e2e1879c40f411eb263dde171589cb5f9390`; this integration is applied to ES foundation base `5787b359a73edd62130caf76f573a40d607463c1`. The newly observed finite-theta certificate is recorded as an update, not used as an unproved extra premise in the integration. The NG20–NG21 passage consumed below is read at the RH pin and retains blob `6122e3b4f165df907a46ddcbc739f4dc159d65c6`. The full reading boundary and citations are in `SOURCE_LEDGER.md`.

The general-family source is denoted **GF**, with its original equation numbers. New results are labelled **MR**, **JS**, **ER**, and **CP**, so they cannot be mistaken for upstream theorem labels. All four original scalar cutoffs remain distinct when a result is returned to an endpoint calculation. The received material is preserved unchanged while the corrected live proof is integrated here.

\newpage

# 1. The constructed section and the canonical metric have a quantitative separation

**Basis and status.** The supplied *General-family control* text (GF below), equations (3), (10), (26)–(31), constructs finite tensor-source sections and their exact pullback metrics. We retain that construction. The asymptotic conclusions in this section are conditional consequences of the repository's native compression law NG20 and rank-one identity NG21, at the pinned version in `SOURCE_LEDGER.md`. We do not claim an independent new proof of the entire upstream spectral-transfer theorem. The finite exterior inequalities used to combine these inputs are proved here.

## 1.1 Same algebra, different metrics, with every scalar retained

Fix the same full divisor \(h\) and the same source measure used by NG1. Within that fixed source, take the stipulated off-line quartet
\[
\rho=\tfrac12\pm\delta\pm i\gamma,\qquad 0<\delta<\tfrac12,\quad\gamma>2,
\]
with a common fixed multiplicity \(m\ge1\). This is the programme's hypothetical-divisor domain, not an assertion that an off-line zero exists. Let \(k\equiv1\pmod4\),
\[
D=k(m-1),\qquad q=(D+1)(k+1)^2,\qquad c=k/2,
\]
and let \(A_k=M_S\) act on the full cyclic algebra \(C_k=\mathbb C[S]/\chi_k\), including every nilpotent level. Set
\[
M_k=(A_k-cI)/i. \tag{MR1}
\]
The canonical metric at the scalar-polynomial cutoff \(N\) is \(G_{k,N}\). Let \(\widetilde G_{k,\eta}\) denote the **actual physical pullback** of the constructed section in GF(28). For identical factors,
\[
\widetilde G_{k,\eta}=\tau_\eta^kG_{k,\eta}.
\]
We do not set \(\tau_\eta=1\). The identity
\((\tau_\eta^kG_{k,\eta})^{-1}X^*(\tau_\eta^kG_{k,\eta})=G_{k,\eta}^{-1}X^*G_{k,\eta}\)
explains exactly why that scalar cancels from adjoints and endomorphism norms in this section. It does not cancel from the norm of the section as a map into the physical source.

Use the source's choice \(\eta=\delta/(D+1)\) when \(D>0\); when \(D=0\), the nilpotent operator is zero and no value of \(\eta\) affects its metric. In the explicit orthonormal jet frame the operator has blocks
\[
M_k=Z_k+N_k,\qquad
Z_k|_{a,b}=[(2b-k)\gamma-i(2a-k)\delta]I_{D+1}.
\]
The source's weighted-shift entries give
\[
\|N_k\|\le\delta/2,\qquad
\|M_k\|_{\widetilde G}\le B_k:=kR_0+\delta/2,
\quad R_0=\sqrt{\delta^2+\gamma^2}. \tag{MR2}
\]
Indeed each squared shift coefficient is \(\eta^2(j+1)(D-j)\le\eta^2(D+1)^2/4\). Since \(k\) is odd, each diagonal block of \(Z_k\) has modulus at least \(R_0\). The finite nilpotent inverse series, or its geometric norm bound, proves
\[
\|M_k^{-1}\|_{\widetilde G}\le(R_0-\delta/2)^{-1}. \tag{MR3}
\]
All block weights and all physical unit maps from GF are retained by their specified congruences. They do not change these intrinsic metric norms.

## 1.2 A finite identity-map exterior bound

For two positive metrics \(G_c,G_a\) on the same \(q\)-dimensional algebra, let
\[
R=G_c^{-1/2}G_aG_c^{-1/2},\qquad
\lambda_1\ge\cdots\ge\lambda_q
\]
be the logarithms of the eigenvalues of \(R\). Define
\[
\mathfrak d(G_c,G_a)=\min_{b\in\mathbb R}\sum_{i=1}^q|\lambda_i-b|,
\quad \kappa(G_c,G_a)=e^{\lambda_1-\lambda_q}. \tag{MR4}
\]
The logarithmic distance and this metric condition number are unchanged when either metric is multiplied by a positive scalar. They are also unchanged under a simultaneous coordinate congruence.

Let \(L=\operatorname{id}:(C,G_c)\to(C,G_a)\), and \(h=\lfloor q/2\rfloor\). The singular values of \(L\) are \(e^{\lambda_i/2}\). A median minimizes the sum of absolute deviations, so
\[
\mathfrak d=\sum_{i=1}^h\lambda_i-\sum_{i=q-h+1}^q\lambda_i
=2\log\bigl(\|\wedge^hL\|\,\|\wedge^hL^{-1}\|\bigr). \tag{MR5}
\]
This is an exact relation to the original inverse-exterior programme, not a claim that the identity map is an isometry. To see the exterior norm formula, apply the singular value decomposition: in wedge bases the diagonal entries are products of the corresponding singular values. The largest is the product of the largest \(h\) values. No normalization of the two original metrics is used in the statement.

**Finite theorem.** Suppose \(b>0\), \(C>0\), \(1\le r\le q-1\), and an endomorphism \(M\) has at least \(r\) singular values, in \(G_a\), not less than \(bq\), while \(\|M\|_{G_c}\le C\). For \(p=\min(r,q-r)>0\),
\[
\mathfrak d(G_c,G_a)\ge2r\log(bq/C),
\qquad
\log\kappa(G_c,G_a)\ge\frac{2r}{p}\log(bq/C). \tag{MR6}
\]
A negative right side is permitted and gives no information. For the useful case \(bq>C\), proof is as follows:
\[
(bq)^r\le\|\wedge^rM\|_{G_a}
\le\|\wedge^rL\|\,C^r\,\|\wedge^rL^{-1}\|.
\]
Twice the logarithm of the two exterior factors is
\(\delta_r=\sum_{i\le r}\lambda_i-\sum_{i>q-r}\lambda_i\).
Cancellation of the overlap gives \(\delta_r=\delta_{q-r}\), while \(\delta_p\le\mathfrak d\) and \(\delta_p\le p(\lambda_1-\lambda_q)\). These prove both inequalities. The same proof without assuming a sign gives the stated universally valid bounds.

## 1.3 The quantitative canonical comparison

Take a canonical cutoff sequence with \((N+1-q)/q\to s\in(0,1]\), or one of the source's separately proved \(s=0\) sequences \(N=q-1,q\). For \(s>0\), NG20 states that the eigenvalue distribution of the selfadjoint attained compression \(C_{k,N}/q\) tends to the positive probability
\[
\nu_s(dy)=\left[h_0\left(\frac y{1+s}\right)-s|y|\rho_s(y^2)\right]dy,
\quad h_0(y)=\frac1{2\pi}\operatorname{arcosh}\frac2{|y|}\,\mathbf1_{0<|y|<2}.
\]
For the separately proved \(s=0\) sequences, write instead
\[
\nu_0(dy)=h_0(y)\,dy;
\]
the provider does not define \(\rho_0\), so no expression \(0\cdot\rho_0\) is used. Each explicit density has no atom at zero. NG21 gives \(M_k-C_{k,N}\) of rank at most one. Hence
\(M_k^{\dagger_{G_{k,N}}}M_k-C_{k,N}^2\) has rank at most two, so their normalized squared-singular-value measures have the same weak limit. This rank statement is checked by expanding the square of \(C+uv^*\); its difference has range in \(\operatorname{span}\{Cu,v\}\).

For every \(\varepsilon\in(0,1/2)\), choose \(b>0\) so that \(\nu_s((-b,b))<\varepsilon/2\). The limit and the rank bound imply that for all sufficiently large \(k\), at least \(r_k=\lfloor(1-\varepsilon)q\rfloor\) canonical singular values of \(M_k\) are at least \(bq\). Apply MR6 with the constructed metric and MR2. Since \(B_k=O_{\delta,\gamma}(k)\) and \(q/k\to\infty\),
\[
\boxed{\liminf_{k\to\infty}
\frac{\mathfrak d(\widetilde G_{k,\eta},G_{k,N})}
{q\log(q/k)}\ge2.} \tag{MR7}
\]
The condition-number bound gives, for each fixed \(\varepsilon\), a lower limit at least \(2(1-\varepsilon)/\varepsilon\) for the quotient of \(\log\kappa\) by \(\log(q/k)\). Letting \(\varepsilon\downarrow0\) proves
\[
\boxed{\frac{\log\kappa(\widetilde G_{k,\eta},G_{k,N})}{\log(q/k)}
\longrightarrow+\infty.} \tag{MR8}
\]
Thus the canonical/constructed metric condition number exceeds every fixed power of \(k\), eventually. This does **not** contradict GF(1): its condition number compares two constructed metrics, not either one with \(G_{k,N}\). It also does not give an effective threshold in \(k\), because the consumed spectral law does not supply one.

## 1.4 Two heat scales that must not be identified

For fixed \(t>0\), the same argument with the bounded function \(e^{-t x^2}\) gives
\[
\frac1q\operatorname{tr}e^{-tM_k^{\dagger_{G_{k,N}}}M_k/q^2}
\to H_s(t):=\int e^{-ty^2}\,d\nu_s(y),
\]
while MR2 gives
\[
\frac1q\operatorname{tr}e^{-tM_k^{\dagger_{\widetilde G}}M_k/q^2}\to1.
\tag{MR9}
\]
At the different, explicitly declared \(k\)-scale,
\[
\boxed{\frac1q\operatorname{tr}e^{-tM_k^{\dagger_{G_{k,N}}}M_k/k^2}\to0.} \tag{MR10}
\]
For proof, outside a threshold \(bq\) each summand is at most \(e^{-t(bq/k)^2}\); inside it the normalized count tends to at most \(\nu_s([-b,b])\). First let \(k\to\infty\), then \(b\downarrow0\).

The constructed metric instead has the source's nonzero limit
\[
\mathcal K_\infty(t)=\frac\pi{4t\delta\gamma}
\operatorname{erf}(\delta\sqrt t)\operatorname{erf}(\gamma\sqrt t)>0.
\tag{MR11}
\]
There is a direct explicit error bound, not a new uncomputed constant:
\[
\left|\frac1q\operatorname{tr}e^{-tM_k^{\dagger_{\widetilde G}}M_k/k^2}
-\mathcal K_\infty(t)\right|
\le\frac{4tR_0^2}{k+1}
+t\left(\frac{R_0\delta}{k}+\frac{\delta^2}{4k^2}\right).
\tag{MR12}
\]
The second term is the Duhamel bound between the two positive squares of \(M_k/k\) and \(Z_k/k\). Their norm difference is at most \(2R_0\delta/(2k)+(\delta/(2k))^2\). The normalized trace error is at most \(t\) times that norm, because both semigroups are contractions. The first term is the rectangle-grid error for \(e^{-t(\delta^2x^2+\gamma^2y^2)}\): its sum of coordinate Lipschitz constants is at most \(2tR_0^2\), and an explicit coupling of each of the \(k+1\) equal cells to its grid node has displacement at most \(2/(k+1)\) in each coordinate. The integral separates into two elementary Gaussian integrals, proving MR11.

The holomorphic trace is metric-independent:
\[
\frac1q\operatorname{tr}e^{-t(M_k/k)^2}\to
\mathcal H_\infty(t)=\frac1{4\delta\gamma}
\int_{-\gamma}^{\gamma}\int_{-\delta}^{\delta}e^{-t(x-iy)^2}\,dy\,dx.
\tag{MR13}
\]
Its grid error is at most
\(4tR_0(\delta+\gamma)e^{t\delta^2}/(k+1)\), by the same coupling and direct differentiation. The supplied error-function primitive in GF(57) evaluates this integral.

For an endomorphism \(M\) and a positive metric \(G\), define the comparison term used here by
\[
\Delta_\tau(M;G)=\Re\operatorname{tr}e^{-\tau M^2}
-\operatorname{tr}e^{-\tau M^{\dagger_G}M}.
\]
The canonical normalized heat gap at \(k\)-scale therefore tends to \(\Re\mathcal H_\infty(t)\), while the constructed one tends to \(\Re\mathcal H_\infty(t)-\mathcal K_\infty(t)\). In particular,
\[
\lim_{t\downarrow0}\lim_{k\to\infty}\frac1q\Delta_{t/k^2}(M_k;G_{k,N})=1,
\qquad
\lim_{k\to\infty}\frac1q\Delta_0(M_k;G_{k,N})=0.
\tag{MR14}
\]
This is a noncommutation of heat-time and packet-degree limits, not an equality of the two metrics. It supplies a precise interpretation of their different heat scales and of the compulsory comparison cost MR7–MR8.

\newpage

# 2. The mixed source minimum: its complete allocation and a certified range inverse

**Basis and status.** GF(36)–(39) supplies an exact joint minimum on the sum of the original scalar source and the constructed tensor section. This section proves the full kernel/observation split of that minimum, its rank-aware regularization, and a dimension bound on the new physical normal directions. These are finite identities. They do not assign a value to the unknown original cross Gram.

## 2.1 Reconstruct the supplied joint minimum

Work in one finite ambient original physical source with its complete Hermitian form. Let \(C\) have dimension \(q\). Let \(X\) embed the original scalar polynomial source, with \(H_X=X^*X>0\), and let \(J\) be its onto value map to \(C\). The supplied \(\mathcal R\) below is a genuine right inverse of the ambient physical value map. Write
\[
G=(JH_X^{-1}J^*)^{-1}.
\]
Let \(\mathcal R:C\to\mathscr H\) be the supplied constructed section, carrying the same physical value for each original class. Put
\[
C_X=X^*\mathcal R,\quad Z=(I-XH_X^{-1}X^*)\mathcal R,
\quad H_Z=Z^*Z=\mathcal R^*\mathcal R-C_X^*H_X^{-1}C_X,
\]
\[
F=I-JH_X^{-1}C_X. \tag{JS1}
\]
All stars here use the indicated original physical form; a coefficient implementation inserts that Gram explicitly. Since \(Zc=0\) means that two source representatives are physically equal, their original values agree: \(\ker H_Z\subset\ker F\). This compatibility is a required hypothesis of the joint-source construction, not a numerical rank guess.

The scalar source and the normal source are orthogonal. Minimizing their squared norms subject to the combined value condition gives
\[
G_J=(G^{-1}+F H_Z^+F^*)^{-1}.
\tag{JS2}
\]
For an elementary proof, restrict the normal coefficient space to the positive range of \(H_Z\), where it has an ordinary positive inverse. The combined onto matrix then has inverse quotient Gram equal to the sum of the two inverse quotient covariance matrices. The killed kernel contributes neither value nor norm. This is also the formula obtained by minimizing a full block diagonal quadratic form with a Lagrange multiplier. It is exactly GF(37), rederived for the extensions below.

Define
\[
T=G^{1/2}F H_Z^+F^*G^{1/2}\succeq0.
\]
Then
\[
\boxed{G_J=G^{1/2}(I+T)^{-1}G^{1/2},\qquad
\log\det G-\log\det G_J=\log\det(I+T).} \tag{JS3}
\]
A changed section metric \(\mathcal R^*\mathcal R\) alone does not determine \(T\). If the new section lies entirely in the old scalar source, \(H_Z=F=0\), so \(T=0\), even though its own Gram can exceed the old minimum by an arbitrary relation energy. The delivered exact fixture tests this distinction.

## 2.2 New physical directions can have extensive rank

Let the fixed one-factor divisor have degree \(d\). GF constructs \(\mathcal R\) in total polynomial degree at most \(K=k(2d-1)\). The polynomial realization is faithful: positivity of the product density makes the norm of every nonzero polynomial positive. Moreover, for nonzero \(P\), substitution into independent variables preserves the top homogeneous term, so
\[
\deg P(S_1+\cdots+S_k)=\deg P.
\]
The section itself is injective because its value is the original class.

If \(Zc=0\), then \(\mathcal R c\) belongs to the original scalar source and hence equals \(P(S_1+\cdots+S_k)\) with \(\deg P\le N\). Equality in the physical space is equality of polynomials by that positivity. Its total degree is exactly \(\deg P\). Therefore it is at most \(\min(N,K)\). The subspace of such scalar polynomials has dimension \(\min(N,K)+1\), proving
\[
\boxed{\operatorname{rank}H_Z\ge
\max\{0,\ q-\min(N,k(2d-1))-1\}.} \tag{JS4}
\]
On a fixed one-factor divisor of degree \(d\) and \(N\asymp q\), this is \(q-O_d(k)\). This is a statement about **physical normal directions**, not about \(\operatorname{rank}F\). Directions may have nonzero physical norm but zero original quotient value. No lower bound on the determinant gain JS3 follows just from JS4.

## 2.3 Exact division between an original kernel and its observed quotient

Fix an onto original observation \(\Lambda:C\to C_{\rm obs}\), let \(r=\operatorname{rank}\Lambda\), and set \(K=\ker\Lambda\). Use the explicit isometry \(G^{1/2}\), then an orthonormal basis adapted to \(K\) and its old-metric orthogonal complement. In these proof coordinates the old metric is \(I\), and split the **full** covariance as
\[
T=\begin{pmatrix}T_{11}&T_{12}\\T_{12}^*&T_{22}\end{pmatrix},
\quad
S_K=T_{11}-T_{12}(I+T_{22})^{-1}T_{12}^*\succeq0.
\tag{JS5}
\]
Nonnegativity follows from the Schur complement of the positive semidefinite block matrix \(T+\operatorname{diag}(0,I)\).

The inverse-block formula gives the restriction of the new metric to the old kernel as \((I+S_K)^{-1}\). The **full new quotient** by that same kernel has inverse covariance \(I+T_{22}\), because the lower-right block of the inverse metric \(I+T\) is \(I+T_{22}\). Thus
\[
\boxed{
\begin{aligned}
D_{\rm obs}&=\log\det(I+T_{22}),\\
D_{\rm ker}&=\log\det(I+S_K),\\
D_{\rm total}&=D_{\rm obs}+D_{\rm ker}=\log\det(I+T).
\end{aligned}} \tag{JS6}
\]
Each \(D\) is a **relative determinant decrease from the original metric** on the stated restriction or quotient; original coordinate Gram determinants have not been set to one in the result. The cross term in \(S_K\) is indispensable.

![The exact source maps, normal covariance, joint minimum, and determinant allocation. Every arrow is typed in JS1--JS9; the mixed block \(T_{12}\) survives in the old-kernel Schur complement.](figures/joint_source_allocation.pdf){width=96%}

Invariantly, with \(Q=(\Lambda G^{-1}\Lambda^*)^{-1}\),
\[
Q_J=(Q^{-1}+\Lambda F H_Z^+F^*\Lambda^*)^{-1}.
\tag{JS7}
\]
For a specified column map \(V:\mathbb C^3\to C\), the observed and kernel forms are exactly
\[
C_J=V^*\Lambda^*Q_J\Lambda V,
\qquad R_J=V^*G_JV-C_J. \tag{JS8}
\]
These compute the full complex pairings using one shared covariance, not independent scalar error choices.

If \(t_1\ge\cdots\ge t_q\ge0\) are the eigenvalues of \(T\), min–max for the rank-\(r\) observation compression gives
\[
\boxed{\sum_{i=q-r+1}^q\log(1+t_i)
\le D_{\rm obs}\le\sum_{i=1}^r\log(1+t_i).} \tag{JS9}
\]
The endpoints are achieved by aligning the observation with the corresponding eigenvectors, but the actual programme observation has its fixed orientation and cannot be selected to attain either endpoint. In particular \(T=\operatorname{diag}(t,0)\) and a unit observed row \((\cos\theta,\sin\theta)\) give \(D_{\rm obs}=\log(1+t\cos^2\theta)\), while the total is always \(\log(1+t)\). A total volume bound alone does not specify its allocation.

## 2.4 A certified alternative to a guessed pseudoinverse

Suppose the actual kernel of \(H_Z\) is specified. Let
\[
\mu=\lambda_{\min}^{+}(H_Z)
\]
be its actual smallest positive eigenvalue, and fix a certified number
\(0<\underline\lambda\le\mu\). Put
\[
C=F H_Z^+F^*,\qquad C_\varepsilon=F(H_Z+\varepsilon I)^{-1}F^*,\quad\varepsilon>0.
\]
Since \(F\) kills the exact zero eigenspace, diagonalizing \(H_Z\) on its positive range proves
\[
\boxed{\frac{\underline\lambda}{\underline\lambda+\varepsilon}C
\preceq C_\varepsilon\preceq C.} \tag{JS10}
\]
Let \(G_{J,\varepsilon}=(G^{-1}+C_\varepsilon)^{-1}\). Inverting the retained positive inequalities yields
\[
G_J\preceq G_{J,\varepsilon}
\preceq(1+\varepsilon/\underline\lambda)G_J.
\]
The relative difference has rank at most \(r_C=\operatorname{rank}C\). Consequently
\[
\boxed{0\le\log\det G_{J,\varepsilon}-\log\det G_J
\le r_C\log(1+\varepsilon/\underline\lambda).} \tag{JS11}
\]
This is an explicit error for a specified regularization, not permission to repair an unknown rank with a diagonal perturbation.

A computable positive floor is available from a certified rank \(r_Z\): the product of the positive eigenvalues is the sum of all principal minors of size \(r_Z\), denoted \(\operatorname{pdet}H_Z\). Hence
\[
\mu\ge\underline\lambda_{\rm det}:=
\frac{\operatorname{pdet}H_Z}{(\operatorname{tr}H_Z)^{r_Z-1}}.
\tag{JS12}
\]
Thus \(\underline\lambda=\underline\lambda_{\rm det}\) is one admissible choice in JS10--JS11. It is rational when the certified entries of \(H_Z\) are rational; for original moment data it is an explicit positive real number unless a rational outward enclosure has also been constructed. This distinction is necessary: an arbitrary certified lower bound need not itself be at least \(\underline\lambda_{\rm det}\).
If \(H_Z=0\), compatibility forces \(F=0\), and the joint metric equals \(G\); no positive-range bound is used.

## 2.5 Consequence for heat transport, including the unchanged endomorphism

For a fixed endomorphism \(M\), the proved metric variation identity from the preceding continuation gives
\[
|\operatorname{tr}e^{-tM^{\dagger_{G_J}}M}
-\operatorname{tr}e^{-tM^{\dagger_G}M}|
\le\frac1{\mathrm e}\mathfrak d(G,G_J)
\le\frac1{\mathrm e}\log\det(I+T),\qquad t>0.
\tag{JS13}
\]
For completeness, along \(G_s=G_0^{1/2}e^{sK}G_0^{1/2}\), let \(B_s=e^{sK/2}G_0^{1/2}MG_0^{-1/2}e^{-sK/2}\), \(X=B_s^*B_s\), and \(Y=B_sB_s^*\). Direct differentiation and cyclicity give the derivative \(t\operatorname{tr}K(Xe^{-tX}-Ye^{-tY})\). The bracket has trace zero and operator norm at most \(1/\mathrm e\), because \(0\preceq tXe^{-tX},tYe^{-tY}\preceq\mathrm e^{-1}I\). Subtract a scalar median from \(K\), apply trace/operator duality, and integrate. For JS13 the relative eigenvalues are \((1+t_i)^{-1}\), so their median distance is at most \(\sum_i\log(1+t_i)\). The regularization error JS11 similarly gives a heat error at most \(r_C\log(1+\varepsilon/\underline\lambda)/\mathrm e\).

This holds for a fixed quotient endomorphism. If the observed endomorphism changes with its minimum lift, that operator change must also be propagated via the actual lift; a bound for its metric alone does not cover it. For an invertible conductor \(L\), its pulled-back target metric is \(L^*G_WL\), not automatically the original \(G_U\).

## 2.6 Explicit source inputs and their finite extent

GF(39) gives every cross-Gram entry by an exponential-generating-function contraction of the actual one-factor pairings \(\langle s^j,R_ie_\alpha\rangle\). If the one-factor sections have degree at most \(n_0=2d-1\) and the original scalar cutoff is \(N\), those pairings use one-factor moments through degree \(N+n_0\); the source Gram uses moments through \(2N\), and the section Gram through \(2n_0\). Thus the full finite calculation consumes moments through \(2\max(N,n_0)\), with their complex binomial coefficients and actual tensor multiplicities. Their values are not supplied by the section's degree bound or by its metric condition number. JS1–JS13 specify the complete receiver once those original entries and their outward errors are given.

## 2.7 A lower bound on the sum of the two actual minimum costs

Let \(G_S=\mathcal R^*\mathcal R\), retaining its full physical scalar. The joint source contains both the old scalar source and this section, so \(G_J\preceq G,G_S\). Define two nonnegative quantities
\[
D_C=\log\det G-\log\det G_J,
\qquad D_S=\log\det G_S-\log\det G_J.
\]
Then
\[
\boxed{\mathfrak d(G,G_S)\le D_C+D_S.} \tag{JS14}
\]
For proof, factor the identity \((C,G)\to(C,G_S)\) through \((C,G_J)\). The first map is a contraction. The product of the top \(h=\lfloor q/2\rfloor\) singular values of the second is at most its full determinant ratio \((\det G_S/\det G_J)^{1/2}\), since all its singular values are at least one. Reverse the two metrics for the inverse map. Multiply the bounds and use MR5. No abstract triangle inequality for a matrix logarithm is required.

This finite constant is sharp: \(G=\operatorname{diag}(16,1)\), \(G_S=\operatorname{diag}(1,9)\), \(G_J=I\) gives \(D_C=\log16\), \(D_S=\log9\), and both sides of JS14 equal \(\log144\). Applied to the actual family and the inherited canonical spectral law, MR7 gives
\[
\boxed{\liminf\frac{D_C+D_S}{q\log(q/k)}\ge2.} \tag{JS15}
\]
It is the sum that is forced large. Either summand can bear the cost; this does not assign a lower bound to the uncomputed canonical improvement alone. The second summand is itself a full relation-energy cost: if \(\mathcal R_J\) is the minimum section in the joint physical source, then \(\mathcal R-\mathcal R_J\) is a value-zero vector orthogonal to its minimum, and
\[
G_S=G_J+(\mathcal R-\mathcal R_J)^*(\mathcal R-\mathcal R_J).
\]
This supplies the exact positive determinant expression for \(D_S\), with its original source meaning retained.

\newpage

# 3. Simultaneous ES and RH action: all primary lengths and the mixed covariance

**Basis and status.** GF calculates the reducing enlargement generated by one sum action and its adjoint. The preceding ES–RH continuation identifies a different loss: the RH cyclic sum forgets a mixed occupation coordinate needed by the ES total. The result below combines these mechanisms. It concerns exact finite algebras with the supplied constructed metrics. The original canonical metric is reached only by the separate mixed minimum in Section 2.

## 3.1 A typed thickened ES/RH morphism

For each factor, suppose labelled roots \(\rho\) have multiplicities \(m_{i,\rho}\), and choose a bijection from those labels to auxiliary centres \(t_{i,\rho}\) of the same local lengths. There is a unique class \(\vartheta_i\bmod h_i\), equivalently a unique representative of degree \(<\deg h_i\), satisfying
\[
\vartheta_i(s)\equiv t_{i,\rho}+(s-\rho)\pmod{(s-\rho)^{m_{i,\rho}}}.
\tag{ER1}
\]
Thus the direct sum of maps \(t-t_{i,\rho}\mapsto s-\rho\) is an algebra isomorphism between the two labelled local quotient systems. Its inverse is the reverse translation on each local factor. The full Hermite remainder formula in GF(2) supplies its coefficients. The label matching is part of the chosen data, not a canonical identification. When the four \(t\)'s are the distinct literal ES roots \(p,x,y,z\), this is an ES/RH map on the squarefree branch; assigning higher multiplicities thickens that auxiliary ES root algebra explicitly. No assertion that ES denominators are zeta zeros or have zeta-zero multiplicities is made.

In an ordered tensor primary component \(\boldsymbol\rho\), write
\[
\kappa=\sum_i\rho_i,\qquad \theta=\sum_i t_{i,\rho_i},\qquad
D=\sum_i(m_{i,\rho_i}-1),\qquad R=\sum_i z_i.
\]
The two transported actions are exactly
\[
A_R=\kappa I+R,\qquad A_E=\theta I+R,
\qquad A_E-A_R=(\theta-\kappa)I. \tag{ER2}
\]
This includes the entire nilpotent total, not just its reduced eigenvalues. The physical multiplication unit is the same complete product \(U_1\otimes\cdots\otimes U_k\) as in GF; all actions and metrics are conjugated by that map on its actual image.

Let \(w_{\boldsymbol\rho}=\prod_i a_{i,\rho_i}>0\), and define
\[
W_{\kappa,\theta,D}
=\sum_{\boldsymbol\rho:\,\sum\rho_i=\kappa,\,\sum t_i=\theta,\,\sum(m_i-1)=D}
 w_{\boldsymbol\rho}.
\tag{ER3}
\]
Let \(1_{\kappa,\theta,D}\) denote the constant top vector in this grouped summand, and write
\[
e_{\kappa,\theta,D,j}=R^j1_{\kappa,\theta,D},\qquad 0\le j\le D.
\]
Actual equalities determine the grouping; centres are not assumed independent. At \(\kappa\) set
\[
S_j=\sum_{\theta,D}W_{\kappa,\theta,D}\binom Dj,
\qquad g_j=(j!)^2\eta^{2j}S_j.
\tag{ER4}
\]
These are the original GF cyclic metric coefficients after summing over \(\theta\), not a new counting convention.

## 3.2 Minimal common reducing space, with projectors

**Theorem.** The smallest space containing the original cyclic image and invariant under \(A_R,A_R^\dagger,A_E,A_E^\dagger\), in the supplied metric, is
\[
\boxed{
\mathscr W^{\mathrm{joint}}
=\bigoplus_{\kappa,\theta,D:\,W_{\kappa,\theta,D}>0}
\operatorname{span}\{R^j1_{\kappa,\theta,D}:0\le j\le D\}.
} \tag{ER5}
\]
Its dimension is \(\sum_{\kappa,\theta,D}(D+1)\), with each distinct triple counted once, not once per tensor word.

To prove generation, the original primary idempotents in \(A_R\) first select \(\kappa\); repeated roots require their full Hermite rather than simple Lagrange polynomials. Inside that component the semisimple normal operator \(A_E-A_R\) has scalar values \(\theta-\kappa\). The polynomial
\[
\prod_{\theta'\ne\theta}
\frac{A_E-A_R-(\theta'-\kappa)I}{\theta-\theta'}
\tag{ER6}
\]
selects \(\theta\). In that subspace, form the source's actual \(E=R/\eta\), \(F=R^\dagger/\eta\), \(H=[F,E]\), and Casimir \(\mathfrak C=H^2+2H+4EF\). Let \(\mathscr T\) be the direct sum of the generated cyclic top chains. Direct multiplication on each summand of \(\mathscr T\) gives \(\mathfrak C=D(D+2)I\). Thus, on \(\mathscr T\),
\[
\prod_{D'\ne D}
\frac{\mathfrak C-D'(D'+2)I}{D(D+2)-D'(D'+2)}
\tag{ER7}
\]
extracts its constant vector when applied to the selected cyclic constant. Applying powers of \(R\) generates the displayed chain. Conversely, each such top chain is invariant under both actions and adjoints, so nothing outside their direct sum is generated. This proves minimality.

The restriction to \(\mathscr T\) is essential and exact. The same interpolation polynomial need not be a projector on the ambient tensor algebra. For example, on
\[
V_1\oplus(V_1\otimes V_1),\qquad \eta=1,
\]
the tensor-block Casimir in the standard four-vector basis is
\[
\begin{pmatrix}
8&0&0&0\\
0&4&4&0\\
0&4&4&0\\
0&0&0&8
\end{pmatrix}.
\]
The lower singlet \(s=z_1-z_2\) has \(\mathfrak C s=0\), whereas the length-one interpolation polynomial \(P_1=(8I-\mathfrak C)/5\) sends \(s\) to \(8s/5\). Hence \(P_1^2s=64s/25\ne P_1s\). The inclusion \(\mathscr T\hookrightarrow\mathscr H_{\rm tensor}\) is the exact map relating the two domains: ER7 is an idempotent after restriction to \(\mathscr T\), and the displayed singlet proves why no ambient idempotence is asserted.

The coefficients in ER6 retain actual centre differences. On \(\mathscr T\), this is an exact finite projector on the given stratum, not a uniform bound through a collision of distinct \(\theta\)'s. If two \(\theta\)'s coincide, their corresponding triples merge. Equal \(D\) and \(\theta\) components that remain repeated are not separated by these four operators.

For a vector in the enlarged space, let \(u_{\kappa,\theta,D,j}\) be its coefficient on \(e_{\kappa,\theta,D,j}\), and let \(v_{\kappa,j}\) be the coefficient of its orthogonal return on the original cyclic vector \(R^j1_\kappa\). Whenever \(S_j>0\), the exact return is
\[
\boxed{v_{\kappa,j}
=\frac{\sum_{\theta,D}W_{\kappa,\theta,D}\binom Dj\,u_{\kappa,\theta,D,j}}{S_j}.}
\tag{ER8}
\]
Its kernel is the displayed full weighted relation at each level. The return is a linear projection, not an assertion that all original values or actions factor through it.

## 3.3 The cross covariance missing from a variance-only calculation

Use the Hermitian convention \(\langle x,y\rangle=x^*Gy\). The length \(D\) is real. At each level \(j\), define the probability on the actual grouped labels
\[
\pi_j(\theta,D)=W_{\kappa,\theta,D}\binom Dj/S_j.
\]
Let
\[
v_j=\mathbb E_{\pi_j}|\theta-\mathbb E_{\pi_j}\theta|^2,
\quad d_j=\operatorname{Var}_{\pi_j}(D),
\quad c_j=\mathbb E_{\pi_j}[(\theta-\mathbb E\theta)(D-\mathbb ED)].
\tag{ER9}
\]
The last quantity may be complex. Because \(D\) is real, it is also the standard Hermitian cross-covariance \(\mathbb E[(\theta-\mathbb E\theta)\overline{(D-\mathbb ED)}]\). It does not use \(\overline\theta\) because the defining leakage below involves the adjoint centre \(\overline\theta\), whose conjugate enters the first argument of the inner product. ER10 determines the stated leakage Gram; it is not by itself a specification of a full improper complex Gaussian law, which would also require a pseudo-covariance.

Let \(\beta\) be the original cyclic injection and \(\Pi\) its orthogonal projection. For the **forward** ES action,
\[
L_E=(I-\Pi)A_E\beta,
\qquad (L_E^\dagger L_E)_{jj}=v_j,
\]
and all off-diagonal entries vanish: the common nilpotent forward term \(R^{j+1}\) is already cyclic, while the residual semisimple term stays at degree \(j\).

For the adjoint action set
\[
Z_E=(I-\Pi)A_E^\dagger\beta.
\]
In the original, unnormalized cyclic basis \(R^j1_\kappa\), its complete raw Gram is tridiagonal:
\[
\boxed{
\begin{aligned}
(Z_E^*G_{\rm tensor}Z_E)_{jj}
 &=g_j\left[v_j+
 \eta^2\frac{S_{j-1}}{S_j}d_{j-1}\right],\\
(Z_E^*G_{\rm tensor}Z_E)_{j,j+1}
 &=g_j\eta^2(j+1)c_j,
\end{aligned}}
\tag{ER10}
\]
with the length-variance summand omitted at \(j=0\); the lower entry is the conjugate of the upper, and every other entry is zero.

To prove this, the degree-preserving residual is
\((\overline\theta-\mathbb E_{\pi_j}\overline\theta)R^j\).
The degree-lowering residual from input \(j+1\) is
\(\eta^2(j+1)(D-\mathbb E_{\pi_j}D)R^j\).
Their inner product is exactly \(g_j\eta^2(j+1)c_j\). Their separate squared norms give the two diagonal terms, with the lowering term at level \(j\) equal to GF(13). Different output degrees are orthogonal, leaving only the neighboring cross terms displayed above. In an orthonormal cyclic frame the off-diagonal entry is \(\eta\sqrt{S_j/S_{j+1}}c_j\). The code checks both the raw formula and the full direct tensor-metric calculation, including a complex \(c_j\ne0\).

For the supplied length example $(2,2,0)$, unit weights, and $\eta=1/3$, assign the real centres $(1,4,2)$. The unchanged cyclic Gram is $\operatorname{diag}(3,4/9,8/81)$, and ER10 gives the complete raw adjoint-leakage Gram
\[
\begin{pmatrix}
14/3&2/27&0\\
2/27&251/243&0\\
0&0&2/9
\end{pmatrix}.
\tag{ER10a}
\]
The off-diagonal $2/27$ is the new centre--length covariance; the source's original length-only raw term $8/243$ is still present in the middle diagonal entry. This is an exact small finite model, not a numerical native zeta packet.

Thus unequal primary lengths produce the source's variance, the different ES centres produce a second variance, and their common adjoint observation produces the **covariance**. Adding only the two diagonal variance matrices would omit a genuine mixed term.

## 3.4 Equal multiplicity: exact enlargement and nonzero ES leakage

Return to one common quartet of multiplicity \(m\), with \(0<\delta<1/2\), \(\gamma>2\), and the inherited programme condition that \(k\) is odd (in the application \(k\equiv1\pmod4\)). Let \(q=(k+1)^2(D+1)\). Fix a sorted positive integral ES witness at a hard prime \(p\equiv1\pmod{12}\):
\[
\frac4p=\frac1x+\frac1y+\frac1z,\qquad 0<x\le y\le z.
\]
Mark
\[
(t_1,t_2,t_3,t_4)=(p,x,y,z),\qquad
\rho_1=\tfrac12+\delta+i\gamma,\space
\rho_2=\tfrac12+\delta-i\gamma,
\]
\[
\rho_3=\tfrac12-\delta+i\gamma,\quad\rho_4=\tfrac12-\delta-i\gamma.
\]
In each occupation vector \((n_1,n_2,n_3,n_4)\), put
\[
u=n_1+n_2,\quad v=n_1+n_3,\quad j=n_1,\quad
\max(0,u+v-k)\le j\le\min(u,v).
\]
The nilpotent top degree is the common \(D=k(m-1)\). The ES centre is
\[
\theta=kt_4+(t_2-t_4)u+(t_3-t_4)v+\omega_{\rm ES} j,
\quad\omega_{\rm ES}=t_1-t_2-t_3+t_4.
\tag{ER11}
\]
Here \(\omega_{\rm ES}=(p-x)+(z-y)>0\): the smallest denominator satisfies \(x\le3p/4\), so \(p-x>0\), while sorting gives \(z-y\ge0\). Positivity of \(\omega_{\rm ES}\) therefore does not depend on the preceding distinct-root theorem. Thus different \(j\)'s in a fixed RH fibre have distinct ES centres. ER5 gives
\[
\boxed{\dim\mathscr W^{\rm joint}=(D+1)\binom{k+3}{3},\qquad
\dim\mathscr W^{\rm joint}-q=(D+1)\binom{k+1}{3}.} \tag{ER12}
\]
Adjoint closure for the RH action alone needed no enlargement at common \(D\). The extra dimension here is created by the second, ES action.

For the explicitly chosen unit root weights, the actual tensor-word weights on a fixed \((u,v)\) fibre are
\[
w_j=\frac{k!}{j!(u-j)!(v-j)!(k-u-v+j)!},
\quad \sum_jw_j=\binom ku\binom kv.
\]
For the variance formula below assume \(k\ge2\); the programme application has \(k\ge5\). The exact generating polynomial is
\(\binom ku\sum_j\binom uj\binom{k-u}{v-j}z^j\).
Differentiating once and twice at one, and applying the binomial generating identity, gives
\[
\mathbb E j=uv/k,\qquad
\operatorname{Var}j=\frac{uv(k-u)(k-v)}{k^2(k-1)}.
\]
The additional factor \(\binom D\ell\) at nilpotent level \(\ell\) is common across the fibre and cancels from its conditional weights, not from the original Gram. Therefore at **every** nilpotent level the forward ES leakage eigenvalue is
\[
\boxed{v_{uv}=\omega_{\rm ES}^2\frac{uv(k-u)(k-v)}{k^2(k-1)}.} \tag{ER13}
\]
It is nonzero exactly at the \((k-1)^2\) interior grid points. Hence
\[
\boxed{\operatorname{rank}L_E=(D+1)(k-1)^2,\qquad
\dim\ker L_E=4k(D+1).} \tag{ER14}
\]
For \(k=1\), every fibre is a singleton, so the variance and leakage rank are zero and \(\dim\ker L_E=4(D+1)\); no division by \(k-1\) is used.
This rank is of order \(q\), not a fixed or negligible rank. The finite-rank \(o(q)\) observation theorem from the native Gaussian source cannot be applied to this enlargement by merely replacing its kernel count.

![Left: every admissible occupation fibre \((u,v)\) for the programme-admissible value \(k=5\), with the exact interval of mixed counts \(j\); the sixteen interior cells are precisely the nonzero-leakage fibres. Right: the complete \((e,f)=(3,2)\) collision exponents from CP2--CP4, meeting at the balanced scale \(a=1\).](figures/family_joint_es_collision.pdf){width=96%}

The missing semisimple generator remains
\(W=n_1-n_2-n_3+n_4=k-2u-2v+4j\).
The pair of original sums plus this explicit mixed count recovers the occupations, while the Casimir recovers the distinct chain lengths. For common \(D\), the joint algebra on each \((u,v)\) is
\[
\prod_j\mathbb C[z]/z^{D+1},\qquad
A_R=\kappa_{uv}+z,\qquad A_E=\theta_{uvj}+z.
\tag{ER15}
\]
The product over \(j\) is separated by the explicit Lagrange polynomials in \(A_E-A_R\), and each full jet follows from powers of \(A_R-\kappa_{uv}\). This is an exact reconstruction rather than an assertion that one scalar observation recovers all amplitudes.

## 3.5 Source realization and its nonclaim

The same one-factor sections \(R_{i,\eta}\) in GF(26) can be tensored and restricted to \(\mathscr W^{\rm joint}\). This realizes the enlarged top-chain space inside the original ordered tensor source, still in total degree at most \(\sum_i(2d_i-1)\). Its metric has the complete factor \(\prod_i\tau_{i,\eta}\) multiplying the restriction of the original constructed tensor metric.

The resulting physical jet map has image \((\bigotimes_iU_i)\mathscr W^{\rm joint}\), which is generally larger than \((\bigotimes_iU_i)\beta(C_k)\). ER8 is a calculated projection back, not the original physical jet map on that larger space. To insert only the original section into the original cyclic source minimum, use Section 2. To admit the entire enlargement one must retain its larger value space or explicitly introduce the additional quotient and its full minimum. This is the typed morphism at the point where a silent identification would lose the new directions.

\newpage

# 4. Complete two-scale collision exponents

**Basis and status.** GF(49)–(52) supplies the two-centre Hermite matrix, its unweighted collision exponents, and a finite minimum over weighted minors. This section evaluates that minimum for every pair of lengths and every common power-law scale. The result is a complete two-regime formula, not a numerical fit.

## 4.1 Original divided-jet map and metric scale

Let \(e\ge f\ge1\), \(n=e+f\), and retain the constant-degree source
\[
\mathbb C[u]/(u^e(u-z)^f),\qquad z\ne0.
\]
In the unmodified power basis \(1,u,\ldots,u^{n-1}\), the divided-jet evaluation matrix is
\[
(E_z)_{(0,j),m}=\mathbf1_{j=m},\quad 0\le j<e,
\qquad
(E_z)_{(z,j),m}=\binom mjz^{m-j},\quad0\le j<f.
\tag{CP1}
\]
Entries with \(m<j\) are zero. Give the two jet blocks the scale factor \(\eta^j\), with
\[
\eta=|z|^a,\qquad a\ge0.
\]
Fixed positive weights, including the exact \((j!)^2\binom{e-1}j\) and \((j!)^2\binom{f-1}j\) from GF, act through row factors \(\sqrt{c_\alpha}\), one coefficient for each row label \(\alpha\), and do not alter the exponents. The input metric is fixed and uniformly equivalent to the standard power-coordinate metric. After extracting the displayed row powers, the residual target metric is required to remain uniformly positive and uniformly bounded. This qualification does not discard a degenerating metric or a vanishing physical unit.

Let \(\nu_1\le\cdots\le\nu_n\) mean
\(\sigma_j(E_{z,\eta})\asymp |z|^{\nu_j}\), with singular values in decreasing order. Constants may depend on the fixed lengths and the retained fixed metrics, but not on \(z\) sufficiently near zero. All formulas retain the phase of complex \(z\) through unitary row/column factors.

## 4.2 The complete phase diagram

For \(0\le a\le1\), the ordered list is
\[
\boxed{
0,a,2a,\ldots,(e-1)a;
\quad e-f+2j-1+a(f-j),\quad j=1,\ldots,f.
} \tag{CP2}
\]
The semicolon separates the \(e\) first-centre jet directions from the \(f\) additional directions; the entire list is nondecreasing.

For \(a\ge1\), the ordered list is
\[
\boxed{
(a+1)j,\ (a+1)j+1\quad(j=0,\ldots,f-1);
\qquad aj+f\quad(j=f,\ldots,e-1).
} \tag{CP3}
\]
Thus the only change of formula occurs at \(a=1\). At that value, both lists are exactly
\[
\boxed{0,1,2,\ldots,e+f-1.} \tag{CP4}
\]
The determinant order is, in both regimes,
\[
ef+\frac a2\{e(e-1)+f(f-1)\}. \tag{CP5}
\]
At \(a=0\), CP2 reduces to the source's \(e\) zero exponents and \(e-f+1,e-f+3,\ldots,e+f-1\). When \(a>0\), even some of the directions that were bounded in the unweighted map acquire scale; they must not be kept as unweighted zeros.

For example, \((e,f)=(3,2)\) gives
\[
\begin{cases}
(0,a,2a,2+a,4),&0\le a\le1,\\
(0,1,a+1,a+2,2a+2),&a\ge1.
\end{cases}
\]
For \((e,f)=(2,2)\), the two lists are \((0,a,a+1,3)\) and \((0,1,a+1,a+2)\). These are exact specialization cases of the all-length theorem.

## 4.3 Proof for \(0\le a\le1\)

Subtract from the second-centre jet of order \(j\) the first-centre jets of orders \(j,\ldots,e-1\), with their exact Taylor coefficients. After weighting, these row-operation coefficients are constants times \((z/\eta)^{m-j}\). Their magnitudes stay bounded because \(|z|/\eta=|z|^{1-a}\le1\); the inverse row operations are bounded too. The matrix becomes a block diagonal matrix with first block \(\operatorname{diag}(1,\eta,\ldots,\eta^{e-1})\) and second block
\[
C_{j,c}=\eta^j\binom{e+c}{j}z^{e+c-j},\qquad 0\le j,c<f.
\tag{CP6}
\]
A nonzero \(r\)-minor of the second block has order
\[
re+\sum_{c\in J}c+(a-1)\sum_{j\in I}j.
\]
For \(a\le1\), its minimum is attained by columns \(0,\ldots,r-1\) and rows \(f-r,\ldots,f-1\), giving
\[
\mu_r=r(e-f+r)+\frac{ar(2f-r-1)}2. \tag{CP7}
\]
The chosen minor does not vanish. Put \(L=f-r\). Its binomial coefficient determinant is
\[
\frac{\prod_{c=0}^{r-1}(e+c)_{\underline L}}
{\prod_{j=L}^{L+r-1}j!}
\prod_{0\le c<d<r}(d-c)>0.
\tag{CP8}
\]
To see it, factor \((e+c)_{\underline L}\) from each column, then use the falling-factorial polynomials of degrees \(0,\ldots,r-1\), all monic. Their evaluation determinant is the ordinary Vandermonde. Here \(e\ge f\) ensures every retained factor is positive.

The squared Hilbert–Schmidt norm of an exterior matrix is the sum of the squared absolute values of all its minors. The operator and Hilbert–Schmidt norms differ by bounded dimension constants. Thus \(\mu_r\) is the exponent of the product of the largest \(r\) singular values of \(C\). Taking consecutive differences gives
\(e-f+2r-1+a(f-r)\), proving CP2 after adjoining the first block. The first exponent in this second block is larger than \((e-1)a\) by \(e-f+1-a(e-f)\ge1\), so the displayed global ordering is valid.

## 4.4 Proof for \(a\ge1\)

Factor a row power \(|z|^{(a-1)j}\) from each derivative row, and a column power \(|z|^m\) from column \(m\). Removing only unitary phase factors leaves the constant confluent matrix for nodes \(0,1\). Every nonzero \(r\)-minor therefore has order
\[
\sum_{m\in J}m+(a-1)\sum_{j\in I}j.
\]
Because \(a-1\ge0\), choose the smallest \(r\) column orders and the smallest \(r\) derivative orders in the multiset
\(\{0,\ldots,e-1\}\cup\{0,\ldots,f-1\}\).
These rows can be chosen as consecutive initial jet segments at each centre. Their first-\(r\)-column determinant is the divided-jet confluent Vandermonde at \(0,1\), equal to one up to row ordering. It is nonzero. If \(j_r\) is the \(r\)-th element of that ordered derivative multiset, the consecutive determinantal orders give
\[
\nu_r=(r-1)+(a-1)j_r.
\]
The paired values \(j,j\) for \(j<f\), followed by \(j=f,\ldots,e-1\), give CP3. Summing either list proves CP5.

## 4.5 Every inverse exterior rank, and explicit balanced-ray constants

For any \(1\le r\le n\), the inverse exterior divergence exponent is exactly
\[
\boxed{\mathfrak e_r(a)=\sum_{j=n-r+1}^{n}\nu_j(a).} \tag{CP9}
\]
This is a sum of an explicitly evaluated list, not the unresolved minimum over minors from the input. For \(0\le a\le1\) it has the closed form
\[
\mathfrak e_r(a)=
\begin{cases}
r(e+f-r)+ar(r-1)/2,&r\le f,\\
ef+\dfrac a2\{f(f-1)+(r-f)(2e-r+f-1)\},&r>f.
\end{cases} \tag{CP10}
\]
At \(a=0\) this is \(p(e+f-p)\), \(p=\min(r,f)\), exactly the original input formula. At \(a=1\),
\[
\mathfrak e_r(1)=\frac{r(2n-r-1)}2.
\]

There are fully finite constants on this balanced ray. In the standard power-coordinate input metric and the specified jet weights \(c_\alpha>0\), let \(B\) be the constant Hermite evaluation at \(0,1\), with row \(\alpha\) multiplied by \(\sqrt{c_\alpha}\). Then
\[
E_{z,|z|}=U_\phi B\operatorname{diag}(1,z,\ldots,z^{n-1}),
\]
where \(U_\phi\) is a diagonal unitary phase matrix. Define
\[
\beta_B=\operatorname{tr}(B^*B),\qquad
\alpha_B=\frac{\det(B^*B)}{\beta_B^{n-1}}>0.
\]
The determinant is \(\prod c_j\), since the unweighted divided-jet confluent determinant is one at the chosen nodes. The elementary eigenvalue product bound gives \(\alpha_B I\preceq B^*B\preceq\beta_B I\), whence
\[
\boxed{
\beta_B^{-r/2}|z|^{-r(2n-r-1)/2}
\le\|\wedge^rE_{z,|z|}^{-1}\|
\le\alpha_B^{-r/2}|z|^{-r(2n-r-1)/2}.
} \tag{CP11}
\]
A different fixed original input form is inserted by its actual square-root coordinate map \(C\). At inverse exterior rank \(r\), the transported constants use \(\|\wedge^r C\|\) and \(\|\wedge^r C^{-1}\|\), or the coarser bounds \(\|C\|^r\) and \(\|C^{-1}\|^r\); first-exterior norms alone would not control CP11. A common physical section multiplier \(T(z)>0\) multiplies the target Gram and therefore multiplies this inverse-exterior norm by \(T(z)^{-r/2}\). In particular the GF section scalar \(\prod_i\tau_{i,\eta}\) cannot be omitted from a physical comparison. If it is asymptotic to \(c|z|^{-b}\), each singular exponent shifts by \(-b/2\); the relative condition number does not change.

The code independently computes all nonzero exact minors for the stated finite test cases and compares their orders with CP2–CP3 at rational values on both sides of one. The all-length, all-real-\(a\) claim follows from the proofs above. No floating singular-value fitting is used as proof.

\newpage

\newpage
# References and continuation boundary

*General-family control: Multiplicities, collisions, source sections, and all mixed minima*. (20 September 2026). Supplied programme continuation; no individual author is identified in the supplied text. The complete 979-line source is preserved as sources/GENERAL_FAMILY_INPUT.md, with its GF(1)–GF(60) labels unchanged.

Elsholtz, C., & Tao, T. (2013). Counting the number of solutions to the Erdős–Straus equation on unit fractions. *Journal of the Australian Mathematical Society*, 94(1), 50–105. [arXiv:1107.1010v6](https://arxiv.org/abs/1107.1010), §2. Read for the established Type I/Type II arithmetic background. The witness-to-jet construction in ER1–ER15 is proved here and is not attributed to this paper.

Higham, N. J. (13 October 2020). *What Is the Singular Value Decomposition?* [Author's exposition](https://nhigham.com/2020/10/13/what-is-the-singular-value-decomposition/). Read for SVD, norm, and singular-space conventions. The finite exterior inequalities used here are proved in MR4–MR6 and CP9–CP11.

National Institute of Standards and Technology. *NIST Digital Library of Mathematical Functions*, [§26.3, Lattice paths: Binomial coefficients](https://dlmf.nist.gov/26.3). Read for binomial definitions and generating-function conventions. The problem-specific multinomial, Vandermonde, and minor identities are proved at their uses.

Split-Zero research programme. (20 September 2026). *Gaussian spectral actions through the original arithmetic quotient*, NG1–NG27. Repository KokunoYumeto/zeta-function-research-reader.

Source version: \nolinkurl{b1f3e2e1879c40f411eb263dde171589cb5f9390}.

File: \path{workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/NATIVE_GAUSSIAN_TRANSFER.tex}.

Verified Git blob: \nolinkurl{6122e3b4f165df907a46ddcbc739f4dc159d65c6}.

NG20–NG21 are the exact theorem dependency for MR7–MR10, MR14, and JS15.

The Clankers. (20 September 2026). *Erdős–Straus Foundation*.

Repository base: \nolinkurl{5787b359a73edd62130caf76f573a40d607463c1}.

The existing equation, labelled witnesses, and earlier finite-algebra continuations supply the workbench context. No global occupancy statement is inherited from the repository name or from the ER thickening.

**Uncomputed native data.** The original source entries, complete cross Gram \(C_X\), value map \(F\), and spectral orientation relative to the observation kernel remain arithmetic inputs. JS6 gives their exact receiver and allocation but does not assign their values. The enlarged ER5 value space returns through the proved ER8 projection; admitting the whole enlargement requires its stated additional quotient. The small exact checkers do not replace these inputs or the NG20–NG21 theorem.
