# Independent review of raw scale and hit incidence

Status: passed after repair. All four statements have been reviewed in full, both definition findings are resolved, and no mathematical finding remains open. Their initial history remains below.

Reviewed input: raw_scale_hit_incidence.tex, together with the referenced definitions and proofs in bounded_transport.tex, unary_boolean_transport.tex and input_output_incidence.tex.

Initial SHA256: b9cd215ee8fb36ccb7f00f579f71f1d691f5b00f67f333d89a3f44dd30c7f888.

Subsequent pre-repair SHA256: a36bd9dab2c5ad64c45495d329fa45291e7b4a870ce8ea4572158d0e9212b3e4.

The accompanying JSON records the final source hash and every theorem label. No main-source edit was made by this subreview.

The repaired source explicitly types the bit coordinate, defines the total hit indicator on each decoded shell, and gives the generic full-to-PCT recoding formula on the full code's own first-half domain. It also explicitly identifies the source orientation \((d,e)=(d_z,d_y)\) and the original reconstruction orientation \((d_y,d_z)\); their change is the involution \((r,s)\mapsto(s,r)\) on the exact positive locus \(rs=S^2\), with singleton fibres.

## Definition findings

RS-001. The initial domain said “all positive integer \((A,B,C,D,\varepsilon)\), \(\varepsilon\in\{0,1\}\).” Read literally, positivity of every tuple coordinate excludes zero, contrary to the exterior channel and the displayed \(\varepsilon=0\) fixture. Required exact repair: \(A,B,C,D\in\mathbb Z_{>0}\) and \(\varepsilon\in\{0,1\}\). This changes no intended arithmetic map; it states its complete domain.

Resolution: the final source states exactly the requested domain; both tags now belong to the written domain.

RS-002. The initial definition of the total indicator \(\chi_H\) referred to the three displayed tests of the fixed seed, which used \(a_q,R_q,A_0,B_0\). The surrounding proof correctly intended each arbitrary code to determine its own shell. Required exact repair: for decoded \((j,A,B,\varepsilon)\), explicitly define

\[
a(c)=\frac{q+4j+3}{4},\quad R(c)=4j+3,\quad S(c)=qa(c),
\]
\[
\chi_H(c)=[AB\mid a(c)]\,[\gcd(A,B)=1]\,
[R(c)\mid A+q^{1-\varepsilon}B].
\]

The full-range hit restriction must likewise use its own decoded shell \(2a(c)\le q-1\). The ray-specific coordinate \(a_q\) is recovered when the candidate is that ray's hit, and remains fixed only for that specified hit. This makes the total selector and the full-to-PCT map explicitly typed on their entire finite domains.

Resolution: the final source gives \(R(c)=4j(c)+3\), \(a(c)=(q+R(c))/4\), all three tests on \(A(c),B(c),\varepsilon(c)\), and the full code's own \(a(c_F)=(q+4j+3)/4\). Its first-half restriction is explicitly \(2a(c_F)\le q-1\), and its recoding is explicitly \(c_F\mapsto(A-1)\Lambda_H+(q-1)j+2(B-1)+\varepsilon\). This resolves both the total indicator and generic map domains.

## thm:raw-scale-fibre

Retain \(p=12h+1\) prime, \(h\ge1\), \(a=ABD\in\{3h+1,\ldots,9h\}\), and the raw equation

\[
4ABCD=A+p^{1-\varepsilon}B+pC.
\]

Since \(A,B\le ABD=a<p\), the positive integer \(k=\gcd(A,B)\) satisfies \(k<p\), hence \(\gcd(k,p)=1\). Reduction of the equation modulo \(k\) gives \(k\mid pC\). Choose integers \(r,s\) with \(rk+sp=1\); multiplying by \(C\) proves \(k\mid C\). Thus

\[
A_0=A/k,\quad B_0=B/k,\quad C_0=C/k,\quad D_0=k^2D
\]

are positive integers, \(\gcd(A_0,B_0)=1\), and the exact raw residual is \(k\) times the residual at \((A_0,B_0,C_0,D_0,\varepsilon)\). Conversely any such coprime tuple and any positive \(k\) with \(k^2\mid D_0\) give positive raw coordinates \((kA_0,kB_0,kC_0,D_0/k^2,\varepsilon)\), residual zero, and gcd exactly \(k\). The two compositions recover all five original coordinates and the scale. There is no further constraint on the scale: the first denominator is identically \(A_0B_0D_0\), already in the original range. Prime factorization gives the full scale fibre and its cardinality:

\[
0\le v_\ell(k)\le\lfloor v_\ell(D_0)/2\rfloor,\qquad
\#\{k:k^2\mid D_0\}=\prod_{\ell\mid D_0}
(\lfloor v_\ell(D_0)/2\rfloor+1).
\]

The empty product at \(D_0=1\) is one, corresponding to \(k=1\).

Every scale cancels in the displayed original monomials:

\[
ABD=A_0B_0D_0,\quad B^2D=B_0^2D_0,
\]
\[
p^\varepsilon ACD=p^\varepsilon A_0C_0D_0,\qquad
pBCD=pB_0C_0D_0.
\]

Consequently \(R=4a-p\), \(S=pa\), and every residual \(4vw-p(v+w)\) of two specified denominators are exactly unchanged with their labels. The original equation gives \(RC=A+p^{1-\varepsilon}B\). Hence, with \(y=p^\varepsilon ACD\) and \(z=pBCD\),

\[
Ry-S=p^\varepsilon A^2D,\qquad
Rz-S=p^{2-\varepsilon}B^2D.
\]

The signs and orientations agree with the displayed ordered witness. Moreover

\[
\gcd(a,u)=\gcd(ABD,B^2D)=BD\gcd(A,B)=kBD=B_0D_0.
\]

The quotients \((B+p^\varepsilon C)/A\), \((A+pC)/B\), and the product \(BCD\) retain their exact values after substitution. The affine parameters satisfy \(\Omega=k\Omega_0\), \(\Theta=k\Theta_0\), so their numerator at each specified \(q\) is multiplied by \(k\), rather than silently identified.

Finally \(y/z=A_0/(p^{1-\varepsilon}B_0)\). This is reduced: coprimality handles \(B_0\), while \(A_0\le a<p\) excludes the prime \(p\) from \(A_0\). Its exact residual quotient is \(C_0\), because \(A_0+p^{1-\varepsilon}B_0=RC_0\). This checks every asserted retained coordinate and the complete inverse.

## thm:raw-scale-period

Fix the same coprime seed, including its original \(D_{0,p}\), and put

\[
K_0=4A_0B_0C_0,\quad
\Theta_0=C_0+(1-\varepsilon)B_0,\quad
\Omega_0=A_0+\varepsilon B_0.
\]

These are positive integers. The seed equation gives
\(K_0D_{0,p}=\Omega_0+p\Theta_0\). Therefore, for every integer \(q\), without any positivity or primality assumption needed for these algebraic assertions,

\[
D_0(q)=D_{0,p}+\frac{(q-p)\Theta_0}{K_0}.
\]

Writing \(g_0=\gcd(K_0,\Theta_0)\), \(m_0=K_0/g_0\), \(w=\Theta_0/g_0\) gives \(\gcd(m_0,w)=1\). Thus \(D_0(q)\in\mathbb Z\) exactly when \(m_0\mid q-p\). For a retained seed scale \(k^2\mid D_{0,p}\), the same argument with denominator \(k^2K_0\) gives

\[
D_k(q)\in\mathbb Z
\iff m_k\mid q-p,\quad
m_k=\frac{k^2K_0}{\gcd(k^2K_0,\Theta_0)}.
\]

The equality \(D_0(q)=k^2D_k(q)\) holds as rational numbers, so membership in \(k^2\mathbb Z\) gives the asserted equivalence even at a nonintegral primitive value. No divisibility predicate is applied to a rational number without that membership interpretation.

For each prime \(\ell\), \(\gcd(m_0,w)=1\) implies
\[
\min(2v_\ell(k)+v_\ell(m_0),v_\ell(w))
=\min(2v_\ell(k),v_\ell(w)).
\]
This proves \(\gcd(k^2m_0,w)=\gcd(k^2,w)\), including primes dividing either operand to arbitrary multiplicity. Hence
\[
\frac{m_k}{m_0}=\frac{k^2}{\gcd(k^2,w)}.
\]
This positive integer divides \(k^2\), proving exactly the raw-return subprogression. Since \(p\equiv1\pmod{12}\), the intersection with \(q\equiv1\pmod{12}\) and \(q\ge p\) is bijective to \(t\in\mathbb Z_{\ge0}\) by
\(q=p+\operatorname{lcm}(12,m_k)t\); the inverse is the displayed quotient of \(q-p\). All primality and output tests remain predicates on those integers.

