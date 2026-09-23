# Typed maps, fibres, kernels, and retained data

## Original divisor source to marked words

For fixed prime `p`, shell `a`, residual `R=4a-p`, and `u|a^2`:

`u -> g=gcd(a,u) -> (h,r,s)=(g^2/u,u/g,a/g)`.

The inverse is `a=hrs`, `u=hr^2`, with `gcd(r,s)=1`. The E and
M gates and ordered denominators remain those displayed in `core.tex`,
equations (1.4)--(1.6).

## Weighted pair fibre

Domain:

`(u,k,position)` with `u` an original E or M word, `k|h_u`, and
the displayed two-valued position or common-`p` bit.

Codomain:

`(d,e)` with `d,e|pa` and `R|(d+e)`.

For E, `r` is oriented from the `p`-bearing divisor:

`(u,k,0)->(pkr,ks)`, `(u,k,1)->(ks,pkr)`.

For M:

`(u,k,0)->(kr,ks)`, `(u,k,1)->(pkr,pks)`.

The inverse reads the two `p`-valuations, divides by their common factor, and
recovers `k,r,s,h,u`. There is no kernel: this is a bijection of labelled
sets. Forgetting `k` and the bit has fibre size `2 tau_div(h_u)`.

## Character and exact-order maps

`e_t -> delta_(t/R)` is a unitary map from
`ell^2((Z/RZ)^times)` onto the exact-order-`R` stratum of
`ell^2(Q/Z)`. Distinct numeric residuals have disjoint images. The global
pullback `A_q f(x)=f(qx)` has
`A_q^*g(y)=sum_(qx=y)g(x)` and `A_q^* J A_q=qJ`.
Its compression to one exact-order stratum is recorded separately from its
support in other strata.

## Cross-shell map and obstruction

Source:

`(p,R,m,d,e)` with `p` prime, `R>0`, `4|(p+R)`,
`q=4m+1`, and `qR<p`. Retain
`a=(p+R)/4` and `a'=(p+qR)/4=a+mR`; require
`d|pa`, `e|pa'`, and `R|(d+e)`.

Retained coordinates:

`alpha=pa/d`, `beta=pa'/e`,
`lambda=(d+e)/R`, `mu=(alpha+beta)/R`.

Output:

the determinant pair `lambda beta-d mu=pm`,
`e mu-lambda alpha=pm`, and the full four-term reciprocal identity.

With `L=lambda mu`, `g=gcd(L,m)`, `ell=L/g`,
`nu=(L+m)/g`, the cyclic map is

`Theta_(ell,nu): Z -> (nu^{-1}Z)/Z`,
`n -> n ell/nu + Z`.

Its kernel is exactly `nu Z`. The obstruction at `a` vanishes exactly when
the fused denominator `aL/(L+m)` is integral. Its order is
`rho=nu/gcd(a,nu)`. No other return mechanism is removed by this map.

## Residual quotient and complement

Assume `gcd(R,p-1)=m`, `R|m^2`, `N=R/m>1`. The source is

`T_N={u|a^2: m|(p+4u)}`.

The colour map is

`b(u)=(p+4u)/m mod N`,

and the complement is the fixed-point-free involution
`iota(u)=a^2/u`. The exact relation is `b(iota(u))=-b(u)`.
The M target is zero and the E target is
`omega=(p-1)/m mod N`.

The orbit map

`T_N/iota -> E disjoint_union (M/iota) disjoint_union (U_N/iota)`

is a bijection. The inverse attaches the actual complement pair; an
input-member bit restores the labelled source. Here
`U_N={u: b(u) notin {0,omega,-omega}}` is the exact uncovered source.

## Morphism to the earlier affine channel

Let `K=product ell^ceil(v_ell(R)/2)`, `D=R/K`, and `t=m/K`.
Then `K|m`, `N|K`, `D=Nt`, and `D|m`. On `T_N`, the earlier
middle fine coordinate is `c_M=t b(u) mod Nt`. The exact subgroup quotient

`tZ/(Nt)Z -> Z/NZ`, `tb -> b`

sends the prior M and E targets to `0` and `omega`, and sends complement
to negation. This proves the relation between the two presentations; it does
not identify their full source sets.

## Third-colour output

At `N=3`, every colour is one of `0,omega,-omega`.
The output map sends `0` to M at `u`, `omega` to E at `u`,
and `-omega` to E at `a^2/u`. Primitive coordinates swap by
`(h,r,s)->(h,s,r)`. The prime, residual, shell, and exponent box remain.

For every odd `N>3`, the construction in Proposition 4.3 gives a source word
with colours `{2,-2}` while `omega=1`; this is an actual uncovered orbit,
not a missing arrow inferred from nonidentity.
