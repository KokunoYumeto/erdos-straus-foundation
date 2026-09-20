# Typed maps, inverse domains and coefficient losses

1. Original E/M divisor: (p,a,R,u,channel,beta_l) -> (h,r,s,k) by gcd(a,u).
   Inverse a=hrs,u=hr^2,R=4a-p with original gate; ordered denominators retained.
2. Reciprocal target: original state -> (p,t1,t2,t3,U), ti=p/xi,
   U=(0,-4,sigma2,-sigma3). Inverse xi=p/ti on positive integer domain then
   the channel-specific ordered divisor inverse. Forgetting p or order loses data.
3. Shape connection: (p,alpha,beta,X,Y) -> original state using the predecessor's
   literal inverse, then map 2. No isomorphism of unmarked cubic curves is asserted.
4. Marked finite Fabel root: (t,A), A^2 f'(t)=1 -> (A,y,z,w) by GF7 with U0=0.
   Inverse t=-(i+Ay)/A and original A. Both signs remain; multiple roots excluded.
5. Infinity factor: one affine point with A=0,b=i. Its b=-i signed factor lies
   outside this chart. Eight projective factor signs do not mean eight affine points.
6. Exact algebraic certificate uses Q[i,A]/(i^2+1,A^2-1/d), a four-dimensional
   algebra that may be reducible. It is not labelled a field without testing.
7. Prime-local base change fixes one i in Q_p. E: two ramified quadratic factors
   and three Q_p factors. M: two unramified quadratic factors and three Q_p factors.
   Roots distinguish repeated isomorphic factors. Counting rational points loses
   ramification. Complex conductor coordinates are not automatically Q_p-valued.
8. Integral specialization: E first two finite root signs have coordinate
   valuations (-1/2,1/2,1,1) and no affine integral reduction. M all seven signs
   are integral over unramified extensions. Neither omission is a Jacobian zero.
9. Root order evaluation: Z_p[T]/f_E -> {(z1,z2,z3):z1=z2 mod p}. Kernel zero,
   index p; inverse by original root interpolation. M evaluation is onto Z_p^3.
10. Order obstruction: Z_p^3 -> F_p, (z1,z2,z3)->z1-z2. Kernel is exactly the E
    order; no Z_p-linear right inverse. The conductor in Z_p^3 is (p,p,1).
    This is not the complex weighted conductor T_A in the Zeta programme.
11. Labelled E/M root interpolation: unique degree<=2 F(x_i)=y_i, G(y_i)=x_i.
    F has coefficient p-valuations (0,-1,-1), G is integral. Compositions are
    identity modulo the respective cubics; their coefficient divisions are retained.
12. Original negative-square E source: alpha=-4c^2 or beta=-4c^2 forces h=3 mod4.
    Set j=(h+1)/4. Exact chosen-word domain c|j; no larger generated subgroup is
    substituted for Div(j^2).
13. alpha return uses U=c^2; beta return uses U=(j/c)^2; Q=h, R_M=(p+4U)/h,
    a_M=(p+R_M)/4. Gcd(j,U) returns original middle h_M,r_M,s_M,lambda_M.
    Output h_M is square. Restore M complement orientation explicitly when needed.
14. Within each branch the target's Q recovers old h; U and j recover c. Source
    fibres retain old r,s. The alpha fibre is the displayed divisor parametrization;
    the beta fibre is the displayed finite discriminant-square parametrization.
15. Across alpha(c1) and beta(c2), the same middle U occurs exactly when c1*c2=j.
    Source-fibre pushforward sums original coefficients. Same-target differences
    generate its kernel. A duplicate target is not a second distinct ES state.
16. Original factor inventories change in a real return. Example p5209 introduces
    target factor47 via the reconstructed integer. It is not an unused old factor.
17. Nonempty Fabel target fibre alone has no arithmetic inverse: the cubic
    T^3-4T^2+1 has an infinity preimage but no rational root. Domain tests remain.

Every finite certificate retains ordered denominators, p, R, u and normalization.
The names 'root-order conductor' and 'weighted complex conductor' refer to the
distinct modules in maps 10 and 7; neither is silently substituted for the other.

Ring directions in map 11 are contravariant: the point map F:E_roots->M_roots
induces Q_p[T_M]/f_M -> Q_p[T_E]/f_E by T_M->F(T_E). Its inverse uses G.
The integral inclusion of the E root order into the M root order corresponds
to the reverse point map G; its image has index p.
