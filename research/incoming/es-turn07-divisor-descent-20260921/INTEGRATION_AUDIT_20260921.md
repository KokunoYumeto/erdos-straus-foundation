# Integration audit — original-divisor descent

Date: 21 September 2026

## Determination

The supplied divisor-descent continuation contains a valid exact descent
theorem after the repairs recorded below. Its domain is a rational E- or
M-channel trace source

\[
(p,a,R,u,c),\qquad R=4a-p,\qquad u\mid a^2,
\]

whose integer tail trace is characterized by \(R\mid G_c^2\), where
\(G_E=4u+1\) and \(G_M=p+4u\). The same-word residual-divisor arrows are
exactly

\[
k\in\mathbb Z_{>0},\qquad k\mid R,\qquad
\frac{R}{\gcd(R,G_c)}\mid k,\qquad k\equiv1\pmod{4K(u)}.
\]

The induced map, its full inverse fibres, its free-abelian kernel, the square
subdomain, the exact nine-word universal class, the integer multiplicity
coefficients, and the CRT/Dirichlet optimality family have each been
rederived independently. The result is an exact theorem about this descent
system. It is not a proof of the Erdős–Straus conjecture and it does not claim
that a trace source exists for every prime.

## Received objects

The received objects are preserved without editing in `received/`.

| Object | Bytes | SHA-256 |
|---|---:|---|
| `ES_Turns6_7_With_Divisor_Descent_20260921.zip` | 13,958,871 | `8e3527bbecb8658021d10f94b49ac98ee202bbca755b5bfb8c750b61606b6481` |
| `USER_HANDOFF.txt` | 19,728 | `dc7dd85522146baece1e7b0063adec106604cd4675068e4f3b12aa41d3133e3c` |
| preserved trace-rigidity archive | — | `e491bee481c629bb1ad2d0c1101261369ee0464fafc6440dc42163431f52fbbd` |
| preserved prime-shell trace archive | — | `1603ba6de57e72169186af3e4026f83a7f7183419cc86e6afa01687c77e9e948` |
| current inner divisor-descent archive | — | `d5973df91e35d50edb5830a3ae3191358ada49ee8b37184fddf660d6769ec57f` |

Every archive member passed resolved-path containment checks before
extraction. Received sources remain distinct from the repaired integration
edition.

## Proof repairs

The integration edition makes the following mathematical repairs.

1. The deletion parameters \(k\) and \(q\) are positive integers. This removes
   negative divisors that satisfy the congruence but give a negative residual.
2. The rational-tail converse now proves integrality without presupposing an
   E/M channel: the two auxiliary rationals are roots of a monic polynomial in
   \(\mathbb Z[X]\), hence are integers, after which their three possible
   \(p\)-valuation pairs recover the E/M classification.
3. The trace denominator proof retains every valuation. For
   \(\ell^e\parallel R\) and \(g=v_\ell(G_c)\),
   \(v_\ell(d)=\max(e-g,0)\) and \(e\le2g\), so \(d^2\mid R\).
