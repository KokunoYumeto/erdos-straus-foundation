# Independent finite-character proof review

Status: **passed** for the four declarations and their complete supporting
arguments in `sieve_character_cover.tex`, read in full. No unresolved
mathematical findings in this scope.

Reviewed source SHA-256:
`916d7bc2a16d681c223de5f73330378f1babf70f7f4c0d657a93926deb5aae3c`.

This review concerns the exact finite character restriction, its labelled
polynomial fibres, and the finite-history identities. It does not independently
verify a Navier--Stokes existence or blowup theorem. The source matrix's
external provenance belongs to the preceding source audit; the literal matrix
used here is checked directly in every calculation below.

## Proof review

1. **`lem:ns-labelled-character-packet`.** The finite character group is
   constructed on the actual multiplication table. The subgroup extension
   argument proves the existence of a character separating any nonidentity
   element, including its well-definedness under two representatives. Finite
   translation then proves character orthogonality. Expansion keeps each
   original prime, valuation bound, and independent formal variable. The
   resulting coefficient is exactly the indicator of the target residue for
   that complete valuation vector. Its integer return is unique prime
   factorization. Both ES targets are units under the displayed shell
   hypotheses.

2. **`thm:ns-character-coset-correction`.** Eliminating the first output
   equation gives the exact root equation
   `14 alpha = 5 gamma - eta` and inverse coordinate
   `beta = gamma - 3 alpha`. Its solutions form one full translate of
   `D[14]`; the image criterion, kernel, quotient map, and exact sequence
   follow in both directions. For the shifted map, the representative of
   `eta - 5 gamma` is unique, and its root equation has precisely
   `delta = |D[14]|` solutions. Consequently every target has delta
   preimages, giving exactly the denominator `delta |D|^2`. The family
   of evaluation maps into the auxiliary tori retains both entire character
   tables, has the stated coordinate inverse on its image, and intertwines
   the literal matrix entry by entry.

3. **`thm:ns-sieve-alias-removal`.** Expanding a fixed pair of original
   monomials yields precisely the equations `g^3 k = 1` and `g k^5 = 1`.
   Their complete solution is `g^14 = 1`, `k = g^(-3)`, so every alias
   term and its sign are accounted for. The corrected phase includes the
   representative in the *twisting character as well as in the packet*.
   Its quotient character cancels all `k != 1` terms; the displayed
   Bezout identity then forces `g = 1`. Every surviving original exponent
   pair remains an independent monomial. The equivalent interpretation as
   Fourier coefficient extraction uses the transported target `J(t1,t2)`;
   it must not be interpreted as an unchanged target coefficient. The
   manuscript's definition of the fully twisted function `F` implements
   the correct transported target.

4. **`cor:ns-finite-history-sieve`.** The affine iteration expansion has
   the correct powers `J^(k-1-j)` and the correct placement of every
   retained representative. The inverse at each stage has a unique last
   representative and delta predecessor states. Induction gives exactly
   `delta^k` labelled histories, including one history at `k = 0`.
   Counting those full fibres proves the polynomial average and the
   original single-packet character projection. The concluding arithmetic
   return uses the previously established no-hit theorem explicitly;
   these operator identities assert preservation of the ES fibres, not
   nonemptiness of an empty fibre.

## Exact computations

Run from any working directory:

```powershell
python 'ns_operator_bridge/check_coset.py'
```

The checker uses only integers and rational fractions. It enumerates integer
character-exponent histograms, constructs the exact monic cyclotomic
polynomial by division of `X^N-1`, and reduces each histogram modulo that
polynomial. No floating-point tolerance or assumed orthogonality predicate
evaluates the character sums. Direct finite map enumeration is separate from
the displayed root-equation test.

`COSET_CHECKS.json` records a passing run over:

- 11 cyclic and noncyclic groups;
- 2,015 complete target fibres and 2,015 character-basis pairs;
- 270 packet target pairs and 33,877 original monomial-pair tests;
- 755,963 explicit labelled histories, each checked against the full closed
  iteration formula and the exact terminal fibre size.

The unit-group fixtures include explicit multiplication-preserving coordinate
bijections for `U(3)`, `U(7)`, `U(8)`, and `U(15)`. In particular, the correct
group is `U(15) = C4 x C2`, with coordinate map
`(e,f) -> 2^e (-1)^f mod 15`. The originally requested `C2 x C2` label for
`U(15)` was corrected during review; `C2 x C2` is separately tested as
`U(8)`. This correction changes no abstract theorem in the source.

For the original shell `p=13`, `a=4`, `R=3`, the complete packet retains
prime 2 with exponents `0,1,2,3,4`, hence divisors `1,2,4,8,16`. The exterior
target 2 has the exact exponents `1,3` and divisors `2,8`. The uncorrected
pair average is 13; the corrected pair average is 4 and retains exactly the
four original exponent pairs. Under two bare matrix iterations, extraction
at the transported first-packet target `(10t,8t)=(0,0)` gives 5, whereas
the original target coefficient is 2. The checker records every exponent
pair, so these cardinalities do not replace the full fibres.

The checker SHA-256 is
`62c1132b6b95bc87fbad9cbe8825002e7a9bc41f6764743a9971c6bcec355678`.
The JSON binds the same reviewed source hash. Finite computations are
corroboration; the general proof review above is the basis of the passed
declaration status.

## Repaired review wording

The phrase "character with nonunit value" was replaced by "character whose
value at k is not 1". All complex character values are multiplicative units;
the proof needs precisely a value unequal to 1. The source hash above
includes this wording correction.
