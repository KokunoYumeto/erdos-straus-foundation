# Exact Lean-ready dependency plan

Status: no Lean toolchain was run for this tranche. The list below is a
formalization dependency specification, not a completed formal proof. No `sorry`
placeholder file is presented as verification.

1. `firstHalf_unit_data`: for prime p=1 mod4 and p/4<a<p/2, R=4a-p is odd,
   3 mod4, 0<R<p, coprime to pa. Use rational/cleared integer inequalities.
2. `square_divisor_normalize`: u|a^2 -> h,r,s positive, gcd(r,s)=1,
   a=hrs,u=hr^2; inverse exponent coordinates. Prime-power proof retained.
3. `E_return`, `M_return`, `ordered_inverse`: cleared polynomial identities,
   integer quotient tests, and the two exact p-colour conventions.
4. `firstHalf_complete`: the explicit TypeI gcd argument in core.tex plus
   TypeII size bound and factor identity (Ry-pa)(Rz-pa)=p^2a^2.
5. `pair_fibre_equiv`: equivalence to M data (d|h,common p-bit) or E data
   (d|h,p-side), not to an unmarked union. Cardinality2*tau_div(h).
6. `pair_swap`, `pair_complement`: involutive self-maps; commuting actions.
7. `pair_action_free`: no S fixed point, no I fixed point since v_p(pa)=1,
   no SI fixed point since -1 is not a square modulo an odd3mod4 integer.
8. `pair_count_dvd_four`: finite orbit equivalence with the Klein group,
   rather than a computation-only mod4 assertion.
9. `histogram_collision_identity`: exact counts for b-c and b+c modulo R.
   Derive both directly by finite sums; no Fourier theory is required here.
10. `principal_lower`: partition G into antipodal pairs or use real
    Cauchy--Schwarz to obtain T>=2*m^2/phi(R)-D.
11. `divisor_cube_bound`: tau_div(n)^3 <64*n, via multiplicativity and the
    four explicit small-prime maxima. This avoids early fractional-power APIs.
12. `reciprocal_totient_decomposition`: n/phi(n)=sum_(d|n) mu(d)^2/phi(d).
13. `progression_harmonic_upper`: either odd mod4 class has harmonic sum
    <=1+log(x)/4. Isolate its first term and compare four-spaced intervals.
14. `odd_coefficient_sum_bound`: finite Euler products bounded by
    exp(sum_(j>=1)1/(2j(2j+1)))=e/2<7/5. Prove convergence explicitly.
15. `principal_full_upper`: Ptotal <224/15*p^(2/3)*(log p+4).
16. `original_diagonal_lower`: D>=2*tau_div(a); paired small divisors and
    exact interval floor counts give Dtotal>p*(log p/2-log2)-2*sqrt p.
17. `explicit_negative_main`: p>=2^20, cube-root/log inequalities and rational
    arithmetic imply sum L<=-p*log(p)/24. No ES premise appears.
18. `adaptive_index_bound`: finite coset sums <=m^2 and [G:B]<=J;
    substitute p>=2^20*J^3 in lemma17 with explicit constants.
19. `coset_integer_minimum`: for s nonnegative integer coordinates with totalm,
    sum squares>=s*q^2+r*(2*q+1), m=s*q+r,0<=r<s; equality criterion.
20. `integer_target_lower`: T+D=sum antipodal-total squares; combine19,
    then round using lemma8. No saturation or actual-stabilizer hypothesis.
21. `kernel_coordinates`: finite residue and coset pushforwards have the
    specified difference bases; reconstruction after retaining sums and
    nonselected coordinates. Prove the separate word quotient metric.
22. `complement_histogram`: c(g)=c(pa/g), even counts at g^2=pa.
23. `complement_orbit_minimum`: paired/self cosets, absence of g^2=-pa,
    convex marginal selection equivalence and the exact lower bound.
24. `certificate_return_terminates`: positive explicit bound -> nonempty
    original target pair finite set -> choose marked gcd inverse. This is
    conditional only on a directly checked numerical inequality, not on an
    assumed global success condition.
25. Finite reflection: compile/check the closed JSON data under their explicit
    bounds; do not mistake this lane for proof of lemma17 or universal occupancy.

Not an available lemma: `forall p, exists a B, integer_lower p a B > 0`.
Not an available lemma: positivity of the complete H_p or pair sum for every p.
Those are the remaining research obligations and must not be axioms of the build.

## Additional proper-spectrum obligations
26. A conjugate-stable set of even characters defines a real orthogonal projector.
27. Its energy lower bound is2*selected_energy-collision_energy.
28. Every selected squared character sum is bounded by total_mass^2, extending
    the all-p obstruction to any at most J retained even modes.
29. Verify the original order46 discrete log, its retained sign lift, and the
    order23 Laurent norm polynomial from the source word list.
30. Prove the rational tangent identities for both arctangent representations
    of pi, with branch intervals; use alternating-series and Lipschitz error.
31. Verify strict rational squared-norm intervals(1009,1010) and(24,25).
32. Combine them with the free-four action and the original pair inverse.
No Lean build is asserted.

33. Prove the all-m divisor-power bound by finite prime separation and strict
consecutive-ratio decrease for e+1>=2m.
34. Prove the general raw-spectrum obstruction under the integer condition
p^(m-2)>=(12*J*C_m^2)^m; certify K_4=127401984/25025 and C_4=9.
35. Deduce the stated effective onset for J<=p^(1-delta), with no conclusion
about zero-truncated or differently weighted observations.
