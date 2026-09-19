# Pointwise localization of the complete original source

Date: 2026-09-19  
Collective byline: The Clankers  
Recovered source locator: supplied session transcript, lines 13194--13587  
Transcript SHA-256: `A92F5139B9AABAE4E9DF7D039D8C74C60B640D65E939D37869A8348488159E90`

## Determination

The substantive localization results are correct under their stated
hypotheses. An independent derivation checked the least-nonresidue facts,
the middle and exterior inequalities, the endpoint-excluded strict inequality,
the reciprocal-coordinate bound, the free Klein-four quotient, the two empty
minimal lanes at `p=2521`, and the odd-square two-colour obstruction.

The recovered plaintext required three presentation repairs, all incorporated
in the proof below.

1. The plaintext extraction erased radicals and fraction bars. In the
   middle proof the two cases must be `j <= sqrt(a)` and `j >= sqrt(a)`, not
   literally `j <= a` and `j >= a`.  The latter case split would not prove the
   result.  Likewise several displayed bounds below are stacked fractions in
   the source rendering and must not be read as products.
2. The recovered freeness proof mentioned the fixed loci of the swap and the
   swap-complement but omits the complement-fixed locus.  It is empty because
   `b^2=pa` is impossible: `v_p(pa)=1`.  Adding this sentence completes the
   proof without changing the theorem.
3. The statement that orbit sum plus three orbit differences has an integral
   inverse is correct **on the image lattice**.  The image must be typed by its
   congruence condition modulo four; it is not all of `Z^4` in the new
   coordinates.

The independent derivation and exhaustive check found no counterexample to any
listed localization inequality.

## 1. Exact coordinate setup

Let `p = 1 (mod 8)` be prime, let

```
p/4 < a < p/2,                 R = 4a-p,
```

and let `u | a^2`.  Put

```
d0 = gcd(a,u),  h=d0^2/u,  r=u/d0,  s=a/d0.
```

Prime valuations give

```
a=hrs,  u=hr^2,  gcd(r,s)=1.
```

Moreover `h | a`, hence `h<p`.  Since `R=3 (mod 4)`, `3<=R<p`, and
`gcd(pa,R)=1`.

For a middle state, the gate `R | 4u+p` is equivalent to

```
R lambda = r+s.
```

For an exterior state, the gate `R | 4u+1` is equivalent to

```
R kappa = pr+s.
```

These equivalences follow after substituting `p=4hrs-R`; the factors
`4hr` are units modulo `R`.

## 2. Least-nonresidue facts

Define

```
nu_p = min{n>0 : (n/p)=-1},
m_p  = min{m>0 : m=3 (mod 4), (m/p)=-1},
J_p  = (m_p+1)/4.
```

Here all symbols with denominator `p` are Legendre symbols.

### 2.1 `nu_p` is an odd prime

There is a nonresidue in `{1,...,p-1}`, so `nu_p<p`.  If `nu_p=xy` were
composite with `1<x,y<nu_p`, then both factors would be residues by
minimality, making their product a residue.  This is impossible.  Also
`(2/p)=1` because `p=1 (mod 8)`, so `nu_p` is not two.  Thus `nu_p` is an
odd prime and `3<=nu_p<p`.

### 2.2 The elementary square-root bound

In fact

```
nu_p^2 <= p.
```

If `nu_p^2>p`, write `p=c nu_p+d` with `0<c,d<nu_p`; the remainder is
nonzero because the two primes `nu_p` and `p` are distinct.  Minimality makes
both `c` and `d` residues.  But

```
c nu_p = -d (mod p)
```

has a nonresidue on the left and a residue on the right, since `(-1/p)=1`.
This contradiction proves the claim.

Consequently `p-2nu_p` is positive.  It is `3 (mod 4)` and

```
((p-2nu_p)/p)=(-2nu_p/p)=-1,
```

because both `-1` and `2` are residues.  Hence

```
m_p <= p-2nu_p < p.
```

For a hard prime, meaning here that `2,3,5,7` are all quadratic residues,
minimality gives `nu_p>=11`, `m_p>=11`, and `J_p>=3`.

## 3. Middle-channel localization

Order a middle state by `r<s`; the other order only swaps the last two
denominators.  Set

