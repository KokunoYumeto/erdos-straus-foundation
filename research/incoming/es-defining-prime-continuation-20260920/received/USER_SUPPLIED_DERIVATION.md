The ES bridge lets the eight-state completion be tested at the **defining prime of an actual Erdős–Straus witness**. That produces a new arithmetic distinction:

$$
\boxed{
\begin{array}{ll}
\text{One denominator divisible by }p:
&
\widetilde{\mathscr E}_p/\mathscr E_p
\cong(\mathbb Z/p\mathbb Z)^2
\quad\text{on the separated residue stratum},\\[4pt]
\text{Two denominators divisible by }p:
&
\widetilde{\mathscr E}_p/\mathscr E_p
\cong
(\mathbb Z/p\mathbb Z)^2
\oplus(\mathbb Z/p^2\mathbb Z)^2
\oplus\mathbb Z/p^3\mathbb Z
\quad\text{on the separated residue stratum}.
\end{array}}
\tag{1}
$$

Here \(\mathscr E_p\) is the **original signed quartic algebra**, and \(\widetilde{\mathscr E}_p\) is its integral normalization. Both retain rank eight. I also calculate the complete answer when additional residue collisions occur.

The second case is particularly informative: **the integral signed fibre is nonreduced, although its normalized field factors are all unramified or split**. Thus ramification of a field extension, failure of an integral observation to be invertible, and loss of geometric point labels are three different phenomena, with explicit maps between them.

There is a corresponding advance in the complex metric calculation. On the ES prime–denominator collision, the algebraic splitting has a divergent Gram determinant, but the complete minimum over its original evaluation kernel cancels that divergence exactly. The four unregularized signed evaluations have covariance eigenvalues of orders

$$
\boxed{1,\quad |t|,\quad |t|^2,\quad |t|^3,}
\tag{2}
$$

with all four leading constants evaluated below in the fixed original Gamma-conductor metric.

I used the ES crosswalk at commit `2b5ab3b63471092624b4fcfac2ab2a0fbafa23a3`, the zeta workbench at `84d8f514c7df50b353a2aa1d039c485234c0a547`, and the complete preceding finite-completion manuscript. The ES source supplies the normalized prime–denominator quartic; the finite-completion source supplies the signed algebra. The normalization, integral invariant factors, ES-restricted gluing, and metric calculations below are the continuation.

## 1. Normalize the ES coefficient hypersurface without losing the prime at its boundary

For an original ES solution, retain

$$
\frac4p=\frac1x+\frac1y+\frac1z,
\qquad
S=p+x+y+z,
$$

and

$$
F(T)=-\frac1S(T-p)(T-x)(T-y)(T-z)
=AT^4+T^3+BT^2+CT+D.
$$

With

$$
s_1=x+y+z,\qquad s_2=xy+xz+yz,\qquad s_3=xyz,
$$

the exact coefficients are

$$
A=-S^{-1},\qquad
B=A(ps_1+s_2),\qquad
C=-5As_3,\qquad
D=Aps_3,
$$

and

$$
ps_2=4s_3,\qquad p=-\frac{5D}{C}.
$$

The ES workbench proves the coefficient equation

$$
625AD^3-125CD^2+25BC^2D-4C^4=0.
\tag{3}
$$

Its earlier inverse uses \(C\ne0\). At the defining prime of an integral witness, however, \(C\) and \(D\) both reduce to zero. The inverse therefore needs an actual extension rather than cancellation of the displayed denominator.

Let

$$
\mathscr S=
\mathbb C[A,A^{-1},B,C,D]\Big/
\bigl(625AD^3-125CD^2+25BC^2D-4C^4\bigr).
$$

Use \(P\) for the retained distinguished-root parameter, so that its arithmetic value will be \(p\). The normalization is

$$
\boxed{
\mathscr N=\mathbb C[A,A^{-1},P,W],
}
$$

with the exact map

$$
\boxed{
B=AW-P-AP^2,\qquad
C=-\frac54APW,\qquad
D=\frac14AP^2W.
}
\tag{4}
$$

The original symmetric data are recovered by

$$
s_1=-A^{-1}-P,\qquad s_2=W,\qquad s_3=PW/4.
$$

Thus the original reciprocal relation remains \(Ps_2=4s_3\).

To prove normalization, put

$$
R_0=\mathbb C[A,A^{-1},B,C].
$$

The parameter \(P\) satisfies the monic equation

$$
P^3+A^{-1}P^2+(B/A)P+\frac{4C}{5A}=0.
\tag{5}
$$

