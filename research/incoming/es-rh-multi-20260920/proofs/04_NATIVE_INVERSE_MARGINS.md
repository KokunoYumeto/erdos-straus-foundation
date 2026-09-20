# Track IV — Exponentially better native monomial inverse margins

**Status.** This improves the explicit interval-Gram floor in the new repository source `NATIVE_MOMENT_PRECISION.tex`. The original native measure, monomials, interval and density floor are unchanged. Classical Legendre identities are credited to NIST DLMF §§18.5 and 18.9. The calculation below returns them to the exact original coordinates.

## 1. The source bound being improved

The repository derives a positive density floor \(d_\lambda\) for each original native parity measure or positive tilt on \([1,2]\). Its monomial interval Gram is

\[
 J_t=\left[\frac{2^{i+j+1}-1}{i+j+1}\right]_{i,j=0}^t.
\]

It uses the valid lower bound

\[
 J_t\succeq g_tI,\qquad g_t=\det J_t/(\operatorname{tr}J_t)^t,
\]

with

\[
 \det J_t=\prod_{j=0}^t\frac{(j!)^4}{(2j)!(2j+1)!}.
\]

The complete source also gives a convenient lower bound for \(g_t\) with an exponent quadratic in \(t\). The determinant identity is retained; the determinant-over-trace enclosure is what is sharpened here.

## 2. Exact inverse in the unmodified monomial coordinates

Set

\[
 L_j(x)=P_j(2x-3)=\sum_{k=0}^j c_{jk}x^k,
\]

where \(P_j\) is the classical Legendre polynomial. Rodrigues' formula, or its finite binomial expansion followed by \(x\mapsto x-1\), gives

\[
 \boxed{c_{jk}=(-1)^{j-k}
 \sum_{m=k}^j\binom jm\binom{j+m}{m}\binom mk.}
\]

All coefficients are explicit integers. Let \(C_t\) contain these rows padded to length \(t+1\). Classical orthogonality and the exact substitution \(u=2x-3\), \(dx=du/2\), give

\[
 C_t J_t C_t^T=\operatorname{diag}((2j+1)^{-1})_{j=0}^t.
\]

The triangular \(C_t\) is invertible, so

\[
 \boxed{J_t^{-1}=C_t^T\operatorname{diag}(2j+1)C_t.}
\]

This is an identity in the original monomial coordinates. It does not replace a native polynomial by a normalized Legendre coordinate without transporting its coefficients.

Define the positive integer

\[
 \tau_t=\operatorname{tr}J_t^{-1}
 =\sum_{j=0}^t(2j+1)\sum_{k=0}^j c_{jk}^2.
\]

The largest eigenvalue of a positive matrix lies between its trace divided by its dimension and its trace. Applying this to \(J_t^{-1}\) proves

\[
 \boxed{J_t\succeq\tau_t^{-1}I,\qquad
 \tau_t^{-1}\le\lambda_{\min}(J_t)\le(t+1)\tau_t^{-1}.}
\]

Thus the new lower margin is within a factor \(t+1\) of the actual smallest eigenvalue of the interval Gram. This is not a claim about the smallest eigenvalue of the entire unknown native Gram; that Gram is only lower-bounded by the interval contribution.

It is also at least as strong as the earlier determinant-over-trace floor in every degree, not only in the checked finite table. If \(\lambda_1,\ldots,\lambda_{t+1}>0\) are the eigenvalues of \(J_t\), then

\[
 \tau_t=\sum_i\lambda_i^{-1}
 =\frac{e_t(\lambda_1,\ldots,\lambda_{t+1})}{\det J_t},
 \qquad
 \tau_t^{-1}=\frac{\det J_t}{e_t(\lambda_1,\ldots,\lambda_{t+1})}.
\]

Every monomial occurring in the elementary symmetric polynomial \(e_t\) occurs with a positive coefficient in \((\sum_i\lambda_i)^t\). Hence

\[
 \boxed{\tau_t^{-1}\ge
 \frac{\det J_t}{(\operatorname{tr}J_t)^t}=g_t.}
\]

## 3. A simple exponential lower bound

The displayed coefficient signs alternate. Hence

\[
 \sum_k|c_{jk}|=|L_j(-1)|=P_j(5).
\]

The three-term Legendre recurrence and positivity for \(x>1\) show \(P_j(5)\le10^j\): the recurrence's subtraction term is nonnegative, and its leading multiplier is below 10; start from \(P_0(5)=1\), \(P_1(5)=5\). Therefore

\[
 \sum_k c_{jk}^2\le\left(\sum_k|c_{jk}|\right)^2\le100^j,
\]

and

\[
 \boxed{\tau_t\le(t+1)(2t+1)100^t,\qquad
 J_t\succeq\frac{I}{(t+1)(2t+1)100^t}.}
\]

This removes the quadratic-in-degree exponent from this part of the conditioning bound. It does not remove other source constants, growing moment caps, quotient singular values or the computational expense of high-degree arithmetic moments.

Exact examples are

