# Independent coordinate checker for the boundary swap completion

This file records the independent finite checker, the algebra used to
check its formulas, and the complete independent read of the proof source.
The computation does not establish an assertion for unbounded primes.

## Original domain retained in the run

The run includes every prime `p = 12h + 1 <= 2000`, every original shell
`a = 3h + j + 1` with `0 <= j < 6h`, every positive ordered raw factor
triple `(A,B,D)` with `ABD = a`, and both tags `epsilon = 0,1`. It selects
the actual passing tuples using `R C = A + p^(1-epsilon) B`, where
`R = 4j + 3`. No raw scale is discarded from this enumeration. The code
records `k = gcd(A,B)` and checks its complete inverse and its complete
square-divisor fibre over `(A0,B0,C0,D0,epsilon)`.

Every target is calculated using `fractions.Fraction`. All powers occurring
as integer powers have nonnegative exponents; negative exponent ratios are
represented explicitly by `Fraction(p**epsilon,p**eta)`. The implementation
contains no floating-point calculation.

## Independently derived coordinate identities

Because `a < p`, primality of `p` and `R = 4a-p` give
`gcd(a,R) = gcd(p,R) = 1`. In particular `A,B,D,k` are units modulo `R`.
For a source tag `epsilon`, write `q = p^(1-epsilon)`. The source equation
gives `A = -q B (mod R)`. On exchanging or retaining `A,B`, call the new
ordered pair `alpha,beta`; the new tag is `eta`. The forced target
coefficient is `C' = (alpha + p^(1-eta) beta)/R`. Repeating the same pair
exchange and tag change recovers `A,B,epsilon` and then the unique original
`C`; compositions of all four maps are the two bitwise exclusive-or rules.
This is checked on the entire positive rational coefficient domain reached
from every original passing tuple, including targets whose coefficients
are not integers.

The reduced denominator of `C'` is the order of the residue class
`[alpha+p^(1-eta) beta]` mapped from `Z/RZ` to `Q/Z` by `n -> n/R`.
The numerator modulo `R` is, up to multiplication by a unit, zero for the
identity and middle same-tag exchange, `1-p^2` for the exterior same-tag
exchange, and `p-1` for either tag-changing row. Thus the exact orders are
respectively `1`, `R/gcd(R,p^2-1)`, and `R/gcd(R,p-1)`. Multipliers
`p^eta alpha D` and `p beta D` are units modulo `R`; they preserve these
orders for the two target denominators. The checker compares all three
reduced denominators with these independently prescribed orders.

The target ordered denominators and oriented residuals are checked as

```
x' = a,  y' = p^eta alpha C' D,  z' = p beta C' D,
R y' - p a = p^eta alpha^2 D,
R z' - p a = p^(2-eta) beta^2 D.
```

Consequently the original residual product is `(pa)^2`, and the original
ordered unit-fraction identity holds with every target rational coordinate
retained. If `d_z = p^(2-epsilon) B^2 D` and `S = pa`, the exact target
`d_z'` is `p^(2-epsilon-eta) S^2/d_z` for a pair exchange and
`(p^epsilon/p^eta) d_z` for a retained pair. The same-tag exchange therefore
keeps the factor `p^(2-2epsilon)` in front of `S^2/d_z`. In particular an
exterior exchange is not the bare complement. Also `u=B^2D` maps to
`a^2/u` on exchange and to itself on retaining the pair.

The ordered witness inverse first forms the exact reduced ratio
`(R y'-pa)/(pa)`. Its reduced numerator is `alpha/k`, and its denominator
is `p^(1-eta) beta/k`. Whether that denominator is divisible by `p`
recovers `eta`. The product with the original `a` then recovers
`D0 = k^2 D`; the source equation recovers `C'/k`. Retaining `k` recovers
every raw coordinate. All these inverse formulas are checked on rational
targets as well as integral ones.

In either original radix, direct encode/decode checks retain every digit.
Subtracting the two original encoded integers gives
`c'-c = swap*(B0-A0)*(Lambda-2) + (eta-epsilon)`. Since both full and
first-half `Lambda-2 > 1`, the minimum among the admissible four target
codes has the asserted ordered pair and tag. The admissible targets are
stored as a set, so coinciding targets are retained with their correct
point cardinality. For example `p=13,j=1,A=B=1,C=2,D=5,epsilon=0` is a
fixed point of the same-tag pair exchange. This prevents an incorrect
claim that every pair-exchange orbit has two distinct points.

## Completeness checks and results

The raw factor enumeration is independently compared, shell by shell,
with the complete original valuation box of divisors of `a^2`. The latter
is generated from the prime factorization of `a`, selects hits by the
independent congruence `R | 4u+p^epsilon`, and reconstructs
`A0=a/gcd(a,u)`, `B0=u/gcd(a,u)`, `D0=gcd(a,u)^2/u`.
These two enumerations give identical sets of primitive hit coordinates
and encoded integers in every full shell.

