# Dated proof bulletin — 23 September 2026

This bulletin indexes the source-level structural results proved and checked on
23 September. It is a mathematical index, not a programme chronology. Every
entry states its domain, conclusion, proof locator and boundary. Finite
enumerations enter only as sharpness certificates or counterexamples to a
proposed universal invariant; their size is not evidence for arbitrary-prime
occupancy.

For the source-level results, let \(p\equiv1\pmod4\) be prime,
\(p/4<a<p/2\), \(R=4a-p\), and \(u\mid a^2\). Put

\[
g=\gcd(a,u),\qquad h=\frac{g^2}{u},\qquad
r=\frac ug,\qquad s=\frac ag.
\]

Then \(a=hrs\), \(u=hr^2\), and \(\gcd(r,s)=1\). The original labelled
channels remain

\[
E:(a,hs\kappa,phr\kappa),\quad \kappa=\frac{pr+s}{R},
\qquad
M:(a,phs\lambda,phr\lambda),\quad \lambda=\frac{r+s}{R}.
\]

Write

\[
K=\prod_{\ell^\nu\parallel R}\ell^{\lceil\nu/2\rceil},
\qquad D=\frac RK.
\]

Thus \(R=KD\), \(D\mid K\), and \(K\mathbf Z/R\mathbf Z\) has square zero.

## SZ-20260923-001 — exact affine E/M channel operator

The same divisor \(u\) is trace-admissible in both channels exactly when

\[
K\mid(4u+1),\qquad K\mid(p-1).
\]

On this common-trace locus,

\[
c_E\equiv\frac{4u+1}{K},\qquad
c_M\equiv p^{-1}\frac{p+4u}{K}\pmod D,
\qquad
c_E=c_M-\omega,\quad \omega=\frac{p-1}{K}\pmod D.
\]

For a retained coefficient vector \(C=(C_x)_{x\in\mathbf Z/D}\), the labelled
two-channel vector is

\[
J=(I+T_\omega)C,\qquad J_x=C_x+C_{x-\omega}.
\]

If \(d=\gcd(D,\omega)\) and \(L=D/d\), then \(L\) is odd and

\[
2C_x=\sum_{j=0}^{L-1}(-1)^jJ_{x-j\omega}.
\]

Moreover,

\[
0\longrightarrow\mathbf Z^{\mathbf Z/D}
\xrightarrow{I+T_\omega}\mathbf Z^{\mathbf Z/D}
\longrightarrow(\mathbf Z/2\mathbf Z)^d\longrightarrow0
\]

is exact, where the last map records the coordinate-sum parity on every
translation orbit. Pairing therefore loses no rational coefficient data and
is not a positivity-producing average.

- **Proof:** [common-trace law, inverse, cokernel and support criterion](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L90-L217).
- **Strengthens:** the separate square-zero channel laws in SZ-20260923-008 by computing their exact common locus and labelled sum.
- **Nonclaim:** the theorem does not produce a common trace at an arbitrary shell.

## SZ-20260923-002 — partial-chain quotient criterion and sharp obstruction

Let \(C_x\) count original bounded exponent words with fine sum \(x\pmod D\).
Choose a strict gcd chain

\[
g_0=D,\qquad g_j=\gcd(g_{j-1},\lambda_{i_j}),\qquad
m_j=\frac{g_{j-1}}{g_j},\qquad g_k=g,
\]

with selected interval lengths \(N_{i_j}\ge m_j\), and put

\[
B=\prod_{j=1}^k\left\lfloor\frac{N_{i_j}}{m_j}\right\rfloor.
\]

If \(Q_y\) counts the unselected words modulo \(g\), then every terminal
interval is retained by integers \(E_x\ge0\) and

\[
C_x=BQ_{x\bmod g}+E_x.
\]

Equality holds when all selected lengths are divisible by their radices. With
\(\delta=\omega\bmod g\), the complete-block subsource covers every paired
target exactly when

