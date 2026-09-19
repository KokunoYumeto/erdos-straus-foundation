# Explicit maps: Turn 6

All maps below retain p and the shell a unless a different domain is stated.
G means the full unit group modulo R=4a-p, not a convenient cyclic replacement.
The chosen observation subgroup B contains -1; it is **not** assumed to be the
actual stabilizer or a saturated part of the available source.

## M01 — Original centered box to square divisors
Domain: beta_l in [-e_l,e_l] for a=product l^e_l. Codomain: u|a^2.
Map u=product l^(e_l+beta_l). Inverse beta_l=v_l(u)-e_l. Fibres singleton.

## M02 — Divisor normalization
u -> d=gcd(a,u), (h,r,s)=(d^2/u,u/d,a/d).
Inverse a=hrs, u=hr^2 with gcd(r,s)=1. All prime valuations retained.

## M03 — E return
R | pr+s, kappa=(pr+s)/R.
Ordered denominators (a,hs*kappa,p*h*r*kappa).
Inverse u=a^2/(Ry-pa), then M02. Canonical p-divisible coordinate stays last.

## M04 — M return
R | r+s, lambda=(r+s)/R.
Ordered denominators (a,p*h*s*lambda,p*h*r*lambda).
Inverse u=p*a^2/(Ry-pa), then M02. Reversal is u -> a^2/u, r <-> s.

## M05 — p-coloured divisor words
(epsilon,v) -> p^epsilon v, epsilon=0,1 and v|a.
Inverse epsilon=v_p(d), v=d/p^epsilon. Because a<p, these are all divisors of pa.
There are 2*tau_div(a) words, counted once each.

## M06 — Residue observation and kernel
Free Z-module on M05 -> Z^G, e_d -> e_(d mod R).
Kernel: same-fibre differences e_d-e_(least fibre word).
An inverse correspondence retains each fibre sum and all nonselected coordinates;
the selected coordinate is sum minus those coordinates. No injective quotient claimed.
The sparse support is the actual set of nonempty original fibres.

## M07 — Original pair to primitive channel
Domain: b,c|pa and R|b+c. Divide by their gcd.
Equal p-valuations give M, retaining the common p-bit; unequal valuations give E,
retaining the side containing p. Read coprime r,s and h=a/(rs).
Full fibres have 2*tau_div(h) members, as in the preserved Turn 5 theorem.

## M08 — Full pair fibres
M: (p^epsilon d r,p^epsilon d s), d|h, epsilon=0,1.
E: (p d r,d s) or (d s,p d r), d|h.
These formulas invert M07 and preserve both channel labels even if target residues coincide.
Weight 1/(2*tau_div(h)) on each original pair returns one canonical state.

## M09 — Swap
S(b,c)=(c,b), involutive on original target pairs. No fixed point (R does not divide 2b).
For M this reverses r,s; for E it changes the recorded p-side.

## M10 — Original divisor complementation
I(b,c)=(pa/b,pa/c). It commutes with S and has no fixed pair.
In M it sends (r,s,d,epsilon) to (s,r,h/d,1-epsilon).
In E it changes side and sends d to h/d. SI cannot fix a pair, because that
would make -1 a square modulo R. All original target orbits have size four.

## M11 — Scalar principal projection
On the declared Euclidean residue coefficient space, c -> constant m/phi(R).
Kernel: zero-total vectors. The exact squared projection norm is P=m^2/phi(R).
No inverse without retaining the zero-total vector. The target form is <c,J_-c>,
not the positive norm <c,c>.

## M12 — Negation target operator
J_-c(g)=c(-g), a self-adjoint isometric involution on residue coordinates.
It has both + and - eigenspaces. Replacing it by identity calculates collision
energy, not the ES target. Signed Fourier coefficients and their exact normalization
are in the proof.

## M13 — Coset pushforward
Z^G -> Z^(G/B), c -> m_C=sum_(g in C)c_g.
Kernel: within-coset differences. Retaining differences gives the full integer
inverse correspondence. Coarse membership is not fine target membership.

## M14 — Coset-constant section and projector
Over Q, j_B(m)_g=m_C/|B|; Q_B=j_B*pi_B is orthogonal for the explicitly declared
Euclidean residue metric. pi_B*j_B=identity; Q_B^2=Q_B.
Original c = Q_B c + (c-Q_B c), with every remainder coordinate retained.
Since -1 is in B, J_-Q_B=Q_B. The residual signed contribution is retained exactly
or bounded below by its negative squared norm. This is the source of the real bound.

