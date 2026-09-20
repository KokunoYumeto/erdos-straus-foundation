The continuation reaches **genuine Gaussian spectral actions in the original arithmetic metrics**, rather than stopping at polynomial trace identities. It also gives a substantially larger unconditional positivity theorem for the programme’s full Weil form.

The principal results are:

$$
\boxed{
\lim_{k\to\infty}\frac1q\,
\mathcal R\operatorname{Tr}
\left[
\frac{M_{B,N}^{\dagger}M_{B,N}}{q^2}
\exp\!\left(
-\frac{M_{B,N}^{\dagger}M_{B,N}}{1024q^2}
\right)
\right]
<-\frac{13}{2400}.
}
\tag{1}
$$

Here \(M_{B,N}\) is the **actual minimum-lift compression to the original observation quotient**, its adjoint uses that quotient’s original metric, and \(\mathcal R\) has the original signs \(+,+,-,-\) at \(q-1,q,2q-1,2q\). The limit is evaluated below, not inferred from a determinant sign.

Separately, for the original Gaussian Mellin factor

$$
\Phi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),
$$

put

$$
D=125\,000\,000\,000,\qquad H=20D+100022.
$$

Then

$$
\boxed{
\mathcal W(\Phi P,\Phi P)
\ge e^{-37D}\sum_{j=0}^{D}H^{2j}|p_j|^2
\qquad
\left(P(s)=\sum_{j=0}^{D}p_js^j\right).
}
\tag{2}
$$

This includes the entire unknown high-zero tail. It requires no numerical computation of a matrix of that size.

These are different receiving forms. Equation (1) is a signed difference of four positive spectral traces. Equation (2) is positivity of the complete Weil quadratic form on a specified finite-dimensional source. No contradiction between them is asserted.

The first result uses the programme’s retained arithmetic–Gamma norm comparison and its stated EIQ one-cut estimate. The second uses published finite-height verification and zero-counting bounds. I also carry the preceding ES integral normalization into its full local Galois representation in Section 8.

# 1. The exact source decomposition has only one coupling direction

Retain

$$
q=e(k+1)^2,\qquad e=1+k(m_0-1),\qquad c=k/2,
$$

the complete polynomial \(\chi_k\), and

$$
d\mu_k(y)=w_h^{*k}(y)\,dy,\qquad S=c+iy.
$$

Write

$$
Q(y)=i^{-q}\chi_k(c+iy),\qquad
M=\frac{M_S-cI}{i}.
$$

At cutoff \(N\), the actual minimum-section space is

$$
\mathcal V_N
=
\mathcal P_N\ominus Q\mathcal P_{N-q}.
$$

Let \(C_N\) be the compression of multiplication by \(y\) to \(\mathcal V_N\). It is selfadjoint in the original quotient metric \(G_N\).

The current spectral-action source proves

$$
\boxed{
C_N=M+\mathsf R_N,\qquad
\operatorname{rank}\mathsf R_N\le1,\qquad
\mathsf R_N^2=0.
}
\tag{3}
$$

It retains the complete outgoing relation and all source phases. Its norm

$$
\varepsilon_N=\|\mathsf R_N\|_{G_N}
$$

is the original canonical allowance, not a new comparison constant. 

There is a second useful rank statement, on the **full polynomial source**.

Put

$$
d=N+1-q.
$$

Let \(J_N^\mu\) be the original \((N+1)\)-dimensional Jacobi matrix, and let \(J_{d-1}^{\chi,\mu}\) be the \(d\)-dimensional Jacobi matrix for the complete relation measure \(Q^2\,d\mu_k\). In the actual orthogonal splitting,

$$
\boxed{
J_N^\mu=
\begin{pmatrix}
C_N&X_N\\
X_N^*&J_{d-1}^{\chi,\mu}
\end{pmatrix},
\qquad \operatorname{rank}X_N\le1.
}
\tag{4}
$$

Indeed, if \(U_j\) are the monic relation polynomials, multiplication of

$$
\frac{QU_j}{\sqrt{\nu_j}}
$$

stays in the relation space for \(j<d-1\). Only the last relation column can leave it. Its norm is explicitly

$$
\boxed{
\|X_N\|^2
=
\frac{\nu_d-\omega_{N+1}}{\nu_{d-1}}.
}
\tag{5}
$$

The numerator is nonnegative because \(\nu_d\) is the norm of a monic degree-\((N+1)\) relation polynomial, whereas \(\omega_{N+1}\) is the unrestricted monic minimum.

Consequently,

$$
\operatorname{Tr}C_N^2
=
\operatorname{Tr}(J_N^\mu)^2
-\operatorname{Tr}(J_{d-1}^{\chi,\mu})^2
-2\|X_N\|^2.
\tag{6}
$$

The final term is \(O_h(q^2)\), uniformly on the original window, by the original multiplication bound. It cannot affect a \(q^3\)-scale second spectral moment.