```
j=hr lambda,  Q=4j-1.
```

Using `R lambda=r+s`, direct expansion gives the exact identities

```
Q s = p lambda+r,             Q R = p+4hr^2.             (M1)
```

### 3.1 `Q` is an actual `3 (mod 4)` nonresidue below `p`

For every odd prime `ell | h`, one has `Q=-1 (mod ell)`.  Since
`Q=3 (mod 4)`, quadratic reciprocity gives `(ell/Q)=1`.  If `2|h`, then
`Q=7 (mod 8)`, so `(2/Q)=1`.  Therefore `(h/Q)=1` as a Jacobi symbol.
The second identity in (M1) gives

```
(p/Q)=(-4hr^2/Q)=-1.
```

Since `p=1 (mod 4)`, reciprocity now gives `(Q/p)=-1`.  Also `hr^2<a<p/2`,
so `QR=p+4hr^2<3p`; because `R>=3`, this implies `Q<p`.  Thus `Q` occurs in
the defining set for `m_p`, and

```
j=(Q+1)/4 >= J_p.                                      (M2)
```

### 3.2 The inequality

Put `y=r/lambda`.  Then

```
R=a/j+y,   y<=j,   jy=hr^2<a.                           (M3)
```

For every real, hence every integral, `J` with `1<=J<=j`, one has

```
R <= a/J+J.                                             (M4)
```

The required proof uses the radical that disappeared in the pasted rendering.
If `j<=sqrt(a)`, then `a/x+x` decreases on `[J,j]`, and (M3) gives

```
R <= a/j+j <= a/J+J.
```

If `j>=sqrt(a)`, then `y<a/j`, so

```
R < 2a/j <= 2sqrt(a) <= a/J+J.
```

Substitution of `R=4a-p` in (M4) is exactly

```
(4J-1)a <= J(p+J).                                      (M5)
```

Equality cannot arise in the second case.  In the first case equality forces
`y=j`, hence `h lambda^2=1`, and also `j=J`.  Thus

```
h=lambda=1,  r=J,  p=(4J-1)s-J.                         (M6)
```

For a hard prime, take `J=3` in (M5):

```
11a <= 3(p+3),              11R <= p+36.                (M7)
```

The stated equality example is correct:

```
p=1009, (a,R,u,h,r,s,lambda)=(276,95,9,1,3,92,1).
```

It has `m_p=11`, `J_p=3`, and `11*276=3*(1009+3)`.  The exact returned
denominators are

```
(276, 92828, 3027),
```

and cross-multiplication verifies the unit-fraction identity.

## 4. Exterior localization

For an exterior state define

```
delta=kappa-r,
D=(r+kappa)/s=(4u+1)/R,
H=h delta^2,
b=(H+1)/D,
g=p-2a.
```

Since `R<p`, the equation `R kappa=pr+s` gives `delta>0`.  Direct
substitution, with no discarded sign, proves

```
sD=2r+delta,
bD=H+1,
p=hs^2D-b,
g=hs delta-b.                                           (E1)
```

In particular `b` is a positive integer.  Eliminating `sD` and then `hs delta`
gives the exact identity

```
p = 2g + g^2/b + (g+b)^2/(bH).                          (E2)
```

Also `D=3 (mod 4)`, because `RD=4u+1`, `R=3 (mod 4)`.

### 4.1 Why `h` is a nonresidue

For every prime factor of `u`, primewise reciprocity using
`R=-p (mod ell)`, `p=1 (mod 4)`, and `R=3 (mod 4)` gives

```
(u/R)=(u/p).
```

The factor two obeys the same equality because both `p` and, when needed,
`R` give symbol `+1` at two.  The exterior gate gives

```
(u/R)=(-1/R)=-1.
```

Since `u=hr^2`, it follows that `(h/p)=-1`.  As `1<=h<p`,

```
h>=nu_p.                                                 (E3)
```

### 4.2 The boundary-gap estimate

If `a<=p/3`, then `g>=p/3` and `(g+1)^2>p+1`; this is stronger than the
desired estimate.  Assume henceforth `a>p/3`.  Algebra gives

```
3a-p = s[hr(3r-kappa)+1]/(r+kappa).                     (E4)
```

