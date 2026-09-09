# Independent review of the successor extensions

Result: no mathematical error found in the final frozen source.
The written statements labelled thm:no-two-shears, prop:affine-point,
and thm:full-connes-shear, together with the explicit /(J/)-conjugation
paragraph and the /(p=1753/) example, were read directly in
bounded_transport.tex. They correctly prove the directed-matching
assertion, affine zero fibre and positivity domain, full /(L/)-return,
failure of uncorrected reciprocal return for /(c>0/), and the distinct
/(J/)-conjugation with its exact domain and inverse. The earlier
orientation clarification is resolved in this final source.

This review modifies neither the manuscript nor the earlier successor
review. The associated JSON retains the exact computation ranges and
source/block hashes for this extension.

## All four possible two-edge types

Keep the fixed prime /(p=12h+1/), original shell interval /(A_p/), and
the fully labelled vertices /((a,m,n)/), with /((m,n)/in/mathcal W_a/).
The existing full shear classification gives:

/[
L:/ (a,m,1)/longmapsto(a+1,m+1,1),
/qquad
J:/ (a,1,n)/longmapsto(a+1,1,n+1).
/]

An /(L/)-edge followed by a /(J/)-edge would require /(m+1=1/), which
contradicts /(m>0/). A /(J/)-edge followed by an /(L/)-edge would require
/(n+1=1/), contradicting /(n>0/).

Suppose two consecutive /(L/)-edges exist. Their three vertices are
/((a+i,m+i,1)/), /(i=0,1,2/). Set

/[
R=4a-p,/qquad K=a-m.
/]

All three vertices satisfy the exact divisor and residual conditions

/[
m+i/mid a+i,/qquad R+4i/mid m+i+1/quad(i=0,1,2).
/]

The divisor conditions imply /(m+i/mid K/). One of the three positive
integers /(m,m+1,m+2/) is divisible by /(3/), hence /(3/mid K/).
This remains valid when /(K=0/); no division by /(K/) is used.
The residual conditions imply, for every /(i/),

/[
R+4i/mid 4(m+i+1)-(R+4i)
=4(m+1)-R=:C.
/]

One of /(R,R+4,R+8/) is divisible by /(3/), since their increments are
/(1/) modulo /(3/). Consequently /(3/mid C/). But

/[
C=4m+4-(4a-p)=p+4-4K/equiv1+1-0=2/pmod3.
/]

This is a contradiction. Coordinate exchange
/(P(m,n)=(n,m)/) preserves the shell label, divisor supplies, positivity,
primitivity and residual sum, and satisfies /(J=PLP/). It therefore
excludes two /(J/)-edges. Every possible two-edge word has been covered.
The obstruction does not require any assumed positivity for /(C/) or
any unproved prime-producing property of a parameter family.

There is also a precise stronger graph consequence. A vertex cannot have
both kinds of outgoing edge: that would force /(m=n=1/), whose sum /(2/)
fails the residual condition /(R_a/ge3/). For an incoming /(L/)-edge at
coordinates /((x,y)/), its positive predecessor is /((x-y,y)/), so
/(x>y/). For an incoming /(J/)-edge the predecessor is /((x,y-x)/), so
/(y>x/). Thus both incoming kinds cannot occur; within either kind the
inverse is unique. Combining indegree and outdegree at most one with
the absence of a length-two path shows that every component is an
isolated vertex or a single directed edge. This directed-matching
conclusion concerns exactly the adjacent elementary /(L/J/) graph.

## Full affine lattice map and exact finite returns

For /(N,M>0/), /(c/in/mathbb Z/), and
/(H_N=(1/N)/mathbb Z/), the map

/[
/Psi_{N,M,c}(x)=/frac NMx-/frac cM
/]

acts on every integer index by

/[
/frac{k}{N}/longmapsto/frac{k-c}{M}.
/]

It is therefore a bijection of the entire underlying lattice sets, with
inverse

/[
/Psi_{M,N,-c}(y)=/frac MN y+/frac cN.
/]

