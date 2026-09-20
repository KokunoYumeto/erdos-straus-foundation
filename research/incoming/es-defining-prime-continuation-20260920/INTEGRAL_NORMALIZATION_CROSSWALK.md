# Exact crosswalk to the original E/M integral completion

## Objects and bases

Let \(p\equiv1\pmod {12}\) be prime and let

\[
\frac4p=\frac1x+\frac1y+\frac1z
\]

be a positive integral witness with \(p\nmid S=p+x+y+z\). Retain the
literal roots

\[
t_0=p,\qquad t_1=x,\qquad t_2=y,\qquad t_3=z,\qquad
f(T)=\prod_{i=0}^3(T-t_i),\qquad A=-S^{-1}.
\]

The two packets use different letters for the same rank-eight order:

\[
\mathscr E_p
=\mathbb Z_p[T,\sigma]/(f,\sigma^2-Af')
=\mathbb Z_p[T,\eta]/(f,\eta^2-Af').
\]

The identification is the identity on \(T\) and sends
\(\sigma\mapsto\eta\). In both sources the ordered original basis is

\[
(1,T,T^2,T^3,\sigma,\sigma T,\sigma T^2,\sigma T^3).
\]

For

\[
b_i=\sum_{j\ne i}\nu_p(t_i-t_j),\qquad
m_i=\left\lfloor\frac{b_i}{2}\right\rfloor,\qquad
\epsilon_i=b_i-2m_i,
\]

put

\[
u_i=p^{-b_i}Af'(t_i),\qquad
\tau_i=\sigma_i/p^{m_i},\qquad
\tau_i^2=p^{\epsilon_i}u_i.
\]

The integral normalization in both presentations is

\[
\widetilde{\mathscr E}_p=\prod_{i=0}^3\mathbb Z_p[\tau_i].
\]

The complete inclusion matrix, from the displayed original basis to the
normalization basis consisting of the four constants followed by the four
\(\tau_i\), is

\[
\mathsf C_p=
\begin{pmatrix}
V&0\\
0&\operatorname{diag}(p^{m_i})V
\end{pmatrix},\qquad
V=(t_i^j)_{0\le i,j\le3}.
\]

Thus the comparison below is an equality of integral maps, not a comparison
of dimensions or a relabelling of two unrelated orders.

## Exterior channel: the general formula gives index \(p^2\)

In the separated exterior channel, exactly one denominator is divisible by
\(p\). Relabel it as \(z=pZ\). The prime equation gives
\(Z\equiv1/4\pmod p\), so

\[
\nu_p(p-z)=1.
\]

The other two denominators \(x,y\) are units. In the original E state they
are distinct modulo \(p\), so

\[
n=\nu_p(x-y)=0.
\]

The general two-cluster Smith formula is

\[
\{0,0,1,1\}\ \cup\
\left\{0,\left\lfloor\frac n2\right\rfloor,
n,n+\left\lfloor\frac n2\right\rfloor\right\}.
\]

Substitution of \(n=0\), with no deletion of unit factors, gives

\[
\boxed{(0,0,0,0,0,0,1,1).}
\]

Consequently

\[
\operatorname{length}_{\mathbb Z_p}
(\widetilde{\mathscr E}_p/\mathscr E_p)=2,\qquad
[\widetilde{\mathscr E}_p:\mathscr E_p]=p^2,
\]

and the torsion module is exactly

\[
\widetilde{\mathscr E}_p/\mathscr E_p
\cong(\mathbb Z_p/p)^2.
\]

This is the exterior statement labelled (IC18)--(IC20) in the integral
completion.

## Middle channel: the general formula gives index \(p^9\)

In the separated middle channel, write

\[
y=pY,\qquad z=pZ,\qquad
Y+Z\equiv4YZ\pmod p.
\]

The three scaled residues \(1,Y,Z\) are pairwise distinct in the original M
state. Hence every difference inside the cluster \(\{p,y,z\}\) has valuation
one. In the notation of the general three-root formula,

\[
n=1,\qquad m=\left\lfloor\frac{n+1}{2}\right\rfloor=1.
\]

Substitution in

\[
0,0,0,1,1,m+1,n+1,n+m+1
\]

gives

\[
\boxed{(0,0,0,1,1,2,2,3).}
\]

Therefore

\[
\operatorname{length}_{\mathbb Z_p}
(\widetilde{\mathscr E}_p/\mathscr E_p)=9,\qquad
[\widetilde{\mathscr E}_p:\mathscr E_p]=p^9,
\]

and

\[
\widetilde{\mathscr E}_p/\mathscr E_p
\cong
(\mathbb Z_p/p)^2\oplus
(\mathbb Z_p/p^2)^2\oplus
\mathbb Z_p/p^3.
\]

This is exactly the middle statement (IC19)--(IC20). The substantial index
does not imply ramification: here all three clustered derivative valuations
are two, so the normalized quadratic factors are unramified or split.

## Special fibres and the retained maps

For the exterior pair, translate the colliding root to \(r=0\). The reduced
local algebra has the exact form

\[
k[r,\sigma]/(r^2,\sigma^2-c r),\qquad c\in k^\times.
\]

The map

\[
k[r,\sigma]/(r^2,\sigma^2-c r)
\longrightarrow k[\sigma]/(\sigma^4),\qquad
r\longmapsto c^{-1}\sigma^2,\qquad
\sigma\longmapsto\sigma
\]

is an isomorphism. Its inverse sends the class of \(\sigma\) to \(\sigma\);
the defining relations give \(r=c^{-1}\sigma^2\) and
\(\sigma^4=c^2r^2=0\). This is the integral completion's E fibre, with its
original unit \(c=2g_0\) retained.

For the middle triple, the reduced local algebra is

\[
k[r,\sigma]/(r^3,\sigma^2-3r^2),
\]

which is literally the integral completion's M fibre after
\(\sigma\mapsto\eta\). Multiplication by \(r\) has two length-three blocks;
multiplication by \(\sigma\) has blocks of lengths four and two. These block
statements describe different endomorphisms of the same six-dimensional
algebra and are not substitutions for the Smith lattice calculation.

## Scope

The crosswalk proves that the \(p^2\) exterior defect and \(p^9\) middle defect
are the separated \(n=0\) and \(n=1\) instances of the full defining-prime
Smith classification. It does not turn a nonreduced special fibre into an
Erdős--Straus counterexample, and it does not identify an integral conductor
ideal with the fixed complex weighted conductor.
