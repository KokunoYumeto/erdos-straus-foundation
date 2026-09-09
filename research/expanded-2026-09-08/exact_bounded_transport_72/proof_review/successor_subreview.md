# Independent review of the arithmetic successors

Result: no mathematical error found in `bounded_transport.tex`, Theorem
`thm:shear`, Corollary `cor:family`, or
`connes_reading/connes_primitive_intersections.tex`, Theorem
`thm:connes-marked-successor`. Current line locators, scope-block hashes, source SHA256 values and the
complete computation counts are recorded in `successor_subreview.json`.
Only these successor results and their needed definitions were reviewed.
No manuscript file was edited.

## General adjacent shear: necessity, converse, and unique parameters

The standing hypotheses are \(p=12h+1\) prime, \(h>0\), and both

\[
a,a+1\in\{3h+1,\ldots,9h\},\qquad R=4a-p\ge3.
\]

Consequently \(a+1<p\), \(R\equiv3\pmod4\), and
\(\gcd(pa,p(a+1))=p\). If a passing primitive pair \((m,n)\) and
its \(L\)-image \((m+n,n)\) both belong to their respective divisor
supplies, then \(n\mid p\), so \(n=1\) or \(n=p\). In the latter
case primitivity gives \(p\nmid m\), hence \(p\nmid m+p\).
Divisibility \(m+p\mid p(a+1)\) then forces \(m+p\mid a+1\),
contradicting \(m+p>p>a+1\). Thus \(n=1\).

If \(p\mid m\), then \(p\nmid m+1\) and the same target divisibility
forces \(m+1\mid a+1\), contradicting \(m+1>p>a+1\). Thus

\[
m\mid a,\qquad m+1\mid a+1.
\]

The source and target marks are precisely

\[
R\mid m+1,\qquad R+4\mid m+2.
\]

Conversely these four divisibilities with \(n=1\) make both pairs
positive and primitive, put their coordinates in the correct divisor
supplies, and give both shell marks. This proves both directions without
enlarging a finite divisor supply.

Write \(m+1=Rk\). The target mark gives

\[
Rk+1\equiv0\pmod{R+4}
\iff 4k\equiv1\pmod{R+4}.
\]

Since \(R\equiv3\pmod4\), the integer \((R+5)/4\) lies strictly
between zero and \(R+4\) and is the inverse of \(4\) modulo \(R+4\).
All positive solutions are uniquely

\[
k=\frac{R+5}{4}+(R+4)t,\quad t\ge0,\qquad
m=\frac{R(R+5)}4-1+R(R+4)t.
\]

A negative \(t\) gives \(k<0\), and the smallest possible parameters
\(R=3,t=0\) give \(m=5>0\), so neither a missing zero solution nor a
positivity boundary occurs. Next \(a=mr\), and \(m+1\mid a+1\) gives

\[
r\equiv1\pmod{m+1},\qquad
r=1+c(m+1),\qquad a=m+c\,m(m+1),\quad c\ge0.
\]

Negative \(c\) would make \(r\le-m<0\). Conversely these formulas
give every displayed divisibility, with unique \(t,c\). The retained
condition that \(p=4a-R\) is a prime of the form \(12h+1\) is essential
and is not inferred from the parameter formulas. The theorem retains it.
The \(J\)-classification follows by the exact identity \(J=PLP\), where
\(P(m,n)=(n,m)\); positivity, coprimality, both divisor bounds and both
marks are invariant under \(P\).

## Explicit family and its smallest instance

For \(R=7,t=0\), one obtains

\[
m=20,\quad a=20+420c,\quad p=73+1680c,
\quad h=6+140c.
\]

The interval lower bound is \(3h+1=19+420c\le a\). Its upper bound
satisfies

\[
9h-(a+1)=33+840c>0.
\]

Also \(a=20(1+21c)\), \(a+1=21(1+20c)\), \(m+1=3\cdot7\), and
\(m+2=2\cdot11\). The family therefore has the asserted arithmetic
domain whenever its retained \(p\) is prime. At \(c=0\), testing
\(2,3,5,7\le\sqrt{73}\) proves primality, and reconstruction gives

\[
(20,4380,219),\qquad(21,3066,146).
\]

Their reciprocal sums are respectively \(240/4380=4/73\) and
\(168/3066=4/73\). No assertion of infinitely many prime specializations
is made or required by this corollary.

## Arithmetic-site marked successor and all its boundaries

For the group isomorphism \(H_{a^2}\to H_{(a+1)^2}\), the reciprocal
return formula is \(a^2/e\mapsto(a+1)^2/e\) with
\(e\mid\gcd(a^2,(a+1)^2)=1\). Thus the only return is

\[
u=a^2\longmapsto v=(a+1)^2.
\]

Every positive \(R\equiv3\pmod4\) has a prime divisor
\(q\equiv3\pmod4\). If \(R\mid4a^2+1\), then \(2a\pmod q\) would
have square \(-1\) and multiplicative order \(4\), forcing
\(4\mid q-1\), a contradiction. This excludes the source \(E\)-mark.
The identical argument applies to \(R+4\equiv3\pmod4\) at \(a+1\).

For the middle marks, \(\gcd(a,R)=1\), \(\gcd(a+1,R+4)=1\), and
\(\gcd(4,R(R+4))=1\) give the exact equivalences

\[
R\mid a^2+a\iff R\mid a+1\iff R\mid p+4,
\]

