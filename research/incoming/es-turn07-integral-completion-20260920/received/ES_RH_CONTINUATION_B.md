The continuation now has **four completed derivation tracks**, including an arithmetic nonvanishing theorem for the ES receiving frame and a finite heat-action theorem that addresses the updated zeta repository’s stated next calculation.

[Download the cumulative research package](sandbox:/mnt/data/ES_RH_Continuation_20260920_B.zip)

[Typeset proofs](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/MANUSCRIPT.pdf) · [Editable manuscript](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/RESEARCH_CONTINUATION.md) · [Verification record](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/results/COMBINED_VERIFICATION_SUMMARY.json) · [Research handoff](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/CODEX_HANDOFF.md)

The package includes the preceding release unchanged. **All fourteen suites pass in ordinary and optimized Python:** 1,150 new exact checks plus 539 predecessor checks, giving **1,689 checks and twenty negative controls per mode**, with matching outputs and receipts. These are exact symbolic calculations and explicitly identified finite diagnostics, not a Lean build or numerical evaluation of hypothetical-zero native moments.

I incorporated the RH repository’s spectral-action edition at `4594c6d7528472bb2c7998ced3a7db5d7ac72bd5`, alongside the ES foundation at `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`. The [source ledger](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/SOURCE_LEDGER.md) records the precise source boundaries. In particular, the aggregate spectral inequality discussed below was already established upstream; the new work evaluates it on the original grid, sharpens its determinant consequences, and extends the finite polynomial calculation to genuine heat functions. Neither repository has been modified.

## 1. The extra ES receiving singularity is excluded for every integral witness in explicit prime classes

The previous continuation found a positive-real ES family crossing the extra receiving-frame divisor while its four roots remained distinct. That established why positivity and the reciprocal identity alone cannot exclude the divisor.

The arithmetic continuation now does exclude it on a substantial, explicitly described prime domain.

Retain an actual positive integral witness

$$
\frac4p=\frac1x+\frac1y+\frac1z,
\qquad p\equiv1\pmod{12},
$$

and the foundation’s literal-root quartic

$$
h(r)=-\frac{(r-p)(r-x)(r-y)(r-z)}{S},
\qquad S=p+x+y+z.
$$

Its coefficients are

$$
(A,B,C,D)=\left(
-\frac1S,\,
-\frac{p(x+y+z)+xy+xz+yz}{S},\,
\frac{5xyz}{S},\,
-\frac{pxyz}{S}
\right).
$$

This is the existing ES–Fable map, with its original scalar and roots retained.

For each simple root \(r_j\), write

$$
d_j=h'(r_j),\qquad \xi_j^2d_j=1,
$$

and retain the original odd receiving column

$$
o_j=\xi_j
\begin{pmatrix}
1\\
-id_j\\
Ad_j^2+2r_jd_j\\
i(7r_j^2d_j-13d_j^2)
\end{pmatrix}.
$$

The preceding determinant calculation gives

$$
\det O=\frac{4\chi}{A^3}F(A,B,C,D),
\qquad \chi\in\{1,-1\}.
$$

The relevant arithmetic numerator is

$$
N=S^6F\in\mathbb Z,
\qquad
|\det O|=\frac{4|N|}{S^3}.
$$

Its complete integer polynomial is retained as equation E1 in the delivered proof.

### The arithmetic theorem

**If**

$$
\boxed{
\left(\frac{-511}{p}\right)
=
\left(\frac{1241}{p}\right)
=
\left(\frac{-15}{p}\right)
=-1,
}
\tag{1}
$$

**then every positive integral ES witness at \(p\) has \(N\ne0\), and hence an invertible original odd receiving frame.**

This is quantified over all witnesses at such a prime. It is not inferred from a sample, and it does not assert that the prime has a witness.

The proof uses all possible \(p\)-divisibility patterns.

First, for \(p\equiv1\pmod{12}\), the four literal roots \(p,x,y,z\) are distinct. A denominator equal to \(p\) would give

$$
(3y-p)(3z-p)=p^2,
$$

