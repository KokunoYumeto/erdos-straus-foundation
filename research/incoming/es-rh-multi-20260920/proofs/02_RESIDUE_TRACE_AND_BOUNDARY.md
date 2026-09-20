# Track II — Residue duality, the exact non-unit element, and boundary transport

**Status.** The finite rank-eight extension was constructed in the preceding continuation. This note calculates its complete residue pairing, trace pairing, determinant and local ES/RH comparison. It does not identify a bilinear residue pairing with the original positive Hermitian metric. A finite flat complete intersection is Gorenstein in the standard sense (Stacks Project, Tag 0C15); the explicit matrices below prove the required duality here directly.

## 1. Root algebra and an everywhere nondegenerate pairing

Work over

\[
 R_0=\mathbb C[A,A^{-1},B,C,D],\quad
 h(r)=Ar^4+r^3+Br^2+Cr+D,\quad E=R_0[r]/(h).
\]

This is free of rank four in the original basis \(1,r,r^2,r^3\). Define the functional

\[
 \lambda_E(f)=A^{-1}[r^3]\operatorname{rem}_h f.
\]

Let \(C_h\) be multiplication by \(r\) in that basis. Reduction of the powers through degree six gives its full bilinear pairing matrix

\[
 J_h=\begin{pmatrix}
0&0&0&A^{-1}\\
0&0&A^{-1}&-A^{-2}\\
0&A^{-1}&-A^{-2}&A^{-3}-BA^{-2}\\
A^{-1}&-A^{-2}&A^{-3}-BA^{-2}&-A^{-4}+2BA^{-3}-CA^{-2}
\end{pmatrix}.
\]

Its anti-triangular pattern gives

\[
 \boxed{\det J_h=A^{-4},\qquad J_h C_h=C_h^T J_h.}
\]

These hold without inverting the discriminant. The pairing is therefore perfect also on nonreduced root fibres. All transposes in this section are ordinary transposes, not conjugate transposes.

At a squarefree target, Lagrange interpolation gives

