"""Finite exact permutation certificates; no numerical path tests."""
from itertools import permutations, product
from collections import Counter

I = tuple(range(8))

def compose(p, q):
    return tuple(p[q[j]] for j in range(8))

def cycle(*items):
    out = list(I)
    for a, b in zip(items, items[1:]+items[:1]):
        out[a] = b
    return tuple(out)

# Index 2*j is root j with positive chosen sign; 2*j+1 is its negative.
betas = [cycle(2*j, 2*(j+1), 2*j+1, 2*(j+1)+1) for j in range(3)]
group = {I}
frontier = [I]
while frontier:
    current = frontier.pop()
    for beta in betas:
        nxt = compose(beta, current)
        if nxt not in group:
            group.add(nxt)
            frontier.append(nxt)

def parity(pi):
    return sum(pi[j] > pi[k] for j in range(4) for k in range(j+1, 4)) % 2

def signed_perm(pi, bits):
    return tuple(2*pi[j]+(sign ^ bits[j]) for j in range(4) for sign in range(2))

rotation_group = set()
weyl_d4 = set()
for pi in permutations(range(4)):
    for bits in product(range(2), repeat=4):
        perm = signed_perm(pi, bits)
        if sum(bits) % 2 == parity(pi):
            rotation_group.add(perm)
        if sum(bits) % 2 == 0:
            weyl_d4.add(perm)
assert group == rotation_group
assert len(group) == 192

def order(p):
    current, n = p, 1
    while current != I:
        current, n = compose(p, current), n+1
    return n

eight_cycle = compose(betas[0], compose(betas[1], betas[2]))
assert order(eight_cycle) == 8
assert all(order(g) != 8 for g in weyl_d4)
all_flip = tuple(j ^ 1 for j in range(8))
centralizer = []
for candidate in permutations(range(8)):
    if all(compose(candidate, beta) == compose(beta, candidate) for beta in betas):
        centralizer.append(candidate)
assert set(centralizer) == {I, all_flip}

print("Adjacent half-exchange generators:", betas)
print("Generated group equals determinant-one signed permutation group; order:", len(group))
print("Element-order distribution:", dict(sorted(Counter(map(order, group)).items())))
print("Product beta1 beta2 beta3 has order:", order(eight_cycle))
print("W(D4) element-order distribution:", dict(sorted(Counter(map(order, weyl_d4)).items())))
print("Full S8 centralizer has exactly identity and simultaneous sign reversal.")
print("All exact finite permutation checks passed.")