whose positive factors have incompatible residues modulo \(3\). Two equal denominators lead to \(d\mid p^2\), with \(d=2a-p\), and each possible divisor produces a nonintegral remaining denominator when \(p\equiv1\pmod4\).

Clearing the reciprocal equation shows that at least one denominator is divisible by \(p\). All three cannot be, since their reciprocal sum would then be at most \(3/p\). This leaves exactly two cases.

**One divisible denominator.** Relabel so that \(x,y\) are units and \(z=pZ\). The valuation of \(z\) is exactly one. Direct reduction of the integer polynomial gives

$$
\boxed{
N\equiv
-x^2y^2(x-y)^2
(20x^2+33xy+20y^2)
\pmod p.
}
\tag{2}
$$

The last quadratic has discriminant

$$
33^2-4\cdot20^2=-511.
$$

The first condition in (1) therefore excludes its vanishing. If \(x\not\equiv y\pmod p\), this already gives \(v_p(N)=0\).

The diagonal \(x\equiv y\pmod p\) requires another calculation. Write \(y=x+pw\) and use the **exact** ES substitution

$$
z=\frac{pxy}{4xy-p(x+y)}.
$$

The denominator is a \(p\)-adic unit. Expanding the original integer expression gives

$$
\boxed{
N\equiv
p^2x^6\left(\frac{153}{16}-73w^2\right)
\pmod{p^3}.
}
\tag{3}
$$

The coefficient cannot vanish under the second condition in (1), because the square class of \(153/1168\) is

$$
1241=17\cdot73,
\qquad
153\cdot1168=12^2\cdot1241.
$$

Thus the diagonal case has \(v_p(N)=2\), rather than an undetermined higher-order zero.

**Two divisible denominators.** Their valuations must be equal, so write

$$
x=p^rX,\qquad y=p^rY,\qquad z=Z,
$$

with \(X,Y,Z\) units. For \(r=1\), the ES relation gives

$$
X+Y\equiv4XY\pmod p.
$$

Setting \(t=X+Y\), the determinant numerator satisfies

$$
\boxed{
\frac{N}{p^2}\equiv
-5Z^6(4t^2-7t+4)\pmod p.
}
\tag{4}
$$

This quadratic has discriminant \(-15\), so the third condition in (1) makes it nonzero.

For \(r\ge2\), the leading term is simpler:

$$
\boxed{
\frac{N}{p^2}\equiv-20Z^6\not\equiv0\pmod p.
}
\tag{5}
$$

This exhausts the witness types and proves the theorem.

An important detail is that the proof reduces the **cleared integer polynomial** \(N\). It never assumes that \(S\) is invertible modulo \(p\).

### The prime domain and the resulting inverse bound

Quadratic reciprocity converts (1), on \(p\equiv1\pmod{12}\), into

$$
\left(\frac p7\right)\left(\frac p{73}\right)=-1,\qquad
\left(\frac p{17}\right)\left(\frac p{73}\right)=-1,\qquad
\left(\frac p5\right)=-1.
$$

These describe **3,456 reduced residue classes modulo \(521{,}220\)**: one eighth of the reduced classes satisfying \(p\equiv1\pmod{12}\). The complete CRT list is in the package.

The exhaustive finite checks at

$$
p=(97,397,613,853,997)
$$

found respectively

$$
(8,29,44,34,48)
$$

sorted positive integral witnesses—**163 in total**—and verified the predicted valuation for every witness. These checks validate the implementation; the quantified theorem is supplied by (2)–(5).

Since \(N\) is a nonzero integer on this domain,

$$
|\det O|\ge\frac4{S^3}.
$$

Combining this with the existing explicit entry estimate \(\|O\|_2\le41S^3\) gives

$$
\boxed{
\|O^{-1}\|_2\le\frac{41^3}{4}S^{12}.
}
\tag{6}
$$

In the valuation-two cases, \(|N|\ge p^2\), improving the right side by \(p^{-2}\).

The norm in (6) is the specified coefficient norm. Passage to the original label and receiving metrics contributes their actual change-of-metric factors. The original conductor remains separate:

$$
(LO)^{-1}=O^{-1}L^{-1}.
$$

The arithmetic theorem removes the extra frame divisor on its prime domain; it does not alter the conductor’s coefficients, quotient or leading moment.

