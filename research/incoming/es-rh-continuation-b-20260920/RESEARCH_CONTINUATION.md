# ES–RH continuation B

## Arithmetic nonsingularity, paired determinant bounds, finite heat actions, and arithmetic descent

**20 September 2026.** This continuation uses the delivered predecessor package and the repository's newer original-metric spectral-action edition. It contains four complete proof tracks and reproducible exact diagnostics. It does not claim that time spent substitutes for proof, or that finite algebra alone closes either global conjecture.

The first result removes the extra receiving-frame singularity for every positive integral ES witness at primes in 3456 explicit residue classes modulo 521220. Three quadratic-character conditions are sufficient. The proof distinguishes all possible divisibility patterns and computes the exceptional diagonal term rather than discarding it. At the five diagnostic primes there are exactly 163 sorted witnesses; their enumeration checks, rather than proves, the quantified theorem.

The second result evaluates the updated repository's existing full-multiplicity spectral allowance on the original quartet grid and carries it into a sharp two-step native determinant inequality. The four cutoff indices are retained. This contribution is not silently identified with the programme's whole action or independent target minimum.

The third result completes the source's stated finite-heat step: a genuinely convergent outgoing-parameter series, dimension-independent truncation remainders, and an explicit small-time comparison between holomorphic heat and singular-value heat in the original metric. The two heat functions remain different. A reusable rational certificate routine implements the finite remainder without numerically sampling an exponential.

The fourth result constructs an exact arithmetic descent test. The actual ES witness (13;4,18,468) has no signed rational lift over F_61, although its base quartic has four distinct roots there. All eight original lifts appear over F_61^2, and the nonsquare twist has eight over F_61. The common integral algebra and both base changes are stated, so no nonexistent map from a complex native metric into a finite field is assumed.

### Verification record

All **four new suites** pass in ordinary and optimized Python, with **1,121 exact checks and ten negative controls per mode** and identical output and receipt bytes. The **ten predecessor suites** also replay successfully: **539 checks and ten controls per mode**, for a combined **1,660 exact checks and twenty controls per mode**. The original predecessor ZIP is included unchanged. This is not a Lean build, independent human peer review, or evaluation of unknown native arithmetic moments.

### Source basis

The ES source is pinned to `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`. The newer RH spectral-action source is pinned to `4594c6d7528472bb2c7998ced3a7db5d7ac72bd5`; its preceding complete secular source was read at `34f960f3af2a9f9eb9f87f3a937051e2473507ea`. MC19–20 already contains the aggregate spectral theorem. It is an input here, not counted as a new theorem. The source ledger records exact paths, Git blob identities, reading scope and primary-literature records. Neither repository was modified.





\newpage

# Track I. Arithmetic exclusion of the receiving-frame divisor

**Status and scope.** This track extends the preceding positive-real frame calculation to a sufficient theorem for **all positive integral witnesses at specified primes**. It does not prove existence of an ES witness at every prime, and it does not claim that the sufficient character conditions are necessary. The inherited receiving polynomial is the one in the preceding delivered package, Track I; its normalized ES input is the foundation's EZ6--EZ13 (The Clankers, 2026). The proof below uses the actual integral reciprocal equation, not just its complex coefficient hypersurface.

## I.1 The literal integer to be tested

