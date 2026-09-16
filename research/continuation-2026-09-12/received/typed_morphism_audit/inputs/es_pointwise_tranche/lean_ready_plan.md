# Exact Lean-ready dependency plan

This is a formalization specification, not a compiled Lean development. No theorem is represented as kernel-checked. Names below are proposed declarations, not claims that identically named mathlib declarations exist. The Python checks are deterministic certificates; importing their results as axioms would not constitute the proposed Lean proof.

## 0. Data and conventions

Use positive natural numbers for coordinates and integers for congruences. Use `ZMod R` units for finite groups. Use rational numbers for the stored representative heights. Treat the three real chamber endpoints separately, proving an integer predicate equivalent to their strict inequalities once.

`Channel := exterior | middle`.

`Shell p R a` contains proofs of `0 < R`, `R < p`, `R % 4 = 3`, `p % 4 = 1`, `4*a = p+R`, and `Nat.Coprime a R`. Primality is a separate hypothesis: the packet construction works without it.

`MarkedState` retains `p R a u h r s channel quotient rawX rawY rawZ`. Its validity predicate includes positivity, `a=h*r*s`, `u=h*r*r`, `Coprime r s`, the shell predicate, and one of:

- exterior: `R*quotient = p*r+s`, raw triple `(a,h*s*quotient,p*h*r*quotient)`;
- middle: `R*quotient = r+s`, raw triple `(a,p*h*s*quotient,p*h*r*quotient)`.

Do not sort the raw triple. A sorted triple is an additional derived field, never the data on which the inverse is defined.

`Hard p := Nat.Prime p ∧ p % 840 ∈ {1,121,169,289,361,529}`.

`ClosureRay r s := 0<r ∧ 0<s ∧ Coprime r s ∧ ((3*s ≤ 2*r ∧ r ≤ 2*s) ∨ (r=1 ∧ 8≤s))`.

`BaseRay` is membership in the explicit seventeen-element fourth mediant row or `(1,s)` with `8≤s≤128`. Define the fourth row by four iterations, not an assumed list.

## 1. Arithmetic and chamber layer

1. `decode_exists_unique`: for positive `a,u` with `u ∣ a²`, there exists a unique positive coprime triple `(h,r,s)` with `a=h*r*s`, `u=h*r²`. The inverse is `d=gcd(a,u)`, `r=u/d`, `s=a/d`, `h=d/r`. Prove the divisibility needed for the last natural-number division before using it. An alternative proof assigns exponents `(e-|f-e|, max(f-e,0), max(e-f,0))` prime by prime, with `0≤f≤2e`.
2. `decode_ratio`: `u*s=a*r`.
3. `exterior_congruence_equiv`: under the shell and normalization, `R ∣ 4u+1 ↔ R ∣ p*r+s`.
4. `middle_congruence_equiv`: similarly `R ∣ 4u+p ↔ R ∣ r+s`.
5. `state_identity`: every valid state satisfies `4*x*y*z=p*(x*y+x*z+y*z)`. This is a polynomial identity using the quotient equations; conversion to reciprocals follows from positivity.
6. `middle_orientation`: replacing `u` by `a²/u` swaps `r,s` and rawY/rawZ. It does not identify the two marked states.
7. `low_integer_iff`: for positive `r,s`, with `D=s²-4rs-3r²`, the real inequality `r/s<alpha` is equivalent to `D>0 ∧ D²>8r²(r+s)²`. Work over integers for `D`.
8. `upper_integer_iff`: with `E=3r²-4rs-s²`, prove the two upper inequalities exactly as in Appendix A, including the `E≥0` branch before squaring.
9. `one_eighth_in_chamber`: `0<r ∧ 8*r<s → r/s<alpha`; also `alpha<1/7`, `beta>1`, `gamma<3` and `[3/2,2]⊂K`.
10. `farey_coordinates`: the integral unimodular inverse is `(2r-3s,2s-r)`; nonnegative coordinates characterize the closed interval. The recursion in Lemma 1.1 decreases their sum and proves membership in some finite Farey refinement.

## 2. Actual signed boxes and the representative height

For a positive anchor `A`, define the finite packet set by positive pairs `n,d≤A` satisfying `Coprime n d` and `n*d ∣ A`. This is a concrete finite set; no generated subgroup is substituted for it.

