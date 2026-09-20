# Global trace integrality and the original ES source

This is a Turn 7 continuation, not a completed universal-existence theorem.

The principal result is a global rational-integrality criterion. For n >= 3
positive rational denominators with reciprocal sum 4/p, their first n-1 power
sums are integral if and only if every denominator is integral. For ES, only
two traces are needed. A general theorem gives a common reduced denominator d
and d^n | (n-1)! times the reduced reciprocal numerator. At n = 3 all possible
denominator types are classified and explicitly constructed.

On the raw *integer* M-gate source, one integral literal trace instead gives
exactly U | p*a^2. The p-adic bit of U returns the original E or M channel.
Two different original raw words have the same trace exactly when their product
is a^2: these are precisely the two middle orientations. Thus the actual kernel
of the trace-label pushforward has rank |M|/2. No theorem forcing that kernel or
an integer trace at every prime is asserted.

An integral first trace without the full gate can leave a square-part residual
obstruction. The p=1009 example and the exact failed R=135 -> R=15 compression
are retained. A further construction at every hard prime has positive irrational
algebraic-integer denominators with all integral traces and the same middle
prime-local cluster data. It prevents replacing rational roots by algebraic
roots in the positive theorem.

## Reading order

- `preprint.pdf` / `preprint.tex`: illustrated mathematical core.
- `workbench.pdf` / `workbench.tex` / `core.tex`: complete proofs and coordinate domains.
- `figures/`: exact source-fibre illustration, its PNG/PDF renders, and the
  rational-arithmetic rendering script.
- `MORPHISMS.md`: maps, inverses, fibres, weights and exceptional loci.
- `certificates/`: machine-readable original states and exact test cases.
- `source_reading.json`: primary antecedents, actual source hashes and scoped search.
- `INTEGRATION_AUDIT_20260920.md`: fresh replay, render verification, exact
  artifact hashes and integration boundary.
- `HANDOFF_TURN_7_REMAINDER.md`: the unresolved implication.

## Reproduction

```
python verify.py --out reproduced
python -O verify.py --out reproduced_optimized
python check_independent.py --input reproduced --out reproduced/independent.json
```

Both implementations use only the Python standard library. The second imports
neither the first nor predecessor software. `run_all.py` runs these commands and
checks byte agreement of the seven mathematical JSON tables. Runtime summaries
are separate because elapsed times are not mathematical output.

Scopes are explicit: all original first-half E/M states at p=1 mod4 through
3000; complete raw integer trace sources through 97; all trace-integral tail
factor pairs through 500; the rational moment presentation scan at d<=80; all
allowed denominator constructions through 500; and algebraic targets at the
hard primes in the original-state range. The finite scans do not prove any
universal occupancy assertion, and are not new overall ES verification coverage.

The current cumulative ZIP preserves the predecessor ZIP byte-for-byte. It is
not a fresh audit of historical claims. The new source does not require any
Jacobian-conjecture claim, new local-field theorem, or conjectural density input.
No historical-priority determination, independent mathematical review or Lean
build is claimed. Publication status is recorded separately.
