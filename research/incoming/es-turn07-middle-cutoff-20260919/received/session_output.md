[**Cumulative source archive: preserved Turn 6 archive plus this Turn 7 continuation**](sandbox:/mnt/data/erdos_straus_cumulative_through_turn7_20260919.zip)

[**Current research package**](sandbox:/mnt/data/es_turn7_middle_cutoff_bundle.zip) · [Complete proof, LaTeX](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/core.tex) · [Compilable manuscript](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/workbench.tex) · [Standard-library verifier](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/verify.py) · [Separate checker](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/check_independent.py)

## Turn 7 continuation: a sharp square-root cutoff, with the existence gap kept separate

The middle channel now has a **complete two-chart atlas indexed by square-root-sized moduli**. For every original middle state at a hard prime, retain its residual \(R\) and its actual cofactor \(Q\). Then

$$
\boxed{
4p\ge 3\min(R,Q)^2+14\min(R,Q)-81.
}
$$

The inequality is attained at the hard prime \(p=1801\).

Consequently, with

$$
\boxed{
K(p)=\left\lfloor\frac{\sqrt{3p+73}-2}{6}\right\rfloor,
\qquad B(p)=4K(p)-1,
}
$$

every middle state is returned from either an original residual \(R\le B(p)\), or a cofactor \(Q\le B(p)\) through its **different, explicitly reconstructed divisor source**.

The distinction between those sources is indispensable. At \(p=2521\), the cofactor chart at \(Q=47\) returns a valid middle state even though the original shell at residual \(47\) has **both channels empty**.

A second theorem rules out a fixed prime-independent cutoff on the original exterior parameter \(h\) and middle parameter \(j=hr\lambda\), even on an explicit infinite progression of primes with known ES solutions.

These are complete reductions and a precise obstruction to a cutoff strategy. **They do not prove that the remaining atlas is occupied for every prime. The universal existence requirement of Turn 7 remains undischarged.**

## 1. The two factors belong to the same original state

Start with an original first-half middle state

$$
\frac p4<a<\frac p2,\qquad
R=4a-p,\qquad
u\mid a^2,\qquad R\mid u+a.
$$

Choose the orientation \(u<a\), retaining the complementary divisor \(a^2/u\) and the corresponding swap of the last two denominators.

With

$$
g=\gcd(a,u),\qquad
(h,r,s)=\left(\frac{g^2}{u},\frac ug,\frac ag\right),
\qquad
\lambda=\frac{r+s}{R},
$$

we have

$$
a=hrs,\qquad u=hr^2,\qquad \gcd(r,s)=1,\qquad r<s,
$$

and the ordered solution is

$$
\boxed{
\frac4p
=
\frac1a+\frac1{phs\lambda}+\frac1{phr\lambda}.
}
$$

The ordered inverse remains

$$
u=\frac{pa^2}{Ry-pa}.
$$

These are the inherited Type-II coordinates, rather than a new parametrization (Elsholtz & Tao, 2013, §2, Proposition 2.6). The preceding localisation proof retains the same normalization and orientation. 

Define

$$
j=hr\lambda,\qquad
Q=4j-1,\qquad
A=h\lambda^2.
$$

The original equations give

$$
\boxed{
RQ=p+4hr^2,\qquad
Qs=p\lambda+r,\qquad
Q+1<2AR.
}
$$

The strict inequality is exactly \(r<s\).

Both \(R\) and \(Q\) are \(3\bmod4\) and lie below \(p\): since \(hr^2<a<p/2\),

$$
RQ=p+4hr^2<3p,
$$

and \(R\ge3\). No coprimality between \(R\) and \(Q\) is assumed.

The useful exact equation is

$$
\boxed{
p=RQ-\frac{(Q+1)^2}{4A}.
}
$$

It retains the full integer \(A=h\lambda^2\). Replacing \(A\) by an arbitrary real parameter would lose the exceptional cases that determine the sharp bound.

## 2. The square-root bound and its hard-prime refinement

Let

$$
t=\min(R,Q).
$$

### General bound

For every prime \(p\equiv1\pmod8\),

$$
\boxed{4p\ge3t^2+6t-25.}
$$

Equivalently,

$$
\boxed{
t\le4\left\lfloor\sqrt{\frac{p+7}{12}}\right\rfloor-1.
}
$$

Suppose first that \(A\ge2\). If \(Q=t\), then \(R\ge t\), so

$$
p\ge t^2-\frac{(t+1)^2}{4A}
\ge\frac{7t^2-2t-1}{8}.
$$

If \(R=t\), the function

$$
tQ-\frac{(Q+1)^2}{4A}
$$

is increasing throughout the actual range \(Q+1<2At\). Setting \(Q=t\) gives the same bound.