## 2. The native spectral allowance forces a sharp four-endpoint determinant cost

The updated source proves an aggregate bound using the full algebraic multiplicities, rather than only the most displaced eigenvalue. Its proof uses invariant generalized eigenspaces, so it does not require diagonalizability of the original companion.

Retain the actual native quotient metric

$$
G_L=
\left(
\sum_{n=0}^L\frac{b_nb_n^*}{\omega_n}
\right)^{-1},
\qquad L\ge q-1.
$$

Here the \(b_n\) are the original polynomial remainder classes and \(\omega_n\) their original squared native norms.

The source constructs

$$
A_L=M+\mathcal Q_L,
\qquad
M=\frac{M_S-kI/2}{i},
$$

where

$$
A_L^{\dagger_{G_L}}=A_L,
\qquad
\mathcal Q_L^2=0,
$$

and

$$
\epsilon_L^2=\|\mathcal Q_L\|_{G_L}^2
=
\frac{
(b_L^*G_Lb_L)(b_{L+1}^*G_Lb_{L+1})
}{\omega_L^2}.
\tag{7}
$$

### Full multiplicity gives the explicit cubic scale

For the original quartet grid,

$$
\kappa_{ab}
=\frac k2+(2a-k)\delta+i(2b-k)\gamma,
\qquad 0\le a,b\le k,
$$

retain

$$
e_k=1+k(m_0-1),\qquad q=e_k(k+1)^2.
$$

The aggregate source inequality is

$$
\epsilon_L\ge
\sum_{\Re\kappa>k/2}e_\kappa(2\Re\kappa-k).
$$

Its value on this grid is exactly

$$
\boxed{
\Theta_k
=
\frac{\delta e_k(k+1)^3}{2}
=
\frac{\delta q(k+1)}2.
}
\tag{8}
$$

For odd \(k\), this is the sum of the positive odd integers \(1,3,\ldots,k\), multiplied by the full remaining multiplicities.

This retains the cyclic multiplicity \(e_k\). Counting tensor words again would be a different—and incorrect—multiplicity.

### The exact determinant-ratio identity

Define

$$
d_L=\det G_L,\qquad
r_L=\frac{d_{L+1}}{d_L},\qquad
a_L^2=\frac{\omega_{L+1}}{\omega_L}.
$$

The rank-one inverse and determinant formulas give

$$
r_L=
\left(
1+\frac{b_{L+1}^*G_Lb_{L+1}}{\omega_{L+1}}
\right)^{-1}.
$$

Retaining the preceding leverage as well gives the stronger exact identity

$$
\boxed{
\epsilon_L^2
=
a_L^2
\frac{(1-r_{L-1})(1-r_L)}{r_L},
\qquad L\ge q.
}
\tag{9}
$$

Therefore

$$
(1-r_{L-1})(1-r_L)
\ge\frac{\Theta_k^2}{a_L^2}\,r_L.
$$

The relevant scalar optimization can be solved sharply. If

$$
0<x,y\le1,\qquad (1-x)(1-y)\ge cy,\qquad c\ge0,
$$

then

$$
\boxed{
xy\le
(\sqrt{1+c}-\sqrt c)^2
=
e^{-2\operatorname{arsinh}\sqrt c}.
}
\tag{10}
$$

Writing \(b=(\sqrt{1+c}-\sqrt c)^2\), the proof is the exact square completion

$$
b(1-x+c)-x(1-x)
=
\left(x-\frac{1+b}{2}\right)^2.
$$

Equality is attained at

$$
x=\frac{1+b}{2},\qquad y=\frac{2b}{1+b}.
$$

Thus this is the best bound available from that constraint alone.

At the programme’s four original cutoff indices,

$$
\mathcal R_q
=
\log\frac{d_{q-1}d_q}{d_{2q-1}d_{2q}},
$$

the full telescoping calculation gives

$$
\boxed{
\mathcal R_q
\ge
2\sum_{L=q}^{2q-1}
\operatorname{arsinh}\!\left(\frac{\Theta_k}{a_L}\right).
}
\tag{11}
$$

