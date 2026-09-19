# Turn 7 attempt and result record

## Requested continuation

Turn 6 left a complete signed pair source but no universal positivity theorem.
Turn 7 returned to the original middle coordinates rather than postulating a
positive shell.  The working question was whether the two odd cofactors can be
bounded sharply enough to make a complete finite atlas and whether a constant
inventory of the natural grades could close the hard-prime branch.

## Successful calculation: exact hyperbola and sharp cutoff

Retaining `A=h*lambda^2` gives the exact equation

```
p = R*Q - (Q+1)^2/(4A),      Q+1 < 2A*R.
```

The proof splits `A>=2` from `A=1` and, inside the latter, retains the exact
orientation `R<Q`, `R>Q`, or the tie.  Concavity is evaluated at both integer
endpoints; no interior case is discarded.  This proves the general sharp bound
and its stronger six-class hard-prime form.  The equality locus is solved in
coordinates, not inferred from numerical fitting.

## Successful calculation: complete two-chart atlas

The smaller cofactor is either the original residual `R` or `Q=4j-1`.  This
gives two disjoint charts with `O(sqrt(p))` possible small moduli.  The cofactor
chart is not treated as an original shell.  Its exact inverse reconstructs
`h,r,lambda,s,a`, proves integrality and positivity, and returns the ordered
unit-fraction solution.  The `p=2521` fixture is a negative control against the
false shell-swap interpretation.

## Failed route: a fixed grade list

The natural hope that a prime-independent list of small `h` and `j` might cover
all hard primes is false.  A CRT/Dirichlet construction forces the least
relevant nonresidue to exceed any prescribed bound, which pushes every E grade
`h` and every oriented M grade `j` above it.  Exact endpoint denominators show
that these primes are nevertheless soluble.  Thus the theorem rejects the
fixed-grade route only; it does not reject `p`-dependent cutoffs, relative
cutoffs, or other structural inventories.

## Bounded computation

The main checker and an independently organized primitive-coordinate checker
agree through the declared bound.  They also verify equality and negative-
control examples and the supplied grade-50 order certificate.  Normal and
optimized Python runs are compared byte for byte.  This is a reproduction
certificate for the stated finite claims, not new global ES verification.

## Exact remaining obligation

The two-chart atlas may still be empty at a prescribed hard prime.  A universal
proof must force at least one original E or M coefficient, or prove an exact
equivalent statement that does so after a typed return.  No positivity,
occupancy, prime-pattern or factor-supply assumption is inserted here.
