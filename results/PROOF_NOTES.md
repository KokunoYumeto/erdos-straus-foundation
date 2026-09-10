# Selected proof notes

These arguments were reconstructed in the 10 September 2026 editorial pass. See [SOURCES.md](SOURCES.md), [the result records](records.json) and [the exact checker](check_selected.py). No formal prover, independent reviewer or comprehensive novelty search is claimed. The imported Kneser theorem is identified explicitly.

## R01

**Adjoining an absent zero to a ring.** Let R be a nonzero commutative ring with identity. Set S=R⊔{τ}, with τ new. Use the original ring operations on R and define τ+a=a+τ=a and τa=aτ=τ for every a∈S. Then S is a commutative semiring: τ is its additive identity and multiplicative annihilator, 1_R is its multiplicative identity, and 0_R remains a distinct supported zero. The ideal {τ} is prime; {τ,0_R} is prime exactly when R is an integral domain.

**Proof.** Ring-element associativity and commutativity are inherited. Removing occurrences of τ from a sum verifies additive associativity; a product involving τ equals τ. Distributivity is the ring law when all arguments lie in R. When the multiplier is τ both sides are τ; when a summand is τ both sides reduce to the other product. Identity laws are immediate. Notice a+(−a)=0_R, not τ: this additive monoid is not the additive group of R.

Both displayed ideals contain τ, are closed under sums and absorb multiplication by S. Their complements are R and R\{0_R}. Products of ring elements always stay in R, whereas nonzero ring elements are multiplicatively closed exactly when there are no zero divisors. This proves primality using the proper-ideal/multiplicatively-closed-complement definition. It does not assert that these are the only prime ideals.

**Source and limit.** Recovered Star–Kneser source CN-cd08053554f277, lines 484–539, and the owner's split-zero programme. No novelty or arithmetic-occupancy claim.

## R02

**All six Fourier components of the weighted defect.** In C[C₆], put δ_k=e₃+2e₍₃₋ₖ₎, with indices modulo 6. Every Fourier component is nonzero, the six cyclic translates are a basis, and the trivial-character value is 3.

**Proof.** With ζ=exp(2πi/6), evaluation at character m gives ζ^(3m)(1+2ζ^(−km)). The first factor is nonzero. The second cannot vanish because ζ^(−km) has absolute value 1, whereas −1/2 has absolute value 1/2. The Fourier transform diagonalizes the translation matrix with these six nonzero eigenvalues; thus it is invertible. At m=0 the value is 3.

**Source and limit.** CN-cd08053554f277, lines 396–482. The retained trivial sector and coefficient 2 matter. Target invertibility does not force another arithmetic measure to have a positive coefficient at the target.

## R03

**Fifteen-to-sixteen finite coordinate algebras.** Let P={2,3,5,7,11,13,17,19,23,29,31,41,47,59,71}. Its residues modulo 5 have fibres {5}, {11,31,41,71}, {2,7,17,47}, {3,13,23}, {19,29,59} at residues 0,1,2,3,4. Combining opposite nonzero residues gives sizes 1,7,7. Adjoining a distinct level-one coordinate and retaining it separately gives 1,1,7,7.

For any field F, pullback along any displayed surjection is an injective unital algebra map from the target coordinate algebra into F^P, or F^(P⊔{1}).

**Proof.** Division by 5 verifies the fibres; they exhaust fifteen distinct elements. Opposite residue pairs have sizes 4+3 and 4+3. The extra label differs from every prime. Pullback is f↦f∘π and preserves operations pointwise. Surjectivity of π implies injectivity of pullback. The characteristic function of the extra label is an idempotent whose product with every prime-coordinate idempotent is zero.

**Source and limit.** CN-e88f271329664e, lines 1441–1743. This proves finite-set/algebra facts. It does not prove a genus-zero classification, Monster action or Lie-algebra identification.

## R04

**The fixed Busy-Beaver/107 arithmetic.** Put p=8,803,369, R=107, a=(p+R)/4=2,200,869, b₂=6, b₃=21 and b₅=47,176,870. Modulo 107:

p=b₃⁻¹=51; b₅=pa=35; b₃b₅=a=93; −b₃b₅=11²=14; (−b₂b₅)⁻¹=27.

**Proof.** We have p=107·82,274+51, a=107·20,568+93, and b₅=107·440,905+35. Then 21·51=1071≡1, 51·93=4743≡35, 21·35=735≡93, and −93≡14≡121. Finally −6·35=−210≡4 and 4·27=108≡1. Also p+107 is divisible by 4, as required.

