# Integration audit: square-zero defects, factor-sum returns and fixed-tail fibres

## Received identity

The supplied outer archive is
`ES_Turns6_7_With_Square_Zero_Pell_20260922.zip`, 25,282,872 bytes, SHA-256
`6708E1277F64AAD2F596BF9E7AC5217212BAE451D88A6644D53D7333DEFC0684`.
The nested archive has SHA-256
`2697DDB6ADA7E088EC172EED495F4E215D6B088B57FD707A2170960FDF0A91FF`.
The accompanying 23,609-byte pasted handoff has SHA-256
`44836BCC6CAC0A447DF310F763A3D33F632C8E3390E2213BFF45E915348AF599`.
These identities are also serialized in `RECEIVED_ARCHIVE.json`.

The nested manifest contained 44 entries. Every listed byte length and SHA-256
hash matched the extracted file. Extraction was read-only; the integrated
module was copied separately before editing.

## Reading and first replay

The complete 717-line `core.tex`, both Python implementations, both TeX
readers, the claims and morphism ledgers, the source ledger, execution receipt,
handoff and negative controls were read. The unmodified supplied package was
then replayed in a new directory:

- main implementation: 26,232 assertions;
- separately written checker: 26,961 assertions;
- nine mathematical JSON outputs identical under ordinary and optimized
  Python;
- all nine hashes identical to the received package.

This replay is implementation agreement, not independent human review.

## Mathematical admission and corrections

The following results survive direct algebraic checking and fresh execution:

1. For `R=KD=delta*D^2`, the ideal `K Z/R Z` is square-zero and is additively
   isomorphic to `Z/D`. The unique defect `c` has zero fibre exactly the full
   original gate, and the common reduced tail denominator is
   `D/gcd(D,c)`.
2. The mixed integer-exponent law retains the literal E/M channel exponent and
   every centred prime exponent. Its bounded-box hypotheses cannot be replaced
   by membership in a generated subgroup.
3. The exact finite coefficient polynomial counts every original word with
   multiplicity. The unit-width threshold `D-1`, its sharpness construction and
   the Fourier coefficient stabilizer are proved at the coefficient level.
4. The prime-power M classification and the complete prime-square channel
   classification are exact. Proper prime-square M sources are terminal for
   the two inherited same-word and fixed-ray deletion systems only.
5. The factor-sum map retains raw `r` and `h+s`, changes
   `(h,s)` to `(h-delta*w,s+delta*w)`, restores the target gcd, and has the
   stated complete marked inverse. Its square-carrier restriction is Pell.
6. The least-prefix theorem at `p=67369` is a complete finite statement in its
   advertised prime class. It excludes a universally nonincreasing first
   denominator on every trace; it is not an Erdős--Straus counterexample.

One scope distinction required explicit repair. The literal prime-square scan
at `p=67369` has an empty source fibre. The eligible carrier primes are

`131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181`,

and all 44 combinations `u=q` or `q^3`, E or M, fail the square gate. The real
least-prefix obstruction at this prime is the composite carrier

`a=16849=7*29*83`, `R=27`,

with four proper E words and four proper M words. Its first full shell is
`a=16850`, `R=31`. The module never identifies this composite shell with the
prime-square family.

The stronger statement that every proper trace at this prime is terminal is
false. For example,

`(a,R,u,channel)=(18208,5463,2,M)`

has a same-word return through `k=9` to `(a',R')=(16994,607)`. The reduced tail
denominator also decreases from three to one when an integral target is
allowed above the first trace shell. The proved obstruction concerns `a`,
equivalently `R` at fixed `p`, not the rational tails' reduced denominator.

For comparison, the nearest reconstructed prime-square diagnostic is

`(p,q,a,R,u,channel)=(68329,131,17161,315,131,E)`.

It is a proper trace with reduced tail denominator three and an empty tested
squarefree target shell `R'=35`. This illustrates a map-specific failed return;
it is not a universal obstruction.

## New continuation: the numerical tail-sum fibre

The integrated continuation proves an exact theorem not present in the received
source. At fixed prime `p` and numerical tail sum `N=Y+Z`, every ordered
integral first-half target is determined by

`rho=4A-p` and `Delta=Z-Y`,

with

`rho | N`, `0<rho<p`, `rho=-p mod 4`, and

`Delta^2=N(N-p)-N*p^2/rho`,

plus positivity and parity. This is a finite divisor-and-square bijection. If
`rho=delta*v^2`, then `X=v*Delta` satisfies the exact Pell lattice equation

`X^2-N(N-p)*v^2=-N*p^2/delta`,

with essential divisibility and congruence gates. In shifted factors the larger
norm equation is exact, but an integer-tail return additionally requires
`rho | w`. Failure of this gate defines the return defect rather than erasing
the norm point.

For the proper M source `(67369,16849,27,1421)`, the fixed sum is `586110300`.
The complete residual list is `3,15,75,87,435,2175`; one discriminant is
negative and the other five have explicit quadratic-nonresidue certificates.
Across all 69 proper trace tags at the prime, there are 51 distinct sums and
507 eligible residuals; 478 discriminants are nonnegative and none is a square.
The 47 integral tags have 37 sums, disjoint from the proper set. A positive
control reconstructs both tail orders at `R=31`, `a=16850`, `u=674`.

After this addition, a fresh two-lane replay reports:

- main implementation: 26,310 assertions;
- separately written checker: 27,484 assertions;
- ten mathematical JSON outputs identical under ordinary and optimized
  Python.

The fixed-tail theorem retains `Y+Z`. It is not the factor-sum map, which
retains `h+s`, and it does not obstruct a construction that changes the
numerical tail sum.

The exact fibre was then propagated back through every proper prime-square
source. If `R=k0*eta^2` and `H=k0*eta*F` is the canonical source
factorization, then `gcd(R,N)=k0`. Any same-`N` integral target at a residual
`S` dividing `R` must satisfy `S|k0`; exact target decoding forces the target
channel to equal the source channel and forces `q` into its gcd factor. The
four source rows reduce to three contradictions: one for E at `u=q`, one for
E at `u=q^3`, and one covering both M orientations. Therefore no proper
prime-square trace has a same-`N` integral return whose residual is a proper
divisor of its source residual. The result leaves smaller nondivisor
residuals, and every change of `N`, outside its scope. The new `k0` is not the
square-zero modulus `K`.

## Literature use

The completed disk-literature index was used for routing. The canonical
Elsholtz--Tao source unit is `PUBUNIT-1D778B56AC2B71BF35EB40F9`; its original
author TeX is `egyptian-count18.tex`, SHA-256
`B0469A67A737B7F4E77778310C87E22F5783AE9704F70AA55919A4A40104611C`.
Lines 487--627 were read for the Type-I/II definitions, converse maps and nine
coordinate equations. A hash-identical copy is retained in the preceding
global-receiver module. The earlier PDF-reading label in `source_reading.json`
has been corrected to this author-TeX source and locator.

Yamamoto's Lemma 2, equation (4), printed page 38, supplies the inherited
exterior congruence antecedent. Sutherland's Theorem 18.1 supplies Dirichlet's
theorem only after the relevant CRT classes are proved reduced. Exact local
index queries did not find author TeX for those two sources; their primary PDF
locators are recorded. No scoped search result is treated as proof of
historical priority.

## Scope boundary

No Lean build, universal Erdős--Straus proof, historical-priority theorem or
independent human review is claimed. The finite checks prove their exact finite
statements and corroborate the displayed universal identities. The workbench
keeps every definition, map, inverse, exceptional locus and nonclaim needed to
reproduce those statements.
