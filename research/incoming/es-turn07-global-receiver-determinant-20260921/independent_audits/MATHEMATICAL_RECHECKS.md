# Separately tasked mathematical rechecks

These rechecks were carried out independently of the supplied prose before the
module was integrated. They are model-assisted mathematical reviews, not human
peer review. The executable checks named below are the durable computational
certificates.

## Receiver determinant and inverse

Writing (V=\prod_{i<j}(\ell_j-\ell_i)), direct reduction of the four receiver
component polynomials modulo (H) gives

\[
\mathsf C_H=\operatorname{diag}(1,-i,1,i)M,
\]

with

\[
M=\begin{pmatrix}
1&0&0&0\\
C&2B&3&4A\\
AC^2-9D&4ABC-8AD-7C&4AB^2-16A^2D-2AC-5B&4AB-8A^2C-3\\
20D/A-13C^2&20C/A+76D-52BC&20B/A+5C-52B^2+208AD&20/A-66B+104AC
\end{pmatrix}.
\]

The recheck obtained

\[
\det M=4F/A,
\qquad
\det U=\epsilon/A^2,
\qquad
\epsilon=A^2V\prod_j\xi_j\in\{1,-1\},
\]

and hence

\[
\det O=4\epsilon F/A^3=-4\epsilon\mathfrak N/S^3.
\]

For four distinct positive integral roots,

\[
2/S\le |H'(\ell_j)|\le S^2.
\]

The four row-entry bounds are

\[
\sqrt{S/2},\quad S,\quad3S^2,\quad20S^3.
\]

Hadamard's inequality gives at most (360S^6) for every (3\times3)
cofactor and at most (1440S^6) for the Frobenius norm of the adjugate. With
the determinant lower bound this yields the stated Hermitian operator-norm
estimate.

## Complete arithmetic domain

The arithmetic recheck proved directly that every denominator is greater than
(p/4), no denominator equals (p), and no two denominators coincide when
(p\equiv1\pmod {12}). It then proved that every witness has a unique smallest
denominator (a) with

\[
p/4<a<p/2.
\]

With (R=4a-p), the factors

\[
X=Ry-pa,qquad Z=Rz-pa
\]

are positive and satisfy (XZ=p^2a^2). The only possible valuation pairs are
((0,2),(2,0)) in the exterior channel and ((1,1)) in the middle channel.
The ordered inverses

\[
u=\frac{a^2}{Ry-pa}\quad(E),
\qquad
u=\frac{pa^2}{Ry-pa}\quad(M)
\]

were rederived, together with (a=hrs), (u=hr^2), ((r,s)=1), the exact
return maps, and the two gates. The character calculation was checked with a
Jacobi symbol modulo the possibly composite (R) and a Legendre symbol modulo
(p). It gives (u\ge2) in the exterior channel and (u\ge5) when
(p\equiv1\pmod {24}). Ordering middle tails as (pb<pc) gives
(b\ge2) and (c-b\ge1).

## Polynomial certificates

The exterior recheck reproduced the bidegree ((12,16)) polynomial and the
full (13\times17) support of each translated array. Each array has 221
positive coefficients. It also obtained

\[
\Phi(2)=\frac{125873811}{262144},
\qquad
\Phi(5)-\frac{327448292668}{47045881}
=\frac{57438937891281016903}{602187276800000}>0.
\]

The middle recheck reproduced all 192 coefficients of (H_M) and the
comparison polynomial with zero constant and 191 positive nonconstant
coefficients. Its two first-degree coefficients are

\[
[X]Q_M=43131132079353572408,
\qquad
[Y]Q_M=48523283252689726776.
\]

The independent program checks the exterior identity on the complete
(17\times17) unisolvent grid and the middle identity on the complete
(25\times17) grid, after proving the displayed bidegree bounds.

## Examples, singular counterdomain and scope

The exact (p=1009) exterior and middle witnesses and the (p=944329) middle
witness were recomputed, including the stated receiver numerators and
(p)-adic valuations (0,2,2). A separate enumeration reproduced the complete
(p\le3000), (p\equiv1\pmod {12}) census:

\[
99\text{ primes},\quad34287\text{ shells},\quad868359\text{ words},
\quad2451\ E\text{ states},\quad2054\ M\text{ states}.
\]

The valuation histogram is

\[
(E,0):2447,qquad(E,1):4,qquad(M,2):2054.
\]

For

\[
p=1,qquad b=t,qquad c=t+\tfrac1{10},
\qquad a=\frac{bc}{4bc-b-c},qquad3\le t\le4,
\]

exact elimination gives the degree-18 polynomial in `core.tex`. Every
coefficient of (P'(3+X)) is positive, so it has exactly one receiver
singularity in

\[
3053/1000<t_0<1527/500.
\]

The roots stay distinct. The gap (1/10) excludes the middle integer domain,
and the two exterior words lie below its proved cone. Finally, the raw
((1009,321,275,9)) source was checked to have a nonsingular rational frame
but a failed exterior divisibility gate (275\nmid37). These controls confirm
the exact scope: the theorem makes every existing integral witness nonsingular;
it does not create a witness at an unoccupied prime.

## Executable replay

`run_all.py --bound 3000 --directory reproduced/normal` completed in ordinary
and optimized Python. The main program recorded 48,542 checks per mode; the
separately implemented checker recorded 30,245 checks per mode. Every
mathematical JSON output was byte-identical across interpreter modes. See
`verification.json` for command lines, hashes and result identities.