\[
R+4\mid(a+1)^2+(a+1)
\iff R+4\mid a+2\iff R+4\mid p+4.
\]

Since \(\gcd(R,R+4)=1\), their intersection is exactly
\(R(R+4)\mid p+4\). The map \(u\mapsto\mu_a(u)\) sends the two
endpoints to \((a,1)\) and \((a+1,1)\), giving the stated \(L\)-square.
The denominator formulas are integral because \(R\mid a+1\) and
\(R+4\mid a+2\), and positive because every factor is positive. Directly,

\[
\frac{R}{pa(a+1)}+\frac{R}{p(a+1)}=\frac{R}{pa},
\qquad
\frac{R+4}{p(a+1)(a+2)}+\frac{R+4}{p(a+2)}
=\frac{R+4}{p(a+1)}.
\]

Adding \(1/a\) or \(1/(a+1)\) proves the two required identities. With
\(p\) retained, the first denominator on the image identifies \(a+1\);
then \(a\), \(R\), \(u\), and the source triple are forced. Thus the
inverse and singleton-fibre claims are valid on the stated marked image.

For \(k=(p+4)/(R(R+4))\), positivity gives \(k>0\). Both numerator and
denominator are \(1\pmod4\), so uniquely \(k=4t+1\), \(t\ge0\).
Substitution yields exactly

\[
p=R(R+4)(4t+1)-4,\qquad
a=\frac{R(R+5)}4-1+R(R+4)t.
\]

Conversely retain \(R\ge3\), \(R\equiv3\pmod4\), \(t\ge0\), and
\(p\) prime with \(p\equiv1\pmod{12}\). The expression has \(p\ge17\),
so \(h=(p-1)/12\) is a positive integer. The displayed \(a\) is integral,
and

\[
a\ge\frac{p+3}{4}=3h+1.
\]

For the other boundary,

\[
2p-(R+7)=2R(R+4)(4t+1)-R-15
\ge2R^2+7R-15>0\quad(R\ge3).
\]

Hence \(a+1=(p+R+4)/4\le(3p-3)/4=9h\). Both shell restrictions
are therefore proved, not assumed. The initial numerical endpoint
\(R=3,t=0\) yields \(p=17\), which correctly fails the separately retained
\(p\equiv1\pmod{12}\) condition; it is not an omitted permitted shell.

## Exact comparison: the marked successor is the \(c=0\) subfamily

In the general shear classification the primitive pair is \((m,1)\).
Under the full middle-channel bijection its source and target divisors
are

\[
u=am,\qquad v=(a+1)(m+1).
\]

Their reciprocal indices in the two finite budgets are

\[
e=\frac{a^2}{u}=\frac am=1+c(m+1),\qquad
e'=\frac{(a+1)^2}{v}=\frac{a+1}{m+1}=1+cm,
\quad e-e'=c.
\]

The ordered-group isomorphism retains the index \(e\). For \(c>0\),
\(e>1\), \(e\mid a\), and \(\gcd(a,a+1)=1\); therefore
\(e\nmid(a+1)^2\). Its image of \(1/u\) is not the reciprocal of any
positive integer. For \(c=0\), \(e=e'=1\), \(m=a\), and the source
and target are exactly \(a^2,(a+1)^2\). Thus the marked successor is
precisely the \(c=0\) part of the general adjacent shear, and the
additional \(c>0\) cases are genuine shear returns with no integral
reciprocal return under this particular ordered-group isomorphism.
There is no conflict between the two classifications.

An explicit strict-inclusion case is \(p=1753,a=440,R=7,m=20,c=1,t=0\).
The pair \((20,1)\mapsto(21,1)\) gives

\[
(440,2313960,115698)\longmapsto(441,1546146,73626).
\]

Here \(u=8800\), \(v=9261\), \(e=22\), and \(e'=21\), while
\(1757\equiv63\pmod{77}\); the endpoint marked-successor domain does
not hold. Trial division by all primes at most \(\sqrt{1753}<42\),
namely \(2,3,5,7,11,13,17,19,23,29,31,37,41\), verifies that \(1753\)
is prime. The two exact rational identities were also independently
checked computationally.

## Independent finite verification

Direct enumeration covered all 63 primes \(p\equiv1\pmod{12}\) with
\(13\le p\le1753\), all 26,439 allowed adjacent shell pairs, and all
3,956 ordered passing source primitive divisor pairs in those shells.
For every source pair, target divisibility and target sum congruence for
both \(L\) and \(J\) were tested directly and compared with the theorem's
domain. There were four successful \(L\)-returns and four successful
\(J\)-returns. The \(L\)-returns occurred at \((p,a)=(73,20),(433,113),
(997,251),(1753,440)\). Exactly the first three are marked endpoint
successors. Exact rational arithmetic checked their reconstructed triples.

Separately, the complete grid \(R=3,7,\ldots,99\), \(0\le t\le9\),
\(0\le c\le5\) comprised 1,500 parameter candidates and 93 retained
prime specializations. All retained primes satisfied both shell bounds;
all candidates satisfied the divisor and sum formulas and the exact
\(c=0\) comparison of reciprocal returns. Finally, among \(0\le c\le30\)
the corollary has 18 prime specializations, and each pair of reconstructed
triples satisfied its exact rational identity.

These computations supplement the all-parameter algebraic review above.
They do not establish global occupancy or infinitude of the retained
prime family. No revision is required for the reviewed theorems.