Its excess over the proposed lower bound is

$$
\frac{7t^2-2t-1}{8}
-\frac{3t^2+6t-25}{4}
=
\frac{(t-7)^2}{8}\ge0.
$$

It remains to handle \(A=1\). Here \(h=\lambda=1\), so

$$
Q=4r-1,\qquad R=r+s.
$$

The tie \(R=Q\) would imply

$$
s=3r-1,\qquad p=(2r-1)(6r-1).
$$

For prime \(p\equiv1\pmod8\), this is impossible: the only prime possibility with \(r=1\) is \(p=5\).

If \(Q=t<R\), their congruences give \(R\ge t+4\), hence

$$
p\ge\frac{3t^2+14t-1}{4},
$$

which is stronger.

If \(R=t<Q\), write

$$
Q=t+4k,\qquad 1\le k\le\frac{t-3}{4}.
$$

Then

$$
\boxed{
p=f_t(k):=
\frac{3t^2+(8k-2)t-(4k+1)^2}{4}.
}
$$

This is concave in \(k\), so its minimum occurs at an endpoint. At \(k=1\), it gives the stated bound. At the other endpoint,

$$
f_t\!\left(\frac{t-3}{4}\right)=t^2-t-1,
$$

whose excess is

$$
\frac{(t-3)(t-7)}4\ge0.
$$

Equality occurs at \(p=41\), in two original states:

$$
(h,r,s,\lambda)=(1,3,4,1)
$$

and

$$
(h,r,s,\lambda)=(2,1,6,1).
$$

Both have \(a=12\) and \(t=7\); the second has \(R=Q=7\).

### Hard-prime bound

For

$$
p\bmod840\in\{1,121,169,289,361,529\},
$$

the stronger inequality is

$$
\boxed{4p\ge3t^2+14t-81.}
$$

For \(A\ge2\), the excess of the preceding estimate over this new bound is

$$
\frac{(t-7)(t-23)}8.
$$

It is nonnegative for \(t\ge23\). For \(t\le23\), the proposed lower bound is at most \(457\), whereas every hard prime is at least \(1009\). Thus this case is settled strictly.

For \(A=1\), the case \(Q=t<R\) exceeds the new bound by \(20\). In the remaining concave calculation, \(k=1\) would give

$$
p=12(r-1)^2-7\equiv2\pmod3,
$$

which is excluded at a hard prime. Therefore \(k\ge2\).

The first remaining endpoint gives

$$
f_t(2)=\frac{3t^2+14t-81}{4}.
$$

The other endpoint has excess

$$
\frac{(t-7)(t-11)}4\ge0.
$$

The small equality case at \(t=11\) produces \(p=109\), outside the hard classes.

Accordingly, equality in the hard-prime theorem requires

$$
\boxed{
h=\lambda=1,\qquad Q=R+8,\qquad
s=3r-9,\qquad p=12r^2-40r+9.
}
$$

At

$$
\boxed{
p=1801,\qquad
(a,u,R,Q,h,r,s,\lambda)
=
(462,196,47,55,1,14,33,1),
}
$$

the bound is attained and the ordered identity is

$$
\boxed{
\frac4{1801}
=
\frac1{462}+\frac1{59433}+\frac1{25214}.
}
$$

The integer family

$$
r=14+210n,\qquad s=3r-9,\qquad n\ge0,
$$

has \(p\equiv121\pmod{840}\) and attains the same equality. No infinitude of prime values of that quadratic is asserted.

The hard-prime hypothesis matters. At \(p=193\), the valid middle state

$$
(h,r,s,\lambda)=(2,2,13,1)
$$

has \(R=Q=15\) and violates the refined inequality. The general bound remains valid.

## 3. A complete, disjoint two-chart atlas

The bound has an original-coordinate inverse; it is not merely a size observation.

For a hard prime, put

$$
K=K(p),\qquad B=4K-1.
$$

**The direct chart** consists of

$$
3\le R\le B,\qquad R\equiv3\pmod4,\qquad a=\frac{p+R}{4},
$$

$$
u\mid a^2,\qquad u<a,\qquad R\mid u+a,
$$

followed by

$$
Q=\frac{p+4u}{R},
$$

and the retained condition

$$
R\le Q.
$$

**The cofactor chart** consists of

$$
1\le j\le K,\qquad Q=4j-1,
$$

$$
u\mid j^2,\qquad Q\mid p+4u,\qquad
R=\frac{p+4u}{Q}>Q.
$$

Its exact inverse is

$$
\boxed{
g=\gcd(j,u),\qquad
h=\frac{g^2}{u},\qquad
r=\frac ug,\qquad
\lambda=\frac jg,\qquad
s=R\lambda-r,
}
$$

