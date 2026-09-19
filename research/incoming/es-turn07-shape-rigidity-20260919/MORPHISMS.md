# Marked maps, inverse domains and information loss

1. Original E (p,a,u) -> gcd normalization (h,r,s,kappa); inverse a=hrs,u=hr^2.
   The ordered denominator inverse is u=a^2/(Ry-pa). Original exponent beta_l
   is v_l(u)-v_l(a); no prime factor or channel tag is discarded.
2. Add v=a^2/u and D=(4u+1)/R. Preserve possible gcd(v,D)>1 and R=D.
3. Shape map: alpha=v-R, beta=v-D, X=v,Y=2a. Inverse R=X-alpha,D=X-beta,
   a=Y/2,p=2Y-R,u=(RD-1)/4. Require positive X, positive even Y, positive
   R,D=3 mod4,Y>R, and reconstructed p prime=1 mod8. It is bijective on this
   explicitly specified original image. The pairs (alpha,beta) and (R,D) are
   ordered; swapping them changes the reconstructed distinguished residual and
   generally changes p. The cubic equation alone is insufficient.
4. Forgetting X,Y at fixed p leaves fibres of at most three original E states,
   the roots of the displayed cubic with every original image test. The coefficient
   pushforward sums the fibre; its kernel has the same-fibre differences.
5. Collision R=D -> z=(R-1)/2=delta*t^2 with delta squarefree. delta is the
   squarefree part, not the radical. The middle output has j=(delta+1)/4,
   c=(p+1)/delta, hM=j,rM=1,sM=c,lambdaM=1,Q=delta,R_M=c+1.
6. The complete collision-map fibre retains positive odd t with R=2delta*t^2+1<p and
   u=(R^2-1)/4 dividing ((p+R)/4)^2. It reconstructs the original E state.
   The measure that decreases is min(R_M,Q), not necessarily R_M or a_M.
7. The endpoint E return uses R0=delta,a0=u0=(p+delta)/4,kappa0=c. Its original
   residual and first denominator both decrease. This is the classical endpoint
   construction after the new source-factor extraction, not a new endpoint identity.
8. Radius-seven hard E records -> n=r, hE=4n^2-2. Original E has sE=1.
   The same-shell M return uses hM=n,rM=1,sM=hE,lambdaM=1,uM=n.
   Its complement is uM'=n*hE^2 and swaps only the last two denominators.
9. The inverse of that family map reads n=hM in the rM=1 orientation; it tests
   sM=4n^2-2,lambdaM=1 and the polynomial prime parameter. Keep the orientation bit.
10. Radius-eight nonsingular E -> h=11,alpha=8,beta=-4 -> p=8 mod11 -> the
    actual M state hM=1,rM=3,sM=(p+3)/11,lambdaM=1,Q=11,uM=9.
    The marked inverse also keeps original r,s satisfying the displayed quartic.
    Any hard source in this branch has p mod840 in {1,121}. Forgetting r,s is a
    many-to-one map, with at most three source states at p.
11. Rational cubic involution (X,Y)->(B/X,BY/X^2), B!=0,X!=0. It preserves the
    shape curve and squares to identity. Positive original integral return fails:
    B<0 makes X' negative; for B>0, X' integral requires s|2; s2 gives odd Y';
    s1 has h'=v'=4r^2+h-R-D, r'=r,s'=1, R'=4r^2-D,
    D'=4r^2-R,a'=rh',u'=h'r^2,kappa'=D'-r and p'=4rh'-R'.
    It changes both residuals to1 mod4 and the reconstructed p to3 mod4.
    The displayed p'=5951 record is composite (11*541). The surviving
    correspondence is explicitly recorded, not called unrelated.
12. A zero observed coefficient retains its actual original fibre. No rational
    curve point, coarse shape, character zero or empty numerical search prefix is
    promoted to a positive original E/M coefficient.
