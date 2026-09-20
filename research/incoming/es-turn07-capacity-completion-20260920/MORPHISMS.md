# Exact maps, inverse domains and coefficient fibres

1. Original square-divisor source: a=prod l^e, beta_l in [-e,e],
   u=prod l^(e+beta_l). Inverse: beta_l=v_l(u)-e. One vector per divisor.
2. Original E normalization: g=gcd(a,u), (h,r,s)=(g^2/u,u/g,a/g),
   kappa=(pr+s)/R. Ordered denominators (a,hs*kappa,phr*kappa).
   Inverse u=a^2/(Ry-pa). No permutation suppressed.
3. Ordered shape: v=a^2/u, D=(4u+1)/R, alpha=v-R, beta=v-D.
   Negative-four coefficient t=-alpha/4 or -beta/4 is retained, not reduced mod h.
4. Cofactor source: j=(h+1)/4, W|j^2, W=t mod h. Full exponent box at j,
   not the old box at a. h may be composite.
5. Canonical label: W=t, defined iff t|j^2. Companion label: W=4tj,
   defined iff 4t|j; it coexists with canonical availability and is unbounded.
6. Finite template: ell>=1, w|ell^2, n=(t-w)/(4ell+1)>0 integral,
   V=ell^2/w, j=ell+4nV, W=j^2/V. Inverse: n=(W-t)/(4j-1),
   V=j^2/W, ell=j-4nV, w=ell^2/V. Domains include 4j-1>t.
7. Small grades h<=t are a separate finite domain; their direct enumeration
   is not attributed to the large-grade classification.
8. Alpha word map U=W. Beta word map U=j^2/W. Both are bijections between
   the complete capacity and complete middle cofactor gate at the original h.
9. Middle inverse: R_M=(p+4U)/h, a_M=(p+R_M)/4; g=gcd(j,U),
   h_M=g^2/U,r_M=U/g,lambda=j/g,s_M=R_M*lambda-r_M.
   Return (a_M, p*h_M*s_M*lambda, p*h_M*r_M*lambda).
   Original ordered inverse u_M=pa_M^2/(R_M*y-p*a_M).
10. The target recovers Q=4h_M*r_M*lambda-1=h, and therefore j.
    It does not recover the original t or original E state when labels are dropped.
11. Finite exceptional primitive map: H=gcd(ell,V)^2/V,
    r0=V/gcd(ell,V),lambda0=ell/gcd(ell,V).
    Alpha (H,lambda0+4n*r0,r0); beta (H,r0,lambda0+4n*r0), in (h,r,lambda)
    order. Here H<=ell<(t/4); every exponent budget is retained.
12. Alpha E preimages: s|(p+4t)/h, r=(s+N/s)/4, with integer r, coprimality,
    first-half range AND R|(4hr^2+1). The last gate is indispensable.
13. Beta E preimages: s bounded by (p-1)/(2h), D=hs^2+4t,
    Delta=s^2(D^2-p)-(4tp+1)/h; positive square k^2=Delta,
    r=(sD-k)/2, kappa=sD-r, original gate and range retained.
14. Two branch returns share a target iff W_alpha*W_beta=j^2 (same p,h).
    Distinct E preimages are original coefficients, not extra residue classes.
15. The integer pushforward sums full same-target fibres. Its kernel has basis
    differences within each fibre; retaining one reference coordinate and the
    differences gives a full integer reconstruction. No normalized support mass
    is substituted for the actual count.
16. M complementation U->a_M^2/U swaps r,s and the last two ordered denominators.
    A selected cofactor word need not already have r<s.
17. Reduced CRT progression: keep t,R,h, both congruences on r, the selected root,
    r_base,r_step,p_base,p_step and the index. Reading these returns the original
    E state. Dirichlet proves infinitely many prime indices, not every index prime.
18. Sharp prime realization: t=6 mod420, h=t^2-3t+1,R=t^2+t+1,
    4r0=t modR, and the original modulus 840hR. No prime polynomial conjecture.
19. The complete fixed-target algorithm may return empty. The constructed
    obstruction primes retain their E solution. Empty old-grade M is not empty ES.
