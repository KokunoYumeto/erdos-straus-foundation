# Integration audit — 20 September 2026

## Received object and scope

The received cumulative archive was
`ES_Turns6_7_With_Trace_Rigidity_20260920.zip`, SHA-256
`e491bee481c629bb1ad2d0c1101261369ee0464fafc6440dc42163431f52fbbd`.
The preceding cumulative archive remains byte-preserved inside that object.
This repository integration adds the new trace-rigidity module; it does not
rewrite the preserved predecessor.

The mathematical scope is exactly the following:

- common-denominator rigidity for a finite rational spectrum from its first
  power traces and reciprocal numerator;
- the resulting two-trace integrality criterion for rational
  three-denominator Erdős--Straus targets;
- the literal trace denominator, channel tag, fibres and coefficient kernel on
  the complete raw integer gate;
- the square-part residual when the complete gate is removed;
- an irrational algebraic-integer boundary family showing that rationality is
  essential.

No universal trace occupancy, universal ES proof, RH statement or historical
priority determination is asserted.

## Independent execution replay

The repository copies of `verify.py`, `check_independent.py` and `run_all.py`
were executed from a fresh output directory.  The result was:

- main checks: `2,655,782`;
- separate-implementation checks: `331,544`;
- all seven mathematical JSON tables identical between normal and optimized
  Python execution;
- state digest:
  `5e0d1f4ac35a1914008a720aaa1fb05032a55b121bdb30ff2e482e2492837381`;
- `universal_ES_proved: false`.

The replay covers the finite ranges declared in `README.md`.  It is evidence
for the stated identities and enumerations at those ranges, not a replacement
for the written universal proofs.

## Source and render corrections made during integration

The received patch referred to `preprint.pdf` and `workbench.pdf` without
including those files.  Both documents were compiled twice from their included
TeX sources and are now present.  A reproducible figure was added to show the
exact denominator implication and a complete raw trace source at
`p=13, a=4, R=3`.  The plotting script uses `fractions.Fraction` for every
trace value; its source words, integral returns and two-point fibre are not
sampled or inferred from floating-point equality.

All three preprint pages and all ten workbench pages were rendered to PNG and
visually inspected.  No clipped equations, overlapping text, unresolved
references or missing glyphs were found.

Current artifact hashes:

| Artifact | SHA-256 |
| --- | --- |
| `core.tex` | `4e7c930e441af37a5d930f04129fa544192426253226b46f6f049e9292254672` |
| `preprint.pdf` | `22ac91cd1414a34ecfd49e00aed78a8268f8e3a0ca2d2d055d7afd9b3bf7a888` |
| `workbench.pdf` | `c52672216f7c38043021a3b433bfcfc0f5a75ed85e2e1bc5aef89c16c01c9325` |
| `figures/trace_integrality_fibres.py` | `180f38ba05a365034f44e7c78de396a0983449b4cbdf98d3898d63a9d2ce3035` |
| `figures/trace_integrality_fibres.pdf` | `c339506603cec936f68abc0c4315471713acc1d703e00483a260392e878183ae` |
| `verify.py` | `705ff786d96819858c4423cf3e5f77653258fbe44a631c0d166f2f6361731f72` |
| `check_independent.py` | `b1630956340d417827e93ab643803b6f6a12677a55f6c7287ebef5c4b0329a77` |

## Human-source lineage

`references.tex` cites Euler for the classical Newton identities and
Elsholtz--Tao for the inherited Type-I/II unit-fraction coordinates.  The
Newton identities are also derived in the proof.  Earlier project results used
by the continuation are identified by their preserved source and hash in
`source_reading.json`; the collective byline does not replace those source
records.

## Remaining mathematical frontier

The exact trace maps test a supplied rational source word.  The still-open
implication is the existence, at every hard prime, of at least one raw word
whose trace is integral, equivalently an original E or M divisor hit.  Neither
the finite scans nor the algebraic boundary family supplies that implication.
