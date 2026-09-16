# Correction: modulus maps at finite branch points and compactified CRT

This correction concerns `received/es_s6_counterfactual/src/core.tex`, Proposition “Functorial modulus maps,” beginning at line 173. The source package is preserved without edits. Its `workbench.tex` and `preprint.tex` both include this source component, so the correction applies to both documents.

The finite residue maps, their equivariance, their fibre counts, the cocycle results, the orbit classification, the genus formulas, and the arithmetic section criterion remain valid. The compactification argument needs the actual cycle lengths at each puncture. Those lengths are not generally the moduli. At infinity they are the moduli; at the finite points they divide three and four.

The source sentence “a cycle of length E maps to one of length D by w↦w^(E/D)” is correct for the cusp of the level-E to level-D reduction. It does not prove extension at the finite branch points, and using that exponent there gives an incorrect local map. Also, the product statement for completed covers must use the normalization of the fibre product over the base. The ordinary fibre product can be singular, even for coprime moduli.

## Explicit finite-branch counterexample to the modulus quotient

Take the reduction from level 15 to level 3 and the order-three generator

\[
a_1(x,y,z)=(6+y,-6-x-y,z-2+x).
\]

At level 15 its cycle through zero is

\[
(0,0,0)\longmapsto(6,9,13)\longmapsto(0,9,2)
\longmapsto(0,0,0).
\]

Coordinate reduction modulo three gives

\[
(0,0,0)\longmapsto(0,0,1)\longmapsto(0,0,2)
\longmapsto(0,0,0).
\]

Both cycles have length three. The local map between the completed source and target curves consequently has degree one. In compatible local coordinates it is `w_source ↦ w_source`, while both curves map to the base by `w ↦ w^3`. Using exponent `15/3=5` here would make the composite base map `w ↦ w^15`, contradicting the actual source base map `w ↦ w^3`.

At infinity the same modulus reduction does have cycle lengths 15 and 3, so its local degree there is five. Thus the correction preserves that cusp formula and specifies the finite branch maps exactly.

## Correct complete compactification proof

Let `D|E` be positive odd integers. Coordinate reduction commutes with each integral affine formula, is surjective, and has `(E/D)^3` elements in every fibre. It gives an equivariant map of finite monodromy sets and therefore a map of unramified covers over the punctured base.

Fix one of the three punctures and a source cycle of length `e_E`. Its image is a target cycle of length `e_D`. Equivariance implies `e_D|e_E`: applying the target monodromy `e_E` times fixes its marked image sheet. With compatible sheet origins, local coordinates may be chosen so that the maps to the base coordinate `t` are

\[
t=w_E^{e_E},\qquad t=w_D^{e_D}.
\]

The map of punctured covers is

\[
w_D=\zeta w_E^{e_E/e_D},\qquad \zeta^{e_D}=1,
\]

where the root of unity records the chosen target branch mark. It extends holomorphically to the origins because `e_E/e_D` is a positive integer. Agreement on the punctured disc gives uniqueness. At the cusp `(e_E,e_D)=(E,D)`; at the two finite punctures one uses the actual cycle lengths dividing three and four. This proves extension at every puncture.

For coprime positive odd `D,E`, coordinate CRT gives the exact inverse

\[
(a,b)\longmapsto a+D\bigl((b-a)D^{-1}\bmod E\bigr)\bmod DE
\]

in each of the three coordinates. Hence the level-`DE` unramified cover is isomorphic to the fibre product of the level-`D` and level-`E` unramified covers over the same punctured base, with the same candidate label retained.

For the compactified statement, take the normalization of the fibre product. The need for normalization and the precise local return can be proved explicitly. A pair of branch cycles of lengths `e_D,e_E` gives a local fibre-product equation

\[
x^{e_D}=y^{e_E}.
\]

Put `d=gcd(e_D,e_E)`, `r=e_D/d`, `s=e_E/d`, so `gcd(r,s)=1`. The local equation factors into the `d` branches

\[
x^r=\xi y^s,\qquad \xi^d=1.
\]

For each chosen `ξ`, choose `η` with `η^r=ξ`. Its normalization is

\[
x=\eta w^s,\qquad y=w^r,
\qquad t=w^{\operatorname{lcm}(e_D,e_E)}.
\]

Indeed `η^(dr)=ξ^d=1`, so both original base maps equal the displayed power of `w`. Coprimality of `r,s` gives a birational parametrization by Bézout, and the smooth parameter disc supplies the normal local curve. The simultaneous product of the two monodromy cycles has exactly `d` orbits, each of length `lcm(e_D,e_E)`, since an orbit returns precisely when its iterate is divisible by both original lengths. Therefore these normalized local branches are exactly the completed product monodromy cover. They agree with the level-`DE` completion on every punctured neighbourhood and hence glue uniquely to the required isomorphism of compact covers.

For example, at a level-three and level-five cusp the ordinary fibre product has equation `x^3=y^5`, singular at the origin. Its normalization is `x=w^5,y=w^3`, with base map `t=w^15`. This is the local level-15 cover, not an isomorphism to the singular fibre product itself.

All statements apply componentwise when the covers are disconnected. The candidate label and base map stay retained throughout. The correction creates no relation between distinct arithmetic leaves.

## Replay evidence

The independent intake replay checked the displayed 15-to-3 cycles with affine arithmetic. `checks/geometry_independent_receipt.json` contains the exact cycles, source hashes, ten independently exercised invalid-certificate rejections, complete normal/optimized comparisons, and independent ordered-witness reconstruction receipts. Its source paths identify the original archive roots in the member manifest. The standalone reader above supplies the complete local coordinate proof.

The two package verifiers passed in both ordinary and optimized Python. All 28 generated mathematical certificate files match the supplied parsed contents, and all 28 ordinary/optimized pairs are byte-identical. The 18 supplied/replayed byte differences are CRLF/LF newline differences; the remaining ten files are byte-identical to the supplied files. The package finite replays do not test the omitted analytic compactification distinction, which is why their passing status does not remove the need for this written correction.

The complete TeX replacement is `reconstructed/compactification_correction.tex`, included in the new reader. It replaces the complete proposition and proof, not merely the problematic sentence, so the explicit normal-model construction is visible in the statement as well as in the proof. The received originals remain byte-identical historical sources.
