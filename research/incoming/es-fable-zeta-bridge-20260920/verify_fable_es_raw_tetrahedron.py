#!/usr/bin/env python3
"""Exact certificate for the ES-aligned three-dimensional tetrahedron."""

import sympy as sp


q = sp.Rational
sqrt3 = sp.sqrt(3)
Phi = sp.Matrix(
    [
        [q(5, 8), 0, q(3, 4), q(5, 8)],
        [0, 1, 0, 0],
        [q(3, 8), 0, q(5, 4), q(3, 8)],
        [q(1, 2), 0, 0, -q(1, 2)],
    ]
)
assert Phi.det() == -q(1, 2)

raw = (
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([2, 2, 0, 2]),
    sp.Matrix([2 + sqrt3, -1, 0, 2 - sqrt3]),
    sp.Matrix([2 - sqrt3, -1, 0, 2 + sqrt3]),
)
expected = (
    sp.Matrix([q(3, 4), 0, q(5, 4), 0]),
    sp.Matrix([q(5, 2), 2, q(3, 2), 0]),
    sp.Matrix([q(5, 2), -1, q(3, 2), sqrt3]),
    sp.Matrix([q(5, 2), -1, q(3, 2), -sqrt3]),
)
transported = tuple(Phi * v for v in raw)
assert transported == expected


def lorentz_norm(v):
    t, x, y, w = v
    return sp.expand(x*x + y*y + w*w - t*t)


assert lorentz_norm(transported[0]) == 1
assert all(lorentz_norm(v) == 0 for v in transported[1:])

spatial = tuple(sp.Matrix([v[1], v[2], v[3]]) for v in transported)
p_star, p0, pp, pm = spatial
centroid = (p0 + pp + pm) / 3
assert centroid == sp.Matrix([0, q(3, 2), 0])
assert centroid - p_star == sp.Matrix([0, q(1, 4), 0])

face_points = (p0, pp, pm)
for i in range(3):
    for j in range(i + 1, 3):
        assert sp.expand((face_points[i] - face_points[j]).dot(
            face_points[i] - face_points[j])) == 12
for point in face_points:
    assert sp.expand((p_star - point).dot(p_star - point)) == q(65, 16)

edge_matrix = sp.Matrix.hstack(p0 - p_star, pp - p_star, pm - p_star)
assert sp.Abs(edge_matrix.det()) / 6 == sqrt3 / 4

print("PASS exact raw-cell to ES-aligned transport")
print("PASS Lorentz norms 1,0,0,0")
print("PASS spatial quarter (0,1/4,0)")
print("PASS edge squares 12 and 65/16")
print("PASS Euclidean volume sqrt(3)/4")
