"""Render exact finite geometry for ER12--ER14 and CP2--CP4."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


ROOT = Path(__file__).resolve().parent


def fibre_interval(k: int, u: int, v: int) -> tuple[int, int]:
    return max(0, u + v - k), min(u, v)


def collision_exponents(a: float) -> list[float]:
    # Exact specialization of CP2--CP3 at (e,f)=(3,2).
    if a <= 1:
        return [0.0, a, 2 * a, 2 + a, 4.0]
    return [0.0, 1.0, a + 1, a + 2, 2 * a + 2]


def main() -> None:
    k = 5
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.6, 6.0), constrained_layout=True)

    sizes = np.zeros((k + 1, k + 1), dtype=int)
    for u in range(k + 1):
        for v in range(k + 1):
            lo, hi = fibre_interval(k, u, v)
            sizes[v, u] = hi - lo + 1

    image = ax0.imshow(
        sizes,
        origin="lower",
        extent=(-0.5, k + 0.5, -0.5, k + 0.5),
        cmap="viridis",
        vmin=1,
        vmax=sizes.max(),
        interpolation="nearest",
    )
    for u in range(k + 1):
        for v in range(k + 1):
            lo, hi = fibre_interval(k, u, v)
            active = hi > lo
            ax0.add_patch(
                Rectangle(
                    (u - 0.5, v - 0.5),
                    1,
                    1,
                    fill=False,
                    linewidth=2.0 if active else 0.7,
                    edgecolor="#d73027" if active else "white",
                )
            )
            label = f"j={lo}" if lo == hi else f"j={lo},...,{hi}"
            ax0.text(u, v, label, ha="center", va="center", fontsize=7.4, color="white")
    ax0.set_xticks(range(k + 1))
    ax0.set_yticks(range(k + 1))
    ax0.set_xlabel(r"$u=n_1+n_2$")
    ax0.set_ylabel(r"$v=n_1+n_3$")
    ax0.set_title(r"Joint ES refinement of one RH grid, $k=5$, $D=0$")
    ax0.text(
        0.02,
        -0.16,
        r"Red cells: $\operatorname{Var}(j\mid u,v)>0$.  "
        r"$\dim\mathscr{W}^{\mathrm{joint}}=\binom{8}{3}=56$, "
        r"$q=36$, $\operatorname{rank}L_E=16$, $\dim\ker L_E=20$.",
        transform=ax0.transAxes,
        fontsize=9.2,
    )
    cbar = fig.colorbar(image, ax=ax0, fraction=0.046, pad=0.04, ticks=range(1, sizes.max() + 1))
    cbar.set_label("number of retained j-values")

    a_values = np.linspace(0.0, 2.5, 501)
    paths = np.asarray([collision_exponents(float(a)) for a in a_values])
    colors = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e"]
    for index in range(5):
        ax1.plot(a_values, paths[:, index], color=colors[index], linewidth=2.2, label=rf"$\nu_{index + 1}$")
    ax1.axvline(1.0, color="black", linestyle="--", linewidth=1.3)
    for index, value in enumerate(range(5)):
        ax1.scatter([1.0], [value], color=colors[index], s=28, zorder=4)
    ax1.set_xlim(0, 2.5)
    ax1.set_ylim(-0.15, 7.2)
    ax1.set_xlabel(r"jet-scale exponent $a$ in $\eta=|z|^a$")
    ax1.set_ylabel(r"singular exponent $\nu_j$")
    ax1.set_title(r"Two-centre collision spectrum, $(e,f)=(3,2)$")
    ax1.grid(alpha=0.23)
    ax1.legend(ncol=5, loc="upper left", fontsize=8.5)
    ax1.text(
        0.03,
        0.83,
        r"$0\leq a\leq1:\ (0,a,2a,2+a,4)$" "\n"
        r"$a\geq1:\ (0,1,a+1,a+2,2a+2)$" "\n"
        r"At $a=1$: $(0,1,2,3,4)$.",
        transform=ax1.transAxes,
        fontsize=9.5,
        bbox={"facecolor": "white", "edgecolor": "#777777", "alpha": 0.92},
    )

    fig.suptitle("Exact joint-observation and collision geometry", fontsize=15)
    for suffix in ("pdf", "png"):
        fig.savefig(ROOT / f"family_joint_es_collision.{suffix}", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