## M15 — Original metric versus observation metric
M06 sends the word Euclidean metric to a quotient metric whose squared norm is
sum y_g^2/c_a(g) on occupied fibres. Its least-norm section assigns y_g/c_a(g)
to each word in that fibre. It is not the unweighted residue metric of M11/M14.
The collision energy sum c_a(g)^2 is a declared integer statistic, not an
isometry claim about the word module.

## M16 — Antipodal pair coordinates
In each B-coset choose unordered pairs {g,-g}. Set z=c(g)+c(-g),
delta=c(g)-c(-g). Inverse (c(g),c(-g))=((z+delta)/2,(z-delta)/2).
The full integer image has z>=|delta|, z=delta mod2. Dropping delta loses the
fine coordinates. T+D=sum z^2. Integer balancing of z at its retained total
proves the lower bound; it does not presume an actual balanced original source.

## M17 — Complement on cosets and antipodal pairs
P=pa mod R=(2a)^2. g -> P/g sends C -> P C^-1, involutively.
The actual coefficient obeys c(g)=c(P/g). A fixed residue g^2=P has even count,
from the free original complementation d -> pa/d. g^2=-P has no solution.
Self-complementary cosets split into r two-pair orbits and f fixed pairs,
2r+f=|B|/2. Their half-mass has exact convex minimum stated in core.tex.

## M18 — Discrete convex inverse
For a specified half-mass M and r,f, select M smallest labelled increments from
r lists 2,6,10,... and f lists 4,12,20,... . Prefix counts give the minimizing
integer coordinates. The selected labels and deterministic tie order are retained.
A separate DP verifies this calculation in the examples. This is an inverse
of the finite minimization, not a manufactured original divisor factorization.

## M19 — Certificate to original witness
When the explicit integer lower bound is positive, scan the finite original
residue buckets for a bucket and its negative. The inequality proves termination
within the complete word list; choose their least words and apply M07 then M03/M04.
The resulting state retains the selected subgroup, bounds, input pair and all
normalization coordinates. No universal positivity premise is inserted.

## M20 — Complete shell assembly
Direct sum over EVERY a in (p/4,p/2), not a graph, chamber, ray family or dyadic
subrange. T_a>0 iff a labelled original state occurs. Exact state counting uses
M07 fibre weights or the inherited Möbius transform; the positive pair sum alone
suffices for existence. Shell reweighting in the negative theorem has its stated
positive lower/upper bounds; arbitrary zero weights are not hidden in it.

## M21 — A proper selected even spectrum
For a conjugate-closed set Sigma of even characters, project the declared real
residue space orthogonally onto those Fourier modes (unitary normalization
1/sqrt(phi(R))). The exact inverse correspondence retains every omitted Fourier
coordinate. J_- is identity on the selected image, and the exact remaining signed
form gives T >= 2 E_Sigma - E. Sigma need not be a subgroup of characters.
The image of a five-mode projector at R47 is proper inside the23 even modes,
even though no intermediate observation subgroup exists. No favourable sign of
the omitted contribution is assumed.

## M22 — Original spectral evaluation and rigorous enclosures
At R47 the full discrete log is base5 modulo46. The even character reads that
log modulo23. Retain the full log, original divisor, p-bit and exponent source;
that readout is inverted by the full log, not the reduced one. The character is
chi(5)=zeta23 and conjugation sends j to -j. Exact rational Taylor intervals
certify the selected squared norms; the second implementation uses a different
arctangent identity and term count. An interval is an enclosure, not equality of
the enclosed algebraic number with an endpoint.

## M23 — Laurent norm observation
C(X) -> C(X) C(X^-1) modulo X23-1 gives all squared character values on evaluation.
It is not injective: a cyclic translation of C leaves the Laurent norm unchanged.
The certificate therefore retains C, all original divisor words, and their full
logs. Q0=collision_energy+target_count is a separately checked identity, not an
assumed value used to create the original source or a missing witness.

## M24. Explicit divisor-power constant

Input m>=3. For every prime q<2^m, retain the complete maximizing exponent
set in 0<=e<2m (the certificate selects its least member) and exact rational
maximum. Multiply them to K_m and take the least integer C_m with C_m^m>=K_m.
This is a scalar bound observation, not an invertible map of integers a. Its
use is the proved tau_div(a)<=C_m*a^(1/m) with a, its factorization and every
original divisor still retained. No factor inventory or probability is supplied.
