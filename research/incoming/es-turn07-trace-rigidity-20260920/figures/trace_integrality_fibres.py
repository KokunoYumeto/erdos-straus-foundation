"""Render the denominator implication and an exact raw trace fibre sample."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent


def trace_value(p: int, a: int, r: int, u: int) -> Fraction:
    """Return S(U)=p+a+p(a+U)^2/(RU) without floating-point arithmetic."""

    return Fraction(p + a, 1) + Fraction(p * (a + u) ** 2, r * u)


fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12.2, 5.25), constrained_layout=True)

ax0.set_axis_off()
box = dict(boxstyle="round,pad=0.45", facecolor="#f8fafc", edgecolor="#475569", linewidth=1.2)
ax0.text(
    0.50,
    0.85,
    r"$x_1,\ldots,x_n\in\mathbf{Q}^{\times}$" "\n"
    r"$s_1,\ldots,s_{n-1}\in\mathbf{Z}$,  $\sum_i x_i^{-1}=m/b$",
    ha="center",
    va="center",
    fontsize=11,
    bbox=box,
    transform=ax0.transAxes,
)
ax0.annotate(
    "",
    xy=(0.50, 0.58),
    xytext=(0.50, 0.73),
    xycoords=ax0.transAxes,
    arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#334155"),
)
ax0.text(0.53, 0.655, "Newton identities + exact valuations", fontsize=9.5, transform=ax0.transAxes)
ax0.text(
    0.50,
    0.46,
    r"one reduced denominator $d$" "\n"
    r"$\gcd(d,b)=1$,  $d^n\mid(n-1)!m$",
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#e0f2fe", edgecolor="#0369a1", linewidth=1.4),
    transform=ax0.transAxes,
)
ax0.annotate(
    "",
    xy=(0.50, 0.18),
    xytext=(0.50, 0.34),
    xycoords=ax0.transAxes,
    arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#334155"),
)
ax0.text(0.53, 0.255, r"$m\mid4$, $n\geq3$: every denominator prime is excluded", fontsize=9.3, transform=ax0.transAxes)
ax0.text(
    0.50,
    0.09,
    r"$d=1$: all $x_i\in\mathbf{Z}$",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="bold",
    color="#166534",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#dcfce7", edgecolor="#15803d", linewidth=1.4),
    transform=ax0.transAxes,
)
ax0.text(
    0.02,
    0.01,
    r"Necessary boundary: at $n=2$, $(p/2,p/2)$ has integral first trace for odd $p$.",
    fontsize=9,
    color="#9f1239",
    transform=ax0.transAxes,
)
ax0.set_title("Global denominator return", fontsize=13, fontweight="bold")

p, a, r = 13, 4, 3
us = [u for u in range(1, p * a * a + 1) if (a + u) % r == 0]
vals = [trace_value(p, a, r, u) for u in us]
ys = np.array([float(v) for v in vals])
ax1.scatter(us, ys, s=20, color="#94a3b8", alpha=0.65, label=r"raw gate $R\mid a+U$")

integral_us = [u for u, s in zip(us, vals) if s.denominator == 1]
assert integral_us == [2, 8, 26, 104]
assert [trace_value(p, a, r, u) for u in integral_us] == [
    Fraction(95), Fraction(95), Fraction(167), Fraction(503)
]
for u in integral_us:
    s = trace_value(p, a, r, u)
    if u in (2, 8):
        color, marker, label = "#7c3aed", "o", "M return"
    else:
        color, marker, label = "#dc2626", "s", "E return"
    ax1.scatter([u], [int(s)], s=70, color=color, marker=marker, zorder=5)
    ax1.annotate(
        f"U={u}, S={int(s)}",
        xy=(u, int(s)),
        xytext=(7, 8 if u not in (2, 8) else (14 if u == 2 else -18)),
        textcoords="offset points",
        fontsize=9,
        color=color,
    )

ax1.annotate(
    "",
    xy=(8, 95),
    xytext=(2, 95),
    arrowprops=dict(arrowstyle="<->", color="#7c3aed", lw=2.0, connectionstyle="arc3,rad=-0.4"),
)
ax1.text(4.4, 111, r"$UV=a^2=16$", color="#7c3aed", fontsize=10)
ax1.text(
    0.98,
    0.97,
    r"$p=13$, $a=4$, $R=3$" "\n"
    r"$S(U)=p+a+\dfrac{p(a+U)^2}{RU}$" "\n"
    r"$S(U)\in\mathbf{Z}\Longleftrightarrow U\mid pa^2$",
    transform=ax1.transAxes,
    ha="right",
    va="top",
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#cbd5e1", alpha=0.96),
)
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlim(1.5, 220)
ax1.set_xlabel(r"raw source word $U$")
ax1.set_ylabel(r"literal trace $S(U)$")
ax1.set_title("Exact trace fibres on one complete raw gate", fontsize=13, fontweight="bold")
ax1.grid(True, which="both", color="#e2e8f0", linewidth=0.7)

fig.suptitle("Integral traces recover arithmetic data without erasing the source fibres", fontsize=14, fontweight="bold")
fig.savefig(OUT / "trace_integrality_fibres.pdf", bbox_inches="tight")
fig.savefig(OUT / "trace_integrality_fibres.png", dpi=220, bbox_inches="tight")
plt.close(fig)
