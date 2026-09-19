[**Rebuilt Turn 6–7 archive: recovered sources, the new continuation, LaTeX and executable certificates**](sandbox:/mnt/data/ES_Turns_6_7_Validated_Handoff_20260919.zip)

[Archive manifest and execution-status receipt](sandbox:/mnt/data/ES_Turns_6_7_Validated_Handoff_Receipt.json) · [New complete proof, LaTeX](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/core.tex) · [Compilable manuscript](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/workbench.tex) · [Standalone preprint, LaTeX](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/preprint.tex)

**This remains Turn 7.** Turn 6 completed its full-source investigation, and the preceding Turn 7 result completed the middle-channel square-root atlas. Neither proved universal occupancy. The earlier proof explicitly distinguishes its complete finite atlas from the remaining existence assertion. 

I have therefore not advanced to Turn 8 as though a universally successful selector existed. The continuation supplies the missing counterpart on the **exterior channel**: a complete three-chart atlas with an explicit \(O(p^{2/3})\) bound on its indexing parameters, an exact integer inverse in every chart, and a family showing that the resulting integer cutoff is sharp.

The new archive has a different filename from the broken links. Its manifest was checked against the bytes included in that archive. Recovered historical files, newly executed results and the present proof remain separately identified; archive integrity is not presented as a fresh audit of every historical theorem.

## 1. The exterior channel has a third useful arithmetic parameter

Start from an original exterior state

$$
\frac p4<a<\frac p2,\qquad
R=4a-p,\qquad
u\mid a^2,\qquad R\mid4u+1,
$$

where \(p>1\), \(p\equiv1\pmod4\), and \(\gcd(p,a)=1\). Primality is not needed for the first bound.

Retain the original normalization

$$
g=\gcd(a,u),\qquad
(h,r,s)=\left(\frac{g^2}{u},\frac ug,\frac ag\right),
\qquad
\kappa=\frac{pr+s}{R}.
$$

Then

$$
a=hrs,\qquad u=hr^2,\qquad \gcd(r,s)=1,
$$

and the ordered return is

$$
\boxed{
\frac4p
=
\frac1a+\frac1{hs\kappa}+\frac1{phr\kappa}.
}
$$

The original divisor is recovered from the ordered denominators by

$$
u=\frac{a^2}{Ry-pa}.
$$

Now retain two additional coordinates:

$$
\boxed{
v=\frac{a^2}{u}=hs^2=Ry-pa,
\qquad
D=\frac{4u+1}{R}=\frac{r+\kappa}{s}.
}
$$

These are not independent auxiliary choices. They are calculated from the same original state.

The exact identities are

$$
\boxed{
pD+1=4hr\kappa,
}
$$

$$
\boxed{
(p+R)^2+4v=4vRD,
}
$$

and

$$
\boxed{p+R<2vD.}
$$

The last inequality is equivalent to \(r<\kappa\), which follows from the original first-half range.

Both \(R\) and \(D\) are \(3\pmod4\). Furthermore,

$$
h>1,\qquad \gcd(h,R)=\gcd(h,D)=1.
$$

Indeed, \(h=1\) would make \(-1\) a square modulo \(R\equiv3\pmod4\). Consequently,

$$
\boxed{v\ne R,\qquad v\ne D.}
$$

This does **not** imply \(\gcd(v,D)=1\). The factor \(s^2\) can overlap \(D\); the proof and verifier retain that possibility.

The Type I/II parametrization is inherited arithmetic in the Elsholtz–Tao framework. The continuation concerns the bound on these three jointly retained coordinates and their complete inverse charts, not a claim to have invented the underlying parametrization.

## 2. A strict cubic cutoff for every original exterior state

Put

$$
w=\min(v,R,D).
$$

### Exterior cutoff theorem

Every state in the stated unit integer domain satisfies

$$
\boxed{
(p+w)^2>4(w+1)^2(w-1).
}
$$

Define \(C(p)\) to be the largest positive integer satisfying that inequality. Then

