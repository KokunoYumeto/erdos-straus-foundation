"""Independent finite check for the fixed-word square-image classification.

This script imports nothing from the supplied Turn 7 package.  It is not a
proof of the unbounded theorem; the accompanying Markdown report contains the
prime-power and CRT proof.  The finite run checks the exact residue maps and
the obstruction residues used in the converse construction.
"""

from math import gcd


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def upper_half(n: int) -> int:
    out = 1
    for prime, exponent in factor(n).items():
        out *= prime ** ((exponent + 1) // 2)
    return out


def square_image(modulus: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            {x * x % modulus for x in range(modulus) if gcd(x, modulus) == 1}
        )
    )


def main() -> None:
    automatic = []
    obstruction_rows = 0
    for u in range(1, 1001):
        modulus = 4 * upper_half(u)
        image = square_image(modulus)
        is_automatic = image == (1,)
        assert is_automatic == (36 % u == 0), (u, modulus, image)
        if is_automatic:
            automatic.append((u, upper_half(u), modulus, image))
            continue

        b = next(
            x
            for x in range(1, modulus)
            if gcd(x, modulus) == 1 and x * x % modulus != 1
        )
        if b % 4 != 1:
            b = (-b) % modulus
        assert b % 4 == 1
        assert gcd(b, modulus) == 1
        assert b * b % modulus != 1

        delta_residue = (-b * b) % modulus
        t_residue = pow(b, -1, modulus)
        residual_delta = (1 + delta_residue) % modulus
        residual_delta_t = (1 + delta_residue * t_residue) % modulus
        r_residue = delta_residue * t_residue * t_residue % modulus

        assert delta_residue % 4 == 3
        assert t_residue % 4 == 1
        assert r_residue == modulus - 1
        assert residual_delta == (1 - b * b) % modulus != 0
        assert residual_delta_t == (1 - b) % modulus != 0
        obstruction_rows += 1

    expected = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert [row[0] for row in automatic] == expected
    print("automatic rows")
    for row in automatic:
        print(row)
    print(f"checked u=1..1000; outside-word obstruction residue rows={obstruction_rows}")


if __name__ == "__main__":
    main()