The outer determinant ratios occur once and the interior ratios twice. No endpoint has been shifted.

This is the **same-cyclic-quotient determinant contribution**, not automatically the entire previously assembled arithmetic action. The independent target minimum, original source Jacobians and matching signed budget terms still have to be propagated through their actual identities.

For a directly usable, albeit coarse, upper input, the original envelope

$$
\underline a_k(1+u^2)^{-M}\sigma(u)
\le m_k(u)\le\overline a_k\sigma(u)
$$

gives

$$
\boxed{
a_L^2\le
\frac{\overline a_k}{\underline a_k}
[1+4(L+1)^2]^M(L+1)(L+1/2).
}
\tag{12}
$$

The proof uses the exact Gamma recurrence, the monic minimum and Jensen’s inequality. It retains the source’s original constants; it does not assign them numerical values.

### The operator must be much more nonnormal than its eigenvalue size suggests

There is another consequence relevant to every subsequent heat bound.

Because \(\mathcal Q_L\) is rank one and square zero, its range vector is orthogonal to the Riesz vector of its defining covector. Thus

$$
\operatorname{Im}_{G_L}M
=\frac{M-M^{\dagger_{G_L}}}{2i}
$$

has eigenvalues

$$
+\epsilon_L/2,\quad-\epsilon_L/2,
$$

and zeros. It follows that

$$
\boxed{
\|M\|_{G_L}
\ge\frac{\epsilon_L}{2}
\ge\frac{\delta e_k(k+1)^3}{4}.
}
\tag{13}
$$

But its spectral radius is only

$$
\rho(M)=k\sqrt{\gamma^2+\delta^2}.
$$

Consequently

$$
\boxed{
\frac{\|M\|_{G_L}}{\rho(M)}
\ge
\frac{\delta e_k(k+1)^3}
{4k\sqrt{\gamma^2+\delta^2}}.
}
\tag{14}
$$

For a fixed simple quartet, the lower bound grows quadratically in \(k\). At higher multiplicity it grows faster through \(e_k\).

This is why replacing the native operator norm by the maximum eigenvalue modulus is not a harmless approximation. For simple roots, every eigenvector isomorphism has condition number at least the ratio in (14). The full determinant can remain nonzero while that conditioning cost grows.

## 3. The finite heat step is now completed with explicit remainders

The repository’s current result index explicitly identifies the next task as applying the finite trace coefficients to genuine heat actions with convergent remainders. The following addresses that finite-dimensional task; it does not introduce an unproved infinite spectral trace.

Fix the original positive metric \(G\), a selfadjoint \(A\), and

$$
Q=r\ell,\qquad \ell r=0,\qquad Q^2=0.
$$

Put

$$
T(t)=A-tQ.
$$

Two different heat functions must be retained:

$$
\mathcal H_\tau(t)
=\operatorname{tr}e^{-\tau T(t)^2},
$$

$$
\mathcal P_\tau(t)
=\operatorname{tr}e^{-\tau T(t)^\dagger T(t)},
\qquad \tau>0.
$$

The first may be complex. The second is the positive singular-value heat trace.

At the original endpoint \(T(1)=M=(M_S-kI/2)/i\), the first exponential is

$$
e^{+\tau(M_S-kI/2)^2},
$$

not \(e^{-\tau M_S^2}\). The centre and the factor \(i\) remain explicit.

### An entire outgoing-parameter expansion

Square-zero nilpotence gives the exact identity

$$
T(t)^2=A^2-tD,
\qquad D=AQ+QA.
$$

The heat trace is entire in \(t\), with

$$
\mathcal H_\tau(t)
=
\operatorname{tr}e^{-\tau A^2}
+\sum_{n\ge1}t^nh_n(\tau),
$$

where

$$
h_n(\tau)
=
\tau^n\int_{\Delta_n}
\operatorname{tr}
\left(
e^{-\tau s_0A^2}D
e^{-\tau s_1A^2}\cdots
D e^{-\tau s_nA^2}
\right)ds.
\tag{15}
$$

Here \(s_j\ge0\), \(\sum s_j=1\), and the simplex has volume \(1/n!\).

Since \(A\) is selfadjoint in the original metric,

