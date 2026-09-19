# Exact Lean-ready dependencies; no build claimed

A. OriginalExterior p a u with p=1 mod4, p/4<a<p/2, gcd(p,a)=1, u|a^2,
   (4a-p)|(4u+1). Use integer inequalities to avoid rational truncation.
B. Prove gcd normalization, ordered rational identity, complement v and cofactor D.
C. Prove h>1 from the impossibility of -1 as a square modulo a 3-mod4 integer;
   derive v!=R,D using the factor h. Do not assume gcd(v,D)=1.
D. Establish (p+R)^2+4v=4vRD and p+R<2vD. Prove the two cases of the t=min(R,D)
   bound, then the strict cubic inequality using v!=t and the square-mod4 equality
   obstruction. A polynomial/nonnegative-square proof can replace the radicals.
E. Define C(p) as the final true integer of the proved monotone predicate. Establish
   its bounds and binary-search specification, not by trusting floating point.
F. Prove K(v)|a iff v|a^2 using prime valuations.
G. Construct Equiv OriginalExterior (Direct + Reciprocal + NormChart), with all
   chosen inequalities, orientation and ordered denominators. All maps are given
   explicitly in core.tex.
H. State finite test theorems separately from the universal existence target.
   No axiom asserting positive original counts, graph escape-to-hit, or ES is used.