**Source and limit.** CN-7bae3791cc8514 and CN-56a02a22fb3296. The Busy Beaver interpretation is cited separately; this proof neither establishes maximal runtimes nor a general complexity identity or machine-to-ES construction.

## R05

**Affine towers and an odd Collatz step.** Let T(n)=4n+1 and θ(n)=3n+1. Then θT=4θ and T^j(n)=4^j n+(4^j−1)/3. Modulo M this is a conjugacy to multiplication by 4 when gcd(3,M)=1, and otherwise a semiconjugacy onto the image of θ.

For positive odd n define U(n)=(3n+1)/2^v₂(3n+1). Then U(T^j(n))=U(n) for every j≥0.

**Proof.** Expansion gives 3(4n+1)+1=4(3n+1). Iterating gives 3T^j(n)+1=4^j(3n+1), hence the formula. Its quotient is integral because 4^j≡1 modulo 3. Modulo M, θ is bijective precisely when multiplication by 3 is invertible. Over Z its image is only 1+3Z, not all Z.

T preserves positive odd integers. The iterated identity increases the 2-adic valuation of 3n+1 by exactly 2j without changing its odd part. This proves the U identity.

**Source and limit.** CN-6fe2d9040d950e, lines 1632–1757, explicitly credits CivQ17's affine/residue diagrams. The U formulation is an added derivation in this pass, not a retroactive attribution or novelty claim. It gives common next-odd-value fibres, not convergence of Collatz.

## R06

**The deficit progression and two translates.** In C₅₃ let A={35r+11s+33t:−2≤r,s≤2,−1≤t≤1}. Its complement is D={23+42j:0≤j≤9}. Then |A|=43, |D|=10, |D−D|=19, 6∉D−D, and (A+29)∪(A+23)=C₅₃.

**Proof.** Exact reduction of the 75 bounded triples yields complement {1,10,12,21,23,30,32,41,43,52}. The checker supplies an exhaustive computation, not a probabilistic sample. Adding 42 repeatedly to 23 gives 23,12,1,43,32,21,10,52,41,30, the same set.

Every difference is 42k for −9≤k≤9, and every such index occurs. These nineteen values are distinct because 42 is invertible modulo 53 and index differences have absolute value at most 18. Its inverse is 24; 6·24≡38 has no representative in [−9,9], so 6 is not a difference. If D+29 met D+23, then 6 would belong to D−D. Disjoint complements imply the displayed union of A translates is the whole group.

**Source and limit.** The observation is credited to u/CommonCareful3149. The pinned public mod-107 workbench provides the logarithmic interpretation; this reconstruction is not the contributor's missing note. It is one finite support calculation, not universal ES coverage.

## R07

**Sharp irrational-direction constant.** Let v be (1,1−√2) or (√2−1,1), and c=√(4+2√2). For every nonzero k∈Z², |v·k|>1/(c‖k‖), and inf |v·k|‖k‖=1/c.

**Proof.** Pair the first v with w=(1,1+√2) and the second with w=(−1−√2,1). They are perpendicular with ‖w‖=c and ‖v‖=d=√(4−2√2). For k=(m,n), (v·k)(w·k) equals (m+n)²−2n² or (n−m)²−2m². This is a nonzero integer for k≠0, by irrationality of √2. Its absolute value is at least 1. Cauchy–Schwarz gives |w·k|<c‖k‖, strictly because a nonzero integer vector cannot have the irrational slope of w. The strict lower bound follows.

Set p₀=1,q₀=0 and pⱼ₊₁=pⱼ+2qⱼ, qⱼ₊₁=pⱼ+qⱼ. With α=1+√2, β=1−√2=−α⁻¹, induction gives pⱼ+qⱼ√2=αʲ and pⱼ−qⱼ√2=βʲ. For j≥1 use kⱼ=(pⱼ−qⱼ,qⱼ) in the first direction and (qⱼ,qⱼ−pⱼ) in the second. The v and w symbols are βʲ,αʲ or their negatives. Orthogonality gives ‖kⱼ‖²=α²ʲ/c²+α⁻²ʲ/d². Thus |v·kⱼ|²‖kⱼ‖²=1/c²+α⁻⁴ʲ/d²→1/c², proving optimality.

**Source and limit.** The pinned public reverse_smooth_inverse.tex supplies this theorem. It needs no PDE existence result; no stronger analytic statements or complete fluid proof are certified here.

## R08

**Three colours: fixed and zero-sum lattice parts.** Let Λ be a positive-definite integral lattice of rank d, Gram matrix G and minimum squared length m. In L=Λ³ use the direct-sum metric and P(x,y,z)=(z,x,y). The fixed lattice is D={(x,x,x)} with Gram matrix 3G. The zero-sum lattice K has Gram matrix [[2G,−G],[−G,2G]]. D⊥K, [L:D⊕K]=3^d, and the minima of L and K are m and 2m. On K, P²+P+I=0 and P defines an Eisenstein-integer action.

