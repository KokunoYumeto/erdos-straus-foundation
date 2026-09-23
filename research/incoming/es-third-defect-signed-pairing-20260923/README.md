# Signed pairings, cross-shell boundaries, and the unique three-colour return

This module develops structural arithmetic at the current Erdős–Straus
existence frontier. It contains no enlarged prime census and does not claim a
proof of the conjecture.

## Principal results

1. The complete divisor source at every original shell has an exact signed
   opposition pairing. Its complete E/M fibres have positive, explicit weights:
   strict positivity is equivalent to occupancy of that shell.
2. The multiplicative-character form retains the sign `chi(-1)`, and the
   pairing is the difference of the even and odd inversion energies. The
   global degree operator satisfies `A_q^* J A_q = qJ`, so it cannot turn a
   signed zero into strict positivity by itself.
3. An actual cross-shell divisor pair gives an exact determinant `pm` and a
   four-term reciprocal identity. The extra term fuses with `1/a` exactly
   when `nu | a`. Outside that locus, a cyclic obstruction class has order
   equal to the retained numerator of the failed fusion.
4. Suppose `m=gcd(R,p-1)`, `R|m^2`, and `N=R/m>1`. Divisor
   complementation reverses the exact colour `b=(p+4u)/m mod N`. If `U_N`
   is the complement-stable set of words whose colours avoid `0`, `omega`,
   and `-omega`, then `|T_N|=|M|+2|E|+|U_N|`; its quotient by
   complementation is exactly the uncovered-orbit space.
5. `N=3` is the unique nontrivial odd quotient where complementation alone
   forces every possible colour orbit into an integer E or M gate. For every
   odd `N>3`, an explicit reduced prime progression realizes uncovered
   orbits, so the uniqueness statement is sharp.
6. Under `gcd(R,p-1)=R/3`, every third-denominator trace returns at the same
   shell to an original integer word, and
   `2|E|+|M|=|T_3|`. The number of increasing triples is `|T_3|/2`.
7. Every applicable residual is classified from the prescribed prime. At
   `R=27`, for `p=73` or `145 mod 216`, the empty locus has exactly two
   factorization types.

The remaining global obligation is exact: for every prescribed hard prime,
force a nonempty applicable third-colour source or force a cross-shell pair
whose cyclic boundary class vanishes.

## Files

- `core.tex`: complete proofs, maps, inverse data, exceptional cases, and
  nonclaims.
- `workbench.tex`, `workbench.pdf`: readable cumulative paper.
- `arithmetic.py`: active exact constructor with corrected output fields.
- `check_independent.py`: separate implementation importing no active
  programme code.
- `verify.py`, `run_all.py`: exact regression and joint replay.
- `received/`: byte-identical supplied PDF and constructor.
- `MORPHISMS.md`: typed map, fibre, kernel, and information-loss ledger.
- `claims.json`, `source_reading.json`, `RECEIVED_INPUT.json`: durable
  machine-readable state.
- `figures/`: reproducible TikZ sources for the colour-orbit and cross-shell
  mechanisms.

## Reproduce

    python run_all.py

The active replay performs 90 exact rational signed-pair comparisons across all
shells at `p=73`, checks the same-shell counts and residual families, and
checks an exact cross-shell nonfusion control. The independent program derives
the residual lists and residual-27 factor classification without importing the
active constructor.

The supplied constructor used one field called `ordered_denominators` for a
marked tuple that was not always increasing, and it recorded input centred
exponents after a complemented return. The active copy retains both
`marked_denominators` and `increasing_denominators`, and records both input
and output centred exponents. The received file is unchanged.

## Scope

The theorem proves a return from a nonempty trace source; it does not prove that
such a source exists for every prime. A failed cross-shell fusion defines the
cyclic obstruction in the paper; it does not exclude a different fusion,
channel, shell, or Erdős–Straus witness.
