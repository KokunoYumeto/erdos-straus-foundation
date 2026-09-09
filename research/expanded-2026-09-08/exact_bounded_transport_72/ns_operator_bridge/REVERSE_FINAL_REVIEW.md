# Reverse transport and smooth inverse: proof review

Reviewer `reviewer-role/reverse_finish` read both TeX files completely, read all changed passages after repair, and read the preserved current manuscript's equations (6.1)–(6.7), Lemma 6.2 and equations (6.17)–(6.20), (8.4)–(8.10), (8.14), and Lemma 8.6 with (8.19)–(8.23). The exact current extracted manuscript has SHA-256 `f83414ea543ffd89910b9b8a35d1680a2e3295246c91cbedf54e719a7bc316d0`. The source's actual normalized charts, original absolute coordinates, and conversion factors are retained; neither vector is divided by its length.

The final static-source paragraph was checked against the preserved pinned `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538` sources: `DiophantineGraph.lean` lines 94, 104, 226, 241; `TorusInverse.lean` lines 52, 195, 278, 323, 342; `SmoothFourierData.lean` lines 351, 561, 565. This is source reading. No Lean, Lake, or Elan process was started.

Authorship and review are distinct: the first file originated with root; the second originated with the prior smooth-inverse agent. This reviewer did a complete new read and authored the repairs recorded here. Those repairs are not described as an independent review of their own author. The separate read-only reviewer `reviewer-role/reverse_finish/transfer_audit` independently checked the first three original transfer/evaluation statements against the current manuscript and supplied the two completeness/wording findings below. Prior analytical reviewers' results remain in `reverse_operator_analysis.md`; they are historical evidence rather than a new execution claim.

## Statement-by-statement audit

| Label | Verified mathematical content |
|---|---|
| `thm:ns-continuous-transfer` | Full `14^m` covering fibres, local smooth transfer, `L_m P_m=1`, `P_m L_m=Q_m`, precise Fourier image lattice, both Haar identities, adjoint and product identities, exact `lambda^{-m}` derivative and `lambda^m` inverse factors, and all three operators' complete fibres. |
| `thm:ns-reverse-mean-correction` | Smooth zero-mean correction, full kernel and inverse fibre with every free slow function, fixed-Q common-band covariance, deck-invariance descent test and inverse, overlap compatibility, and the original signed physical/chart conversion `Q^{-1-h} T_g^{-i}`. |
| `thm:ns-physical-evaluation-fibre` | Exact evaluation graph, right inverse, kernel and every affine fibre, all three physical and chart chain rules including negative slow time, explicit failure of mean descent through evaluation, and the full joint evaluation/mean correspondence, including real data. The domain stays `r>0`. |
| `thm:ns-reverse-sampling-fibres` | Full residue-sum quotient and free original-frequency fibres; exact derivative and inverse descent obstructions; necessary and sufficient restricted-spectrum conditions, with the original frequency zero excluded only for the inverse; uniqueness on the actual grid image. |
| `thm:ns-reverse-lifted-inverse` | Inverse interpolation on the stated image, original zero-Haar condition, full-preimage coefficient recovery with `14^m N^2` points, exact original multiplier after covering, exact quadrature error and the cover-independent weighted Fourier bound. Original spectrum collisions remain recorded. |
| `thm:ns-sharp-denominator` | Both original conjugate products, nonzero integer norm, strict `1/(c|k|)` lower bound, explicit two Pell-frequency sequences, exact squared-length identity, sharp infimum and its nonattainment. |
| `lem:ns-fourier-analytic-bridge` | Original period-one Fourier constants, Bessel argument, multinomial norm estimate, integration-by-parts decay, reconstruction by the previously proved Fejer kernel, explicit shell count, lattice constant bound, and uniform differentiated reconstruction. |
| `thm:ns-sharp-smooth-inverse` | Exact operator norm `(c/(4 pi^2))^q` for the specified Sobolev norms, failure of every smaller loss, actual smooth inverse and complete kernel/image/fibre, distributional continuity estimate and uniqueness on test functions. |
| `thm:ns-cm-improvement` | Explicit `C^{m+q+2}` to `C^m` estimate, including `m+3` for one inverse, with the full lattice constant and exact norm convention. No unjustified optimality claim about this C-norm count. |
| `prop:ns-inverse-parameters` | Joint smoothness, all parameter derivatives, slice support, reality, explicitly typed common and absolute tori, original signed source update, the full A1 cutoff integral, actual axial remainder and retained slow-time derivatives. |