$$
\|e^{-sA^2}\|_G\le1.
$$

Taking one occurrence of \(D\) in trace norm and the others in operator norm gives

$$
\boxed{
|h_n(\tau)|
\le
\frac{\tau^n\|D\|_{1,G}\|D\|_G^{n-1}}{n!}.
}
\tag{16}
$$

If \(x=\tau|t|\|D\|_G\), the truncation error after degree \(m\) satisfies

$$
\boxed{
|\mathcal E_m(t)|
\le
\tau|t|\|D\|_{1,G}
\frac{e^x x^m}{(m+1)!}.
}
\tag{17}
$$

The original rank-one norm supplies

$$
\|D\|_G,\ \|D\|_{1,G}
\le2\|A\|_G\|Q\|_G.
$$

There is **no extra factor equal to the packet dimension** in these bounds. The norms themselves may grow with packet degree; equation (14) shows why that dependence matters.

The same coefficients also extend the source’s cyclic polynomial formula:

$$
\boxed{
h_n(\tau)
=
\frac{(-1)^n}{n}
\sum_{\lambda_1,\ldots,\lambda_n}
F_\tau'[\lambda_1,\ldots,\lambda_n]
\prod_{j=1}^n\eta_{\lambda_j},
}
\tag{18}
$$

where

$$
F_\tau(z)=e^{-\tau z^2},
\qquad
\eta_\lambda=\ell P_\lambda r.
$$

All repeated nodes use confluent divided differences, and every complex \(\eta_\lambda\) is retained before taking any bound. The coefficient is \(1/n\), not an omitted or substituted factorial. Uniform convergence of the finite matrix Taylor series proves the entire-function extension.

### A heat-gap theorem with numerical constants

For any finite matrix \(T\) in the specified metric, define

$$
a_n
=
\operatorname{tr}((T^\dagger T)^n)
-\Re\operatorname{tr}(T^{2n}),
$$

so

$$
a_1
=
\frac12\|T-T^\dagger\|_{\mathrm{HS},G}^2.
$$

For every \(R\ge\|T\|_G\),

$$
\boxed{
|a_n|
\le n(2n-1)R^{2n-2}a_1.
}
\tag{19}
$$

The proof writes \(T=H+iK\) and interpolates \(T_s=H+isK\). The trace difference and its first derivative vanish at \(s=0\). Every second-derivative term contains two \(K\)'s, which are bounded in Hilbert–Schmidt norm, while the remaining factors are bounded by \(R\). Integrating the resulting bound yields (19), without diagonalizing \(T\).

For

$$
\Delta_\tau(T)
=
\Re\operatorname{tr}e^{-\tau T^2}
-\operatorname{tr}e^{-\tau T^\dagger T},
$$

the exact series and remainder become

$$
\Delta_\tau(T)
=
\sum_{n\ge1}\frac{(-1)^{n+1}\tau^na_n}{n!},
$$

$$
\boxed{
|\Delta_\tau(T)-\tau a_1|
\le
\tau a_1\bigl[(1+2x)e^x-1\bigr],
\qquad x=\tau R^2.
}
\tag{20}
$$

In particular, if \(\tau R^2\le1/8\), then

$$
\boxed{
\frac47\tau a_1
\le\Delta_\tau(T)
\le\frac{10}{7}\tau a_1.
}
\tag{21}
$$

The constants follow from \(e^{1/8}\le8/7\).

For the actual outgoing relation,

$$
a_1=t^2\epsilon_L^2.
$$

At \(t=1\), the original grid allowance therefore gives

$$
\boxed{
\Delta_\tau(M)
\ge\frac47\tau\Theta_k^2,
\qquad \tau R^2\le\frac18.
}
\tag{22}
$$

There is also an explicit finite stopping certificate. After \(m\) terms,

$$
\boxed{
\left|
\Delta_\tau(T)-
\sum_{n=1}^{m}\frac{(-1)^{n+1}\tau^na_n}{n!}
\right|
\le
\tau a_1
\frac{(2m+1)x^m}
{m!\,[1-3x/(m+1)]},
}
\tag{23}
$$

provided \(m+1>3x\).

