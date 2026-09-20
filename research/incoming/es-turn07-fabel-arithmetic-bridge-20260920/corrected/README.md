# Corrected and extended public source

The files in the parent directory that are listed in `MANIFEST.json` are the
unchanged received packet. This directory is the public integration build.

- `core.tex` repairs the middle special-fibre wording, restores the material
  alpha inverse-fibre gate, and states collision and line-occupancy scope
  exactly.
- `root_orders.tex` retains the complete integral-order and interpolation
  argument.
- `fixed_cofactor_atlas.tex` proves the new complete fixed-(Q) fibre theorem,
  its negative-square slices, residual locus, exact examples and nonclaims.
- `workbench.tex` is the complete corrected reader and inputs all three proof
  modules.
- `preprint.tex` is the shorter corrected reader and now also inputs the
  fixed-cofactor theorem.
- `output/` contains PDFs compiled from these sources after executable and
  visual checks.

The new exact replay is `../verify_integration_extensions.py`; its machine
receipt is `../integration_extension_receipt.json`. See
`../INTEGRATION_AUDIT.md` for the identity of the received packet, every
correction, and the distinction between mathematical proof and finite replay.

