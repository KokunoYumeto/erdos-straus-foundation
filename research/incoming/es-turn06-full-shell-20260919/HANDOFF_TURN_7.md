# Turn 7 handoff: the unbounded step after the full-shell attempt

## What Turn 6 actually proves

For every prime p=1 mod4, p>=2^20, the complete unweighted estimate
sum_a [8*tau_div(a)^2/phi(4a-p) - sum_g c_a(g)^2]
is <= -p*log(p)/24. The same obstruction covers any adaptive per-shell selection of at most J even-character modes
(including any subgroup observation B containing -1 with index <=J) at p>=2^20*J^3, and bounded-condition
positive shell weights with their explicitly changed threshold.

The estimate is a VALID lower bound. Its negative upper bound is a failure of
this particular principal/limited-resolution magnitude approach, not a theorem
that the positive original sum is zero or small. The diagonal word mass is
exactly cancelled in the true signed character expression. Estimating all
nonprincipal terms by adverse magnitudes loses that cancellation.

The original p-coloured pair source has a free Klein-four action, so every local
pair count is divisible by four. An unsaturated subgroup B supplies the exact
integer lower bound

    sum_(cosets C) b_(|B|/2)(m_C) - collision_energy,
    b_s(m) = s*floor(m/s)^2 + (m mod s)*(2*floor(m/s)+1).

No subgroup saturation is assumed. The full fine counts and kernel differences
remain. Complementation supplies the additional fixed-residue parity and
labelled discrete-convex refinement. A positive bound returns an original pair,
then an E/M state and ordered denominators.

## Mandatory negative controls

- p=87481: EVERY first-half real principal bound and its basic integer version
  is nonpositive. There are nevertheless 34 occupied shells. Arbitrary
  nonnegative weights on those scalar bounds cannot help. An index-three
  observation at R=31 returns an existing endpoint E state.
- p=944329, a=236098, R=63: B=<-1,13> has size12, quotient C3, masses8,8,0,
  energy16. The integer lower bound is exactly8. Both occupied coarse counts
  reduce to zero in F2 and retain their original words. This is a real lift,
  not an assertion that a coarse nonzero class automatically lifts.
- At the SAME p, a=236094, R=47, T=60 but all nonterminal subgroup choices of
  the present kind are unavailable: the group has order46 and the only
  subgroups containing -1 have orders2 and46. The order2 choice is the exact
  target computation, not a new reduced proof. HOWEVER, retaining only the
  principal mode and chi^(+/-1),chi^(+/-2), where chi(5)=zeta23, proves T>=60.
  Exact rational intervals for the two energies are(1009,1010) and(24,25).
  This proper five-mode projector is not a quotient by an intermediate subgroup.
  Keep this surviving map; subgroup nonexistence does not disprove spectral repair.
- p=3361, a=847, R=27 has positive principal mass and zero original target.
  Keeping only that mass or replacing the signed operator by a positive norm
  would give a false proof.
- The verified square-graph cycles and missing carry lifts from Turns2--5 remain
  valid negative controls. Do not return to canonical cycle closure as if it
  had not been refuted.

## The unproved universal assertion remains explicit

For an arbitrary prescribed hard prime, prove either:

    sum_(p/4<a<p/2) T_a > 0,

or a genuinely sufficient positive bound on it. The expression involving
chosen coset bounds, with negative bounds replaced by zero, is sufficient;
its positivity is NOT established universally. A finite successful scan or a
single occupied coset is not a discharge of this assertion.

An exact next analytic input is the diagonal-free identity

    T_a = 1/phi(R) sum_chi chi(-1) (|sum_(d|pa) chi(d)|^2 - 2*tau_div(a)).

The diagonal was removed by the exact character identity sum_chi chi(-1)=0,
not by an estimate. Proving a useful ONE-SIDED bound for its actual original
signed arithmetic sum, using the same-p relations R=4a-p, is still needed.
A bound on independent arbitrary arrays or another Gaussian/metric inverse
is insufficient. Alternatively, prove that the actual full-shell inventory
forces a positive proper-spectrum or nonterminal quotient certificate; do not assume its output.

## Executed finite scope

- Complete first-half atlas for all 211 p=1 mod4 primes <=3000:
  73798 shells, 1877004 original square-divisor vectors,
  5700 E states, 5268 oriented M states, 70596 target pairs.
- All 4519 hard primes <=2m:4515 principal certificates;
  exact misses87481,196561,944329,1915201; explicit quotient/integer repairs.
- Independent implementation replays EVERY first-half shell at all four misses,
  not merely a fixed residual prefix. Original counts are not new overall ES
  coverage. Generic Cauchy--Schwarz and integer balancing are classical ingredients.
- Discovery-only extension to10m reports20513 hard primes and a fifth scalar
  miss5410441, with an observed R31 quotient repair. That larger scan is NOT
  independently replayed in the release theorem lane.

## Status

Turn 6 executed the prescribed complete-sum attempt and proved the quantitative
failure of a specific attempted bound. It did NOT complete the universal closure.
Turn 7 must not treat that missing lower bound as a hypothesis already obtained.
No theorem depending on it may be labelled unconditional. No Lean build or
independent mathematical review is claimed.

The new proper-spectrum example has60 target PAIRS, not60 distinct ES states.
Every common gcd/p-colour fibre is retained. The full log modulo46 is kept when
observing its even-character image modulo23. The norm polynomial is not an
injective transform of the original counting polynomial.

## Effective all-sublinear refinement

For m>=3, let K_m be the product over primes q<2^m of the maximum of
(e+1)^m/q^e for 0<=e<2m, and C_m the least positive integer with C_m^m>=K_m.
The written monotonic-ratio proof gives tau_div(a)<=C_m*a^(1/m) at every a.
If p>=2^20 and p^(1-2/m)>=12*J*C_m^2, the raw complete-sum lower estimate
retaining at most J even modes per shell is <=-p*log(p)/8. The condition can
be checked using only integers as p^(m-2)>=(12*J*C_m^2)^m. For m=4, C_m=9;
thus p>=max(2^20,944784*J^2) suffices. Choosing m with 2/m<delta gives an
explicit onset for every per-shell budget at most p^(1-delta). This is NOT
an obstruction to every algorithm using few modes: zero truncation, integer
refinement, arbitrary sparse shell selection, and additional signed arithmetic
estimates are outside the proved raw-sum bound. The constant checks include
m=3,...,8; the general statement is proved by the all-exponent ratio argument.