For exact rational-complex inputs and rational \(\tau\), this produces a rigorous rational interval. The delivered `heat_certificate.py` implements it without sampling a matrix exponential.

### The time scale and metric cannot be suppressed

Equation (13) shows that the sufficient small-time condition can only hold at

$$
\tau\le\frac1{2\Theta_k^2}
$$

when \(\Theta_k>0\). This is a restriction on the applicability of (21), not a claim that the actual heat gap must become negative later.

Within that same domain, \(\epsilon_L\le2R\) also gives

$$
0\le\Delta_\tau(M)\le\frac57.
$$

Thus the norm-scaled regularized difference has a dimension-independent bound, while the original nonnormality cost remains explicit.

An all-time positivity claim would be false. For

$$
T=
\begin{pmatrix}1&-1\\1&1\end{pmatrix},
\quad
Q=
\begin{pmatrix}0&2\\0&0\end{pmatrix},
\quad
A=T+Q=
\begin{pmatrix}1&1\\1&1\end{pmatrix},
$$

one has \(A=A^*\), \(Q^2=0\), but

$$
\Delta_\tau(T)
=
2\cos(2\tau)-2e^{-2\tau},
$$

which is negative at \(\tau=\pi/2\).

Finally, an original conductor \(L:U\to W\) need not be an isometry for its two separately prescribed metrics. If

$$
T_W=LT_UL^{-1},
\qquad H=L^*G_WL,
$$

the exact positive-heat transport is

$$
\boxed{
\operatorname{tr}e^{-\tau T_W^{\dagger_{G_W}}T_W}
=
\operatorname{tr}e^{-\tau T_U^{\dagger_H}T_U}.
}
\tag{24}
$$

Replacing \(H\) by the different original source metric \(G_U\) requires another proved comparison. The holomorphic trace is conjugacy-invariant; the positive heat trace carries the metric.

## 4. A genuine ES witness can have no rational signed lift at a good prime

The fourth track tests whether the complex signed cover can be used as an arithmetic existence condition. It exposes a precise obstruction and gives the corresponding extension and twist.

Take the actual integral witness

$$
\frac4{13}
=
\frac14+\frac1{18}+\frac1{468}.
$$

Its literal normalized quartic reduces modulo \(61\) to

$$
\boxed{
h(r)=4r^4+r^3+35r^2+8r+28.
}
\tag{25}
$$

The four roots are

$$
(4,13,18,41),
$$

with derivatives

$$
(18,38,26,30).
$$

Every derivative is a quadratic nonresidue modulo \(61\). Therefore the original signed algebra

