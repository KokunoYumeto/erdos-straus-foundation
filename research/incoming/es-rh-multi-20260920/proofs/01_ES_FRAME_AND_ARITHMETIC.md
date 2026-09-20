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