# 2. A rank-one quotient comparison determines the arithmetic spectral limit

The main technical step is to compare characteristic values without paying the dimension times the arithmetic–Gamma norm width.

The original comparison is

$$
\ell_k\|P\|_\sigma^2
\le\|P\|_{\mu_k}^2
\le u_k\|P\|_\sigma^2,
\qquad
\Lambda_k=\log(u_k/\ell_k)=O_h(k+\log q),
\tag{7}
$$

on the complete polynomial spaces needed here. The comparison applies before the same affine minimum is taken.

## 2.1 Characteristic values use two rank-one minima

Push an even measure forward under

$$
x=y^2/q^2,
$$

and let \(P_h^\mu\) be its monic degree-\(h\) polynomial. For \(a\ge1\), define

$$
f_\mu(t)
=
\log\det\operatorname{Gram}_{\mathcal P_{h-1}}
[(x+a)^t\,d\mu].
$$

The determinant formula for the monic polynomial gives

$$
\log|P_h^\mu(-a)|=f_\mu(1)-f_\mu(0).
$$

Convexity gives

$$
\frac{f_\mu(0)-f_\mu(-2)}2
\le\log|P_h^\mu(-a)|
\le\frac{f_\mu(2)-f_\mu(0)}2.
\tag{8}
$$

The spaces

$$
\mathcal P_{h-1},
\qquad
(x+a)\mathcal P_{h-1}
$$

share \((x+a)\mathcal P_{h-2}\), of codimension one in each. Factoring their complete Grams through this common subspace cancels its determinant. Therefore

$$
\left|
[f_\mu(2)-f_\mu(0)]
-[f_\sigma(2)-f_\sigma(0)]
\right|
\le\Lambda_k.
\tag{9}
$$

There is no factor \(h\).

For the negative slope, the spaces

$$
\mathcal P_{h-1},\qquad
\frac{\mathcal P_{h-1}}{x+a}
$$

share \(\mathcal P_{h-2}\). If the original multiplication estimates give

$$
\int x|P|^2\,d\mu\le B_\mu\|P\|_\mu^2,
$$

Jensen supplies

$$
(a+B_\mu)^{-2}\|P\|_\mu^2
\le
\left\|\frac P{x+a}\right\|_\mu^2
\le a^{-2}\|P\|_\mu^2.
$$

The rational comparison consequently has width

$$
\Lambda_k^{\mathrm{rat}}
=
\Lambda_k+
2\log\frac{(a+B_\mu)(a+B_\sigma)}{a^2},
$$

and the second pair of rank-one quotients gives

$$
\left|
[f_\mu(0)-f_\mu(-2)]
-[f_\sigma(0)-f_\sigma(-2)]
\right|
\le\Lambda_k^{\mathrm{rat}}.
\tag{10}
$$

For the reference measure, consecutive Christoffel transformations by \(x+a\) interlace the positive zeros. A bound \(B_*\) for their largest zero therefore gives a bound

$$
\log(1+B_*/a)
$$

for each successive convexity gap in (8). Combining the two sides proves

$$
\boxed{
\left|
\log|P_h^\mu(-a)|
-\log|P_h^\sigma(-a)|
\right|
\le
\frac{\Lambda_k^{\mathrm{rat}}}{2}
+\frac32\log(1+B_*/a).
}
\tag{11}
$$

All \(B\)'s here are fixed finite quantities obtained from the original multiplication estimates at degree \(O(q)\). The same proof applies to the relation measures \(Q^2\mu_k\) and \(Q^2\sigma\): their comparison concerns the original polynomials \(QP\), so every root factor remains.

For an even-dimensional Jacobi matrix, (11) yields

$$
\boxed{
\left|
\frac1q\log\det\!\left(aI+\frac{J_\mu^2}{q^2}\right)
-
\frac1q\log\det\!\left(aI+\frac{J_\sigma^2}{q^2}\right)
\right|
\le\frac{\Lambda_k+C_h}{q}.
}
\tag{12}
$$

Adjacent odd dimensions are handled by ordinary interlacing, not by identifying their parity measures.

The squared spectral measures have uniformly bounded support. Equation (12), for every \(a\ge1\), determines their common weak limit: expansion at large \(a\) recovers all moments, and compact support makes those moments determining. This is the step that transfers the reference spectral calculation to the actual arithmetic source.

## 2.2 The full compression density is explicit

The ordinary Gamma Jacobi coefficients are

$$
a_n=\sqrt{n(n-\tfrac12)}.
$$

Counting fixed-length closed walks in the tridiagonal matrix gives the limiting even moments

$$
\frac{\binom{2j}{j}}{2j+1}.
$$

Equivalently, its \(q\)-scaled probability density is

$$
h_0(y)
=
\frac1{2\pi}\operatorname{arcosh}\frac2{|y|}
\,1_{\{0<|y|<2\}}.
\tag{13}
$$

