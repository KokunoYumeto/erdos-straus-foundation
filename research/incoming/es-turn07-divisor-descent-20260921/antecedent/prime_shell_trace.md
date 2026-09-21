# Prime-shell trace descent and an exact global denominator cutoff

Status: Turn 7 remains the universal original-source existence task.
The theorem below starts from a rational first-trace candidate; it does not
assert that every prime supplies such a candidate.

## Exact rational source

Let p=1 mod4 be prime, p/4<a<p/2 an integer, and R=4a-p.
Positive rational tails with 1/y+1/z=R/(pa) and integral N=y+z have
b=Ry-pa, c=Rz-pa positive integers satisfying bc=(pa)^2. Their inverse is
y=(pa+b)/R, z=(pa+c)/R. The integral trace condition is exactly
R|(pa+b)^2, equivalently K(R)|(pa+b), where
K(R)=product(l^ceil(e/2)) for l^e||R. The complete original integer gate is
R|(pa+b). These are the predecessor's retained rational-tail coordinates.

Their common reduced denominator d satisfies d^2=R/gcd(R,N). Therefore d is
odd, d^2|R, and 3d^2<=R. For any prime l|d, both y,z have valuation -v_l(d),
as do their differences from a. Since y+z is integral and l is odd,
y-z has the same negative valuation. The monic cubic discriminant consequently
has reduced denominator d^6. For the literal roots p,a,y,z, the five differences
involving y or z have the same negative valuation. The remaining difference
p-a=3a-R has valuation zero at l!=3 and exactly one at l=3. Hence the monic
literal quartic discriminant has denominator d^10/9 if 3|d, and d^10 otherwise.

Thus, on this exact rational domain, integrality of the cubic or monic literal
quartic discriminant is equivalent to integrality of both tails. Every possible
denominator prime is at most floor(sqrt(R/3)), hence at most
floor(sqrt((p-2)/3)). This is a finite per-input integrality test, not a proof
that an integral trace is attained. For the normalized Fabel quartic H=-L/S,
the relevant monic discriminant is S^6 Disc(H); the scale cannot be omitted.

## Complete prime-shell classification

Suppose a=q is prime. Orient y<=z, or b<=c. The only divisors of (pq)^2 at
most pq are 1,q,p,q^2,pq. The trace is N=(pq+b)^2/(Rb).

b=1 is impossible: a prime 3 mod4 dividing R would divide 4q^2+1.
b=q^2 is impossible: its condition forces R|25, inconsistent with R=3 mod4.
b=pq is impossible since gcd(R,2pq)=1.
The remaining two candidates are precisely

1. b=q: (y,z)=(q(p+1)/R,pq(p+1)/R), present iff R|(p+1)^2.
2. b=p: (y,z)=(p(q+1)/R,pq(q+1)/R), present iff R|(p+4)^2.

The reduced denominators are respectively R/gcd(R,p+1) and
R/gcd(R,p+4). The original tails are integral iff R divides the corresponding
unsquared integer. For p=1 mod3 at most one candidate occurs: if both occur,
K(R) divides p+1 and q+1, and also R=4q-p; hence K(R)|3. This gives R=3,
contradicting p=1 mod3.

## Actual same-prime middle return

Write R=delta*t^2, with delta the positive squarefree part (odd exponents,
not the radical). Then delta=3 mod4 and delta<p. In the first branch
delta|p+1. Set j=(delta+1)/4 and c=(p+1)/delta. The original M marking is
(h,r,s,lambda)=(j,1,c,1), a_M=jc, R_M=c+1, u_M=j, Q_M=delta.
The ordered denominators are (jc,pjc,pj).

In the second branch delta|p+4. Set j=(delta+1)/4 and c=(p+4)/delta.
Then a_M=cj-1 and (h,r,s,lambda)=(1,1,a_M,j), R_M=c, u_M=1, Q_M=delta.
The ordered denominators are (a_M,pj*a_M,pj).

In both cases substitution verifies the identity, original divisor gate,
coprimality and first-half range. If the old rational pair was nonintegral,
R is not squarefree; hence delta<R. Thus the new middle cofactor strictly
decreases from the old failed residual, and the construction terminates with
an actual witness. It does not claim that the new residual itself decreases.

Keeping p,q,R,branch and the orientation reconstructs the original rational
source. After these data are forgotten, the complete fibre is described by
R|(p+epsilon)^2, 0<R<p, R=3 mod4, q=(p+R)/4 prime, and the retained squarefree
part delta, with epsilon=1 or4. Distinct source records are not counted as one
until this pushforward is explicitly taken.

## Exact examples and obstruction to unrestricted extension

At p=8929, q=2351, R=475, the sole rational trace pair is
(220994/5,1973255426/5), with tail sum394695284.
The original q-shell has both E and M gates empty. Its squarefree part delta19
returns M(a2350,R471,u5,h5,r1,s470,lambda1), giving
4/8929=1/2350+1/20983150+1/44645.
All printed integers and primality claims are checked by verify.py.

The composite shell p1009,a286,R135 has rational tails
6413/3,168238642/3 with integral first trace. Square stripping to R15,a256
has both gates empty. Thus the prime-shell proof is not asserted for arbitrary a.

At p193,a55,R27,b5 the common tail denominator3 attains d^2=R/3.
This proves sharpness of the residual-dependent square-part cutoff in the
stated prime domain; no prime-asymptotic sharpness claim is made.

At p1009, p+1=2*5*101 and p+4=1013 are supported on primes1 mod4, apart from2.
Consequently no prime distinguished denominator in its entire first-half interval
has an integral rational first trace. The theorem cannot be promoted to universal
occupancy by assuming a prime shell exists.

## Provenance and nonclaims

The rational-tail factor-pair source, common-denominator formula and failed
square-stripping example are from the preceding trace-rigidity tranche, TR17--19.
The original Type-I/II identities are classical: Elsholtz and Tao (2013),
arXiv:1107.1010, Section2, Propositions2.2 and2.6.
All additional calculations above are proved directly. No historical-priority
claim, universal ES theorem, independently reviewed proof, Lean build or new
overall verification range is asserted.
