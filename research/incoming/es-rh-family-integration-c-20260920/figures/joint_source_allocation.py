"""Render the typed source-minimum and determinant-allocation maps in JS1--JS9."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent


def box(ax, xy, width, height, title, formula, color):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.025",
        linewidth=1.7,
        edgecolor=color,
        facecolor="#ffffff",
    )
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + 0.67 * height, title, ha="center", va="center", fontsize=11, weight="bold")
    ax.text(xy[0] + width / 2, xy[1] + 0.30 * height, formula, ha="center", va="center", fontsize=10)


def arrow(ax, start, end, label, color="#333333"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, linewidth=1.5, color=color))
    ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.035, label, ha="center", va="bottom", fontsize=9.5, color=color)


def main() -> None:
    fig, ax = plt.subplots(figsize=(12.6, 7.4), constrained_layout=True)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    box(ax, (0.04, 0.70), 0.25, 0.18, "old scalar source", r"$X:\mathcal{P}_N\hookrightarrow\mathcal{H}$" + "\n" + r"$H_X=X^*X$", "#1f78b4")
    box(ax, (0.375, 0.70), 0.25, 0.18, "constructed section", r"$\mathcal{R}:C\to\mathcal{H}$" + "\n" + r"$J_{\mathrm{phys}}\mathcal{R}=I_C$", "#33a02c")
    box(ax, (0.71, 0.70), 0.25, 0.18, "normal component", r"$Z=(I-XH_X^{-1}X^*)\mathcal{R}$" + "\n" + r"$H_Z=Z^*Z$", "#6a3d9a")
    arrow(ax, (0.29, 0.79), (0.375, 0.79), r"$C_X=X^*\mathcal{R}$")
    arrow(ax, (0.625, 0.79), (0.71, 0.79), "orthogonal projection")

    box(ax, (0.06, 0.43), 0.27, 0.17, "old quotient metric", r"$G=(JH_X^{-1}J^*)^{-1}$", "#1f78b4")
    box(ax, (0.365, 0.43), 0.27, 0.17, "new value covariance", r"$F=I-JH_X^{-1}C_X$" + "\n" + r"$C=FH_Z^+F^*$", "#6a3d9a")
    box(ax, (0.67, 0.43), 0.27, 0.17, "joint minimum", r"$G_J=(G^{-1}+C)^{-1}$", "#e31a1c")
    arrow(ax, (0.50, 0.69), (0.50, 0.60), r"$\ker H_Z\subseteq\ker F$")
    arrow(ax, (0.33, 0.515), (0.365, 0.515), "add inverse covariances")
    arrow(ax, (0.635, 0.515), (0.67, 0.515), "invert")

    box(ax, (0.39, 0.285), 0.22, 0.075, "whitened covariance", r"$T=G^{1/2}CG^{1/2}$", "#4d4d4d")
    arrow(ax, (0.805, 0.43), (0.61, 0.345), "congruence")

    box(ax, (0.08, 0.075), 0.37, 0.135, "observed quotient", r"$D_{\rm obs}=\log\det(I+T_{22})$", "#ff7f00")
    box(ax, (0.55, 0.075), 0.37, 0.135, "old-kernel restriction", r"$K=\ker\Lambda$" + "\n" + r"$D_{\rm ker}=\log\det(I+S_K)$", "#b15928")
    arrow(ax, (0.46, 0.285), (0.28, 0.21), "")
    arrow(ax, (0.54, 0.285), (0.72, 0.21), "")
    ax.text(
        0.5,
        0.018,
        r"$D_{\rm total}=D_{\rm obs}+D_{\rm ker}=\log\det(I+T)$; the mixed block $T_{12}$ is retained.",
        ha="center",
        va="bottom",
        fontsize=10.5,
    )
    ax.set_title("Exact joint-source minimum and determinant allocation", fontsize=15, pad=14)
    for suffix in ("pdf", "png"):
        fig.savefig(ROOT / f"joint_source_allocation.{suffix}", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
