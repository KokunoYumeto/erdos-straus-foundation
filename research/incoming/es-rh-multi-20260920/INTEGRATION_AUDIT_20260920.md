# Integration audit — ES/RH multi-track continuation

Date: 20 September 2026.

## Received identity

- ZIP SHA-256: 85B2D350ACE2D5C740C3707A292B9DE5B6C9C133D375212B0944E011AEEA964F.
- Pasted continuation SHA-256: 74237417B837D43B3C5FBD483873591CDDE44BD83CA892EC1D1620841A6FE021.
- Received combined derivation SHA-256:
  9D39034C1885204F9C300FCF9BB33456406B5F417912FF89C768356DFDD0D045.
- The received manifest verified all 50 listed files before integration.
- The received manifest and verification summary are preserved under
  received/ as historical receipts. They are not represented as hashes of
  the corrected live tree.

## Mathematical audit repairs

1. Track II no longer claims that bounded literal roots alone imply
   eta q tends to e_1. A bounded-root counterexample has
   A=-t^-3, eta^2=2t(t^4-t^3+2) tending to zero, but
   t A eta^4 tends to -16. The limit now assumes a finite coefficient-base
   approach, while the metric noncancellation is proved unconditionally from
   the first coordinate of eta q.
2. Track III now retains supp rho inside [0,infinity) for the positive
   resolvent statement and displays the exact nonnegative Gauss error.
3. Track IV now proves in every degree that the inverse-trace floor dominates
   the earlier determinant-over-trace floor. It also records that a
   degree-L weight requires moments through degree 2t+L.
4. Track V now gives the complete ordered noncommutative cancellation,
   the exact projection congruence, the onto hypothesis for the nested
   observation, the active-coordinate Bernstein estimate, the implemented
   branch-depth conversion, and unambiguous moving-monic notation and norms.
5. Track V's README scope now says that the package derives a certification
   procedure. No actual native-current certificate is claimed.

## Reproduction

The corrected live suite passes in ordinary and optimized Python with
byte-identical outputs:

- ten suites;
- 541 exact checks per mode;
- eleven deliberately false-inference controls per mode.

The new boundary counterexample is part of the executable residue suite.

## Integration scope

- SZ-20260920-045 through SZ-20260920-047 are exact ES/Fable or
  cross-programme interfaces.
- SZ-20260920-048 and SZ-20260920-049 are RH-facing conditioning and
  propagation interfaces. They are outside the ES occupancy theorem chain.
- No universal ES occupancy, integral odd-frame nonvanishing, global
  ES-zeta identification, RH theorem, or actual native-current sign
  certificate is inferred.

## Attribution

The packet names no separable individual author. It is preserved as a received
collective continuation. Human and project sources are retained in
SOURCE_LEDGER.md and source_reading.json; no attribution was invented.
