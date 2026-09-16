# Three-coordinate Jordan extraction — 11 September 2026

The note develops the proposal in this conversation into explicit algebra and
marked geometric maps. It does not claim a new number field or an ES proof.

## Files

- `note.pdf`, `note.tex`: written definitions and proofs, source-specific references.
- `verify.py`: Python 3.9+ standard-library exact checker.
- `checks.json`: actual deterministic output of the checker.
- `dependencies.md`: dependency/verification scopes for subsequent formalization.
- `manifest.json`: exact file identities, not a mathematical truth certificate.

Run `python verify.py --output reproduced.json`. Running `python -O verify.py`
produces the same JSON on standard output; both executions were run and compared.
There are no removable assertions and no third-party packages.

The coefficient-family commutator and two determinant identities are checked as
formal sparse rational polynomials. The Fourier product and inverse checks have
explicit finite domains. The 27-dimensional Albert generator checks cover all
basis pairs, hence the associated bilinear identity; they are not a fresh proof
of the whole Albert algebra's quartic Jordan identity. The latter and the
Spin(8) stabilizer are classical imported facts identified in the note.

The literal Mobius construction is in real symmetric two-by-two corners. The
older passage described informally as a Mobius twist was not recovered. No claim
is made that these are the same historical construction. The finite A4 action
records a specified endpoint action, not every integer winding or all global
holonomy. Full paths/lifts remain separate marking data.

The user supplied the research direction. The displayed derivations and checker
were developed in this session, with standard mathematical antecedents cited.
No historical-priority claim is made. No GitHub content has been changed.
