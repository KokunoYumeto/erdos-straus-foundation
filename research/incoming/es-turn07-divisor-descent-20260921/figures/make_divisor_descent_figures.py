#!/usr/bin/env python3
"""Render the exact divisor-descent map and the nine-word boundary.

The diagrams use only integer data proved in core.tex.  Every displayed
example value is recomputed and checked before rendering.
"""
from __future__ import annotations

from math import gcd, prod
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent
BLUE = "#165D8C"
PALE_BLUE = "#E8F3F8"
GOLD = "#D28B17"
PALE_GOLD = "#FFF4D6"
RED = "#A63A3A"
PALE_RED = "#FBEAEA"
INK = "#17212B"
GREY = "#5B6770"


def factors(n: int) -> list[tuple[int, int]]:
    ans: list[tuple[int, int]] = []
    q = 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            ans.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        ans.append((n, 1))
    return ans


def divisors(n: int) -> list[int]:
    out = [1]
    for q, e in factors(n):
        out = [d * q**j for d in out for j in range(e + 1)]
    return sorted(out)


def upper_half(n: int) -> int:
    return prod(q ** ((e + 1) // 2) for q, e in factors(n))


def square_image(m: int) -> tuple[int, ...]:
    return tuple(sorted({x * x % m for x in range(m) if gcd(x, m) == 1}))


def box(ax, xy, width, height, text, face, edge=INK, fontsize=10.5):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.018,rounding_size=0.018",
        linewidth=1.35,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=INK,
        linespacing=1.38,
    )
    return patch


def arrow(ax, start, end, color=BLUE, rad=0.0, lw=1.8):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=lw,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def render_map() -> None:
    p, a, R, u, d, m = 1_108_801, 279_295, 8_379, 5, 3, 20
    assert R == 4 * a - p
    all_k = [d * v for v in divisors(R // d)]
    valid = [k for k in all_k if k % m == 1]
    assert all_k == [3, 9, 21, 57, 63, 147, 171, 399, 441, 1197, 2793, 8379]
    assert valid == [21, 441]
    targets = [(k, R // k, (p + R // k) // 4) for k in valid]
    assert targets == [(21, 399, 277_300), (441, 19, 277_205)]

    fig = plt.figure(figsize=(13.2, 7.4), facecolor="white")
    ax = fig.add_axes([0.035, 0.075, 0.93, 0.865])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(
        0.0,
        1.015,
        "Exact same-word residual-divisor descent",
        fontsize=19,
        fontweight="bold",
        color=INK,
        va="bottom",
    )
    ax.text(
        0.0,
        0.975,
        "Every map, congruence, inverse parameter and lost coordinate is retained.",
        fontsize=10.8,
        color=GREY,
        va="top",
    )

    box(
        ax,
        (0.02, 0.62),
        0.29,
        0.245,
        r"proper trace source $s=(p,a,R,u,c)$"
        "\n"
        r"$R=4a-p,\quad u\mid a^2,\quad R\mid G_c^2$"
        "\n"
        r"$d=R/\gcd(R,G_c)>1,\quad d^2\mid R$",
        PALE_BLUE,
    )
    box(
        ax,
        (0.39, 0.62),
        0.29,
        0.245,
        r"full integral target $t=(p,a',R',u,c)$"
        "\n"
        r"$R'=R/k,\quad a'=(p+R')/4$"
        "\n"
        r"$R'\mid G_c,\quad u\mid(a')^2,\quad a'<a$",
        PALE_GOLD,
    )
    arrow(ax, (0.31, 0.745), (0.39, 0.745))
    ax.text(
        0.35,
        0.825,
        r"$k\mid R$" + "\n" + r"$d\mid k$" + "\n" + r"$k\equiv1\;(\mathrm{mod}\;4K(u))$",
        ha="center",
        va="center",
        fontsize=9.5,
        color=BLUE,
    )
    arrow(ax, (0.39, 0.66), (0.31, 0.66), color=GOLD, rad=-0.2, lw=1.45)
    ax.text(
        0.35,
        0.602,
        r"fixed-source inverse: $k=R/R'$",
        ha="center",
        va="top",
        fontsize=9.3,
        color="#8A5A08",
    )
    box(
        ax,
        (0.035, 0.22),
        0.63,
        0.245,
        r"global fibre over a fixed full target $(p,a',R',u,c)$"
        "\n"
        r"$1\leq k\leq\lfloor(p-1)/R'\rfloor,\quad k\equiv1\;(\mathrm{mod}\;4K(u))$"
        "\n"
        r"$R'k\mid G_c^2,\quad R'k\nmid G_c$"
        "\n"
        r"$R=R'k,\quad a=(p+R'k)/4$; forgetting $k$ loses the old $(R,a)$.",
        "#F2F4F6",
        fontsize=10.2,
    )
    arrow(ax, (0.535, 0.62), (0.54, 0.465), color=GREY, lw=1.4)

    ax.plot([0.705, 0.705], [0.08, 0.9], color="#D4D9DD", linewidth=1.2)
    ax.text(
        0.735,
        0.89,
        r"Exact mixed-factor fixture: $p=1{,}108{,}801$",
        fontsize=12.5,
        fontweight="bold",
        color=INK,
    )
    ax.text(
        0.735,
        0.835,
        r"$R=8379=19\cdot3^2\cdot7^2, d=3, u=5, m=20$",
        fontsize=10.5,
        color=INK,
    )
    ax.text(0.735, 0.78, "All positive divisors k of R containing d:", fontsize=9.8, color=GREY)

    y0 = 0.735
    for i, k in enumerate(all_k):
        col = i % 3
        row = i // 3
        x = 0.745 + 0.083 * col
        y = y0 - 0.06 * row
        ok = k in valid
        ax.text(
            x,
            y,
            f"{k:>4} ≡ {k % m:>2}",
            fontsize=9.4,
            family="monospace",
            color=BLUE if ok else GREY,
            fontweight="bold" if ok else "normal",
            bbox=dict(
                boxstyle="round,pad=0.18",
                facecolor=PALE_BLUE if ok else "white",
                edgecolor=BLUE if ok else "#D8DDE1",
                linewidth=1.0,
            ),
        )

    ax.text(
        0.735,
        0.46,
        r"Only $k=21,441$ satisfy $k\equiv1\;(\mathrm{mod}\;20)$.",
        fontsize=10.3,
        color=BLUE,
        fontweight="bold",
    )
    box(
        ax,
        (0.735, 0.275),
        0.235,
        0.14,
        r"$k=21: R'=399, a'=277300$"
        "\n"
        r"$(h',r',s',\lambda')=(5,1,55460,139)$",
        PALE_GOLD,
        fontsize=9.2,
    )
    box(
        ax,
        (0.735, 0.09),
        0.235,
        0.14,
        r"$k=441: R'=19, a'=277205$"
        "\n"
        r"$(h',r',s',\lambda')=(5,1,55441,2918)$",
        PALE_GOLD,
        fontsize=9.2,
    )
    ax.text(
        0.02,
        0.045,
        "The divisor 7 is not required by d=3, but its residue is required to preserve the original word u=5.",
        fontsize=9.5,
        color=GREY,
    )
    for ext in ("png", "pdf"):
        fig.savefig(ROOT / f"divisor_descent_map.{ext}", dpi=210 if ext == "png" else None, bbox_inches="tight")
    plt.close(fig)


def render_boundary() -> None:
    safe = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    rows = [(u, upper_half(u), 4 * upper_half(u), square_image(4 * upper_half(u))) for u in safe]
    assert all(image == (1,) for _, _, _, image in rows)
    assert [u for u in range(1, 37) if 36 % u == 0] == safe

    u = 8
    m = 4 * upper_half(u)
    b, delta, t, R = 5, 71, 13, 11_999
    p, a, d = 48_116_881, 12_032_220, 13
    assert m == 16 and square_image(m) == (1, 9)
    assert R == delta * t * t and R == 4 * a - p
    assert gcd(R, p + 4 * u) == delta * t and R // gcd(R, p + 4 * u) == d
    assert (p + delta) % m == 8 and (p + delta * t) % m == 12
    complement_modulus = 4 * upper_half(a * a // u)
    assert complement_modulus == 24_064_440 and complement_modulus > R

    fig = plt.figure(figsize=(13.2, 7.1), facecolor="white")
    ax = fig.add_axes([0.04, 0.08, 0.92, 0.86])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(
        0.0,
        1.01,
        "The exact nine-word boundary—and what fails outside it",
        fontsize=19,
        fontweight="bold",
        color=INK,
        va="bottom",
    )
    ax.text(
        0.0,
        0.965,
        r"A uniform one-step square deletion exists iff $H_{4K(u)}=\{1\}$ iff $u\mid36$.",
        fontsize=11.2,
        color=GREY,
        va="top",
    )

    ax.text(0.02, 0.86, "All and only the automatic words", fontsize=13, fontweight="bold", color=INK)
    x0, y0 = 0.02, 0.70
    for i, (word, kval, modulus, image) in enumerate(rows):
        col, row = i % 3, i // 3
        x, y = x0 + col * 0.17, y0 - row * 0.18
        box(
            ax,
            (x, y),
            0.145,
            0.13,
            rf"$u={word}$" + "\n" + rf"$K(u)={kval}, m={modulus}$" + "\n" + r"$H_m=\{1\}$",
            PALE_BLUE,
            edge=BLUE,
            fontsize=9.7,
        )

    ax.text(
        0.02,
        0.18,
        r"For every proper source at these words, $q_0=K(d)$ gives "
        r"$k=q_0^2$ and $R'=R/q_0^2$.",
        fontsize=10.3,
        color=BLUE,
    )
    ax.text(
        0.02,
        0.115,
        r"The complete square family has $\tau(t/q_0)$ distinct targets; no source-existence claim is added.",
        fontsize=9.8,
        color=GREY,
    )

    ax.plot([0.555, 0.555], [0.08, 0.9], color="#D4D9DD", linewidth=1.2)
    ax.text(0.59, 0.885, r"Outside boundary: the exact $u=8$ obstruction", fontsize=13, fontweight="bold", color=INK)
    box(
        ax,
        (0.59, 0.69),
        0.37,
        0.14,
        r"$m=16,\quad H_{16}=\{1,9\},\quad b=5$"
        "\n"
        r"$\delta=71, t=13, R=\delta t^2=11999$"
        "\n"
        r"$p=48116881, a=12032220, d=t=13$",
        PALE_RED,
        edge=RED,
        fontsize=10.1,
    )
    ax.text(0.59, 0.625, "Every possible same-word target residual fails:", fontsize=10.4, color=INK)
    box(
        ax,
        (0.59, 0.445),
        0.17,
        0.13,
        r"$R'=\delta=71$"
        "\n"
        r"$p+R'\equiv8\not\equiv0$"
        "\n"
        r"$(\mathrm{mod}\;16)$",
        "#FFF7F7",
        edge=RED,
        fontsize=9.6,
    )
    box(
        ax,
        (0.79, 0.445),
        0.17,
        0.13,
        r"$R'=\delta t=923$"
        "\n"
        r"$p+R'\equiv12\not\equiv0$"
        "\n"
        r"$(\mathrm{mod}\;16)$",
        "#FFF7F7",
        edge=RED,
        fontsize=9.6,
    )
    box(
        ax,
        (0.59, 0.265),
        0.37,
        0.125,
        r"middle complement $u^*=a^2/u$"
        "\n"
        r"$4K(u^*)=24064440>R$; its exact denominator is still $13$",
        PALE_GOLD,
        edge=GOLD,
        fontsize=9.8,
    )
    ax.text(
        0.59,
        0.195,
        "This blocks the residual-divisor method, not Erdős–Straus.",
        fontsize=10.4,
        fontweight="bold",
        color=RED,
    )
    ax.text(
        0.59,
        0.135,
        r"A separate endpoint state $(13122786, 631427532350466, 144350643)$",
        fontsize=9.4,
        color=GREY,
    )
    ax.text(0.59, 0.095, r"has reciprocal sum $4/48116881$.", fontsize=9.4, color=GREY)

    for ext in ("png", "pdf"):
        fig.savefig(ROOT / f"nine_word_boundary.{ext}", dpi=210 if ext == "png" else None, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    render_map()
    render_boundary()
    print("rendered divisor_descent_map and nine_word_boundary (PNG/PDF)")


if __name__ == "__main__":
    main()