4. The inverse-fibre theorem now begins with every target condition:
   \(R'=4a'-p\), \(3\le R'<p\), \(R'\equiv3\pmod4\),
   \(u\mid(a')^2\), and \(R'\mid G_c\).
5. The global map is typed on decorated arrows \((s,k)\), not on source
   records. Same-target arrow differences generate the kernel; a chosen arrow
   in each fibre gives a right inverse, and retaining the kernel coordinate
   gives the two-sided direct-sum isomorphism.
6. Group-ring basis elements and coefficient extraction are distinct. The
   labelled divisor module is retained before its residue pushforward, so
   equal residue classes do not erase multiplicity.
7. The middle-complement identity
   \[
   4u(p+4u^*)\equiv p(p+4u)\pmod R
   \]
   is included. It proves exact denominator preservation for the M complement.
8. Strict complement descent is not asserted for arbitrary E complements. At
   \((p,a,R,u,c)=(37,16,27,2,E)\), the complement \(u^*=128\) is already
   integral and admits only \(k=1\).
9. The mixed fixture has one retained word \(u=5\) and two arrows
   \(k=21,441\); channel tuples are labelled rather than asserted to increase
   numerically.
10. The optimality family proves reducedness of every CRT class, retains the
    exact complement denominator, and gives explicit E and M endpoint states.
    Those endpoints prove the constructed primes are not ES counterexamples.

## Independent proof sources

- [Exact trace, arrow and fibre derivation](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/DIVISOR_DESCENT_EQUIVALENCE.md#L28-L332)
- [Exact nine-word classification](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/NINE_WORD_CLASSIFICATION.md#L62-L261)
- [CRT/Dirichlet optimality derivation](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/OPTIMALITY_PROGRESSION.md#L20-L237)
- [Independent bounded challenge](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/1400e6301429cf9c66d8071e107be9dc41f5b907/research/incoming/es-turn07-divisor-descent-20260921/independent_audits/NINE_WORD_BRUTEFORCE.md#L47-L177)

The inherited Type-I/II coordinates are cited to Elsholtz and Tao,
[Propositions 2.2 and 2.6](https://arxiv.org/pdf/1107.1010#page=12).
The only analytic input in the optimality family is Dirichlet's theorem after
reducedness is proved; the cited source is Sutherland,
[Theorem 18.1](https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf#page=1).

## Reproducible execution

The main verifier and the separately implemented checker run in ordinary and
optimized Python modes. The release runner requires byte-identical
mathematical JSON across modes and fails on any disagreement.

- Main checks per mode: `428449`.
- Independent checks per mode: `4084626`.
- Enumerated primes: all primes \(p\equiv1\pmod4\) through \(3000\).
- Shells: `73798`.
- Original divisor vectors: `1877004`.
- Proper trace sources: `5274`.
- Returned proper-source arrows: `1864`.
- Hit targets: `1457`.
- Integral sources with a nonidentity return: `289`.
- Integral-source return arrows: `11356`.

The main mathematical JSON hashes are:

| File | SHA-256 |
|---|---|
| `abstract.json` | `d465e027df7e24549212b8017941faba8ec4916b82c33021cce2e74c04352427` |
| `examples.json` | `7266952d1874a2b1ab03704cdc74afeb3ceb8ca4bf2f9f5ed991b29f6b1c402c` |
| `progressions.json` | `25c2cd34eaf6cdaa68d1d5241593205879e189a9dac822213159173574f2cd54` |
| `scan.json` | `c957f58958991788ffed844d7930f124791dcd4259d9aa20bf9c4910a520523b` |
| `sources.json` | `fd316854a7e7f561bb29046453dd67168bc89840833171d059628d8bcbf8606c` |

The final release receipt is `results/REPLAY.json`.

## Reader and figure verification

Both TeX readers are compiled twice. Every page is rendered and visually
inspected after the final source change. The exact source map and the nine-word
boundary figures are generated from `figures/make_divisor_descent_figures.py`,
which recomputes every displayed coordinate before drawing it.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `preprint.pdf` | 3 | `23e419c5614feece4a25798ab35fa3f5c9306401ab1c63c114f9f2dd23beefdb` |
| `workbench.pdf` | 10 | `936ffc210563ed3e62215f303c33004c995996bc75feae5ca560515a3762146c` |

## Nonclaims

- No universal trace-source occupancy theorem is claimed.
- No universal Erdős–Straus theorem or counterexample is claimed.
- Failure of the residual-divisor predicate does not imply failure of every
  other construction; the optimality family includes explicit occupied
  endpoint states.
- A word outside the nine-word class may return at a particular source. The
  theorem says exactly that no universal fixed-word guarantee survives there.
- No Lean build is claimed for this tranche.
- No historical-priority or novelty determination is made.