For a target /(j/M/), its fibre is the singleton
/(/{(j+c)/N/}/). The zero fibre is /(/{c/N/}/). For /(c/ne0/),
the map is not an additive homomorphism because
/(/Psi_{N,M,c}(0)=-c/M/ne0/); the term homomorphism kernel must not be
used for that zero fibre. Its linear part has trivial kernel.
The coefficient /(N/M>0/) makes the map order preserving, but it need
not send positive elements to positive elements. For example /(c=1/)
sends /(1/N>0/) to zero. The manuscript correctly calls the map affine
and disclaims additivity for nonzero /(c/).
Its stated positive-image domain is exactly
/(/{x/in H_N:Nx>c/}/), because
/(/Psi_{N,M,c}(x)=(Nx-c)/M/) and /(M>0/).

For /(u/mid N/), put /(e=N/u/), so /(e/in/operatorname{Div}(N)/).
Then

/[
/Psi_{N,M,c}(1/u)=/frac{e-c}{M}.
/]

It equals /(1/v/) for a positive integer /(v/) exactly when

/[
e>c,/qquad e-c/mid M.
/]

In that case /(v=M/(e-c)/mid M/). The full positive return domain,
including both prime-exponent budgets, is therefore

/[
e/in/operatorname{Div}(N)/cap
       /bigl(c+/operatorname{Div}(M)/bigr).
/]

The inverse divisor formula is

/[
v/longmapsto
/frac{N}{M/v+c},
/quad v/mid M,/quad M/v+c>0,/quad M/v+c/mid N.
/]

The sign condition covers arbitrary negative as well as positive /(c/).
When /(e=c/), the image is zero and is correctly excluded; when /(e<c/),
it is negative and is correctly excluded.

For a third budget /(T>0/) and /(d/in/mathbb Z/), direct substitution gives

/[
/Psi_{M,T,d}/circ/Psi_{N,M,c}
=/Psi_{N,T,c+d}.
/]

The complete domain for two consecutive positive reciprocal returns is

/[
/operatorname{Div}(N)/cap
/bigl(c+/operatorname{Div}(M)/bigr)/cap
/bigl(c+d+/operatorname{Div}(T)/bigr).
/]

The middle intersection cannot be dropped merely because the composite
formula is defined on all of /(H_N/). Every successful return and its
inverse retain actual positive divisor labels.

For example, /(N=M=T=1,c=-1,d=1,e=1/) gives a valid initial and final
reciprocal divisor /(1/), but the intermediate image is /(2/), which is
not the reciprocal of a positive integer: its index /(2/) does not
divide the middle budget /(1/). Also /(N=M=T=1,c=1,d=-1,e=1/)
has the same valid endpoints but intermediate image zero. These
examples separately verify the necessity of intermediate divisibility
and strict positivity.

## The /(L/)-edge identification

For the complete adjacent /(L/)-shear parameters,

/[
a=m+c/,m(m+1),/qquad b=a+1,/qquad c/ge0,
/]

the source and target primitive pairs are /((m,1)/) and /((m+1,1)/).
Their middle divisors and reciprocal indices are

/[
u_L=am,/qquad v_L=b(m+1),/qquad
e=/frac{a^2}{u_L}=1+c(m+1),/qquad
e'=/frac{b^2}{v_L}=1+cm.
/]

Both divisor bounds follow from /(m/mid a/), /(m+1/mid b/).
Since /(e-e'=c/) and /(e'>0/),

