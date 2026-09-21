# Explicit source maps, fibres and observations

1. **Integral ES witness to first-half state.** Domain: p prime =1 mod12,
   positive integer denominators. Select the unique smallest a, proved to satisfy
   p/4<a<p/2. The channel is the number of p-divisible tails. E puts its unique
   p-divisible tail last; M retains a tail-orientation bit. The finite permutation
   fibre is kept, not counted as new arithmetic states.
2. **Divisor normalization.** From u|a², g=gcd(a,u), h=g²/u,r=u/g,s=a/g.
   The inverse is a=hrs,u=hr², gcd(r,s)=1. Exponents are retained as (prime,e,f,f-e).
3. **Original ordered return.** E quotient kappa=(pr+s)/R and output
   (a,hs*kappa,phr*kappa); M quotient lambda=(r+s)/R and output
   (a,phs*lambda,phr*lambda). Inverses are a²/(Ry-pa) and pa²/(Ry-pa).
4. **Middle complement.** u->a²/u swaps r,s and only the last two denominators.
   The fixed locus would have equal tails and is empty on the prime domain.
5. **Literal quartic.** Root order (p,a,y,z) and S=p+a+y+z produce
   -prod(T-root)/S. Coefficients alone forget denominator order. Retain p,
   labels and S; positive integral roots plus the ES relation are additional
   original-domain conditions, not inferred from the complex quartic.
6. **Homogeneous norm.** N=S^6 F is degree eight in roots. Root scaling by p
   multiplies N by p^8. The coefficient normalization is not divided away:
   det O=-4*epsilon*N/S³.
7. **Signed roots.** xi_i² H'(ell_i)=1, with every sign recorded. Changing signs
   changes columns, and permuting labels permutes columns. The product epsilon
   is A² times the oriented Vandermonde times product xi_i, equal to +/-1.
8. **Reduction/evaluation factorization.** `O,C_H,U` lie in `M_4(C)`,
   O=C_H U, U_nj=ell_j^n xi_j. The complete coefficient matrix C_H is displayed
   in `core.tex`; det C_H=4F/A and det U=epsilon/A². The current theorem removes F=0 only on
   the stated original arithmetic domain. The complex, p-adic and generic
   real boundaries remain distinct.
9. **Moment inverse.** Given z=O beta, m=C_H^-1 z; Lagrange interpolation in
   core.tex equation (inverse) returns every beta_j. All labels and xi signs
   are part of the inverse source. Their squared moduli alone are insufficient.
10. **Exterior cone.** w=p/R and the original word u give the raw rational
    normalized roots displayed in core.tex. The actual original witness has
    u>=2,w>1, or u>=5 at p=1 mod24. The real cone u,w>=1 is a stronger
    sign domain, not a promise of gate integrality.
11. **Exterior polynomial scaling.** Multiply all normalized roots by 16wu;
    exact division -N/(64u²) defines P_E. Return to the original determinant by
    -N_original/p^8=P_E/(2^26 u^6 w^8). Every factor is retained.
12. **Positive translate and derivatives.** u=1+X,w=1+Y; inverse subtracts one.
    The derivative certificates include -6P_E and -8P_E from the exact
    denominator. Discarding those terms would certify another quantity.
13. **Middle cone.** b=min(y,z)/p, c=max(y,z)/p, X=b-2,Y=c-b-1. Keep the
    ordering bit. The integer gap, not real-root distinctness alone, makes
    X,Y nonnegative. Inverse: b=2+X,c=3+X+Y,a/p=bc/(4bc-b-c).
14. **Middle coefficient transport.** L=4bc-b-c, T=(b+c)L+bc,V=b²c²,
    -N/p^8=P(T/L,V/L)=H_M/L^6. The exact denominator L^6 remains.
15. **Coefficient certificates.** The full integer arrays are injective records
    of the specified polynomials. Row minima/counts alone discard values and
    are not substitutes for the full arrays. The grid checker is injective only
    under its displayed bidegree bounds, which are proved separately.
16. **Norm transport.** The coefficient norm is the operator norm induced by
    the standard Hermitian norm on `C^4`. For label G and receiving Q, use
    G^1/2 O^-1 Q^-1/2.
    Its actual two metric factors multiply the coefficient-norm bound. No
    monodromy-invariant or averaged metric is substituted.
17. **Conductor composition.** If the original conductor L is invertible on its
    own stated image, (LO)^-1=O^-1 L^-1. The original conductor coefficients,
    moment factors and its own norm remain; this theorem supplies only O^-1.
18. **Enriched receiver.** J(alpha,beta)=(alpha,E alpha+O beta) has inverse
    (alpha,z)->(alpha,O^-1(z-E alpha)). Erasing alpha can lose a different
    kernel and is not covered by the inverse assertion.
19. **Integral versus local defect.** Nonzero rational determinant is not a
    p-adic unit assertion. In particular original M numerators in the replay
    have valuation two. No existing integral normalization index is erased.
20. **Source existence.** The map from original witnesses to nonsingular
    receiving frames is not a surjectivity statement onto all frames. The raw
    E gate-failure example has a nonsingular frame and no integral return at
    that word. Universal original occupancy is still a separate theorem.

21. **Original observation.** For any further map Lambda, ker(Lambda O)=
    O^-1 ker Lambda and ranks agree. The original quotient metric on the image
    is (Lambda O G^-1 O* Lambda*)^-1. Nonvanishing of O does not imply Lambda
    has full rank; the receiving kernel has been separated, not erased.

22. **Positive-real counterdomain.** The map
    `t -> (1,a(t),t,t+1/10)`, with
    `a(t)=t(10t+1)/(40t^2-16t-1)`, is a reciprocal-quartic section on
    `3<=t<=4`. Its receiver numerator is
    `P(t)/(100000(40t^2-16t-1)^6)`. The shifted derivative `P'(3+X)` has
    eighteen positive coefficients, so the exact sign bracket
    `3053/1000<t<1527/500` contains the unique receiver singularity. This map
    lands outside both integral cones: its middle gap is `1/10`, and both raw
    exterior words are below one.

23. **Orientation of the middle cone.** Passing from an oriented middle word
    `u` to ordered integers `b<c` identifies the complementary labels
    `u` and `a^2/u`. The determinant numerator is symmetric in the roots, but
    reconstruction of the original marked state must retain the orientation
    bit.

24. **Conditional receiver statement.** For
    `W_p={(x,y,z) in Z_{>0}^3: 4/p=1/x+1/y+1/z}`, the theorem proves
    `det O(w) != 0` for every `w in W_p` when `p=1 mod12`. It supplies no map
    from the prime alone to an element of `W_p`, and therefore no occupancy
    theorem.
