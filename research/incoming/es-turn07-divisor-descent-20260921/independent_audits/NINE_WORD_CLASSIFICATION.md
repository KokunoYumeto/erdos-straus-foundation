# Independent audit: exact nine-word square-deletion classification

## Determination

The classification is correct under the source domain stated in `core.tex`.
For a fixed positive integer word (u), every **proper** E- or M-trace source
with that word has a same-word square-deletion return if and only if

\[
u\mid 36.
\]

The nine words are

\[
1,2,3,4,6,9,12,18,36.
\]

The word "automatic" must retain its universal meaning: the return is forced
for every proper source in the exact domain.  A word outside this list can
still descend for particular sources.  What fails outside the list is the
uniform guarantee.

## Exact source data needed by the argument

Let (p\equiv1\pmod 4) be prime, let (p/4<a<p/2) be an integer, and put

\[
R=4a-p.
\]

Retain a positive integer word (u\mid a^2).  Define

\[
K(n)=\prod_{\ell^e\parallel n}\ell^{\lceil e/2\rceil},
\qquad m=4K(u).
\]

For channel (c\in\{E,M\}), let (G_E=4u+1) and (G_M=p+4u).  A proper
trace source satisfies (R\mid G_c^2) and

\[
d=\frac{R}{\gcd(R,G_c)}>1.
\]

Primewise valuation gives (d^2\mid R).  Also (K(u)\mid a), and no prime
dividing (K(u)) divides either (p) or (R).  Therefore

\[
p+R=4a\equiv0\pmod m,
\qquad \gcd(pR,m)=1.
\]

The complete same-word divisor-removal condition is

\[
k\mid R,\qquad d\mid k,\qquad k\equiv1\pmod m.
\]

No weaker domain is used below.

## Square deletions and the square-image group

Write the exact square decomposition

\[
R=\delta t^2,
\qquad
\delta=\prod_{\ell^e\parallel R}\ell^{e\bmod2},
\qquad
t=\prod_{\ell^e\parallel R}\ell^{\lfloor e/2\rfloor},
\]

and put (q_0=K(d)).  Since (d^2\mid R), one has (q_0\mid t).
For (k=q^2), the two divisibility conditions are equivalent to

\[
q_0\mid q\mid t.
\]

Every such (q) is a unit modulo (m), because (q\mid t) and
(gcd(R,m)=1).  Thus the remaining return condition is exactly

\[
q^2\equiv1\pmod m.
\]

Let

\[
G_m=(\mathbb Z/m\mathbb Z)^\times,
\qquad H_m=\{x^2:x\in G_m\}.
\]

If (H_m=\{1\}), then every allowed (q), and in particular (q=q_0),
satisfies the congruence.  The return is

\[
k=q_0^2,
\qquad R'=\frac{R}{q_0^2},
\qquad a'=\frac{p+R'}4,
\qquad u'=u.
\]

