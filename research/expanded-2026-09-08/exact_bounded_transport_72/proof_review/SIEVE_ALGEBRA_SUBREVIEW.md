# Independent algebra review of the first two shells

The review concerns the original prime /(p=12h+1/), where /(h/geq1/), the original full shell range /(A_p=/{3h+1,/ldots,9h/}/), and the positive-divisor channels

/[
E_a=/{u/in/mathbb Z_{>0}:u/mid a^2,/ R_a/mid4u+1/},/qquad
M_a=/{u/in/mathbb Z_{>0}:u/mid a^2,/ R_a/mid u+a/},/qquad R_a=4a-p.
/]

**Verdict.** Both proposed criteria for shell occupancy /(E_a/cup M_a/ne/varnothing/) are correct, including all proposed witnesses with multiplicity. At /(R_a=3/), the criterion holds separately for each channel. At /(R_a=7/), it is a criterion for their union: neither channel individually has the stated equivalence. For example /(p=13,a=5,R_a=7/) has /(E_a=/{5/}/) and /(M_a=/varnothing/).

## Original domain and exact divisor coordinates

Put /(a_3=3h+1/) and /(a_7=3h+2/). Their original moduli are /(4a_3-p=3/) and /(4a_7-p=7/). Both lie in /(A_p/): the upper inequalities are /(1/leq6h/) and /(2/leq6h/). Also /(0<a_i<p/). Thus /(/gcd(a_i,R_{a_i})=1/): any prime dividing both would divide /(p=4a_i-R_{a_i}/), contradicting /(a_i<p/). In particular neither factorization contains a prime equal to the shell modulus.

Write the complete factorization /(a=/prod_{/ell/mid a}/ell^{b_/ell}/), /(b_/ell/geq1/). The full map

/[
/prod_{/ell/mid a}/{0,/ldots,2b_/ell/}/longrightarrow/operatorname{Div}(a^2),/qquad
(e_/ell)_/ell/longmapsto/prod_/ell/ell^{e_/ell}
/]

is a bijection, with inverse /(u/mapsto(v_/ell(u))_/ell/), by unique factorization. All the constructions below use this exact box. Factors counted with multiplicity select copies from the /(b_/ell/) available copies, rather than requiring distinct primes. No exponent interval is enlarged and no auxiliary cutoff is imposed.

## First shell: modulus three

Since /(a_3/equiv1/pmod3/), both channel targets are /(2/pmod3/): /(4u+1/equiv u+1/) and /(-a_3/equiv2/). Every prime factor of /(a_3/) has residue one or two modulo three.

If there is no residue-two prime factor, every divisor of /(a_3^2/) is one modulo three; hence both channels are empty. Conversely, if /(/ell/mid a_3/) and /(/ell/equiv2/pmod3/), then /(u=/ell/) is a positive divisor of /(a_3^2/) and belongs to /(E_{a_3}/). In fact it also belongs to /(M_{a_3}/), since /(a_3/equiv1/). An alternative middle witness is /(u=a_3/ell/): its exponent at /(/ell/) is /(b_/ell+1/leq2b_/ell/), every other exponent is /(b_r/), and /(u/equiv-a_3/pmod3/). Therefore

/[
E_{a_3}/ne/varnothing/ /Longleftrightarrow/ M_{a_3}/ne/varnothing
/ /Longleftrightarrow/ /exists/ell/mid a_3:/ell/equiv2/pmod3.
/]

## Second shell: modulus seven

For the complete factorization of /(a=a_7/), define

/[
n_3=/sum_{/ell/mid a,/ /ell/equiv3/ (7)}b_/ell,/qquad
m_{24}=/sum_{/ell/mid a,/ /ell/equiv2/text{ or }4/ (7)}b_/ell.
/]

The assertion is

/[
E_a/cup M_a/ne/varnothing
/ /Longleftrightarrow/
/bigl(/exists/ell/mid a:/ell/equiv5/text{ or }6/ (7)/bigr)
/ /lor/ n_3/geq3
/ /lor/ (n_3/geq1/ /land/ m_{24}/geq1).
/]

The exterior target is /(5/pmod7/), since /(4/cdot2/equiv1/pmod7/) and /(-2/equiv5/). The middle condition is exactly /(u/a/equiv-1/pmod7/), with modular division permitted by the proved unit condition. This congruence is used only to check the stated integer /(u/); the original integer and exponent box remain present.

### Positive witnesses and all exponent bounds