$$
\boxed{
\min\!\left(\frac{a^2}{u},R,\frac{4u+1}{R}\right)\le C(p)<p,
}
$$

and

$$
\boxed{
C(p)=\left(\frac p2\right)^{2/3}+O(p^{1/3}).
}
$$

The cutoff is calculated by exact integer comparisons and binary search. No floating-point root determines whether a state is retained.

### Proof

Let

$$
t=\min(R,D).
$$

If \(R=t\), the norm identity gives

$$
(p+t)^2\ge4v(t^2-1).
$$

If \(D=t\le R\), calculate

$$
\begin{aligned}
(p+t)^2-4v(t^2-1)
&=(R-t)(4vt-2p-R-t)\\
&\ge0.
\end{aligned}
$$

The second factor is positive by \(p+R<2vt\). Thus in either case

$$
\boxed{p\ge2\sqrt{v(t^2-1)}-t.}
$$

There are two possibilities, since \(v\ne t\).

If \(v>t\), then \(v\ge t+1\) and \(w=t\). Hence

$$
p\ge2(w+1)\sqrt{w-1}-w.
$$

Equality would require the rational number \(\sqrt{w-1}\) to be an integer. But \(w=t\equiv3\pmod4\), so \(w-1\equiv2\pmod4\), which is not a square. The inequality is strict.

If \(v<t\), then \(w=v\) and \(t\ge w+1\). The expression

$$
2\sqrt{w(t^2-1)}-t
$$

is increasing in \(t\), giving

$$
p\ge2w\sqrt{w+2}-w-1.
$$

This is strictly greater than

$$
2(w+1)\sqrt{w-1}-w.
$$

For an explicit check, set

$$
U=w\sqrt{w+2},\qquad V=(w+1)\sqrt{w-1}.
$$

Then

$$
U^2-V^2=w^2+w+1,
\qquad
U+V\le2w(w+1),
$$

so \(U-V>1/2\).

Both cases therefore give

$$
p+w>2(w+1)\sqrt{w-1},
$$

which proves the theorem after squaring.

The right-hand boundary

$$
2(w+1)\sqrt{w-1}-w
$$

is strictly increasing for \(w>1\). At \(w=p\), the required inequality fails because

$$
(p+1)^2(p-1)-p^2=p^3-p-1>0.
$$

This proves \(C(p)<p\). The leading term \(2w^{3/2}\) gives the stated asymptotic.

## 3. The bound produces a complete, disjoint exterior atlas

For the rest of the construction, let \(p\equiv1\pmod4\) be prime and put \(C=C(p)\).

Define

$$
K(v)=\prod_{\ell^e\parallel v}\ell^{\lceil e/2\rceil}.
$$

The original square-divisor condition is exactly

$$
v\mid a^2\iff K(v)\mid a.
$$

Every exterior state belongs to exactly one of the following three charts.

### Direct residual chart

Take

$$
3\le R\le C,\qquad R\equiv3\pmod4,\qquad
a=\frac{p+R}{4},
$$

and retain every

$$
u\mid a^2,\qquad R\mid4u+1.
$$

Compute the original \(D\) and \(v\), and retain

$$
\boxed{R\le D,\qquad R<v.}
$$

This includes an \(R=D\) tie once.

### Reciprocal chart

Take

$$
3\le D\le C,\qquad D\equiv3\pmod4,\qquad
B=\frac{pD+1}{4},
$$

and retain

$$
w\mid B^2,\qquad w<B,\qquad D\mid w+B.
$$

Its exact inverse is

$$
g=\gcd(B,w),\qquad
h=\frac{g^2}{w},\qquad
r=\frac wg,\qquad
\kappa=\frac Bg,
$$

$$
\boxed{
s=\frac{r+\kappa}{D},\qquad
a=hrs,\qquad u=w.
}
$$

Keep the result precisely when

$$
\boxed{D<R,\qquad D<v.}
$$

The source condition makes \(s\) an integer. Moreover,

$$
R\kappa=pr+s>0,
$$

and

$$
\boxed{
D(p-2a)=2hr(\kappa-r)-1>0.
}
$$

