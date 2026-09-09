# Ordered-witness correction and exact inverse

## Findings and decisions

- The existing logbook and session provenance remain under parent ownership. This file records this bounded repair and its instruction without changing the cumulative manuscript or review records.
- Read the full no-hit source and checker, the original residual/divisor proof in `bounded_transport.tex`, and the unary chart proof in `unary_boolean_transport.tex`.
- The sentence asserting that every ordered witness has a unique `d=p^epsilon u` with `epsilon` in `{0,1}` is false. The full residual `d_y=Ry-pa` can have `p`-adic exponent 0, 1, or 2.
- The chart actually printed in the no-hit source has `d_y=p^epsilon a²/u` and `d_z=p^(2-epsilon)u`. Thus the unswapped exterior chart has exponent 0 in `d_y`; its transposed chart has exponent 2.
- Preserve the original chart and add the exterior swap bit. The exact domain is the disjoint union of `(0,u,sigma)` for `u in E_a`, `sigma in {0,1}`, and `(1,u,0)` for `u in M_a`. The middle complement already supplies its opposite orientation and receives no extra swap bit.
- A second error occurs in the printed common-denominator identity: `(pABCD)/a=pC`, not `pCD`. The repair corrects this integer calculation explicitly.
- Independent read-only checking was delegated for the three residual inverse cases, the middle complement, and the `p=13,a=4` fixture.

## Completed proof and independent review

The source now defines the full domain and codomain, the chart map `Phi`, the exact residual-divisor domain, and its inverse to the original ordered triple. It proves all three `v_p(d_y)` inverse branches:

| `v_p(d_y)` | `epsilon` | Original divisor `u` | `sigma` |
|---:|---:|---|---:|
| 0 | 0 | `a²/d_y` | 0 |
| 1 | 1 | `pa²/d_y` | 0 |
| 2 | 0 | `d_y/p²` | 1 |

Every gate is proved equivalent using specified units modulo the original `R_a`. Both inverse compositions recover all original exponents and chart coordinates. The swap involution retains the exterior divisor and toggles its bit; middle complementation replaces `u` by `a²/u` and exchanges `A,B` while retaining `C,D`. The two order-forgetting maps are explicitly typed, with their complete tag and witness fibres.

The independent reviewer confirmed every formula and the six-row `p=13,a=4` fixture. The reviewer requested explicit typing of the order-forgetting map because its displayed fibres consisted of tags; this was added. The same final edit wrote a modular unit as `[a]_R [u]_R^{-1}` instead of the potentially ambiguous notation `a/u`, and split long displayed equations. These edits change no arithmetic formula or test predicate.

At `p=13,a=4`, the omitted exterior orientations before repair were exactly `(4,130,20)` and `(4,468,18)`. The full passing residual set is `{2,8,26,104,338,1352}`. There are six ordered witnesses and three unordered pairs.

## Exact finite verification

The checker now independently factors the original `S=pa`, enumerates every divisor of `S²`, applies the original condition `R | d+S`, and reconstructs the ordered pair from the two complementary residuals. This route does not use an exterior or middle gate to select its divisors. It is compared with the entire oriented tagged chart, with uniqueness, both inverse compositions, each `p`-valuation count, the exact swap action, and every order-forgetting fibre checked.

Both runs passed:

| Prime bound | Primes | Shells | Original `S²` divisors | Ordered witnesses | Two-element order-forgetting fibres |
|---:|---:|---:|---:|---:|---:|
| 1000 | 36 | 8,124 | 503,580 | 1,828 | 914 |
| 5000 | 159 | 186,882 | 16,815,504 | 14,120 | 7,060 |

For the bound 5000, the residual-valuation counts at exponents `(0,1,2)` are `(5037,4046,5037)`. The run has 3,538 hit shells and zero no-hit primes. The finite verification does not prove universal occupancy.

The command `python counterexample_sieve/check_nohit.py --limit 5000 --certificate` wrote `CHECK_NOHIT.json`. Its source digest was refreshed after the final explicit quotient typing and equation formatting edit, with that timing recorded in the certificate. The checker did not change after its successful arithmetic run.

Final source SHA-256: `f440b496cf8298657b4bb17d2d97a12ce3392ca14ad09cb20859e97edbb608f2`.

Final checker SHA-256: `f3c0b332ae140a63e265377e1dc7ab8dd93f783168a159d92a6ca46391f440d2`.

## Integration boundary

Only `counterexample_sieve/all_shell_no_hit.tex`, `counterexample_sieve/check_nohit.py`, `counterexample_sieve/CHECK_NOHIT.json`, and this log were edited. Cumulative TeX, review, crosswalk, PDF and checkpoint records remain under parent ownership and must be refreshed there for this new source hash. No Lean process, publication, external mirror edit, or new NS implication is part of this repair.
