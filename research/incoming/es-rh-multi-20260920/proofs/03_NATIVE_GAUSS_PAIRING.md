# Track III — The exact map from residue duality to native moment Grams

**Status.** A finite algebraic identity for the original positive measures. It explains exactly which multiplier converts a residue pairing into a native Gram, and exactly which correction survives for an arbitrary ES root polynomial. The classical Gauss/Stieltjes context is not claimed as new; the explicit receiving factorization and residual are the objects used here. The finite diagnostic uses six rational atoms and is not an evaluation of the arithmetic density.

## 1. Original positive moment problem

Let \(d\rho\) be one of the programme's actual native parity measures or its positive tilt, with \(\operatorname{supp}\rho\subset[0,\infty)\). Retain its full mass \(\mu_0\), moments \(\mu_j=\int x^j d\rho\), and original real coordinate \(x\). Assume its polynomial Grams through the degree in use are positive definite. For the native measures this follows from their positive-almost-everywhere density and finite moments.

For \(n\ge1\), let \(p_n\) be the monic degree-\(n\) orthogonal polynomial. Define

\[
 H_{n-1}=[\mu_{i+j}]_{i,j=0}^{n-1},\qquad
 E_n=\mathbb C[z]/(p_n),
\]

and the monic residue functional

\[
 \lambda_p(f)=[z^{n-1}]\operatorname{rem}_{p_n}f.
\]

Let \(J_p\) be its pairing matrix and \(C_p\) multiplication by \(z\), in \(1,z,\ldots,z^{n-1}\). The anti-diagonal entries of \(J_p\) are one; the entries above that anti-diagonal are zero. Hence

\[
 \det J_p=(-1)^{n(n-1)/2}\ne0.
\]

This algebraic pairing is complex bilinear and can be indefinite on real vectors. It is not the native Hermitian form.

## 2. The multiplier with its original mass

Define the second-kind polynomial by the finite identity

\[
 q_{n-1}(z)=\int\frac{p_n(z)-p_n(x)}{z-x}\,d\rho(x).
\]

The numerator is divisible by \(z-x\), so this is a polynomial of degree \(n-1\) whose leading coefficient is exactly \(\mu_0\). No normalization of the measure is needed.

For every polynomial \(f\) of degree less than \(n\),

\[
 \lambda_p(q_{n-1}f)=\int f(x)\,d\rho(x).
\]

