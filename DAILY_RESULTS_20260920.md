# Dated proof bulletin — 20 September 2026

This bulletin records the new ES–Fable–weighted-conductor bridge with stable result IDs and proof locators. It is a mathematical index, not a programme chronology. The complete derivations are in [the crosswalk](research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex), and the exact symbolic receipt is [here](research/incoming/es-fable-zeta-bridge-20260920/verification_receipt.json).

## SZ-20260920-019 — normalized ES quartic and intrinsic prime

For every ordered positive solution `4/p=1/x+1/y+1/z`, the normalized binary quartic

```text
-(p+x+y+z)^{-1}(U-pV)(U-xV)(U-yV)(U-zV)
```

has fixed `U^3V` coefficient one, recovers `p=-5u4/u3`, and satisfies

```text
625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0.
```

On `u0u3u4 != 0` the converse holds algebraically: the recovered `p` is a root, and the other roots satisfy the ES reciprocal equation when nonzero.

- **Proof:** crosswalk, EZ6–EZ10.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.
- **Antecedent strengthened:** canonical corpus unit `PUBUNIT-1C9A160031EECC8F3F032D4D`, generic resultant-one ES quartic carrier.

## SZ-20260920-020 — complete eight-point signed fibre

When the four arithmetic roots are distinct, the target lies in `u0 Disc(H) != 0` and its complete Fable fibre consists of two explicitly displayed source points over each of `p,x,y,z`. The full discriminant is

```text
(p+x+y+z)^(-6) product_{j<k}(t_j-t_k)^2.
```

- **Proof:** crosswalk, EZ11–EZ14; upstream GF1–GF18.
- **Certificate:** new crosswalk checker plus `upstream/independent/verify_global_fibre.py`.

## SZ-20260920-021 — the prime-marked resultant-one pair

With `Delta_p=(p-x)(p-y)(p-z)`, the two choices `lambda^2=-(p+x+y+z)/Delta_p` give the exact prime-marked factor pairs. They satisfy `LC=H_ES`, `Res(L,C)=1`, `ad+bc=1` and `4af-be=0`. The remaining six states mark the denominators rather than the prime.

- **Proof:** crosswalk, EZ15–EZ17.
- **Certificate:** `verify_es_fable_zeta_bridge.py`.

## SZ-20260920-022 — every Turn 7 exterior target is in the étale locus

For the retained exterior normalization, `x<p`, `x<y<z`, `z>p`, and `y!=p`. Thus every actual Turn 7 exterior state has four distinct roots and lands in the genuine degree-eight locus, not the nonproper boundary. On the strict real chamber, the intrinsic prime and sorted remaining roots reconstruct all exterior coordinates.

- **Proof:** crosswalk, EZ18–EZ23.
- **Strengthens:** `SZ-20260919-006`, by embedding its complete marked-cubic inverse in the global signed quartic cover without losing the arithmetic inverse.

## SZ-20260920-023 — separate seven-state reciprocal suspension

The reciprocal cubic with roots `p/x,p/y,p/z` has a canonical quartic suspension on `u0=0`. For distinct denominators it has exactly seven states: two over each finite root and one infinity-chart point. It lies on the nonproper hyperplane and is not identified with the eight-state arithmetic quartic.

- **Proof:** crosswalk, EZ24–EZ28.
- **Certificate:** `verify_es_fable_zeta_bridge.py` and upstream GF1–GF18.

## SZ-20260920-024 — fixed weighted-conductor transport

The invertible maps `Phi_*` and `Psi_*` transport the nonlinear Fable map and all of its fibres through the original conductor identity `T_A,* Phi_*=Psi_*`. Kernels are zero; fibres, deck action and exceptional loci are preserved. `Psi_*` is the receiving isomorphism and is not renamed as the conductor.

- **Proof:** crosswalk, EZ29–EZ35; upstream FC26–FC35.
- **Literature:** exact Meixner–Pollaczek formulas in DLMF 18.19.8–9, 18.22.8 and 18.23.7.
- **Nonclaim:** no ES root is thereby identified with a zeta zero.

## SZ-20260920-025 — root-algebra isomorphism and exact projective obstruction

A chosen bijection between the four ES roots and four fixed reference roots induces an explicit evaluation/Lagrange-interpolation algebra isomorphism with zero kernel. A single Möbius realization exists exactly when the corresponding cross ratios agree up to relabelling. Failure of that stronger map is an exact obstruction, not a claim of disconnection.

- **Proof:** crosswalk, EZ36.

The frozen cumulative packet also contains the previously numbered global Fable/conductor results `SZ-20260920-009` through `SZ-20260920-014`, `SZ-20260920-017`, and `SZ-20260920-018`. [Audit notes](research/incoming/es-fable-zeta-bridge-20260920/AUDIT_NOTES.md) record the endpoint-label, fixed-frame and signed-evaluation qualifications discovered on independent replay.