Positivity forces `kappa<=3r`.  Equality would make both `s/(4r)` and
`4r/s` integers; using `gcd(r,s)=1` gives `r=1,s=4`, and then
`p=12h-1=3 (mod 4)`, a contradiction.  Hence `delta<2r`.  From (E1),

```
D(g-b)=h delta(2r-delta)-2>0,                            (E5)
```

where the strict inequality uses (E3).  Thus `1<=b<g`; in particular the odd
integer `g` is at least three.

Because `D` is odd, `b` and `H` have opposite parity.  If `b` is odd, then
`H` is even.  When `delta` is odd, `h` is even and `h/2` remains a nonresidue
because `(2/p)=1`, hence `H>=2nu_p`; when `delta` is even,
`H>=4nu_p`.  Thus the odd case always has `H>=2nu_p`.  If `b` is even, then
`b>=2` and `H>=nu_p` (if `H>=p` this is immediate; otherwise it is itself a
nonresidue).

For fixed `c>0`,

```
2g + g^2/b + (g+b)^2/(bc)
```

strictly decreases on `1<=b<=g`; its derivative is
`1/c-(1+1/c)g^2/b^2<0`.  Therefore (E2) is at most

```
F1=2g+g^2+(g+1)^2/(2nu_p)        (b odd),
F2=2g+g^2/2+(g+2)^2/(2nu_p)      (b even).
```

Moreover

```
F1-F2=(nu_p g^2-2g-3)/(2nu_p)>0.
```

Thus `p<=F1`, which is equivalent to

```
2nu_p(p+1) <= (2nu_p+1)(g+1)^2.                         (E6)
```

Recalling `g=p-2a` gives exactly the exterior gap theorem in the session.
Equality requires

```
b=1, h=2nu_p, delta=1, D=2nu_p+1.                      (E7)
```

The example

```
p=41, nu_p=3, (a,R,u,h,r,s,kappa)=(18,31,54,6,3,1,4)
```

satisfies all these equalities and returns `(18,24,2952)`.

For a hard prime, `nu_p>=11` in (E6) gives

```
22(p+1) <= 23(p-2a+1)^2.
```

## 5. Removing the elementary endpoint

If `p+1` has a prime factor `ell=3 (mod 4)`, then

```
R=ell,  a=u=(p+ell)/4,  (h,r,s,kappa)=(a,1,1,(p+1)/ell)
```

is an original first-half exterior state and gives denominators
`(a,a kappa,pa kappa)`.  If `ell` is the least such factor, then
`ell^2<=(p+1)/2`: the odd number `(p+1)/2=1 (mod 4)` contains an even number
of `3 (mod 4)` prime factors counted with multiplicity.

Now suppose `p+1` has no prime factor `3 (mod 4)`.  The case `b=1` in (E1)
would give `p+1=hs^2D`, impossible because `D=3 (mod 4)`.  Hence `b>=2`.
The even case remains bounded by `F2`; in the odd case `b>=3` and

```
F3=2g+g^2/3+(g+3)^2/(6nu_p) < F2.
```

Consequently

```
2nu_p(p+2) <= (nu_p+1)(g+2)^2.                          (E8)
```

Equality in (E8) would force

```
b=2, h=H=nu_p, delta=1, D=(nu_p+1)/2,
nu_p=2D-1, p+2=nu_p D s^2.                              (E9)
```

Every prime `ell|D` is below `nu_p`, hence `(ell/p)=1`.  Reciprocity and
`p=-2 (mod ell)` imply `(-2/ell)=1`, so every such prime is `1` or `3 (mod 8)`
and therefore `D=1` or `3 (mod 8)`.  On the other hand `s` is odd and (E9)
modulo eight gives

```
3 = nu_p D = (2D-1)D = 2-D (mod 8),
```

so `D=7 (mod 8)`, a contradiction.  Equality is impossible.  The exact
unconditional disjunction is therefore:

```
the endpoint construction gives an ES solution,
or 2nu_p(p+2) < (nu_p+1)(p-2a+2)^2 for every exterior state.
```

For a hard prime this implies the stated strict specialization

```
11(p+2) < 6(p-2a+2)^2.                                  (E10)
```