For \(N=q-1+\lfloor sq\rfloor\), \(s>0\), the relation parity blocks have the original EIQ potential

$$
V_s(x)=\frac{\pi}{s}\sqrt x-\frac2s\log x.
$$

Write their equilibrium support as \([u_s^2,v_s^2]\), with

$$
u_sK(\kappa_s)=2,\qquad
v_sE(\kappa_s)=2(1+s),\qquad
\kappa_s^2=1-u_s^2/v_s^2.
\tag{14}
$$

These are the existing EIQ conventions. The reference asymptotic uses the stated one-cut theorem on the retained positive interval, not analyticity through zero (Borot & Guionnet, 2013).

The density has the fully specified positive formula

$$
\boxed{
\rho_s(x)=
\frac{\sqrt{(v_s^2-x)(x-u_s^2)}}{4\pi s\,x}
\int_0^\infty
\frac{\sqrt w\,dw}
{(x+w)\sqrt{(u_s^2+w)(v_s^2+w)}}.
}
\tag{15}
$$

It follows by writing \(x^{-1/2}\) as its Stieltjes integral and applying the two endpoint identities in (14).

Equations (4) and (12) now give the actual arithmetic compression law:

$$
\boxed{
d\nu_s(y)
=
\left[
h_0\!\left(\frac y{1+s}\right)
-s|y|\rho_s(y^2)
\right]dy.
}
\tag{16}
$$

Its mass is \((1+s)-s=1\). Its positivity also follows from its construction as the weak limit of the actual compressed spectral probabilities.

In particular, define

$$
H_0(t)=
\int_0^1e^{-2tu^2}I_0(2tu^2)\,du,
$$

where \(I_0\) is the modified Bessel function, and

$$
\boxed{
H_s(t)
=
(1+s)H_0((1+s)^2t)
-s\int e^{-tx}\rho_s(x)\,dx.
}
\tag{17}
$$

Then

$$
\boxed{
\frac1q\operatorname{Tr}e^{-tC_N^2/q^2}\longrightarrow H_s(t),
\qquad
\frac1q\operatorname{Tr}
\left[
\frac{C_N^2}{q^2}e^{-tC_N^2/q^2}
\right]
\longrightarrow-H_s'(t).
}
\tag{18}
$$

The four original cutoffs correspond to \(s=0,0,1,1\). These limits retain the original relation subtraction. They are not spectral limits of a trial norm.

# 3. Evaluate the coefficient controlling the signed Gaussian return

The first moment of the relation equilibrium is

$$
\boxed{
\int x\rho_s(x)\,dx
=
\frac{(1+s)(u_s^2+v_s^2)-2u_sv_s}{6s}.
}
\tag{19}
$$

To derive it, expand the equilibrium Cauchy transform at infinity. The required elliptic integral reduces by

$$
\int_0^{\pi/2}(1-\kappa^2\sin^2\theta)^{3/2}d\theta
=
\frac{2(2-\kappa^2)E(\kappa)
-(1-\kappa^2)K(\kappa)}3,
$$

after which (14) gives (19).

Therefore

$$
\boxed{
\mathfrak m(s):=
\lim\frac{\operatorname{Tr}C_N^2}{q^3}
=
\frac23(1+s)^3
-\frac{(1+s)(u_s^2+v_s^2)-2u_sv_s}{6}.
}
\tag{20}
$$

At the endpoints,

$$
\mathfrak m(0)=\frac23,\qquad
\mathfrak m(1)=\frac{16-u^2-v^2+uv}{3}.
\tag{21}
$$

The strict comparison needed for a sign can be proved without inserting numerical elliptic values:

$$
\boxed{\mathfrak m(1)>\frac{17}{25}>\frac23.}
\tag{22}
$$

Here are the finite inequalities. Put \(r=u/v\). The endpoint equation is \(rK/E=1/2\). The function \(rK/E\) is strictly increasing because

$$
\frac{d}{dr}\frac{rK}{E}
=
\frac{(K-E)(E-r^2K)}{(1-r^2)E^2}>0.
$$

The AGM bound at \(r=1/8\) gives \(K<4\), while \(E\ge1\); hence \(r>1/8\). Also \(K>E\) gives \(r<1/2\).

If \(r\ge3/20\), then

$$
v^2(1-r+r^2)<16(1-3/20+9/400)=349/25.
$$

If \(1/8<r\le3/20\), the identity

$$
E-1
\ge \frac{r^2(K-E)}{2(1-r^2)}
$$

gives

$$
E\ge\left(1-\frac{r(1-2r)}{4(1-r^2)}\right)^{-1}
\ge(1-7/320)^{-1}.
$$

Consequently,

$$
v^2(1-r+r^2)
\le\frac{57}{4}\left(\frac{313}{320}\right)^2
<\frac{349}{25}.
$$

Since \(u^2+v^2-uv=v^2(1-r+r^2)\), equation (22) follows.

There is also a uniform positive bound throughout the original window:

$$
\boxed{\mathfrak m(s)>\frac1{24}\qquad(0\le s\le1).}
\tag{23}
$$

Indeed \(v_s\le2(1+s)\), \((1+s)u_s/v_s=E/K<1\), and \(u_s>1/2\). Substitution in (20) gives

$$
\mathfrak m(s)\ge\frac{u_sv_s}{6}>\frac1{24}.
$$

# 4. The actual observation quotient has the same bulk Gaussian action

This is where the result passes through the previously unresolved observation metric.

In the original simple-packet observation, write

$$
r_K=\dim K_k=8k-16=o(q).
$$

Let \(\Pi_{B,N}\) be the \(G_N\)-orthogonal projection onto the attained observation complement. In the original quotient metric,

$$
C_{B,N}=\Pi_{B,N}C_N|_B
$$

is selfadjoint, and

$$
\boxed{
M_{B,N}
=\Lambda_kML_N
=C_{B,N}-\mathsf R_{B,N},
\qquad
\operatorname{rank}\mathsf R_{B,N}\le1.
}
\tag{24}
$$

No nilpotence of the compressed rank-one term is assumed.

Compression by a codimension-\(r_K\) subspace changes a normalized bounded-variation spectral trace by \(O(r_K/q)\). A rank-one perturbation changes the normalized singular-value trace by \(O(1/q)\). Applying those two exact interlacing bounds to

$$
x^2e^{-tx^2}
$$

gives

$$
\boxed{
\frac1q\operatorname{Tr}
\left[
\frac{M_{B,N}^{\dagger}M_{B,N}}{q^2}
e^{-tM_{B,N}^{\dagger}M_{B,N}/q^2}
\right]
\longrightarrow-H_s'(t).
}
\tag{25}
$$

The convergence is uniform over original observation kernels of the stated \(O(k)\) dimension. It does not require the values of \(U_N,V_N,\theta_N\).

The same expression is one half of the genuine selfadjoint Gaussian spectral action on

$$
\mathscr D_{B,N}
=
\frac1q
\begin{pmatrix}
0&M_{B,N}\\
M_{B,N}^{\dagger}&0
\end{pmatrix}:
$$

$$
\frac12\operatorname{Tr}
\left(\mathscr D_{B,N}^2e^{-t\mathscr D_{B,N}^2}\right).
$$

Both copies retain the original quotient metric.

Thus the complete four-cutoff limit is the evaluated function

$$
\boxed{
\mathfrak A(t)
=
2[-H_0'(t)+H_1'(t)].
}
\tag{26}
$$

At \(t_*=1/1024\), the limiting squared spectral supports are contained in \([0,4]\) and \([0,16]\). Therefore

$$
-H_0'(t_*)\le\mathfrak m(0)=2/3,
$$

while

$$
-H_1'(t_*)
\ge(1-16t_*)\mathfrak m(1)
>\frac{63}{64}\frac{17}{25}.
$$

It follows that

$$
\boxed{
\mathfrak A(1/1024)
<
\frac43-\frac{34}{25}\frac{63}{64}
=-\frac{13}{2400},
}
\tag{27}
$$

which proves (1).

This is a definite sign in a complete original-metric, original-observation receiver. Its distinction from the projected current is explicit: it is a four-cutoff trace of a bounded function of the singular-value operator, not the quadratic expression

$$
2\Re(\overline{s_{N-1}^B}s_N^B)/D_{N-1}^B.
$$

The heat parameter also matters. The complete function is not of one sign. From (13),

$$
H_0(t)
=
\frac{\log(64t)+\gamma_{\mathrm E}}{4\sqrt{\pi t}}
+O(t^{-3/2}),
$$

and the relation support stays away from zero. Hence

$$
H_1(t)-H_0(t)
=
\frac{\log2}{2\sqrt{\pi t}}+O(t^{-3/2}),
$$

$$
\mathfrak A(t)
=
-\frac{\log2}{2\sqrt{\pi}\,t^{3/2}}
+O(t^{-5/2}).
\tag{28}
$$

Moreover,

$$
\int_0^\infty\mathfrak A(t)\,dt=0.
$$

Since \(\mathfrak A\) is negative near zero and at sufficiently large \(t\), it must be positive on an intermediate interval. This is an exact feature of the evaluated receiver, not an independently chosen favorable heat scale.

# 5. The Gaussian action and the canonical allowance are connected by one singular mode

The preceding bulk limit does not make the original canonical allowance small. Its location can now be identified quantitatively.

The exact rank-one trace identity is

$$
\operatorname{Tr}M^2
=
\operatorname{Tr}C_N^2-2\ell_NC_Nr_N.
$$

For the full original grid,

$$
\operatorname{Tr}M^2
=
\frac{qk(k+2)}3(\gamma^2-\delta^2)
=o(q^3).
$$

Since

$$
|\ell_NC_Nr_N|
\le\|C_N\|_{G_N}\varepsilon_N
$$

