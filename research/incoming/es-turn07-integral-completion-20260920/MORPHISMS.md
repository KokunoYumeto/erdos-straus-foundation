# Original maps and inverse domains

1. **Original square divisor -> state.** For a prime p=1 mod12, p/4<a<p/2,
   R=4a-p and u|a^2, retain channel gate, gcd g, (h,r,s)=(g^2/u,u/g,a/g), and
   the original exponent vector. E uses kappa=(pr+s)/R; M uses lambda=(r+s)/R.
   Denominator order is (a,hs*kappa,p*hr*kappa) or (a,p*hs*lambda,p*hr*lambda).
   The inverse is u=a^2/(Ry-pa) or pa^2/(Ry-pa), with its stated order.

2. **State -> literal coefficient target.** Keep p and the four labels
   (p,x,y,z), S their sum, H=-prod(T-root)/S. Its cubic coefficient is one.
   Recover denominators by labelled roots. Forgetting labels aggregates actual
   permutations; it is not an injective coefficient observation.

3. **Supplied signed completion.** The original basis is T^j, eta*T^j for
   0<=j<4; eta^2=H'(T). Its open inverse uses xi=1/eta and the supplied four
   physical polynomial coordinates. The eta=0 boundary cannot be declared
   an original finite xi point. A=0 is outside this literal quartic base.

4. **Generic root evaluation.** Over Q_p, evaluate at all four distinct roots,
   retaining separate quadratic factors eta_i^2=d_i. Its inverse is Lagrange
   interpolation of the two coefficient columns. Two signs over one root are
   not two different denominator states. There is no infinity point here.

5. **Integral normalization.** Put k_i=floor(v_p(d_i)/2), theta_i=eta_i/p^k_i.
   The map is f+eta*g -> (f(root_i)+p^k_i*g(root_i)*theta_i). N_i has its own
   labelled square class; equal fields do not identify their factors.
   Inverse: interpolate a_i and b_i/p^k_i. All eight coefficients must be
   p-integral. Its cokernel is (Z_p/p)^2 for E and
   (Z_p/p)^2+(Z_p/p^2)^2+Z_p/p^3 for M.

6. **Root-order sublattices.** E requires equality modulo p at labels0,3.
   M uses the Newton lattice of the three roots p,pb,pc, with invariants1,p,p^2.
   Unit-resultant singleton factors split off integrally. Root conductor is
   p on the E pair and p^2 on the M triple; signed conductor is respectively
   p and p^3 on those normal factors, with no restriction outside them.

7. **Original action transport.** Multiplication by T and eta is computed in
   the original free basis and the normal basis; the normalization matrix
   intertwines them exactly. Both matrices and the inverse are in orders.json.
   On N/S the exact nilpotence indices are (1,2) for E and (3,3) for M.
   N/S is a finite S-module, not a quotient ring of N.

8. **Reduction modulo p.** The E collision block has length4 and eta-chain4.
   M has length6, epsilon-chains3+3 and eta-chains4+2. The normalization map
   on those special blocks has kernel dimensions2 and5. Original coefficients
   and finite torsion are retained rather than normalized to a support count.

9. **Boundary lift.** E (T,eta)=(0,0) has p solutions modulo p^2 and none
   modulo p^3. T/p has forced residue5/8; the next root equation is the
   nonzero residue9ab/(64S). Thus the reduction fibre is not an integral section.

10. **M collision normalization chart.** Z=T/p, theta=eta/p satisfies the
    rank-six etale equations G(Z)=0, theta^2=(a-pZ)G'(Z)/S, with
    G=(Z-1)(Z-b)(Z-c). The inverse divides by precisely p in both coordinates.
    This is an actual original-lattice extension, not an arbitrary coordinate
    renormalization asserted to preserve the lattice.

11. **Prime projector and deck signs.** e_p is the labelled Lagrange projector
    at p. The prime-only flip eta -> (1-2e_p)eta has exact p-denominator1 or2.
    Identity and the global sign preserve the original order; prime-only and
    denominator-only do not. All four preserve N. No classification of every
    automorphism of a specialized split algebra is asserted.

12. **Literal E/M root interpolation.** Given both actual states at the same
    p, F sends the labelled E roots to M roots and G does the reverse.
    They are inverse quotient-algebra maps. In common label coordinates,
    O_M lies inside O_E with index p^2. F is integral; min v_p(G_j)=-2,
    and p^2G modp is c*T^2*(T-a_M), c nonzero. This comparison is not a
    construction of the still-missing target state.

13. **Full signed comparison after field extension.** Adjoin the recorded
    square roots delta_i^2=d_i^M/d_i^E. Map eta_M to delta(T)*eta_E.
    Reciprocal deltas give the inverse. The extension has degree at most four
    for odd p. Original integral membership is still tested through map5.

14. **The actual capacity crossing.** The antecedent p825241 cofactor word25
    produces the M state from the original E source. Only after that proved
    integer return is supplied do maps5 and12 compare the two orders. The
    old E prime budget is not enlarged retroactively by M factors.

15. **Literal -> augmented reciprocal roots.** I(T)=-p/D*(AT^3+T^2+BT+C)
    evaluates to p/T. All four labels remain. The original coefficient
    denominator is p (E) or p^2 (M). The inverse is the same labelled rational
    root operation, not an assertion that both integral orders coincide.

16. **Signed reciprocal twist.** With N=prod roots, the exact derivative
    factor is omega/root_i^2, omega=-p^3*S/(5N). Retain sqrt(omega) for the
    signed map. The normalized reciprocal quartic has scale -1/5 because
    its four roots sum to five.

17. **Removing the prime root.** The augmented reciprocal root at1 is marked.
    Removing it leaves the older reciprocal cubic, whose signed derivatives
    differ by -(z_i-1)/5. The older rank-seven affine chart is not the current
    rank-eight cover. E's collided pair also changes label positions.

18. **Single-prime numerical control.** p=1 mod840, p=-1 mod l, l=11 mod12,
    p>4l. Use a=(p+3)/4, u=al. Both numerical E/M gates pass; the sole extra
    occurrence is l^1, while a has l-exponent zero. The state normalization
    has rational h=a/l, so this is outside map1's original integral domain.
    Rational triples are recorded as fractions; they are never E/M states.

19. **Finite-place tests on that control.** For any prescribed finite set of
    primes choose l outside it. The only denominator-prime failure is l,
    while the original-prime local order and supplied scalar height and
    separation tests pass. This says nothing about all primes simultaneously
    or an adaptive enumeration of all possible denominator primes.

20. **Genuine endpoint states of the control prime.** The two independent
    original returns at R_E=l and Q_M=l have their complete normalization,
    factors, exponent boxes and denominators recorded. They prove these control
    primes are not counterexamples, without promoting their failed R=3 source.

21. **Additional CRT control.** crt_control_note.tex retains a different
    construction of positive rational (a,pb,pc) with one omitted denominator
    prime. It is independently replayed but not used as the main source
    obstruction or substituted for the joint-gate construction.

22. **Complex versus local transport.** The attached complex conductor and
    its Gamma metric are not assigned Q_p entries. The current model is the
    literal polynomial over rational coefficient fields, specialized at p.
    Its finite-order conductor ideals are different mathematical objects.
