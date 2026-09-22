# Original domains, maps, inverses and coefficient fibres

1. Rational trace -> integer factor source.
   Domain: p prime1mod4, p/4<a<p/2, y,z positive rational, reciprocal identity,
   y+z integer. The common denominator d satisfies d^2=R/gcd(R,y+z).
   b=Ry-pa,c=Rz-pa are positive integers, bc=(pa)^2. Inverse adds pa and divides
   by the original R. The two p-valuations choose E or M; an exterior swap bit
   records the other tail orientation. This is not a claim about arbitrary
   rational tails without the integral first trace.
2. Factor source -> original divisor.
   p-valuation pair (0,2): u=a^2/b. Pair (2,0): swap and use a^2/c.
   Pair (1,1): u=pa^2/b. In every case u divides a^2. Keep its complete prime
   exponents, not merely its square class or residue.
3. Gcd normalization.
   g=gcd(a,u); h=g^2/u,r=u/g,s=a/g; inverse a=hrs,u=hr^2.
   beta_l=v_l(u)-v_l(a)=v_l(r)-v_l(s), with box radius v_l(a).
4. Rational channel return.
   E quotient kappa=(pr+s)/R may be nonintegral. M lambda=(r+s)/R likewise.
   Keep positive rational ordered denominators (a,hs*kappa,phr*kappa) or
   (a,phs*lambda,phr*lambda). Trace iff square gate; full integrality iff full
   gate. Original tail denominator d=R/gcd(R,G), not discarded by the trace.
5. General ray deletion.
   Keep p,r,s,channel E; k|R with d|k and k=1 mod4rs. Return R'=R/k,
   h'=(p+R')/(4rs),u'=h'r^2,a'=h'rs,kappa'=k*kappa.
   Retaining k inverts the operation. Centred beta is unchanged, but both box
   radius and absolute u exponents can change. This differs from fixed-u deletion.
6. Original integer deletion coefficient.
   Write k=dv. The geometric product over prime powers of R/d counts v at
   residue d^{-1} modulo4rs. Every integer divisor gets coefficient one before
   projection. Equal residues sum multiplicities; no binomial prime colours.
7. Automatic squarefree part.
   For rs|6 and p1mod24, R=delta*t^2 has delta=-1 mod4rs and delta|pr+s.
   Delta is the odd-exponent squarefree part, not the radical. It may be
   composite or share prime factors with t. Return the full E source at delta.
8. Exact trace fibres.
   A is the odd part of pr+s. Delta ranges over squarefree divisors of A with
   delta=-1 mod4rs. Preimages are t|A/delta, delta*t^2<p. Keep all exponents.
   The bounded source condition is indispensable (p97,delta7,t7 is excluded).
   At t=1 the target embeds back. The integer kernel is spanned by each other
   original source basis vector minus its t=1 vector. This split map does not
   imply the target set is nonempty.
9. Automatic E -> M.
   H=(delta+1)/(4rs),J=(pr+s)/delta; return hM=H,rM=s,sM=J,lambdaM=r,
   aM=HsJ,uM=Hs^2,RM=(s+J)/r,QM=delta, with ordered formula
   `(HsJ,pHJr,pHsr)`. Inverse reads r=lambdaM,s=rM,J=sM,
   delta=4hM*rM*lambdaM-1, then retained t gives original R,h.
   An exterior-swapped input uses the target complement HJ^2 and reverses the
   last two denominators. Receiver sorting is a separate tail permutation.
   Proper input strictly decreases min(RM,QM), not necessarily RM or aM.
10. Prime-carrier source.
    For a=cq,c|6,q>3 prime, characters force (q/p)=-1. E words have q-exponent
    one; their normal rays satisfy rs|c. The cofactor c and prime q are recovered
    from a in this domain. The assumption fails for a composite carrier.
11. Middle carrier orientation.
    q-exponent is zero or two. If two, retain epsilon=1 and replace u by a^2/u;
    otherwise epsilon=0. The resulting u0 divides c^2, hence36. Square deletion
    preserves its actual 4K(u0) budget. Recompute the target gcd normalization.
    Restore epsilon at the NEW shell by u_out=a'^2/u0, not with the old a.
12. Arbitrary input ordering.
    repair.py retains a separate exterior-input swap bit. It maps the canonical
    source first and restores the output middle order by a new-shell complement.
    It supplies both the canonical map and final ordered return in JSON.
13. Nonautomatic-ray CRT construction.
    Keep r,s,m,b, auxiliary primes delta,t,e, L, residue, modulus, threshold.
    CRT provides a reduced arithmetic progression, not primality of every sample.
    Dirichlet provides infinitely many prime members. A separately reconstructed
    endpoint M state exists for those primes. No arbitrary failed ray is treated
    as a failed ES instance.
14. Projection to a failed-ray certificate.
    At p6975049201 retain the entire factorization of 5p+3 and all32 divisors.
    The eight odd residue products miss59mod60. The old a-square has243 words
    and both full gates empty. The CRT source has a proper rational trace and a
    separately available endpoint integer state; all these objects coexist.
15. Ordered denominator inverse on a full hit.
    E: u=a^2/(Ry-pa). M: u=pa^2/(Ry-pa). Repeat gcd normalization to recover
    h,r,s and quotient. Sorting the middle tails loses its exact twofold
    orientation; no such sorting is used in the verification state hashes.