For \(q\ge p>0\), every returned integral coefficient is positive. Substitution in the original denominator formulas proves the exact witness equality and the reciprocal identity. At a returned prime \(q\equiv1\pmod{12}\),
\[
\frac{a_q}{q}
=\frac{\Theta_0}{4C_0}+\frac{\Omega_0}{4C_0q}
>\frac14.
\]
The right side is decreasing in \(q>0\), because \(\Omega_0>0\). At \(q\ge p\) it is at most \(a_p/p\le 3/4-3/(4p)\le3/4-3/(4q)\). For integer \(a_q\) and \(q=12h_q+1\), these inequalities give exactly \(3h_q+1\le a_q\le9h_q\). The first denominator stays in the full original shell interval.

At an integral primitive return \(q\), a seed scale returns precisely when its square divides both \(D_{0,p}\) and \(D_0(q)\). Thus its complete fibre is the square-divisor set of their displayed gcd, with no other scale excluded or admitted.

## thm:raw-first-half-code

The exact formula \(a_q=(\Omega_0+q\Theta_0)/(4C_0)\), with \(C_0>0\), gives
\[
2a_q\le q-1
\iff q(2C_0-\Theta_0)\ge\Omega_0+2C_0.
\]
The right-hand constant is strictly positive. If the coefficient of \(q\) is nonpositive, no positive input passes. If it is positive, the integral threshold is exactly the stated ceiling. A seed passing at \(p\) continues to pass at all \(q\ge p\). Raw scales retain \(a_q\), so this gate is scale invariant.

For \(q=12h_q+1\), the first-half digit ranges are
\[
M_H=6h_q,\quad J_H=3h_q,\quad
0\le j<J_H,\quad1\le A,B\le M_H,\quad\varepsilon\in\{0,1\}.
\]
Every digit tuple determines the integer \(a(c)=3h_q+j+1\) and \(R(c)=4j+3\). The inner digit \(2(B-1)+\varepsilon\) is bijective to \(0,\ldots,2M_H-1\); the next digit \(j\) is bijective to the possible quotient on division by \(2M_H=q-1\); and the outer digit \(A-1\) is bijective to the quotient on division by \(\Lambda_H=2M_HJ_H\). Consequently the code formula and all successive quotient/remainder inverses are exact bijections on the stated full rectangle. No candidate is lost by retaining the remainders.

For the ray's specified hit, \(a_q=A_0B_0D_0(q)\le M_H\) proves both \(A_0,B_0\le M_H\). The shell bounds and first-half gate give \(0\le j<J_H\). Coprimality and the primitive equation supply exactly its three hit tests, with positive integral quotients \(D_0(q)\) and \(C_0\).

For the total indicator defined on each decoded shell, suppose its first hit is \(c_0\). In the selector sum, the product through \(n\) is one if \(n<c_0\) and zero if \(n\ge c_0\). There are exactly \(c_0\) unit terms. With no hit all \(N_H\) terms equal one. Thus the sum is the least code or the exact sentinel \(N_H\). Because the specified hit is present, its least selector is at most \(c_H\), and its digit range gives \(c_H<A_0\Lambda_H\). The first \(r_0\) outer layers are exactly the integer interval \([0,r_0\Lambda_H)\), proving the occupancy biconditional and the separate specified-witness criterion for \(A_0\le2\).

In the full radix \(M_F=9h_q\), \(J_F=6h_q\). A full hit satisfying its own decoded first-half gate has \(j<3h_q=J_H\) and, from \(AB\mid a(c)\), has \(A,B\le a(c)\le6h_q=M_H\). Hence decode–recode is defined in the PCT rectangle. Conversely every PCT hit has these same bounds, lies in the full rectangle, and has first-half shell \(a(c)\le6h_q\). Both maps retain \((j,A,B,\varepsilon)\), and their inverse compositions are therefore identities. The exact quotient coordinates
\[
D=a(c)/(AB),\quad C=(A+q^{1-\varepsilon}B)/R(c),\quad u=B^2D
\]
and the original ordered witness are computed from those unchanged digits. Predicates on them retain their truth values. An attached \(k\) is a separate label; recoding neither invents nor forgets it.

