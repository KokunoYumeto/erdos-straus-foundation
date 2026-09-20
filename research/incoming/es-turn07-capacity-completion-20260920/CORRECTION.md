# Correction: one gate in the predecessor's textual alpha inverse domain

Affected source: `es_turn7_fabel_bridge_20260920/core.tex`, subsection
“Complete inverse fibres and coefficient collisions”, alpha formula with
N=(p+4c^2)/h and s|N.

That formula's stated coprimality and first-half tests do not imply the original
exterior gate. The complete inverse additionally requires

    R=4hrs-p > 0,  R | (4hr^2+1).

At p=5209,h=95,c=2 (t=4), N=55, s=5,r=4 satisfies the factor equation,
coprimality, shape and range. It gives a=1900,R=2391,u=1520 and

    (4u+1) % R = 1299.

It is not an exterior state.

The predecessor Python inverse-fibre enumeration already checks this original
E gate before appending a state. Thus the correction concerns the prose claim
about the complete inverse domain, not the forward channel theorem or a
previously admitted executable preimage. The original files and their hashes
are preserved in the preceding ZIP. The present `core.tex` equation (21) and
both new implementations retain the full gate.
