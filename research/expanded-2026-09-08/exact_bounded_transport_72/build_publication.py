"""Build the citation-bearing reading edition without changing canonical proofs."""
from pathlib import Path
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parent
original=(ROOT/"bounded_transport.tex").read_text(encoding="utf-8")
EXPECTED="4356f53962f2da9b418e066f2c2ca1ba9572e45dc398bb2ca4d37981301e5050"
assert sha256((ROOT/"bounded_transport.tex").read_bytes()).hexdigest()==EXPECTED
leaf_maps=[]
for name,note in [
    ("input_output_incidence.tex",r"\paragraph{Contribution provenance.} The input--output prime construction continues the arithmetic and Euclid material of \texttt{u/UmbrellaCorp\_HR} \cite{UmbrellaContribution}, including equations (88)--(90) and (96). The complete incidence fibres and witness returns below are subsequent proved calculations."),
    ("shared_variable_crt.tex",r"\paragraph{Contribution provenance.} The simultaneous constraints continue \texttt{u/UmbrellaCorp\_HR}'s equations (78)--(80), (88)--(90), (96) and (98) \cite{UmbrellaContribution}. This credit identifies the original arithmetic input; the full shared-variable construction below supplies its complete proof and computed lift fibres."),
    ("raw_scale_hit_incidence.tex",r"\paragraph{Contribution provenance.} The original positivity-code and Euclid/prime-production material is credited to \texttt{u/UmbrellaCorp\_HR} \cite{UmbrellaContribution}. The named intermediate project calculations \cite{PositivityTransport} below retain that lineage; they do not replace the original contributor's credit."),
]:
    raw=(ROOT/name).read_text(encoding="utf-8")
    edited=note+"\n\n"+raw
    if name=="shared_variable_crt.tex":
        edited=edited.replace(r"\input{input_output_incidence.tex}",r"\input{publication_input_output_incidence.tex}")
    dest="publication_"+name
    (ROOT/dest).write_text(edited,encoding="utf-8",newline="\n")
    restored=edited[len(note)+2:]
    if name=="shared_variable_crt.tex":
        restored=restored.replace(r"\input{publication_input_output_incidence.tex}",r"\input{input_output_incidence.tex}")
    assert restored==raw
    leaf_maps.append({"canonical":name,"publication":dest,"canonical_sha256":sha256((ROOT/name).read_bytes()).hexdigest(),
                     "publication_sha256":sha256((ROOT/dest).read_bytes()).hexdigest(),"inserted_provenance":note,
                     "mathematical_text_unchanged":True})
