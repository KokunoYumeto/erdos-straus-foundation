# Exact Lean-ready dependency plan

No Lean file has been compiled. The plan separates finite exact constructions from general theorems. Use rational coefficients and explicit finite types; do not replace marking types with coefficient equality.

## Root algebra and half-units

1. Define `rootPolynomial : Polynomial ℚ := X * (3*X-2) * (X-2)` and `A := AdjoinRoot rootPolynomial`.
2. Prove its roots `0`, `2/3`, `2` are distinct; establish the CRT evaluation isomorphism `A ≃ₐ[ℚ] (Fin 3 → ℚ)`.
3. Define the three idempotent polynomials from `orthogonal_algebra.json`; prove their Kronecker evaluation laws, multiplication laws, and sum-one law.
4. Define trace and norm as trace/determinant of left multiplication. Prove coordinate-sum trace and coordinate-product norm.
5. Prove the trace bilinear form is the standard dot product in the idempotent basis, positive definite over ℝ.
6. Define `q_i=e_i/2`, numerator `H0=(1/2,1/2,-1/2)`, denominator `K0=(0,1,1)`. Prove `-2*N(U*K0-V*H0)=V*(U-V/2)*(U+V/2)` as a polynomial.

## Four directions and their complete norm/metric stabilizer

7. Define four sign vectors in `Fin 3 → ℚ` with coordinate product `-1/8`; prove the Gram matrix `δ_ij-1/4` and centroid formulas.
8. Over ℝ, use AM–GM on squared coordinates to prove these four vectors exhaust `sum x_i²=3/4`, `product x_i=-1/8`.
9. Define the twelve even-coordinate signed permutations with sign product one. Prove closure, determinant +1, norm and metric preservation.
10. Classify the common orientation-preserving norm/metric stabilizer: a norm-preserving linear map permutes the irreducible coordinate-plane factors; orthogonality gives signs; determinant gives an even permutation.
11. Prove faithful action on four numerator directions, identifying the group with `alternatingGroup (Fin 4)`.
12. For each `ν=-2H`, define `x ∘_ν y = (ν_i*x_i*y_i)_i`. Prove associativity, commutativity, unit ν, the common norm, and the common trace pairing.
13. Prove every signed permutation R gives the exact unital algebra isomorphism from product ν to product Rν; inverse R⁻¹.

## Marked pencil and normalized factor fibre

14. Define `PencilState` with group element, numerator, denominator, selected ambient slot, and orientation. Prove the orbit has 12 elements by trivial stabilizer.
15. Prove projection to numerator has exactly three elements per fibre. Define homogeneous root readout, including infinity as `[1/2:0]`.
16. Prove every fixed numerator has readouts ∞,+1/2,-1/2 exactly once; alternatively replay the complete twelve-entry table after proving its completeness from the group orbit.
17. Define resultant of a degree-one and degree-two binary form. Prove the scaling law for `(L/ρ,ρQ)` and nonvanishing in this orbit.
18. Verify the three normalized factor pairs, three Fable source points, and their exact polynomial images. Prove four pencil states lie over each source point.
19. Extend to all six coordinate permutations and prove 24 states and two orientation choices per `(numerator, observed root)`.

## Cayley atlas and rational A4 action

20. Define the marked Cayley coordinate torus using nonzero `a_i`, pairwise unequal `a_i`, and `sum 1/a_i=0`; define explicit projective equivalence or use marked affine representatives and retain scale.
21. Define face normalization `b_j=-a_j/(4a_i)` and roots `t_ij=-4a_i/a_j`. Prove sum-four, exact inverse, and all exceptional-locus equivalences.
22. Prove the face cubic coefficient formulas `alpha=-16a_i^4/product a` and `beta=-8a_i^3*(sum a-a_i)/product a`.
23. Define oriented flag `(i,j,k,l)` with even parity. Prove unique completion from `(i,j)` and free transitive A4 action on the 12 flags.
24. Derive `C(r,s,t)=(s,t,r)` and `J(r,s,t)=(16/r,-4t/r,-4s/r)`. Prove `C³=J²=(JC)³=id` on the nonzero domain; keep flag labels when numerical stabilizers occur.
25. Derive root–derivative coefficients and verify Fable source `(1/d,-r-d,5d²+3rd+d³/2)` by `field_simp` and `ring` with explicit nonzero denominators.
26. Prove root–derivative reversal `(r,d) ↦ (16/r,8+16(d-8)/r²)`, its involution law, and coefficient transitions.
27. Prove the companion discriminant and signed transition `η'=4η/r`; do not suppress the two-valued fibre when η is not marked.
28. Prove domain condition `f(-4)=-(r+4)r²d'/16` and enumerate what zero/equal-coordinate exclusions mean. Do not import an unproved rational splitting assertion.
29. Prove positivity distinguishes the original negative-coordinate face from three mixed-sign charts. Prove four numerical targets distinct for positive ES states with distinct denominators.
30. Replay the three full arithmetic examples and all 36 face/root states. Recover the exact E/M markings using ordered denominator inverses, not sorted triples.

## Analytic boundary

The componentwise ξ construction uses the classical functional equation as an imported theorem. It does not prove RH. A finite-dimensional algebra and a reflection symmetry do not provide an analytic coupling or zero-location theorem. No formal target proving either has been declared in this plan.