Retain
\[
\frac4p=\frac1x+\frac1y+\frac1z,\qquad
S=p+x+y+z,
\]
with positive integers and prime \(p\equiv1\pmod{12}\). Define
\[
e_2=p(x+y+z)+xy+xz+yz,\quad e_3=5xyz,\quad e_4=pxyz.
\]
The normalized literal-root quartic is
\[
h(r)=-S^{-1}(r-p)(r-x)(r-y)(r-z)
=Ar^4+r^3+Br^2+Cr+D,
\]
where \((A,B,C,D)=(-S^{-1},-e_2/S,e_3/S,-e_4/S)\).
For distinct roots \(r_j\), set \(d_j=h'(r_j)\), retain both signs of
\(\xi_j^2d_j=1\), and use the original odd columns
\[
o_j=\xi_j\bigl(1,-id_j,Ad_j^2+2r_jd_j,
 i(7r_j^2d_j-13d_j^2)\bigr)^T.
\]
The already established coefficient calculation gives
\[
\det O=4\chi F/A^3,\quad \chi\in\{1,-1\},
\]
\[
\begin{aligned}
F={}&20(3C-B^2)+A(87B^3-282BC-51D)\\
&+A^2(-28B^4+22B^2C+431C^2+204BD)\\
&+A^3(224B^2D-168BC^2-856CD)-448A^4D^2.
\end{aligned}
\]
Consequently the actual integer \(N=S^6F\) is
\[
\begin{aligned}
N={}&60S^5e_3-20S^4e_2^2-51S^4e_4-282S^3e_2e_3\\
&+87S^2e_2^3+204S^2e_2e_4+431S^2e_3^2
 +22Se_2^2e_3-856Se_3e_4\\
&-28e_2^4+224e_2^2e_4-168e_2e_3^2-448e_4^2.
\end{aligned}\tag{E1}
\]
We work with E1 before reducing modulo \(p\); **no inverse of \(S\) modulo \(p\) is assumed**.

## I.2 Exact divisibility alternatives

First, \(p,x,y,z\) are distinct. If \(x=p\), then
\((3y-p)(3z-p)=p^2\), with both factors positive. Each factor is a power of \(p\), hence is \(1\pmod3\), whereas each is \(-p\equiv2\pmod3\). This is impossible. If two denominators equal \(a\), put \(d=2a-p>0\). Clearing the equation gives
\(4dz=p(d+p)\), and thus \(d\mid p^2\). The possibilities \(d=1,p,p^2\) respectively give
\(z=p(p+1)/4,p/2,(p+1)/4\), none integral for \(p\equiv1\pmod4\).

The equation \(p(xy+xz+yz)=4xyz\) makes at least one denominator divisible by \(p\). All three cannot be divisible by \(p\), because their reciprocal sum would be at most \(3/p\). There are precisely two cases, after relabelling.

**Type I:** \(x,y\) are units modulo \(p\), and \(z=pZ\) with \(p\nmid Z\). Indeed, if \(v_p(z)=r\), the valuation of the left side is one and that of the right side is \(r\), forcing \(r=1\).

**Type II:** after relabelling, \(x=pX,y=pY,z=Z\), where \(X,Y,Z\) are units.  To prove equality of the two positive valuations, suppose they are \(a<b\). Then the two sides of the cleared equation have valuations \(a+1\) and \(a+b\), implying \(b=1\), contrary to \(1\le a<b\).  If their common valuation were \(r\ge2\), then the remaining denominator would obey
\[
\frac p4<z\le \frac{p^2}{4p-2}<\frac{p+1}{4}.
\]
For \(p\equiv1\pmod4\), this interval contains no integer.  Hence the common valuation is exactly one.

These arguments cover every positive integral witness; no exterior/middle selector is imposed.

## I.3 Type I, including its exceptional diagonal

At \(e_3=e_4=0\), E1 factors as
\[
N=-e_2^2(4e_2-S^2)(7e_2-20S^2).
\]
For Type I this gives
\[
N\equiv-x^2y^2(x-y)^2(20x^2+33xy+20y^2)\pmod p.
\tag{E2}
\]
The discriminant of the last quadratic is \(-511=-7\cdot73\). If
\(\left(\frac{-511}{p}\right)=-1\), that factor has no zero with \(xy\ne0\). Hence \(x\not\equiv y\pmod p\) gives \(v_p(N)=0\).

The diagonal case must not be discarded. Write \(y=x+pw\). The exact ES equation solves
\[
z=\frac{pxy}{4xy-p(x+y)}.
\]
Its denominator is a \(p\)-adic unit. Expanding the **integer polynomial E1 after this exact substitution** gives
\[
N\equiv p^2x^6\left(\frac{153}{16}-73w^2\right)\pmod {p^3}.
\tag{E3}
\]
An independently reproducible way to check every coefficient is to put
\(T_0=4xy-p(x+y)\) and clear \(T_0^6\). After replacing \(y\) by \(x+pw\), the constant and linear coefficients vanish, and the coefficient of \(p^2\) is
\[
-256x^{18}(1168w^2-153).
\]
Dividing by the constant unit \((4x^2)^6\) gives E3. Terms of higher degree in \(p\) cannot contribute to this coefficient.

The square class of \(153/1168\) is \(1241=17\cdot73\), since
\(153\cdot1168=12^2\cdot1241\). If
\(\left(\frac{1241}{p}\right)=-1\), the coefficient in E3 is nonzero. Thus \(v_p(N)=2\) in this case.

## I.4 Type II and a different quadratic obstruction

For the only possible witness valuation \(r=1\), substitution in E1 yields
\[
\frac{N}{p^2}\equiv
20Z^6\{15XY-(1+X+Y)^2\}\pmod p.
\]
The ES relation itself gives \(X+Y\equiv4XY\pmod p\). With \(t=X+Y\), this becomes
\[
\frac{N}{p^2}\equiv-5Z^6(4t^2-7t+4)\pmod p.
\tag{E4}
\]
The discriminant is \(-15\). If \(\left(\frac{-15}{p}\right)=-1\), E4 is nonzero, and \(v_p(N)=2\).

For reference, the same polynomial calculation on the formal, non-witness branch \(r\ge2\) would give \(S\equiv Z\), \(e_2/p\equiv Z\), \(v_p(e_3)\ge4\), \(v_p(e_4)\ge5\), and
\[
\frac{N}{p^2}\equiv-20Z^6\not\equiv0\pmod p.
\tag{E5}
\]
Equation E5 is retained as an exact polynomial specialization, but the preceding positivity argument proves that no positive integral witness enters that branch.  The exceptional primes dividing the displayed constants are excluded by the character conditions below.

## I.5 Universal conditional-on-witness theorem

**Theorem E.** Suppose \(p\equiv1\pmod{12}\) is prime and
\[
\boxed{
\left(\frac{-511}{p}\right)=
\left(\frac{1241}{p}\right)=
\left(\frac{-15}{p}\right)=-1.
}
\tag{E6}
\]
Then **every positive integral ES witness at this prime has \(N\ne0\)**. Its four literal roots and all eight signed inverse states are distinct, and its original odd receiving matrix is invertible. In Type I, \(v_p(N)=0\) or \(2\), according as the two unit denominators are distinct or equal modulo \(p\). In Type II, \(v_p(N)=2\).

**Proof.** The exact divisibility alternatives exhaust the witnesses. Equations E2--E5 give the stated finite valuations. They exclude \(N=0\), whose valuation would not be finite. Root distinctness was proved before the case split. The inherited determinant identity now proves invertibility. This is a theorem about all witnesses at primes satisfying E6, not an inference from their enumeration.

Quadratic reciprocity, with \(p\equiv1\pmod{12}\), writes the three conditions as
\[
\left(\frac p7\right)\left(\frac p{73}\right)=-1,
\quad
\left(\frac p{17}\right)\left(\frac p{73}\right)=-1,
\quad
\left(\frac p5\right)=-1.
\tag{E7}
\]
Thus they specify **3456 reduced residue classes modulo 521220**. To count them, fix the residue one modulo 12; there are two choices modulo 5, 72 choices modulo 73, three choices modulo 7 with the required sign, and eight modulo 17. Their product is 3456, out of \(4\cdot6\cdot16\cdot72=27648\) reduced classes with residue one modulo 12. The complete CRT list is delivered. For the narrower \(1\pmod{24}\) domain, choose the unique suitable lift of each class modulo 1042440. Primes 97, 397, 613, 853 and 997 satisfy E6. No density theorem or new ES verification range is claimed.

## I.6 Constants, exact original transport, and remaining arithmetic

The earlier entry bounds give \(\|O\|_2\le41S^3\), while
\(|\det O|=4|N|/S^3\). Therefore Theorem E makes the previously conditional bound unconditional for these witnesses:
\[
\boxed{\|O^{-1}\|_2\le\frac{41^3}{4}S^{12}.}
\tag{E8}
\]
In the valuation-two cases the stronger \(|N|\ge p^2\) gives an extra factor \(p^{-2}\) on the right. For original label and receiving metrics \(R,G>0\), multiply the coefficient bound by \(\|R^{1/2}\|_2\|G^{-1/2}\|_2\). These metrics have not been declared Euclidean.

For the unchanged invertible conductor \(L\), the exact relationship remains
\[
\ker(LO)=\ker O,\quad \det(LO)=\det L\det O,
\quad (LO)^{-1}=O^{-1}L^{-1}.
\]
The result removes the extra frame divisor on E6 without changing \(L\), its leading moment, its quotient, or its source and target norms.

The complement of E6 is not a singularity theorem: the sufficient conditions may fail even at entirely regular witnesses. Conversely, the positive-real singular curve in the predecessor shows why dropping integrality from this argument is invalid. The complete integral zero-locus outside E6 and universal ES occupancy remain separate questions.

## I.7 Verification boundary

`check_es_padic.py` verifies all polynomial expansions and CRT counts exactly. It also exhausts the sorted witnesses at the five displayed primes, finding 8, 29, 44, 34 and 48 respectively, for a total of **163**, and checks each predicted valuation.

Completeness of each finite enumeration is proved as follows. The smallest denominator satisfies \(p/4<a\le3p/4\). With \(R=4a-p\),
\((Rb-pa)(Rc-pa)=(pa)^2\); for \(b\le c\), the first positive integer factor is at most \(pa\). Enumerating all its divisors, imposing the two actual divisibilities and \(a\le b\le c\), recovers every sorted witness. These finite checks do not establish occupancy for all primes.


\newpage

# Track II. Full spectral multiplicity and sharp paired determinant returns

**Status and source distinction.** The aggregate spectral inequality is already proved in the updated repository, MC19--MC20 (Split-Zero programme, 2026b). It is used here, not presented as a new discovery. The extensions in this track are its exact original-grid evaluation, its expression through consecutive native determinant ratios, and the sharp two-ratio optimization with the original four cutoffs retained.

## II.1 The fixed original metric and outgoing relation

Retain one original packet and its actual even measure \(m=w_h^{*k}\), with its mass unchanged. Let \(Q_n\) be its real monic orthogonal polynomials, \(\omega_n=\int Q_n^2m>0\), and \(a_n^2=\omega_{n+1}/\omega_n\). Set
\[
c=k/2,\quad p_n(S)=i^nQ_n((S-c)/i),\quad b_n=[p_n]_\chi,
\]
where \(\chi\) is the full original cyclic annihilator of degree \(q\). In the same fixed remainder coordinates define
\[
K_L=\sum_{n=0}^L\frac{b_nb_n^*}{\omega_n},\qquad
G_L=K_L^{-1},\qquad L\ge q-1.
\tag{D1}
\]
The first \(q\) monic columns span the quotient, so these matrices are positive definite. They are the source's attained quotient metric, not a comparison weight.

NS6--NS9 and NS35--NS37 give
\[
M=(M_S-cI)/i,\qquad A_L=M+\mathcal Q_L,
\quad \mathcal Q_L=\frac{i}{\omega_L}b_{L+1}b_L^*G_L,
\]
\[
A_L^{\dagger_{G_L}}=A_L,\quad \mathcal Q_L^2=0,
\quad b_L^*G_Lb_{L+1}=0,
\]
\[
\epsilon_L^2=\|\mathcal Q_L\|_{G_L}^2
=\frac{(b_L^*G_Lb_L)(b_{L+1}^*G_Lb_{L+1})}{\omega_L^2}.
\tag{D2}
\]
The zero cross pairing is the result of the proved original parity, not a term discarded from a Gram determinant.

The Hermitian defect \(M_S+M_S^{\dagger_G}-2cI\) has eigenvalues \(+\epsilon_L,-\epsilon_L\) and zeros. The repository's aggregate theorem therefore yields
\[
\Theta:=\sum_{\Re\kappa>c}e_\kappa(2\Re\kappa-2c)
\le\epsilon_L.
\tag{D3}
\]
For completeness, let \(W\) be the invariant sum of the generalized eigenspaces on the indicated side, and let \(P_W\) be its original-metric orthogonal projection. Then \(\Theta\) is the trace of this projection against the Hermitian defect, and is at most the trace of its positive part, namely \(\epsilon_L\). Generalized eigenspaces retain algebraic multiplicities and require no diagonalizability of \(M_S\).

## II.2 Exact cost of the original quartet grid

For the stipulated quartet \(1/2\pm\delta\pm i\gamma\), retain the full common root multiplicity \(m_0\). The odd tensor degree has
\[
e_k=1+k(m_0-1),\quad q=e_k(k+1)^2,
\]
\[
\kappa_{ab}=k/2+(2a-k)\delta+i(2b-k)\gamma,
\qquad 0\le a,b\le k.
\]
The cyclic multiplicity is \(e_k\), not the number of tensor words that give the same sum. Summing D3 gives
\[
\begin{aligned}
\Theta_k
&=2\delta e_k(k+1)\sum_{a>k/2}(2a-k)\\
&=\boxed{\frac{\delta e_k(k+1)^3}{2}
=\frac{\delta q(k+1)}2}.
\end{aligned}\tag{D4}
\]
Indeed for \(k=2r+1\) the positive terms are \(1,3,\ldots,2r+1\), whose sum is \((r+1)^2\). No \(\gamma\)-dependent phase is removed from the actual operators; D4 only evaluates the real-part sum appearing in D3.

## II.3 The exact consecutive determinant identity

Write
\[
d_L=\det G_L,\qquad
r_L=\frac{d_{L+1}}{d_L},\qquad
\beta_L=\frac{b_{L+1}^*G_Lb_{L+1}}{\omega_{L+1}}.
\]
The rank-one update of \(K_L\), with the determinant lemma, gives
\[
\boxed{r_L=(1+\beta_L)^{-1}\in(0,1].}
\tag{D5}
\]
For \(L\ge q\), the same update one index earlier yields
\[
\frac{b_L^*G_Lb_L}{\omega_L}
=\frac{\beta_{L-1}}{1+\beta_{L-1}}=1-r_{L-1}.
\]
Substituting in D2 proves the full relation
\[
\boxed{
\epsilon_L^2
=a_L^2\frac{(1-r_{L-1})(1-r_L)}{r_L}.
}
\tag{D6}
\]
Every ratio uses the same packet, measure and remainder coordinates. The source mass cancels in this displayed relation only; it remains in each individual Gram.

Combining D3 with D6 gives
\[
(1-r_{L-1})(1-r_L)\ge c_Lr_L,
\qquad c_L=\Theta^2/a_L^2.
\tag{D7}
\]
This retains the preceding leverage rather than bounding it by one.

## II.4 Sharp two-ratio optimization

**Lemma D.** If \(0<x,y\le1\), \(c\ge0\), and \((1-x)(1-y)\ge cy\), then
\[
\boxed{xy\le(\sqrt{1+c}-\sqrt c)^2
=\exp[-2\operatorname{arsinh}\sqrt c].}
\tag{D8}
\]
For \(c>0\), put \(b=(\sqrt{1+c}-\sqrt c)^2\); then
\(c=(1-b)^2/(4b)\). The exact square completion
\[
b(1-x+c)-x(1-x)=\left(x-\frac{1+b}{2}\right)^2
\]
shows \(xy\le x(1-x)/(1-x+c)\le b\). Equality is attained at
\(x=(1+b)/2\), \(y=2b/(1+b)\). For \(c=0\), the claim is simply \(xy\le1\). Thus D8 is the best bound obtainable from that one scalar constraint, without a further original relation.

Applying the lemma to D7 gives
\[
\boxed{
-\log(r_{L-1}r_L)\ge
2\operatorname{arsinh}(\Theta/a_L).
}
\tag{D9}
\]

## II.5 The original four endpoint indices

Consider the **same-cyclic-quotient determinant contribution**
\[
\mathcal R_q
=\log\frac{d_{q-1}d_q}{d_{2q-1}d_{2q}}.
\]
It has exactly the telescoping expansion
\[
\mathcal R_q=-\sum_{L=q}^{2q-1}\log(r_{L-1}r_L).
\]
The outer ratios occur once and the interior ratios twice; no endpoint is shifted. Hence
\[
\boxed{
\mathcal R_q\ge
2\sum_{L=q}^{2q-1}\operatorname{arsinh}(\Theta/a_L).
}
\tag{D10}
\]
For the original quartet insert D4. This is not a claim that \(\mathcal R_q\) equals the programme's entire assembled Gamma/arithmetic action. Any additional source Jacobians, target minima, boundary terms and signed budget corrections still have to be included through their actual identities.

For example, **conditional** on a proved bound \(a_L\le Cq\) throughout the window, D10 implies
\[
\frac{\mathcal R_q}{q}\ge
2\operatorname{arsinh}\left(\frac{\delta(k+1)}{2C}\right).
\tag{D11}
\]
No such uniform \(C\) is asserted by this track.

There is nevertheless an explicit coarse input from the existing native envelope. If
\[
\underline a_k(1+u^2)^{-M}\sigma(u)\le m(u)
\le\overline a_k\sigma(u),\quad
\sigma(u)=|\Gamma(1/4+iu/2)|^2/(2\pi),
\]
then
\[
\boxed{
a_L^2\le\frac{\overline a_k}{\underline a_k}
[1+4(L+1)^2]^M(L+1)(L+1/2).
}
\tag{D12}
\]
To prove this, the exact Gamma recurrence bounds multiplication by \(u\) from degree \(L\) to degree \(L+1\) by \(2(L+1)\). For any degree-\(L\) polynomial, Jensen's inequality for \((1+x)^{-M}\) bounds its weighted Gamma norm below by \([1+4(L+1)^2]^{-M}\) times its Gamma norm. Minimizing over monic polynomials gives the lower bound for \(\omega_L\). Testing the native minimum at the monic Gamma polynomial gives \(\omega_{L+1}\le\overline a_k\omega^\Gamma_{L+1}\). Their exact Gamma ratio is \((L+1)(L+1/2)\), giving D12. The original constants and mass are unchanged.

## II.6 A forced nonnormality scale in the same native metric

There is a quantitative consequence for interpreting the heat scale. The original imaginary part of \(M\) satisfies
\[
\Im_GM=(M-M^\dagger)/(2i)=-\Im_G\mathcal Q_L.
\]
For a square-zero rank-one map, its range vector and the Riesz vector of its defining covector are orthogonal. In the orthonormal basis of their two-plane its matrix is \(\left(\begin{smallmatrix}0&\epsilon_L\\0&0\end{smallmatrix}\right)\), with zeros on the complement. Thus \(\Im_GM\) has eigenvalues \(\pm\epsilon_L/2\) and zeros. This is a proof in an explicitly isometric basis, not a declaration that the original coordinate vectors are orthonormal. Since \(\|\Im_GM\|_G\le\|M\|_G\),
\[
\boxed{\|M\|_{G_L}\ge\frac{\epsilon_L}{2}
\ge\frac{\delta e_k(k+1)^3}{4}.}
\tag{D13}
\]
The spectral radius of this original quartet companion is exactly
\(\rho(M)=k\sqrt{\gamma^2+\delta^2}\). Consequently
\[
\frac{\|M\|_{G_L}}{\rho(M)}
\ge\frac{\delta e_k(k+1)^3}{4k\sqrt{\gamma^2+\delta^2}}.
\]
For simple roots, any eigenvector isomorphism from standard label space to this native space has condition number at least this ratio, by \(M=V\operatorname{diag}(\lambda_j)V^{-1}\). At higher multiplicity no diagonalizer is asserted. The operator norm and the maximum eigenvalue modulus therefore cannot be interchanged in a heat remainder. This lower bound is compatible with the finite inverse-exterior identities; it quantifies the nonnormality those determinant identities do not by themselves control.

## II.7 Meaning and invariance

For any fixed invertible coordinate map \(J\), the transformations
\(M'=JMJ^{-1}\), \(G'_L=J^{-*}G_LJ^{-1}\) preserve D2 and all determinant ratios. In particular the source's full physical-jet injection, used only on its image with its transported metric, carries these identities exactly. An original conductor with a different target metric requires the corresponding full pullback; it is not declared unitary.

D3--D10 hold for any positive even measure and the stated symmetric quotient, not only for a zeta measure. They are necessary structural constraints. A closing upper estimate would have to use additional actual arithmetic information. For instance a proved \(\epsilon_{L(k)}/[e_k(k+1)^3]\to0\) would exclude a fixed \(\delta>0\), but that decay has not been established here.

`check_spectral_returns.py` verifies the complete formulas in exact positive compact-support models, including repeated nonreal roots, real roots and nonunitary coordinate changes. Those models are explicitly not values of unknown native arithmetic moments. It also verifies the quartet sum and the sharp scalar equality case symbolically.


\newpage

# Track III. Genuine finite heat actions with explicit remainders

**Status.** The updated source proves polynomial trace coefficients, the exact square-zero outgoing relation, and quadratic metric curvature. Its stated next step is a finite heat action with convergent remainders (Split-Zero programme, 2026b, SA1--43 and MC1--35). This track supplies that step. Every space is finite-dimensional. No infinite spectral trace, limiting determinant, Schwartz functional calculus on a nonnormal infinite operator, or RH endpoint is asserted.

## III.1 Original metric and the two different heat actions

Keep a specified positive Hermitian form \(G\), the adjoint
\(X^\dagger=G^{-1}X^*G\), a selfadjoint \(A^\dagger=A\), and
\[
Q=r\ell,\quad \ell r=0,\quad Q^2=0,\quad
\epsilon=\|Q\|_G=\|Q\|_{\mathrm{HS},G}.
\]
The original native instance is the outgoing correction in D2. For real \(t\), put \(T(t)=A-tQ\). The repository's exact quadratic identity is
\[
\operatorname{tr}(T^\dagger T)-\Re\operatorname{tr}(T^2)
=t^2\epsilon^2.
\tag{H1}
\]
For \(\tau>0\), define separately
\[
\begin{aligned}
\mathcal H_\tau(t)&=\operatorname{tr}e^{-\tau T(t)^2},\\
\mathcal P_\tau(t)&=\operatorname{tr}e^{-\tau T(t)^\dagger T(t)}.
\end{aligned}
\tag{H2}
\]
The first may be complex; the second is positive. Nilpotence does not identify them. At the original endpoint \(T(1)=M=(M_S-cI)/i\), the first exponential is
\(e^{+\tau(M_S-cI)^2}\), not \(e^{-\tau M_S^2}\). The second is
\(e^{-\tau(M_S-cI)^\dagger(M_S-cI)}\). These identities retain the original centre and the factor \(i\).

## III.2 Entire outgoing-parameter series and a dimension-independent remainder

Because \(Q^2=0\),
\[
T(t)^2=A^2-tD,\qquad D=AQ+QA.
\tag{H3}
\]
The rank of \(D\) is at most two, but it is not generally selfadjoint. Let \(\|X\|_{1,G}\) be its trace norm in the original metric. The finite heat trace has the entire expansion
\[
\mathcal H_\tau(t)=\operatorname{tr}e^{-\tau A^2}
+\sum_{n=1}^\infty t^nh_n(\tau),
\tag{H4}
\]
\[
h_n(\tau)=\tau^n\int_{\Delta_n}
\operatorname{tr}\left(e^{-\tau s_0A^2}D e^{-\tau s_1A^2}
\cdots D e^{-\tau s_nA^2}\right)ds.
\tag{H5}
\]
Here \(s_j\ge0\), \(\sum_{j=0}^ns_j=1\), and the simplex measure has volume \(1/n!\). In particular
\[
\boxed{|h_n(\tau)|\le
\frac{\tau^n\|D\|_{1,G}\|D\|_G^{n-1}}{n!}.}
\tag{H6}
\]

**Proof.** The operator Volterra equation is
\[
U(\tau)=e^{-\tau A^2}
+t\int_0^\tau e^{-(\tau-s)A^2}DU(s)\,ds.
\]
Successive substitution gives the ordered-simplex products in H5. The original-metric norm of every \(e^{-sA^2}\), \(s\ge0\), is at most one by selfadjointness. In the trace, bound one occurrence of \(D\) in trace norm and all other factors in operator norm. This proves H6, including the simplex volume. The analogous operator-norm bounds give a uniformly absolutely convergent series on every bounded complex \(t\)-disk; its substitution in the Volterra equation proves equality and entire dependence.

Set \(x=\tau|t|\|D\|_G\). Define the actual truncation error by
\[
\mathcal E_m(t)=\mathcal H_\tau(t)-\operatorname{tr}e^{-\tau A^2}
-\sum_{n=1}^m t^nh_n(\tau).
\]
Then
\[
\boxed{|\mathcal E_m(t)|\le\tau|t|\|D\|_{1,G}
\frac{e^x x^m}{(m+1)!}.}
\tag{H7}
\]
For \(D=0\) the remainder is zero and no division by its norm is used. For \(D\ne0\), sum H6 and use the scalar exponential tail. The original rank-one identity supplies the explicit estimates
\[
\|D\|_G\le2\|A\|_G\epsilon,
\qquad \|D\|_{1,G}\le2\|A\|_G\epsilon.
\tag{H8}
\]
There is no factor \(\dim E\) in H6--H8. Dependence of the actual norms on degree is, of course, still present.

For completeness, the positive heat action has
\[
T^\dagger T=A^2+U_t,
\quad U_t=-t(AQ+Q^\dagger A)+t^2Q^\dagger Q,
\]
\[
\|U_t\|_{1,G},\ \|U_t\|_G
\le2|t|\|A\|_G\epsilon+t^2\epsilon^2.
\tag{H9}
\]
A second Volterra expansion, now using \(-U_t\), gives the same form of convergent remainder at each real \(t\). It is not the same perturbation as H3.

## III.3 Exact extension of the source's cyclic coefficients

Let \(A=\sum_\lambda\lambda P_\lambda\) use the complete original-metric spectral projections, including eigenspaces of dimension greater than one. Put \(\eta_\lambda=\ell P_\lambda r\). For \(F_\tau(z)=e^{-\tau z^2}\), the coefficient in H4 is also
\[
\boxed{
h_n(\tau)=\frac{(-1)^n}{n}
\sum_{\lambda_1,\ldots,\lambda_n}
F_\tau'[\lambda_1,\ldots,\lambda_n]
\prod_{j=1}^n\eta_{\lambda_j}.
}
\tag{H10}
\]
All repeated nodes use their actual confluent divided differences. To prove the formula, first use the source's polynomial identity SA10, whose derivative factor is \((n-1)!\), so its coefficient factor is \(1/n\). For rank one, each cyclic trace product equals the product of the \(\eta\)'s. Approximate \(F_\tau\) by its Taylor polynomials uniformly on a disk containing the spectra of \(A-tQ\) for a bounded \(t\)-disk. The finite matrix series and every fixed \(t\)-derivative converge uniformly. Divided differences on the finite node set converge as well, including derivative-defined repeated nodes. The polynomial identities therefore pass to the entire function. H7 supplies a separate explicit bound for summing these coefficients in \(t\).

The proof preserves the phases of all \(\eta_\lambda\). No absolute values are inserted into H10 itself. Bounds are taken only after the exact coefficient is formed. The two formulas H5 and H10 compute the same entire Taylor series.

## III.4 A quantitative heat-gap theorem for any finite matrix

This part does not require rank one. For a finite matrix \(T\) in the original metric, define
\[
a_n=\operatorname{tr}((T^\dagger T)^n)-\Re\operatorname{tr}(T^{2n}),
\quad a_1=\tfrac12\|T-T^\dagger\|_{\mathrm{HS},G}^2\ge0.
\]
Let \(R\ge\|T\|_G\). Then for every integer \(n\ge1\),
\[
\boxed{|a_n|\le n(2n-1)R^{2n-2}a_1.}
\tag{H11}
\]

**Proof.** Write \(T=H+iK\) with \(H,K\) selfadjoint and put
\(T_s=H+isK\), \(0\le s\le1\). Since
\(T_s=(1+s)T/2+(1-s)T^\dagger/2\), its norm is at most \(R\). Set
\[
f_n(s)=\operatorname{tr}((T_s^\dagger T_s)^n)
-\Re\operatorname{tr}(T_s^{2n}).
\]
Both terms agree at zero, and their first derivatives there have zero difference. The first trace is even in \(s\), since \(T_{-s}=T_s^\dagger\) and the two cyclic products have the same trace. The real part of the second is also even. Each second derivative is a sum of \(2n(2n-1)\) ordered choices of two differentiated factors. Each trace term contains two factors \(K\), with all remaining factors bounded by \(R\). Cyclicity and Hilbert--Schmidt Cauchy--Schwarz bound its modulus by
\(\|K\|_{\mathrm{HS},G}^2R^{2n-2}\). There are two traces, so
\[
|f_n''(s)|\le4n(2n-1)\|K\|_{\mathrm{HS},G}^2R^{2n-2}.
\]
Integrating against \(1-s\) gives H11 because \(a_1=2\|K\|_{\mathrm{HS},G}^2\). All uses of a Euclidean basis, if made, are through the explicit isometry \(G^{1/2}\); the original metric is not changed.

Define the real finite heat gap
\[
\Delta_\tau(T)=\Re\operatorname{tr}e^{-\tau T^2}
-\operatorname{tr}e^{-\tau T^\dagger T}.
\]
Absolute convergence and H11 give
\[
\Delta_\tau(T)=\sum_{n=1}^\infty
\frac{(-1)^{n+1}\tau^na_n}{n!},
\]
\[
\boxed{
|\Delta_\tau(T)-\tau a_1|
\le\tau a_1\{(1+2x)e^x-1\},\quad x=\tau R^2.
}
\tag{H12}
\]
The scalar sum is exact: after putting \(m=n-1\), it is
\(\sum_{m\ge1}(2m+1)x^m/m!\).

In particular, \(x\le1/8\) gives \(e^x\le(1-x)^{-1}\le8/7\), and hence
\[
\boxed{
\frac47\tau a_1\le\Delta_\tau(T)
\le\frac{10}{7}\tau a_1,
\qquad \tau R^2\le\frac18.
}
\tag{H13}
\]
For the original \(T(t)=A-tQ\), H1 gives \(a_1=t^2\epsilon^2\). At the actual quotient endpoint \(T=M\), D3--D4 therefore give
\[
\boxed{
\Delta_\tau(M)\ge\frac47\tau\Theta_k^2,
\qquad \tau R^2\le\frac18.
}
\tag{H14}
\]
This is an exact finite heat comparison, not a proof of decay of \(\epsilon\) or a sign for a different projected arithmetic current. D13 also shows that the sufficient condition \(\tau R^2\le1/8\), with \(R\ge\|M\|_G\), can only hold at \(\tau\le1/(2\Theta_k^2)\) when \(\Theta_k>0\). This restriction concerns the applicability of H13, not a necessary condition for positivity of the actual heat gap. The much smaller eigenvalue radius is not a substitute for the original operator norm. Since \(\epsilon_L\le2R\), H13 also gives \(0\le\Delta_\tau(M)\le5/7\) on this same small-time domain.

## III.5 A rational finite stopping certificate

Let \(\Delta_{\tau,m}(T)=\sum_{n=1}^m(-1)^{n+1}\tau^na_n/n!\).
After \(m\ge1\) terms, H11 gives
\[
\boxed{\left|\Delta_\tau(T)-\Delta_{\tau,m}(T)\right|
\le\tau a_1\frac{(2m+1)x^m}{m!\{1-3x/(m+1)\}}.}
\tag{H15}
\]
The condition is \(m+1>3x\).
Indeed the positive majorant terms are
\(b_n=(2n-1)x^{n-1}/(n-1)!\). Their ratio satisfies
\(b_{n+1}/b_n=x(2n+1)/(n(2n-1))\le3x/n\); summing the geometric majorant after \(n=m\) proves H15. Thus rational matrix entries, a rational upper bound for \(R^2\), and rational \(\tau\) give an entirely rational outward interval. A convenient available upper bound is \(R^2\le\operatorname{tr}(T^\dagger T)\), though it may be coarse.

The small-time restriction is essential. Take
\[
T=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\quad
Q=\begin{pmatrix}0&2\\0&0\end{pmatrix},\quad
A=T+Q=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Then \(A=A^*\), \(Q^2=0\), but
\(\Delta_\tau(T)=2\cos(2\tau)-2e^{-2\tau}\), which is negative at \(\tau=\pi/2\). No all-time positivity statement follows from H13.

## III.6 The exact physical maps and the verification scope

For a fixed coordinate isomorphism \(J\), transform \(T'=JTJ^{-1}\) and
\(G'=J^{-*}GJ^{-1}\). Both heat traces and all constants in the appropriate original-metric norms are preserved. This includes the source's physical-jet injection onto its image with its transported metric.

An original conductor \(L:U\to W\) need not be an isometry for its two separately given metrics. If \(T_W=LT_UL^{-1}\) and \(H=L^*G_WL\), the exact relation is instead
\[
\begin{aligned}
\operatorname{tr}e^{-\tau T_W^{\dagger_{G_W}}T_W}
&=\operatorname{tr}e^{-\tau T_U^{\dagger_H}T_U}.
\end{aligned}
\tag{H16}
\]
Replacing \(H\) by the different original \(G_U\) requires an additional metric estimate. The holomorphic trace is conjugacy-invariant without this qualification. Finally the repository's selfadjoint dilation has
\(\operatorname{tr}e^{-\tau\mathcal D_T^2}=2\mathcal P_\tau(T)\); it is not the same as the holomorphic heat trace.

`check_heat.py` verifies repeated-node cyclic coefficients, the affine square identity, original nonidentity-metric conjugacies, the scalar majorant, and rational heat-gap intervals in exact diagnostic matrices. It uses 12 terms for its explicit intervals and includes false-inference controls. These are not native arithmetic moment evaluations. The original unknown moments and their outward tolerances must still be inserted before using these finite certificates on a hypothetical zero packet.


\newpage

# Track IV. Arithmetic descent of the signed cover and an exact twist correction

**Status.** This is a concrete arithmetic specialization of the original ES/Fable algebra, not a new conjecture about finite-field spectra. It shows that even an actual integral ES witness need not have a rational signed lift at a good residue prime. The missing signs are recovered by an explicit quadratic extension or a different quadratic twist. The analytic receiving metric is not silently reduced modulo a prime.

## IV.1 A common integral model, not a map from complex numbers to a finite field

For a distinct integral ES witness with literal roots \(t_1=p,t_2=x,t_3=y,t_4=z\), put
\[
S=\sum_jt_j,\quad \Delta=\prod_{j<k}(t_k-t_j),
\quad R=\mathbb Z[i,1/(2S\Delta)].
\]
The original normalized quartic lies in \(R[r]\), with invertible leading coefficient. Its signed algebra is
\[
\mathscr S=R[r,\eta]/(h(r),\eta^2-h'(r)).
\tag{F1}
\]
It is finite free of rank eight; the root algebra is rank four and the second relation is monic of degree two. The derivative is a unit because the discriminant is inverted. The relation therefore agrees with the original inverse chart by \(\xi=\eta^{-1}\).

An embedding \(R\to\mathbb C\) and a good reduction \(R\to\mathbb F_q\) give two actual base changes of F1. They do **not** give a field homomorphism \(\mathbb C\to\mathbb F_q\). A native receiving map with Gamma or arithmetic coefficients acts on the complex base change; no integral model of those extra coefficients is assumed. Thus this is a common algebraic source for two fibres, not an identification of their physical metrics.

## IV.2 All rational signed points and both twists

Suppose the reduced quartic has four distinct roots in \(\mathbb F_q\), where \(q\) is odd. Let \(d_j=h'(t_j)\ne0\), and write \(\chi_q\) for its quadratic character. For any \(a\in\mathbb F_q^*\), define the explicitly different twist
\[
\mathscr S_a=\mathbb F_q[r,\eta]/(h(r),\eta^2-a h'(r)).
\]
Counting the two square roots or their absence gives
\[
\boxed{\#\operatorname{Spec}\mathscr S_a(\mathbb F_q)
=4+\chi_q(a)\sum_{j=1}^4\chi_q(d_j).}
\tag{F2}
\]
The product of the derivatives is \(A^4\Delta^2\), a square. Consequently the number of nonsquare derivatives is even, and the count for either twist is 0, 4 or 8. For a nonsquare \(a\),
\[
\boxed{\#\mathscr S_1(\mathbb F_q)+\#\mathscr S_a(\mathbb F_q)=8.}
\tag{F3}
\]
This is a point-count identity, not an identification of the two covers. Their disjoint union has sixteen geometric points. After adjoining a square root \(b^2=a\), the map \(\eta_a=b\eta_1\) is an explicit isomorphism of the two base-changed covers.

## IV.3 An actual integral witness with no rational signed lift

The witness
\[
(p;x,y,z)=(13;4,18,468)
\]
satisfies \(4/13=1/4+1/18+1/468\). Reduce at \(q=61\), taking \(i\mapsto11\), for which \(11^2=-1\pmod{61}\). The complete normalized quartic is
\[
h(r)=4r^4+r^3+35r^2+8r+28\quad\text{in }\mathbb F_{61}[r].
\tag{F4}
\]
Its roots and corresponding derivatives, in increasing residue order, are
\[
(t_j)=(4,13,18,41),\qquad(d_j)=(18,38,26,30).
\tag{F5}
\]
All four derivatives are quadratic nonresidues. Therefore
\[
\boxed{\#\mathscr S_1(\mathbb F_{61})=0.}
\tag{F6}
\]
This does not remove the original ES witness. It only obstructs the additional choice of a rational normalized square root in this particular fibre.

The element 2 is a nonresidue modulo 61, while
\[
(6^2,25^2,28^2,11^2)=2(18,38,26,30)\pmod{61}.
\]
Thus the twist \(\eta^2=2h'(r)\) has eight rational points. In the extension
\(\mathbb F_{61^2}=\mathbb F_{61}[w]/(w^2-2)\), the eight original points have
\[
\eta_j=\pm(b_j/2)w,\quad(b_j)=(6,25,28,11),\quad \xi_j=\eta_j^{-1}.
\tag{F7}
\]
The complete original source coordinates follow without selecting another polynomial:
\[
\begin{aligned}
a_j&=\eta_j^{-1},\qquad y_j=-t_j-i\eta_j,\\
z_j&=A\eta_j^3+2t_j\eta_j+3i\eta_j^2,\\
w_j&=7it_j^2\eta_j+(B-17t_j+At_j^2)\eta_j^2
-13i\eta_j^3-2A\eta_j^4,\\
q_j&=(a_j,y_j,z_j,w_j).
\end{aligned}
\tag{F8}
\]
The exact checker evaluates the original four-component Fable polynomial at all eight F8 points and obtains F4's target coefficients. It does not substitute a fitted map.

## IV.4 Frobenius, trace and the surviving algebra

Since \(w^{61}=-w\), Frobenius exchanges the two signs above every root. Its permutation is four disjoint transpositions. Thus the point counts over extensions are
\[
N_n=\begin{cases}0&n\text{ odd},\\8&n\text{ even},\end{cases}
\]
and the local point-count zeta function is
\[
\boxed{Z_{\mathscr S_1}(T)
=\exp\left(\sum_{n\ge1}N_nT^n/n\right)=(1-T^2)^{-4}.}
\tag{F9}
\]
This is the zeta function of this finite fibre, not the Riemann zeta function. Its Frobenius characteristic polynomial is \((z^2-1)^4\). All eight complex permutation eigenvalues have modulus one, but their trace is zero. The finite algebra itself is the product of four quadratic fields over \(\mathbb F_{61}\), of dimension eight, not the zero algebra.

There are also two different traces here. The trace of multiplication by the algebra unit is \(\operatorname{Tr}_{\mathscr S/\mathbb F_{61}}(1)=8\), while the trace of Frobenius on the eight-point permutation space is zero. In the predecessor's residue identity the multiplier \(2\eta^3\) is a unit on this good-reduction fibre, so the multiplication trace pairing is nondegenerate. Zero Frobenius trace does not make that pairing or the algebra vanish.

The corrected arithmetic conclusion is explicit: the original complex signed cover may require a field extension after good reduction; alternatively the nonsquare twist has the complementary rational-point count. Any proposed ES inference requiring a rational original signed lift at every good prime is disproved by F4--F8. A native analytic metric or a purity statement alone supplies neither that rational lift nor the universal ES occupancy theorem.

`check_finite_field.py` verifies the literal reciprocal identity, all coefficients and derivative square classes, all eight source points in the explicit quadratic field, their Frobenius action, and the formal point-count zeta identity. No transcendental receiving coefficient is given an invented finite-field image.

\newpage

# Closure conditions and continuing research

The arithmetic theorem is universal over witnesses at its specified primes. It is not a witness-production theorem. The central ES occupancy question remains, as does the integral receiving divisor outside the sufficient character classes. The next arithmetic calculation should keep the same integer N and refine the residual cases where one or more quadratic obstructions becomes a square; a failed sufficient symbol test is not itself a singularity.

For RH, the paired return is a necessary inequality for the original quotient and native metric. The aggregate spectral charge and the recurrence coefficients enter on different sides of a fully explicit formula. A proof that closes the programme still needs additional native arithmetic information, not a generic positive-measure argument that would apply equally to the diagnostic nonreal quotients.

The finite heat step now has explicit convergent remainders and certified small-time signs for its stated difference. It does not evaluate the earlier, distinct phase-sensitive projected current. The source's moment intervals, full quotient kernels, moving orthogonal-polynomial columns and two minimum residuals must be carried into any numerical or asymptotic application. The reusable routine takes exact inputs; a numerical midpoint is not automatically the exact native operator.

The finite-field example supplies a precise obstruction to one possible arithmetic inference and an explicit replacement via a quadratic extension or twist. It neither identifies a denominator with a zeta zero nor imports finite-field purity into the original infinite arithmetic action. The local zeta function in F9 belongs to a finite fibre.

# References

The Clankers. (2026, September 20). *The normalized Erdős–Straus quartic and its exact passage through the signed Fable cover to a fixed weighted conductor* [Research manuscript]. Erdős–Straus Foundation, commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`. Exact file and theorem locators: SOURCE_LEDGER.md, ES.

Connes, A., Consani, C., & Moscovici, H. (2025). *Zeta spectral triples* [Preprint]. arXiv:2511.22755. https://arxiv.org/abs/2511.22755

Connes, A., & van Suijlekom, W. D. (2025). *Quadratic forms, real zeros and echoes of the spectral action* [Preprint]. arXiv:2511.23257. https://arxiv.org/abs/2511.23257

*Combined ES–Fable–RH research continuation*. (2026, September 20). [Predecessor research package supplied in the conversation]. ES_RH_Multi_20260920.zip. Preserved unchanged under prior/; original source identities and verification receipts remain inside it.

Split-Zero programme. (2026a, September 20). *The native arithmetic secular determinant: Complete pole cancellation and the retained quotient metric* [Research manuscript]. Zeta-function research reader, commit `34f960f3af2a9f9eb9f87f3a937051e2473507ea`. NS1–NS37; exact pinned path in SOURCE_LEDGER.md.

Split-Zero programme. (2026b, September 20). *Original arithmetic spectral action and metric curvature* [Research source edition]. Zeta-function research reader, commit \path{4594c6d7528472bb2c7998ced3a7db5d7ac72bd5}. \path{NATIVE_SPECTRAL_ACTION.tex} and \path{RANK_ONE_METRIC_CURVATURE.tex}; point-of-use SA/MC locators and reading boundary in \path{SOURCE_LEDGER.md}.

The external papers provide primary-literature context. The exact finite receiving formulas used from the programme, and every new derivation asserted here, are specified separately. No claim of global historical priority is made for classical determinant, quadratic-reciprocity, spectral, or heat-expansion methods.
