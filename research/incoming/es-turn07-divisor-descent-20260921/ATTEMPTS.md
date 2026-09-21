# Attempt ledger

Purpose: extend the preceding prime-distinguished-denominator trace descent to
composite distinguished denominators and test the actual missing source budget.

1. Directly stripping all squares from the residual was not accepted as an
   original-source map. Recomputing the word budget gave the exact criterion
   k=1 mod4K(u). The p51361 example proves why maximal stripping can fail even
   when a smaller square deletion succeeds.
2. Restricting deletions to squares was also unnecessary. The complete map
   permits every divisor k with d|k and k=1 mod4K(u). This repairs additional
   actual sources, including an available complemented form of the earlier
   p1009 negative control.
3. Universal descent for arbitrary fixed word u was tested at its real arithmetic
   group, not guessed from coverage. The group of unit squares is trivial
   exactly at u|36. This yields a source-level positive theorem.
4. The opposite implication was investigated constructively, not inferred from
   one failed example: a nontrivial unit-square class supplies two auxiliary
   primes and a reduced progression of hard primes with a genuinely available
   original word. Every residual-divisor return fails there. The middle
   complement fails too, and a finite cofactor-capacity theorem exhausts the
   specified cofactor box. Independent endpoint states prove these are not
   counterexamples to ES.
5. Larger groups are retained through geometric coefficient products. A shortest
   existing word has a finite occurrence bound. This is not used as a hypothesis
   replacing missing positivity.

Outcome: a complete original composite-source descent domain; an optimal nine-word
universal guarantee within it; explicit integer multiplicities; and an infinite
arithmetic obstruction to extending the guarantee to all seeds. Universal
starting-source existence is still not proved.
