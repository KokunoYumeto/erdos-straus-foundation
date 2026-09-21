# Dated proof bulletin — 21 September 2026

This bulletin indexes the proved Erdős–Straus divisor-descent results added on
21 September. Each item states its complete domain, maps, exceptions, proof
source, checks and nonclaims. It is a mathematical index, not a programme
chronology.

## SZ-20260921-001 — exact rational trace denominator and complete residual-divisor arrow

Fix a prime \(p\equiv1\pmod4\), an integer \(p/4<a<p/2\), and
\(R=4a-p\). Retain an original divisor word \(u\mid a^2\) and channel
\(c\in\{E,M\}\), with

\[
G_E=4u+1,\qquad G_M=p+4u,\qquad
K(n)=\prod_{\ell^e\parallel n}\ell^{\lceil e/2\rceil},
\qquad m=4K(u).
\]

The channel-labelled positive rational tails are

\[
E:\left(a,\frac{pa+a^2/u}{R},\frac{pa+p^2u}{R}\right),
\qquad
M:\left(a,\frac{p(a+a^2/u)}{R},\frac{p(a+u)}{R}\right).
\]

Their sum is integral exactly when \(R\mid G_c^2\). In that case both tails
have the same reduced denominator

\[
d=\frac{R}{\gcd(R,G_c)},\qquad d^2\mid R.
\]

Every positive same-channel return that retains \(p,u\) and replaces \(R\) by
one of its divisors is indexed by exactly

\[
\mathcal K_s=
\{k\in\mathbb Z_{>0}: k\mid R,\ d\mid k,\ k\equiv1\pmod m\},
\]

with

