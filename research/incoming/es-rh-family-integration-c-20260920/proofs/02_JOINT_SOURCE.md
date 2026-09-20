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
