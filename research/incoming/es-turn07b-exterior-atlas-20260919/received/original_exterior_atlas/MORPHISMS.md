# Maps, inverse domains and information loss

1. Original divisor exponent box -> u: beta_l=v_l(u)-v_l(a), inverse by prime
   valuations. Neither repeated prime occurrences nor signs are dropped.
2. (a,u) -> (h,r,s) using gcd(a,u), inverse a=hrs,u=hr^2. gcd(r,s)=1.
3. E gate -> kappa=(pr+s)/R and ordered triple (a,hs*kappa,phr*kappa).
   Ordered inverse u=a^2/(Ry-pa); sorting is not silently performed.
4. Original complement v=a^2/u=hs^2 and exterior cofactor D=(4u+1)/R.
   The complement is an integer divisor. This does not assert that the complement
   itself passes the E gate.
5. Norm identity: (p+R)^2+4v=4vRD. Retaining R,v,p recovers a,u,D only on
   the original availability domain v|a^2 and the displayed residue conditions.
6. The grade v differs from both R and D. R=D is allowed. gcd(h,R)=gcd(h,D)=1,
   but gcd(v,D)=1 is FALSE in general; example p37,v18,D3.
7. The cubic cutoff is computed with exact integer inequalities. It is a necessary
   bound on existing states, not an assertion that a state exists.
8. Direct chart: R<=D,R<v. Reciprocal chart: D<R,D<v. Norm chart: v<R,v<D.
   The three sets are disjoint. A tie of R,D belongs to the direct chart.
9. Reciprocal B=(pD+1)/4,w|B^2,w<B,D|w+B -> h,r,kappa, s=(r+kappa)/D.
   The input orientation fixes r<kappa. Inverse w=hr^2, B=hr*kappa.
10. Norm chart v,R -> a=(p+R)/4,u=a^2/v. The exact original-domain test is
    R=-p mod 4K(v); norm divisibility alone is insufficient. K(v) carries every
    ceiling-half prime exponent.
11. The norm chart need not factor a to decide availability, but factorization of
    the reconstructed a is retained when producing beta and the final witness.
12. Projecting a state to its least one of v,R,D is noninjective. The other
    marked coordinates and chosen chart are retained in every serialized state.
13. Full E atlas plus the earlier full M atlas decides the complete first-half
    source at a given prime. Its possible empty output remains logically open.
14. If a reduced coefficient is zero, that alone is not used to infer absence.
    This tranche uses exact original integer/divisibility conditions throughout.
