# Typed maps, inverse domains, fibres, and loss

## Original arithmetic

1. Fix p prime, p=1 mod4 and p/4<a<p/2. The source is the entire exponent box
   0<=f_q<=2e_q at a=prod q^e_q, with the channel separately retained.
2. u -> g=gcd(a,u), (h,r,s)=(g^2/u,u/g,a/g). Its inverse is
   a=hrs,u=hr^2,gcd(r,s)=1. No original exponent occurrence is discarded.
3. E: kappa=(pr+s)/R, ordered denominators (a,hs*kappa,phr*kappa).
   M: lambda=(r+s)/R, ordered denominators (a,phs*lambda,phr*lambda).
   The quotients are rational before the full gate. Ordered inverses are
   u=a^2/(Ry-pa) and u=pa^2/(Ry-pa), respectively.
4. M complement already encodes its two tail orders. An E tail exchange is a
   separate permutation; it is not another free bit on an already ordered M word.

## Fine defect and its source boxes

5. R=4a-p, K=prod l^ceil(v_l(R)/2), D=R/K. The map c -> Kc identifies the
   additive group Z/D with the literal square-zero ideal KZ/R. D=1 is retained.
6. On an actual trace, p^eta*u/a=-1+Kc modR, eta=1 for E,0 for M. Full gate
   iff c=0; common rational tail denominator is D/gcd(D,c).
7. Original prime exponent intervals are partitioned by ord_K(q):
   beta_q=b_q+o_q*t_q, 0<=t_q<N_q. On a coarse trace part the fine map is
   c=c0-sum lambda_q*t_q, lambda_q=(q^o_q-1)/K modD.
   Inversion reads the original beta, the unique part, and t_q. Explicitly chosen
   subrectangles retain all omitted original words in the surrounding source.
8. The integer polynomial coefficients count one actual original vector per
   index. Group indices, not integer coefficients, are reduced modulo D.

## Exact channel translation

9. For the same original divisor u, the trace gates are K|(4u+1) in E and
   K|(p+4u) in M. Their intersection is nonempty exactly when K|(p-1). If this
   divisibility holds, the complete E and M trace sets coincide; otherwise they
   are disjoint.
10. On the common locus, omega=(p-1)/K and the typed fine-coordinate map is
    c_M -> c_E=c_M-omega in Z/D. The M full target is 0 and the E full target,
    expressed in the M coordinate, is omega. No such translation is asserted
    outside the common-trace locus.
11. On integer coefficient lattices, T_omega sends f_x to f_(x-omega) and the
    labelled paired-count map is I+T_omega. If d=gcd(D,omega) and L=D/d, then
    L is odd and its inverse over the image is the exact alternating formula
    2C_x=sum from j=0 to L-1 of (-1)^j J_(x-j omega). The integral cokernel is
    one parity bit for each of the d translation orbits.
12. Uniform paired positivity is exactly the support cover by S and S+omega.
    A chain ending at g reduces the complete-block subsource to the residual
    quotient vector Q on Z/g. The quotient support and its omega-translate must
    cover Z/g. Terminal intervals remain in the original source and are not
    removed by this reduction.

## Mixed-order section

13. A strict chain g0=D, gj=gcd(g(j-1),lambda_ij)>0, gk=1, has relative radices
   mj=g(j-1)/gj. Distinct labels, all actual lengths N_ij>=mj, are required.
14. Digits 0<=t_ij<mj -> sum lambda_ij*t_ij modD is a bijection of sets. The
    reverse divisions c_j/g_j and lambda_ij/g_j are exact, and the latter is
    inverted modulo mj. This is not generally a product-group isomorphism.
15. The carried group law is obtained by decoding the sum of two residue images.
    In D=9 with steps6,1 and radices3,3, (0,2)*(0,1)=(2,0).
16. Each full radix block and each unused coordinate vector gives a separate
    original word over every residue. The lower bound is
    prod(unused N_i)*prod floor(N_ij/mj). If selected lengths equal the radices,
    every coefficient is exactly prod(unused N_i). The decoder inverts the
    augmented map to the residue and retained unused-digit vector. For the
    residue projection, choose one reference word in each bin; its differences
    from the other words in that bin form a kernel basis. The rank is the
    multiplicity times D minus D. All pairwise same-bin differences generate
    this kernel but are dependent.
17. The optimizer's states are actual divisors g of D. Its edge weight for label i
    is floor(N_i/(g/gcd(g,lambda_i)))/N_i, with a strict decrease and sufficient
    original length. No effective label can recur. Optimization is complete only
    within this specified chain certificate class; it does not decide positivity.
18. Shortening the last relative digit interval in the arithmetic sharpness family
    gives a bijection onto the complement of H_m=mZ/D. The actual coefficient
    stabilizer is H_m. The zero fibre is empty, not a supported reduced coefficient.

## Upward plus-factor relation

19. From an original cell and a chosen s|a retain n=a/s, C=R+s, M=p+C=4a+s.
    The choice s is taken from the exact gcd factorization in the trace examples.
20. Every cell in that fibre is a divisor s'|M with M/s'=1 mod4 and
    0<R'=C-s'<p. Its inverse retains the old and new s. Set
    n'=(M/s'-1)/4,a'=(M-s')/4. Then a'-a=(s-s')/4 exactly.
21. An E terminal with primitive r'=1 additionally requires R'|M. Its marking is
    (h',r',s',kappa')=(n',1,s',M/R'-1), u'=n'. The ordered denominators are
    (a',n's'kappa',pn'kappa'). Here
    gcd(R',s')=gcd(4n's'-p,s')=gcd(p,s')=1, so R'|(4n'+1) is equivalent to
    R'|M=(4n'+1)s'. This condition is tested, not assumed nonempty.
22. Over a marked unit-ray E target, reconstruct C=R'+s', M=p+C. For every
    source cell and every r|n with gcd(r,s)=1, put h=n/r,u=nr and test the
    literal E/M square gates. This is the complete canonical trace input fibre.
23. On ordered rational solution triples, the exact E-tail map is
    tau_E(a,Y,Z)=(a,Z,Y), with tau_E squared equal to the identity. It need not
    preserve the original E exponent box, so it is not inserted as another word
    in the canonical incoming fibre. The M word already retains its tail order.
24. The arrow source includes its selected target. Forgetting that choice gives
    a relation when several targets pass. Choose one reference arrow over every
    actual target; the differences between every other arrow and its reference
    form a basis of the free-integer projection kernel. It is not a section over
    all hypothetical targets.
25. Old and new prime supports are not identified. At p67369 the shift from
    16849 to16850 changes {7,29,83} to{2,5,337}. The invariant 4a+s is retained;
    an assertion that each factor was transported unchanged would be false.

No receiver, analytic metric, or independently defined Split-Zero support object
is identified with these finite-ring coordinates without an additional typed map.