**Proof.** Fixed and zero-sum conditions immediately give D and orthogonality. For a basis eᵢ of Λ set gᵢ=(eᵢ,−eᵢ,0), Pgᵢ=(0,eᵢ,−eᵢ). Any zero-sum triple (x,y,z) has unique expression x·g−z·Pg in basis coordinates. Inner products give the stated matrix. The sum map L→Λ has kernel K and takes D to 3Λ, so L/(D+K)≅Λ/3Λ, proving the index. The real splitting by division by 3 is not generally integral.

A nonzero triple has a nonzero coordinate, proving minimum m in L, attained by (x,0,0). A nonzero zero-sum triple has at least two nonzero coordinates, giving minimum at least 2m, attained by (x,−x,0). On K, I+P+P² sends a triple to its sum in each coordinate, hence zero. Letting ω act as P gives a Z[ω]-module; the displayed basis identifies it as free of rank d.

For a rank-24 Leech input with minimum squared length 4, L has rank 72 and minimum 4; K has rank 48 and minimum 8. This is not Nebe's extremal rank-72 minimum-8 lattice.

**Source and limit.** This is a new explicit test of one interpretation of the owner's colour proposal. It is not recovered old work, a novel lattice claim or an ES morphism. The glue order 72 in R10 is a different invariant.

## R09

**A miss supplies a Star–Kneser obstruction.** Let H be finite abelian, A₁,…,Aₛ nonempty subsets, B their sumset and T a nonempty target. For K≤H put aᵢ(K)=|(Aᵢ+K)/K|, t(K)=|(T+K)/K| and Σ(K)=1+Σᵢ(aᵢ(K)−1)+t(K)−|H/K|. If B∩T is empty, then Σ(K)≤0 for K=Stab(B). Consequently positivity for every subgroup implies a hit.

**Proof.** The imported finite Kneser addition theorem gives |B/K|≥1+Σᵢ(aᵢ(K)−1) for the actual stabilizer. If one coset met both B and T, its T point would lie in B because B+K=B. Hence a miss makes the quotient images disjoint; their sizes sum to at most |H/K|. Combining the inequalities yields Σ(K)≤0. The forcing assertion is its contrapositive. The many-set form follows by induction from the two-set theorem: any partial-sum stabilizer in the final quotient stabilizes the final sum, so the relevant quotient partial sums are aperiodic.

**Source and limit.** CN-cd08053554f277, lines 566–694. External input: Matt DeVos, A short proof of Kneser's addition theorem for abelian groups, arXiv:1303.3539. This does not establish the positive-surplus hypotheses for every ES input.

## R10

**Finite order-72 glue.** Label four coordinates by Q=F₂², represented by 0,1,2,3 under XOR. Let C₂ contain each even-weight binary word u together with the XOR y of its occupied labels. Let C₃ be the F₃-span of (1,1,1,0) and (1,2,0,1). Set H={(3u+2v,y):(u,y)∈C₂,v∈C₃} in (Z/6Z)⁴×Q. It is a subgroup of order 72. For q(k,y)=Σᵢ5kᵢ²/6+1[y≠0] modulo 2Z, q(H)=0. The cost Σᵢkᵢ(6−kᵢ)/6+1[y≠0], with 0≤kᵢ≤5, occurs once at 0, 46 times at 4 and 25 times at 6.

**Proof.** The even binary words form a vector space of order 8 and y is linear. The two ternary generators are independent, giving 9 words. Reduction modulo 2 of 3u+2v recovers u; reduction modulo 3 recovers −v. Thus the map is injective and a homomorphism on its primary parts, giving a subgroup of order 72.

The cross term in q is even. The binary contribution is 3·wt(u)/2+1[y≠0] modulo 2: respectively 0,6,4 for the empty word, all-one word and a duad. Every nonzero ternary word has weight 3 by evaluation of its eight nonzero coefficient pairs; its contribution is −2·wt(v)/3, also even. Hence q is zero. Evaluation of the stated cost on the full eight-by-nine list gives the claimed multiplicities. The exact Fraction-based checker enumerates all 72 values and all 5,184 ordered products, so this finite verification is exhaustive for the displayed objects.

**Source and limit.** CN-679a329c81c154, lines 703–739. Interpreting these data as an even unimodular overlattice also uses the root-lattice discriminant forms and standard overlattice correspondence. Later ES/modular/Leech implications do not follow just from this finite computation.
