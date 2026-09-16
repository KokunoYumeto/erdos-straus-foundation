# Short mathematical preprints and posting images

12 September 2026. Each full note is three pages, defines its coordinate model, states its exact domain, and gives complete proofs with fixed finite certificates. Each also has a one-page card suitable for posting and full-page PNGs for sharing the proof itself.

| Note | Proof PDF | One-page PNG | Specific content |
|---|---|---|---|
| P1 | `preprints/01_symmetry_complete_traces.pdf` | `preprints/png/01_symmetry_complete_traces_card.png` | Minimal joint-symmetry completion, exact 759-trace inverse, and a single necessary-and-sufficient mod-four syndrome. |
| P2 | `preprints/02_octad_aligned_octonions.pdf` | `preprints/png/02_octad_aligned_octonions_card.png` | Explicit projective-octad/Wilson isometry, all inverse coordinates, two obstruction witnesses, and the full cubic correction. |
| P3 | `preprints/03_shortest_trace_lifts.pdf` | `preprints/png/03_shortest_trace_lifts_card.png` | All-integer shortest three-trace formula, now with eight norm-four seeds, one norm-six seed and complete phase transports. |

These are potentially original exact coordinate results or shorter proofs in this project, not priority claims. Wilson's model comparison, Golay design incidence, the Leech lattice and Jordan constructions remain attributed to their human antecedents. The exact literature search and its incomplete lead are in `novelty_review.json` and `source_reading.json`.

All new checks use standard-library Python. Run `python verify_audit.py --out output` and `python verify_shortest.py --out output/eight_seed.json`. No original package is needed for those two checkers. The patched inverse and mutation regressions additionally need the preserved `inputs/leech_trace_inverse/` certificate files.

The cards do not replace the proofs. No ES/RH solution, independent review, historical priority, or Lean build is claimed.
