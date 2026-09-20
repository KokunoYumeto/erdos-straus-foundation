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