\[
 \lambda_E(f)=\sum_j\frac{f(r_j)}{h'(r_j)}.
\]

For the original signed moment matrix \(U=(r_j^n)\operatorname{diag}(\xi_j)\), with \(\xi_j^2h'(r_j)=1\), this proves

\[
 \boxed{UU^T=J_h.}
\]

The identity uses the squares \(\xi_j^2\), not their squared moduli. Neither positive definiteness nor an isometry of the original Gamma or arithmetic norm follows. At collisions the individual entries of the inverse states may diverge while this bilinear product has a finite algebraic continuation.

## 2. A finite extension that keeps the original pole

Define

\[
 \widehat S=E[\eta]/(\eta^2-h'(r)).
\]

It is free of rank eight with basis

\[
 1,r,r^2,r^3,\eta,\eta r,\eta r^2,\eta r^3.
\]

The original signed inverse algebra is the exact open subalgebra

\[
 E[\xi]/(\xi^2h'-1)\simeq\widehat S[\eta^{-1}],
 \quad\eta=\xi h',\quad\xi=\eta^{-1}.
\]

Substitution proves both compositions. This is a finite flat extension over \(A\ne0\); it is not asserted to be a normalization, nor to repair the separate boundary at \(A=0\).

In these coordinates the original Fable point is exactly

\[
 q(r,\eta)=\left(
 \eta^{-1},\ -r-i\eta,\ A\eta^3+2r\eta+3i\eta^2,
 7ir^2\eta+(B-17r+Ar^2)\eta^2-13i\eta^3-2A\eta^4
 \right)^T.
\]

The first coordinate is a genuine meromorphic pole. For a fixed injective receiving map \(F\) with its actual positive metric \(Q\), put \(G=F^*QF\). If the approach to \(\eta=0\) stays over a finite coefficient-base point, then \(r,A,B\) remain bounded; boundedness of \(r,A,B\) is the sufficient hypothesis used in the following coordinate calculation. Direct multiplication of every displayed coordinate by \(\eta\) gives

\[
 \eta q\longrightarrow e_1,\qquad
 \boxed{|\eta|\,\|Fq\|_Q\longrightarrow\sqrt{G_{11}}>0.}
\]

Bounded literal roots alone are not enough for this limit, because the leading coefficient \(A\) may diverge while roots remain bounded. The noncancellation conclusion itself needs no coefficient-boundedness assumption: the first coordinate of \(\eta q\) is identically one, so positive definiteness of \(G\) gives the uniform estimate

\[
 \boxed{|\eta|\,\|Fq\|_Q=\|F(\eta q)\|_Q
 \ge \sqrt{\lambda_{\min}(G)}\,\|\eta q\|_2
 \ge \sqrt{\lambda_{\min}(G)}>0.}
\]

Adding the finite algebraic boundary therefore does not cancel an original metric infinity.

## 3. The exact non-invertible element is multiplication by \(2\eta^3\)

Write every element as \(f+\eta g\), \(f,g\in E\), and define

\[
 \Lambda(f+\eta g)=\lambda_E(g).
\]

Products show that its full residue Gram is

\[
 \mathcal J=\begin{pmatrix}0&J_h\\J_h&0\end{pmatrix},
 \qquad \boxed{\det\mathcal J=A^{-8}.}
\]

Indeed the even-even and odd-odd products have no odd component; each mixed product contributes \(\lambda_E(fg)\). Thus this pairing stays perfect everywhere on the base.

Let \(M_f\) denote multiplication by an element \(f\) in \(\widehat S\). Then

\[
 \boxed{\operatorname{Tr}(M_f)=\Lambda(2\eta^3 f).}
\]

Proof: on the squarefree open set, the eight states are \((r_j,\pm\eta_j)\), with \(\eta_j^2=h'(r_j)\). Their trace on \(f_0+\eta f_1\) is \(2\sum_j f_0(r_j)\). On the other hand,

\[
 \Lambda(2\eta^3(f_0+\eta f_1))
 =2\lambda_E(h'f_0)=2\sum_j f_0(r_j).
\]

Both sides are regular functions over the integral base ring \(R_0\), so equality on the dense squarefree open set proves it globally. Applying this identity to every product proves the pairing factorization

\[
 \boxed{\text{trace pairing}=\text{residue pairing}\circ M_{2\eta^3}.}
\]

The Jacobian determinant of the two defining relations \((h,\eta^2-h')\), in variables \((r,\eta)\), is also \(2\eta h'=2\eta^3\), agreeing with the explicit trace calculation. No general residue theorem is required to verify the displayed formula.

Let \(\Delta_h=\operatorname{Disc}(h)\). Since

\[
 \operatorname{Norm}_{E/R_0}(h')=\Delta_h/A^2,
\]

and multiplication by \(\eta\) has determinant \(\Delta_h/A^2\) on \(\widehat S\),

\[
 \det M_{2\eta^3}=2^8\Delta_h^3/A^6.
\]

Consequently

\[
 \boxed{\det(\text{trace Gram})=256\,\Delta_h^3/A^{14}.}
\]

This locates the loss exactly. The residue map to the dual is invertible. Multiplication by \(2\eta^3\) is a unit precisely on the squarefree open set; it becomes singular on the boundary. The original linear conductor is a separate map and remains governed by its own nonzero leading moment and WCF quotient.

## 4. Local fibre and rank at an arbitrary multiple root

Fix a target with an \(m\)-fold root \(r_0\), and write

\[
 h(r)=(r-r_0)^m g(r),\qquad g_0=g(r_0)\ne0,\quad\varepsilon=r-r_0.
\]

In the local root algebra \(\mathbb C[\varepsilon]/(\varepsilon^m)\),

\[
 h'=m g_0\varepsilon^{m-1}.
\]

Therefore the local completed signed fibre is

\[
 \boxed{\mathbb C[\varepsilon,\eta]/
  (\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1})},
 \qquad \text{length}=2m.
\]

Multiplication by \(\varepsilon\) has two Jordan blocks of size \(m\), since the algebra is free with basis \(1,\eta\) over the truncated root algebra. For \(m\ge2\),

\[
 \eta^3=mg_0\eta\varepsilon^{m-1}\ne0,\qquad \eta^4=0.
\]

Every nonconstant monomial annihilates \(\eta^3\), while multiplication by 1 does not. Thus multiplication by \(2\eta^3\) has rank one on this length-\(2m\) local fibre, and the trace pairing has rank one. The residue pairing stays nondegenerate because it is the restriction of the perfect pairing to the corresponding idempotent summand.

For the quartic \(h\), only \(m=2,3,4\) can occur. The certificate's additional \(m=5,6,7\) checks test the same local formula in the generalized degree-\(m\) model; they are not multiplicities of this quartic.

For \(m=2\), \(\varepsilon=\eta^2/(2g_0)\), so the algebra is exactly \(\mathbb C[\eta]/(\eta^4)\). This is one length-four nonreduced state, not four finite distinct points. It retains the limiting algebraic multiplicity of four nearby signed states.

## 5. An explicit ES/RH local algebra map, including its residue correction

The ES family

\[
 (p;x,y,z)=(p;p,2p/5,2p)
\]

satisfies the original reciprocal equation. Its normalized quartic is

\[
 h_E(r)=-\frac5{22p}(r-p)^2(r-2p/5)(r-2p).
\]

At the double root \(p\),

\[
 g_{0,E}=3p/22,\qquad g_{1,E}=1/11,
 \qquad\eta_E^2=(3p/11)\varepsilon_E.
\]

For \(p=5\), this is the actual integral example \((5;5,2,10)\). It is not in the hard-prime domain from the preceding continuation.

Fix the source parameter \(\gamma>0\). The RH source's *auxiliary* paired-root polynomial is

\[
 h_R(r)=-\tfrac12((r-\tfrac12)^2+\gamma^2)^2.
\]

At \(r_s=1/2+s i\gamma\), \(s=\pm1\),

\[
 g_{0,R}=2\gamma^2,\qquad g_{1,R}=-2s i\gamma,
 \qquad\eta_R^2=4\gamma^2\varepsilon_R.
\]

Choose either square root \(c^2=3p/(44\gamma^2)\). Then

\[
 \phi:\eta_E\mapsto c\eta_R,\quad
 \varepsilon_E\mapsto\varepsilon_R
\]

is an isomorphism of the two length-four local algebras. It intertwines centred multiplication exactly; the uncentred variable acquires the explicit scalar correction \(p-r_s\).

The full residue functional contains the derivative of the cofactor. At a double root,

\[
 \lambda_E(f_0+f_1\varepsilon)
 =f_1/g_0-f_0g_1/g_0^2.
\]

Therefore the residue functionals under \(\phi\) are **not** in general related by just a constant. The exact relation is

\[
 \boxed{\Lambda_R(\phi f)=\Lambda_E(u_E f),\qquad
 u_E=c^3\left[1+\left(\frac2{3p}+\frac{s i}{\gamma}\right)\varepsilon_E\right].}
\]

To check it, write the odd part of \(f\) as \(\eta_E(b_0+b_1\varepsilon_E)\). The two sides are respectively

\[
 c\left(b_1/g_{0,R}-b_0g_{1,R}/g_{0,R}^2\right)
\]

and the same expression after using \(g_{0,E}=c^2g_{0,R}\). The even part contributes zero. The bracketed element is a unit because \(\varepsilon_E^2=0\); its inverse is obtained by changing the sign of its nilpotent term, followed by \(c^{-3}\). This is an explicit correction, not an assumed residue isometry.

In the basis \(1,\eta,\eta^2,\eta^3\), the algebra map has matrix \(\operatorname{diag}(1,c,c^2,c^3)\). A positive Hermitian metric transforms by its complete conjugate congruence, with determinant factor \(|c|^{12}\). The algebra map does not supply numerical values for either original native Gram.

## 6. Why this does not produce purity by itself

For a nonzero nilpotent \(N\) with \(N^2=0\), every positive Hermitian metric \(G\) has an indefinite defect \(N^*G+GN\). Choose \(Nv=w\ne0\), \(Nw=0\). On the two vectors \((w,v)\), the upper-left entry is zero and the off-diagonal entry is \(\|w\|_G^2\). The determinant of that compression is \(-\|w\|_G^4<0\). Thus both signs occur.

The completed local algebra and its perfect bilinear pairing are useful exact structures. Neither removes the native metric pole nor proves an isometric arithmetic action or RH. The separate analytic metric return is addressed in Tracks III–V.

## 7. Transport through the fixed original conductor

Let the original fixed four-plane maps be \(\Phi_*:\mathbb C^4\to U_*\), \(\Psi_*:\mathbb C^4\to W_*\), with \(L\Phi_*=\Psi_*\), as in the source. Realize the eight coefficient coordinates through

\[
 F_U=\operatorname{diag}(\Phi_*,\Phi_*),\quad
 F_W=\operatorname{diag}(\Psi_*,\Psi_*),\quad
 (L\oplus L)F_U=F_W.
\]

For every displayed algebra multiplication matrix \(M_a\), define \(M_a^U=F_U M_a F_U^{-1}\) and \(M_a^W=F_W M_a F_W^{-1}\). Then

\[
 (L\oplus L)M_a^U=M_a^W(L\oplus L).
\]

This includes the non-unit multiplication \(M_{2\eta^3}\), at every allowed auxiliary parameter. The residue and trace matrices transport by \(F^{-T}\mathcal JF^{-1}\), and their factorization persists. The original Hermitian forms transport separately by conjugate transpose. Every map here is on its specified image, with the reference conductor and norms fixed. The inverse-exterior factors of \(L\oplus L\) remain exactly those of the source's direct-sum conductor; no boundary singularity is reclassified as a zero of its original triangular determinant.