11. `packet_exponent_equiv`: the packet set is bijective to exponent vectors `j_q∈[-v_q(A),v_q(A)]`, with positive/negative parts assigned to `n,d`. Preserve occurrences and upper bounds.
12. `anchor_box`: the image of those packets under `n*d⁻¹` in `(ZMod R)ˣ`.
13. `anchor_saturated`: the predicate `Coprime A R`, `prime factors of A lie in H`, and `anchor_box=H`; `H` is a subgroup of index two and `-1∉H`.
14. `height_exists`: every residue of `H` has a minimizing packet for rational `d/n`; the finite maximum `B` exists and satisfies `0<B≤A`.
15. `height_representative`: for every `v∈H`, there is an actual packet of residue `v` with `d≤B*n`.
16. `outside_coset`: in an index-two quotient with `-1∉H`, for units `t∉H`, one has `-t⁻¹∈H`; if `b∈H` and an actual divisor `q∉H` divides `b`, then `b/q∉H`.
17. `outside_factor`: if all prime factors lie in `H`, the product and every available divisor ratio lie in `H`. Contraposition gives an actual outside prime factor when the product is outside. Do not infer an available divisor from abstract group generation.

## 3. The constructive pointwise theorem

18. `large_outside_divisor`: let `b>0`, `T>0`. If `b∉H` and `b>T`, take `t=b`. If `b∈H`, an actual prime `q∣b` is outside, and `b>T²`, take `t=q` when `q>T`, otherwise `t=b/q`. Prove `t∣b`, `t∉H`, and `t>T`. The argument removes precisely one prime occurrence.
19. `packet_construct`: from `a=A*b`, an actual anchor packet `(n,d)`, `t∣b`, `R∣tn+d` and `tn>8d`, set `g=gcd(d,tn)`, `r=d/g`, `s=tn/g`, `h=a*g²/(dtn)`, `u=a*d/(tn)`. Prove `dtn∣a` before division. Prove `Coprime g R` and `R∣(d+tn)/g`. Construct a `MarkedState middle` and prove `8r<s`.
20. `weighted_forcing`: combine 14–19 with `T=B/eta`, `0<eta≤alpha`, yielding both branches of Theorem 2.2. The rational specialization `eta=1/8` avoids real optimization in the executable certificate.
21. `uniform_forcing`: `a>A*max(1,B/eta)²`, together with an actual outside prime factor, implies the conclusion. The coarse `64A³` bound is a corollary, not a substituted hypothesis for universal selection.
22. `packet_inverse`: for a target state and anchor pair, `t=d*s/(n*r)` is the only possible preimage value. Prove exactness under positivity, integrality, `t∣a/A` and the packet congruence. Derive `r∣d` using `Coprime r s`; then `g=d/r`.
23. `packet_collision`: two valid packets have the same target iff `t*n*d'=t'*n'*d`. Derive equality of `u` and invoke unique decoding. Record the fibre bound `∏(2e+1)`.
24. `pure_support_no_middle`: if all factors of `a` are in `H`, every middle target is impossible, independently of angle.
25. `counterexample_height_obstruction`: contraposition gives the two necessary inequalities `a≤8AB` or `a≤64AB²` for every saturated anchor of a failed shell with an outside factor.

## 4. Finite anchor lemmas and angular obstruction

26. `seven_anchor_boxes`: each of the seven explicit signed boxes equals its indicated subgroup. Their finite cardinalities and heights are checked by enumerating the exact exponent rectangles. The JSON stores all packets and minimizing representatives, so a reflection proof can check both upper and lower height bounds.
27. `small_prime_packet_tables`: the bad-prime lists through `8A` are exactly `{2,19}`, `{5}`, `{17}` for the first three anchors. The verifier lists all possible packet orientations. Prove completeness of the finite prime list rather than trusting a JSON label.
28. `hand_angular_exceptions`: follow Proposition 3.2, partitioning by the actual outside prime and exponent counts, then enumerate the eight remaining `a` values exactly.
29. `finite_anchor_cutoff`: for each row, all possible additional exceptions satisfy `b≤floor(64B²)`. Primality testing by complete trial division and enumeration of `0≤f_q≤2e_q` suffice. Expected hard-prime/NR counts are in `anchor_certificates.json`; only exceptions `{1201}`, `{837601}`, `{3361}` remain in their stated rows.
30. `exception_repair`: check each complete marked repair by polynomial arithmetic and the exact chamber predicate. No density premise occurs.
31. `seven_support_implications`: combine 20, 24, 29 and 30 to derive every implication of Theorem 3.1 for a hypothetical hybrid counterexample.
32. `shell_three_exact`: for hard `p`, `a3≡1 mod6`. Choose the least outside prime `q≡2 mod3`; parity of its total outside-factor multiplicity gives `a3/q≥q`, and the only `s<8` possibility is `p=97`, outside the hard classes. Construct the exterior state `(R,h,r,s)=(3,q,1,a3/q)`. Prove the converse from `h≡2 mod3`.
33. `forced_anchors_mod144`: with `b=(p+23)/24`, prove `a11=3(2b-1)`, `a23=6b`; the complement of the first three anchor conditions is exactly `p≡1 mod144`.
34. `forced_anchor_121`: `p≡121 mod840 → 35∣(p+19)/4`.
35. `variable_height_11`: the nine symbolic packets for `A=3*l`, prime `l>3`, give heights `3l,l/3,1,3` for residues `3,4,5,9`. The proof is a four-case residue calculation with rational inequalities using `l>3` (and `l>9` in residue class 9, implied by primality); finite tests are supplementary, not its universal proof.
36. `balanced_factor_box`: for distinct primes `l,q≠3,11`, residues `3,2 mod11`, solve the 27-element box equation `8(i+j)+k=5 mod10`. It has exactly the two extreme solutions. Recover the two raw states, `h=1`.
37. `balanced_factor_angle`: `9l≤q≤21l` gives `1/7≤3l/q≤1/3`, hence both orientations fail the chamber. The explicit hard prime `2016361` is checked by deterministic primality and full state arithmetic.