1. If a prime factor /(/ell_5/equiv5/pmod7/) occurs, choose /(u=/ell_5/). Its single nonzero exponent is one, at most /(2b_{/ell_5}/), and /(4u+1/equiv21/equiv0/). Thus /(u/in E_a/).
2. If a prime factor /(/ell_6/equiv6/pmod7/) occurs, choose /(u=a/ell_6/). Its exponent at /(/ell_6/) is /(b_{/ell_6}+1/leq2b_{/ell_6}/); all others are their original /(b_r/). It is positive and /(u/equiv-a/), so /(u/in M_a/).
3. If /(n_3/geq3/), select exactly three available prime-factor copies of residue three. Their product /(d/) divides /(a/), even when some selected copies are equal. The residue is /(d/equiv3^3=27/equiv-1/). Set /(u=ad/). Each exponent is /(b_/ell+v_/ell(d)/), lying in /([b_/ell,2b_/ell]/). Thus /(u/mid a^2/), /(u>0/), and /(u/equiv-a/), proving /(u/in M_a/).
4. Suppose a residue-three prime /(/ell_3/) and a residue-two prime /(t/) occur. They are distinct, because their residues differ. Choose /(u=a/ell_3t/). The two affected exponents are /(b_{/ell_3}+1/) and /(b_t+1/), within their full bounds; all other exponents are unchanged. Since /(/ell_3t/equiv3/cdot2/equiv-1/), this is a middle witness.
5. Suppose a residue-three prime /(/ell_3/) and a residue-four prime /(t/) occur. Again they are distinct. Choose /(u=a/ell_3/t/). This is a positive integer since /(t/mid a/). Its exponents are /(b_{/ell_3}+1/), /(b_t-1/), and /(b_r/) at the remaining primes. In particular /(0/leq b_t-1/leq2b_t/) and /(b_{/ell_3}+1/leq2b_{/ell_3}/), so /(u/mid a^2/). Since the inverse of four modulo seven is two, /(/ell_3/t/equiv3/cdot2/equiv-1/), giving /(u/equiv-a/) and /(u/in M_a/).

These five cases prove sufficiency for the exact disjunction.

### Converse, including the finite bounds

Suppose the disjunction is false. No prime factor has residue five or six. Every prime factor therefore has residue one, two, three, or four. There are two exhaustive cases.

First, if /(n_3=0/), all prime factors belong to the explicitly multiplicatively closed set /(H=/{1,2,4/}/pmod7/): products are verified by /(2^2/equiv4/), /(2/cdot4/equiv1/), and /(4^2/equiv2/). Thus /(a/) and every positive divisor of /(a^2/) have residue in /(H/). The exterior target five is outside /(H/); the middle target belongs to /(-H=/{6,5,3/}/), disjoint from /(H/). Both channels are empty.

Second, suppose /(n_3/geq1/). Falsity of the disjunction implies /(n_3/leq2/) and /(m_{24}=0/). Hence only residue-one and residue-three prime factors remain. For an arbitrary divisor /(u=/prod/ell^{e_/ell}/) in the original box, put /(j=/sum_{/ell/equiv3/ (7)}e_/ell/). Then

/[
0/leq j/leq2n_3,/qquad u/equiv3^j/pmod7,/qquad a/equiv3^{n_3}/pmod7.
/]

The full power table is

/[
(3^0,3^1,3^2,3^3,3^4,3^5,3^6)/equiv(1,3,2,6,4,5,1)/pmod7.
/]

Its first six entries are pairwise distinct, so equality of powers holds exactly when their exponents are congruent modulo six. Exterior membership would require /(j/equiv5/pmod6/); this is impossible for /(0/leq j/leq2n_3/leq4/). Middle membership would require /(j/equiv n_3+3/pmod6/). If /(n_3=1/), this is /(j/equiv4/) with /(0/leq j/leq2/); if /(n_3=2/), it is /(j/equiv5/) with /(0/leq j/leq4/). Both are impossible. This exhausts all divisors in the original box and proves necessity.

## Exact reconstruction in the original integer denominators

For any of the witnesses above, retain /(p,a,R_a,S_a=pa/). If /(u/in E_a/), take

/[
d=p^2u,/quad S_a^2/d=a^2/u,/quad
y=/frac{pa+p^2u}{R_a},/quad z=/frac{pa+a^2/u}{R_a}.
/]

If /(u/in M_a/), take

/[
d=pu,/quad S_a^2/d=pa^2/u,/quad
y=/frac{pa+pu}{R_a},/quad z=/frac{pa+pa^2/u}{R_a}.
/]

All displayed divisors are positive integers. For the exterior channel, using /(p/equiv4a/pmod{R_a}/), the two numerators are respectively congruent to /(4a^2(1+4u)/) and /(a^2u^{-1}(4u+1)/), hence divisible by /(R_a/). For the middle channel, their residues are /(p(a+u)/) and /(pa u^{-1}(u+a)/), also zero. Every use of /(u^{-1}/) is valid because /(u/mid a^2/) and /(/gcd(a,R_a)=1/). Thus /(y,z/) are positive integers with their displayed original order. Finally, with either channel's /(d/),

/[
/frac1y+/frac1z
=/frac{R_a}{S_a+d}+/frac{R_ad}{S_a(S_a+d)}
=/frac{R_a}{S_a}
=/frac4p-/frac1a.
/]

This proves the original three-term identity for every constructed witness without changing the first denominator, permuting the last two, deleting scale, or replacing a bounded divisor problem by an unrestricted residue subgroup.

## Task provenance

The bounded task received from the parent agent was:

> Independently adversarially derive the proposed first-two-shell criteria, no edits outside proof_review. p=12h+1 prime,h>=1. a3=3h+1,R3: E/M iff a3 has prime factor2mod3. a7=3h+2,R7: n3=sum exponents of factors3mod7,m24=sum exponents factors2or4; E/M iff factor5or6 OR n3>=3 OR(n3>=1 andm24>=1). E: u|a² and u≡-4^-1 modR. M:u|a² andu≡-a modR. Explicit witnesses:ell5 E; a*ell6 M; a*d M with d|a productthree factors3mod7 counted multiplicity; a*ell3*t M ift2; a*ell3/t M ift4. Check edge cases signs,budgets and full converse. Source bounded_transport.tex under .. Send rigorous verdict and any gap promptly; optionally proof_review/SIEVE_ALGEBRA_SUBREVIEW.md.
