# Typed morphisms

## 1. Exterior source to ordered denominators

- Domain: actual Turn 7 exterior states `(p;h,r,s,kappa,R,D)` satisfying every original positivity and divisibility gate.
- Codomain: ordered positive ES solutions `(p;x,y,z)`.
- Map: `(x,y,z)=(hrs,hs kappa,phr kappa)`.
- Inverse on the image: `R=4x-p`, `u=xz/(py)=x^2/(Ry-px)`, `D=(4u+1)/R`, `v=x^2/u`, followed by the gcd normalization in the TeX.
- Kernel/information loss: none on the stated ordered image.

## 2. Ordered denominators to normalized quartic

- Domain: ordered nonzero solutions `(p;x,y,z)`.
- Codomain: the coefficient chart `(u0,u2,u3,u4)` with fixed `U^3V` coefficient one.
- Map: `-(p+x+y+z)^{-1} product(U-tV)` over `t in {p,x,y,z}`.
- Fibre: algebraically quotients the three denominator labels by `S3`; on the strict exterior chamber sorting recovers `x<y<z`.
- Retained marking: `p=-5u4/u3`.
- Image equation: `625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0` on `u0u3u4 != 0`.

## 3. Normalized quartic to the signed Fable fibre

- Domain: the distinct-root arithmetic image.
- Codomain: `P^{-1}(J4)` for the polynomial map `P:C^4 -> C^4` stated in the TeX.
- Fibre: exactly eight points, two for each root, with all four source coordinates explicit.
- Prime-marked subfibre: the two choices `lambda^2=-(p+x+y+z)/((p-x)(p-y)(p-z))`.
- Deck map: the rational involution `Sigma`; it exchanges the two signs over each fixed root.

## 4. Reciprocal-cubic suspension

- Domain: the reciprocal cubic with roots `p/x,p/y,p/z` and sum four.
- Codomain: the hyperplane `u0=0` in the same quartic target.
- Map: multiplication by the retained factor `V` with fixed normalization.
- Fibre: seven points for distinct denominators: two over each finite root and one infinity-chart point.
- Information loss: denominator order and common scale unless separately retained.
- Exceptional locus: the entire image lies in the `u0=0` component of the nonproper locus. This is different from Morphism 2.

## 5. Literal quartic to reciprocal suspension

- Domain: the normalized literal quartic \(H_{\rm ES}\), together with its
  intrinsic marked root \(p=-5u_4/u_3\), on \(u_4\ne0\).
- Codomain: the reciprocal suspension \(H_{\rm rec}\) with finite roots
  \(p/x,p/y,p/z\) and the distinguished root at infinity.
- Map:
  \[
  H_{\rm rec}(U,V)=u_4^{-1}\frac{V}{U-V}H_{\rm ES}(pV,U).
  \]
  The factor \(U-V\) cancels the image of the marked root \(p\); the factor
  \(V\) inserts infinity.
- Projective root map: \([U:V]\mapsto[pV:U]\), followed by the stated
  deletion/insertion. With \(p\) retained, the inverse sends
  \(t_i\mapsto x_i=p/t_i\), restores the marked root \(p\), and restores the
  normalized literal quartic.
- Coefficient fibre without \(p\): exactly the common scale
  \((p,x,y,z)\mapsto(\lambda p,\lambda x,\lambda y,\lambda z)\).
- Signed fibres: their exact fibre product has fourteen points. The direct
  signed lift is obstructed by the displayed derivative-twist square class;
  after its quadratic trivialization the projective correspondence is
  \(8\)-to-\(8\), while the affine reciprocal chart forgets exactly the prime
  sign.

## 6. Fixed conductor square

- Domain and codomain: the Fable coefficient/source space, the fixed exponential-polynomial four-plane `U_*`, and fixed polynomial receiver `W_*`.
- Maps: `Phi_*=(V_*^T)^{-1}K^{-1}`, `Psi_*=B_{v,*}(V_*^T)^{-1}K^{-1}`, and the original conductor restriction `T_A,*`.
- Identity: `T_A,* Phi_*=Psi_*`.
- Kernels: all zero.
- Nonlinear conjugates: `P_U,*=Phi_* P Phi_*^{-1}` and `P_W,*=Psi_* P Psi_*^{-1}`.
- Information loss: none after the coefficient target has been formed.
- Nonidentity retained: `Psi_*` is a receiving isomorphism, not the conductor.

