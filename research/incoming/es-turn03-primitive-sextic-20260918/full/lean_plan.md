# Exact Lean-ready dependency plan

No Lean executable or proof build is claimed. This is a proposition-level plan,
not uncompiled Lean code presented as a certificate. The universal mathematical
proofs use only the listed classical inputs and explicitly proved finite lemmas.

1. Finite cyclic unit group, Legendre symbol and quadratic reciprocity;
   supplementary laws at 2. State the hard-prime residue hypotheses explicitly.
2. `source_units`: for prime p, q<p, q=3 mod4, set A=(p+q)/4;
   show A<p/2, gcd(A,q)=1, and the factorwise Legendre transfer.
3. `centered_divisor_equiv`: exponent-box beta <-> u dividing A^2,
   with every prime valuation and its inverse retained.
4. `selector_return_E`, `selector_return_M`: over rational fractions,
   integral quotient gates imply the displayed positive reciprocal identities;
   prove the ordered u inverses by clearing denominators.
5. `full_order_prime`: recursively proved prime factors of n-1 plus the exact
   power/gcd conditions imply Nat.Prime n. Its proof uses multiplicative order
   modulo each prime divisor; do not substitute a probabilistic primality test.
6. Instantiate the 80-node certificate, with trial-prime leaves checked by
   complete bounded divisibility; every internal dependency is smaller.
7. `inactive_saturation_31`, `_223`, `_307`: finite field exponent intervals
   prove the three fixed packets cover their kernels. Retain added actual
   factors inside K; do not promote support equality to measure uniformity.
8. `triangle_closed`: use factorizations, saturation and quotient target classes
   to prove every original channel empty and the successor list exhaustive.
9. `no_two_cycle_3mod4`: quadratic reciprocity excludes opposite edges.
10. `primitive_form`: actual stabilizer plus effective C6, aperiodicity, strict
    growth and the central coefficient relation yield the unique simple atom
    and inactive saturation. This lemma is reproduced in the proof.
11. `C6_dual_CRT`: build the explicit algebra map and inverse by polynomial
    quotient relations; prove e0,e1 orthogonal, E^2=0, and Z's cubic relation.
    `primitive_packet`: map 1+X+X^5 to (1,epsilon), retaining its nonzero jet.
12. Finite Eisenstein norm and residue tables. The finite values can be proved
    by modular power computation. The general interpretation uses classical
    cubic reciprocity with the declared primary convention and conjugate.
13. `triangle_max_bound`: any all-3-mod4 directed triangle has 3*max(C)<p.
14. `square_factor_transfer`: for odd t with t^2 q<3p, the square source lies
    below p, has negative character, and all nonresidue factor edges obey the
    stated reciprocity law. Prove no hidden denominator/zero exceptions.
15. `square_gcd`: exact formula gcd(A_i,A_j)=gcd(A_i,(j-i)(i+j+1)).
16. `triangle_square_escape`: exclude self, successor and predecessor as in
    the full proof. This is a universal theorem, not a finite scan assertion.
17. `square_cardinality`: disjoint source-factor sets plus no opposite edges
    imply L*|C| <= |C|(|C|-1)/2 and |C|>=2L+1.
18. `primitive_B_ge_four`, `primitive_max_bound`: derive B>=4 and 15Q<p;
    then certify the 1,9,25 escape for components of size <=6.

The remainder for Turn 4 is NOT entered as an axiom: no theorem of eventual
selector occupancy for the enlarged graph has been proved. The finite scan
and the counterexample certificates are separate from that missing assertion.