Thus the reconstructed state is genuinely in the original first-half range.

Its inverse reads the retained \(D\), reconstructs \(B=hr\kappa\), and returns the selected orientation \(w=hr^2<B\). It does not treat both reciprocal orientations as distinct copies of the same original E state.

### Complement–norm chart

Take

$$
2\le v\le C,
$$

and enumerate the actual divisors

$$
\boxed{
R\mid p^2+4v,\qquad
v<R<p,\qquad
R\equiv-p\pmod{4K(v)}.
}
$$

Set

$$
\boxed{
a=\frac{p+R}{4},\qquad
u=\frac{a^2}{v},\qquad
D=\frac{4u+1}{R},
}
$$

and retain \(v<D\).

The congruence is essential: it is exactly the original condition \(K(v)\mid a\), ensuring that \(u\) is an integer divisor of \(a^2\).

Because \(v<p\) and \(p\) is prime,

$$
\gcd(R,4v)=1.
$$

The identity

$$
4v(4u+1)=(p+R)^2+4v
$$

then shows that \(R\mid p^2+4v\) supplies the actual exterior gate.

The inverse reads the original \(v=a^2/u\) and \(R\). It is not an independent choice of a convenient factor of a norm.

### Completeness and information retained

The cutoff proves that at least one of \(R,D,v\) is at most \(C\). The coordinate \(v\) cannot tie either \(R\) or \(D\). A possible \(R=D\) tie belongs only to the direct chart. The three rules are therefore disjoint and exhaustive.

All three return the original

$$
p,a,R,u,h,r,s,\kappa
$$

and the ordered denominators

$$
(a,hs\kappa,phr\kappa).
$$

The prime-exponent box for \(a^2\), the reciprocal box for \(B^2\), and the norm-factor source are different objects. Their calculated inverses connect them; their factor inventories are not identified.

The outer index lists have \(O(p^{2/3})\) entries. That statement is **not an overall running-time bound**: the reciprocal and norm integers can be larger, and their factorizations and divisor counts remain part of the actual computation.

## 4. The middle cutoff cannot simply be applied to the exterior channel

The preceding middle theorem gives

$$
\min(R,Q)\le
4\left\lfloor\frac{\sqrt{3p+73}-2}{6}\right\rfloor-1
$$

at a hard prime. Its hypotheses and equality case concern the original M cofactor \(Q=4hr\lambda-1\). 

An actual exterior state prevents transferring that conclusion by analogy.

At

$$
\boxed{p=48049\equiv169\pmod{840}},
$$

retain

$$
\boxed{
(a,u,R,D,v,h,r,s,\kappa)
=
(12090,24180,311,311,6045,6045,2,1,309).
}
$$

Here

$$
4u+1=311^2,
$$

and

$$
\boxed{
\frac4{48049}
=
\frac1{12090}
+\frac1{1867905}
+\frac1{179501934690}.
}
$$

The middle cutoff at this prime is \(247\). Both exterior factors \(R,D\) are \(311\).

This is a counterexample to imposing that middle bound on **every exterior state**. It does not rule out a smaller different solution at the same prime, or a different theorem about the existence of a square-root-sized witness.

The third coordinate is also not automatically coprime to the reciprocal factor. At

$$
p=37,\qquad
(a,u,h,r,s,\kappa)=(12,8,2,2,3,7),
$$

one has

$$
v=18,\qquad D=3.
$$

The chart calculations retain this overlap.

## 5. The exterior cutoff is exactly attained on an integer family

For every integer \(n\ge2\), set

$$
\boxed{
h=4n^2-2,\qquad r=n,\qquad s=1,
}
$$

$$
\boxed{
R=D=4n^2-1,\qquad
\kappa=4n^2-n-1,
}
$$

$$
\boxed{
p=16n^3-4n^2-8n+1,\qquad
a=hn,\qquad u=hn^2.
}
$$

These are original unit integer E states:

$$
R=4a-p,\qquad
R^2=4u+1,\qquad
\gcd(p,a)=1,\qquad
\frac p4<a<\frac p2.
$$