Both \(\mathscr S\) and \(\mathscr N\) are free of rank three over \(R_0\). In their respective bases

$$
(1,D,D^2),\qquad (1,P,P^2),
$$

the inclusion is exactly

$$
\boxed{
\operatorname{diag}\left(1,-\frac C5,\frac{C^2}{25}\right).
}
\tag{6}
$$

It is injective, finite, and becomes an isomorphism after inverting \(C\). The ring \(\mathscr N\) is a Laurent polynomial ring and hence normal. This proves the assertion.

More precisely,

$$
\boxed{
\mathscr N/\mathscr S
\cong R_0/(C)\oplus R_0/(C^2),
}
\tag{7}
$$

and its exact conductor ideals are

$$
\boxed{
\mathfrak c_{\mathscr S}=(C,D)^2,
\qquad
\mathfrak c_{\mathscr N}=C^2\mathscr N.
}
\tag{8}
$$

For the last statement, write an element of \(\mathscr S\) as

$$
a+C bP+C^2cP^2.
$$

Requiring its products with \(P\) and \(P^2\) to remain in \(\mathscr S\), using (5), forces \(a\) to be divisible by \(C^2\) and \(b\) by \(C\). Conversely, every element of \(C^2\mathscr N\) and every product of it with \(\mathscr N\) belongs to \(\mathscr S\).

This calculation identifies the exact information missing from the coefficient formula \(P=-5D/C\). At \(C=D=0\), the distinguished parameter is retained in the normalization and satisfies

$$
P(AP^2+P+B)=0.
$$

It is not recovered by assigning a value to \(0/0\).

The same formulas work over \(\mathbb Z[1/10,A^{-1}]\), so they are available at every hard prime considered below.

## 2. Every hard-prime witness has four distinct complex roots, but collides at its own prime

The six hard classes in the ES workbench all satisfy \(p\equiv1\pmod{12}\). The following argument applies to **every positive integral ES solution at such a prime**, rather than only the exterior states covered by the preceding crosswalk.

First, the denominators are distinct. If \(y=z\), set \(d=4x-p>0\). The ES equation gives

$$
dy=2px,\qquad 2dy=p(d+p),
$$

so \(d\mid p^2\). But \(d\equiv-p\equiv3\pmod4\), whereas every positive divisor of \(p^2\) is \(1\pmod4\), a contradiction.

No denominator equals \(p\). If \(x=p\), then

$$
(3y-p)(3z-p)=p^2.
$$

Both factors are positive and \(2\pmod3\), whereas every positive divisor of \(p^2\) is \(1\pmod3\).

Therefore

$$
\boxed{p,x,y,z\text{ are pairwise distinct}.}
\tag{9}
$$

Now reduce the original equation

$$
4xyz=p(xy+xz+yz)
\tag{10}
$$

at \(p\).

At least one denominator is divisible by \(p\). All three cannot be divisible by \(p\), since division by \(p\) would give

$$
4=\frac1X+\frac1Y+\frac1Z\le3.
$$

Moreover, each denominator divisible by \(p\) has valuation exactly one.

If only \(z\) is divisible, the right side of (10) has valuation one, so

$$
z=pZ,\qquad p\nmid Z.
$$

The divided equation gives

$$
\boxed{Z\equiv\frac14\pmod p.}
\tag{11}
$$

In particular, \(\nu_p(p-z)=1\).

If two denominators have valuations \(a<b\), valuation comparison in (10) gives \(b=1\), contradicting \(b>a\ge1\). Their valuations must therefore agree. If both were at least two, then \(y,z\ge p^2\), and

$$
\frac p4<x\le\frac{p^2}{4p-2}<\frac{p+1}{4},
$$

which contains no integer. Hence

$$
\boxed{
\text{Exactly one or two denominators are divisible by }p,
\text{ and every such valuation is }1.
}
\tag{12}
$$

Thus every actual hard-prime witness lies in the eight-point complex étale locus, while its defining-prime reduction necessarily has a repeated root. That repeated root is supplied by the arithmetic equation itself.

## 3. The complete integral normalization matrix

Assume first that \(p\nmid S\), so the literal coefficient \(A=-1/S\) is a \(p\)-adic unit. Write

$$
t_0=p,\quad t_1=x,\quad t_2=y,\quad t_3=z,
\qquad
f(T)=\prod_{i=0}^3(T-t_i).
$$

The integral signed algebra is