\[
\operatorname{supp}(Q)\cup
\bigl(\operatorname{supp}(Q)+\delta\bigr)=\mathbf Z/g.
\]

For odd \(g\), if \(e=\gcd(g,\delta)\), this requires the sharp bound

\[
|\operatorname{supp}(Q)|\ge\frac{g+e}{2}.
\]

If

\[
b=\gcd\bigl(g,\{\lambda_i:i\notin I\}\bigr)>1,
\]

with \(b=g\) when no residual coordinate remains, the two labelled translates
meet at most two of at least three quotient cosets, so this certificate cannot
close.

- **Proof:** [partial-chain decomposition, support cover and no-go theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L281-L360).
- **Strengthens:** a full chain to \(1\) may be replaced by a partial chain exactly when the surviving quotient support satisfies the displayed cover.
- **Nonclaim:** terminal intervals can add further words; failure here proves failure of this certificate, not zero occupancy of the complete shell.

## SZ-20260923-003 — mixed-order bounded section with exact decoder

If the gcd chain reaches \(g_k=1\), every fine coefficient satisfies

\[
C_x\ge
\left(\prod_{i\notin I}N_i\right)
\prod_{j=1}^k\left\lfloor\frac{N_{i_j}}{m_j}\right\rfloor.
\]

The proof supplies an integer reverse decoder through the successive quotients,
retains cyclic carry, and gives equality at the exact radix lengths.

- **Proof:** [mixed-order theorem, radix bijection and reverse decoder](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L228-L279).
- **Nonclaim:** reaching the generated subgroup without the actual bounded radix lengths is insufficient.

## SZ-20260923-004 — exact divisor-DAG optimizer

Within the preceding strict-chain certificate class, dynamic programming on the
divisor DAG of \(D\) finds the maximum lower bound. There are at most
\(n\tau(D)\) candidate labelled edges; retained predecessor data reconstruct
the optimizing chain and its integer section.

- **Proof:** [divisor-DAG proposition and reconstruction](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L396-L417).
- **Certificate:** [independent exhaustive comparison](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/check_independent.py).
- **Nonclaim:** optimizer failure is only failure of this certificate class.

## SZ-20260923-005 — arithmetic realization and sharp last capacity

The \(D=9\) and \(D=15\) specified original hard-prime packets have every
coefficient equal to two while the earlier unit-width criterion fails; the
\(D=15\) selected chain uses two nonunit steps. More generally, for every odd
\(D>1\) and strict chain ending at \(1\), removing one digit from the last
radix yields specified original subpackets at infinitely many sufficiently
large prime members, with coefficient zero on
\(H_m=m\mathbf Z/D\) and one on its complement. The stabilizer is exactly
\(H_m\), proving the last-capacity hypothesis sharp.

- **Proof:** [original packets and arbitrary odd-defect sharpness](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L432-L599).
- **Prime supply:** reducedness is proved before applying Dirichlet's theorem, cited below.
- **Nonclaim:** these are specified subpackets. The finite realization certifies sharpness and is not progress by census size or an ES counterexample.

## SZ-20260923-006 — complete plus-factor fibre

Put \(C=R+s\). The retained integer is

\[
M=p+C=4a+s.
\]

At fixed \(p,C\), every labelled cell is recovered from a divisor \(s'\mid M\)
through

\[
a'=\frac{M-s'}4,\qquad R'=C-s',
\]

together with the exact congruence, range and channel gates. The theorem gives
the inverse, first-denominator displacement and complete canonical incoming
trace fibre.

- **Proof:** [plus-factor cells, inverse and incoming fibre](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L601-L675).
- **Nonclaim:** an empty fixed-\(C\) fibre obstructs this map only; it is not an empty ES source box.

## SZ-20260923-007 — controlled upward return

The proper middle trace

\[
(p,a,R,u,h,r,s)=(67369,16849,27,4067,83,7,29)
\]