Finally \(\Lambda_F=108h_q^2=3\Lambda_H\), while the two coefficients of \(j\) are \(18h_q\) and \(12h_q\). Subtraction gives the exact integer relation
\[
c_F-c_H=2(A-1)\Lambda_H+6h_qj
=2(A-1)\Lambda_H+\frac{q-1}{2}j.
\]
This verifies both radix scales and their offset.

## thm:raw-scale-hit-incidence

For each allowed \(k\), the fixed raw seed is positive, has its original first denominator, and has coefficient period
\[
\frac{4(kA_0)(kB_0)(kC_0)}
{\gcd(4(kA_0)(kB_0)(kC_0),k\Theta_0)}
=\frac{k^2K_0}{\gcd(k^2K_0,\Theta_0)}=m_k.
\]
The factor \(k\) cancels exactly from the numerator and gcd, leaving the necessary \(k^2\); it does not remove the raw-scale condition. Thus the cited input–output incidence theorem applies with precisely this raw seed and period, and with every original input bound and congruence unchanged. The first-half gate adds only its already proved predicate on \(q\).

For clarity, for each retained prime \(q\), let \(\rho\) run over all roots of \(X^4-X^2+1\) modulo \(q\) compatible with \(X\equiv a_{\rm in}\pmod M\). Compatibility is
\(\gcd(M,q)\mid\rho-a_{\rm in}\). With \(g=\gcd(M,q)\), solve
\[
(M/g)t\equiv(\rho-a_{\rm in})/g\pmod{q/g}.
\]
The coefficient is a unit; when the modulus is one the single residue is zero. This gives exactly the cited representative \(x_{q,\rho}\) modulo \(L_q=\operatorname{lcm}(M,q)\). The entire bounded branch is
\[
X=x_{q,\rho}+L_qt,\quad
\left\lceil\frac{U-x_{q,\rho}}{L_q}\right\rceil
\le t\le
\left\lfloor\frac{V-x_{q,\rho}}{L_q}\right\rfloor.
\]
The inverse is \(\rho=X\bmod q\) and \(t=(X-x_{q,\rho})/L_q\). Distinct roots yield disjoint input branches. Thus the fixed-scale prime projection has exactly the full input fibre asserted, including empty branches and the case \(q\mid M\). For fixed \((k,X)\), the remaining choices are exactly the distinct prime divisors of the same \(N(X)\) passing that scale's complete output tests. Multiplicities of prime factors do not duplicate prime labels.

All graph coordinates are explicit functions of the fixed data and \((k,X,q)\). The scale period proves positive integrality of \(D_0(q)/k^2\); the scale identities prove the displayed raw and primitive coordinates and their ordered witness; the gate proves the two codes. Projection to the retained original data and \((k,X,q)\) is inverse to adjoining this output, hence both graph maps have singleton fibres.

Forgetting \(k\) retains the primitive period because \(m_0\mid m_k\). Conversely over a primitive incidence \((X,q)\), a scale lifts exactly when
\[
k^2\mid D_{0,p},\qquad k^2\mid D_0(q),
\]
equivalently \(k^2\mid\gcd(D_{0,p},D_0(q))\). The fibre contains one, giving the stated surjection and section. Counting this full fibre gives the first cardinality formula. Partitioning instead by \(k\), then \(q\), then the disjoint compatible root branches gives the second; each integer interval contributes its exact nonnegative length
\[
\max\left(0,
\left\lfloor\frac{V-x_{q,\rho}}{L_q}\right\rfloor-
\left\lceil\frac{U-x_{q,\rho}}{L_q}\right\rceil+1\right).
\]
All these sets are finite. If the original input solvability tests fail, the inherited convention makes every incidence empty; no nonexistent residue representative is needed.

Finally a predicate is evaluated on a single complete graph member. Reindexing its code while retaining its other labels is a bijection, so every predicate truth fibre is transported bijectively. A projection forgetting a label has selected fibre equal to its already proved full fibre intersected with the same predicate. Consequently intersections require one common graph member, and finite unions and inclusion–exclusion use the original common domain. This proves the Boolean and count assertions without an implicit replacement of several occurrences by independent witnesses.

## Exact fixtures checked

For \(p=13\), the primitive tuple \((2,1,5,2,0)\) has residual zero, \(a=4\), \(R=3\), and \(j=0\). The radices give \(c_H=36\) and \(c_F=108\). Decoding the unchanged integer 36 in the full radix instead gives \((A,j,B,\varepsilon)=(1,2,1,0)\), shell \(a=6,R=11\), and \(11\nmid14\). This confirms that the numerical codes differ while the proved recoding retains the tuple.

