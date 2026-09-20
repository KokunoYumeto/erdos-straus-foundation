# Typed morphisms

## 1. Exterior source to ordered denominators

- Domain: actual Turn 7 exterior states `(p;h,r,s,kappa,R,D)` satisfying every original positivity and divisibility gate.
- Codomain: ordered positive ES solutions `(p;x,y,z)`.
- Map: `(x,y,z)=(hrs,hs kappa,phr kappa)`.
- Inverse on the image: `R=4x-p`, `u=xz/(py)=x^2/(Ry-px)`, `D=(4u+1)/R`, `v=x^2/u`, followed by the gcd normalization in the TeX.
- Kernel/information loss: none on the stated ordered image.

## 2. Ordered denominators to normalized quartic

- Domain: ordered nonzero solutions `(p;x,y,z)`.
- Codomain: the coefficient chart `(u0,u2,u3,u4)` with fixed `U^3V` coefficient one.
- Map: `-(p+x+y+z)^{-1} product(U-tV)` over `t in {p,x,y,z}`.
- Fibre: algebraically quotients the three denominator labels by `S3`; on the strict exterior chamber sorting recovers `x<y<z`.
- Retained marking: `p=-5u4/u3`.
- Image equation: `625u0u4^3-125u3u4^2+25u2u3^2u4-4u3^4=0` on `u0u3u4 != 0`.

## 3. Normalized quartic to the signed Fable fibre

- Domain: the distinct-root arithmetic image.
- Codomain: `P^{-1}(J4)` for the polynomial map `P:C^4 -> C^4` stated in the TeX.
- Fibre: exactly eight points, two for each root, with all four source coordinates explicit.
- Prime-marked subfibre: the two choices `lambda^2=-(p+x+y+z)/((p-x)(p-y)(p-z))`.
- Deck map: the rational involution `Sigma`; it exchanges the two signs over each fixed root.

## 4. Reciprocal-cubic suspension

- Domain: the reciprocal cubic with roots `p/x,p/y,p/z` and sum four.
- Codomain: the hyperplane `u0=0` in the same quartic target.
- Map: multiplication by the retained factor `V` with fixed normalization.
- Fibre: seven points for distinct denominators: two over each finite root and one infinity-chart point.
- Information loss: denominator order and common scale unless separately retained.
- Exceptional locus: the entire image lies in the `u0=0` component of the nonproper locus. This is different from Morphism 2.

## 5. Fixed conductor square

- Domain and codomain: the Fable coefficient/source space, the fixed exponential-polynomial four-plane `U_*`, and fixed polynomial receiver `W_*`.
- Maps: `Phi_*=(V_*^T)^{-1}K^{-1}`, `Psi_*=B_{v,*}(V_*^T)^{-1}K^{-1}`, and the original conductor restriction `T_A,*`.
- Identity: `T_A,* Phi_*=Psi_*`.
- Kernels: all zero.
- Nonlinear conjugates: `P_U,*=Phi_* P Phi_*^{-1}` and `P_W,*=Psi_* P Psi_*^{-1}`.
- Information loss: none after the coefficient target has been formed.
- Nonidentity retained: `Psi_*` is a receiving isomorphism, not the conductor.

## 6. Root-algebra interpolation

- Domain: `C[T]/product(T-t_j)` for four distinct ES roots and a chosen bijection to four fixed reference roots.
- Codomain: `C[S]/product(S-rho_j)`.
- Map: evaluation at `t_j` followed by Lagrange interpolation at `rho_j`.
- Kernel: zero; inverse is the opposite evaluation/interpolation map.
- Choice: depends on the root bijection.
- Stronger projective map: exists exactly when the corresponding cross ratios agree up to relabelling; cross-ratio mismatch is the exact obstruction, not a claim of unrelatedness.
