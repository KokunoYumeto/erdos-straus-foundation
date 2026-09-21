# Independent audit of the Turn 7 optimality progression

## Determination

The optimality construction in `core.tex`, lines 342--424, is mathematically
valid.  It does construct, for every fixed positive integer \(u\nmid36\),
infinitely many hard primes carrying a proper relaxed middle-channel trace
source with word \(u\), while every same-word residual-divisor return fails.
The complementary middle word also has no such return.  A separate pair of
explicit integral Erdős--Straus solutions proves that none of these primes is
an Erdős--Straus counterexample.

One wording correction is required.  The tagged middle-channel denominator
triple \((jc,pjc,pj)\) is not increasing.  Its increasing permutation is
\((jc,pj,pjc)\).  The tagged orientation may and should remain in the source,
but it must not be called numerically ordered.  The same caution applies to any
general E/M output whose tuple order records a channel orientation rather than
denominator magnitude.

## Exact theorem

For a positive integer \(n\), put
\[
 K(n)=\prod_{\ell^r\parallel n}\ell^{\lceil r/2\rceil},
 \qquad
 B(n)=\prod_{\ell^r\parallel n}\ell^{\lfloor r/2\rfloor}.
\]
Fix \(u\nmid36\) and let \(m=4K(u)\).  There is a unit
\(b\in(\mathbb Z/m\mathbb Z)^\times\) such that
\[
 b\equiv1\pmod4,
 \qquad b^2\not\equiv1\pmod m.
\]
Choose distinct primes
\[
 \delta\equiv-b^2\pmod m,
 \quad
 \delta>\max\{u,u^2-3u+1,7\},
\]
and
\[
 t\equiv b^{-1}\pmod m,
 \quad t>\max\{u,7\}.
\]
Set
\[
 L=\operatorname{lcm}(840,m),\qquad R=\delta t^2,
\]
and choose a prime \(e\equiv3\pmod4\) with \(\gcd(e,LR)=1\).  The simultaneous
congruences
\[
 p\equiv1\pmod L,
 \qquad
 p\equiv\delta t-4u\pmod R,
 \qquad
 p\equiv-1\pmod e
\]
define a reduced residue class modulo \(LRe\).  Infinitely many primes \(p\) in
this class satisfy
\[
 p>\max\{R,e,B(u)R\}.
\]
For every such \(p\), with
\[
 a=\frac{p+R}{4},
\]
the record \((p,a,R,u,M)\) is a proper rational trace source.  Its reduced tail
denominator is \(d=t\), it has no same-word residual-divisor return, and its
middle complement \(u^*=a^2/u\) has no residual-divisor return either.  If
\(j=(\delta+1)/4\), the entire cofactor box
\[
 \{W:W\mid j^2,\ W\equiv u\pmod\delta\}
\]
is empty.  Nevertheless the same prime \(p\) has explicit positive integral
E- and M-channel Erdős--Straus solutions.

## Proof of the progression and source

Since \(u\nmid36\), the square image of
\((\mathbb Z/m\mathbb Z)^\times\) is nontrivial.  Hence a unit with
\(b^2\ne1\) exists; replacing \(b\) by \(-b\) if needed gives
\(b\equiv1\pmod4\) without changing \(b^2\).  The two required prime classes
are reduced, so Dirichlet's theorem gives \(\delta\) and \(t\) above any fixed
lower bound.  Their congruences give
\[
 \delta\equiv3\pmod4,
 \qquad t\equiv1\pmod4.
\]
Because \(\delta,t>u\), neither prime divides \(u\); because they exceed seven,
neither divides 840.  Thus \(\gcd(L,R)=1\).  The chosen \(e\) is coprime to
\(LR\), so \(L,R,e\) are pairwise coprime.

The middle CRT residue is a unit modulo \(R\): modulo either \(\delta\) or
\(t\), it is \(-4u\), and \(\gcd(4u,\delta t)=1\).  The other residues are
units modulo \(L\) and \(e\).  Therefore the combined residue class modulo
\(LRe\) is reduced, and Dirichlet gives infinitely many primes in it.  Removing
the finitely many primes below the displayed threshold preserves infinitude.
Since \(840\mid L\), each such prime has \(p\equiv1\pmod{840}\), one of the
programme's hard residue classes.

The auxiliary congruences give
\[
 R=\delta t^2\equiv(-b^2)(b^{-1})^2\equiv-1\pmod m.
\]
Since \(p\equiv1\pmod m\), one has \(p+R\equiv0\pmod m\).  Consequently
\(a\in\mathbb Z\), \(K(u)\mid a\), and hence \(u\mid a^2\).  The inequality
\(0<R<p\) gives
\[
 \frac p4<a=\frac{p+R}{4}<\frac p2.
\]
The residue of \(p\) modulo \(R\) is a unit, and
\(4a\equiv p\pmod R\); hence \(\gcd(pa,R)=1\) as required by the source
coordinates.

Let \(G_M(v)=p+4v\).  The CRT equation modulo \(R\) gives
\[
 G_M(u)\equiv\delta t\pmod{\delta t^2}.
\]
Therefore
\[
 \gcd(R,G_M(u))=\delta t,
 \qquad R\mid G_M(u)^2,
 \qquad R\nmid G_M(u),
\]
and the exact reduced tail denominator is
\[
 d=\frac{R}{\gcd(R,G_M(u))}=t>1.
\]
Thus this is a proper relaxed M trace source, not a full integer source.

## Completeness of the same-word failure

