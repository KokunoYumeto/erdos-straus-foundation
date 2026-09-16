# Three-slot unification: research continuation

11 September 2026. This package develops the uploaded associator/TERZO programme into explicit three-slot cubes, faithful integer return, three-graded cubic-norm actions, and marked arithmetic. It is not a relabelling of R + C as a new number system.

## Reading

`note.pdf` is the 13-page mathematical tranche; `note.tex` is its complete source. The principal results and constructions are:

- Exact associator recovery, including full 32-dimensional tagged seed calculations, and the local Möbius annihilator line.
- Complete gluing of three marked faces: a 19-dimensional visible image and an 8-dimensional joint fibre. All nine coordinate slices are NOT being called incomplete.
- An explicit integral 3x3x3 cube with three identical smooth determinant cubics and an infinite-order round trip through its three typed kernel maps. The proof combines a cited translation theorem, exact orbit coordinates, and good-reduction torsion bounds; it is not a finite-orbit extrapolation.
- An injective, explicitly invertible coefficient map from cubes to degree-one operators in a 24+27+27 graded representation. Pure tensor moves are integral, invertible and cubic-norm preserving, but change the quadratic trace. Pure and general tensor moves are distinguished.
- All 27 entries of the first-Tits/Zorn bridge, its compact real structure, and an exact Wilson-basis identification.
- Full reconstruction of Wilson's 196560 minimal Leech vectors, their original joint membership constraints, and the distribution of the ternary Jordan determinant on that one quadratic shell.
- An exact ES-marked face and its reversible attachment to the infinite-return cube, with a worked p=1201 marking. This encodes an existing witness, not a circular existence proof.
- The Cayley cubic and the complete positive integral reciprocal return p0=4*lcm(A,B,C)/gcd(4*lcm(A,B,C),A+B+C).
- Terzo's conditional exponential-kernel theorem separated from an unconditional marked period subgroup and its faithful integer action on the cube.

## Reproduction

Python 3.9 or later, standard library only. Run from this directory:

    python verify.py --out regenerated_main.json
    python graded_lie.py > regenerated_graded.json
    python leech_ternary.py > regenerated_leech.json

Repeat each with `python -O`. The JSON on stdout is byte-identical to ordinary execution. The three scripts use explicit runtime checks, not removable Python assertions. `graded_lie.py` and `leech_ternary.py` import helpers from `verify.py`; keep those files together.

`execution_receipt.json` records actual local normal and optimized runs, environment, timing, and output hashes. `certificate.json`, `graded_lie_certificate.json`, and `leech_certificate.json` are the resulting exact records. Large integers must be parsed with arbitrary precision, not a JavaScript floating-point JSON number implementation.

To build the PDF, run `pdflatex -interaction=nonstopmode -halt-on-error note.tex` twice. Dependencies are standard TeX packages listed in the source. No external image assets are needed.

## Evidence and limitations

General algebraic proofs, formal polynomial identities, exact finite enumerations, and imported primary theorems have distinct scopes. `lean_ready_plan.md` supplies proposed declarations and exact dependencies; no Lean build or formal certification is claimed. The work was developed and checked by one assistant execution, not multiple independent reviewers. Full archive reading, historical novelty, a universal ES proof, and Schanuel's conjecture are not claimed.

The source archive is not republished. `source_reading.json` records only selected mathematical source locators and hashes; it is not a full private inventory. Classical first-Tits, genus-one cube, and Leech constructions retain their cited antecedents. The basis calculations, cube instance, integral attachment and histograms are derivations/certificates in this continuation; priority is unassessed.

The exact pointwise obligation still open here is to construct a positive integral return for every required prime, not merely an intrinsic Jordan point or a complex orbit. Unlike the earlier frame-only action, the present three-graded moves actually change the invariant that must change.
