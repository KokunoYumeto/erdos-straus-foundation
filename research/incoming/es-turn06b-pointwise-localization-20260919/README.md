# Pointwise localization after the complete-shell attempt

This proof was recovered from the supplied research-session transcript and then
independently rederived before integration. It is a separate continuation of
the complete-shell programme, not a replacement for the spectral Turn 6 proof.

For a hard prime $p\equiv1\pmod8$, every original middle state satisfies

\[
11a\le 3(p+3),\qquad 11R\le p+36,
\]

and the first bound is attained at $p=1009$. For exterior states, the least
quadratic nonresidue $\nu_p$ gives

\[
2\nu_p(p+1)\le(2\nu_p+1)(p-2a+1)^2.
\]

If the elementary $(p+1)$ endpoint construction is unavailable, the stronger
strict inequality

\[
2\nu_p(p+2)<(\nu_p+1)(p-2a+2)^2
\]

holds; at a hard prime this gives
$11(p+2)<6(p-2a+2)^2$. The complete reciprocal exterior coordinate also obeys

\[
D\le\left\lfloor\frac{(p+3)^2+4\nu_p}{12\nu_p}\right\rfloor,
\]

with equality at the recorded $p=1009$ state.

The proof also gives the exact free Klein-four action on the original positive
pair source, its unique fundamental representative $b<c$, $bc<pa$, and the
primitive fibre weights. It checks two exact failures of the smallest permitted
parameter choices at $p=2521$, while retaining the actual state with $Q=111$.
Finally, an odd-square example disproves a prime-free two-colour positivity
argument but not Erdős--Straus, because the two-colour source omits genuine
divisors of the composite numerator.

- `pointwise_localization.md`: complete proof, exact coordinates, equality
  cases, corrections to the plaintext extraction, and citations.
- `verify_localization.py`: independently enumerates the declared finite range
  and checks every displayed example and inequality.
- `verification.json`: deterministic normal/optimized replay receipt.
- `integration_verification.json`: transcript locator, explicit repairs,
  independent derivation audit, and fresh integration replay.

The result localizes every possible original state but does not prove that the
remaining region is occupied. It therefore does not prove Erdős--Straus.
