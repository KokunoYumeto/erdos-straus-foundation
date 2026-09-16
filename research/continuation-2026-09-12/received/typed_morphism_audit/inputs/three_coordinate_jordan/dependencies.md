# Exact proof dependency and scope plan

This is a plan, not a compiled Lean development.

1. Construct K = Q[omega]/(omega^2+omega+1); prove its pair formulas, involution,
   trace and norm. Verify the characteristic-two norm table.
2. Define normalized Fourier coordinates from ordered triples and prove both
   composites are identities over R, and on Q^3 with values in Q direct-sum K.
3. Transport componentwise multiplication, deriving the cubic product exactly.
4. Derive T, S and N and the cubic adjoint. Prove inverse uniqueness off N=0.
5. Derive the Koide quadratic identity with factor 9; retain the defect -1.
6. Classify commutative bilinear plane maps using the two S3 generators and the
   fixed scalar pairing. Establish the one-parameter product family.
7. Compute the left-multiplication matrix and its commutator with L_(v^2).
   The checker verifies all nine entries as exact sparse polynomials.
8. Use gamma(gamma^2-1)=0 to classify Jordan parameters; construct the sign
   isomorphism between gamma = +1 and -1.
9. Construct the real Sym_2 matrix map at gamma=0, with sqrt(2) retained.
10. Prove rational anisotropy by primitive-integer parity descent, not by a bound.
11. Derive the spin Jordan inverse; prove det(U_v)=D(v)^3 and distinguish L_v.
12. Import the real octonion composition algebra and standard Albert Jordan
    identity from a named formal/library statement if available. This note does
    not include a new proof of that imported quartic identity.
13. Define ordered Peirce embeddings, prove squares and the mixed product, then
    prove the three full off-diagonal spaces generate all 27 coordinates.
14. Prove frame evaluation and projector recovery on distinct spectra. Handle
    repeated spectra and order forgetting separately.
15. Import Yokota's identified frame-stabilizer theorem or formally prove it;
    do not infer Spin(8) just from dimension 28.
16. Differentiate the frame equations to prove the explicit O^3 tangent map
    and its inverse at the fixed frame.
17. Verify the continuous half-angle eigenvector formula. Use the clutching
    sign and the intermediate value theorem to prove the Mobius line bundle.
    The rational sample computations are not the proof of this topology.
18. Prove real-orthogonal conjugation preserves the Albert product by entrywise
    index contraction; identify the three specified lifted-loop endpoints.
19. Prove the Klein-four relations, cyclic action, faithful tetrahedral action,
    and exact diagonal-action kernel. Complete finite group data are in JSON.
20. Prove the inverse-trace form of ES, exact Eisenstein integer lattice, its
    inverse and positivity inequalities. Separate these denominator coordinates
    from the workbench's normalized Koide-root chart.
21. Prove F4 invariance of the ES scalar residual; this limits frame-only maps,
    not possible spectrum-changing constructions.
22. Preserve selector p,R,u,h,r,s,tag,quotient and raw denominator order when
    attaching the spectral encoding. The Fourier isomorphism does not justify
    dropping these additional coordinates.

No item claims universal primewise occupancy, a proof of the ES conjecture, or
identification of a lost source passage. A future arithmetic theorem must operate
on the exact lattice/marked divisor domain rather than only its real image.