oldintro=original[original.index("This text retains"):original.index(r"\section{Original shells")]
newintro=r"""We study positive integer solutions of $4/p=1/x+1/y+1/z$ through
their complete bounded divisor-shell coordinates. The starting arithmetic,
positivity-code and prime-production constructions were contributed by Reddit
user \texttt{u/UmbrellaCorp\_HR} and developed further in this collaboration
\cite{UmbrellaContribution}. Their relation to the established Egyptian-fraction
parametrizations of Christian Elsholtz and Terence Tao is recorded explicitly;
the elementary reconstructions needed in this article are proved here
\cite{ElsholtzTao}. The cross-shell calculations classify ratio-preserving
transport and two elementary positive unimodular shears. The gluing
construction retains the finite exponent bounds throughout its integral lifts.
The divisor-category connection uses Alain Connes and Caterina Consani's
embedded ordered groups and their exact reciprocal-divisor locus
\cite{CCPericyclic}. A later part returns exact covering and inverse-operator
calculations to the auxiliary torus of the announced Navier--Stokes manuscript
\cite{OpenAINS}. No universal arithmetic occupancy, empty prime shell, or
complete fluid blowup proof is asserted by these calculations.

"""
aftertitle=r"""
\begin{center}
\small Arithmetic contributor: Reddit user \texttt{u/UmbrellaCorp\_HR}.\\
Expanded edition: 72 statements with full proofs.\\
Project DOI: \href{https://doi.org/10.5281/zenodo.20401937}{10.5281/zenodo.20401937}.
\end{center}
\noindent This edition adds fourteen statements to the 58-statement snapshot
\cite{PriorEdition}. The canonical mathematical source files are unchanged;
this reading edition adds contribution credit and citations at the relevant
source interfaces. Exact computation supplements the proofs at stated finite
bounds. References distinguish a contribution's mathematical source from
broader historical context. The full announced Navier--Stokes construction
remains outside this article's independent verification claim.
\par\medskip
"""
patches=[
    (r"\input{shared_variable_crt.tex}",r"\input{publication_shared_variable_crt.tex}"),
    (r"\input{raw_scale_hit_incidence.tex}",r"\input{publication_raw_scale_hit_incidence.tex}"),
    (r"\author{}",r"\author{The Clankers}"),
    (r"\maketitle",r"\maketitle"+aftertitle),
    (oldintro,newintro),
    (r"\input{unary_boolean_transport.tex}",r"""
\paragraph{Arithmetic lineage.}
The original finite-code and simultaneous-constraint input is the colleague's
continuation \cite{UmbrellaContribution}, especially its equations (71)--(100).
The intermediate source is \cite{PrimewiseCoordinates}.
The following construction proves the complete bounded code and witness
correspondences used here; it does not attribute this later proof to that input.
\input{unary_boolean_transport.tex}"""),
    (r"\input{boundary_swap/boundary_swap_completion.tex}",r"""
\paragraph{Boundary-source lineage.}
The same-tag exchange antecedent is \cite{SignedMarginAntecedent}, within
the arithmetic programme originating in \cite{UmbrellaContribution}.
The four-candidate construction below writes out all maps and proofs needed
for its expanded conclusions.
\input{boundary_swap/boundary_swap_completion.tex}"""),
    (r"\input{integral_cyclic_bridge.tex}",r"""
\paragraph{Cyclic-source interface.}
The degree-zero quotient and fibre-trace viewpoint is compared with
Connes--Consani \cite[Proposition 3.1 and equation (3.2)]{CCTrace}.
The following integral augmentation calculation is proved directly, including
its torsion and finite arithmetic return. It is not imported as a finite-box
lifting theorem from that source.
\input{integral_cyclic_bridge.tex}"""),
    (r"\input{connes_reading/connes_primitive_intersections.tex}",r"""
\paragraph{Divisor-category lineage.}
The precise source for the next construction is
Connes--Consani \cite[Section 7.4, Lemma 7.7 and Proposition 7.8]{CCPericyclic}.
The finite shell specialization, its primitive-pair return and its corrections
are the calculations proved below.
\input{connes_reading/connes_primitive_intersections.tex}"""),
    (r"\input{ns_operator_bridge/torus_cover_lemma.tex}",r"""
\paragraph{Source operators and intellectual context.}
The specific auxiliary matrix and original directions used below are from
\cite[Section 6.1, equations (6.1)--(6.7), and Lemma 6.2]{OpenAINS};
the separately pinned source is \cite{OpenAISource}. Earlier forced-fluid
research is credited in \cite{BuckmasterStatement,CMZEuler,CMZIPM,CMZHypo}.
The separate smooth-forcing IPM and Boussinesq manuscripts are
\cite{ABCIPM,ABBoussinesq}; their authorship and theorem domains are not
interchanged. None of these complete fluid theorems is assumed in the
arithmetic operator proofs below.
\input{ns_operator_bridge/torus_cover_lemma.tex}"""),
    (r"\input{ns_operator_bridge/reverse_proof_transport.tex}",r"""
\paragraph{Return to the continuous source calculation.}
The next two subsections address the actual continuous operators in
\cite[Lemma 6.2, (6.17)--(6.20), (8.4)--(8.10), (8.14), and
Lemma 8.6, (8.19)--(8.23)]{OpenAINS}. The sharp constants, full inverse
fibres and strengthened derivative estimates are proved here. The original
cutoff remainder and slow derivatives remain in those identities.
\input{ns_operator_bridge/reverse_proof_transport.tex}"""),
    (r"\end{document}",r"\input{publication_bibliography.tex}"+"\n"+r"\end{document}"),
]
result=original
for old,new in patches:
    assert result.count(old)==1,old[:80]
    result=result.replace(old,new,1)
back=result
for old,new in reversed(patches):
    assert back.count(new)==1
    back=back.replace(new,old,1)
assert back==original
(ROOT/"publication.tex").write_text(result,encoding="utf-8",newline="\n")
(ROOT/"PUBLICATION_EDITORIAL_MAP.json").write_text(json.dumps({
    "canonical_main_sha256":EXPECTED,"reading_main_sha256":sha256((ROOT/"publication.tex").read_bytes()).hexdigest(),
    "status":"reversing_all_editorial_insertions_and_author_label_recovers_the_exact_canonical_text",
    "changes":[{"original":a,"publication":b} for a,b in patches],
    "mathematical_proof_edits":False,"leaf_editorial_maps":leaf_maps
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Publication source generated; exact editorial inverse passed.")
