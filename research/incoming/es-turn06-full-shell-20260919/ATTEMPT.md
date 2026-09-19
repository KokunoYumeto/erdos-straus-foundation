# Turn 6 attempt record

## Goal and source
Prove positive occupancy of the complete first-half p-coloured divisor-pair sum
for an arbitrary prescribed prime. The Turn 5 handoff and full core were read.
The earlier structural graph escape, reciprocal return, and favourable-factor
packet theorems were not assumed to supply a target.

## Attempt A: principal-character domination of the complete sum
The principal term P_a is explicit and positive. Parseval gives a rigorous lower
bound L_a=2P_a-E_a after every other term is assigned the adverse sign. The new
calculation proves that the complete sum of these lower bounds is instead at
most -p log(p)/24 for every p=1 mod4, p>=2^20. Its cause is quantified: the
original diagonal mass grows at least on a p log(p) scale, whereas the explicit
bound on principal mass is O(p^(2/3) log(p)). The true signed sum cancels the
diagonal exactly. This failure does not settle the true sum.

The same calculation rules out an unweighted/bounded-condition positive-weight
sum of these real bounds for any shellwise adaptive subgroup observations of
index <=J, once p>=2^20 J^3 (with the stated weight-ratio modification).
The theorem does not cover dropping negative bounds or arbitrarily growing
quotient resolution.

## Attempt B: exact integer lower bounds retaining nonprincipal even characters
Instead of ignoring all nonprincipal information, retain the original coset
masses for a chosen B containing -1, together with the exact collision energy.
No saturation is assumed. Balanced antipodal-pair totals give the sharp integer
bound; the free original Klein-four action rounds a positive bound upward to a
multiple of four. Divisor complementation supplies a further convex refinement.
Each positive bound has an original finite pair return, its gcd/channel inverse,
and ordered denominators.

The finite comparison found four complete failures of the principal-only test
through the declared hard-prime bound2m. The new bounds give explicit returns at
all four. This is not new ES verification. At p87481 no nonnegative weighting
of the scalar real or basic integer bounds is positive at any first-half shell.
At p944329,R63 an unsaturated cubic quotient has masses8,8,0 and a sharp target
lower bound8. At another occupied shell of the same prime, R47, no intermediate
subgroup observation is available. A further attempt retained individual even
character modes instead of a complete quotient. Five of23 modes prove T>=60
there, using two exact rational spectral-energy enclosures. This repairs that
specific subgroup limitation; universal spectral selection is not established.

## Discovery boundaries
The discovery search inspected occupied shells in order to choose illustrative
subgroups. The proved inequalities and the released certificate evaluation use
actual coset/collision data; they do not take target membership as an assumption.
The exact target is separately calculated for checking. A further10m probe is
kept in discovery/ only; its larger prime range is not independently replayed in
the proof lane. A discovery-only full-group complement probe at87481 is not
promoted into a new universal or finite theorem.

## Outcome
A theorem at every sufficiently large prescribed prime has been proved, but it
is a quantitative obstruction to a specified proposed lower estimate. The actual
universal positive lower bound is not established. Turn7 must preserve that gap
and attack the diagonal-free signed arithmetic sum or prove an original inventory
that forces a nonterminal quotient certificate, rather than postulate its output.

## Final spectral continuation
The quantitative bounded-resolution obstruction also holds for arbitrary
adaptive sets of at most J even characters, not only character subgroups.
The original p944329,R47 example is certified with principal and two conjugate
pairs; its selected set is not multiplicatively closed. A nine-control verifier
retains this distinction. The proof uses exact arctangent/cosine series; one
early direct Python-function test compared tuples with JSON lists and was
repeated through the actual JSON boundary. It was a test-call type mismatch,
not an arithmetic discrepancy. No floating point enters the final interval proof.

## Effective all-sublinear refinement

For m>=3, let K_m be the product over primes q<2^m of the maximum of
(e+1)^m/q^e for 0<=e<2m, and C_m the least positive integer with C_m^m>=K_m.
The written monotonic-ratio proof gives tau_div(a)<=C_m*a^(1/m) at every a.
If p>=2^20 and p^(1-2/m)>=12*J*C_m^2, the raw complete-sum lower estimate
retaining at most J even modes per shell is <=-p*log(p)/8. The condition can
be checked using only integers as p^(m-2)>=(12*J*C_m^2)^m. For m=4, C_m=9;
thus p>=max(2^20,944784*J^2) suffices. Choosing m with 2/m<delta gives an
explicit onset for every per-shell budget at most p^(1-delta). This is NOT
an obstruction to every algorithm using few modes: zero truncation, integer
refinement, arbitrary sparse shell selection, and additional signed arithmetic
estimates are outside the proved raw-sum bound. The constant checks include
m=3,...,8; the general statement is proved by the all-exponent ratio argument.