Because the source is proper, (d>1), hence (q_0>1), so (a'<a).

## Exact computation of (H_m)

Factor

\[
m=2^\alpha\prod_{i=1}^r \ell_i^{e_i},
\qquad \alpha\ge2,
\]

with distinct odd primes (\ell_i).  The squaring map on each unit group is a
homomorphism.  For an odd prime power (\ell^e), the kernel has exactly two
elements.  Indeed, (x^2\equiv1\pmod{\ell^e}) gives
((x-1)(x+1)\equiv0\), while the two factors are coprime modulo the odd prime;
the whole prime power therefore divides one factor.  Hence (x\equiv\pm1).
Its square-image size is

\[
\frac{\ell^{e-1}(\ell-1)}2.
\]

For (2^\alpha), the image size is (1) for (\alpha=2,3), and
(2^{\alpha-3}) for (\alpha\ge4).  For (\alpha\ge3), the four square roots
of one are

\[
1,-1,1+2^{\alpha-1},-1+2^{\alpha-1}\pmod{2^\alpha};
\]

the unit group has order (2^{\alpha-1}).  The Chinese remainder theorem now
gives

\[
|H_m|=
2^{\max(0,\alpha-3)}
\prod_{i=1}^r\frac{\ell_i^{e_i-1}(\ell_i-1)}2.
\]

This product equals one exactly when (\alpha\in\{2,3\}), and the odd part is
either absent or is (3^1).  Since (4\mid m), this is exactly

\[
m\in\{4,8,12,24\},
\qquad\text{equivalently}\qquad m\mid24.
\]

As (m=4K(u)), this is (K(u)\mid6).  Write
(u=\prod\ell^{f_\ell}).  The definition of (K) shows that
(K(u)\mid6) exactly when no primes other than (2,3) occur and

\[
0\le f_2\le2,
\qquad 0\le f_3\le2.
\]

Therefore (u=2^i3^j) with (i,j\in\{0,1,2\}), which is equivalent to
(u\mid36) and gives exactly nine words.

| (u) | (K(u)) | (m=4K(u)) | (H_m) |
|---:|---:|---:|:---|
| 1 | 1 | 4 | \(\{1\}\) |
| 2 | 2 | 8 | \(\{1\}\) |
| 3 | 3 | 12 | \(\{1\}\) |
| 4 | 2 | 8 | \(\{1\}\) |
| 6 | 6 | 24 | \(\{1\}\) |
| 9 | 3 | 12 | \(\{1\}\) |
| 12 | 6 | 24 | \(\{1\}\) |
| 18 | 6 | 24 | \(\{1\}\) |
| 36 | 6 | 24 | \(\{1\}\) |

## Why no other word has the universal guarantee

Assume (u\nmid36).  Then (H_m\ne\{1\}), so choose a unit (b\pmod m)
with (b^2\not\equiv1\pmod m).  Replacing (b) by (-b) if needed gives
(b\equiv1\pmod4) without changing its square.

Dirichlet's theorem supplies arbitrarily large distinct primes

\[
\delta\equiv-b^2\pmod m,
\qquad t\equiv b^{-1}\pmod m.
\]

They can be chosen above seven and above all prime factors under discussion,
so they are coprime to (L=\operatorname{lcm}(840,m)).  Then

\[
\delta\equiv3\pmod4,
\qquad t\equiv1\pmod4,
\qquad R=\delta t^2\equiv-1\pmod m.
\]

Choose a prime (e\equiv3\pmod4) coprime to (LR).  The simultaneous class

\[
p\equiv1\pmod L,
\qquad p\equiv\delta t-4u\pmod R,
\qquad p\equiv-1\pmod e
\]

is reduced modulo (LRe): modulo each of (\delta,t), its middle residue is
(-4u), a unit.  CRT and Dirichlet therefore give infinitely many primes (p)
in this class, and they may be taken with (p>R).  Set (a=(p+R)/4).  Since
(p+R\equiv0\pmod m), the original word condition (u\mid a^2) holds.

For the M channel,

\[
p+4u\equiv\delta t\pmod R,
\qquad
\gcd(R,p+4u)=\delta t,
\qquad d=t>1.
\]

The gcd equality is exact: the middle congruence writes
(p+4u=\delta t+n\delta t^2=\delta t(1+nt)), and
(1+nt\equiv1\pmod t).  The factor (\delta) occurs only once in (R), so
no further factor of (R) enters the gcd.

Thus this is a proper M-trace source.  A square deletion satisfying the gate
would have residual (R'=\delta), hence deletion factor (k=t^2).  But its
word budget fails exactly:

\[
p+\delta\equiv1-b^2\not\equiv0\pmod m.
\]

Indeed, the only residual divisors of (R=\delta t^2) that are (3\pmod4)
are (\delta,\delta t,R).  The second also fails its word budget because

\[
p+\delta t\equiv1-b\not\equiv0\pmod m,
\]

and (R) fails the full gate.  Hence these sources have no same-word
residual-divisor return of any kind, and in particular no square-deletion
return.  This proves necessity without turning a bounded computation into an
unbounded assertion.

## Exact multiplicity inside the automatic class

For (u\mid36), every (q) with (q_0\mid q\mid t) works.  Writing
(T=t/q_0), the number of distinct square-deletion targets is therefore

\[
\tau(T)=
\prod_{\ell^e\parallel R}
\left(
\left\lfloor\frac e2\right\rfloor
-\left\lceil\frac{v_\ell(d)}2\right\rceil+1
\right).
\]

Different positive (q) give different (R'=R/q^2), hence different
distinguished denominators (a'=(p+R')/4).

## Corrections and qualifications for integration

1. The displayed factorization and product in `core.tex` lines 188--193 have a
   malformed odd-prime subscript.  It should be written, for example, as
   (m=2^\alpha\prod_{\ell\ \mathrm{odd}}\ell^{e_\ell}), with the product
   explicitly over the odd prime powers dividing (m).
2. The theorem needs the adjective **proper**.  If (d=1), then (q_0=1), and
   the chosen factor does not give strict descent.
3. The statement needs the full original-source hypotheses, especially
   (u\mid a^2), (R\mid G_c^2), and the unchanged-word modulus
   (m=4K(u)).  It is not a statement about arbitrary rational triples or an
   arbitrary modulus.
4. (H_m\ne\{1\}) does not mean every source for that word fails.  It means the
   congruence is not forced for all unit square factors.  The explicit
   CRT--Dirichlet family above is what proves failure of the universal property.
5. The nine-word positive statement can be vacuous at an individual
   prime/channel if no proper trace source exists there.  The theorem quantifies
   over sources that exist.  Finite source data in the package contains proper
   examples for each of the nine words, but those examples are not needed for
   the universal proof.
6. No part of this classification proves initial trace-source occupancy for
   every prime, and it does not prove the Erdős--Straus conjecture.

## Independent finite check

`enumerate_square_images.py` directly enumerates unit-square images for
(1\le u\le1000), without importing package code.  It also checks, for every
outside word in that range, the exact residue identities used by the obstruction
family: (R\equiv-1), (1-b^2\ne0), and (1-b\ne0\pmod m).
