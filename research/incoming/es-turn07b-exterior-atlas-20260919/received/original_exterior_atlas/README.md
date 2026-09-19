# Turn 7 continuation: exterior complement--norm atlas

The universal existence requirement is unresolved. This tranche does not advance
that missing assertion to Turn 8. It supplies the missing exterior counterpart
to the previous complete middle-state decision atlas, and a reliable rebuilt
source handoff for the preceding work.

## Main statement
For every unit first-half exterior state, retain R, D=(4u+1)/R and v=a^2/u.
With w=min(R,D,v),

    (p+w)^2 > 4(w+1)^2(w-1).

The maximal integer satisfying this inequality is C(p)=(p/2)^(2/3)+O(p^(1/3)).
The resulting three disjoint charts are the direct shell, reciprocal sum-gate,
and complementary norm-divisor chart. The last requires BOTH R|(p^2+4v) AND
R=-p mod 4K(v), where K(v) is the primewise square-root divisibility kernel.
The latter is the original condition v|a^2; it is not optional.

At the hard prime p=48049, an original E state has R=D=311, above the preceding
middle cutoff 247. Its triple is (12090,1867905,179501934690). At p=37 the original
v=18 and D=3 are not coprime. These are explicit negative controls against
transferring a different chart's bounds or cancelling unavailable units.

The unit integer family h=4n^2-2, R=D=4n^2-1 has p=16n^3-4n^2-8n+1 and
min(v,R,D)/(p/2)^(2/3) -> 1. No infinite prime subfamily is asserted.

## Reproduce

    python verify.py --bound 3000 --out certificates
    python -O verify.py --bound 3000 --out certificates_optimized
    python check_independent.py --input certificates --out independent.json
    pdflatex -halt-on-error workbench.tex
    pdflatex -halt-on-error workbench.tex

The second checker imports none of the first program or its predecessor. It
enumerates the full primitive h,r,s source. The finite replay tests a proved
atlas; it is not evidence that every prime has a state. Source and output
hashes, command outcomes and bounds are in EXECUTION.json and the certificates.
No historical-priority claim, full-history mathematical audit, remote
publication, Lean build or independent mathematical review is inferred.