\[
F(s,k)=(p,a',R',u,c),\qquad
R'=\frac Rk,\qquad a'=\frac{p+R'}4.
\]

The target is an original positive integral ES state. If \(d>1\), every arrow
has \(k>1\) and \(a'<a\). With the source retained, the inverse parameter is
\(k=R/R'\).

For a fixed full target satisfying

\[
R'=4a'-p,\quad 3\le R'<p,\quad R'\equiv3\pmod4,\quad
u\mid(a')^2,\quad R'\mid G_c,
\]

the complete fibre consists of the positive integers

\[
1\le k\le\left\lfloor\frac{p-1}{R'}\right\rfloor,\qquad
k\equiv1\pmod m,\qquad R'k\mid G_c^2,\qquad R'k\nmid G_c.
\]

The global domain is the arrow set
\(\mathcal A=\{(s,k):k\in\mathcal K_s\}\). If one arrow
\(\alpha_t\in F^{-1}(t)\) is chosen for each hit target, then

\[
\ker F_*=
\bigoplus_t
\left\langle[\alpha]-[\alpha_t]:
\alpha\in F^{-1}(t)\setminus\{\alpha_t\}\right\rangle_{\mathbb Z},
\]

and the exact integral reconstruction is

\[
x\longmapsto(F_*x,x-sF_*x):
\mathbb Z^{(\mathcal A)}
\stackrel{\sim}{\longrightarrow}
\mathbb Z^{(\mathcal T_{\rm hit})}\oplus\ker F_*.
\]

- **Proof:** [complete trace, arrow and fibre proof](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L42-L201).
- **Independent derivation:** [divisor-descent equivalence audit, source and target spaces through the global fibre theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/DIVISOR_DESCENT_EQUIVALENCE.md#L28-L332).
- **Human lineage:** the inherited Type-I/II coordinates are those of Elsholtz and Tao, [Propositions 2.2 and 2.6](https://arxiv.org/pdf/1107.1010#page=12); the specialized formulas and arrow theorem are derived in the linked proof.
- **Strengthens:** [SZ-20260920-062](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/DAILY_RESULTS_20260920.md#sz-20260920-062--exact-rationality-boundary-of-the-trace-test) by classifying every integral return from its rational square-part residual.
- **Nonclaim:** the theorem does not force a trace source to exist at every prime.

## SZ-20260921-002 — square subdomain and the exact nine-word universal class

Write

\[
R=\delta t^2,\qquad
\delta=\prod_{\ell^e\parallel R}\ell^{e\bmod2},\qquad
q_0=K(d),\qquad T=t/q_0.
\]

The positive square deletion factors in \(\mathcal K_s\) are exactly

\[
k=q^2,\qquad q_0\mid q\mid t,\qquad q^2\equiv1\pmod m.
\]

For \(H_m=\{x^2:x\in(\mathbb Z/m\mathbb Z)^\times\}\), write

\[
m=2^\alpha\prod_{i=1}^r\ell_i^{e_i}
\]

with distinct odd primes \(\ell_i\). Then

\[
|H_m|=
2^{\max(0,\alpha-3)}
\prod_{i=1}^r\frac{\ell_i^{e_i-1}(\ell_i-1)}2.
\]

Consequently

\[
H_m=\{1\}
\Longleftrightarrow m\mid24
\Longleftrightarrow K(u)\mid6
\Longleftrightarrow u\mid36.
\]

Thus every proper E or M trace source has an automatic strict return at
\(k=K(d)^2\) exactly for the nine fixed words

\[
u\in\{1,2,3,4,6,9,12,18,36\}.
\]

The complete square-deletion family has

\[
\tau(T)=
\prod_{\ell^e\parallel R}
\left(
\left\lfloor\frac e2\right\rfloor
-\left\lceil\frac{v_\ell(d)}2\right\rceil+1
\right)
\]

distinct original targets.

- **Proof:** [square deletion and nine-word theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L233-L317).
- **Independent proof:** [square-image group and exact classification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/NINE_WORD_CLASSIFICATION.md#L62-L261).
- **Independent finite challenge:** [4,410-source and 17,635-safe-source audit](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/NINE_WORD_BRUTEFORCE.md#L47-L177).
- **Nonclaim:** a word outside the list can return at particular sources; what fails outside the list is the universal fixed-word guarantee.

## SZ-20260921-003 — integer coefficient multiplicities retain every labelled deletion

The complete divisor count is the coefficient

\[
|\mathcal K_s|=
\operatorname{coeff}_{[d^{-1}]}
\prod_{\ell^e\parallel R/d}
\left([1]+[\ell]+\cdots+[\ell^e]\right)
\quad\text{in }\mathbb Z[(\mathbb Z/m\mathbb Z)^\times].
\]

It is the pushforward of the labelled divisor module

\[
\pi_{R,d}:
\mathbb Z^{(\operatorname{Div}(R/d))}
\longrightarrow\mathbb Z[(\mathbb Z/m\mathbb Z)^\times],
\qquad e_v\longmapsto[v\bmod m].
\]

The group ring aggregates equal residues; it does not erase the retained
labelled certificate. The square subdomain has the analogous coefficient

\[
\operatorname{coeff}_{[q_0^{-2}]}
\prod_{\ell^e\parallel T}
\left([1]+[\ell^2]+\cdots+[\ell^{2e}]\right)
\quad\text{in }\mathbb Z[H_m].
\]

At

\[
p=1{,}108{,}801,\quad a=279{,}295,\quad
R=8{,}379,\quad u=5,\quad c=M,
\]

one has \(d=3\), \(m=20\), and the complete deletion set is

\[
\mathcal K_s=\{21,441\}.
\]

The two labelled witnesses are \(v=7,147\). Their pushforward is \(2[7]\),
which vanishes after reduction modulo two even though both integral targets
remain. This is one retained original word \(u=5\) with two distinct arrows,
not two source words.

- **Proof:** [coefficient maps and mixed-factor fixture](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L203-L409).
- **Figure:** [exact source map and mixed-factor fixture](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/figures/divisor_descent_map.pdf).
- **Correction:** coefficient reduction modulo two is not a replacement for the integer multiplicity or the labelled source module.

## SZ-20260921-004 — optimality: infinite proper sources without a same-word return

For every fixed \(u\nmid36\), put \(m=4K(u)\). Choose a unit
\(b\bmod m\) with \(b^2\ne1\) and \(b\equiv1\pmod4\). Dirichlet's theorem,
used only on reduced classes, supplies distinct primes

\[
\delta\equiv-b^2\pmod m,\qquad
t\equiv b^{-1}\pmod m,
\]

with

\[
\delta>\max\{u,u^2-3u+1,7\},\qquad t>\max\{u,7\}.
\]

Set \(R=\delta t^2\), \(L=\operatorname{lcm}(840,m)\), choose
\(e\equiv3\pmod4\) coprime to \(LR\), and take primes in the reduced CRT class

\[
p\equiv1\pmod L,\qquad
p\equiv\delta t-4u\pmod R,\qquad
p\equiv-1\pmod e,
\]

above \(\max\{R,e,B(u)R\}\). Then \(a=(p+R)/4\) is an original word source,
and

\[
\gcd(R,p+4u)=\delta t,\qquad d=t>1.
\]

The only possible residual divisors are \(\delta,\delta t,R\); the first two
fail the exact word budget because

\[
p+\delta\equiv1-b^2\ne0\pmod m,\qquad
p+\delta t\equiv1-b\ne0\pmod m,
\]

while \(R\) fails the full gate. For the middle complement \(u^*=a^2/u\),

\[
K(u^*)=\frac a{B(u)},\qquad 4K(u^*)=\frac{p+R}{B(u)}>R,
\]

and

\[
4u(p+4u^*)\equiv p(p+4u)\pmod R.
\]

Therefore the complement remains proper with the same exact denominator
\(t\), but no deletion factor can satisfy its larger budget. The inherited
capacity theorem also makes the specified cofactor-\(\delta\) box empty.

These primes are not ES counterexamples. With \(c=(p+1)/e\) and
\(j_e=(e+1)/4\), both

\[
E:\left(\frac{p+e}{4},\frac{p+e}{4}c,
p\frac{p+e}{4}c\right)
\]

and the channel-labelled middle tuple

\[
M:(j_ec,pj_ec,pj_e)
\]

have reciprocal sum \(4/p\) and satisfy the first-half range.

- **Proof:** [exact universal classification and CRT construction](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/core.tex#L440-L533).
- **Independent derivation:** [progression theorem through the explicit endpoint states](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/OPTIMALITY_PROGRESSION.md#L20-L237).
- **Human source:** Sutherland, [Theorem 18.1](https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf#page=1), for Dirichlet's theorem after reducedness is proved.
- **Depends on:** [SZ-20260920-041](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/DAILY_RESULTS_20260920.md#sz-20260920-041--sharp-finite-boundary-and-returned-grade-reduction).
- **Nonclaim:** the family proves that this descent predicate is not universal; its displayed endpoint states explicitly prevent promotion to an ES counterexample.

## SZ-20260921-005 — global arithmetic sign of the literal odd receiver

Let \(p\equiv1\pmod {12}\) be prime and let

\[
\frac4p=\frac1x+\frac1y+\frac1z
\]

be any positive integral witness. Retain the ordered literal roots
\(\ell=(p,x,y,z)\), put \(S=\sum_j\ell_j\), and define

\[
H(T)=-S^{-1}\prod_j(T-\ell_j)
=AT^4+T^3+BT^2+CT+D.
\]

For the exact coefficient polynomial \(F\) in the proof, put
\(\mathfrak N=S^6F\). Then

\[
\boxed{\mathfrak N<-\frac{125873811}{262144}p^8<0.}
\]

If \(p\equiv1\pmod {24}\), then the stronger bound is

\[
\boxed{\mathfrak N<-\frac{327448292668}{47045881}p^8.}
\]

The arithmetic proof first shows that the four literal roots are distinct and
that there is a unique smallest denominator \(a\) with \(p/4<a<p/2\). With
\(R=4a-p\), every witness lies in exactly one of the exterior or middle
factor-coordinate domains. In the exterior domain,

\[
-\frac{\mathfrak N}{p^8}
=\frac{P_E(u,w)}{2^{26}u^6w^8},
\qquad w=p/R,
\]

and the translated polynomial and its two exact derivative numerators each
have 221 positive coefficients. The arithmetic gate gives \(u\ge2\), or
\(u\ge5\) in the mod-\(24\) subdomain. In the middle domain, with
\(X=b-2\ge0\) and \(Y=c-b-1\ge0\), the comparison

\[
47045881H_M(X,Y)-327448292668L_M(X,Y)^6
\]

has zero constant and 191 positive nonconstant coefficients. Equality would
force \(a=6p/19\), which is impossible in the stated prime domain.

- **Proof:** [global theorem and complete arithmetic certificates](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex#L1-L346).
- **Executable certificates:** [ordinary/optimized replay receipt](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/verification.json).
- **Human lineage:** Elsholtz and Tao, [Type I and Type II parametrizations, Propositions 2.2 and 2.6](https://arxiv.org/abs/1107.1010); the specialized first-half reduction and sign certificates are derived in the linked proof.
- **Strengthens:** [SZ-20260920-053](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/49976b17491ba927df8bc7f2c2f81d39dfb15ce8/DAILY_RESULTS_20260920.md#sz-20260920-053--arithmetic-nonsingularity-on-3456-crt-classes) by replacing the sufficient three-character sieve with a theorem on the complete integral witness domain.
- **Nonclaim:** this theorem starts from an existing witness and does not prove that the E/M source set is occupied for every prescribed prime.

## SZ-20260921-006 — exact determinant phase and quantitative original inverse

Choose \(\xi_j\in\mathbb C^\times\) with
\(\xi_j^2H'(\ell_j)=1\). The original odd receiver has columns

\[
o_j=\xi_j
\begin{pmatrix}
1\\-iH'(\ell_j)\\
A H'(\ell_j)^2+2\ell_jH'(\ell_j)\\
i(7\ell_j^2H'(\ell_j)-13H'(\ell_j)^2)
\end{pmatrix}.
\]

Writing \(O=\mathsf C_HU\), \(U_{nj}=\ell_j^n\xi_j\), and

\[
\epsilon=A^2\prod_{i<j}(\ell_j-\ell_i)\prod_j\xi_j\in\{1,-1\},
\]

the exact identities are

\[
\det\mathsf C_H=\frac{4F}{A},
\qquad
\det U=\frac\epsilon{A^2},
\qquad
\det O=-\frac{4\epsilon\mathfrak N}{S^3}.
\]

If \(c\) denotes the applicable constant from SZ-20260921-005, then

\[
\boxed{|\det O|>\frac{4cp^8}{S^3}},
\qquad
\boxed{\|O^{-1}\|_2<\frac{360S^9}{cp^8}}.
\]

Here \(\|\cdot\|_2\) is the operator norm for the standard Hermitian norm on
\(\mathbb C^4\). The proof keeps every root label and square-root sign. It
uses the displayed coefficient matrix, an exact Lagrange inverse,
\(2/S\le|H'(\ell_j)|\le S^2\), row bounds
\((\sqrt{S/2},S,3S^2,20S^3)\), and a \(360S^6\) bound for every
\(3\times3\) cofactor.

- **Proof:** [coefficient reduction, determinant phase, Lagrange inverse and cofactor bound](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex#L155-L424).
- **Typed-map record:** [domains, inverses, fibres, signs, metrics and information loss](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/MORPHISMS.md).
- **Nonclaim:** no unordered-root norm or altered receiving metric is substituted, and receiver invertibility is not an occupancy theorem.

## SZ-20260921-007 — unique collision-free singularity in the exact real counterdomain

On \(3\le t\le4\), set

\[
p=1,\qquad b=t,\qquad c=t+\frac1{10},
\qquad a=\frac{bc}{4bc-b-c},
\qquad D=40t^2-16t-1.
\]

Then \(1/a+1/b+1/c=4\), the four literal roots are positive and distinct,
and exact elimination gives

\[
\mathfrak N(t)=\frac{P(t)}{100000D^6},
\]

where \(P\) is the degree-18 integer polynomial displayed in the proof. All
18 coefficients of \(P'(3+X)\) are positive. Therefore there is exactly one
receiver singularity on this family, and it satisfies

\[
\boxed{\frac{3053}{1000}<t_0<\frac{1527}{500}},
\qquad
t_0\approx3.05367681075890.
\]

The tail gap is \(1/10\), so the family does not enter the middle integral
cone; both raw exterior words are below the exterior cone. This is an exact
counterdomain to an unrestricted positive-real nonvanishing claim and is
compatible with SZ-20260921-005.

- **Proof:** [exact polynomial, derivative certificate, bracket and domain exclusions](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/core.tex#L425-L488).
- **Separate recheck:** [algebraic, arithmetic, certificate and counterdomain audit](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6bdfce25724b95a4b30e97f0df69879a87793302/research/incoming/es-turn07-global-receiver-determinant-20260921/independent_audits/MATHEMATICAL_RECHECKS.md).
- **Nonclaim:** the real singularity is not an integral Erdős--Straus witness and is not an ES counterexample.
