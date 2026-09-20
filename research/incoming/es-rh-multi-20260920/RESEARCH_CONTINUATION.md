# Combined ES–Fable–RH research continuation

20 September 2026. Five connected derivation tracks.

The source ledger at the end identifies the pinned snapshots and reading scope. The ZIP contains the executable exact checks and complete receipts.

**Verification:** 541 exact checks and eleven deliberately false-inference controls per interpreter mode; normal and optimized outputs are byte-identical. This is not Lean verification and does not evaluate unknown native arithmetic moments.


---

# Track I — The odd receiving divisor on the positive-real ES family

**Status.** New derivations relative to the pinned ES/RH sources; the generic odd-frame factorization and the earlier singular example are independently rechecked. This note proves neither universal ES occupancy nor nonvanishing of the odd determinant at every integral ES witness. Sources and their exact versions are in `SOURCE_LEDGER.md`.

## 1. Original source and receiving objects

For an ES solution, retain

\[
 4/p=1/x+1/y+1/z,\qquad S=p+x+y+z,
\]
\[
 h(r)=-S^{-1}(r-p)(r-x)(r-y)(r-z)=Ar^4+r^3+Br^2+Cr+D.
\]

The ES foundation's EZ6–EZ10 gives

\[
 A=-S^{-1},\quad B=-[p(x+y+z)+xy+xz+yz]/S,
 \quad C=5xyz/S,\quad D=-pxyz/S,
\]

and recovers \(p=-5D/C\). The coefficient equation is
\(625AD^3-125CD^2+25BC^2D-4C^4=0\). That equation alone has no integrality or positivity condition.

