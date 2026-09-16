# Typed maps and explicit information loss

1. Original fixed-seed domain: p=1mod4,p>2u,gcd(p,u)=1; K=prod l^ceil(v_l(u)/2). Retain the original u-exponents; K alone merges exponents2j-1 and2j. Availability u|a^2 iff K|a is proved by valuations.

2. Original middle state to ordered factors: R=4a-p,Q=(p+4u)/R. Codomain RQ=N,Q=-1mod4K. Inverse a=(p+R)/4. Both factors lie in[3,p). The factorization of N is input and the factorization of the returned a is separate output.

3. Normalization: d=gcd(a,u),(h,r,s)=(d^2/u,u/d,a/d),lambda=(r+s)/R. Inverse a=hrs,u=hr^2. Ordered denominators (a,phs lambda,phr lambda) have divisor inverse u=pa^2/(Ry-pa). Retain M,p and the raw order.

4. Reflection: swap R,Q on the full positive3mod4 factor-pair set. Inverse is the same swap. At an existing original state it returns another original state iff p=1mod4K. Otherwise retain a_Q, the zero gate, and both exact defects K/gcd(K,a_Q) and u/gcd(u,a_Q^2). Their prime-wise expressions at (p-1)/4 are in the proof. The map is not silently extended as a valid selector.

5. Unique prime-power divisor coordinates: N=3^eM,3 not dividing M; R<->(i,t) with i=v3(R),t=R/3^i,0<=i<=e,t|M. All actual divisor multiplicities survive.

6. Residue logarithm: for t in -<3> modulo2^k, t=-3^j,0<=j<o. Residue inverse j->-3^j; original integer t and its factorization remain attached. Successive2-adic lifting is given, not an assumed logarithm oracle.

7. Divisor complement: t->M/t, inverse itself. Logarithmic action j->L-e-j. Numerical fixed points are permitted. The half-weight average of the two expressions counts the same original objects; it does not assume every orbit has size2.

8. Exact count fibre: a_j counts original divisors t|M in one log class. n_j counts the actual available i. C=sum a_j n_j. The complete fibre over each class consists of those t and i; neither coefficient is replaced by support size.

9. Character observation: A=(tau(M)-sum_{t|M}chi(t))/2, with chi8=+ at1,3 and - at5,7. Product expansion keeps every exponent. A forgets logarithms; the exact count outside equality cases retains the full a_j. It is not possible to recover a_j from A alone.

10. One-prime construction: choose actual outside q, compute j, then choose the unique one of -j and L-j modulo o below L. Keep whether3^i q is R or Q. The codomain is the constructed subset of original states. Its full choice fibre can have multiple q/role records or be empty for a state outside that subset. At p26460001, q37 with i5 as residual and q109 with i3 as cofactor give the same original (R,Q)=(8991,2943); they do not count as two states.

11. Deep short-residual map: at e>=2o-2, use the least outside q and residual index(L-j)mod o. Parity of the original outside-prime multiplicity gives q^2<=M. This yields R<=sqrtN without identifying it with reflection.

12. Source observations: an actual factor word gives positive counting mass. A zero gate is e at a present receiving label. A missing bounded exponent word is absent from the original divisor atlas. These are not three interchangeable meanings of the same scalar result.

The canonical middle reversal u->a^2/u belongs to a different seed fibre unless explicitly retained. No denominator sorting, forced injectivity of the one-prime choice map, or universal cross-seed surjectivity is asserted.