$$
\boxed{a=Rj-u=hrs.}
$$

The square-divisor cofactor condition itself belongs to the classical Mizony/Thépault and Rosati–Yamamoto Type-II lineage. The calculation here concerns the sharp cutoff, its disjoint use with the original residual chart, and the complete return. It is not a claim to have invented that parametrization.

### Why the cofactor inverse is available

The condition \(u\mid j^2\) proves, prime by prime, that \(h=g^2/u\) is a positive integer. It gives

$$
j=hr\lambda,\qquad u=hr^2,\qquad \gcd(r,\lambda)=1.
$$

The cofactor equation becomes

$$
p=4hr(R\lambda-r)-R,
$$

so \(a=hrs\).

The cutoff also supplies the required inequalities. From \(j\le K\),

$$
p\ge12j^2+8j-23,
$$

and therefore

$$
p>4j^2-2j.
$$

For \(j=1\), this follows directly from \(p\ge1009\).

Since \(u\le j^2\),

$$
jp>u(4j-2),
$$

which implies

$$
Rj>2u.
$$

Thus \(u<a\) and \(s>r>0\).

Similarly,

$$
p(Q-1)>4u,
$$

so \(R<p\). Both \(R,Q\) are \(3\bmod4\), and hence

$$
\frac p4<a<\frac p2.
$$

Finally, a prime dividing \(r\) and \(R\) would divide \(p\), but \(r\le j<p\). Therefore

$$
\gcd(r,s)=\gcd(r,R\lambda)=1.
$$

The inverse returns precisely the original state. Conversely, every original state satisfies \(u\mid j^2\), because

$$
\frac{j^2}{u}=h\lambda^2.
$$

The sharp bound puts either \(R\) or \(Q\) in the declared range.

The inequalities \(R\le Q\) and \(Q<R\) make the charts disjoint. The tie is counted once. Restoring the recorded orientation gives the complete original middle source, including both ordered denominator returns.

### The two exponent boxes must remain distinct

The cofactor input is

$$
u\mid j^2.
$$

Its output is the different integer \(a\) and the original condition

$$
u\mid a^2.
$$

The retained integer \(u\) connects them; their prime factorizations are not silently identified.

At \(p=2521\),

$$
\boxed{
(a,R,Q,u,h,r,s,\lambda,j)
=
(644,55,47,16,1,4,161,3,12)
}
$$

is a valid cofactor-chart state. In particular, \(u=16\) divides \(12^2\) but does not divide \(12\). A divisor-only replacement would lose it.

The original shell at residual \(47\), however, has

$$
a'=\frac{2521+47}{4}=642=2\cdot3\cdot107.
$$

Its 27 square-divisor residues modulo \(47\) are obtained by multiplying

$$
\{1,3,9,2,6,18,4,12,36\}
$$

by \(1,13,28\). None equals its middle target \(16\) or exterior target \(35\).

Thus:

$$
\boxed{
\text{a small cofactor certificate is not an occupied original shell
at that cofactor.}
}
$$

The valid return uses the \(j^2\)-source and the displayed inverse.

An actual hard-prime tie is

$$
p=8929,\qquad
(a,u,h,r,s,\lambda)=(2256,24,24,1,94,1),
$$

with

$$
R=Q=95.
$$

The repeated cofactor is retained, not removed by an unjustified coprimality condition.

## 4. The finite candidate domain is explicit

There are \(K(p)\) possible small residuals and \(K(p)\) possible small cofactors.

The direct chart requires at most

$$
\frac12\sum_{j=1}^{K(p)}
\left[
\tau_{\mathrm{div}}\!\left(
\left(\frac{p+4j-1}{4}\right)^2
\right)-1
\right]
$$

original divisor tests. The subtraction removes the impossible middle fixed point \(u=a\); complementation retains the other orientation.

The cofactor chart has the uniform candidate bound

$$
\boxed{
\sum_{j\le K}\tau_{\mathrm{div}}(j^2)
\le K\left(\sum_{d\le K}\frac1d\right)^2
\le K(1+\log K)^2.
}
$$

Indeed,

$$
\tau_{\mathrm{div}}(j^2)
=
\sum_{d\mid j}2^{\omega(d)}
\le d_3(j),
$$

and

$$
\sum_{j\le K}d_3(j)
=
\sum_{abc\le K}1
\le
K\left(\sum_{a\le K}\frac1a\right)^2.
$$

This changes the middle-state decision domain from a linear number of original residuals to two square-root-length lists. It does not claim polynomial-time factorization, nor that either list necessarily contains a hit.

## 5. A fixed original-grade cutoff cannot resolve the remaining existence step