## 6. Reciprocal exterior coordinate

Since `a=hrs` and `u=hr^2`,

```
u=a^2/(hs^2) <= a^2/nu_p.
```

Thus

```
D=(4u+1)/R
 <= ((p+R)^2+4nu_p)/(4nu_p R).                          (D1)
```

The right side strictly decreases for `3<=R<p`, because before division by
`4nu_p` its derivative is `1-(p^2+4nu_p)/R^2<0`.  Hence

```
D <= floor(((p+3)^2+4nu_p)/(12nu_p)).                   (D2)
```

At a hard prime this becomes

```
D <= floor(((p+3)^2+44)/132).                           (D3)
```

The claimed equality example is exact:

```
p=1009, (a,R,u,h,r,s,kappa)=(253,3,5819,11,23,1,7736),
D=7759=((1012)^2+44)/132.
```

Its returned denominators are `(253,85096,1974822872)`.  This also confirms
that the additive `4nu_p` in (D1)--(D3) cannot be deleted while retaining the
example.

## 7. Free fourfold fundamental domain

Let `N=pa` and

```
P_R(a)={(b,c): b|N, c|N, R|(b+c)}.
```

The maps

```
S(b,c)=(c,b),   C(b,c)=(N/b,N/c)
```

are commuting involutions.  Complementation preserves the gate because
`N=pa=(2a)^2 (mod R)`.

The action is free:

* `S(b,c)=(b,c)` would give `R|2b`, impossible since `gcd(b,R)=1` and `R>=3`.
* `C(b,c)=(b,c)` would give `b^2=N` (and `c^2=N`), impossible because
  `v_p(N)=1`.  This is the subcase omitted from the pasted prose.
* `SC(b,c)=(b,c)` would give `bc=N` and then
  `b^2=-N=-4a^2 (mod R)`, making `-1` a square modulo `R`.  An integer
  `R=3 (mod 4)` has a prime `3 (mod 4)` to odd exponent, so this is impossible.

Every orbit has exactly one representative satisfying

```
b<c,  bc<N.                                              (F1)
```

Indeed the products of a pair and its complement are `bc` and `N^2/(bc)`;
exactly one is below `N`, and the swap selects its increasing order.  The
smaller coordinate is `<sqrt(N)<p`, so it divides `a` rather than carrying the
factor `p`.  Splitting according as the larger coordinate does or does not
carry `p` proves the exact decomposition

```
T_R(a)=4(M_a+E_a),                                      (F2)
M_a=#{b<c: b|a,c|a,R|(b+c)},
E_a=#{b|a,d|a: bd<a,R|(b+pd)}.
```

The primitive fibres also agree.  For a middle state with `r<s`, each
`d|h` gives one fundamental representative `(dr,ds)`, hence

```
M_a = sum_(middle states r<s) tau(h).
```

For an exterior state, the fundamental representative is selected from the
paired divisors `d` and `h/d` according as `d^2<h`.  Since `(h/p)=-1`, `h` is
not a square, so

```
E_a = (1/2) sum_(exterior states) tau(h).
```

Equivalently, weighting each fundamental representative by `2/tau(h)` returns
the full oriented state count: a middle state with `r<s` represents its two
orders, while an exterior state has its retained orientation.

On a four-element orbit, the sum map `Z^4 -> Z` has kernel generated by three
differences from a chosen representative.  The coordinates consisting of the
sum and those three differences invert integrally on the image lattice

```
sum-d2-d3-d4 = 0 (mod 4).
```

This is the precise typed version of the claimed integral inverse.

## 8. The two empty minimal lanes at `p=2521`

Direct Euler-criterion calculation gives

```
nu_p=m_p=11,  J_p=3.
```

### 8.1 Exterior lane `h=11,s=1`

Here `a=11r` and `R=44r-p`.  The exterior gate is equivalent to

```
R | p^2+44,   R=-p (mod 44),   0<R<p.                   (L1)
```

For `p=2521`,

```
p^2+44 = 6355485 = 3^2*5*141233.
```

Complete trial division through `floor(sqrt(141233))=375` gives no divisor,
so `141233` is prime.  The divisors of `p^2+44` below `p` are exactly

```
1,3,5,9,15,45.
```

