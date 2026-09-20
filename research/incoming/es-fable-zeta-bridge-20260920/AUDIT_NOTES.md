# Independent audit notes for the frozen upstream packet

The `upstream` directory is retained byte-for-byte as received. These notes record the independent checks used by the new crosswalk and prevent known notation or scope issues from being propagated silently.

1. **Global fibre theorem.** GF1–GF28 correctly give `det DP=-2`, the complete fibre formula, exact omitted square-quartic surface, finite étale degree-eight domain, and nonproper locus `{u0 Disc(H)=0}`. The map is a nonsurjective Keller map; `(1,1/4,0,0)` is an explicit omitted target.

2. **GF5 wording.** “Contains all such states” must be read as “contains all such states with the retained `b=i` infinity-chart convention.”

3. **GF24–GF25 endpoint labels.** The literal limit notation must retain `eta`:

   ```text
   b_{epsilon,eta,sigma}(delta)=sqrt(delta) a_{epsilon,eta,sigma}(delta),
   b^2=[4 gamma (epsilon gamma-i eta delta)]^{-1}.
   ```

   Only the unordered squared endpoint pair is automatically independent of `eta`. A coherent endpoint convention gives `kappa_{+,sigma}=sigma/(2 gamma)` and `kappa_{-,sigma}=sigma i/(2 gamma)`.

4. **Two escape problems.** FC45–FC71 concern the auxiliary quartic `UV(U-V)(U+V)`. GF19–GF28 concern the literal arithmetic quartet. They have different roots and must not be identified.

5. **Label frames.** The labels M,N,T,E separately index arithmetic roots, conductor vectors, auxiliary roots at `infinity,0,1,-1`, and output coefficients. The exact bridge is through `K^{-1}` and the fixed receiving maps. Numerical reuse of a label does not identify the objects.

6. **Conductor versus receiver.** `Psi_*` is the fixed receiving coordinate isomorphism. The original conductor is `T_A,*|U_*`, and the equation is `T_A,* Phi_*=Psi_*`.

7. **Moving period nonclaim.** GF26–GF28 freeze the reference period, moment, actual order, frame and Gamma norm while the auxiliary target degenerates. No moving-period asymptotic follows. The moving Vandermonde determinant is `-64 delta^2 gamma^2(delta^2+gamma^2)` and becomes singular at the collision.

8. **Signed evaluation scope.** The inverse `O^{-1}` and downstream graph-kernel formulas hold for the stated literal quartet, or generally where `det O != 0`; squarefreeness alone does not force that determinant to be nonzero. The example `(A,B,C,D)=(-1/2,-1/2,0,-1/4)` has quartic discriminant `9/16` but rank-three odd matrix.

9. **Monodromy scope.** The order-192 determinant-one signed permutation group is the monodromy of the generic degree-eight cover. It is not a monodromy assertion about the seven-state `u0=0` suspension.

These qualifications do not alter the global inverse or the normalized ES quartic theorem proved in the new TeX.