and \(\|C_N\|=O_h(q)\), equations (20)–(23) prove

$$
\boxed{\varepsilon_N\ge c_hq^2}
\tag{29}
$$

eventually, uniformly over the complete original window.

Let

$$
s_1(M)\ge\cdots\ge s_q(M)
$$

be its singular values in \(G_N\). Rank-one singular interlacing gives

$$
|s_1(M)-\varepsilon_N|\le\|C_N\|,
\qquad
s_j(M)\le\|C_N\|\quad(j\ge2).
\tag{30}
$$

Thus precisely one singular value can carry the super-macroscopic scale.

In particular,

$$
\boxed{
\log s_1(M)^2
=
2\log\varepsilon_N+O_h(q^{-1}).
}
\tag{31}
$$

After the original window weights are summed,

$$
\boxed{
J_k^{\mathrm{action}}
=
\sum_{N=q-1}^{2q-1}w_N\log s_1(M;G_N)^2
+O_h(1).
}
\tag{32}
$$

This is an explicit spectral identification of the existing allowance. It also explains why a bounded heat action can miss it. Put

$$
\lambda_{1,N}=s_1(M;G_N)^2/q^2.
$$

Frullani’s identity gives the complete formula

$$
\boxed{
J_k^{\mathrm{action}}
=
4q\log q+
\sum_Nw_N
\int_0^\infty
\frac{e^{-t}-e^{-\lambda_{1,N}t}}t\,dt
+O_h(1).
}
\tag{33}
$$

The contribution is concentrated at shrinking heat times. It cannot be discarded by taking a fixed-\(t\) Gaussian limit first.

There is a further finite-part value. For every fixed \(t>0\),

$$
\boxed{
\operatorname{Tr}
\left[
\frac{M^{\dagger_N}M}{q^3}
e^{-tM^{\dagger_N}M/q^3}
\right]
\longrightarrow\mathfrak m(s),
}
\tag{34}
$$

whereas

$$
\boxed{
\operatorname{Tr}
\left[
\frac{M^2}{q^3}e^{-tM^2/q^3}
\right]\longrightarrow0.
}
\tag{35}
$$

Equation (34) follows directly from (30): the largest singular mode is killed by the Gaussian, while the remaining squared singular values sum to

$$
\operatorname{Tr}C_N^2+O_h(q^2).
$$

Equation (35) uses the actual complex eigenvalues and their full multiplicities. Triangular functional calculus makes their nilpotent derivatives trace-zero; it does not delete the nilpotent operators.

Thus the metric and holomorphic Gaussian actions have a nonzero calculated gap. They are related by the original rank-one correction, rather than treated as interchangeable spectral traces.

# 6. The rank-one interpolation has genuine Gaussian asymptotics and escaping spectral modes

The source edition requested a continuation from finite polynomial traces to genuine heat functions. The following supplies that continuation with a convergent remainder.

Set

$$
T_{\eta,N}=C_N-\eta\mathsf R_N.
$$

Its complete characteristic polynomial is

$$
p_\eta(z)
=(1-\eta)\det(zI-C_N)+\eta\chi_u(z).
\tag{36}
$$

This is the original SA characteristic identity, with all repeated-root factors retained. 

Let

$$
B_N=\max\{\|C_N\|,k\sqrt{\delta^2+\gamma^2}\}.
$$

For \(|\eta|\le U\), pairing every opposite root proves that all eigenvalues of \(T_{\eta,N}\) lie in

$$
|z|\le R_*:=2B_N\sqrt{q(1+2U)}.
\tag{37}
$$

Indeed, on this circle each of the two monic characteristic polynomials, divided by \(z^q\), differs from one by less than a fixed fraction of \(1/(1+2U)\). Their combination therefore cannot vanish.

For any complex heat parameter \(\tau\),

$$
\boxed{
\left|
\operatorname{Tr}e^{-\tau T_{\eta,N}^2}
-\sum_{j=0}^{m}\frac{(-\tau)^j}{j!}
\operatorname{Tr}T_{\eta,N}^{2j}
\right|
\le
q e^X\frac{X^{m+1}}{(m+1)!},
\quad X=|\tau|R_*^2.
}
\tag{38}
$$

For a requested tolerance \(0<\epsilon<q\), it is sufficient to take

$$
m+1\ge
\max\{e^2X,\ 2\log(q/\epsilon)\}.
$$

At \(\tau=t/q^2\), this requires \(m=O_{h,U,t}(q+\log\epsilon^{-1})\), rather than an exponential number of terms in \(\varepsilon_N\).

There is also a nontrivial limiting characteristic function. Put

$$
a_s=\mathfrak m(s)/2.
$$

Uniformly on compact subsets of \(w\ne0\),

$$
\boxed{
\frac{p_\eta(q^{3/2}w)}{(q^{3/2}w)^q}
\longrightarrow
\eta+(1-\eta)e^{-a_s/w^2}.
}
\tag{39}
$$