There is a useful unconditional obstruction to one possible next shortcut.

### Fixed-grade obstruction theorem

For every integer \(B\ge1\), there are infinitely many hard primes \(p\) such that

$$
\boxed{
\text{every E state has }h>B,
\qquad
\text{every oriented M state has }j=hr\lambda>B.
}
$$

These primes nevertheless have explicit endpoint E solutions.

Choose a prime

$$
q\equiv3\pmod4,\qquad q>\max(7,4B),
$$

and put

$$
L=8\prod_{\substack{\ell<q\\ \ell\ \mathrm{odd\ prime}}}\ell.
$$

The conditions

$$
\boxed{
p\equiv1\pmod L,\qquad p\equiv-1\pmod q
}
$$

define a reduced residue class modulo \(Lq\). Dirichlet’s theorem supplies infinitely many primes \(p>q\) in that class (Sutherland, 2017, Theorem 18.1). They are \(1\bmod840\).

Every prime below \(q\) is a quadratic residue modulo \(p\), by reciprocity and the supplementary law for two. But

$$
\left(\frac qp\right)
=
\left(\frac pq\right)
=
\left(\frac{-1}{q}\right)
=-1.
$$

Therefore

$$
\boxed{\nu_p=m_p=q.}
$$

Every exterior state has \((h/p)=-1\), so

$$
h\ge q>B.
$$

Every middle cofactor satisfies

$$
Q=4hr\lambda-1\equiv3\pmod4,\qquad
\left(\frac Qp\right)=-1.
$$

Hence

$$
Q\ge m_p=q,\qquad
j=\frac{Q+1}{4}>B.
$$

Nevertheless, \(q\mid p+1\) gives the original endpoint state

$$
R=q,\qquad a=u=\frac{p+q}{4},\qquad
h=a,\qquad r=s=1,\qquad
\kappa=\frac{p+1}{q},
$$

and

$$
\boxed{
\frac4p
=
\frac1a+\frac1{a\kappa}+\frac1{pa\kappa}.
}
$$

This is a consequence of classical reciprocity and Dirichlet, with the original grades made explicit. It is not a historical-priority claim.

Its scope is narrow and important. It excludes a prime-independent bound on **these two parameters**. It does not exclude a \(p\)-dependent bound, a bound relative to \(\nu_p\) or \(J_p\), a different selector, or a useful theorem in the endpoint-free branch. The constructed primes are deliberately endpoint-soluble.

## 6. Status of the unbounded step

The completed mathematical reduction is

$$
\boxed{
\text{every original M state}
\longleftrightarrow
\text{one of two explicit square-root-modulus charts}.
}
$$

The fixed-grade theorem shows why replacing the moving domain by a constant \(h/j\) inventory cannot be universal.

What remains is still

$$
\boxed{
\forall p\text{ hard prime},\quad
\text{at least one original E or M coefficient is positive}.
}
$$

The two-chart algorithm may decide that its middle source is empty. That would concern Type II at that prime; the exterior source must still be examined. A proof that the middle atlas is always occupied would itself prove the stronger Type-II conjecture.

Accordingly, this continuation is **not** being marked as completion of Turn 7. It supplies a sharp finite per-input reduction and excludes a specific fixed-cutoff route, while leaving the universal positivity assertion explicit.

The remaining-source handoff is in [HANDOFF_TURN_7_REMAINDER.md](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/HANDOFF_TURN_7_REMAINDER.md). The [map register](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/MORPHISMS.md) records the original and cofactor exponent boxes, both orientations, the tie locus and the denominator inverse.

### Reproduction and publication record

The supplied main verifier compares the complete first-half middle source with the two-chart atlas at every prime \(p\equiv1\bmod8\) through its declared bound. The separate implementation enumerates primitive \((h,r,s)\) parameters directly and imports neither the main code nor predecessor software.

```sh
python verify.py --bound 3000 --out certificates
python -O verify.py --bound 3000 --out certificates_optimized
python check_independent.py --input certificates \
  --out certificates/independent.json
```

The fixed-grade example uses a separate partial-factor order certificate for primality; its probable-prime discovery screen is not the proof.

[Command-status record](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/execution_status.json) · [Source ledger](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/source_reading.json) · [Lean-ready dependency plan](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/lean_plan.md) · [Publication record](sandbox:/mnt/data/es_turn7_middle_cutoff_20260919/publication_receipt.json)

I am not reporting a confirmed numerical replay total, rendered-PDF inspection, or remote pull request from this continuation. The cumulative source archive preserves the preceding archive rather than asserting a fresh audit of all its mathematics. No universal ES proof, independent mathematical review, Lean build or new overall verification range is claimed.