But `-p=31 (mod 44)`, and none of these six divisors is `31 (mod 44)`.
Thus the exterior minimal lane is empty.

### 8.2 Middle lane `hr lambda=3`

The only triples are

```
(h,r,lambda)=(3,1,1),(1,3,1),(1,1,3).
```

The equation `(4hr lambda-1)s=p lambda+r` would require, respectively,

```
11|(p+1),  11|(p+3),  11|(3p+1).
```

Their remainders are `3,5,7`; the lane is empty.

Nevertheless the recorded state

```
(a,R,u,h,r,s,lambda)=(636,23,8,2,2,159,7)
```

is valid.  It has `j=28`, `Q=111`, and returns exact denominators

```
(636,5611746,70588).
```

Thus failure of the smallest admissible `Q=11` lane is not failure of the
middle channel.

## 9. Odd-square two-colour obstruction

Let `n=t^2>1` be an odd square, choose

```
n/4<a<n/2,  gcd(n,a)=1,  R=4a-n,
```

and consider only

```
{n^epsilon d : d|a, epsilon in {0,1}}.                  (C1)
```

For every odd prime `q|a`, `R=-n (mod q)` and `n` is a nonzero square modulo
`q`.  Since `R=3 (mod 4)`, reciprocity gives `(q/R)=1`.  If `2|a`, then
`R=7 (mod 8)`, so `(2/R)=1`.  Hence every `d|a` is Jacobi-positive modulo
`R`; `n` is positive as an actual square.  Every member of (C1) therefore has
Jacobi symbol `+1`.  An opposite pair would satisfy `b=-c (mod R)` and hence

```
(b/R)=(-1/R)(c/R)=-(c/R),
```

a contradiction.  The two-colour source is empty of targets at every such
shell.

This does not give a composite counterexample to ES, because (C1) is not the
complete divisor set of `na`.  At

```
n=25, a=7, R=3,
```

the restricted source is `{1,7,25,175}`.  It omits the divisor `5`; the full
pair `(1,5)` has `k=(1+5)/3=2` and returns

```
4/25 = 1/7 + 1/350 + 1/70.
```

Thus this is an exact counterexample only to a **prime-free two-colour
positivity argument**, not to Erdős--Straus.

## 10. Independent finite checks

An independent standard-library enumeration, not importing the supplied Turn
6 verifier, checked every `p=1 (mod 8)` prime through `1000`:

```
37 primes, 4388 first-half shells,
293 ordered-normalized middle states (r<s),
474 exterior states,
74 endpoint-excluded exterior states.
```

For every enumerated state it checked the exact normalizations, the Legendre
and Jacobi conclusions, (M5), (E6), (E8) where applicable, (D1), all fourfold
orbits, the uniqueness of (F1), and both fibre-count identities following
(F2).  It also checked separately:

* `nu_41=m_41=3`, `nu_1009=m_1009=11`, and
  `nu_2521=m_2521=11`;
* the five displayed unit-fraction examples by integer cross multiplication;
* the complete trial-division primality check of `141233`.

These computations are corroborative only; the proofs above establish the
general claims.

## Sources and status

The Type I/II coordinate framework is due to Christian Elsholtz and Terence
Tao, *Counting the number of solutions to the Erdős--Straus equation on unit
fractions*, Journal of the Australian Mathematical Society 94 (2013), §2,
Propositions 2.2 and 2.6, arXiv:1107.1010. The quadratic-reciprocity input is
classical; a source used by this programme is Allen Hatcher, *Topology of
Numbers* (2022), §6.4, pp. 205--212. The exact original pair fibres and channel
tags are inherited from the preceding channel-coupling proof in
`../es-turn05-channel-coupling-20260919/core.tex`. Every localization identity
used here is rederived above.

## Final status

The localization theorem is a genuine structural result, not a numerical
stamp: it bounds every original middle or exterior state at a prescribed prime
without presupposing a favourable factorization.  It does not prove occupancy
of the remaining region and therefore does not prove Erdős--Straus.  After
restoring the radical/fraction typography, adding the missing complement-fixed
case, and typing the image lattice of the orbit-sum inverse, the audited chain
is proof-complete at the scope it claims.
