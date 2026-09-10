# A full turn that returns the frame but retains internal holonomy

This is a further exact construction in the same incoming programme. It makes the difference between a returned observable and an unchanged full object explicit without introducing another support scalar.

## The 24-dimensional tangent to the ordered frame

Fix the ordered diagonal Jordan frame (e1,e2,e3) in J=H3(O). Let F12(u), F23(v), F31(w) be the three Hermitian off-diagonal matrices in the coordinate convention of README.md. The map

```math
(u,v,w)\longmapsto
(\delta e_1,\delta e_2,\delta e_3)
=(F_{12}(u)-F_{31}(w),\ F_{23}(v)-F_{12}(u),\ F_{31}(w)-F_{23}(v))
```

is an isomorphism from O^3 to the tangent space of the ordered-frame equations at the fixed frame.

Indeed, differentiation of e_i circle e_i=e_i gives 2e_i circle delta e_i=delta e_i, so delta e_i has only the adjacent off-diagonal components. Differentiation of e_i circle e_j=0 gives opposite components in each shared Peirce space. Their sum is zero, as required by differentiating sum e_i=I. These relations are both necessary and sufficient and give the displayed inverse by reading one component per edge. The frame manifold is F4/Spin(8) by the cited stabilizer theorem, and its dimension is 52-28=24. Thus the three 8-dimensional components are also the exact tangent directions of the marked-frame moduli.

## A nontrivial operator after three returns

Use the Cayley–Dickson coordinates O=H direct-sum H, with

```math
(a,b)(c,d)=(ac-\bar d b,\ da+b\bar c).
```

For any unit quaternion p, define

```math
g_p(a,b)=(pap^{-1},\ pbp^{-1}).
```

Quaternion conjugation commutes with this inner automorphism, so substitution into both components proves g_p(xy)=g_p(x)g_p(y). It also preserves octonion conjugation. Entrywise action therefore defines a Jordan automorphism G_p of H3(O), fixing each e_i.

Let C be the cyclic frame automorphism X -> PXP^T from README.md. Real permutation of entries commutes with entrywise G_p. Set

```math
H=G_pC.
```

Then

```math
H(e_i)=e_{i+1},\qquad H^3=G_p^3.
```

Choose the explicit unit quaternion p=(3+4i)/5. It has

```math
p^3=(-117+44i)/125,
```

and its threefold inner action on the quaternion j is

```math
g_p^3(j)=\frac{11753}{15625}j-\frac{10296}{15625}k.
```

That is not j. The fixed coefficients satisfy 11753^2+10296^2=15625^2, so the norm is retained. Three applications of H return every labelled frame idempotent, but they do not return all octonionic entries. The full transformation is not being inferred from the frame permutation alone.

In general, for a frame-fixing g and cyclic C, with theta(g)=CgC^(-1),

```math
(gC)^3=g\,\theta(g)\,\theta^2(g).
```

This is the retained noncommutative full-turn product. Setting it equal to I is an additional equation, not an operation that can be hidden by observing the frame.

## The origin and the loop label

Every H is linear, hence H(0_J)=0_J, but its derivative at that origin is H itself. The equivariant map {0_J} -> J induces

```math
B\mathbb Z=[\{0_J\}/\mathbb Z]\longrightarrow[J/\mathbb Z],
```

for the action w -> H^w. This retains the automorphisms at the supported origin; the set-level zero value does not record them. Adjoining the single common scalar tau extends every H by H(tau)=tau. It does not replace 0_J by tau.

For the whole all-degree family, use T_n(H):J^n -> J^n. Its n-th power applies H in every component; after 3n steps its power applies G_p^3 in every component. The integer count, the cyclic frame return, and the internal holonomy are therefore all simultaneously represented.

This gives a precise implementation of the proposed retained-winding picture. It does not identify this chosen quaternionic holonomy with an Artin Frobenius or a GRH zero. It specifies a family of operators and origin data on which such a further arithmetic assignment would act.

## Verification

The companion local research package checked the displayed quaternion powers, automorphism products on three explicit octonionic samples, all first-order frame equations on three explicit samples, and frame return. These add 33 finite groups to that package's earlier 255. The PR's standalone 46-group checker continues to cover the README's cyclic and ES/Koide formulas; it is not relabeled as verification of this whole note. The proofs above give the general algebraic statements. No formal theorem-prover certification is claimed.

Reference: Yokota, I. (2009). *Exceptional Lie groups*, arXiv:0902.0431, §§1.16, 2.1, 2.7. The frame stabilizer is imported; the coordinate holonomy calculation is written out here.
