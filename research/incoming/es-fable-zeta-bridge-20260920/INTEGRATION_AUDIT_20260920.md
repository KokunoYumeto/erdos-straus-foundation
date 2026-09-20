# Integration audit: fixed-input and boundary continuation

Date: 20 September 2026

Received source: `received/combined-continuation-20260920.txt`
SHA-256: 85d28cc83185acc948635f2b0386c2762e4330d3eff6a52634723b5db5f18a9e

The received continuation was treated as candidate mathematics. Several
internal proof rechecks were run, followed by an exact symbolic and finite
group replay. These checks are not represented as external peer review. The
accepted ES-facing arguments are now written in full in
FIXED_INPUT_BOUNDARY_MONODROMY.tex. The certificate
verify_fixed_input_boundary.py writes
fixed_input_boundary_receipt.json.

## Accepted results

1. Every positive integral witness at a prime \(p\equiv1\pmod {12}\) has
   \(p,x,y,z\) pairwise distinct. The fixed-\(p\) bounds on \(S\), the
   discriminant, the four derivatives, signed coordinates, and all four
   inverse coordinates are correct with the displayed constants.
2. At fixed nonzero \(p\), over
   \(\mathcal B_p=\{(A,C):ACd_p\operatorname{Disc}(g_p)\ne0\}\), the literal
   signed cover splits into ranks \(2+6\). Its monodromy has order \(48\), its
   two sheet-orbits have sizes \(2\) and \(6\), and its deck group is
   \(C_2\times C_2\).
3. The order-\(48\) orbit metric retains a full \(2\times2\) block on the two
   trivial representations. The prime-odd line is the nontrivial character
   \(\chi_{\det}\), not another trivial representation.
4. Replacing \(\xi\) by \(\eta=\xi^{-1}\) gives a finite flat rank-eight
   completion. A root of multiplicity \(m\) gives the exact local algebra
   \[
   \mathbb C[\varepsilon,\eta]/
   (\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1}).
   \]
   A double root gives \(\mathbb C[\eta]/(\eta^4)\).
5. The family \((p;p,2p/5,2p)\) and the auxiliary paired-root quartic have an
   exact length-four local-algebra isomorphism after the stated scaling. This
   is a local algebra/action map, not a global identification.
6. The marked odd-moment frame is invertible on the ordered signed-root
   cover. Its factorization \(O=V_hU\) locates the additional odd receiving
   divisor in \(V_h\), and the full Lagrange inverse is explicit.

## Corrections made during integration

- Equation EZ57 is derived from the pair consisting of the intrinsic-root
  relation \(p=-5D/C\) and the coefficient hypersurface equation. The
  hypersurface equation alone is not equivalent to the fixed-\(p\) chart.
- The fixed-input representation is
  \(\mathbf1^{\oplus2}\oplus V_2\oplus\chi_{\det}\oplus V_3\).
- The connected ordered-denominator space, its free \(S_3\)-quotient onto
  \(\mathcal B_p\), and every coefficient and derivative factor used by the
  two sign-generating loops are now proved and printed explicitly.
- The factor \(C=0\) is removed by the intrinsic-prime ES chart. The exact
  squarefreeness boundary at fixed \(p\ne0\) is
  \(A d_p\operatorname{Disc}(g_p)=0\).
- The term “physical pole” was removed. The proof concerns the original
  meromorphic Fable coordinate. Its norm limit requires approach to a fixed
  finite coefficient target.
- The nilpotent obstruction uses
  \(N=M_\varepsilon=(2g_0)^{-1}M_{\eta^2}\). It does not claim that every
  nilpotent in the length-four algebra squares to zero.
- Metric transport now states its direction: the pullback is
  \(D_c^*G_{\rm pair}D_c\), with determinant factor \(|c|^{12}\).
- The moment matrix \(U\) is defined on the ordered signed-root cover.
  Its determinant and the zero-divisor conclusion descend as invariant
  statements; \(U\) itself is not a single-valued unmarked frame.
- The hard-prime proof now includes the positivity of both factor terms,
  the step \(x+y+z\le3z\), and the exact metric hypothesis.

## Material preserved but not imported into the ES theorem chain

The received source also contains an auxiliary-degree estimate for native RH
resolvents and a sequence of rank-one error-propagation identities through
two minima and phase-sensitive currents. Those arguments may be useful in the
zeta programme, but the source does not prove a dependency from them to the
ES occupancy problem or to the fixed-input cover. They remain preserved in
the received source file and are not presented here as ES advances.

## Verification

Run:

    python verify_fixed_input_boundary.py

The current receipt records:

- fixed-\(p\) factorization and discriminant identities;
- both exact monodromy paths;
- group order \(48\), orbit sizes \(2,6\), and deck centralizer order \(4\);
- the \(p=5\), rational ES-family, and paired-root local equations;
- the two Jordan blocks of size two at a double root;
- the odd-moment factorization and inverse.

## Cumulative integration completed later on 20 September

Three further proof modules are now printed in the cumulative reader.

1. `INTEGRAL_COMPLETION.tex` retains the original literal-root order over
   `Z_p`, all normalization matrices, Smith factors, quotient modules,
   conductor ideals, specialization kernels, the Type-I boundary lift and the
   finite-place control family.  Fresh main and independent receipts record
   104,538 and 27,154 checks.  The control family tests a proposed criterion;
   it is not an ES counterexample.
2. `DEFINING_PRIME_CONTINUATION.tex`,
   `INTEGRAL_NORMALIZATION_CROSSWALK.tex` and
   `LOCAL_GALOIS_REPRESENTATION.tex` give the general collision-stratum
   formula, the exact translated-chart quadratic twist, the fixed-prime
   rank-2+6 fibre product, and the signed-label conductor identity.  The
   crosswalk proves literal equality of the two E/M orders and their ordered
   bases.  Its checker passes 80 exact checks.
3. `ES_RH_CONTINUATION_B.tex` gives the three-character receiving-frame
   theorem, the paired determinant inequality, finite heat remainders, and
   the `q=61` signed-descent example.  A separate reconstruction passes 923
   exact checks for the arithmetic and descent tracks.  The received 1,121
   and 1,660 check counts for the determinant/heat packet are preserved as a
   received receipt because the four scripts that produced them were absent.

The cumulative PDF has 124 pages.  It compiled in two clean passes, all pages
were rendered, complete contact sheets were inspected, and pages 47, 57,
103--105 and 124 were rechecked at original detail.  The final PDF hash and
module-receipt hashes are in `pdf_qa.json` and `verification_receipt.json`.