Their third coordinate is

$$
v=h=4n^2-2,
$$

so

$$
\min(v,R,D)=h.
$$

In fact,

$$
\boxed{C(p)=h.}
$$

The general theorem proves that \(h\) passes the strict cutoff. On the other hand,

$$
p=2h\sqrt{h+2}-h-1,
$$

whereas the boundary at \(h+1\) is

$$
2(h+2)\sqrt h-h-1>p.
$$

The next integer is therefore excluded.

This proves exact integer sharpness and

$$
\frac{\min(v,R,D)}{(p/2)^{2/3}}\longrightarrow1.
$$

The members \(n=2\) and \(n=4\) give the primes \(97\) and \(929\). Choosing

$$
n=24+210j
$$

puts the integer parameter in the hard class \(289\bmod840\). **No infinitude of prime values in that polynomial family is asserted.** The asymptotic sharpness claim is for the proved unit integer domain, not a secretly assumed prime subsequence.

## 6. What this completes—and what it does not

The current source reduction is now symmetrical in scope, though not in formulas:

$$
\boxed{
\begin{aligned}
M:&\quad\text{complete direct/cofactor atlas with square-root-sized indices};\\
E:&\quad\text{complete direct/reciprocal/complement–norm atlas}\\
&\quad\text{with }O(p^{2/3})\text{ outer indices}.
\end{aligned}}
$$

Both keep the original divisor multiplicities, orientation rules, ties and ordered inverses. Together they give a complete per-prime decision domain.

They do **not** prove that this domain contains a state for every prime. A terminating enumeration can terminate with an empty result; ruling that out remains the unbounded existence step. The earlier Turn 7 source already makes that distinction, and this continuation preserves it rather than silently promoting a cutoff to a selector theorem. 

One concrete obstruction remains visible in the new coordinates. At \(p=2521\), taking the least nonresidue complementary grade \(v=11\) gives

$$
p^2+4v=6355485=3^2\cdot5\cdot141233.
$$

The divisors below \(p\) are

$$
1,3,5,9,15,45,
$$

and none has the necessary residue

$$
R\equiv-p\equiv31\pmod{44}.
$$

Thus selecting the smallest available nonresidue grade does not occupy the norm chart. Its availability congruence cannot be dropped.

The remaining statement is therefore still

$$
\boxed{
\text{For every prescribed hard prime, at least one retained original
E or M coefficient is positive.}
}
$$

The new proof removes a missing exterior-state reduction and supplies exact negative controls. It does not discharge that statement. **Turn 8 is not being started under an assumed universal-existence hypothesis.**

## Reproduction and handoff

The new main verifier compares the three exterior charts with exhaustive original first-half E enumeration. The separate checker enumerates primitive \((h,r,s)\) parameters directly and imports neither the main implementation nor predecessor code.

```sh
python verify.py --bound 3000 --out certificates
python -O verify.py --bound 3000 --out certificates_optimized
python check_independent.py --input certificates \
  --out certificates/independent.json
```

[Main verifier](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/verify.py) · [Separate checker](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/check_independent.py) · [Proof and inverse maps](sandbox:/mnt/data/es_turn6_7_recovery_20260919_v2/exterior_atlas/core.tex)

The archive separates the recovered Turn 6 and Turn 7 source snapshots from this continuation. Its delivery receipt records the actual available recovery, execution and publication results. I have not reused a historical check total as the count for this run, and I am not assigning an unconfirmed remote PR number.

[**Rebuilt archive**](sandbox:/mnt/data/ES_Turns_6_7_Validated_Handoff_20260919.zip) · [**Manifest, recovery and execution-status receipt**](sandbox:/mnt/data/ES_Turns_6_7_Validated_Handoff_Receipt.json)

No universal ES or Type-II positivity theorem, historical-priority determination, independently reviewed proof or Lean build is claimed. The established continuation is a complete exterior atlas with a strict, exactly attained cutoff; the remaining task is still to force an original positive coefficient inside the now fully specified domains.