The proof expands the two complete paired products. The \(C_N\) term has

$$
\log\frac{\det(q^{3/2}w-C_N)}{(q^{3/2}w)^q}
=
-\frac{\operatorname{Tr}C_N^2}{2q^3w^2}
+O_h(q^{-1}),
$$

whereas every fixed-grid root of \(\chi_u\) is \(o(q^{3/2})\).

For fixed \(0<\eta<1\), put

$$
L_\eta=\log\frac{\eta}{1-\eta}.
$$

Rouché’s theorem now produces actual interpolation eigenvalues with

$$
\boxed{
\frac{\lambda_{\pm,j}}{q^{3/2}}
\longrightarrow
\pm\sqrt{
-\frac{a_s}{L_\eta+i(2j+1)\pi}
},
\qquad j\in\mathbb Z\text{ fixed}.
}
\tag{40}
$$

These are eigenvalues of the specified interpolated operator, not additional zeta zeros.

For \(\eta>1/2\), they force genuine holomorphic heat growth:

$$
\boxed{
\liminf\frac1q
\log\left\|e^{-tT_{\eta,N}^2/q^2}\right\|_{G_N}
\ge
\frac{t\,a_sL_\eta}{L_\eta^2+\pi^2}.
}
\tag{41}
$$

At \(\eta=e^\pi/(1+e^\pi)\), the right side is \(t\mathfrak m(s)/(4\pi)\).

Finally, all fixed trace coefficients, and then the entire coarse heat function, have explicit limits. Let \(\kappa_r(p)\) be the Bernoulli cumulants:

$$
\kappa_1(p)=p,\qquad
\kappa_{r+1}(p)=p(1-p)\frac{d}{dp}\kappa_r(p).
$$

Then

$$
\boxed{
q^{-3r}\operatorname{Tr}T_{\eta,N}^{2r}
\longrightarrow
\frac{2(-1)^{r+1}a_s^r}{(r-1)!}\,
\kappa_r(1-\eta),
}
\tag{42}
$$

and

$$
\boxed{
\operatorname{Tr}e^{-tT_{\eta,N}^2/q^3}-q
\longrightarrow
-2\sum_{r\ge1}
\frac{(a_st)^r}{r!(r-1)!}\kappa_r(1-\eta).
}
\tag{43}
$$

The series is entire in \(t\). Uniform coefficient bounds follow by extracting the logarithm of (39) on one sufficiently large circle, so (43) is not merely a formal exchange of limits.

# 7. The complete Weil form is positive through degree \(125\) billion

This result is independent of the hypothetical offcritical packet.

Retain the original form

$$
\mathcal W(F,F)
=
\sum_\rho m_\rho\,
\overline{F(1-\bar\rho)}F(\rho),
$$

and the original Gaussian source

$$
F_P(s)=\Phi(s)P(s),\qquad
\Phi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
$$

Its physical representative is \(P(D)\phi_*\), with

$$
D=-x\frac d{dx},\qquad
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.
$$

Every finite polynomial degree remains in the original even Schwartz source, vanishes at zero, and has zero integral. The source edition had proved complete positivity for the cubic subspace; the following estimates extend that conclusion. 

Use

$$
T_0=3\cdot10^{12}.
$$

Platt and Trudgian’s finite-height theorem puts every zero below \(T_0\) on the critical line. The Hasanalizade–Shen–Wong bound gives, with a conservative allowance for the counting convention,

$$
\left|
N(T)-\frac{T}{2\pi}\log\frac{T}{2\pi e}
\right|
\le
0.104\log T+0.258\log\log T+10.25.
\tag{44}
$$

In particular, \(N(T)\le T\log T\) for \(T\ge100\). These are finite-height and unconditional counting inputs, not assumptions about the remaining zeros (Platt & Trudgian, 2021; Hasanalizade, Shen, & Wong, 2022).

## 7.1 A separated set of \(D+1\) verified critical zeros

For every \(T\ge10^5\), equation (44) proves

$$
N(T+20)-N(T)>0.
$$

For example, its lower bound is

$$
\frac{10}{\pi}\log\frac{T}{2\pi}
-2\left[
0.104\log(T+20)
+0.258\log\log(T+20)+10.25
\right].
$$

It is positive at \(10^5\) and increasing thereafter.

Take the even integer

$$
D=125\,000\,000\,000.
$$

Choose one critical zero in each interval

$$
[100000+40j,\ 100020+40j],
\qquad 0\le j\le D/2,
$$

and include the negatives for \(0\le j<D/2\). This gives exactly \(D+1\) distinct critical zeros, all below

$$
B=20D+100020<T_0,
$$

with successive distances at least \(20\). No simplicity assumption is needed.

Put \(H=B+2\), and write

$$
P(s)=\sum_{j=0}^Dp_js^j
=\sum_{j=0}^Dc_j(s/H)^j,
\qquad c_j=H^jp_j.
$$

