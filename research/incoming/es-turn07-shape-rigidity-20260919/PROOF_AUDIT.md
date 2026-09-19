# Proof audit for the Turn 7 shape-rigidity continuation

This audit concerns the mathematical claims in `core.tex`, not merely the
presence of files or agreement of record counts. Four isolated re-derivations
were carried out before integration. Each retained the ordered source
coordinates and checked the displayed maps in both directions.

## Diagonal exterior-to-middle return

Starting from an actual original exterior state with `R=D`, the audit rederived

\[
z=(R-1)/2=\delta t^2,
\qquad c=(p+1)/\delta,
\qquad j=(\delta+1)/4,
\]

where `delta` is the positive squarefree part and `t` is a positive odd
integer. It checked `delta | a`, `delta | p+1`, `delta = 3 (mod 4)`, the
original middle gate for `(a_M,u_M)=(jc,j)`, both ordered denominator
orientations, and the strict inequality `min(R_M,Q_M)<R`. The complete fibre
over a retained middle mark is the positive odd `t` satisfying the source
divisibility conditions; the map is not represented as injective after that
integer is forgotten.

## Radius-seven and radius-eight rigidity

The radius-seven audit independently exhausted all 52 ordered nonzero profiles
with coordinates in `[-7,7]` and congruent modulo four. It checked the complete
`B=alpha*beta-1` spectrum and each exceptional large-prime row. The surviving
singular family is exactly

\[
h=4n^2-2,\quad r=n,\quad s=1,\quad R=D=4n^2-1,
\quad \kappa=4n^2-n-1,
\]

with even `n`, and it has the two stated original middle orientations.

The radius-eight audit independently exhausted the 12 new ordered pairs and all
16 eligible grade rows. The only possible nonsingular profile is
`(alpha,beta,h)=(8,-4,11)`, with

\[
4r^2=11s^4-4s^2-3.
\]

The grade congruence was then used directly to construct the original middle
state `(h_M,r_M,s_M,lambda_M)=(1,3,(p+3)/11,1)` with `u_M=9`; no quartic
integral-point classification is assumed. Reducing the retained quartic
conditions modulo `3`, `5`, and `7` strengthens the possible hard residue
classes for this branch to `p mod 840` in `{1,121}`.

## Marked cubic and involution

The cubic audit checked the ordered inverse

\[
R=X-\alpha,\quad D=X-\beta,\quad a=Y/2,
\quad p=2Y-R,\quad u=(RD-1)/4,
\]

the fixed-prime line `2Y=p+X-alpha`, and the distinction between the cubic
polynomial discriminant and the Weierstrass discriminant
`16 B^2 ((alpha-beta)^2+4)`. For the rational involution
`(X,Y) -> (B/X,BY/X^2)`, the full transported coordinates
`(h',r',s',R',D',a',u',kappa',p')` were checked. Its integral branch does not
preserve the fixed prime: `p'-p=(4r-1)(4r^2-R-D)`. The displayed value
`p'=5951=11*541` is therefore identified as a composite parameter, not a prime
source.

## Executable replay and its boundary

The supplied main verifier and Python-optimized replay agree byte-for-byte on
the four deterministic certificate files. The strengthened independent checker
does not import the main verifier or predecessor module. It recomputes hard
flags, the 52 radius-seven profiles, the 12 radius-eight pairs, 16 grade rows,
ordered denominators, and the fixed prefix `s<=200000` of the quartic search.
It also hashes every certificate it consumes.

At the declared prime bound `3000`, the scan contains no actual hard
radius-seven or radius-eight state. Thus the conditional rigidity theorems are
supported by the complete finite profile proofs above, not inferred from a
vacuous scan branch. The quartic prefix is a bounded calculation and is not an
effective cutoff or a global integral-point theorem.

No universal Erdős--Straus theorem, universal E/M occupancy theorem,
historical-priority determination, independent human review, or Lean proof is
claimed.
