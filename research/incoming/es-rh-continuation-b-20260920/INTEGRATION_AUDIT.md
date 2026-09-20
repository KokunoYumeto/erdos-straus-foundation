# Integration audit

## Corrections made to the working source

1. The Type II witness branch originally left a formal common valuation (r\ge2) beside the positive integral argument.  The working source now proves
   \[
   \frac p4<z\le\frac{p^2}{4p-2}<\frac{p+1}{4},
   \]
   which contains no integer when (p\equiv1\pmod4).  Thus an actual positive Type II witness has (v_p(x)=v_p(y)=1).  The (r\ge2) substitution is retained only as an exact polynomial specialization with an empty positive-witness locus.
2. The first draft of the independent checker incorrectly evaluated a Legendre-symbol routine with a composite CRT residue as denominator.  The final checker instead evaluates the three reciprocity conditions at the prime CRT coordinates (5,7,17,73).  It then recovers exactly 3,456 classes modulo 521,220.  The failed draft produced no published receipt.

## Proof audit

- E1 is tested before any modular inversion of (S).
- The denominator divisibility split is exhaustive: at least one and at most two denominators are divisible by (p); Type I has valuation one; Type II has two equal valuations, and positivity forces both to equal one.
- The Type I off-diagonal reduction has discriminant (-511).  The retained diagonal coefficient has square class (1241) because (153\cdot1168=12^2\cdot1241).  The Type II obstruction has discriminant (-15).
- The five finite witness lists are complete by the displayed divisor parametrization; their counts are (8,29,44,34,48).
- In the (q=61) fibre, the quartic coefficients, roots, derivatives, four nonsquare tests, eight extension points, twist points, forward coordinates and Frobenius transpositions were reconstructed directly.
- D5--D10 retain one quotient and all four endpoint determinants.  The sharp scalar optimization is an equality-capable consequence of its stated constraint, not the whole programme action.
- H4--H10 distinguish the entire holomorphic heat series from positive singular-value heat.  H11--H15 are finite-dimensional estimates in the retained metric and preserve the small-time hypothesis.

## Verification boundary

The local receipt is:

```json
{"exact_checks": 923, "scope": "Independent replay of Continuation B Tracks I and IV only", "status": "PASS"}
```

The received JSON reports 1,121 new checks and 1,660 combined checks, but its underlying four new-suite scripts were not among the supplied files.  Those numbers remain source-reported rather than locally replayed.

## Figure QA

`arithmetic-frame-sieve`, `determinant-heat-mechanism` and `finite-field-twist-descent` were regenerated from `tools/generate_20260920_illustrations.py` in PDF and PNG form and visually inspected.  They preserve the equations, hypotheses, fields, maps, point counts and proof boundaries stated in the text.

## Nonclaims

- No result here proves existence of an Erdős--Straus witness at every prime.
- A failed character test does not imply (N=0).
- The finite-field cover does not delete the original integral witness.
- Its local zeta function is not the Riemann zeta function.
- The determinant return and heat certificate do not equal the programme's unassembled arithmetic action.