One proof is to use the simple real roots \(t_j\) of the orthogonal polynomial and the Lagrange cardinals \(L_j(z)=p_n(z)/((z-t_j)p_n'(t_j))\). Evaluating the defining formula of \(q\) at \(t_j\) gives

\[
 \frac{q(t_j)}{p_n'(t_j)}=\int L_j(x)\,d\rho(x).
\]

Lagrange interpolation of \(f\) then proves the identity. For completeness, the roots are simple and lie in the convex hull of the positive support by the usual elementary sign-change argument: if the real polynomial had fewer than \(n\) sign changes in that support, multiplying the factors at its sign changes would give a polynomial of degree below \(n\) whose product with \(p_n\) has a fixed nonzero sign almost everywhere, contradicting orthogonality.

For any product \(z^{i+j}\), \(0\le i,j<n\), divide by \(p_n\). The quotient has degree at most \(n-2\). Its integral multiplied by \(p_n\) vanishes by orthogonality. Thus the same identity applies to all moment-Gram entries and gives

\[
 \boxed{H_{n-1}=J_p\,q_{n-1}(C_p).}
\]

The order of the matrices is specified. Multiplication is self-adjoint for the residue pairing: \(J_pC_p=C_p^TJ_p\). Therefore the product is symmetric, as required. Since the original moments are real, that same real symmetric matrix is the native positive Hermitian form on complex coefficient vectors.

Both \(H_{n-1}\) and \(J_p\) are invertible, so \(q(C_p)\) is a unit of this root-algebra representation. Equivalently \(p_n\) and \(q_{n-1}\) are coprime. The native mass is present in \(q\): multiplying \(d\rho\) by a positive scalar multiplies \(q\) and \(H\) by that scalar, while \(p_n\) and \(J_p\) stay unchanged.

## 3. Positivity of the finite weights and the resolvent identity

The polynomial \(L_j^2-L_j\) vanishes at every root of \(p_n\). Its quotient by \(p_n\) has degree at most \(n-2\). Orthogonality therefore proves

\[
 w_j:=\frac{q(t_j)}{p_n'(t_j)}
 =\int L_j\,d\rho=\int L_j^2\,d\rho>0.
\]

The native Gram has the exact Gauss decomposition

\[
 H_{n-1}=\sum_j w_j(1,t_j,\ldots,t_j^{n-1})^T
                    (1,t_j,\ldots,t_j^{n-1}).
\]

This is a consequence of the native orthogonality, not an arbitrary choice of the ES roots as nodes.

For \(a>0\), partial fractions give

\[
 \sum_j\frac{w_j}{a+t_j}=-\frac{q(-a)}{p_n(-a)}.
\]

The same quantity is the scalar Gauss lower approximation obtained from the native finite matrices:

\[
 c^T(D+aH)^{-1}c=-\frac{q(-a)}{p_n(-a)},
\]

where \(H=[\mu_{i+j}]_{0\le i,j<n}\), \(D=[\mu_{i+j+1}]\), and \(c=(\mu_0,\ldots,\mu_{n-1})^T\). To see this without selecting new nodes, the Galerkin equation asks for \(Q\) with \(\deg Q<n\) such that \(1-(x+a)Q\) is orthogonal to every polynomial of degree below \(n\). Thus

\[
 1-(x+a)Q(x)=p_n(x)/p_n(-a).
\]

Integrating \(Q\), using the defining divided difference of \(q\), gives the rational expression. Expanding the squared residual in the original measure gives the standard nonnegative Gauss error. No unknown native integral is assigned a numerical value by this identity.

More explicitly, \(p_n(-a)\ne0\) because all roots of \(p_n\) lie in \([0,\infty)\), and the exact error is

\[
 \boxed{
 \int\frac{d\rho(x)}{x+a}
 -c^T(D+aH)^{-1}c
 =\frac1{p_n(-a)^2}\int\frac{p_n(x)^2}{x+a}\,d\rho(x)\ge0.}
\]

For a positive measure whose support is not contained in \([0,\infty)\), the same algebraic resolvent formula requires the separate hypothesis \(p_n(-a)\ne0\), and the displayed sign additionally requires \(x+a>0\) on the support.

## 4. Arbitrary root polynomials retain a full relation defect

Now take any monic real polynomial \(h\) of degree \(n\), whether orthogonal or not. Let \(J_h\) be its perfect residue Gram and \(C_h\) its companion. Define the polynomial \(k\), of degree below \(n\), by

\[
 [k]=J_h^{-1}(\mu_0,\ldots,\mu_{n-1})^T.
\]

Then \(\lambda_h(kf)=\int f d\rho\) for all \(f\) of degree below \(n\), by the definition of \(k\). For higher products, exact polynomial division gives

\[
 \boxed{H_{ij}=[J_h k(C_h)]_{ij}+\mathcal D_{ij},\qquad
 \mathcal D_{ij}=\int h(x)\operatorname{quo}_h(x^{i+j})\,d\rho(x).}
\]

This is valid even if \(h\) has repeated roots, because no root evaluation or discriminant inverse is used. The entire defect is a finite linear combination of original moments. If \(h=p_n\), orthogonality kills it, and \(k=q_{n-1}\). For a generic ES quartic divided by its leading coefficient, no such orthogonality has been established, so the defect must remain.

For complex \(h\), the coefficient-functional identity is still an exact bilinear statement on polynomial products. One must separately include conjugated coefficients when forming a Hermitian moment Gram; it is not legitimate to replace transpose by adjoint in the algebraic identity. The real ES literal-root polynomial and the real native orthogonal polynomials already give the directly applicable real case.

## 5. Programme-level meaning

The combined map is now explicit:

\[
 \text{root-algebra residue duality}
 \xrightarrow{\ M_q\ }
 \text{native Gauss Gram},
\]

with full mass in \(q\), and with the additional \(\mathcal D\) whenever the root polynomial is not the native orthogonal polynomial. The ES/Fable algebra and the RH native moment calculation can use the same finite algebra machinery, but the map between their metrics contains a computed multiplier and, generally, a relation residual.

The next analytic task is to evaluate or enclose the actual moments determining \(q\), \(k\), and \(\mathcal D\), rather than infer positivity from a complex residue pairing. Tracks IV and V give improved inverse margins and exact simultaneous propagation for that purpose.

## 6. An explicit inverse margin for the residue-to-native multiplier

Track IV proves \(H_{n-1}\succeq(d_\rho/\tau_{n-1})I\) whenever the original measure has density at least \(d_\rho\) on the retained interval \([1,2]\). The exact factorization above therefore gives

\[
 \boxed{\|q(C_p)^{-1}\|_2
 =\|H_{n-1}^{-1}J_p\|_2
 \le\frac{\tau_{n-1}}{d_\rho}\|J_p\|_2.}
\]

All entries of \(J_p\) are finite polynomial remainders determined by the actual native monic polynomial. No assertion of positivity of \(q(C_p)\) in the Euclidean coefficient metric is needed. The bound is not valid for an arbitrary nonorthogonal ES polynomial after discarding \(\mathcal D\); that difference is precisely why the full residual in Section 4 is retained.