For distinct roots \(r_j\), put \(d_j=h'(r_j)\) and choose both signs of \(\xi_j^2d_j=1\). The original sign-odd columns are

\[
 o_j=\xi_j(1,-id_j,Ad_j^2+2r_jd_j,
                i(7r_j^2d_j-13d_j^2))^T.
\]

Let \(O=[o_1\ o_2\ o_3\ o_4]\), and let \(V_h\) be the coefficient matrix of the remainders of the four polynomials in this formula, in the unmodified basis \(1,r,r^2,r^3\). If

\[
 U=(r_j^n)_{0\le n\le3,1\le j\le4}\operatorname{diag}(\xi_j),
\]

then \(O=V_hU\). The product of all derivative factors gives

\[
 \det U=\chi/A^2,\qquad \chi\in\{1,-1\}.
\]

The sign changes with the chosen ordering and square-root branches; the following divisor does not.

## 2. The complete extra determinant factor

Define

\[
\begin{aligned}
 F(A,B,C,D)={}&20(3C-B^2)+A(87B^3-282BC-51D)\\
 &+A^2(-28B^4+22B^2C+431C^2+204BD)\\
 &+A^3(224B^2D-168BC^2-856CD)-448A^4D^2.
\end{aligned}
\]

Polynomial division gives

\[
 \det V_h=4F/A,\qquad \boxed{\det O=4\chi F/A^3.}
\]

This is checked over the rational function field, not fitted from samples. For an independently inspectable determinant, after the constant first row and the cancelling factors \((-i)i=1\), the remaining coefficient matrix is

\[
\begin{pmatrix}
2B&3&4A\\
4ABC-8AD-7C&4AB^2-2AC-16A^2D-5B&4AB-8A^2C-3\\
20C/A+76D-52BC&20B/A+5C-52B^2+208AD&20/A-66B+104AC
\end{pmatrix}.
\]

Its determinant is exactly \(4F/A\). In particular this is not the discriminant of \(h\), the Jacobian of the nonlinear Fable map, or the determinant of the original linear conductor.

## 3. A positive-real ES family crossing this divisor

For every real \(p>0\), define

\[
 (p;x,y,z)=p\left(1,\frac{t}{4t-402},\frac{t}{202},\frac{t}{200}\right),
 \qquad t>202.
\]

The reciprocal identity follows by adding \((4t-402)/(pt)\), \(202/(pt)\), and \(200/(pt)\). The strict ordering is

\[
 0<x<p<y<z.
\]

Thus the four literal roots are distinct throughout this interval. The normalization retains \(A=-1/S\).

At \(p=1\), direct substitution in the preceding polynomial gives

\[
 F(t)=-\frac{5t^2 f(t)}{(402t^2+10099t-4060200)^6},
\]

where the exact integer polynomial is

```text
f(t) = 2359424*t^12
 -2380972032*t^11
 -125022004322048*t^10
 +199766203719977640*t^9
 -126442260595802541476*t^8
 +41598937953326627478150*t^7
 -7385542427424681354996253*t^6
 +544226493322473956433710982*t^5
 +40187872427398803311778426564*t^4
 -12845040782988159530278491608280*t^3
 +1219651834158063698018605839792000*t^2
 -55076685665576109738730352971200000*t
 +998076020859413480649547526400000000.
```

The coefficients scale with \(p\) by \((A,B,C,D)\mapsto(p^{-1}A,pB,p^2C,p^3D)\). Every term of \(F\) has weight two, so the result for any \(p>0\) is \(p^2F(t)\).

The following are exact, reproducible polynomial facts, proved by the Euclidean/Sturm procedures implemented in `check_es_slice.py`:

\[
 \gcd(f,f')=1,\qquad \#\{t\in(551,651):f(t)=0\}=1,
\]

and its unique root \(t_*\) lies in

\[
 \boxed{\frac{3520743}{6176}<t_*<\frac{3562358}{6249}.}
\]

The decimal \(t_*\approx570.0684909\) is only a locator. No floating-point value is used to establish the root or the rank. The determinant scalar is negative at 551 and positive at 651. There is no denominator zero on that interval. A displayed 3-by-3 coefficient minor, stored exactly in `results/es_frame_divisor.json`, has numerator coprime to \(f\), so it is nonzero at \(t_*\). Consequently

\[
 \boxed{\operatorname{rank}O(t_*)=3}
\]

while \(A\operatorname{Disc}(h)\ne0\). The nonlinear inverse still has eight separate simple branches. The receiving frame alone has lost one direction.

Under the literal scaling by \(p\), the odd matrix satisfies

\[
 O_p=\operatorname{diag}(p^{-1},p,p^2,p^3)O_1
\]

for coherent sign choices. This proves rank preservation for every fixed positive \(p\), without declaring the diagonal map an isometry. The polynomial has no rational root. This is a positive-real ES solution family, including a fixed arbitrary prime value of \(p\), but its singular point is not an integral ES witness. No implication about occupancy or frame degeneracy at integral denominators follows from this example. It proves that positivity and the exact reciprocal equation, by themselves, do not remove the extra receiving divisor.

## 4. Integer separation when the extra factor is nonzero

Suppose the four literal roots are distinct positive integers. Their elementary symmetric sums \(e_1=S,e_2,e_3,e_4\) are integers, and

\[
 (A,B,C,D)=(-S^{-1},-e_2/S,e_3/S,-e_4/S).
\]

Inspection of every denominator in \(F\) shows

\[
 N=S^6F\in\mathbb Z.
\]

Therefore, **conditional on \(N\ne0\)**,

\[
 \boxed{|\det O|=4|N|/S^3\ge4/S^3.}
\]

For a selected root \(r_j\), the three differences from the remaining roots are distinct nonzero integers. The product of their absolute values is at least two and at most \(S^3\), so

\[
 2/S\le|d_j|\le S^2,\qquad S^{-1}\le|\xi_j|\le\sqrt{S/2}.
\]

The four entries of \(o_j\) consequently have absolute bounds

\[
 \sqrt{S/2},\quad S,\quad3S^2,\quad20S^3.
\]

Here \(|\xi_jd_j|=|d_j|^{1/2}\) and \(|\xi_jd_j^2|=|d_j|^{3/2}\); no branch phase has been replaced in the exact formulas. Summing the sixteen squared bounds gives \(\|O\|_2\le41S^3\) for \(S\ge1\). The exterior identity then proves

\[
 \boxed{\|O^{-1}\|_2\le\frac{41^3}{4}S^{12}\quad(N\ne0).}
\]

For the actual receiving Hermitian form \(G>0\), the map from \((\mathbb C^4,G)\) to Euclidean label coordinates has the additional factor \(\|G^{-1/2}\|_2\). A different original source metric contributes its own \(\|R^{1/2}\|_2\). No coefficient-frame norm is silently identified with the physical norm.

This estimate separates two tasks: arithmetic nonvanishing of the integer \(N\), which is not proved here, and quantitative inverse control once that nonvanishing is known.

## 5. Exact return to the original conductor

Let \(L\) be the original invertible finite conductor on the appropriate receiving four-plane, with the quotient and target norms in WCF4. Then

\[
 \ker(LO)=\ker O,\qquad \det(LO)=\det L\det O.
\]

Thus neither the extra frame divisor nor the missing direction is removed by the original conductor. Its inverse-exterior bound controls the \(L^{-1}\) factor where an inverse exists. In the actual-observation construction, replace the older cubic receiver by the source's \(F_B=\Lambda_kJ_+K^{-1}\), retaining \(\Lambda_kF_+=F_B\) and \(\bar C F_B=F_-\). These are maps on the indicated images, not identifications of ES roots with zeta zeros. The full original arithmetic Gram and both residual minimum energies remain those of MO5–MO10.

The next arithmetic question is whether \(N\) can vanish at an admissible integral hard-prime witness, or whether an exact congruence/positivity argument excludes it. A real-parameter frame singularity is not an answer to that arithmetic question.


---

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


---

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


---

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
|20|\(\begin{gathered}5634990444070\\6399022163411\\9557036635401\end{gathered}\)|reciprocal of preceding integer|427.757|

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


---

# Track V — Simultaneous native moment uncertainties through both minima

**Status.** Exact simultaneous finite-rank formulas and a finite polynomial certification procedure. The parameters enclose errors generated by the same native measure; independence of those errors is not asserted. The fixed-column degree bounds are not reused unchanged when the native orthogonal-polynomial columns are recomputed. The original outer-tail bound and the newest projection-error bounds remain separate inputs.

## 1. A common source family

Let the original positive source Gram be enclosed by

\[
 H(\theta)=H_0+V\Theta V^*,\qquad
 \Theta=\operatorname{diag}(\theta_1,\ldots,\theta_m),
 \quad H_0>0.
\]

The parameters are real, and the family is positive definite on the box being certified. Negative parameter intervals are allowed. This directly includes the RR finite resolvent family

\[
 H^{[J]}=H^{[J],+}
 -\frac4\pi\sum_j a_j\lambda_j z_jz_j^*,
 \qquad0\le\lambda_j\le\gamma_j,
\]

in both original parity blocks, followed by the exact complex coefficient congruence. The lower Radau source bound gives a positive floor for that whole enclosing box. The original infinite tail is not deleted; it must be attached through TR/RR or the latest PD bracket.

Let \(\mathsf A\) be any one of the actual onto maps: source remainder, its composition with the original observation, or its composition with the full conductor observation. Put

\[
 P=H_0^{-1},\quad G_0=(\mathsf A P\mathsf A^*)^{-1},
\]
\[
 L=V^*PV,\quad Z=G_0\mathsf A PV,
 \quad K=L-Z^*G_0^{-1}Z.
\]

Writing \(T=\mathsf A P^{1/2}\), the matrix

\[
 Q:=P-P\mathsf A^*G_0\mathsf A P
 =P^{1/2}\!\left[I-T^*(TT^*)^{-1}T\right]P^{1/2}
\]

is positive semidefinite. The bracketed matrix is the Euclidean orthogonal projection onto \(\ker T\), and the complete congruence by \(P^{1/2}\) transports it back to the original source coordinates. Therefore \(K=V^*QV\succeq0\). Neither \(K\) nor \(\Theta\) is assumed to commute with the other matrices.

## 2. Exact quotient, determinant and minimum representative

The whole attained quotient is

\[
 \boxed{G(\theta)=G_0+Z\Theta(I+K\Theta)^{-1}Z^*.}
\]

Its determinant and minimizing source lift are

\[
 \boxed{\frac{\det G(\theta)}{\det G_0}
 =\frac{\det(I+L\Theta)}{\det(I+K\Theta)},}
\]
\[
 \boxed{X_\theta=P\mathsf A^*G_0
 -B\Theta(I+K\Theta)^{-1}Z^*,\quad
 B=(P-P\mathsf A^*G_0\mathsf A P)V.}
\]

Here \(\mathsf A B=0\). Thus the correction remains inside the full original source kernel; \(X_\theta u\) is the actual minimum representative of \(u\).

Proof: the rank update identity, valid without \(\Theta^{-1}\), is

\[
 H(\theta)^{-1}=P-PV\Theta(I+L\Theta)^{-1}V^*P.
\]

To make the noncommutative cancellation explicit, put

\[
 X_0=P\mathsf A^*G_0,\qquad B=QV,
 \qquad \mathcal R=\Theta(I+K\Theta)^{-1}.
\]

The definitions give the ordered identities

\[
 \mathsf A B=0,\qquad V^*B=K,\qquad V^*X_0=Z^*.
\]

For \(X=X_0-B\mathcal R Z^*\), first \(\mathsf A X=I\). Also

\[
 H_0B=V-\mathsf A^*Z,
\]

and \(\mathcal R+\Theta K\mathcal R=\Theta\). Expanding every factor in its displayed order therefore gives

\[
 H(\theta)X
 =\mathsf A^*\!\left(G_0+Z\mathcal R Z^*\right).
\]

It follows that \(X=H(\theta)^{-1}\mathsf A^*G(\theta)\) and proves both the quotient and the minimizing lift without ever using \(\Theta^{-1}\). The identity
\(\Theta(I+K\Theta)^{-1}=(I+\Theta K)^{-1}\Theta\)
also proves the Hermitian symmetry. Finally, since \(Z^*G_0^{-1}Z=L-K\),

\[
 \frac{\det G}{\det G_0}
 =\det\!\left(I+\mathcal R(L-K)\right)
 =\det\!\left((I+\Theta K)^{-1}(I+\Theta L)\right)
 =\frac{\det(I+L\Theta)}{\det(I+K\Theta)}.
\]

Both denominator determinants are strictly positive wherever \(H(\theta)>0\). For \(L\), whiten by \(H_0\) and use the determinant lemma on the positive source Gram. For \(K\), compress that positive whitened source to \(\ker(\mathsf A P^{1/2})\), and use the same lemma. This argument covers indefinite \(\Theta\), zero parameters and linearly dependent columns of \(V\).

## 3. Nested minima use the same parameters

Let \(\mathsf A_E\) be the original remainder map and \(\Lambda:E\to B\) the original onto observation map. Build \(G_E(\theta)\) from \(\mathsf A_E\) and \(G_B(\theta)\) directly from \(\Lambda\mathsf A_E\). Then

\[
 G_B(\theta)=(\Lambda G_E(\theta)^{-1}\Lambda^*)^{-1}.
\]

This follows either by substitution or by minimizing the source norm first over a remainder fibre and then over its observation fibre. The set of all allowed source representatives is the same composite fibre. There is no second independent moment error after the first minimum.

For the fixed original three-column matrix \(W=[b_N,b_{N+1},v_\lambda]\), define

\[
 F=W^*G_EW,\qquad
 C=W^*\Lambda^*G_B\Lambda W,\qquad R=F-C.
\]

These are the full three-vector Gram, observed part and kernel part. The definitions retain all original complex entries. The equality \(R=F-C\) follows from the orthogonal minimum decomposition in \(G_E\); it is not a subtraction of unrelated bounds.

## 4. Multiaffine entry numerators and bounded-degree current polynomials

For either actual map, write

\[
 \Delta(\theta)=\det(I+K\Theta),
\]
\[
 N(\theta)=G_0\Delta+Z\Theta\operatorname{adj}(I+K\Theta)Z^*.
\]

Then \(G=N/\Delta\). Every entry of \(N\), and \(\Delta\), has degree at most one in each individual parameter. Indeed the \(i\)-th column of \(I+K\Theta\) depends only affinely on \(\theta_i\). In \(\Theta\operatorname{adj}(I+K\Theta)\), the cofactor paired with \(\theta_i\) omits that column, so it contains no further \(\theta_i\).

Let the complete fixed-frame numerators be \(N_F\) over \(\Delta_E\) and \(N_C\) over \(\Delta_B\). Then

\[
 R=\frac{N_R}{\Delta_E\Delta_B},\qquad
 N_R=N_F\Delta_B-N_C\Delta_E.
\]

Each entry of \(N_R\) has degree at most two in each parameter. The original undivided currents are

\[
 I_C=2\operatorname{Re}(\overline{C_{13}}C_{23}),
 \quad I_R=2\operatorname{Re}(\overline{R_{13}}R_{23}),
\]
\[
 I_\times=2\operatorname{Re}
 (\overline{R_{13}}C_{23}+\overline{C_{13}}R_{23}).
\]

Consequently \(I_C\) has a real numerator of degree at most two in each parameter over \(\Delta_B^2>0\). The other two have real numerators of degree at most four in each parameter over \((\Delta_E\Delta_B)^2>0\). Explicitly,

\[
 P_C=2\operatorname{Re}(\overline{(N_C)_{13}}(N_C)_{23}),
\]
\[
 P_R=2\operatorname{Re}(\overline{(N_R)_{13}}(N_R)_{23}),
\]
\[
 P_\times=2\operatorname{Re}
 [\overline{(N_R)_{13}}(N_C)_{23}\Delta_E
 +\overline{(N_C)_{13}}\Delta_E(N_R)_{23}].
\]

Both mixed products are present. Their exact sum identity is

\[
 P_R+P_C\Delta_E^2+P_\times
 =2\operatorname{Re}(\overline{(N_F)_{13}}(N_F)_{23})\Delta_B^2.
\]

The positive original factor \(\omega_N\) can then be divided out with its own exact value or positive enclosure. This step does not assign a constant \(\omega_N\) while the underlying native polynomials are changing.

## 5. A finite sign certificate, not endpoint sampling

Let a real polynomial \(P\) have degree at most \(d_i\) in parameter \(\theta_i\), and transport a specified rational box to \([0,1]^m\) by its stated affine coordinate map. Write its monomial coefficients there as \(a_\beta\). Its tensor-product Bernstein coefficients are

\[
 b_\alpha=\sum_{\beta\le\alpha}a_\beta
 \prod_i\frac{\binom{\alpha_i}{\beta_i}}{\binom{d_i}{\beta_i}},
 \qquad0\le\alpha_i\le d_i.
\]

Expanding the Bernstein basis proves this conversion. The basis functions are nonnegative and sum to one, so

\[
 \min_\alpha b_\alpha\le P(\theta)\le\max_\alpha b_\alpha.
\]

All positive coefficients certify \(P>0\) on the whole box. Otherwise subdivide and repeat. The code in `checks/bernstein.py` performs the coefficient conversion exactly over rational arithmetic and returns either a full positive covering certificate, a rational negative witness, or `inconclusive` at its prescribed depth. It does not claim that a negative point of the enclosing box is feasible for the original correlated native moments.

There is an explicit termination bound when a strict margin exists. Suppose \(P\ge\mu>0\) on the original box, let \(J=\{i:d_i\ge1\}\) be the active-coordinate set, and let \(L_i\) bound the absolute Bernstein coefficients of its physical-coordinate derivative \(\partial_iP\) on that box. Restriction to a subbox preserves this bound because de Casteljau subdivision is convex averaging. For a subbox with widths \(h_i\), the derivative-coefficient identity gives, for \(i\in J\),

\[
 |b_{\alpha+e_i}-b_\alpha|\le h_iL_i/d_i.
\]

Summing at most \(d_i\) steps in each active coordinate shows that every coefficient is at least \(P(\text{lower corner})-\sum_{i\in J} h_iL_i\). Thus any subdivision satisfying

\[
 \sum_{i\in J} h_iL_i<\mu
\]

certifies positivity. Uniform tensor refinement after \(s\) bisections in every one of \(m\) coordinates has widths \(h_i=2^{-s}\ell_i\), uses \(2^{ms}\) subboxes, and has sequential branch depth \(ms\); it is sufficient once \(2^{-s}\sum_{i\in J}\ell_iL_i<\mu\). For the implemented longest-side one-coordinate splitter, branch depth \(D\) is sufficient whenever

\[
 \boxed{\ell_{\max}2^{-\lfloor D/m\rfloor}
 \sum_{i\in J}L_i<\mu.}
\]

This is a conditional finite-completion theorem, not an assertion that the unknown native current has a positive margin. A smaller configured depth can return `inconclusive`, but cannot create a false positive because acceptance still requires an actual positive Bernstein covering.

Checking only vertices is invalid. The positive Gram family

\[
 C(s)=\begin{pmatrix}2&0&-1/4\\0&2&-3/4\\-1/4&-3/4&2\end{pmatrix}
 +s(1,1,1)^T(1,1,1),\quad0\le s\le1,
\]

has current numerator \(2(s-1/4)(s-3/4)\). It is positive at both endpoints and negative at \(s=1/2\). This is an exact counterexample to that checking rule, not an arithmetic counterexample.

## 6. Native monic columns must move with the same moments

If the original monic polynomial itself is recomputed from \(H(\theta)\), let \(q_0\) be the original monic degree-\(n\) minimizer and let \(J\) insert all lower-degree coefficients. Put

\[
 M_0=J^*H_0J,\quad B_0=J M_0^{-1}J^*V,
 \quad K_{\mathrm{mon}}=V^*J M_0^{-1}J^*V,
 \quad b=V^*q_0,
\]

and define the squared monic norms

\[
 h_0=q_0^*H_0q_0,\qquad
 h_\theta=q_\theta^*H(\theta)q_\theta.
\]

Then

\[
 \boxed{q_\theta=q_0-B_0\Theta(I_m+K_{\mathrm{mon}}\Theta)^{-1}b,}
\]
\[
 \boxed{h_\theta=h_0+b^*\Theta(I_m+K_{\mathrm{mon}}\Theta)^{-1}b.}
\]

Here \(I_m\) is the identity on the \(m\)-parameter space. The first correction has no leading-degree coefficient. Multiplying \(J^*H(\theta)q_\theta\) out gives zero, so it is the actual monic minimizer. Substitution in its squared norm, or completing the square in the lower-degree variables, gives the second identity. Orthonormal columns must also include \(h_\theta^{-1/2}\).

The same parameters therefore propagate through the native polynomials, quotient, observation, class and current. The fixed-\(W\) per-parameter degree-four bound must not be claimed after replacing \(W\) by moving columns without substitution. For monic conventions the substituted entries remain rational; positive norm factors can be cleared with their proved positivity where applicable, or bounded separately. This note makes no blanket degree claim for that expanded expression.

## 7. What the certificate does and does not settle

This method processes a finite native moment enclosure without breaking phase or kernel dependencies. It supports original-map congruences, both attained minima and simultaneous pole errors. A successful box certificate proves a sign for the actual native parameter point inside that box. A failed box certificate may only mean that the enclosing box discarded useful moment correlations.

The still-needed inputs are actual certified native moments and source constants, control of the outer tail, and the growing-degree sign margin relevant to the closing proposition. The repository's newest finite tolerances and projection-radius estimates help certify those inputs; they are not replaced by our synthetic exact tests or by ES root samples. Neither ES occupancy nor RH follows from constructing this finite certificate alone.


---

# Source and verification ledger

## Reading boundary

This continuation read the relevant repository definitions and new finite-precision sections through the GitHub connector, and checked the original weighted-conductor provider from the conversation upload. It did not read every historical manuscript, replay either repository's complete verification suite, or verify a Lean build. Definitions already displayed in the preceding conversation were used only with their explicit formulas and receiving domains; the carried calculations have their own recheck suite.

The GitHub refs below are immutable snapshots, not a promise that their branches remain at those commits. The ES and RH branch refs were checked at the start of this continuation. No write action was performed.

## Repository sources

### ES-1 — Source identity and actual quartic

The Clankers. (2026, September 20). *The normalized Erdős–Straus quartic and its exact passage through the signed Fable cover to a fixed weighted conductor* [Research manuscript]. Erdős–Straus Foundation.

Repository: \path{KokunoYumeto/erdos-straus-foundation}.
Commit: \path{2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3}.
Path: \path{research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex}.
Git blob: \path{dd7aa82fed5dc8ea6dd903a8731ec475a85984be}.
Read scope: original polynomial EZ4, source ES equation and normalized coefficients, EZ6–EZ17, source lines 1–260. The whole raw file was not downloaded into this package.

<https://github.com/KokunoYumeto/erdos-straus-foundation/blob/2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3/research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex>

The companion root README and bridge README were read for programme scope and exact locators, not treated as proof of every inherited claim.

### ES-2 — Existing receiving-frame qualification

The Clankers. (2026, September 20). *Independent audit notes for the frozen upstream packet* [Research audit]. Same repository and commit.
Path: \path{research/incoming/es-fable-zeta-bridge-20260920/AUDIT_NOTES.md}.
Git blob: \path{99c6799fc1fd4c3a289913ea140fc682dc8bf9d8}.
Read completely through the connector. In particular, squarefreeness does not imply odd-frame invertibility; the source gives a distinct regular-target rank-three example. Our positive-real ES slice is an additional computation, not the first discovery of the general qualification.

### RH-1 — Current programme frontier

Split-Zero programme. (2026, September 20). *Original theta transfer and certified complex-current precision* [Source release]. Zeta-function research reader.
Repository: \path{KokunoYumeto/zeta-function-research-reader}.
Commit: \path{1bcdcebb766d84c6edbb42bc7d4d845e960ec325}.
Its parent is \path{f8b73284d2e669e981bf2c7609e99f4d2b3a50be}.
Read root README and \path{workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/RESULT_INDEX.json} for the exact new release and remaining native moment/sign calculations. Source-reported test counts are not represented as our executions.

### RH-2 — Native inverse margin being improved

Split-Zero programme. (2026, September 20). *Explicit native moment precision, inverse margins, and the original signed receiver* [Research manuscript]. Same RH commit.
Path: \path{workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/NATIVE_MOMENT_PRECISION.tex}.
Git blob: \path{d7d4efac164faa684142fa4c38d9f58aab3fbcce}.
Read source lines 1–460: original native objects, density floors, interval determinant/trace floor, weighted inverse margins, finite moment budget, outward quadratic estimates and Radau/phase formulas. Later sections were not exhaustively read in this continuation.

<https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1bcdcebb766d84c6edbb42bc7d4d845e960ec325/workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/NATIVE_MOMENT_PRECISION.tex>

### RH-3 — Existing projection and phase bounds

Split-Zero programme. (2026, September 20). *Sharp original-metric projection control and disks for complex mixed pairings* [Research manuscript]. Same RH commit.
Path: \path{workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/PROJECTION_PHASE_RETURN.tex}.
Git blob: \path{ce29a20ba43452d913682ce428708db4a12b1982}.
Read source lines 1–240: PD1–PD17, including the sharp fixed-kernel projection bound and both complex pairing radii. Those are existing source results. The simultaneous rational-parameter update and polynomial certificate in Track V do not reattribute them as new results.

### RH-4 — The actual arithmetic observation receiver

Split-Zero programme. (2026, September 20). *The ES–Fable inverse correspondence in the original weighted conductor* [Cumulative manuscript]. Same RH commit.
Path: \path{workbenches/splitzero-tandem/continuations/20260920-marked-observation-illustrated/FABLE_TO_ORIGINAL_CONDUCTOR.tex}.
Git blob: \path{4674db16bf242f95e0b800f8dac14514363d6d76}.
Read the displayed cumulative definitions from the preceding conversation and re-read source lines 3835–3975 at the current pinned commit: MO4–MO11, original minimum residuals, the exact K-inverse marking, source/observation/conductor maps, original arithmetic action and its preserved scope. No whole-cumulative-manuscript reading claim is made.

### UP-1 — Byte-preserved original weighted conductor

Split-Zero programme. (n.d.). *A polynomial forward bound for the full weighted conductor* [Additive LaTeX provider, WCF].
Provider body: \path{sources/WEIGHTED_CONDUCTOR_FORWARD.tex}.
Original body size: **25,840 bytes**.
Original SHA-256:
\path{d86dcb3daf13c9b2d5a0aaa4d72cce35a1aff48066ad69c7d9846b9d097dc354}.
Recovered from the automatically mounted conversation upload \path{02_Recent_Forward_Calculations.tex}. Its byte length and digest were checked against the provider header. The package includes the complete provider body, not the surrounding source-recovery collection or a guessed GitHub reconstruction. The operator, quotient, actual order, Gamma norm and polynomial definitions WCF1–WCF9 were inspected; this does not certify every downstream asymptotic in the complete provider.

## Primary external sources

National Institute of Standards and Technology. (n.d.). *NIST Digital Library of Mathematical Functions*, §§18.5, 18.9 and equation 18.23.7. Retrieved September 20, 2026.

<https://dlmf.nist.gov/18.5>
<https://dlmf.nist.gov/18.9>
<https://dlmf.nist.gov/18.23.E7>

Use: classical Rodrigues/binomial representation and recurrence for the shifted Legendre calculation; Meixner–Pollaczek generating-function context for the retained WCF and prior auxiliary-degree rate. The new coordinate identities are derived in the proof notes, not copied from a purported programme-specific DLMF theorem.

The Stacks Project Authors. (n.d.). *Lemma 48.25.5* (Tag 0C15); *Integral and finite morphisms* (Tag 03ZN). Retrieved September 20, 2026.

<https://stacks.math.columbia.edu/tag/0C15>
<https://stacks.math.columbia.edu/tag/03ZN>

Use: standard finite-flat local-complete-intersection/Gorenstein and finite/proper background. The precise rank-eight algebra, perfect pairing, trace factor and all local constants used here are proved explicitly; no general theorem is used to hide a missing coordinate map.

Zimmerling, J., Druskin, V., & Simoncini, V. (2025). *Monotonicity, bounds and extrapolation of Block-Gauss and Gauss-Radau quadrature for computing B^T phi(A) B* (Version 3) [Preprint]. arXiv:2407.21505.

<https://arxiv.org/abs/2407.21505>

Use: primary Gauss/Radau context cited by the new native-moment source. The abstract metadata were checked; this continuation does not claim a fresh complete reading of its full author source or import its finite-dimensional assumptions into the native measure problem. Track III contains its own finite orthogonality and residue derivation.

## New versus carried statements

New relative to the inspected snapshots: the positive-real ES slice with exact frame-rank loss; the trace/residue factorization by multiplication by `2 eta^3` and complete local residue-unit comparison; the explicit residue-to-native multiplier and arbitrary-frame defect as used in this programme; the improved interval inverse-trace margin; simultaneous correlated-parameter quotient/current formulas and their finite sign-certificate interface.

Carried and rechecked: the general odd determinant factor and earlier one-point repair, the fixed-prime order-48 signed group calculation, the prior Gauss residual degree bound, and the original four-dimensional polynomial/Jacobian identities. Classical mathematics is credited at use. No global priority claim is made for elementary linear algebra, quadrature, residue identities or representation-theoretic facts.