/[
/Psi_{a^2,b^2,c}(1/u_L)=/frac{e-c}{b^2}
=/frac{e'}{b^2}=/frac1{v_L}.
/]

The source mark /(R_a/mid u_L+a/) is equivalent to
/(R_a/mid m+1/), because /(/gcd(a,R_a)=1/). The target mark
/(R_b/mid v_L+b/) is equivalent to /(R_b/mid m+2/).
These are exactly the original edge conditions. Thus no missing
mark-preservation implication is being assumed. The reconstruction
through the previously proved middle-divisor bijection returns the same
positive ordered denominator triples.

For this /(L/)-oriented correspondence, using zero correction instead
would give the same reciprocal target exactly when /(e=e'/), hence
exactly when /(c=0/).
For /(c>0/), it has no positive reciprocal integer return at all:
/(e=1+c(m+1)>1/), /(e/mid a/), and
/(/gcd(a,b)=1/), so /(/gcd(e,b^2)=1/). Thus the uncorrected
image /(e/b^2/) cannot equal /(1/v/) with /(v/) an integer. The final
manuscript proves this stronger assertion explicitly.

## The required /(J/)-conjugation, with explicit inverse and domain

The integer-divisor complement at budget /(N/) is

/[
C_N(u)=N/u.
/]

Its corresponding involution on the explicitly specified finite locus
/(/mathscr R_N=/{1/u:u/in/operatorname{Div}(N)/}/) is

/[
/kappa_N(x)=/frac1{Nx}.
/]

It exchanges the two primitive coordinates under the middle-divisor
bijection. Therefore the /(J/)-oriented map is
/(/kappa_M/circ/Psi_{N,M,c}/circ/kappa_N/), with each involution
restricted to its actual positive reciprocal-divisor set. Directly,

/[
/kappa_M/!/left(
/Psi_{N,M,c}/!/left(/frac1{Nx}/right)/right)
=/kappa_M/!/left(/frac{1-cx}{Mx}/right)
=/frac{x}{1-cx}.
/]

The same rational formula for /(/kappa_N/) is an involution of
/(/mathbb Q_{>0}/), but it is not an everywhere-defined map /(H_N/to H_N/):
zero is excluded, and /(/kappa_1(2)=1/2/notin H_1=/mathbb Z/).
All group-lattice and divisor domains must therefore remain attached.

If /(x=1/u/), its exact positive divisor return is

/[
u/longmapsto v=u-c,/qquad
u/mid N,/quad u>c,/quad u-c/mid M.
/]

The inverse on this image is /(v/mapsto v+c/), retaining
/(v/mid M/), /(v+c>0/), and /(v+c/mid N/).
The conjugated formula is undefined at /(u=c/), corresponding exactly
to the excluded zero intermediate image.

For the actual /(J/)-edge obtained by exchanging the two coordinates,

/[
(1,m)/longmapsto(1,m+1),/qquad
u_J=/frac am=1+c(m+1),/qquad
v_J=/frac b{m+1}=1+cm=u_J-c.
/]

These are the complements of /(u_L,v_L/). The source and target marks
are retained by complement: if /(u/mid a^2/), then /(u/) is a unit
modulo /(R_a/), and

/[
R_a/mid u+a
/iff
R_a/mid /frac{a^2}{u}+a,
/]

because multiplying the second expression by /(u/) gives
/(a(a+u)/), and both /(a/) and /(u/) are units modulo /(R_a/).
The same calculation applies at /(b/). The reconstruction exchanges
the last two ordered denominators, as required by pair exchange.

An unconjugated /(J/)-interpretation would be false. At the valid shear
/(p=1753,a=440,b=441,m=20,c=1/), the /(J/)-divisors are
/(u_J=22/), /(v_J=21/). But

/[
/Psi_{193600,194481,1}(1/22)
=/frac{8799}{194481}
=/frac{419}{9261}/ne/frac1{21}.
/]

The conjugated map gives
/((1/22)/(1-1/22)=1/21/) exactly.
The final manuscript makes no such unconjugated assertion. Its explicit
equation labelled eq:conjugate-affine and the following domain, inverse,
complement and example calculations give the correct conjugated map.
They restrict /(/iota_N/), which is the manuscript's notation for
/(/kappa_N/), to the positive reciprocal-divisor locus. The orientation
clarification is therefore fully resolved.

## Exact finite checks and scope

Direct enumeration tested all 63 eligible primes through /(1753/),
all 26,439 allowed adjacent shell pairs, and all 3,956 passing ordered
source primitive pairs. It found eight directed elementary shear edges
and no length-two path; each indegree and each outdegree was at most one.

The complete grid /(1/le N,M/le40/), /(-8/le c/le8/) checked
244,800 full-lattice index/inverse/order instances, 107,440 reciprocal
return instances, and 107,440 /(J/)-conjugation instances, including zero
and negative intermediate values. Another 125,440 exact rational
calculations checked the composition rule for /(1/le N,M,T/le8/),
/(-3/le c,d/le3/), and integer labels /(-4,-1,0,1,4/).

All assertions passed, and no unresolved mathematical finding remains
in the reviewed final blocks. These finite calculations supplement the
all-parameter proofs above. The elementary-shear obstruction does not
exclude other arithmetic successor maps or prove a global occupancy
theorem; the affine composition law alone makes neither claim.
