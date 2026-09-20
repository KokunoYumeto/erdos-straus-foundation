# Exact ES–Fable–zeta coordinate bridge

This continuation proves an exact map from every actual ordered Erdős–Straus exterior state to the generic eight-sheet signed Fable cover and then through one fixed weighted conductor. The principal readable source is [ES_FABLE_ZETA_CROSSWALK.tex](ES_FABLE_ZETA_CROSSWALK.tex).

For a solution `4/p = 1/x + 1/y + 1/z`, put `S=p+x+y+z` and

```text
H_ES(U,V) = -S^{-1}(U-pV)(U-xV)(U-yV)(U-zV).
```

Its normalized coefficient vector has

```text
u0 = -1/S,
u2 = -(p(x+y+z)+xy+xz+yz)/S,
u3 = 5xyz/S,
u4 = -pxyz/S.
```

Consequently the prime is intrinsic, `p=-5u4/u3`, and the coefficients satisfy

```text
625u0u4^3 - 125u3u4^2 + 25u2u3^2u4 - 4u3^4 = 0.
```

On the stated chart `u0u3u4 != 0` the converse is exact at the algebraic level. The equation does not itself impose positive integral roots, primality, ordering, or the original channel gates.

For every actual Turn 7 exterior state, the four roots `p,x,y,z` are distinct. The target therefore lies in the genuine finite étale degree-eight locus, not in the nonproper locus. The two states marking `p` are given explicitly, and all eight source coordinates are stated in the TeX. The earlier reciprocal-cubic suspension is retained as a separate seven-state boundary map; it is not substituted for this stronger quartic.

The final bridge uses fixed invertible maps `Phi_*`, `Psi_*` and the original conductor `T_A,*`, with `T_A,* Phi_* = Psi_*`. `Psi_*` is a receiving coordinate map, not the conductor. No ES root is identified with a zeta zero, and no universal ES existence theorem is claimed.

## Reproduce

Run the new checker:

```powershell
python verify_es_fable_zeta_bridge.py
```

The frozen upstream packet in [upstream](upstream) contains the full global inverse, conductor, signed-evaluation and monodromy proofs and their independent checkers. Its principal source SHA-256 is `bfb75ff468f35b71103ad2671e22f20fee0414df4a43d1dab5fc2d19aabbd1b6`. See [AUDIT_NOTES.md](AUDIT_NOTES.md) before quoting its endpoint-label notation.

## Files

- `ES_FABLE_ZETA_CROSSWALK.tex`: complete new derivation and exact scope.
- `verify_es_fable_zeta_bridge.py`: exact symbolic certificate.
- `verification_receipt.json`: current checker output.
- `MORPHISMS.md`: domains, codomains, fibres, kernels and information loss.
- `claims.json`: stable result records.
- `source_reading.json`: content-level source-use ledger.
- `AUDIT_NOTES.md`: independent audit corrections and qualifications for the frozen upstream packet.
- `upstream/`: byte-preserved cumulative source packet.
- `build/`: documented, formatting-only build copy with one repaired TeX delimiter.
- `output/pdf/`: visually checked seven-page crosswalk and 32-page cumulative source PDF.
- `pdf_qa.json`: hashes, page counts, render review and checker replay receipt.

## Status

This is structural continuation, not sample collection. It proves a coefficient hypersurface, complete generic fibre, arithmetic inverse on the strict exterior chamber, a distinct seven-state degeneration, and exact operator transport. The unresolved global problem remains existence of an original ES state at every prescribed hard prime.