For the normalized nodes \(z_j=\rho_j/H\), each has modulus less than one. The coefficient norm of its Lagrange polynomial is bounded by

$$
\|\ell_j\|_2
\le
\frac{(H/10)^D}{j!(D-j)!}.
$$

Indeed, the numerator has coefficient \(\ell^1\)-norm at most \(2^D\), and its denominator is at least

$$
(20/H)^D j!(D-j)!.
$$

Therefore

$$
\sum_j\|\ell_j\|_2^2
\le
(H/10)^{2D}\frac{\binom{2D}{D}}{(D!)^2}
\le
\left(\frac{eH}{5D}\right)^{2D}
<e^{4.8D}.
$$

Interpolation and Cauchy–Schwarz give

$$
\boxed{
\sum_{j=0}^D|P(\rho_j)|^2
\ge e^{-4.8D}\sum_{j=0}^D|c_j|^2.
}
\tag{45}
$$

Complex Stirling with its remainder gives

$$
|\Phi(1/2+it)|^2\ge e^{-\pi t/2}\qquad(t\ge10).
$$

Since \((\pi/2)B<31.5D\), the selected verified zeros contribute at least

$$
\boxed{
e^{-36.3D}\sum_j|c_j|^2.
}
\tag{46}
$$

## 7.2 The entire unknown tail is smaller

Uniformly for \(0\le\beta\le1\) and \(|t|\ge10\),

$$
|\Phi(\beta+it)|
\le5(1+t^2)e^{-\pi|t|/4}.
$$

For a coefficient vector \(c\),

$$
|P(\beta+it)P(1-\beta+it)|
\le
(D+1)\left(1+\frac{t^2}{H^2}\right)^D
\sum_j|c_j|^2.
$$

Put \(c=\pi/2\). Stieltjes integration by parts, \(N(t)\le t^2\), and the preceding inequalities bound both signs of the unknown tail by

$$
\boxed{
\mathcal T_D
\le
\frac{200c(D+1)}
{c-(2D+6)/T_0}\,
T_0^6
\left(1+\frac{T_0^2}{H^2}\right)^D
e^{-cT_0}.
}
\tag{47}
$$

The denominator is positive.

To obtain (47), use, for \(t\ge T_0\),

$$
1+t^2/H^2
\le
(t/T_0)^2(1+T_0^2/H^2)
$$

and

$$
(t/T_0)^{2D+6}
\le
\exp\!\left(\frac{2D+6}{T_0}(t-T_0)\right).
$$

No tail zero has been placed on the critical line.

Now \(T_0=24D\) and \(T_0/H<6/5\). Hence

$$
\log\mathcal T_D
<
-36.78D+206.
\tag{48}
$$

Combining (46)–(48), and retaining every other verified zero as a nonnegative contribution, proves

$$
\boxed{
\mathcal W(\Phi P,\Phi P)
\ge
e^{-37D}
\sum_{j=0}^DH^{2j}|p_j|^2,
\qquad \deg P\le D.
}
\tag{49}
$$

This is an analytic certificate for the whole \(D+1\)-dimensional space. It does not require locating the selected zeros more accurately than their disjoint intervals, computing their multiplicities, or evaluating a \(125\)-billion-dimensional matrix.

Consequently, any negative full-Weil vector of this original Gaussian-polynomial type must have degree greater than \(125\,000\,000\,000\). This statement is finite; it does not supply positivity at arbitrary degree.