The minimum of each complete hit set is also compared with an independent
search in original code order: first `A0`, then `j`, then `B0`, then the
tag. This search excludes all failed budget and coprimality candidates,
without replacing the original order by a shell-first ordering. Every
finite minimum satisfies the exact integral-orbit consequences. The
finite run found a hit in both radices for every included prime; this is
only a statement about the explicitly bounded run.

The successful run through 2000 includes:

- 70 eligible primes and 33,012 original shells;
- 1,070,569 raw factor triples and 2,141,138 raw tagged candidates;
- 3,566 raw passing tuples and 2,895 complete raw scale fibres;
- 14,264 rational map rows and 57,056 composition checks;
- 28,020 original full or first-half code differences;
- 812,698 original square divisors and 33,012 complete shell hit-set comparisons;
- 140 independent global minimum comparisons.

The residual-three theorem received an additional independent check:
all 70 primes' complete shell hit sets were compared with the existence
of a prime factor of `a3` congruent to two modulo three. There are 51
occupied shells and 19 empty shells. The exact formula
`2*(ell_star-1)` and the full digits of the global minimum agree in all
102 full/half comparisons on the occupied domain. All 71 points in the
selected records' complete raw scale fibres and 201 passing raw boundary
sources satisfy the displayed coordinate and sharp inequality formulas.

The exact source hash of the checker, its input bound, every prime's two
minima, illustrative passing/obstructed targets, and all counters are in
`CHECK_BOUNDARY_SWAP.json`. Rerun with
`python boundary_swap/check_boundary_swap.py --limit 2000` from the
containing research directory.

## Proof source read receipt

The complete source `boundary_swap_completion.tex` was independently read.
Its first version's unfinished residual-seven numerical tail was reported
to the author and replaced by the explicit rational coordinates. The final
paragraph, including the residue-domain statement and primality calculation,
was then read and checked. The exact reviewed source SHA256 is

`aa2af846808a077ce951d279da4249df742ab18c4e0d0f1880a47c3a675c60dc`.

The final typesetting revision splits the initial complete-record display
into three gathered rows. Its mathematical symbols and predicates are
unchanged. This was checked at the byte level: removing only that first
`gathered` wrapper and replacing the two display line breaks by the prior
`qquad` and `quad` commands reconstructs exactly the previously reviewed
source hash
`ad2ce900fc8b0ea2d9b706c8a0b39d9bcabc6ebb87ffbfa0d36f8bc9763e1bc8`.
Thus the entire remaining file is byte-identical to that reviewed version.
The newly arranged display was read, the checker was rebound to its exact
new hash, and the complete finite run through 2000 passed again.

The earlier complete read covered revision
`17a284e69697f81e3314088210c3a68830a0f4afe2593502fa80a4e5aa34fddf`.
The final revision additionally displays the entire code decoder, both
encode/decode composites by Euclidean division, and the recovery of every
remaining hit coordinate with `k` retained. These additions were read and
checked. The author also accepted the review's precision correction:
for an exterior hit with `A0>B0`, the candidate code numerically decreases
even on an obstructed rational target; `R | p^2-1` is the exact criterion
for that target to be a lower *integral hit*. The final wording states this
exactly and retains the rational companion on the complementary domain.

All four theorem statements and their full proofs passed this read:

- `thm:boundary-four-rational`: the complete rational domains, involutions,
  group law, stabilizers, ordered reciprocal calculation, both residuals,
  graph inverse, and retained raw scale fibre are explicit and correct.
- `thm:boundary-obstruction-fibres`: all six residue rows have their correct
  signs; each cancellation uses an established unit. The exact common
  denominators, integral restrictions, `Z/RZ -> (Q/Z)[R]` isomorphism,
  and every multiplier's image/kernel/fibre are proved, including multiplier
  zero. Failure of integrality retains the exact rational map and inverse.
- `thm:boundary-orbit-code`: both original radix domains are respected;
  the full decoder, both composites, and every hit coordinate's recovery
  with its scale retained are proved. The complete signed difference is
  exact. The admissible integral orbits and
  their stabilizers give the stated point counts, the unique minimum at
  each retained scale, and all fibres of the minimum selector. The global
  least-hit consequences follow by an actual smaller original code.
- `thm:boundary-r3-global-minimum`: the occupied-domain equivalence follows
  in both directions from the original factor congruence. On that computed
  domain, every hit in a larger outer digit or later shell has a code
  strictly larger than the exhibited one. Among the remaining candidates,
  the least prime factor congruent to two modulo three is the least possible
  `B0`, and tag zero comes first. This establishes the actual global minimum
  in both original rectangles, all displayed coordinates, its complete
  raw scale fibre, and the boundary source's sharp inequality/equality case.

The final residual-seven examples were checked independently:
`(19,1,56,5,0)` maps to coefficient `7088/7` and witness
`(95,35440/7,251163280/7)`; `(5,1,54,19,0)` maps to coefficient `1866/7`
and witness `(95,35454/7,66121710/7)`. All exact reduced denominators are
seven. The eight trial-division remainders for 373 are correct and suffice
because its square root is less than 20.

There are no pending findings against this exact source revision. The
checker now fails if this proof file is absent or its bytes differ from the
reviewed hash; source changes require a new read and an explicit hash update.