## 7. Root-algebra interpolation

- Domain: `C[T]/product(T-t_j)` for four distinct ES roots and a chosen bijection to four fixed reference roots.
- Codomain: `C[S]/product(S-rho_j)`.
- Map: evaluation at `t_j` followed by Lagrange interpolation at `rho_j`.
- Kernel: zero; inverse is the opposite evaluation/interpolation map.
- Choice: depends on the root bijection.
- Stronger projective map: exists exactly when the corresponding cross ratios agree up to relabelling; cross-ratio mismatch is the exact obstruction, not a claim of unrelatedness.

## 8. Raw-cell to Lorentz transport

- Domain: the ordered raw-cell vector space with basis
  \((E_{11},E_{12},E_{21},E_{22})\).
- Codomain: the ordered Lorentz coordinate space \((T,X,Y,W)\).
- Map:
  \[
  \Phi_\triangle=
  \begin{pmatrix}
  5/8&0&3/4&5/8\\
  0&1&0&0\\
  3/8&0&5/4&3/8\\
  1/2&0&0&-1/2
  \end{pmatrix}.
  \]
- Inverse:
  \[
  \Phi_\triangle^{-1}=
  \begin{pmatrix}
  5/4&0&-3/4&1\\
  0&1&0&0\\
  -3/4&0&5/4&0\\
  5/4&0&-3/4&-1
  \end{pmatrix}.
  \]
- Kernel and fibre: zero kernel and singleton fibres because
  \(\det\Phi_\triangle=-1/2\).
- Spatial projection: \((T,X,Y,W)\mapsto(X,Y,W)\) forgets the \(T\)-coordinate.
  On the four stated transported vertices it yields the exact tetrahedron with
  face edges \(2\sqrt3\), apex edges \(\sqrt{65}/4\), volume \(\sqrt3/4\), and
  face-centroid displacement \((0,1/4,0)\).

## 9. ES coefficient chart to the odd receiving divisor

- Domain: \(X_{\rm ES}^{\rm ord}=\{ps_2=4s_3,\,
  (p+s_1)ps_3\Delta\ne0\}\).
- Codomain: the distinct-root coefficient chart
  \(\mathbb A^4_{A,B,C,D}\), followed by \(\mathbb A^1\).
- Map:
  \[
  \Theta(p,s_1,s_2,s_3)=
  \left(-\frac1{p+s_1},
  -\frac{ps_1+s_2}{p+s_1},
  \frac{ps_2+s_3}{p+s_1},
  -\frac{ps_3}{p+s_1}\right),
  \qquad \mathfrak D_{\rm odd}\circ\Theta.
  \]
- Pullback: with \(T=s_1/p\), \(Z=s_3/p^3\),
  \[
  \mathfrak D_{\rm odd}\circ\Theta
  =\frac{p^2\Phi(T,Z)}{(1+T)^6},
  \]
  where \(\Phi\) is the explicit primitive irreducible polynomial EZ45.
- Fibre and information: at the ordered-root level, \(\Theta\) forgets only
  denominator relabelling through the symmetric sums. On the symmetric chart,
  the intrinsic-prime inverse recovers \(p,s_1,s_2,s_3\).
- Divisor meaning: \(\Phi(T,Z)=0\) is exactly the loss locus of the odd
  receiving matrix after pullback; it is not identified with a zeta-zero
  divisor.

## 10. Rational ES shape to integral and prime-numerator solutions

- Domain: positive rational \((T,Z)\in V(\Phi)\) for which
  \(X^3-TX^2+4ZX-Z\) splits into three distinct positive rational roots
  \(a_1,a_2,a_3\), none equal to \(1\).
- Codomain: positive integral ordered ES solutions.
- Map: if \(L\) is the common denominator of the reduced \(a_i\), choose
  \(p\in L\mathbb Z_{>0}\) and set \(x_i=pa_i\).
- Inverse: \((p;x_1,x_2,x_3)\mapsto(T,Z;a_i=x_i/p)\).
- Fibre over one rational shape: all positive scales \(p\in L\mathbb Z_{>0}\).
  The prime-numerator subfibre is nonempty exactly when \(L=1\) or \(L\) is
  prime.
