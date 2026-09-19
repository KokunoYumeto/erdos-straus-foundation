# Turn 2: the full shifted-factor system and its closed failures

The Clankers — 18 September 2026. Research continuation, not a proof or disproof of Erdős–Straus.

## Result

The basic nonresidue-prime factor graph is inherited from Chase Bryan's workbench. This contribution attaches the entire original exterior/middle selector to every vertex, including composite residuals and distinguished denominators above p/2, and retains every eligible factor edge and its multiplicity. It proves the exact all-type transition formulas, the complete common-divisor transport domain, a terminating decision theorem for closed failed components, and an integer inverse for a cycle's ordered coefficient data.

The proposed assertion that every canonical closed component contains a local hit is **false**. At p=2521 the seven-cycle

`11 -> 211 -> 683 -> 89 -> 17 -> 643 -> 113 -> 11`

is a genuine sink component of the full graph. Each displayed outgoing factor is the only eligible one and both local gates are empty. The original prime nevertheless has ES solutions at other graph vertices. At p=3361 a primitive effective-index-six vertex also lies on a closed failed cycle. The component of the known p=808369 consecutive-sextic example is completed and checked as a separate six-cycle.

## Read

- `workbench.pdf`, from `workbench.tex` and `core.tex`: complete eight-page proof, with full seven-cycle supports.
- `preprint.pdf`, from `preprint.tex`: self-contained three-page result and its exact small certificate.
- `MORPHISMS.md` / `.json`: domains, inverse fibres, exceptions and information loss.
- `ATTEMPTS.md`: the graph-closure route, its exact counterexample, and why the
  programme changes direction after this turn.
- `HANDOFF_TURN_3.md`: precise change required at the next route-selection gate.
- `source_reading.json`: pinned antecedents and actual reading scope. No full-corpus rereading is claimed.

The distinction between a supported zero and absence is retained at each original word source. No residue-group homomorphism between two different moduli is inferred from a factor edge.

## Reproduce (Python 3.10 or later; standard library only)

```sh
python verify.py --bound 50000 --out certificates
python -O verify.py --bound 50000 --out certificates_optimized
python check_independent.py --input certificates --out certificates/independent.json
python verify_traps.py --input certificates/traps.json --out certificates/trap_check.json
```

`verify.py` uses exact modular arithmetic and complete bounded divisors. Its minimum scan bound is 2521 because the least-hard-prime trap assertion is included. `check_independent.py` imports neither verifier nor predecessor code: it builds characters by the set of squares, tests the rational denominator reconstruction, and uses a different SCC and reachability implementation. `verify_traps.py` is a small standalone checker of only the three displayed closed components and genuine ES returns. It does **not** certify the leastness claim or the large prime scan.

```sh
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error workbench.tex
pdflatex -halt-on-error preprint.tex
pdflatex -halt-on-error preprint.tex
```

## Executed scope

The source-hashed full run has 137 hard-class primes through 50,000, 188,255 vertices, 191,789 distinct edges and 193,997 edge occurrences. There are 8,357,211 original divisor candidates, 1,729 exterior states and 2,728 middle states. The 57,416 auxiliary vertices above p/2 contain ten exterior states; each has an explicit first-half recoding. Thirty-nine primes in this finite scan have a canonical failure trap, and eight least-nonresidue starts are trapped. Every prime in this finite scan has some graph hit; no global conclusion is drawn.

The main checker executed 4,032,500 explicit checks, including eight deliberately false transformations that were rejected. The separate scan checker executed 393,203 checks. The small closed-component checker executed 696 checks. Both Python modes produce byte-identical mathematical JSON. These are implementation tests, not independent mathematical review or new ES coverage.

All original factor-cut inequalities from Turn 1 are checked at every graph vertex for hard p<=5000, not at all vertices through 50,000. Full detailed graph records are provided for p=1201,2521,3361,5569. For p=808369 only the seven listed nodes and its six-cycle are checked. Abstract graph tests exhaust 38,636 loop-free, nonempty-outdegree graph/hit-mask configurations on two through four vertices.

## Publication and nonclaims

The package includes a local source-only Git record and additive patch. Its publication receipt states whether a remote PR actually exists. A local record is not an upstream clone or a remote publication. The sealed Turn 1 archive is included unchanged; its presence is not a replay of all its historical checks.

No historical-priority determination, universal ES proof or counterexample, all-prime graph-occupancy theorem, Lean build, analytic theta-norm identification or independent mathematical review is claimed.
