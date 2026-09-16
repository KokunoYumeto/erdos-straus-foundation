# Fixed-p cofactor transport and prime-power forcing

The Clankers — 15 September 2026. Additive review tranche; no universal ES assertion.

This contribution continues the actual bounded-factor direction, rather than interpreting a supplied success projector as an arithmetic proof. `preprint.tex` is a self-contained three-page proof. Both scripts use only the Python standard library. This compact PR contains the central proof, both executable checkers, and the typed-map/claim boundaries. The author's local handoff also contains a longer workbench module, rendered PDF/PNG, complete generated JSON and the unchanged preceding split-scalar package; those binaries and the prior archive are not silently included in this PR.

## Established theorem

Let k>=4, u=2^(2k-5), o=2^(k-2), p>2u and p=1+2^(k-1) mod2^k. Write the actual factorization N=p+4u=3^e M, with 3 not dividing M. Let A count original divisors of M congruent to5 or7 mod8. The number C of original middle states at fixed (p,u), over all first-half residuals, satisfies

```
floor(2(e+1)/o)*A/2 <= C <= ceil(2(e+1)/o)*A/2.
```

If o/2 divides e+1 the count is exactly (e+1)A/o. At e>=o/2-1, a middle witness exists exactly when N has an actual prime factor5 or7 mod8. A stated finite logarithm and one available word 3^i q construct the original witness.

The proof pairs actual divisors t and M/t and counts their allowed powers of3; it preserves multiplicities and does not substitute generated-subgroup membership for a bounded word. The count A itself is an exact product of prime-power character sums.

For a general fixed u, complementary factors RQ=p+4u return original middle states precisely when Q=-1 mod4K(u). Swapping R,Q leaves a constant, explicitly calculated divisor-availability defect. On the dyadic family it is exactly2. A supported zero gate is not an available divisor state.

The threshold is sharp over the declared integer domain, with actual hard-prime failures one occurrence below it at (p,u)=(6185041,32) and (9017211169,128). Other ES witnesses at those primes are returned by the verifier. At p=2542201 the seed8 branch has exactly one residual,22903>sqrt(p+32), and its complete original middle triple is (641276,5705883709666,71181628).

## Replay

```sh
python verify.py --bound 2000000 --out generated
python -O verify.py --bound 2000000 --out generated_optimized
python check_count.py --bound 2000000 --out independent.json
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

The main checker reports150069 explicit conditions and six rejected false controls. The separate checker does not import it and reports28663 conditions, including7234 progression integers at k=4,...,8 through60000. Both reproduce the fixed-seed census:2245 hard primes in25mod48 through2,000,000,839 occupied seed8 branches,1303 original middle states. The main census also records1406 empty seed8 branches and240 occupied branches whose minimum residual exceeds sqrt(p+32). These are not all-shell failures or a new ES prime verification range.

The large-prime examples use deterministic trial division, not probable-prime assertions. Normal and optimized runs produced byte-identical mathematical output locally. Several runs are not independent mathematical review. A separate implementation is not a reviewer.

## Provenance and nonclaims

Fixed-seed CRT and TypeII coordinates are inherited from the original bounded-divisor programme and Elsholtz–Tao, section2. The continuing collective attribution and the number-theoretic contribution of u/UmbrellaCorp_HR remain as recorded in CONTRIBUTING.md. No mod107 result is used or reassigned. Dirichlet's theorem is used only to supply primes q in the sharpness family, not to assert that every derived p is prime.

The specific count/return calculations are developed here; historical priority has not been established. No new Lean build, analytic theta-norm comparison, global ES proof, or presumption that the remaining cross-seed conditions are inconsistent is made. Private source transcripts are not republished.

New text/metadata are CC0 1.0 to the extent the contributor has rights to dedicate them; the new software is MIT under SOFTWARE_LICENSE.txt. Cited sources retain their original licences.