$$
\mathscr S_1
=
\mathbb F_{61}[r,\eta]/
(h(r),\eta^2-h'(r))
$$

has

$$
\boxed{\#\operatorname{Spec}\mathscr S_1(\mathbb F_{61})=0.}
\tag{26}
$$

This does not remove the ES witness. It obstructs an additional rational square-root choice in its signed fibre.

The correction is explicit. The element \(2\) is a nonresidue modulo \(61\), and

$$
(6^2,25^2,28^2,11^2)
=
2(18,38,26,30)\pmod{61}.
$$

Thus the nonsquare twist

$$
\eta^2=2h'(r)
$$

has eight rational points.

Over

$$
\mathbb F_{61^2}
=
\mathbb F_{61}[w]/(w^2-2),
$$

the eight **original** signed points are

$$
\eta_j=\pm\frac{b_j}{2}w,
\qquad
(b_j)=(6,25,28,11),
\qquad
\xi_j=\eta_j^{-1}.
\tag{27}
$$

The checker substitutes all eight full source-coordinate vectors into the original four-component Fable polynomial. It does not fit a substitute map.

### The exact descent diagram

For any distinct integral ES witness, put

$$
R=\mathbb Z[i,1/(2S\Delta)],
\qquad
\Delta=\prod_{j<k}(t_k-t_j).
$$

The common integral model is

$$
\mathscr S
=
R[r,\eta]/(h(r),\eta^2-h'(r)).
\tag{28}
$$

It has rank eight. An embedding \(R\to\mathbb C\) and a good reduction \(R\to\mathbb F_{61}\), with \(i\mapsto11\), produce two base changes of this same algebra.

There is no asserted homomorphism \(\mathbb C\to\mathbb F_{61}\), and no reduction of a transcendental Gamma receiving metric without an independently supplied integral model. The complex native receiver acts after the complex base change.

For a fully split squarefree quartic over any odd finite field,

$$
\#\mathscr S_a(\mathbb F_q)
=
4+\chi_q(a)\sum_j\chi_q(h'(r_j)).
$$

Since the derivative product is a square, the original and nonsquare-twisted point counts are each \(0,4,\) or \(8\), and

$$
\boxed{
\#\mathscr S_1(\mathbb F_q)
+
\#\mathscr S_a(\mathbb F_q)=8
\quad\text{for nonsquare }a.
}
\tag{29}
$$

This is a point-count identity, not an identification of the two covers.

For the explicit \(61\)-example, Frobenius sends \(w\) to \(-w\), exchanging the signs above all four roots. Consequently

$$
N_n=
\begin{cases}
0,&n\ \text{odd},\\
8,&n\ \text{even},
\end{cases}
$$

and the finite fibre’s point-count zeta function is

$$
\boxed{
Z_{\mathscr S_1}(T)=(1-T^2)^{-4}.
}
\tag{30}
$$

Its Frobenius permutation has eight unit-modulus eigenvalues, four \(+1\) and four \(-1\), but trace zero. Meanwhile the finite algebra has dimension eight, and the trace of multiplication by its unit is \(8\).

These are different traces on different objects. In particular, zero Frobenius trace does not make the algebra or its nondegenerate multiplication-trace pairing vanish. The corrected arithmetic statement is that the signed lift may require a quadratic extension—or a different twist—not that the underlying ES witness is absent.

## What this settles in the combined programme

The ES receiving-divisor question now has a proved integral nonvanishing domain, exact valuation strata, and an explicit inverse bound. Outside those prime classes, failure of a sufficient quadratic-character condition is **not** a singularity certificate; the remaining integral cases still require their actual arithmetic analysis.

On the RH side, the finite heat step is no longer merely a proposed extension of polynomial trace formulas. It has an entire series, explicit remainders, correct repeated-node coefficients, a rational stopping rule, and a metric-sensitive transport identity. The new paired determinant bound also retains the full grid multiplicity and all four original cutoffs.

The remaining closing estimates are still the original ones: native moment values and their growing-degree bounds, the phase-sensitive projected currents, the independent proper-source target minimum, and the complete signed budget. The new structural inequalities do not replace those quantities by a generic positive measure. Instead, they specify more sharply what any closing estimate must satisfy—and provide finite certificates into which the actual arithmetic inputs can be inserted.

### References

The Clankers. (2026, September 20). *The normalized Erdős–Straus quartic and its exact passage through the signed Fable cover to a fixed weighted conductor* [Research manuscript]. *Erdős–Straus Foundation*, commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`.

Connes, A., Consani, C., & Moscovici, H. (2025). *Zeta spectral triples* [Preprint]. arXiv:2511.22755. This supplies primary-literature context for the upstream rank-one spectral programme, not a claim of proved limiting RH convergence. ([arXiv][1])

Connes, A., & van Suijlekom, W. D. (2025). *Quadratic forms, real zeros and echoes of the spectral action* [Preprint]. arXiv:2511.23257.

Split-Zero programme. (2026a, September 20). *The native arithmetic secular determinant: Complete pole cancellation and the retained quotient metric* [Research manuscript]. *Zeta-function research reader*, commit `34f960f3af2a9f9eb9f87f3a937051e2473507ea`.

Split-Zero programme. (2026b, September 20). *Original arithmetic spectral action and metric curvature* [Research source edition]. *Zeta-function research reader*, commit `4594c6d7528472bb2c7998ced3a7db5d7ac72bd5`. Exact source paths, reading boundaries, and SA/MC theorem locators are retained in the [source ledger](sandbox:/mnt/data/ES_RH_Continuation_20260920_B/SOURCE_LEDGER.md).

[1]: https://arxiv.org/abs/2511.22755 "https://arxiv.org/abs/2511.22755"
