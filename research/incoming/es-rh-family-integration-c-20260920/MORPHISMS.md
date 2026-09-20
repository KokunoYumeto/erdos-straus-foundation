# Typed maps and interfaces

## Mixed physical source

\[
X:\mathcal P_N\longrightarrow\mathscr H,\qquad
J:\mathcal P_N\longrightarrow C,\qquad
\mathcal R:C\longrightarrow\mathscr H.
\]

Here \(J\) is onto and \(\mathcal R\) is a right inverse of the ambient physical value map. With \(H_X=X^*X\),
\[
Z=(I-XH_X^{-1}X^*)\mathcal R,\qquad
H_Z=Z^*Z,\qquad
F=I-JH_X^{-1}X^*\mathcal R.
\]
The compatibility map is the inclusion
\[
\ker H_Z\hookrightarrow\ker F.
\]
Restricting \(H_Z\) to its positive range gives the exact covariance
\[
C=FH_Z^+F^*:C\longrightarrow C.
\]
For the onto observation \(\Lambda:C\to C_{\rm obs}\), the old kernel is \(K=\ker\Lambda\). JS5–JS9 prove the exact quotient and restriction maps and their determinant allocation; the mixed block \(T_{12}\) is part of the map.

## Labelled local algebras

For each chosen label match \(\rho\leftrightarrow t_{i,\rho}\),
\[
\Phi_{i,\rho}:
\mathbb C[t]/(t-t_{i,\rho})^{m_{i,\rho}}
\longrightarrow
\mathbb C[s]/(s-\rho)^{m_{i,\rho}},
\qquad
t-t_{i,\rho}\longmapsto s-\rho.
\]
Its inverse sends \(s-\rho\) back to \(t-t_{i,\rho}\). Taking the labelled direct sum and tensor product gives the full finite-algebra isomorphism used by ER1–ER2, including every nilpotent level.

## Common reducing space and return

The inclusion
\[
\iota:\mathscr T=\mathscr W^{\rm joint}
\hookrightarrow\mathscr H_{\rm tensor}
\]
retains the generated top chains. ER6 and ER7 define spectral projectors only after restriction to \(\mathscr T\). ER8 gives the orthogonal return
\[
P_{\rm cyc}:\mathscr W^{\rm joint}\longrightarrow\beta(C_k),
\]
with its weighted kernel at every level. The ambient counterexample in INTEGRATION_AUDIT_20260920.md proves why the Casimir interpolation cannot be extended as the same projector on all of \(\mathscr H_{\rm tensor}\).

## Collision map

\[
E_{z,\eta}:
\mathbb C[u]/(u^e(u-z)^f)
\longrightarrow
\mathbb C^e\oplus\mathbb C^f,
\qquad \eta=|z|^a.
\]
Its two components are the divided jets at \(0\) and \(z\), including every row factor. CP2–CP11 prove the singular and inverse-exterior exponents of this exact map. A change of input coordinates is transported through \(\wedge^r C\), and a physical target multiplier is retained as \(T(z)^{-r/2}\) on the inverse rank-\(r\) exterior norm.

## Interface not yet constructed

The trace-rigidity continuation maps raw divisor words to literal rational trace labels and has fibre involution \(U\leftrightarrow a^2/U\). Family C maps labelled tensor occupations to \((\kappa,\theta,D)\) top chains and then to a metric quotient. No identification of these target presentations is assumed.

The strongest proved present correspondence uses their common source. Let \(\mathcal E\) be the set of sorted integral ES witnesses with all retained labels. The trace construction gives a map \(\tau:\mathcal E\to\mathcal T_{\rm raw}\), and ER11 gives a map \(\epsilon:\mathcal E\to\mathcal O_{\rm occ}\). Therefore
\[
(\tau,\epsilon):\mathcal E\longrightarrow
\mathcal T_{\rm raw}\times\mathcal O_{\rm occ}
\]
is an exact span relating the two calculations. Its projections recover the existing maps without information loss beyond the respective fibres. A morphism directly from one target to the other has not yet been proved.

The exact next bridge requires:

1. a column map from raw divisor words into the cyclic space \(C\);
2. the literal observation \(\Lambda\) on those columns;
3. a physical lift into the source \(\mathscr H\);
4. proofs of its fibres, kernel, induced Gram form, and compatibility with the trace involution.

One failed identification does not establish disconnection; these four typed arrows state the missing construction.