| t | tau_t | new floor | approximate log10(new/old) |
|---:|---:|---:|---:|
|0|1|1|0|
|1|40|1/40|0|
|2|2685|1/2685|1.864|
|5|1556000328|1/1556000328|20.239|
|10|9826531238433072229|reciprocal of preceding integer|96.934|
|20|563499044407063990221634119557036635401|reciprocal of preceding integer|427.757|

The exact rational old/new values are recorded in `results/native_gram_floor.json`; decimals are descriptive only. `check_gram_floor.py` checks the inverse factorization through degree 7, all finite coefficient bounds through degree 20, and the exact floor comparison through degree 20. The proof above is for all degrees.

## 4. Native floors and finite moment tolerances

For a native measure with density at least \(d_\lambda>0\) on \([1,2]\),

\[
 H_t^\lambda=\left[\int x^{i+j}d\lambda\right]\succeq
 d_\lambda J_t\succeq m_tI,\qquad m_t=d_\lambda/\tau_t.
\]

For every original positive pole \(a>0\), the same argument gives

\[
 H_t^{(1)}+aH_t\succeq(1+a)m_tI,
\quad H_t^{(2)}+aH_t^{(1)}\succeq(1+a)m_tI.
\]

Indeed \(x\ge1\) on that interval. Let all scalar moments through degree \(2t+2\) have an absolute error at most \(\epsilon\), with real symmetric assembled approximations. A dimension-\((t+1)\) matrix with entry errors bounded by \(e\) has operator error at most \((t+1)e\). Thus the relative error is at most

\[
 \boxed{\delta=\frac{(t+1)\epsilon\tau_t}{d_\lambda}}
\]

for each of these matrices; the common factor \(1+a\) cancels in the weighted cases. A sufficient explicit prescription is

\[
 \boxed{\epsilon\le\frac{d_\lambda}{4(t+1)\tau_t},}
\]

which gives \(\delta\le1/4\). If an individual true matrix has lower margin \(m\) and absolute operator error \(e<m\), then

\[
 \|\widetilde H^{-1}-H^{-1}\|\le\frac{e}{m(m-e)}.
\]

This follows from the resolvent identity \(\widetilde H^{-1}-H^{-1}=-\widetilde H^{-1}(\widetilde H-H)H^{-1}\). A relative certificate also yields

\[
 (1+\delta)^{-1}H^{-1}\preceq\widetilde H^{-1}
 \preceq(1-\delta)^{-1}H^{-1}.
\]

These finite bounds can replace the old \(g_t\)-based margin at each use in the repository's moment-to-current composition. All other terms in that composition must remain; the present calculation is not an evaluation of its native inputs.

## 5. Coupling with the previously derived auxiliary-degree rate

The earlier continuation proved, for the original tilted parity measures and poles \(a_j=4j^2\),

\[
 \lambda_r^{(b)}(4j^2)
 \le\frac{\mathcal K_{k,j}}{(r+1)^{2j}},\qquad
 \mathcal K_{k,j}=
 \frac{\pi\sqrt{2\pi}}{4j}\overline a_k((5/4)_{j-1})^2.
\]

Here \(\lambda_r^{(b)}\) is the native Gauss residual scalar; \(\overline a_k\) is the unchanged source upper-envelope constant. The proof used the actual scalar residual minimum, domination by the original Gamma measure, and the Meixner–Pollaczek coefficient identity at \(2ij\). Its finite coefficient inequalities have been rechecked in `check_previous_bounds.py`; no new rate is being claimed for the first time in this packet.

At a chosen pole, replace the existing finite-moment upper scalar \(\gamma_r\) by

\[
 \widehat\gamma_r=\min\{\gamma_r,\mathcal K_{k,j}(r+1)^{-2j}\}.
\]

This is a minimum of scalar bounds on the same rank-one ray. It is not a minimum of unrelated Loewner matrices. The required \(r\) follows from the prior source-error allocation; the improved margin above then prescribes sufficient accuracy for the moments used at that \(r\). This provides a two-stage degree/precision prescription, still dependent on the stated original source constants and moments. Outer-tail truncation remains governed by the original TR/RR bounds.

## 6. General positive-coefficient weights in the newest precision source

For every degree-\(L\) polynomial weight \(w(x)=\sum_{l=0}^Lw_lx^l\) with \(w_l\ge0\) and \(w(1)>0\), its original weighted moment Gram has lower floor \(w(1)d_\lambda/\tau_t\), because \(w(x)\ge w(1)\) on \([1,2]\). If every scalar moment needed by this weight has absolute error at most \(\epsilon\), its scalar entry error is at most \(w(1)\epsilon\). Those data extend through degree \(2t+L\); in particular, \(x(x+a)(x+b)\) requires moments through degree \(2t+3\), rather than the degree \(2t+2\) sufficient for the matrices in Section 4. The same relative budget therefore applies with all original moment shifts present. This replaces only the interval factor \(g_t\) by \(\tau_t^{-1}\). The source's separate Radau subtraction, reciprocal scalar margin, multiplication errors and quotient-coordinate constants still have to be included at their actual uses.