The original conductor receiver remains available: translate \(S'=s+c_*-1/2\), apply the actual conductor coefficient map, and retain the coefficient scaling \(\operatorname{diag}(H^j)\) in the lower bound. Thus the result applies to the retained finite jet lifts from the signed ES algebra without identifying their multiplication-trace form with the Weil form.

# 8. The ES integral degeneration now has its full local representation

The preceding integral calculation also admits a further completion.

At a hard prime \(p\equiv1\pmod{12}\), retain the actual distinct roots

$$
t_0=p,\quad t_1=x,\quad t_2=y,\quad t_3=z,
$$

and

$$
F(T)=A\prod_i(T-t_i),\qquad A=-1/(p+x+y+z).
$$

On the \(p\)-integral coefficient chart, put

$$
b_i=\sum_{j\ne i}\nu_p(t_i-t_j),
\qquad
\epsilon_i=b_i\bmod2,
\qquad
u_i=p^{-b_i}F'(t_i)\in\mathbb Z_p^\times.
$$

The normalized factor at label \(i\) is

$$
\mathbb Z_p[\tau_i],\qquad
\tau_i^2=p^{\epsilon_i}u_i.
$$

The roots, signs, and fixed conductor transport are the original ES crosswalk data.

Let \(\chi_i\) be the corresponding quadratic character of the local Galois group, trivial when the factor splits. A residue cluster of \(m\ge2\) labels has one geometric point in the original nonreduced special fibre, while its generic signed fibre has \(2m\) points. Its exact specialization representation is

$$
0\longrightarrow\mathbf1
\longrightarrow
\bigoplus_{i\in\mathcal C}(\mathbf1\oplus\chi_i)
\longrightarrow\mathcal V_{\mathcal C}
\longrightarrow0.
$$

Therefore

$$
\boxed{
\mathcal V_{\mathcal C}
\cong
\mathbf1^{\,m-1}
\oplus\bigoplus_{i\in\mathcal C}\chi_i.
}
\tag{50}
$$

Its rank is \(2m-1\), its Swan conductor is zero, and its Artin conductor is

$$
\boxed{a(\mathcal V_{\mathcal C})=\sum_{i\in\mathcal C}\epsilon_i.}
\tag{51}
$$

This makes the earlier normalization-index identity more informative:

$$
\boxed{
2\,\operatorname{length}(\widetilde{\mathscr E}_p/\mathscr E_p)
+a(\text{generic signed representation})
=
6\sum_{i<j}\nu_p(t_i-t_j).
}
\tag{52}
$$

For a separated one-divisible-denominator exterior state, the colliding labels \(p,z\) have the same ramified quadratic character. The earlier cofactor calculation gives

$$
\chi_p=\chi_z=\chi_{pD_E}.
$$

Thus

$$
\boxed{
\mathcal V_{\{p,z\}}
=
\mathbf1\oplus\chi_{pD_E}^{\oplus2},
\quad
a=2,\quad
\dim\mathcal V^{I_p}=1.
}
\tag{53}
$$

For a separated two-divisible-denominator state,

$$
y=pY,\qquad z=pZ,\qquad Y+Z\equiv4YZ\pmod p,
$$

all derivative valuations in the three-label cluster are even. Its three quadratic characters are unramified, and their residue units are

$$
u_\alpha\equiv
(\alpha-\beta)(\alpha-\gamma)\pmod p,
\qquad
\{\alpha,\beta,\gamma\}=\{1,Y,Z\}.
$$

Their product has square class \(-1\), which is a square at the retained hard primes. Hence the Frobenius polynomial of the rank-five quotient in (50) is either

$$
\boxed{(1-T)^5}
$$

or

$$
\boxed{(1-T)^3(1+T)^2.}
\tag{54}
$$

For the exact witness

$$
(p;x,y,z)=(1201;306,21618,61251),
$$

one has \(Y=18,Z=51\), and the three units are

$$
850,\qquad640,\qquad449\pmod{1201}.
$$

Their quadratic characters are \(-1,+1,-1\). Thus the actual quotient representation has Frobenius polynomial

$$
\boxed{(1-T)^3(1+T)^2}
$$

and trace one.

The original special fibre has three \(\mathbb F_{1201}\)-points; the normalized unramified fibre has four. Their difference is precisely that trace. The original normalization cokernel still has length nine and Smith exponents

$$
0,0,0,1,1,2,2,3.
$$

This is an explicit case where a substantial integral gluing defect coexists with an unramified normalized representation. It does not identify local Galois Frobenius with the zeta programme’s complex multiplication operator.

# Resulting state

The finite spectral-action task has advanced beyond polynomial identities. The full original source and observation quotients now have an evaluated Gaussian bulk law, an evaluated signed four-cutoff Gaussian action, a quantified singular mode carrying the canonical allowance, and convergent heat expansions for the rank-one interpolation. The interpolation also has explicitly located escaping spectral modes and a proved Gaussian norm-growth rate.

The complete Weil calculation now proves positivity of the original Gaussian-polynomial source through degree \(125\) billion, with all unknown high zeros retained in the error estimate. The ES continuation identifies the full local specialization representation and its conductor, rather than only its integral index or number of geometric points.

The remaining original projected-current expression still depends on the consecutive complex phase

$$
\Re(\overline{s_{N-1}^B}s_N^B).
$$

Neither the bounded Gaussian trace nor finite-degree Weil positivity determines that phase. The independent proper-source target minimum also remains distinct from the source and relation spectral differences calculated here. These results do not establish RH.

The derivations above are written proofs from the stated inputs. No new numerical zeta-zero or period evaluation, large-matrix computation, execution receipt, remote commit, or formal verification is claimed.

**References used.** Borot, G., & Guionnet, A. (2013). *Asymptotic expansion of β matrix models in the one-cut regime*. Hasanalizade, E., Shen, Q., & Wong, P.-J. (2022). *Counting the zeros of the Riemann zeta function*. Platt, D. J., & Trudgian, T. S. (2021). *The Riemann hypothesis is true up to \(3\cdot10^{12}\)*. *Bulletin of the London Mathematical Society, 53*, 792–797. The Clankers. (2026, September 20). *Native spectral action along the outgoing arithmetic relation: Exact cyclic coefficients, full determinants and metric curvature*, together with the original EIQ, GRA, ES-crosswalk, and complete-Weil source editions.
