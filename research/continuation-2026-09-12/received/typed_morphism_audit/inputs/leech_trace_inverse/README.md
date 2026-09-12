# Integral Leech trace inverses — research tranche

The mathematical note gives a fully explicit inverse for every integral three-trace vector, exact optimal lifting cost modulo 4, and a complete integral inverse for the four independent time triples of the previous order-12 Leech action. All twelve time readings follow with exact cyclic orientation. An affine kernel correction, rather than an invariant choice of a single lattice point, preserves the full tetrahedral action.

This is not an Erdős–Straus proof. The exact cubic equation and positivity conditions remain additional arithmetic requirements. The packet preserves the difference between surjectivity of linear trace fibres and occupancy of a prescribed positive cubic fibre.

## Read

- `note.pdf`: nine-page statement/proof tranche, with the explicit nine-column inverse.
- `note.tex`: complete source.
- `certificates/trace_frame.json`: octads, three dual lifts, and all 12 tetrahedral corrections on basis traces.
- `certificates/shortest_lifts.json`: every residue mod 4, exact shortest representative and multiplicity, all 123 projected minimal-shell signatures.
- `certificates/twelve_views.json`: nine universal lift columns, both Gram matrices, all time-return corrections.
- `certificates/arithmetic.json`: existing marked ES witnesses mapped in and back out, in original denominator order.

## Reproduce

Python 3.9 or newer, standard library only:

```
python verify.py --out replay
python -O verify.py --out replay_optimized
```

The mathematical JSON outputs are byte-identical in the recorded runs. No packages, network, prior bundle or Lean installation are required.

## Use the inverse

```
python reconstruct.py --trace 306 16218 1082101 --p 1201
python reconstruct.py --four 1 2 3 2 3 1 3 2 1 1 4 1
```

The output is an integer numerator; divide it by sqrt(8) to obtain the Leech vector. The three-trace option returns a shortest lift. The four-triple option returns an explicit lift, not an asserted shortest one. Every result is rechecked for Leech membership and trace return. A p argument checks the ES identity, without assuming it.

The four `--four` rows are time views of T, not unannounced replacements for the four Klein-group branch marks. They must share their sum; the theorem proves this is the full integral compatibility condition.

## Boundaries

The verifier exhausts all 196560 minimal vectors, all 64 trace residue classes, the fixed-code possibilities and specified matrix identities. The infinite lifting theorems use explicit sections and translation proofs; they do not extrapolate a prime census. The 51-item Lean document is a dependency plan, not a compiled proof. No independent reviewer or historical-priority claim is asserted.