For \(p=61\), the raw tuple \((2,4,2,2,1)\) has equation \(128=128\), first denominator 16, scale two, and coprime tuple \((1,2,1,8,1)\). Its periods are \(m_0=8\), \(m_2=32\), with modulo-twelve intersections 24 and 96.

At \(q=109\), \(D_0=14\), \(a=28\), \(R=3\), \(j=0\), \(c_H=3\), and the ordered witness is \((28,1526,3052)\). The common-denominator numerators are \(109,2,1\), with sum \(112\); since \(3052=28\cdot109\), this equals \(4/109\). The raw value \(14/4=7/2\) is nonintegral, and the full scale fibre is \(\{1\}\), as the gcd is two.

At \(q=157\), \(D_0=20\), \(D_2=5\), and the raw and primitive tuples both give \((40,3140,6280)\). Over denominator \(6280=40\cdot157\), the reciprocal numerators are \(157,2,1\), summing to \(160\), hence the sum is \(4/157\). The gcd of 8 and 20 is four and its square-divisor fibre is exactly \(\{1,2\}\). Trial division by the primes at most the square roots verifies the primality claims for 13, 61, 109, and 157.

## Bounded task provenance

The additional exact checker raw_scale_checks.py passed with PATH Python 3.13.9 and installed SymPy 1.13.1. It enumerated all 1,524 positive divisors of \(a^2\) over the original full shell intervals at \(p=13,37,61,73,97\), giving 53 canonical seed hits. Their complete square-divisor fibres gave 57 raw seeds, and this set equalled the independent enumeration of every raw factorization \(a=ABD\) satisfying its exact gate.

It verified 34,608 signed integer-input period cases, all 225 primitive prime returns through 501 in the stated residue domains, and all 234 returned raw coordinate tuples. The first-half gate passed at 222 returns and failed at three with nonpositive coefficient. Both full and PCT rectangles were completely enumerated at the five seed primes: 856,332 full codes and 190,296 PCT codes, including 51 exact hit recodings. Every source orientation, denominator inverse, scale fibre, selector value, and layer criterion checked in this finite domain passed.

The independently implemented raw_scaled_incidence_fixture.py completely factored \(X^4-X^2+1\) for all 100 inputs \(X=6,12,\ldots,600\), retaining all prime factors without a cutoff. There were 149 distinct factor primes, the largest 114733609453. The prescribed \(p=61\) primitive output conditions retained 82 incidence pairs over 74 primes. Their exact scale fibres gave 97 triples: 82 for scale one and 15 for scale two; 67 primitive pairs had one scale and 15 had two. All 296 polynomial roots were certified by their full quartic factorization, all 296 bounded CRT branches were checked including 214 empty branches, and the direct, gcd-weighted, and root-branch counts all equalled 97. The aggregate check embeds the complete input factorizations, prime labels, root certificates, inverse parameters, and scale fibres in its JSON.

These finite checks supplement the four universal proofs above. The companion JSON records the current source hash, script hashes, runtime, coverage, and resolution history.

All 97 scaled incidence outputs, including their large prime labels, also passed the original raw/coprime coordinate equality, ordered \(d_y,d_z\) and denominator inverse, first-half gate, and both complete radix inverses. The predicates \(k=2\), \(12\mid X\), and \(q\equiv13\pmod{48}\) partitioned the retained graph into all eight exact truth cells, including empty cells. Five Boolean expressions on these same three bits were checked under the projections forgetting scale, input, or both, giving 1,220 complete selected-fibre checks. Their complete selected fibres equal the proved original fibres intersected with the same predicate, and inclusion–exclusion holds on the retained graph. A further explicit fixture verifies that the scale-one and scale-two subsets have empty graph intersection while their prime projections overlap; the JSON retains two distinct scale-labelled witnesses with the same input and prime.

The parent requested:

> Now independently review complete raw_scale_hit_incidence.tex (4 new statements) under the same assigned research directory. Root/provenance wrote and froze it. Read it fully, verify exact scale fibres, fixed-scale period, first-half/PCT/full radix inverse, full prime/input/hit incidence projections and witnesses. Write proof_review/RAW_SCALE_SUBREVIEW.md/json with all labels, hash, rigorous reasoning and findings; no main edits. I am reviewing first_two_shell_sieve.tex and updating shared review/audit records in parallel. Send mathematical verdict promptly.