maps to the full exterior state

\[
(a',R',u',h',r',s',\kappa')=(16850,31,674,674,1,25,2174),
\]

with ordered denominators

\[
(16850,36631900,98714178844).
\]

The formulas persist whenever

\[
h=83+4650k,\qquad p=67369+3775800k
\]

is prime. The source is \((203h,27,49h,h,7,29)\); the target has
\(a'=203h+1\), \(R'=31\), \(u'=h'=(203h+1)/25\), and \(s'=25\).

- **Proof:** [exact upward family and original-gate verification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6125e74b1aadb860965964e2ae3587c902dbbab8/research/incoming/es-turn07-mixed-order-upward-20260923/core.tex#L677-L736).
- **Strengthens:** it crosses the nonincreasing-\(a\) obstruction SZ-20260923-014 by changing the retained invariant.
- **Nonclaim:** only prime progression members are included, and only the initial member is claimed to have the earlier completely empty lower-shell pattern.

## SZ-20260923-008 — square-zero trace defect and mixed exponent law

For each actual exponent part, the exact trace defect lies in
\(K\mathbf Z/R\mathbf Z\). The full integer-exponent formula retains the
original factor, exponent, channel and mixed terms; reduction to the additive
fine coordinate is proved rather than substituted for the original object.

- **Proof:** [complete source, reciprocal hypothesis, defect and mixed law](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L33-L238).
- **Module alias:** SZP-01.
- **Nonclaim:** no initial trace-source existence follows.

## SZ-20260923-009 — bounded coefficient partition and sharp unit width

The full original exponent box is partitioned by finite geometric coefficient
polynomials, and their stabilizers are calculated exactly. If an actual unit
direction has width at least \(D-1\), every coefficient is positive with the
displayed integer lower count; the threshold is sharp.

- **Proof:** [coefficient partition, saturation and stabilizers](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L239-L339).
- **Module alias:** SZP-02.
- **Nonclaim:** generated-subgroup support without the bounded width condition is insufficient.

## SZ-20260923-010 — prime-power and prime-square classification

For \(a=q^e\), the middle trace exponents are classified by the original gates.
For \(a=q^2\), both channel orientations and every trace word are classified
without replacing the divisor box by a subgroup surrogate.

- **Proof:** [prime-power and prime-square classification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L340-L404).
- **Module alias:** SZP-03.
- **Nonclaim:** the classification is restricted to this carrier locus and does not supply a carrier prime at an arbitrary input.

## SZ-20260923-011 — terminality for inherited deletion systems

Every proper middle trace at \(a=q^2\) has both original full gates empty at
that shell and no return under either inherited residual-divisor deletion
system. The proof retains every residual divisor and both channel domains.

- **Proof:** [prime-square terminality theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L405-L429).
- **Module alias:** SZP-04.
- **Nonclaim:** terminality for these maps says nothing about other maps or ES.

## SZ-20260923-012 — factor-sum return and complete inverse in its exact ansatz

Fix the displayed squarefree target residual \(\delta\), retain the raw factor
\(r\), and shift \(h,s\) oppositely. In this exact ansatz, the
source-to-target displacement is biconditional to the displayed integer-root
quadratic. Positivity, primitive gcd reduction, target denominators and every
incoming source over a marked full middle target are proved.

- **Proof:** [factor-sum theorem, quadratic gate and inverse](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L431-L544).
- **Module alias:** SZP-05.
- **Nonclaim:** completeness is relative to the stated residual, unchanged \(r\), and opposite-shift ansatz; the quadratic root is not assumed for every trace.

## SZ-20260923-013 — Pell specialization

On the prime-square word \(r=1,h=s=q\), the factor-sum quadratic becomes the
displayed Pell equation. Its recurrence, source and target maps, positivity,
and isolated hard-prime examples retain every old and new word and ray.

- **Proof:** [Pell equation, recurrence and exact returns](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L545-L615).
- **Module alias:** SZP-06.
- **Nonclaim:** infinitely many integer Pell points do not prove infinitely many prime values.

## SZ-20260923-014 — least obstruction to nonincreasing trace repair

Among primes \(p\equiv1\pmod {24}\), \(p=67369\) is the least input for which
the first rational trace precedes every original full gate. Therefore no
universal repair from every trace can require the distinguished denominator
\(a\) to decrease or remain fixed.

- **Proof:** [finite least-example theorem and complete prefix certificate](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L990-L1045).
- **Module alias:** SZP-07.
- **Nonclaim:** this finite theorem proves leastness of a route boundary, not general occupancy and not an ES counterexample.

## SZ-20260923-015 — exact fixed-tail-sum fibre

Let \(p\) be an odd prime and \(N=Y+Z>p\). Ordered positive integral triples
with \(p/4<A<p/2\), reciprocal sum \(4/p\), and fixed sum \(N\) are in
bijection with residual divisors \(\rho\mid N\) satisfying the exact
discriminant-square, positivity and parity gates. The inverse is explicit.
Writing \(\rho\) as its squarefree part times a square gives the exact Pell
lattice together with all required divisibility and congruence gates.

- **Proof:** [fixed-sum bijection, inverse and Pell lattice](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L616-L721).
- **Module alias:** SZP-08.
- **Nonclaim:** an unrestricted Pell point need not satisfy the integer-tail gates; an empty fixed-sum fibre does not obstruct maps changing \(N\).

## SZ-20260923-016 — prime-square fixed-sum divisor obstruction

For every proper prime-square E or M trace with word \(q\) or \(q^3\), every
target word, both channels and both tail orders, no integral target retaining
the same numerical tail sum can have residual a proper divisor of the source
residual. The proof is a universal four-case argument.

- **Proof:** [all-word, both-channel obstruction theorem](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/6c064a07298cdba38352998364ce6b7cb3efa973/research/incoming/es-turn07-square-zero-pell-20260922/core.tex#L722-L947).
- **Module alias:** SZP-09.
- **Nonclaim:** a smaller residual not dividing the source residual, or a map changing the numerical tail sum, lies outside this theorem.

## SZ-20260923-017 — exact weighted signed-pair fibres

For \(S=pa\), let \(G_R=(\mathbb Z/R\mathbb Z)^\times\), give
\(\{e_t:t\in G_R\}\) the orthonormal counting inner product, and retain

\[
v_{p,a,\sigma}=\sum_{d\mid S}
\left(\frac d{\sqrt S}\right)^{-\sigma}e_{d\bmod R},
\qquad J_Re_t=e_{-t},
\]

for every real \(\sigma\). For
\(W_\sigma(h)=\sum_{k\mid h}(h/k^2)^\sigma\), the complete ordered-pair
fibre calculation gives

\[
\mathcal T_{p,a}(\sigma)
=\langle v_{p,a,\sigma},J_Rv_{p,a,\sigma}\rangle
=2\sum_{u\in E_a}W_\sigma(h_u)
+(p^\sigma+p^{-\sigma})\sum_{u\in M_a}W_\sigma(h_u).
\]

The mixed fibre is oriented from the \(p\)-bearing divisor; its two position
bits are \((pkr,ks)\) and \((ks,pkr)\). The middle fibre consists of
\((kr,ks)\) and \((pkr,pks)\). These labelled maps have exact inverses through
the two \(p\)-valuations, \(k=\gcd(b,c)\), and
\((a,u)=(hrs,hr^2)\). Every displayed weight is positive, so

\[
\mathcal T_{p,a}(\sigma)>0
\Longleftrightarrow E_a\cup M_a\ne\varnothing.
\]

- **Proof:** [complete weighted fibre and inverse](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L45-L138).
- **Lineage:** the unweighted Boolean-pair antecedent is credited to JT in the [source ledger](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/source_reading.json); the specialized E/M coordinates cite Elsholtz--Tao.
- **Nonclaim:** the identity is an exact criterion for occupancy; it does not prove that every shell or every prime has positive pairing.

## SZ-20260923-018 — character sign, parity energies, and degree covariance

For
\(Z_{S,\chi}(\sigma)=\sum_{d\mid S}\chi(d)(d/\sqrt S)^{-\sigma}\),

\[
\mathcal T_{p,a}(\sigma)=\frac1{\varphi(R)}
\sum_{\chi\in\widehat G_R}\chi(-1)|Z_{S,\chi}(\sigma)|^2.
\]

With \(P_\pm=(I\pm J_R)/2\), the same form is

\[
\mathcal T_{p,a}(\sigma)=
\|P_+v_{p,a,\sigma}\|^2-\|P_-v_{p,a,\sigma}\|^2.
\]

The unitary map \(e_t\mapsto e_{t/R}\) lands in the exact-additive-order-
\(R\) stratum of \(\ell^2(\mathbb Q/\mathbb Z)\), so distinct residuals have
disjoint support. For the unscaled global pullback
\((A_qf)(x)=f(qx)\), one has

\[
(A_q^*g)(y)=\sum_{qx=y}g(x),
\qquad A_q^*JA_q=qJ.
\]

- **Proof:** [character orthogonality, parity decomposition, exact-order embedding and degree action](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L140-L204).
- **Nonclaim:** an unsigned energy lower bound does not imply strict signed positivity, and degree amplification preserves signed isotropy.

## SZ-20260923-019 — exact cross-shell boundary and cyclic obstruction

Let \(q=4m+1\), \(qR<p\),
\(a=(p+R)/4\), \(a'=a+mR\), and take actual divisors
\(d\mid pa\), \(e\mid pa'\) with \(R\mid d+e\). Set

\[
\alpha=\frac{pa}{d},\quad \beta=\frac{pa'}e,
\quad \lambda=\frac{d+e}{R},\quad
\mu=\frac{\alpha+\beta}{R}.
\]

The integrality of \(\mu\) uses \(\gcd(d,R)=1\), which follows from the
original-shell domain. The retained columns satisfy

\[
\lambda\beta-d\mu=pm,
\qquad e\mu-\lambda\alpha=pm,
\]

and

\[
\frac4p=\frac1a+\frac1{\lambda\alpha}
+\frac1{\mu d}+\frac{m}{a\lambda\mu}.
\]

Writing \(L=\lambda\mu\), \(g=\gcd(L,m)\),
\(\ell=L/g\), and \(\nu=(L+m)/g\), the first and fourth terms fuse to one
unit fraction exactly when \(\nu\mid a\). The exact obstruction map is

\[
\Theta_{\ell,\nu}:\mathbb Z\longrightarrow
(\nu^{-1}\mathbb Z)/\mathbb Z,
\qquad n\longmapsto\frac{n\ell}{\nu}+\mathbb Z,
\]

with kernel \(\nu\mathbb Z\). Its value at \(a\) has order

\[
\rho=\frac{\nu}{\gcd(a,\nu)},
\]

which is also the reduced numerator retained by the failed fusion.

- **Proof:** [cross-shell determinant, reciprocal identity, fusion criterion and obstruction space](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L206-L337).
- **Nonclaim:** a nonzero class obstructs only this prescribed fusion; it does not exclude another cross-shell pair, shell, channel or return map.

## SZ-20260923-020 — exact odd-quotient complement decomposition

Assume

\[
m=\gcd(R,p-1),\qquad R\mid m^2,
\qquad N=\frac Rm>1,
\]

and define

\[
\mathcal T_N=\{u\mid a^2:m\mid p+4u\},
\qquad b_u=\frac{p+4u}{m}\pmod N,
\qquad \omega=\frac{p-1}{m}\pmod N.
\]

The complement \(\iota(u)=a^2/u\) is a fixed-point-free involution of
\(\mathcal T_N\), \(\omega\) is a unit modulo \(N\), and

\[
b_{\iota(u)}=-b_u,\qquad
u\in M_a\Longleftrightarrow b_u=0,\qquad
u\in E_a\Longleftrightarrow b_u=\omega.
\]

For
\(U_N=\{u\in\mathcal T_N:b_u\notin\{0,\omega,-\omega\}\}\), there is an
exact labelled orbit bijection

\[
\mathcal T_N/\iota\simeq
E_a\amalg(M_a/\iota)\amalg(U_N/\iota),
\]

and hence

\[
|\mathcal T_N|=2|E_a|+|M_a|+|U_N|.
\]

The inverse attaches the actual complement pair; one input-member bit restores
the labelled source.

- **Proof:** [complement congruence, free action, gates, orbit inverse and count](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L339-L418).
- **Nonclaim:** the term \(U_N\) is retained; quotient support is not replaced by total mass or by a generated subgroup.

## SZ-20260923-021 — unique and sharp three-colour closure

Complementation alone forces every possible colour orbit into an E or M gate
exactly when

\[
\{0,\omega,-\omega\}=\mathbb Z/N\mathbb Z,
\]

which, for nontrivial odd \(N\), is equivalent to \(N=3\). This is sharp for
every odd \(N>3\). Put

\[
m=3N,\qquad R=3N^2,\qquad
U=\frac{ms-1}{4},\qquad a=U(mk-1),\qquad p=4a-R,
\]

where \(s\equiv1\pmod N\), \(ms\equiv5\pmod8\), and even \(k\) satisfies
\(4Uk\equiv2\pmod N\). The resulting reduced arithmetic progression contains
infinitely many primes \(p\equiv1\pmod {24}\), with
\(\gcd(R,p-1)=m\), \(\omega=1\), and the actual complement orbit of \(U\)
having colours \(\{2,-2\}\), wholly outside the two gates.

- **Proof:** [uniqueness and explicit reduced prime progression](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L420-L493).
- **Literature input:** Dirichlet's theorem is used only after reducedness of the displayed progression is proved.
- **Nonclaim:** uncovered orbits for \(N>3\) prove sharpness of complement closure, not failure of Erdős--Straus on those primes.

## SZ-20260923-022 — same-shell third-defect return and affine quotient map

Under

\[
\gcd(R,p-1)=R/3,
\qquad m=R/3,
\qquad
\mathcal T_3=\{u\mid a^2:m\mid p+4u\},
\]

every member of \(\mathcal T_3\) returns at unchanged \((p,R,a)\) to an
original M word at \(u\), an E word at \(u\), or an E word at \(a^2/u\),
according as its colour is \(0\), \(\omega\), or \(-\omega\). The two
rational middle tails have reduced denominators dividing three, and

\[
2|E_a|+|M_a|=|\mathcal T_3|,
\qquad
\#\{\text{increasing original triples}\}=\frac{|\mathcal T_3|}{2}.
\]

For the earlier square-zero root
\(K=\prod_{\ell^e\parallel R}\ell^{\lceil e/2\rceil}\), put
\(D=R/K\) and \(t=m/K\). Then \(D=Nt\), and on \(\mathcal T_N\) the prior
middle fine coordinate is exactly \(c_M=tb_u\pmod{Nt}\). The subgroup quotient

\[
t\mathbb Z/(Nt)\mathbb Z\longrightarrow\mathbb Z/N\mathbb Z,
\qquad tb\longmapsto b,
\]

carries the prior E/M targets and complement action to
\(\omega,0\), and negation. This is an exact morphism between the two
presentations; it does not identify their full source sets.

- **Proof:** [affine-coordinate quotient and whole-shell third-defect completion](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L485-L623).
- **Nonclaim:** return is proved from a nonempty trace source; the theorem does not force such a source at every prime.

## SZ-20260923-023 — complete applicable-residual family

Write

\[
p-1=2^k3^\eta b,
\qquad \gcd(b,6)=1,
\qquad k\ge3,\quad\eta\ge1.
\]

The residuals \(0<R<p\), \(R\equiv3\pmod4\), satisfying
\(\gcd(R,p-1)=R/3\) are exactly

\[
R=3^{\eta+1}d,
\qquad d\mid b,
\qquad d\equiv(-1)^\eta\pmod4.
\]

Every such residual obeys
\(R\le3(p-1)/2^k<p\). The family is nonempty exactly when \(\eta\) is even
or \(b\) has a prime divisor congruent to \(3\pmod4\).

- **Proof:** [valuation classification, converse gcd identity and nonemptiness criterion](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L625-L662).
- **Nonclaim:** constructing every applicable residual does not prove that one associated \(\mathcal T_3\) is nonempty.

## SZ-20260923-024 — complete residual-27 empty locus

Let \(p\equiv73\) or \(145\pmod {216}\) be prime and
\(a=(p+27)/4\). Then

\[
\mathcal T_3=\{u\mid a^2:u\equiv2\pmod9\}.
\]

The original residual-27 shell is empty exactly in either of two disjoint
factorization types:

1. every prime factor of \(a\) is \(1\pmod3\);
2. exactly two prime-factor occurrences of \(a\), counted with multiplicity,
   are \(5\pmod9\), and every remaining prime factor is \(1\pmod9\).

Outside these types, the proof constructs a word with at most three signed
prime occurrences in \(u/a\) and applies SZ-20260923-022. The empty examples
\((p,a)=(1009,259)\) and \((73,25)\) exhibit the two factorization types; they
are not Erdős--Straus counterexamples.

- **Proof:** [complete factor-level classification and bounded construction](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/core.tex#L664-L729).
- **Certificate:** [independent implementation and exact replay](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/13cdd6c8d1236b078bb503af698d132017ed99d7/research/incoming/es-third-defect-signed-pairing-20260923/check_independent.py).
- **Nonclaim:** this is a complete theorem for one applicable residual, not universal all-prime occupancy.

## Human mathematical lineage

- Christian Elsholtz and Terence Tao, [Counting the number of solutions to the Erdős–Straus equation on unit fractions, Section 2, Propositions 2.2 and 2.6](https://arxiv.org/abs/1107.1010), supply the Type-I/II coordinate lineage. The modules preserve the [author TeX and read locators](research/incoming/es-turn07-square-zero-pell-20260922/source_reading.json).
- K. Yamamoto, [On the Diophantine equation \(4/n=1/x+1/y+1/z\), Lemma 2, equation (4), printed page 38](https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf), supplies the inherited exterior congruence context.
- Miguel Angel Lopez, [A Complete Congruence System for the Erdős–Straus Conjecture](https://arxiv.org/abs/2404.01508), supplies hard-residue-class and solution-form context. No theorem above assumes the paper's proposed coverage system.
- Andrew V. Sutherland, [Dirichlet L-functions, primes in arithmetic progressions, Theorem 18.1](https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf#page=1), is used only after each arithmetic progression is proved reduced.
- JT and The Clankers, [Boolean product formulation and exact cyclotomic reconstruction, BP15--BP16 and the following divisor-pair fibre](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/a8cefe028e383d1967cc8876fbbdd9325db9bfb8/research/continuation-2026-09-12/reconstructed/boolean_cyclotomic.tex), supply the unweighted signed-pair and character antecedent used in SZ-20260923-017--018.

The original formulas, hypotheses, proofs, figures, executable certificates,
source hashes and integration boundaries are retained in the three standalone
modules. The next structural obligation is to prove a quotient-support cover,
force a nonempty applicable three-colour source, force a cross-shell pair in
the kernel of its cyclic boundary map, or construct a different source-changing
morphism at every hard prime; enlarging a finite census does not discharge it.