$$
\boxed{
\mathscr E_p=
\mathbb Z_p[T,\sigma]/
\left(f(T),\ \sigma^2-Af'(T)\right).
}
\tag{13}
$$

It is free of rank eight, with basis

$$
1,T,T^2,T^3,\quad
\sigma,\sigma T,\sigma T^2,\sigma T^3.
$$

This is the \(A\)-invertible chart of the preceding finite completion, not the original affine factor chart with \(a=1/\sigma\). The completion’s multiplication-trace convention is retained.

Define

$$
n_{ij}=\nu_p(t_i-t_j),\qquad
b_i=\sum_{j\ne i}n_{ij},
$$

$$
m_i=\left\lfloor\frac{b_i}{2}\right\rfloor,\qquad
\epsilon_i=b_i-2m_i\in\{0,1\},
$$

and retain the full unit

$$
u_i=p^{-b_i}Af'(t_i)\in\mathbb Z_p^\times.
$$

In the generic fibre,

$$
\mathscr E_p\otimes\mathbb Q_p
=
\prod_{i=0}^3
\mathbb Q_p[\sigma_i]/(\sigma_i^2-Af'(t_i)).
$$

Its integral normalization is

$$
\boxed{
\widetilde{\mathscr E}_p
=
\prod_{i=0}^3
\mathbb Z_p[\tau_i],
\qquad
\tau_i=\sigma_i/p^{m_i},
\qquad
\tau_i^2=p^{\epsilon_i}u_i.
}
\tag{14}
$$

Each factor is interpreted as a quadratic field algebra or a split quadratic algebra, as appropriate.

For completeness, no integral-basis theorem is being used without its local check. If \(x+y\tau_i\) is integral, its trace makes \(2x\) integral, hence \(x\in\mathbb Z_p\). Its square after subtracting \(x\) gives

$$
2\nu_p(y)+\epsilon_i\ge0,
$$

so \(y\in\mathbb Z_p\). Thus (14) is the full integral closure. Unit square roots and the decomposition into separated residue clusters use the ordinary Henselian lifting statements with \(p\ne2\) (The Stacks Project Authors, 2026, §10.153). ([The Stacks Project][1])

Let

$$
V=(t_i^j)_{0\le i,j\le3}.
$$

In the ordered normalization basis consisting first of its four constants and then its four \(\tau_i\), the inclusion is exactly

$$
\boxed{
\mathsf C_p=
\begin{pmatrix}
V&0\\
0&\operatorname{diag}(p^{m_i})V
\end{pmatrix}.
}
\tag{15}
$$

This evaluates the entire normalization map. The inverse over \(\mathbb Q_p\) is the corresponding labelled Lagrange interpolation, with the displayed powers of \(p\) retained.

Consequently,

$$
\boxed{
\begin{aligned}
\operatorname{length}_{\mathbb Z_p}
(\widetilde{\mathscr E}_p/\mathscr E_p)
&=
2\sum_{i<j}n_{ij}+\sum_i m_i\\
&=
3\sum_{i<j}n_{ij}
-\frac12\sum_i\epsilon_i.
\end{aligned}}
\tag{16}
$$

The exact trace-discriminant check is

$$
\nu_p(\det T_{\mathscr E_p})=6\sum_{i<j}n_{ij},
\qquad
\nu_p(\det T_{\widetilde{\mathscr E}_p})
=\sum_i\epsilon_i.
$$

Their difference is twice (16), as required by the squared determinant of (15). The trace here is multiplication trace, with the discriminant convention of The Stacks Project, §49.3. ([The Stacks Project][2])

### One \(p\)-divisible denominator: every invariant factor

Let

$$
z=pZ,\qquad p\nmid xyZ,\qquad n=\nu_p(x-y).
$$

The pair \(p,z\) has difference valuation one by (11), and its differences from \(x,y\) are units. Thus the complete Smith exponents of (15) are the multiset

$$
\boxed{
\{0,0,1,1\}
\ \cup\
\left\{
0,\left\lfloor\frac n2\right\rfloor,
n,n+\left\lfloor\frac n2\right\rfloor
\right\}.
}
\tag{17}
$$

An exponent zero denotes a unit invariant factor.

To prove (17), separate the two residue clusters by their unit resultant. For a two-root cluster whose gap has valuation \(n\), the ordinary evaluation matrix has Smith exponents \(0,n\). Its two derivative valuations both equal \(n\), so the odd evaluation block is multiplied by \(p^{\lfloor n/2\rfloor}\). This gives the second set in (17). The first set is the same calculation for \(n=1\).

In particular,

$$
\boxed{
\operatorname{length}
(\widetilde{\mathscr E}_p/\mathscr E_p)
=2+3n-(n\bmod2).
}
\tag{18}
$$

When \(x\not\equiv y\pmod p\), this is the first case of (1).

### Two \(p\)-divisible denominators: every invariant factor

Write

$$
y=pY,\qquad z=pZ,\qquad p\nmid xYZ.
$$

The exact reduced relation is

$$
Y+Z\equiv4YZ\pmod p.
\tag{19}
$$

The three scaled roots \(1,Y,Z\) cannot all coincide. If two coincide, there is only one closer pair: \(Y=Z\) forces \(Y=Z=1/2\), whereas \(Y=1\) forces \(Z=1/3\), and conversely.

Let

$$
n=\max\{\nu_p(p-y),\nu_p(p-z),\nu_p(y-z)\}\ge1,
\qquad
m=\left\lfloor\frac{n+1}{2}\right\rfloor.
$$

The other two differences within this three-root cluster have valuation one.

The full Smith exponents are

$$
\boxed{
0,\ 0,\ 0,\ 1,\ 1,\ m+1,\ n+1,\ n+m+1.
}
\tag{20}
$$

For the proof, the three-root Vandermonde has exponents

$$
0,\ 1,\ n+1.
$$

The normalization multipliers on its rows have exponents \(1,m,m\). The least valuations of its \(1\times1\), \(2\times2\), and \(3\times3\) minors are respectively

$$
1,\qquad m+2,\qquad n+2m+3.
$$

Its odd-block Smith exponents are therefore

$$
1,\ m+1,\ n+m+1.
$$

The isolated unit root \(x\) contributes two further unit factors. This proves (20), including all complementary directions.

Its length is

$$
\boxed{
3n+6-((n+1)\bmod2).
}
\tag{21}
$$

When \(1,Y,Z\) are distinct modulo \(p\), \(n=1\), giving the second case of (1).

In that case all three clustered derivative valuations are two. Thus all four normalized quadratic factors in (14) are unramified or split, even though the original integral fibre has a length-six nonreduced block.

### The \(p\mid S\) case is retained by an explicit chart change

When \(p\mid S\), the literal normalized coefficients are not all integral. Take the recorded shift \(\lambda=1\) and define

$$
F_\lambda(T)
=
-\frac1{S-4\lambda}
\prod_i[T-(t_i-\lambda)].
$$

Since \(p>3\), \(S-4\lambda\) is a unit. The root differences are unchanged, so (15)–(21) apply in this integral chart.

Its return to the original coefficient chart is

$$
\boxed{
F_\lambda(T)
=
\frac S{S-4\lambda}F_0(T+\lambda),
\qquad
\sigma_\lambda^2
=
\frac S{S-4\lambda}\sigma_0^2.
}
\tag{22}
$$

Both square-root choices and the translation are retained. This is an explicit alternative integral model, not a claim that the original nonintegral coefficients were units.

## 4. Actual hard-prime examples, including the boundary points

At the hard prime \(p=1201\), two exact positive solutions are

$$
( x,y,z )=(306,16218,1082101)
\tag{23}
$$

and

$$
( x,y,z )=(306,21618,61251).
\tag{24}
$$

The first is an original exterior state with

$$
h=17,\quad r=1,\quad s=18,\quad \kappa=53,
$$

$$
R=23,\quad u=17,\quad D_E=3,
\qquad
23\cdot53=1201+18.
$$

Its denominator formulas are precisely

$$
x=hrs,\qquad y=hs\kappa,\qquad z=phr\kappa.
$$

These are the retained Turn 7 coordinates, not another Egyptian-fraction parametrization.

The identities can be checked without numerical approximation:

$$
\frac1{16218}+\frac1{1082101}
=\frac{23}{306\cdot1201},
$$

and

$$
\frac1{18}+\frac1{51}=\frac{23}{306}.
$$

For (23), the normalized coefficient vector reduces to

$$
\boxed{(A,B,C,D)\equiv(410,100,0,0)\pmod{1201}.}
\tag{25}
$$

The colliding prime and divisible-denominator labels give the local algebra

$$
\boxed{
\mathbb F_{1201}[r,\sigma]/(r^2,\sigma^2-200r)
\cong\mathbb F_{1201}[\sigma]/(\sigma^4).
}
\tag{26}
$$

The normalization inclusion has six unit Smith factors and two factors \(1201\).

For (24),

$$
\boxed{(A,B,C,D)\equiv(522,0,0,0)\pmod{1201}.}
\tag{27}
$$

Here the prime and both divisible-denominator labels give

$$
\boxed{
\mathbb F_{1201}[r,\sigma]/(r^3,\sigma^2-3r^2),
}
\tag{28}
$$

of length six. Its normalization inclusion has exponents

$$
0,0,0,1,1,2,2,3.
$$

These are explicit critical boundary points of the finite completion: \(r=\sigma=0\), where its Jacobian \(2\sigma^3\) vanishes. The original affine factor map still has Jacobian \(-2\), and its missing integral lifts have

$$
a=1/\sigma.
$$

In the first example their \(p\)-adic valuation is \(-1/2\); in the second it is \(-1\).

The nilpotent actions are also different. In (26), multiplication by \(\sigma\) has one block of length four, while multiplication by \(r\) has two blocks of length two. In (28), multiplication by \(\sigma\) has blocks of lengths four and two, whereas multiplication by \(r\) has two blocks of length three.

More generally, in a multiplicity-\(m\) local block

$$
k[r,\sigma]/(r^m,\sigma^2-r^{m-1}u(r)),
\qquad u(0)\ne0,
$$

the ranks of multiplication by \(\sigma,\sigma^2,\sigma^3\) are

$$
m+1,\qquad2,\qquad1.
$$

Hence its complete Jordan list is

$$
\boxed{4,\underbrace{2,\ldots,2}_{m-2\text{ blocks}},}
\tag{29}
$$

while multiplication by \(r\) retains two length-\(m\) blocks.

### The original exterior cofactor determines a local quadratic field

There is a further arithmetic identification. For an original exterior state, put \(z=pZ\). When \(p\nmid S\),

$$
\frac{xy}{x+y}=\frac Z{D_E}
$$

holds exactly in the original \(h,r,s,\kappa\) coordinates. Together with \(Z\equiv1/4\pmod p\), it gives

$$
\boxed{
\frac{F'(p)}p\equiv-\frac3{16D_E}\pmod p.
}
\tag{30}
$$

For \(p\equiv1\pmod{12}\), \(-3\) is a square modulo \(p\): if \(\zeta\) is a primitive cube root in \(\mathbb F_p\), then \((2\zeta+1)^2=-3\). Hensel lifting therefore proves

$$
\boxed{
\mathbb Q_p\bigl(\sqrt{F'(p)}\bigr)
\cong
\mathbb Q_p\bigl(\sqrt{pD_E}\bigr).
}
\tag{31}
$$

The isomorphism multiplies by the actual lifted unit square root; it does not set that unit equal to one. The two factor signs remain distinct. ([The Stacks Project][1])

Thus the finite signed cover records the quadratic class of the **original exterior cofactor**. For (23), \(D_E=3\), and the prime-marked factor is a ramified quadratic field. For the separated two-divisible case, the normalized factors instead have even derivative valuations and are unramified or split.

## 5. Restricting the cover to ES gives a \(2+6\) decomposition with a calculable gluing defect

Over the smooth normalized ES parameter space, retain

$$
g(T)=T^3-s_1T^2+\frac{4s_3}{P}T-s_3,
\qquad
F(T)=A(T-P)g(T),
$$

and put

$$
R=g(P)=P^3-P^2s_1+3s_3.
$$

The signed algebra has two natural quotients:

$$
\mathscr E_P
=
B[\sigma]/(\sigma^2-AR),
$$

of rank two, and

$$
\mathscr E_g
=
B[T,\sigma]/
\bigl(g(T),\sigma^2-A(T-P)g'(T)\bigr),
$$

of rank six.

Their complete relation is

$$
\boxed{
0\longrightarrow\mathscr E
\longrightarrow\mathscr E_P\oplus\mathscr E_g
\longrightarrow
B/(R)[\sigma]/(\sigma^2)
\longrightarrow0.
}
\tag{32}
$$

The final arrow is the difference of the two restrictions. Equivalently, \(\mathscr E\) is their fibre product over the displayed length-two overlap.

This follows from the exact ideals

$$
(T-P)\cap(g)=((T-P)g),
\qquad
(T-P,g)=(T-P,R),
$$

applied separately to the even and odd polynomial parts. Thus the prime-marked and denominator-marked sectors split after \(R\) is inverted, but they have a retained gluing module at a prime–denominator collision.

The ordinary root Chinese-remainder matrix is

$$
\mathsf C_R=
\begin{pmatrix}
1&P&P^2&P^3\\
1&0&0&s_3\\
0&1&0&-4s_3/P\\
0&0&1&s_1
\end{pmatrix},
\qquad
\det\mathsf C_R=-R.
\tag{33}
$$

The signed comparison consists of two such blocks, with determinant \(R^2\).

If \(\Delta_g=\operatorname{disc}(g)\), the two trace determinants are exactly

$$
\boxed{
\det T_{\mathscr E}=256A^4R^6\Delta_g^3,
\qquad
\det T_{\mathscr E_P\oplus\mathscr E_g}
=256A^4R^2\Delta_g^3.
}
\tag{34}
$$

The factor \(R^4\) is the square of the comparison determinant. On \(\Delta_g\ne0\), the direct sum is the normalization near \(R=0\).

### The ES collision has a different extension from a transverse ambient collision

Suppose one denominator is \(P+t\), with the other two roots remaining distinct from \(P\). Locally,

$$
F=A\,x(x-t)h(P+x),\qquad x=T-P,\quad h(P)\ne0.
$$

Retain an analytic square root of the nonzero unit and set

$$
\zeta=\sigma/\sqrt{Ah(P+x)}.
$$

Then

$$
\zeta^2=2x-t,
$$

and the complete local algebra becomes

$$
\boxed{
B[\zeta]/(\zeta^4-t^2),
\qquad
x=\frac{\zeta^2+t}{2}.
}
\tag{35}
$$

Its normalization is the sum of

$$
\zeta^2=t,\qquad \zeta^2=-t.
$$

In the bases \((1,\zeta,\zeta^2,\zeta^3)\) and the two copies of \((1,\zeta)\), the comparison has determinant \(4t^2\) and Smith exponents

$$
0,0,1,1.
$$

Its cokernel is \((B/(t))^2\).

At \(t=0\), the original fibre is \(\mathbb C[\zeta]/(\zeta^4)\). Normalizing first and then specializing gives two copies of \(\mathbb C[\zeta]/(\zeta^2)\). The specialization map kills precisely

$$
\operatorname{span}\{\zeta^2,\zeta^3\}.
$$

The associated \(\operatorname{Tor}_1\) term retains those two directions in the specialized exact sequence.

The connection residue in the original four-dimensional extension is

$$
\boxed{0,\quad\tfrac12,\quad1,\quad\tfrac32,}
\tag{36}
$$

whereas the normalized extension has

$$
0,\quad0,\quad\tfrac12,\quad\tfrac12.
$$

Their trace difference is two, exactly

$$
t\,\partial_t\log\det\mathsf C=2.
$$

The integer parts in (36) therefore have a measured lattice meaning; discarding them changes the extension.

The ES-restricted geometric monodromy is correspondingly

$$
\boxed{
\left\{
(\epsilon,\pi):
\pi\in S_3\text{ fixes }P,\quad
\prod_{\alpha=0}^3\epsilon_\alpha=\operatorname{sgn}\pi
\right\},
\qquad\text{order }48.
}
\tag{37}
$$

The intrinsic prime prevents arbitrary permutation of all four root labels. Denominator collisions generate \(S_3\); a loop around \(R=0\) flips the signs at \(P\) and the colliding denominator without exchanging their labels. Those three pair flips generate the full eight-element even-sign subgroup. This proves (37), rather than simply restricting the number \(192\) by a dimension count.

## 6. Carry the gluing defect through the fixed original Gamma metric

The preceding ES bridge gives the fixed maps

$$
\Phi_*=(V_*^{\mathsf T})^{-1}K^{-1},
\qquad
\Psi_*=B_{v,*}(V_*^{\mathsf T})^{-1}K^{-1},
$$

with

$$
T_{\mathcal A,*}\Phi_*=\Psi_*.
$$

The period, quartet, conductor moments, and reference matrices remain fixed while the ES coefficients vary.

Use two copies of this actual four-dimensional receiving map:

$$
f_0(T)+\sigma f_1(T)
\longmapsto
\bigl(\Psi_*[f_0],\Psi_*[f_1]\bigr),
\qquad \deg f_i\le3.
\tag{38}
$$

Every algebra multiplication is transported by its full matrix under (38). It is not identified with multiplication by \(S'\) in the conductor target.

Let \(\mathcal H_\Gamma\) be the original monomial Gamma Gram on \(\mathcal P_3\), and put

$$
H_*=\Psi_*^*\mathcal H_\Gamma\Psi_*,
\qquad
v(r)=(1,r,r^2,r^3)^{\mathsf T}.
$$

Define its exact evaluation covariance

$$
K_*(r,s)=v(r)^{\mathsf T}H_*^{-1}\overline{v(s)}.
\tag{39}
$$

This is a fixed four-dimensional expression, and it can be evaluated without an unnamed inverse. Put \(b=s/2\), \(M=(2\pi)^{s/2}\), and retain the original target centre \(c_*\). Its four orthonormal polynomials are

$$
\begin{aligned}
\phi_0(S')&=M^{-1/2},\\
\phi_1(S')&=\frac{-i(S'-c_*)}{\sqrt{Mb}},\\
\phi_2(S')&=
-\frac{(S'-c_*)^2+b}{\sqrt{2Mb(b+1)}},\\
\phi_3(S')&=
\frac{i[(S'-c_*)^3+(3b+2)(S'-c_*)]}
{\sqrt{6Mb(b+1)(b+2)}}.
\end{aligned}
$$

If

$$
q_j(r)=v(r)^{\mathsf T}\Psi_*^{-1}[\phi_j],
$$

then

$$
\boxed{K_*(r,s)=\sum_{j=0}^3q_j(r)\overline{q_j(s)}.}
\tag{40}
$$

All source masses, centres, and conductor coefficients remain in these finite polynomials.

### The complete minimum cancels the splitting pole

Observe the prime coefficient pair

$$
f_0(P)=u,\qquad f_1(P)=v.
$$

The exact minimum in the metric (38) is

$$
\boxed{
\min\|f_0+\sigma f_1\|^2
=
\frac{|u|^2+|v|^2}{K_*(P,P)}.
}
\tag{41}
$$

Its minimum representatives are

$$
f_0(r)=u\,\frac{K_*(r,P)}{K_*(P,P)},
\qquad
f_1(r)=v\,\frac{K_*(r,P)}{K_*(P,P)}.
$$

The algebraic Chinese-remainder section instead uses

$$
e_P(r)=g(r)/R.
$$

Its exact excess is

$$
\boxed{
\left\|\Psi_*\frac gR\right\|_\Gamma^2
=
\frac1{K_*(P,P)}
+
\left\|
\Psi_*\left(
\frac gR-\frac{K_*(\,\cdot,P)}{K_*(P,P)}
\right)
\right\|_\Gamma^2.
}
\tag{42}
$$

The second term lies in the whole original evaluation kernel and is orthogonal to the minimum section.

For the two-column signed section, the determinant ratio is consequently

$$
\boxed{
\frac{\det G_{\mathrm{CRT}}}{\det G_{\min}}
=
\left[
\frac{
K_*(P,P)\,\|\Psi_*g\|_\Gamma^2
}{
|R|^2
}
\right]^2.
}
\tag{43}
$$

Thus the algebraic section has a fourth-order Gram-determinant pole as \(R\to0\), while the attained coefficient quotient (41) remains positive and finite. The pole is carried by the explicitly displayed kernel correction, rather than removed by a normalization convention.

### All four raw signed-evaluation eigenvalues

The raw point values are different observations:

$$
f_0(P)\pm\sigma_Pf_1(P),\qquad
f_0(P+t)\pm\sigma_{P+t}f_1(P+t).
$$

A unitary sum/difference transformation splits their covariance into

$$
2K_2,\qquad
2D_\sigma K_2D_\sigma^*,
$$

where

$$
K_2=
\begin{pmatrix}
K_*(P,P)&K_*(P,P+t)\\
K_*(P+t,P)&K_*(P+t,P+t)
\end{pmatrix}.
$$

Set

$$
K=K_*(P,P),
$$

$$
L=
\sum_j|q_j'(P)|^2
-\frac{\left|\sum_jq_j'(P)\overline{q_j(P)}\right|^2}{K}>0,
$$

and

$$
H_0=|A_0h(P)|.
$$

The strict positivity of \(L\) follows from independence of evaluation and derivative on \(\mathcal P_3\); explicitly,

$$
KL=\sum_{i<j}|q_i(P)q_j'(P)-q_j(P)q_i'(P)|^2.
$$

Since

$$
\sigma_P^2=-tA_0h(P)(1+O(t)),\qquad
\sigma_{P+t}^2=tA_0h(P)(1+O(t)),
$$

the four covariance eigenvalues are

$$
\boxed{
\begin{aligned}
\lambda_1&=4K(1+o(1)),\\
\lambda_2&=4H_0K\,|t|(1+o(1)),\\
\lambda_3&=L\,|t|^2(1+o(1)),\\
\lambda_4&=H_0L\,|t|^3(1+o(1)).
\end{aligned}}
\tag{44}
$$

The corresponding attained raw-value metric has their reciprocals.

This calculation can be realized on an explicit ES coefficient family:

$$
\boxed{
\left(
P;\ P+t,\ 2P,\
\frac{2P(P+t)}{5P+7t}
\right).
}
\tag{45}
$$

Its reciprocal sum is identically \(4/P\). At \(t=0\),

$$
H_0=\left|\frac{3P}{22}\right|.
$$

Thus even the local factor in (44) is explicit. The family is an algebraic ES family; it is not claimed to consist of integral witnesses for arbitrary \(t\).

The exact passage to retained jets is

$$
a_r=\frac{u_{r,+}+u_{r,-}}2,\qquad
b_r=\frac{u_{r,+}-u_{r,-}}{2\sigma_r},
$$

followed by

$$
\left(
a_P,\frac{a_{P+t}-a_P}{t},
b_P,\frac{b_{P+t}-b_P}{t}
\right).
\tag{46}
$$

Its determinant has modulus

$$
\frac1{4|\sigma_P\sigma_{P+t}t^2|}.
$$

The limiting jet covariance is two copies of the positive evaluation–derivative Gram. Its singular coordinate factors account exactly for the \(|t|^6\) covariance determinant in (44).

This completes the metric comparison between the coalescing signed points, their retained jet algebra, and the specified original Gamma-conductor receiver.

## 7. How this returns to the zeta workbench

The common arithmetic object is the rational signed algebra

$$
\mathscr E_{\mathbb Q}
=
\mathbb Q[T,\sigma]/(f,\sigma^2-F').
$$

It has two explicit base changes:

$$
\mathscr E_{\mathbb Q}\otimes_{\mathbb Q}\mathbb Q_p,
$$

with the integral normalization matrix (15), and

$$
\mathscr E_{\mathbb Q}\otimes_{\mathbb Q}\mathbb C
\xrightarrow{\ \Psi_*^{\oplus2}\ }
\mathcal P_3^{\oplus2},
$$

with the original Gamma metric and minimum calculations (41)–(46).

No \(p\)-adic valuation has been assigned to an unspecified transcendental period. The fixed complex conductor retains its nonzero moment \(\mu_v\), and its determinant remains the original one.

The newest zeta workbench also supplies a finite-prime theta transfer. At the same rational prime \(p\), its original multiplier is

$$
b_p(s)=1-p^{s-1}.
$$

At a stipulated zeta root \(\rho=1/2+\delta+i\gamma\),

$$
\boxed{
|b_p(\rho)|\ge1-p^{-1/2+\delta}>0.
}
\tag{47}
$$

For a full primary of order \(m\), its jet matrix retains the coefficients

$$
\frac{b_p^{(j)}(\rho)}{j!}
=
-\frac{p^{\rho-1}(\log p)^j}{j!},
\qquad j\ge1,
$$

and determinant \(b_p(\rho)^m\ne0\). These are exactly the source’s finite-prime multiplier and full-jet conventions.

Therefore the defining-prime degeneration calculated here does not manufacture a zero of the theta-transfer multiplier or of the weighted conductor. It instead supplies the missing arithmetic and metric accounting for the ES–Fable map: the complete integral cokernel, the retained collision algebra, the changed extension lattice, and the actual minimum that removes an algebraic-section pole.

The substantive new conclusions are equations (6)–(8), (15)–(21), (25)–(31), (32)–(37), and (41)–(46). They go beyond the previous eight-point count and generic discriminant calculation. In particular, they exhibit explicit singular integral points coming from an actual hard-prime witness and evaluate what survives after normalization and after the specified Gamma minimum.

These are written derivations. The execution tools timed out during this turn, so I am not attaching a new automated verification receipt or claiming that a new archive was generated. The growing-\(k\) RH projected-current phase and the independent proper-source target minimum are not assigned values from this fixed finite receiver.

[1]: https://stacks.math.columbia.edu/tag/04GE "Section 10.153 (04GE): Henselian local rings—The Stacks project"
[2]: https://stacks.math.columbia.edu/tag/0BVH "Section 49.3 (0BVH): Discriminant of a finite locally free morphism—The Stacks project"