- Exceptional loci: repeated roots, nonpositive roots, the root \(1\), and
  irrational splitting are excluded exactly as stated in EZ48. The proved
  positive-real intersection does not establish a rational point.

## 11. Fixed-input rank-\(2+6\) decomposition

- Domain: the fixed-\(p\) coefficient base
  \(A C d_p\operatorname{Disc}(g_p)\ne0\).
- Codomain: the product of the marked rank-two signed algebra and the
  denominator rank-six signed algebra in EZ61.
- Map: Chinese-remainder projection using
  \(e_p(r)=g_p(r)/g_p(p)\).
- Inverse: sum of the two idempotent inclusions.
- Kernel: zero.
- Boundary: \(g_p(p)=0\) is the collision of the marked root with a
  denominator root; \(\operatorname{Disc}(g_p)=0\) is a denominator collision.
- Group action: monodromy has order \(48\); deck reversal acts independently
  on the rank-two and rank-six components.

## 12. Finite collision completion

- Domain: the signed inverse algebra
  \(\mathcal E[\xi]/(\xi^2h_u'-1)\).
- Codomain: the localization at \(\eta\ne0\) of
  \(\widehat{\mathcal S}=\mathcal E[\eta]/(\eta^2-h_u')\).
- Map: \(\eta=\xi h_u'=\xi^{-1}\).
- Inverse: \(\xi=\eta^{-1}\).
- Kernel: zero on the localization.
- Added fibre: at an \(m\)-fold root, the complete local algebra is
  \(\mathbb C[\varepsilon,\eta]/
  (\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1})\).
- Information retained: multiplicity and nilpotent length.
- Information not repaired: the infinity chart \(A=0\), and the
  meromorphic \(\eta^{-1}\) pole of the original first source coordinate.

## 13. Local ES to paired-root algebra map

- Domain: the length-four local algebra of the rational ES family
  \((p;p,2p/5,2p)\), with
  \(\eta_{\rm ES}^2=(3p/11)\varepsilon_{\rm ES}\).
- Codomain: one length-four local algebra at
  \(r_\pm=1/2\pm i\gamma\), with
  \(\eta_{\rm pair}^2=4\gamma^2\varepsilon_{\rm pair}\).
- Map:
  \(\varepsilon_{\rm ES}\mapsto\varepsilon_{\rm pair}\) and
  \(\eta_{\rm ES}\mapsto c\eta_{\rm pair}\), where
  \(c^2=3p/(44\gamma^2)\).
- Inverse: the same map with \(c^{-1}\).
- Intertwining: centred multiplication is preserved; uncentred
  multiplication has the exact translation \(p-r_\pm\).
- Nonidentity retained: this does not map the full global fibres, native
  metrics, or zeta zeros.

## 14. Marked odd-moment factorization

- Domain: the ordered signed-root cover with labels \(r_j\) and
  \(\xi_j^2h_u'(r_j)=1\).
- Intermediate carrier: the weighted Vandermonde matrix
  \(U=(r_j^k)\operatorname{diag}(\xi_j)\), with
  \(\det U=\pm A^{-2}\).
- Codomain: the original odd evaluation matrix \(O\).
- Map: \(O=V_hU\), where the rows of \(V_h\) are the ascending coefficient
  vectors of the four reduced component polynomials.
- Inverse of the carrier: the complete Lagrange formula EZ80.
- Information loss: exactly the kernel of \(V_h\); \(U\) has none.
- Descent: \(U\) lives on the marked cover, while the divisor
  \(\det O=0\iff\det V_h=0\) is invariant on the unmarked squarefree base.

## 15. Original signed order to its integral normalization

- Base: (mathbb Z_p), with the ordered literal roots
  (t_0=p,t_1=x,t_2=y,t_3=z) and (p\nmid S).
- Domain:
  (mathscr E_p=mathbb Z_p[T,\sigma]/(f,\sigma^2-Af')), in the retained
  ordered polynomial/signed basis.
- Codomain: the direct sum of the four normalized quadratic factors in their
  retained bases.
- Inclusion matrix:
  [
  \mathsf C_p=\operatorname{diag}
  \bigl(V,\operatorname{diag}(p^{m_i})V\bigr),
  \]
  where (V=(t_i^j)) and
  (m_i=\lfloor\sum_{j\ne i}v_p(t_i-t_j)/2\rfloor).
- Kernel: zero.
- Cokernel: the Smith factors printed in SZ-20260920-050; on the separated E
  and M strata they are respectively
  ((\mathbb Z/p)^2) and
  ((\mathbb Z/p)^2\oplus(\mathbb Z/p^2)^2\oplus\mathbb Z/p^3).
- Information loss after tensoring with (mathbb Q_p): the finite cokernel is
  killed.  Its length is retained before that base change.

## 16. Translated defining-prime chart to the original chart

- Base ring before descent:
  (K(q)), where (K=\mathbb Q_p) and
  (q^2=c_\lambda=S/(S-4\lambda)).
- Domain: the translated signed algebra with coordinates
  ((T_\lambda,\sigma_\lambda)).
- Codomain: the original signed algebra with coordinates
  ((T_0,\sigma_0)).
- Map:
  [
  T_\lambda\longmapsto T_0-\lambda,
  \qquad \sigma_\lambda\longmapsto q\sigma_0.
  ]
- Inverse:
  (T_0\mapsto T_\lambda+\lambda),
  (sigma_0\mapsto q^{-1}\sigma_\lambda).
- Kernels: zero in both directions.
- Descent obstruction: the square class of (c_\lambda) in
  (K^\times/K^{\times2}).  Without its triviality there is no asserted
  (K)-isomorphism between these presentations.

## 17. Fixed-prime rank-(2+6) integral gluing map

- Domain: the original fixed-prime order (mathscr E_p).
- Codomain: the product (mathscr E_p^{(2)}\oplus\mathscr E_p^{(6)}) of
  the marked-root and denominator sectors.
- Map: the two restriction homomorphisms.
- Difference map from the product: subtract their restrictions to
  (B/(R)[\sigma]/(\sigma^2)).
- Exact sequence:
  [
  0\longrightarrow\mathscr E_p\longrightarrow
  \mathscr E_p^{(2)}\oplus\mathscr E_p^{(6)}\longrightarrow
  B/(R)[\sigma]/(\sigma^2)\longrightarrow0.
  ]
- Kernel of the first map: zero.  Cokernel of the first map: the displayed
  overlap algebra of length two.
- Collision normalization: (B[\zeta]/(\zeta^4-t^2)) maps to the two
  quadratic branches; its normalization inclusion has Smith exponents
  ((0,0,1,1)), and specialization has kernel
  ((\zeta^2,\zeta^3)).

## 18. Arithmetic receiving numerator and character exclusion

- Domain: every positive integral ES witness at a fixed prime
  (p\equiv1\pmod {12}).
- Codomain: (mathbb Z), followed by reduction in the retained local
  valuation stratum.
- Map: the exact numerator (N=S^6F), with
  (det O=4\chi N/S^3).
- Type-I images: either the E2 term with discriminant (-511), or the retained
  diagonal term with discriminant (1241).
- Type-II image: exact valuation two and residual discriminant (-15).
- Consequence: if all three Legendre symbols are (-1), none of the possible
  images is zero, so (O) is invertible.
- Nonconverse: a character value (+1) only removes this exclusion; it is not
  a map to a singular witness and has no singularity conclusion.

## 19. Original signed fibre, quadratic base extension and nonsquare twist

- Integral source: the normalized signed algebra of the witness
  ((13;4,18,468)), reduced modulo (q=61).
- Original cover:
  (mathscr S_1: \eta_1^2=h'(r)).
- Twist:
  (mathscr S_2: \eta_2^2=2h'(r)).
- Base extension: adjoining (w) with (w^2=2).
- Isomorphism over (mathbb F_{61^2}):
  ((r,\eta_1)\mapsto(r,w\eta_1)), with inverse
  ((r,\eta_2)\mapsto(r,w^{-1}\eta_2)).
- Rational fibres: (mathscr S_1(mathbb F_{61})) is empty and
  (mathscr S_2(mathbb F_{61})) has eight points; both have eight geometric
  points over the quadratic extension.
- Frobenius: (w\mapsto-w), giving four disjoint transpositions on the
  original cover.  The resulting finite-fibre zeta function belongs to this
  finite scheme and is not a morphism to the Riemann zeta function.
