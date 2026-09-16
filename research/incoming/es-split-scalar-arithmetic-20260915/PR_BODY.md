## Summary

This additive branch publishes the recovered split-zero arithmetic tranche at
`research/incoming/es-split-scalar-arithmetic-20260915/`. It keeps the absent
coefficient `tau`, the supported zero `e`, and a positive supported coefficient
as three explicitly typed cases; computes the exact boundary between ordinary
amplitude inversion and split-support inversion; and then carries the actual
prime factors and exponent fibres into the Erdős--Straus shell calculation.

The main mathematical result is a complete fixed-residual classification at
`R = 27`. It gives 174 coordinatewise minimal capacity profiles: 9 supported
on one nonidentity residue class, 99 on two, and 66 on three. Every occupied
profile has an original-factor witness reserving at most nine prime occurrences
from at most three residue classes. The package also proves the all-multiplicity
thresholds for the `{1,7,11} mod 27` family, retains ordered denominator
inverses, and derives the fixed-residual Dirichlet carrier and character
factors in the half-plane of absolute convergence.

## Exact maps and retained information

`MORPHISMS.md` records the domains, codomains, inverse fibres, and information
loss for the split coefficient encoding, amplitude observation, idempotent
completion, positive count lift, original exponent coordinates, periodic
capacity reduction, grouping of equal residues, catalogue witness selection,
arithmetic source extension, and Dirichlet/character observations. The package
does not identify support activation with a positive arithmetic witness and
does not replace distinct original primes by an unmarked residue count.

## Reproduction

The publication replay used Python 3.13.9 and reran every advertised checker in
normal and optimized mode. Both modes reproduced the ten archived certificate
objects exactly after JSON parsing:

- `verify.py`: 409,536 checks, 5 rejected negative controls, 44 small primes,
  2,480 shells, 80,032 canonical candidates, and 1,043 hits;
- `check_catalogue.py`: 62,812 unoccupied capped profiles, 629,841 tested
  frontier edges, and 567,030 occupied boundary edges;
- `check_dirichlet.py --bound 120`: 1,268 integer/channel/modulus cases and
  1,800 local-factor coefficients;
- the residual-27 application: 4,519 hard-class primes, 1,214 occupied shells,
  1,880 exterior states, and 1,800 middle states.

The original archive manifest also passed for all 27 archived files.
`publication_replay.json` gives the exact commands, finite contracts, hashes,
and nonclaims. `MANIFEST.json` pins the public branch bytes.

## Scope

This branch proves a fixed-residual theorem and its finite exhaustive
classification. It does **not** prove that every prime occupies the `R = 27`
shell, does not establish a universally bounded residual selector, and does
not prove the Erdős--Straus conjecture. The hard-prime scan is regression and
finite evidence, not new universal prime coverage. No Lean build, independent
mathematical review, Riemann-hypothesis implication, or historical-priority
determination is claimed.

## Provenance and licensing

The public provenance record cites the antecedent SplitZero programme, the
support-completed center-sector work, the Boolean-product shell analysis,
Elsholtz--Tao's Type I/II framework, and the NIST DLMF conventions actually
used. Private platform identifiers and transcript filenames are deliberately
excluded. Mathematical prose/data are CC0 1.0; the Python checkers are MIT.