## Repairs and work found by the review

1. S17 previously used the same symbol for a directional inverse in common coordinates and in absolute coordinates. It now defines `D_v^y`, `D_v^Y`, `T_v^y`, `T_v^Y`, `Pi_y`, `Pi_Y`, and the actual covering `P_i`. It proves each covariance on the original character `e_k(y)` and its absolute frequency `(J^i)^T k`. The signed absolute representative is exactly `P_i Delta v = -Q^{-1-h} T_{v_t}^Y P_i E_theta^circ`.
2. The same passage now retains the source's actual axial increment `Delta gamma=gamma_d+a`, with `a=-A_1 gamma_d`. It gives A1's radial integral, its domain and original radial shift, proves local smoothness for the displayed shell-supported data, and derives `c_i D_t^y Delta gamma=-E_z^circ+c_i D_t^y a`. It does not turn the desired axial increment into the actual one or erase either slow derivative. No flatness theorem for the cutoff remainder is claimed here.
3. The finite-spectrum criterion is now sharp. Derivative descent requires distinct residues of all original frequencies in Omega. Inverse descent requires this only of `Omega` with the original zero removed. For each collision, the explicit difference of characters has zero samples and a nonzero derivative or inverse sample; the exact converse conjugates the original operator by restriction's bijection onto its image. This retains the legitimate case where original zero collides with one nonzero frequency but the inverse domain omits zero.
4. The independent transfer reviewer requested the full deck-projection fibre. It is now explicit: `ker Q_m=ker L_m`, and `Q_m^{-1}(h)=h+ker L_m` for fixed points h, with empty fibre otherwise. The proof follows from the already proved compositions and injectivity, and is now written out.
5. The evaluation proof's attribution of the source authors' “exact reason” was replaced with the mathematical structural consequence actually proved by its joint fibres.
6. The distributional continuity/uniqueness gap had already been repaired in the incoming source. This reviewer checked its functional definition, polynomial coefficient growth, explicit test-seminorm bound, differentiation sign and uniqueness from Fourier sums converging in every smooth seminorm. No additional assumption replaces this proof.

After these changes, `reviewer-role/reverse_finish/transfer_audit` returned a further independent bounded pass bound to the final two source hashes in the table below. That follow-up verified Q_m's complete fibres, the corrected evaluation conclusion, both sharp spectral criteria including the empty and original-zero cases, and S17's new common/absolute identities and A1 integral against source (8.5)–(8.6), (8.14), and (8.20)–(8.23). Its check of the smooth file covers the S17 additions only, not a second independent audit of the earlier analytical proofs. The reviewer made no source edits.

## Exact computation and binding

`python ns_operator_bridge/check_reverse_transport.py` completed successfully. It used rational arithmetic, exact pairs for `Q(sqrt(2))`, exact rational torus coordinates and monic cyclotomic reductions. The original Fourier constant `tau=2*pi*i` remains symbolic with its exponent; no floating comparison occurs.

- 5,100 exact sample/DFT checks and 64 unrestricted-obstruction fixtures.
- 16 retained spectra, 13,293 complete preimage points, 84 lifted Gram checks and 60 cover-direction checks.
- 4,800 derivative frequency pairs and 4,416 inverse frequency pairs for the sharp spectral criterion.
- 204 affine-fibre DFT checks with every free original coefficient retained.
- 80 original-vector Pell identities and 864 typed common/absolute inverse identities.
- Both proof files contain exactly five theorem/lemma/proposition declarations; their actual hashes are bound in the JSON.

| File | SHA-256 |
|---|---|
| `reverse_proof_transport.tex` | `cf42ea9475aecd08268d1af5795fcbec92ca62b67d3ec0f73ddb04e187c74d62` |
| `reverse_smooth_inverse.tex` | `b9083db518d98550f2bd9928a0fbbc061d3a70ee846441774ce331be5288ad5b` |
| `check_reverse_transport.py` | `bd4678a1c628dc343a12f89479d36e4908feec17dcd380d531ee1d314ce0338b` |
| `CHECK_REVERSE_TRANSPORT.json` | `e337bc28b37ad43528f9909ce20b48156056260a505d7fa9069caeab952ee132` |

The exact finite checks corroborate the written general proofs; they do not establish the analytic limit, a global Erdős–Straus existence theorem, or the complete Navier–Stokes PDE theorem. The analytic arguments are the complete proofs in the sources, not additional conditions delegated to a later calculation.