A target residual \(R'\mid R\) must divide \(G_M(u)\), must satisfy
\(R'\equiv3\pmod4\), and must preserve the original word budget
\[
 p+R'\equiv0\pmod m.
\]
Since \(\gcd(R,G_M(u))=\delta t\), the only target residuals satisfying the
first two requirements are \(R'=\delta\) and \(R'=\delta t\).  They fail the
budget exactly:
\[
 p+\delta\equiv1-b^2\not\equiv0\pmod m,
\]
and
\[
 p+\delta t\equiv1-b\not\equiv0\pmod m.
\]
The first nonzero statement is the choice of \(b\); the second follows because
\(b^2\ne1\) implies \(b\ne1\).  No residual divisor has been omitted, so the
same-word return set is empty.

For the complementary word \(u^*=a^2/u\), prime-by-prime valuation comparison
gives
\[
 K(u^*)=\frac{a}{B(u)},
 \qquad
 4K(u^*)=\frac{p+R}{B(u)}>R.
\]
The middle trace condition and its exact denominator are preserved.  Indeed,
using \(4a\equiv p\pmod R\),
\[
 4u\,G_M(u^*)
 =4up+16a^2
 \equiv p(p+4u)=pG_M(u)\pmod R.
\]
Both \(4u\) and \(p\) are units modulo \(R\), so
\[
 \gcd(R,G_M(u^*))=\gcd(R,G_M(u))=\delta t;
\]
in particular the complement is still proper and has \(d^*=t>1\).  Every
removal factor \(k\mid R\) satisfies \(1\le k\le R<4K(u^*)\).  The congruence
\(k\equiv1\pmod{4K(u^*)}\) therefore forces \(k=1\), which fails
\(d^*\mid k\).  The complementary return set is empty.

## Complete fixed-cofactor box

Put \(j=(\delta+1)/4\).  Since
\[
 \delta+1\equiv1-b^2\not\equiv0\pmod{4K(u)},
\]
one has \(K(u)\nmid j\), equivalently \(u\nmid j^2\).  The CRT equation gives
\(-p/4\equiv u\pmod\delta\).  Hence a cofactor-\(\delta\) word in the specified
box would be a divisor \(W\mid j^2\) satisfying \(W\equiv u\pmod\delta\).
The capacity lemma forces
\[
 \delta\le u^2-3u+1,
\]
contrary to the chosen strict bound.  This exhausts that fixed cofactor box; it
does not assert that every source over residual \(\delta\) is absent.

## Independent integral Erdős--Straus solutions

The congruence \(p\equiv-1\pmod e\) gives
\[
 c=\frac{p+1}{e}\in\mathbb Z_{\ge2},
 \qquad
 j_e=\frac{e+1}{4}\in\mathbb Z_{>0}.
\]
The E-channel state is
\[
 a_E=u_E=\frac{p+e}{4},quad R_E=e,quad
 (h_E,r_E,s_E,\kappa_E)=(a_E,1,1,c),
\]
with increasing denominators
\[
 (a_E,a_Ec,pa_Ec).
\]
Directly,
\[
 \frac1{a_E}+\frac1{a_Ec}+\frac1{pa_Ec}
 =\frac{pc+p+1}{pa_Ec}
 =\frac{c(p+e)}{pa_Ec}
 =\frac4p.
\]
The M-channel state is
\[
 a_M=j_ec,quad R_M=c+1,quad u_M=j_e,quad
 (h_M,r_M,s_M,\lambda_M)=(j_e,1,c,1),
\]
with tagged denominators \((j_ec,pj_ec,pj_e)\).  Its increasing permutation is
\((j_ec,pj_e,pj_ec)\), and
\[
 \frac1{j_ec}+\frac1{pj_ec}+\frac1{pj_e}
 =\frac{p+1+c}{pj_ec}
 =\frac{(e+1)c}{pj_ec}
 =\frac4p.
\]
Both distinguished denominators lie in the required first-half range.  For E,
\(p<4a_E=p+e<2p\).  For M,
\[
 4a_M=(e+1)c=p+c+1,
 \qquad
 p-(c+1)=(e-1)c-2>0.
\]
Thus every prime in the obstruction progression has two independently written
positive integral solutions and is not an Erdős--Straus counterexample.

## Concrete fixture

For \(u=8\), the package uses
\[
 m=16,\quad b=5,\quad\delta=71,\quad t=13,\quad e=11,
 \quad R=11999,\quad L=1680.
\]
The reduced progression is
\[
 p=48116881+221741520n.
\]
At its certified prime first term,
\[
 a=12032220,quad \gcd(R,p+32)=923=71\cdot13,quad d=13.
\]
The two endpoint solutions are
\[
 E:(12029223,52618973058426,2531860864994489889306),
\]
and, in tagged M orientation,
\[
 M:(13122786,631427532350466,144350643).
\]
Both reciprocal sums were recomputed exactly as \(4/48116881\).

As a second independent finite audit, the construction was generated for all
111 nonautomatic words \(u\le120\).  For every generated model, all divisors of
\(R=\delta t^2\), both middle orientations, and every divisor in the fixed
cofactor box were exhausted directly.  Every source, obstruction, complement
and cofactor assertion agreed with the proof above.

## Source and checker locators

- `core.tex`, lines 342--424: theorem and complete proof.
- `preprint.tex`, lines 107--136: shorter public proof.
- `verify.py`, lines 176--202 and 223--235: constructed progressions and the
  terminal fixture.
- `check_independent.py`, lines 149--175: independent CRT, cofactor, source and
  complement replay.