## 5. Exact per-candidate termination

38. `closure_u_iff`: using `u/a=r/s`, prove the two conditions (16), including `r=1 ↔ u∣a` after unique normalization.
39. `least_exterior_residue`: for `R≡3 mod4`, positive solutions of `R∣4u+1` are exactly `u=(3R-1)/4+jR`, `j≥0`.
40. `lower_shell_bound`: the lower branch implies `23R≤p+8`.
41. `hyperbola_bijection`: prove all identities and coprimality conditions of Proposition 6.1 before canceling `k²` modulo `u`; retain `u` and the channel in both directions.
42. `closure_hyperbola_bound`: `u≤2a≤p-1 → kR≤4p-3`.
43. `two_pass_complete`: for arbitrary integer `0≤T<p`, partition states by `R≤T` or `R>T`; the latter implies `k≤(4p-3)/(T+1)`. Enumerate complete divisor boxes and apply 38. The strict partition makes the two passes disjoint.

These lemmas prove a decision procedure for one input; they do not prove that its output is always nonempty.

## 6. Finite range certificate by verified reflection

44. `exterior_rule_sound`: for each JSON row `(r,s,R)`, check primitive closure membership, positivity and `gcd(4r²s,R)=1`; prove the CRT class (14) reconstructs a valid marked state for every prime `p>R` in that class.
45. `middle_rule_sound`: for each `(R,u,d,pl,ph0,ph1)`, check `u∣d²`, `Coprime d R`, and the two CRT conditions. Prove `u∣a²` without factoring `u` or `a`. Check low/upper endpoint chamber inequalities with the integer predicate.
46. `middle_interval_monotone`: for fixed `u,R`, `u/((p+R)/4)` is strictly decreasing; the stored low threshold or upper interval therefore stays in the relevant connected component of the chamber. Do not treat the union of components as one interval.
47. `progression_intersection`: prove the generalized CRT formula with `g=gcd(840,M)`, including the incompatible case and the modulus-one convention.
48. `hard_sieve_sound_complete`: flags enumerate exactly `840k+c`; delete 1 and out-of-range entries. Strike by primes through `isqrt(bound)`, starting at `q²`. A composite flag has a least prime factor within that bound; striking never removes a prime. Primes dividing 840 cannot divide a hard residue.
49. `cover_replay`: use 44–48 to replay all 78,332 exterior and 414,902 middle rules against the exact prime flags. The remaining base flags are exactly the three stored primes; the three additional ray rules clear them.
50. `base_failure_exact_at_three`: independently enumerate all divisors of all 138 ray linear forms and all four middle square-divisor boxes at the three primes. Use certified factorizations, with each factor proven prime by complete trial division. All middle boxes are empty; no base exterior residual is eligible.
51. `finite_range_theorem`: conclude Theorem 5.1. Its statement explicitly includes `p≤10^10`. Prime and state counts remain distinct.

For a full Lean proof, the large reflection checker must be proved sound and then evaluated in a trusted evaluation path (or its work decomposed into verified finite blocks). A hash of a Python result is not a mathematical proof. The supplied SHA-256 list establishes file integrity only.

## 7. Unproved statements, deliberately not declarations or axioms

There is no declaration asserting nonempty closure output for every hard prime. There is no fixed-progression prime-production hypothesis, no subgroup-support replacement for an exponent box, and no density-to-pointwise lemma. Infinitely many primes in the balanced-factor family are not asserted. No general counterexample is claimed or encoded.
