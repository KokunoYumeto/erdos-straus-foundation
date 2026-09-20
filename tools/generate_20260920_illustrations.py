"""Generate exact static illustrations for the 20 September ES continuations.

The figures are explanatory projections of proved formulas, not new geometric
identifications.  Every displayed coordinate and numerical example is taken
from the cited TeX proof.  Both vector PDF and inspection PNG are emitted.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "research/incoming/es-fable-zeta-bridge-20260920/figures"
LOCAL = ROOT / "research/incoming/es-turn07-fabel-arithmetic-bridge-20260920/corrected/figures"
CAPACITY = ROOT / "research/incoming/es-turn07-capacity-completion-20260920/figures"
ES_RH = ROOT / "research/incoming/es-rh-multi-20260920/figures"
INTEGRAL = ROOT / "research/incoming/es-turn07-integral-completion-20260920/figures"
DEFINING = ROOT / "research/incoming/es-defining-prime-continuation-20260920/figures"
CONT_B = ROOT / "research/incoming/es-rh-continuation-b-20260920/figures"
BRIDGE.mkdir(parents=True, exist_ok=True)
LOCAL.mkdir(parents=True, exist_ok=True)
CAPACITY.mkdir(parents=True, exist_ok=True)
ES_RH.mkdir(parents=True, exist_ok=True)
INTEGRAL.mkdir(parents=True, exist_ok=True)
DEFINING.mkdir(parents=True, exist_ok=True)
CONT_B.mkdir(parents=True, exist_ok=True)

INK = "#17202a"
BLUE = "#2166ac"
ORANGE = "#b35806"
GREEN = "#1b7837"
PURPLE = "#762a83"
MUTED = "#65737e"
LIGHT_BLUE = "#dbeaf5"
LIGHT_ORANGE = "#f6e3ce"
LIGHT_GREEN = "#ddefdf"
LIGHT_PURPLE = "#eadcf0"


def save(fig: plt.Figure, directory: Path, stem: str) -> None:
    fig.savefig(directory / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(directory / f"{stem}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def node(ax, xy, label, edge=INK, face="white", radius=0.22, fontsize=11):
    ax.add_patch(Circle(xy, radius, facecolor=face, edgecolor=edge, lw=1.6))
    ax.text(*xy, label, ha="center", va="center", fontsize=fontsize, color=INK)


def arrow(ax, start, end, label=None, color=INK, rad=0.0, label_offset=(0, 0)):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12,
                                lw=1.4, color=color,
                                connectionstyle=f"arc3,rad={rad}"))
    if label:
        mx = (start[0] + end[0]) / 2 + label_offset[0]
        my = (start[1] + end[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center", fontsize=10,
                color=color, bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def quartic_transform() -> None:
    fig, ax = plt.subplots(figsize=(10.8, 6.4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Exact elementary transform: literal roots to reciprocal suspension",
                 fontsize=15, weight="normal", color=INK, pad=12)

    rows = [(5.7, ["$p$", "$x_1$", "$x_2$", "$x_3$"]),
            (3.65, ["$1$", "$t_1$", "$t_2$", "$t_3$"]),
            (1.55, ["$\\infty$", "$t_1$", "$t_2$", "$t_3$"])]
    xs = [1.7, 3.2, 4.7, 6.2]
    faces = [LIGHT_ORANGE, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE]
    for (yy, labels) in rows:
        for xx, lab, fc in zip(xs, labels, faces):
            node(ax, (xx, yy), lab, edge=ORANGE if xx == xs[0] else BLUE, face=fc)

    ax.text(0.2, 5.7, "$H_{ES}$", fontsize=12, color=INK, va="center")
    ax.text(0.08, 3.65, "after inversion", fontsize=9.5, color=INK, va="center")
    ax.text(0.2, 1.55, "$H_{rec}$", fontsize=12, color=INK, va="center")
    ax.text(3.95, 4.82, "$t_i=p/x_i$", fontsize=11, ha="center", color=INK)
    arrow(ax, (3.95, 5.40), (3.95, 3.93), "$T\\mapsto p/T$", color=PURPLE,
          label_offset=(1.05, 0))
    arrow(ax, (3.95, 3.37), (3.95, 1.84), "delete marked $1$; insert $\\infty$",
          color=GREEN, label_offset=(1.55, 0))

    box = FancyBboxPatch((7.05, 4.25), 4.55, 2.0, boxstyle="round,pad=0.15",
                         facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.2)
    ax.add_patch(box)
    ax.text(9.325, 5.78,
            "$H_{rec}(U,V)=\\dfrac{1}{u_4}\\dfrac{V}{U-V}H_{ES}(pV,U)$",
            ha="center", va="center", fontsize=11, color=INK)
    ax.text(9.325, 5.12,
            "$=V\\prod_{i=1}^3(U-(p/x_i)V)$",
            ha="center", va="center", fontsize=11, color=INK)
    ax.text(9.325, 4.58, "EZ28C: exact identity, including sign and scale",
            ha="center", va="center", fontsize=9.5, color=MUTED)

    box2 = FancyBboxPatch((7.05, 1.0), 4.55, 2.55, boxstyle="round,pad=0.15",
                          facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.2)
    ax.add_patch(box2)
    ax.text(9.325, 3.15, "Information retained / lost", ha="center", fontsize=11,
            color=INK)
    ax.text(7.3, 2.66, "$e_2=125u_4^2(u_3-5u_0u_4)/u_3^4$", fontsize=10, color=INK)
    ax.text(7.3, 2.22, "$e_3=625u_0u_4^3/u_3^4$", fontsize=10, color=INK)
    ax.text(7.3, 1.76, "fibre: $(p,x_i)\\mapsto(\\lambda p,\\lambda x_i)$",
            fontsize=10, color=INK)
    ax.text(7.3, 1.32, "projective signs: $8\\leftrightarrow8$; affine chart: $8\\to7$",
            fontsize=10, color=INK)

    ax.text(0.25, 0.35,
            "Schematic of the proved projective root operation; horizontal spacing is not a metric.",
            fontsize=9.5, color=MUTED)
    save(fig, BRIDGE, "quartic-elementary-transform")


def local_fibres() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.8), sharey=True)
    fig.suptitle("Prime-local reciprocal fibres retain the E/M arithmetic type",
                 fontsize=15, weight="normal", color=INK)
    for ax in axes:
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6.2)
        ax.axis("off")

    ax = axes[0]
    ax.set_title("Exterior channel E", fontsize=12, color=INK)
    ax.text(0.25, 5.45, "root reductions: $(0,0,4)$", fontsize=11, color=INK)
    node(ax, (1.35, 4.4), "$t_1$", BLUE, LIGHT_BLUE)
    node(ax, (2.25, 4.4), "$t_2$", BLUE, LIGHT_BLUE)
    node(ax, (4.65, 4.4), "$t_3$", GREEN, LIGHT_GREEN)
    ax.text(1.8, 3.9, "same residue $0$", ha="center", fontsize=9.5, color=MUTED)
    ax.text(4.65, 3.9, "residue $4$", ha="center", fontsize=9.5, color=MUTED)
    for x0 in (1.35, 2.25):
        arrow(ax, (x0, 4.13), (x0 - .32, 3.25), "$K_{ram}$", BLUE,
              label_offset=(-.35, 0))
        arrow(ax, (x0, 4.13), (x0 + .32, 3.25), None, BLUE)
    arrow(ax, (4.65, 4.13), (4.30, 3.25), "$\\mathbb{Q}_p$", GREEN,
          label_offset=(-.38, 0))
    arrow(ax, (4.65, 4.13), (5.00, 3.25), "$\\mathbb{Q}_p$", GREEN,
          label_offset=(.38, 0))
    node(ax, (3.0, 2.35), "$\\infty$", ORANGE, LIGHT_ORANGE)
    ax.text(0.25, 1.58, "$\\mathcal{A}_E=\\mathbb{Q}_p^3\\times K_{ram}^2$",
            fontsize=11, color=INK)
    ax.text(0.25, 1.10, "$v_p(d_1,d_2,d_3)=(1,1,0)$", fontsize=10, color=INK)
    ax.text(0.25, 0.62, "$\\mathcal{O}_E=\\{z:z_1\\equiv z_2\\ (\\mathrm{mod}\\ p)\\}$; index $p$",
            fontsize=10, color=INK)

    ax = axes[1]
    ax.set_title("Middle channel M", fontsize=12, color=INK)
    ax.text(0.25, 5.45, "three distinct root reductions", fontsize=11, color=INK)
    node(ax, (1.2, 4.4), "$t_1$", GREEN, LIGHT_GREEN)
    node(ax, (3.0, 4.4), "$t_2$", BLUE, LIGHT_BLUE)
    node(ax, (4.8, 4.4), "$t_3$", BLUE, LIGHT_BLUE)
    arrow(ax, (1.2, 4.13), (.85, 3.25), "$\\mathbb{Q}_p$", GREEN,
          label_offset=(-.34, 0))
    arrow(ax, (1.2, 4.13), (1.55, 3.25), "$\\mathbb{Q}_p$", GREEN,
          label_offset=(.34, 0))
    for x0 in (3.0, 4.8):
        arrow(ax, (x0, 4.13), (x0 - .28, 3.25), "$K_{unr}$", BLUE,
              label_offset=(-.42, 0))
        arrow(ax, (x0, 4.13), (x0 + .28, 3.25), None, BLUE)
    node(ax, (3.0, 2.35), "$\\infty$", ORANGE, LIGHT_ORANGE)
    ax.text(0.25, 1.58, "$\\mathcal{A}_M=\\mathbb{Q}_p^3\\times K_{unr}^2$",
            fontsize=11, color=INK)
    ax.text(0.25, 1.10, "all $d_i$ are units; one square, two nonsquares",
            fontsize=10, color=INK)
    ax.text(0.25, 0.62, "$\\mathcal{O}_M=\\mathbb{Z}_p^3$; maximal order",
            fontsize=10, color=INK)

    fig.text(0.5, 0.015,
             "Each side has seven geometric affine branches and exactly three $\\mathbb{Q}_p$-points; the field and integral-order types differ.",
             ha="center", fontsize=9.5, color=MUTED)
    fig.tight_layout(rect=(0, .045, 1, .93))
    save(fig, LOCAL, "prime-local-fibre-comparison")


def fixed_q_example() -> None:
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    ax.set_title("Complete fixed-$Q$ fibre at $p=41161$, $h=11$, $j=3$",
                 fontsize=15, weight="normal", color=INK, pad=12)

    ax.text(0.4, 5.35, "$U\\mid j^2=9$", fontsize=12, color=INK)
    positions = {1: (1.5, 4.1), 3: (3.35, 4.1), 9: (5.2, 4.1)}
    for u, pos in positions.items():
        chosen = u == 3
        node(ax, pos, f"$U={u}$", GREEN if chosen else MUTED,
             LIGHT_GREEN if chosen else "#f0f2f3", radius=.38, fontsize=10.5)
        residue = (41161 + 4*u) % 11
        ax.text(pos[0], 3.48, f"${residue}$", ha="center",
                fontsize=10, color=GREEN if chosen else MUTED)
    ax.text(2.95, 3.05, "residues of $(p+4U)\\ (\\mathrm{mod}\\ 11)$ beneath the three divisors",
            ha="center",
            fontsize=9.5, color=MUTED)
    arrow(ax, (1.9, 4.1), (2.93, 4.1), None, color=MUTED)
    arrow(ax, (3.77, 4.1), (4.78, 4.1), None, color=MUTED)

    box = FancyBboxPatch((6.35, 2.55), 5.2, 2.65, boxstyle="round,pad=0.16",
                         facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.2)
    ax.add_patch(box)
    ax.text(8.95, 4.78, "Unique fixed-$Q$ target ($U=3$)", ha="center",
            fontsize=11, color=INK)
    ax.text(6.65, 4.25, "$R_U=(p+4U)/h=3743,\\quad A_U=(p+R_U)/4=11226$",
            fontsize=10, color=INK)
    ax.text(6.65, 3.72, "$(h_U,r_U,s_U,\\lambda_U)=(3,1,3742,1)$",
            fontsize=10, color=INK)
    ax.text(6.65, 3.18,
            "$4/41161=1/11226+1/462073386+1/123483$",
            fontsize=10, color=INK)
    arrow(ax, (5.6, 4.1), (6.30, 4.1), "EZ28Q--S", color=GREEN,
          label_offset=(0, .52))

    box2 = FancyBboxPatch((0.5, .48), 5.15, 1.65, boxstyle="round,pad=0.14",
                          facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.2)
    ax.add_patch(box2)
    ax.text(3.075, 1.75, "Why this strictly extends the selected square word",
            ha="center", fontsize=10.5, color=INK)
    ax.text(.78, 1.24, "$\\alpha=-4c^2=-100$, so $c=5$ but $5\\nmid j=3$.",
            fontsize=9.5, color=INK)
    ax.text(.78, .88, "Selected square word unavailable;", fontsize=9.2, color=INK)
    ax.text(.78, .60, "nonsquare $U=3$ still returns.", fontsize=9.2, color=INK)

    ax.text(6.45, 1.55,
            "General theorem: $\\mathcal{U}_{p,h}=\\{U>0:U\\mid j^2,\\ h\\mid p+4U\\}$",
            fontsize=9.5, color=INK)
    ax.text(6.45, 1.02, "$\\mathcal{U}_{p,h}\\longleftrightarrow\\{$ all original M states with $Q=h\\}$",
            fontsize=9.5, color=INK)
    ax.text(6.45, .52, "This fibre starts from an existing E state; it does not force occupancy.",
            fontsize=9.5, color=MUTED)
    save(fig, LOCAL, "fixed-q-fibre-41161")


def odd_divisor_crossing() -> None:
    """Plot the exact positive-real line on which the odd divisor changes sign."""

    def q(w):
        return (
            319186534400*w**6 + 12383961481216*w**5
            - 26262983737344*w**4 - 1257389244416*w**3
            + 1383887871744*w**2 + 2670303991200*w - 90309375
        )

    ws = np.linspace(1e-6, 1e-4, 1000)
    values = -8*q(ws)/(144*ws - 65)**6
    fig, ax = plt.subplots(figsize=(9.2, 5.0))
    ax.plot(ws, values, color=PURPLE, lw=2.0)
    ax.axhline(0, color=INK, lw=0.8)
    ax.scatter([1e-6, 1e-4], [values[0], values[-1]],
               color=[GREEN, ORANGE], zorder=4)
    ax.set_xlabel(r"$w=d^2$")
    ax.set_ylabel(r"$\mathfrak{D}_{\mathrm{odd}}\circ\Theta$")
    ax.set_title("The odd receiving divisor meets the positive-real ES locus")
    ax.grid(alpha=0.22)
    ax.text(0.02, 0.96,
            r"$p/x=1/4-d,\quad p/y=1/4+d,\quad p/z=7/2,\quad p=1$",
            transform=ax.transAxes, va="top", fontsize=10,
            bbox=dict(facecolor="white", edgecolor="0.8", alpha=.9))
    ax.text(0.02, 0.84,
            r"$\mathfrak{D}_{\mathrm{odd}}\circ\Theta=-8Q(w)/(144w-65)^6$",
            transform=ax.transAxes, va="top", fontsize=10)
    ax.text(0.02, 0.76,
            r"exact signs: $Q(10^{-6})<0<Q(10^{-4})$",
            transform=ax.transAxes, va="top", fontsize=10)
    ax.text(0.50, 0.03,
            "The plotted curve is numerical; the endpoint signs and existence interval are exact.",
            transform=ax.transAxes, ha="center", fontsize=9, color=MUTED)
    save(fig, BRIDGE, "odd-receiver-positive-real-crossing")


def raw_tetrahedron() -> None:
    """Render the exact three-dimensional ES-aligned raw-cell tetrahedron."""

    sqrt3 = np.sqrt(3.0)
    # Plot order is (X,W,Y); the exact spatial coordinates are (X,Y,W).
    apex = np.array([0.0, 0.0, 5.0/4.0])
    face = np.array([
        [2.0, 0.0, 3.0/2.0],
        [-1.0, sqrt3, 3.0/2.0],
        [-1.0, -sqrt3, 3.0/2.0],
    ])
    centroid = face.mean(axis=0)
    fig = plt.figure(figsize=(9.6, 5.3))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.add_collection3d(Poly3DCollection([face], facecolors=LIGHT_BLUE,
                                         edgecolors="0.35", linewidths=1.2,
                                         alpha=.36))
    labels = [r"$v_0$", r"$v_+$", r"$v_-$"]
    colours = ["#c43c35", BLUE, GREEN]
    for k in range(3):
        j = (k + 1) % 3
        ax.plot([face[k,0], face[j,0]], [face[k,1], face[j,1]],
                [face[k,2], face[j,2]], color="0.35", lw=1.1)
        ax.plot([apex[0], face[k,0]], [apex[1], face[k,1]],
                [apex[2], face[k,2]], color="0.45", lw=1.0)
        ax.scatter(*face[k], s=65, color=colours[k], depthshade=False)
        ax.text(face[k,0], face[k,1], face[k,2] + .018, labels[k], fontsize=10)
    ax.scatter(*apex, s=80, color=ORANGE, depthshade=False)
    ax.text(apex[0], apex[1], apex[2] - .018, r"$v_\ast$", fontsize=10)
    ax.scatter(*centroid, s=32, color=INK, depthshade=False)
    ax.plot([apex[0], centroid[0]], [apex[1], centroid[1]],
            [apex[2], centroid[2]], color="#8b1a1a", lw=2.0)
    ax.set_xlabel("$X$")
    ax.set_ylabel("$W$")
    ax.set_zlabel("$Y$")
    ax.set_zlim(1.19, 1.56)
    ax.set_zticks([1.25, 1.5])
    ax.set_zticklabels([r"$5/4$", r"$3/2$"])
    ax.set_box_aspect((4.3, 3.9, .42))
    ax.view_init(elev=20, azim=-56)
    ax.grid(False)
    ax.set_title("Exact spatial tetrahedron", loc="left")

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.axis("off")
    ax2.text(.02, .92, r"$p_\ast=(0,5/4,0)$", fontsize=11)
    ax2.text(.02, .82, r"$p_0=(2,3/2,0)$", fontsize=11)
    ax2.text(.02, .72, r"$p_+=(-1,3/2,\sqrt{3})$", fontsize=11)
    ax2.text(.02, .62, r"$p_-=(-1,3/2,-\sqrt{3})$", fontsize=11)
    ax2.text(.02, .49, r"$\bar p_{\rm face}-p_\ast=(0,1/4,0)$", fontsize=11,
             color="#8b1a1a")
    ax2.text(.02, .37, r"face edges: $2\sqrt{3}$", fontsize=10.5)
    ax2.text(.02, .28, r"apex edges: $\sqrt{65}/4$", fontsize=10.5)
    ax2.text(.02, .19, r"volume: $\sqrt{3}/4$", fontsize=10.5)
    ax2.text(.02, .07,
             "These are the retained spatial coordinates after the exact\n"
             "raw-cell to ES-aligned Lorentz transport; no Euclidean\n"
             "regularity is asserted.", fontsize=9.2, color=MUTED)
    fig.suptitle("Fable raw cells transported into the Erdős–Straus spatial slice",
                 fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, .93))
    save(fig, BRIDGE, "fable-es-raw-tetrahedron-3d")


def fixed_input_cover() -> None:
    """Show the exact rank-2 plus rank-6 sheet decomposition and actions."""

    fig, ax = plt.subplots(figsize=(11.2, 6.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Fixed-$p$ signed cover: rank $2+6$, monodromy order $48$",
                 fontsize=15, weight="normal", color=INK, pad=12)

    prime_box = FancyBboxPatch((.45, 2.55), 2.25, 2.7, boxstyle="round,pad=.15",
                               facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.4)
    denom_box = FancyBboxPatch((3.35, 1.15), 8.1, 5.35, boxstyle="round,pad=.15",
                               facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.4)
    ax.add_patch(prime_box)
    ax.add_patch(denom_box)
    ax.text(1.575, 4.87, "marked prime root", ha="center", fontsize=11, color=INK)
    ax.text(7.4, 6.13, "three denominator roots", ha="center", fontsize=11, color=INK)

    node(ax, (1.15, 3.75), "$p,+$", ORANGE, "white", radius=.30, fontsize=10)
    node(ax, (2.02, 3.75), "$p,-$", ORANGE, "white", radius=.30, fontsize=10)
    arrow(ax, (1.47, 3.75), (1.70, 3.75), "$\\tau_p$", ORANGE,
          label_offset=(0, .43))

    x_positions = [4.45, 7.35, 10.25]
    labels = ["$x$", "$y$", "$z$"]
    for xpos, label in zip(x_positions, labels):
        node(ax, (xpos, 4.5), label + "$,+$", BLUE, "white", radius=.31, fontsize=10)
        node(ax, (xpos, 2.65), label + "$,-$", BLUE, "white", radius=.31, fontsize=10)
        arrow(ax, (xpos, 4.16), (xpos, 2.99), None, PURPLE)

    arrow(ax, (4.82, 5.05), (6.98, 5.05), "$S_3$", GREEN,
          rad=.08, label_offset=(0, .35))
    arrow(ax, (7.72, 5.05), (9.88, 5.05), None, GREEN, rad=.08)
    arrow(ax, (9.88, 2.05), (7.72, 2.05), "denominator pair flips", PURPLE,
          rad=.08, label_offset=(0, -.35))
    arrow(ax, (6.98, 2.05), (4.82, 2.05), None, PURPLE, rad=.08)

    ax.text(.72, 2.93, "rank $2$", fontsize=10.5, color=ORANGE)
    ax.text(10.05, 1.48, "rank $6$", fontsize=10.5, color=BLUE)
    ax.text(.55, .70,
            "$G_p=\\{(\\sigma,\\pi):\\pi(p)=p,\\ \\prod_j\\sigma_j=\\operatorname{sgn}\\pi\\}$,"
            "  $|G_p|=8\\cdot6=48$",
            fontsize=10.5, color=INK)
    ax.text(.55, .24,
            "deck group: independent prime-pair and denominator-sheet reversals"
            " $\\cong C_2\\times C_2$",
            fontsize=10, color=MUTED)
    save(fig, BRIDGE, "fixed-input-cover-decomposition")


def finite_boundary_fibre() -> None:
    """Show the finite eta-completion, local length-four fibre, and typed map."""

    fig, ax = plt.subplots(figsize=(11.4, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.4)
    ax.axis("off")
    ax.set_title("Finite inverse-derivative completion at a double root",
                 fontsize=15, weight="normal", color=INK, pad=12)

    for xpos, ypos, label in [
        (1.0, 5.55, "$r_1,+$"), (1.0, 4.65, "$r_1,-$"),
        (3.15, 5.55, "$r_2,+$"), (3.15, 4.65, "$r_2,-$"),
    ]:
        node(ax, (xpos, ypos), label, BLUE, LIGHT_BLUE, radius=.30, fontsize=9.5)
        arrow(ax, (xpos + .33, ypos), (5.05, 5.10), None, BLUE)

    local_box = FancyBboxPatch((5.10, 4.15), 3.0, 1.92, boxstyle="round,pad=.15",
                               facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.4)
    ax.add_patch(local_box)
    ax.text(6.60, 5.68, "double-root fibre", ha="center", fontsize=11, color=INK)
    ax.text(6.60, 5.14, "$\\eta^2=2g_0\\varepsilon$", ha="center",
            fontsize=11, color=INK)
    ax.text(6.60, 4.62, "$\\mathbb{C}[\\eta]/(\\eta^4)$: length $4$",
            ha="center", fontsize=10.5, color=INK)

    pole_box = FancyBboxPatch((8.65, 4.15), 2.85, 1.92, boxstyle="round,pad=.15",
                              facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.4)
    ax.add_patch(pole_box)
    ax.text(10.075, 5.68, "original inverse", ha="center", fontsize=11, color=INK)
    ax.text(10.075, 5.14, "$q_1=\\eta^{-1}$", ha="center", fontsize=11, color=INK)
    ax.text(10.075, 4.62, "$|\\eta|\\,\\|Fq\\|\\to\\sqrt{G_{11}}$",
            ha="center", fontsize=10, color=INK)
    arrow(ax, (8.10, 5.10), (8.62, 5.10), "meromorphic map", ORANGE,
          label_offset=(0, .45))

    es_box = FancyBboxPatch((.65, 1.03), 4.0, 2.15, boxstyle="round,pad=.15",
                            facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.3)
    pair_box = FancyBboxPatch((7.35, 1.03), 4.0, 2.15, boxstyle="round,pad=.15",
                              facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    ax.add_patch(es_box)
    ax.add_patch(pair_box)
    ax.text(2.65, 2.76, "ES boundary family", ha="center", fontsize=11, color=INK)
    ax.text(2.65, 2.18, "$(p;p,2p/5,2p)$", ha="center", fontsize=10.5, color=INK)
    ax.text(2.65, 1.56, "$\\eta_{ES}^2=(3p/11)\\varepsilon_{ES}$",
            ha="center", fontsize=10.5, color=INK)
    ax.text(9.35, 2.76, "paired-root auxiliary", ha="center", fontsize=11, color=INK)
    ax.text(9.35, 2.18, "$r_\\pm=1/2\\pm i\\gamma$", ha="center",
            fontsize=10.5, color=INK)
    ax.text(9.35, 1.56, "$\\eta_{pair}^2=4\\gamma^2\\varepsilon_{pair}$",
            ha="center", fontsize=10.5, color=INK)
    arrow(ax, (4.70, 2.08), (7.30, 2.08),
          "$\\varepsilon\\mapsto\\varepsilon,\\quad\\eta\\mapsto c\\eta$",
          GREEN, label_offset=(0, .48))
    ax.text(6.0, .62, "$c^2=3p/(44\\gamma^2)$; local algebras and centred actions only",
            ha="center", fontsize=9.8, color=MUTED)
    save(fig, BRIDGE, "finite-boundary-local-fibre")


def capacity_partition() -> None:
    """Draw the proved inverse classification of one fixed-target word."""

    fig, ax = plt.subplots(figsize=(11.4, 6.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")
    ax.set_title("Exact inverse classification of a fixed-target cofactor word",
                 fontsize=15, weight="normal", color=INK, pad=12)

    source = FancyBboxPatch((3.0, 6.12), 6.0, .92, boxstyle="round,pad=.14",
                            facecolor="white", edgecolor=INK, lw=1.4)
    ax.add_patch(source)
    ax.text(6.0, 6.58,
            r"$h=4j-1>t,\quad W\mid j^2,\quad W\equiv t\ (\mathrm{mod}\ h)$",
            ha="center", va="center", fontsize=12, color=INK)

    canonical = FancyBboxPatch((.45, 3.58), 2.85, 1.68, boxstyle="round,pad=.14",
                               facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.4)
    inverse = FancyBboxPatch((4.0, 3.25), 4.0, 2.35, boxstyle="round,pad=.14",
                             facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.4)
    ax.add_patch(canonical)
    ax.add_patch(inverse)
    ax.text(1.875, 4.78, "canonical", ha="center", fontsize=11, color=INK)
    ax.text(1.875, 4.30, r"$W=t$", ha="center", fontsize=12, color=INK)
    ax.text(1.875, 3.84, r"exactly when $t\mid j^2$", ha="center",
            fontsize=10, color=INK)
    ax.text(6.0, 5.17, "exact inverse data", ha="center", fontsize=11, color=INK)
    ax.text(6.0, 4.63, r"$n=(W-t)/h,\quad V=j^2/W$", ha="center",
            fontsize=11, color=INK)
    ax.text(6.0, 4.10, r"$\ell=j-4nV$", ha="center", fontsize=12, color=INK)
    ax.text(6.0, 3.59, r"$16tV=1+(4\ell+1)h$", ha="center",
            fontsize=10.5, color=INK)

    companion = FancyBboxPatch((8.72, 4.35), 2.82, 1.45, boxstyle="round,pad=.14",
                               facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.4)
    finite = FancyBboxPatch((8.30, 1.16), 3.65, 2.37, boxstyle="round,pad=.14",
                            facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.4)
    ax.add_patch(companion)
    ax.add_patch(finite)
    ax.text(10.13, 5.39, r"$\ell=0$: companion", ha="center", fontsize=11, color=INK)
    ax.text(10.13, 4.90, r"$W=4tj$", ha="center", fontsize=12, color=INK)
    ax.text(10.13, 4.54, r"exactly when $4t\mid j$", ha="center",
            fontsize=9.7, color=INK)
    ax.text(10.125, 3.12, r"$\ell>0$: finite word", ha="center",
            fontsize=11, color=INK)
    ax.text(10.125, 2.61, r"$w=\ell^2/V,\quad w\mid\ell^2$", ha="center",
            fontsize=10.5, color=INK)
    ax.text(10.125, 2.13, r"$t=(4\ell+1)n+w$", ha="center",
            fontsize=10.5, color=INK)
    ax.text(10.125, 1.65,
            r"$1\leq\ell\leq(t-2)/4,\quad h\leq t^2-3t+1$",
            ha="center", fontsize=9.8, color=INK)

    arrow(ax, (4.35, 6.10), (2.55, 5.30), "$W=t$", GREEN,
          label_offset=(-.15, .22))
    arrow(ax, (6.0, 6.10), (6.0, 5.62), r"$W\ne t$", BLUE,
          label_offset=(.82, 0))
    arrow(ax, (8.03, 4.80), (8.67, 5.02), r"$\ell=0$", ORANGE,
          label_offset=(0, .35))
    arrow(ax, (7.55, 3.28), (8.50, 2.95), r"$\ell>0$", PURPLE,
          label_offset=(0, -.35))

    ax.text(.55, .50,
            "The three outputs are disjoint and the displayed formulas recover every label. "
            "The quadratic bound applies only to the finite branch.",
            fontsize=9.7, color=MUTED)
    save(fig, CAPACITY, "fixed-target-capacity-partition")


def capacity_sharp_bound() -> None:
    """Plot every finite template through t=120 against the proved bound."""

    points: list[tuple[int, int]] = []
    equality: list[tuple[int, int]] = []
    for t in range(1, 121):
        for ell in range(1, (t - 2) // 4 + 1):
            for w in range(1, ell * ell + 1):
                if (ell * ell) % w:
                    continue
                denominator = 4 * ell + 1
                if t <= w or (t - w) % denominator:
                    continue
                n = (t - w) // denominator
                v = ell * ell // w
                j = ell + 4 * n * v
                h = 4 * j - 1
                if h <= t:
                    continue
                points.append((t, h))
                if h == t * t - 3 * t + 1:
                    equality.append((t, h))

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.4),
                             gridspec_kw={"width_ratios": [1.55, 1]})
    ts = np.arange(1, 121)
    bound = ts * ts - 3 * ts + 1
    ax = axes[0]
    if points:
        ax.scatter([p[0] for p in points], [p[1] for p in points], s=14,
                   color=BLUE, alpha=.62, label="all finite words")
    ax.plot(ts, bound, color=PURPLE, lw=2.0,
            label=r"proved boundary $h=t^2-3t+1$")
    if equality:
        ax.scatter([p[0] for p in equality], [p[1] for p in equality],
                   s=24, color=ORANGE, zorder=4, label="equality family")
    ax.set_xlabel(r"shape coefficient $t$")
    ax.set_ylabel(r"original grade $h=4j-1$")
    ax.set_title(r"Complete finite templates, $t\leq120$")
    ax.grid(alpha=.2)
    ax.legend(frameon=False, fontsize=9)

    ax = axes[1]
    ax.axis("off")
    ax.text(.04, .90, "Sharp original prime example", fontsize=12, color=INK)
    ax.text(.04, .79, r"$t=6,\quad j=5,\quad h=19$", fontsize=11, color=INK)
    ax.text(.04, .68, r"$\operatorname{Div}(j^2)=\{1,5,25\}$", fontsize=11,
            color=INK)
    ax.text(.04, .57, r"residues mod $19$: $1,5,6$", fontsize=11, color=INK)
    ax.text(.04, .46, r"canonical $W=6$ absent; finite $W=25$ present",
            fontsize=10.5, color=GREEN)
    ax.text(.04, .32, r"$p=825241$", fontsize=11, color=INK)
    ax.text(.04, .22,
            r"$4/p=1/217170+1/(825241\cdot43434)+1/(825241\cdot5)$",
            fontsize=9.7, color=INK)
    ax.text(.04, .07,
            "Blue points are an exact finite enumeration of the proved templates; "
            "the boundary curve is the theorem, not a fit.",
            fontsize=9.1, color=MUTED, wrap=True)
    fig.suptitle("Sharp capacity boundary and its nonsquare channel return",
                 fontsize=14.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, .94))
    save(fig, CAPACITY, "capacity-sharp-bound")


def positive_real_rank_crossing() -> None:
    """Show the exact ES ray and the separately certified frame crossing."""

    t = np.linspace(203.0, 700.0, 1000)
    x = t / (4.0 * t - 402.0)
    y = t / 202.0
    z = t / 200.0
    lo = 3520743 / 6176
    hi = 3562358 / 6249
    locator = (lo + hi) / 2

    coeffs = np.array([
        2359424, -2380972032, -125022004322048,
        199766203719977640, -126442260595802541476,
        41598937953326627478150, -7385542427424681354996253,
        544226493322473956433710982,
        40187872427398803311778426564,
        -12845040782988159530278491608280,
        1219651834158063698018605839792000,
        -55076685665576109738730352971200000,
        998076020859413480649547526400000000,
    ], dtype=np.float64)
    tf = np.linspace(551.0, 651.0, 1200)
    fvals = np.polyval(coeffs, tf)
    fvals /= np.max(np.abs(fvals))

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.5))
    ax = axes[0]
    ax.plot(t, x, color=GREEN, lw=2.0, label=r"$x/p=t/(4t-402)$")
    ax.axhline(1.0, color=INK, lw=1.2, label=r"$p/p=1$")
    ax.plot(t, y, color=BLUE, lw=2.0, label=r"$y/p=t/202$")
    ax.plot(t, z, color=ORANGE, lw=2.0, label=r"$z/p=t/200$")
    ax.axvline(locator, color=PURPLE, lw=1.5, ls="--")
    ax.set_xlim(203, 700)
    ax.set_ylim(0, 3.65)
    ax.set_xlabel(r"parameter $t>202$")
    ax.set_ylabel("literal roots divided by $p$")
    ax.set_title(r"$0<x<p<y<z$ throughout the ray")
    ax.grid(alpha=.20)
    ax.legend(frameon=False, fontsize=8.7, loc="upper left")

    ax = axes[1]
    ax.plot(tf, fvals, color=PURPLE, lw=2.0)
    ax.axhline(0, color=INK, lw=.8)
    ax.axvspan(lo, hi, color=ORANGE, alpha=.45,
               label="exact rational isolating interval")
    ax.set_xlim(551, 651)
    ax.set_xlabel(r"parameter $t$")
    ax.set_ylabel(r"scaled $f(t)$ (locator only)")
    ax.set_title("Unique simple zero and rank-three receiver")
    ax.grid(alpha=.20)
    ax.legend(frameon=False, fontsize=8.7, loc="upper right")
    ax.text(.04, .18,
            r"$3520743/6176<t_*<3562358/6249$" "\n"
            r"$\operatorname{rank}O(t_*)=3$; $A\,\operatorname{Disc}(h)\ne0$",
            transform=ax.transAxes, fontsize=9.4,
            bbox=dict(facecolor="white", edgecolor="0.8", alpha=.93))
    ax.text(.04, .035,
            r"Integral roots: $N=S^6F\in\mathbb{Z}$.  Either $N=0$, or"
            "\n" r"$|\det O|\geq4/S^3$ and $\|O^{-1}\|_2\leq41^3S^{12}/4$.",
            transform=ax.transAxes, fontsize=8.2, color=MUTED)
    fig.suptitle("Positive-real Erdős–Straus solutions cross the extra odd-frame divisor",
                 fontsize=14.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, .93))
    save(fig, ES_RH, "positive-real-receiving-divisor")


def residue_trace_factorization() -> None:
    """Draw the exact perfect-residue to degenerate-trace factorization."""

    fig, ax = plt.subplots(figsize=(11.6, 6.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.4)
    ax.axis("off")
    ax.set_title("Trace degeneration is multiplication by $2\\eta^3$",
                 fontsize=15, color=INK, pad=12)

    left = FancyBboxPatch((.45, 4.55), 3.35, 1.75, boxstyle="round,pad=.15",
                          facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.4)
    middle = FancyBboxPatch((4.35, 4.55), 3.15, 1.75, boxstyle="round,pad=.15",
                            facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.4)
    right = FancyBboxPatch((8.05, 4.55), 3.45, 1.75, boxstyle="round,pad=.15",
                           facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.4)
    for box in (left, middle, right):
        ax.add_patch(box)
    ax.text(2.125, 5.88, "perfect residue pairing", ha="center", fontsize=11, color=INK)
    ax.text(2.125, 5.35, r"$\mathcal{J}$ has off-diagonal blocks $J_h$",
            ha="center", fontsize=11, color=INK)
    ax.text(2.125, 4.86, r"$\det\mathcal{J}=A^{-8}$", ha="center", fontsize=10.5, color=INK)
    ax.text(5.925, 5.88, "exact algebra endomorphism", ha="center", fontsize=11, color=INK)
    ax.text(5.925, 5.29, r"$M_{2\eta^3}$", ha="center", fontsize=15, color=PURPLE)
    ax.text(5.925, 4.92, "unit off the discriminant;", ha="center",
            fontsize=8.9, color=INK)
    ax.text(5.925, 4.68, "rank $1$ at a collision", ha="center",
            fontsize=8.9, color=INK)
    ax.text(9.775, 5.88, "trace pairing", ha="center", fontsize=11, color=INK)
    ax.text(9.775, 5.34, r"$\operatorname{Tr}(M_f)=\Lambda(2\eta^3f)$",
            ha="center", fontsize=10.5, color=INK)
    ax.text(9.775, 4.86, r"$\det=256\,\operatorname{Disc}(h)^3/A^{14}$",
            ha="center", fontsize=9.6, color=INK)
    arrow(ax, (3.83, 5.42), (4.31, 5.42), "compose", PURPLE,
          label_offset=(0, .40))
    arrow(ax, (7.53, 5.42), (8.01, 5.42), "equals", ORANGE,
          label_offset=(0, .40))

    local = FancyBboxPatch((.65, 1.08), 4.6, 2.35, boxstyle="round,pad=.15",
                           facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    bridge = FancyBboxPatch((6.1, 1.08), 5.25, 2.35, boxstyle="round,pad=.15",
                            facecolor="white", edgecolor=INK, lw=1.3)
    ax.add_patch(local)
    ax.add_patch(bridge)
    ax.text(2.95, 3.00, "collision-local algebra", ha="center", fontsize=11, color=INK)
    ax.text(2.95, 2.47,
            r"$\mathbb{C}[\varepsilon,\eta]/(\varepsilon^m,\eta^2-mg_0\varepsilon^{m-1})$",
            ha="center", fontsize=10.2, color=INK)
    ax.text(2.95, 1.94, r"length $2m$; trace rank $1$ for $m\geq2$",
            ha="center", fontsize=10, color=INK)
    ax.text(2.95, 1.45, r"$m=2:\ \mathbb{C}[\eta]/(\eta^4)$",
            ha="center", fontsize=10, color=INK)
    ax.text(8.725, 3.00, "exact local ES/RH transport", ha="center", fontsize=11, color=INK)
    ax.text(8.725, 2.47,
            r"$\varepsilon_E\mapsto\varepsilon_R,\quad\eta_E\mapsto c\eta_R$",
            ha="center", fontsize=10.5, color=INK)
    ax.text(8.725, 1.94,
            r"residue unit $u_E=c^3[1+(2/(3p)+s i/\gamma)\varepsilon_E]$",
            ha="center", fontsize=9.7, color=INK)
    ax.text(8.725, 1.50,
            "This relates local auxiliary factors;\n"
            "it is not a global ES–zeta map.",
            ha="center", fontsize=8.9, color=MUTED)
    ax.text(6.0, .48,
            r"The original coordinate $q_1=\eta^{-1}$ remains meromorphic; the finite boundary does not cancel its metric divergence.",
            ha="center", fontsize=9.5, color=MUTED)
    save(fig, ES_RH, "residue-trace-factorization")


def residue_native_gram_bridge() -> None:
    """Show the exact multiplier and the relation defect for an ES polynomial."""

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.8))
    fig.suptitle("Residue duality reaches a native moment Gram through a typed multiplier",
                 fontsize=14.5, color=INK)
    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis("off")

    ax = axes[0]
    ax.set_title("Native monic orthogonal polynomial $p_n$", fontsize=11.5)
    node(ax, (1.6, 4.75), "$J_p$", GREEN, LIGHT_GREEN, radius=.48, fontsize=12)
    node(ax, (5.0, 4.75), "$M_q$", PURPLE, LIGHT_PURPLE, radius=.48, fontsize=12)
    node(ax, (8.4, 4.75), "$H_{n-1}$", BLUE, LIGHT_BLUE, radius=.58, fontsize=11)
    arrow(ax, (2.10, 4.75), (4.49, 4.75), "right multiplier", PURPLE,
          label_offset=(0, .47))
    arrow(ax, (5.51, 4.75), (7.79, 4.75), "$J_pq(C_p)$", BLUE,
          label_offset=(0, .47))
    ax.text(5.0, 3.63,
            r"$q(z)=\int\dfrac{p_n(z)-p_n(x)}{z-x}\,d\rho(x)$",
            ha="center", fontsize=10.3, color=INK)
    ax.text(5.0, 3.03, r"leading coefficient $=\mu_0$; $q(C_p)$ is a unit",
            ha="center", fontsize=9.5, color=INK)
    ax.text(5.0, 2.15,
            r"$\int\frac{d\rho}{x+a}+\frac{q(-a)}{p_n(-a)}"
            r"=\frac{1}{p_n(-a)^2}\int\frac{p_n(x)^2}{x+a}\,d\rho\geq0$",
            ha="center", fontsize=9.1, color=INK)
    ax.text(5.0, 1.15, r"hypothesis: $\operatorname{supp}\rho\subset[0,\infty)$, $a>0$",
            ha="center", fontsize=9.3, color=MUTED)

    ax = axes[1]
    ax.set_title("Arbitrary monic ES root polynomial $h$", fontsize=11.5)
    left = FancyBboxPatch((.55, 4.15), 3.0, 1.25, boxstyle="round,pad=.12",
                          facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.3)
    defect = FancyBboxPatch((.55, 2.05), 3.0, 1.25, boxstyle="round,pad=.12",
                            facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.3)
    total = FancyBboxPatch((6.45, 3.08), 2.95, 1.35, boxstyle="round,pad=.12",
                           facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    ax.add_patch(left); ax.add_patch(defect); ax.add_patch(total)
    ax.text(2.05, 4.77, r"$J_hk(C_h)$", ha="center", fontsize=12, color=INK)
    ax.text(2.05, 2.67, r"$\mathcal{D}_{ij}=\int h(x)\mathrm{quo}_h(x^{i+j})d\rho$",
            ha="center", fontsize=9.2, color=INK)
    ax.text(7.925, 3.75, r"native $H_{ij}$", ha="center", fontsize=12, color=INK)
    arrow(ax, (3.59, 4.70), (6.38, 3.92), "+", GREEN,
          label_offset=(0, .45))
    arrow(ax, (3.59, 2.70), (6.38, 3.58), "+", ORANGE,
          label_offset=(0, -.45))
    ax.text(5.0, 1.18,
            "The defect vanishes when $h=p_n$ by orthogonality.\n"
            "For a generic ES quartic it remains part of the exact map.",
            ha="center", fontsize=9.5, color=MUTED)
    fig.tight_layout(rect=(0, 0, 1, .92))
    save(fig, ES_RH, "residue-native-gram-bridge")


def integral_normalization_smith() -> None:
    """Display the exact E/M instances of the defining-prime Smith map."""

    fig, axes = plt.subplots(1, 2, figsize=(12.4, 7.0))
    fig.suptitle("The original integral signed order and its exact normalization",
                 fontsize=15, color=INK)
    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 9)
        ax.axis("off")

    panels = [
        (
            axes[0], "Exterior channel E", LIGHT_ORANGE, ORANGE,
            [("$p$", 1.7), ("$z=pZ$", 3.5), ("$x$", 6.5), ("$y$", 8.3)],
            r"$b=(1,1,0,0),\quad m=(0,0,0,0),\quad\epsilon=(1,1,0,0)$",
            r"$\mathrm{Smith}(\mathsf{C}_p)=(0,0,0,0,0,0,1,1)$",
            r"$\widetilde{\mathcal{E}}_p/\mathcal{E}_p\simeq(\mathbb{Z}_p/p)^2$",
            r"$[\widetilde{\mathcal{E}}_p:\mathcal{E}_p]=p^2$",
            r"$V_{\{p,z\}}=\mathbf{1}\oplus\chi_{pD_E}^{\oplus2},\quad a=2$",
        ),
        (
            axes[1], "Middle channel M", LIGHT_BLUE, BLUE,
            [("$p$", 1.3), ("$y=pY$", 3.0), ("$z=pZ$", 4.7), ("$x$", 8.0)],
            r"$b=(2,2,2,0),\quad m=(1,1,1,0),\quad\epsilon=(0,0,0,0)$",
            r"$\mathrm{Smith}(\mathsf{C}_p)=(0,0,0,1,1,2,2,3)$",
            r"$\widetilde{\mathcal{E}}_p/\mathcal{E}_p\simeq(\mathbb{Z}_p/p)^2"
            r"\oplus(\mathbb{Z}_p/p^2)^2\oplus\mathbb{Z}_p/p^3$",
            r"$[\widetilde{\mathcal{E}}_p:\mathcal{E}_p]=p^9$",
            r"$\det(1-T\mathrm{Frob}\mid V)=(1-T)^5$ or $(1-T)^3(1+T)^2$",
        ),
    ]

    for ax, title, face, edge, roots, valuation, smith, quotient, index, rep in panels:
        ax.set_title(title, fontsize=12.5, color=INK)
        for label, xpos in roots:
            marked = "p" in label or "=" in label
            node(ax, (xpos, 7.78), label, edge=edge if marked else GREEN,
                 face=face if marked else LIGHT_GREEN, radius=.34, fontsize=10)
        if title.startswith("Exterior"):
            ax.plot([1.7, 3.5], [7.28, 7.28], color=edge, lw=2.2)
            ax.text(2.6, 6.93, r"$\nu_p(p-z)=1$", ha="center", fontsize=9.5, color=edge)
        else:
            ax.plot([1.3, 4.7], [7.28, 7.28], color=edge, lw=2.2)
            ax.text(3.0, 6.93, "all three gaps have valuation $1$",
                    ha="center", fontsize=9.4, color=edge)

        top = FancyBboxPatch((.55, 5.2), 8.9, 1.05, boxstyle="round,pad=.13",
                             facecolor="white", edgecolor=MUTED, lw=1.0)
        ax.add_patch(top)
        ax.text(5.0, 5.88,
                r"$\mathsf{C}_p=\mathrm{diag}\!\left(V,\mathrm{diag}(p^{m_i})V\right)$",
                ha="center", fontsize=10.7, color=INK)
        ax.text(5.0, 5.47, valuation, ha="center", fontsize=9.1, color=INK)

        result = FancyBboxPatch((.55, 2.4), 8.9, 2.3, boxstyle="round,pad=.14",
                                facecolor=face, edgecolor=edge, lw=1.35)
        ax.add_patch(result)
        ax.text(5.0, 4.24, smith, ha="center", fontsize=9.3, color=INK)
        ax.text(5.0, 3.66, quotient, ha="center", fontsize=8.9, color=INK)
        ax.text(5.0, 3.08, index, ha="center", fontsize=10.2, color=INK)
        ax.text(5.0, 1.73, rep, ha="center", fontsize=8.9, color=INK)
        ax.text(5.0, .88,
                "Integral defect and ramification are computed from the same factors;\n"
                "neither invariant is substituted for the other.",
                ha="center", fontsize=8.6, color=MUTED)

    fig.tight_layout(rect=(0, 0, 1, .94))
    save(fig, INTEGRAL, "integral-normalization-smith")
    for ext in ("pdf", "png"):
        target = DEFINING / f"integral-normalization-smith.{ext}"
        target.write_bytes((INTEGRAL / f"integral-normalization-smith.{ext}").read_bytes())


def defining_prime_twist_and_gluing() -> None:
    """Show the exact base extension for the shifted chart and the 2+6 gluing."""

    fig, ax = plt.subplots(figsize=(12.0, 7.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Defining-prime chart change and retained collision gluing",
                 fontsize=15, color=INK, pad=12)

    left = FancyBboxPatch((.45, 5.85), 4.3, 2.3, boxstyle="round,pad=.15",
                          facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.35)
    right = FancyBboxPatch((7.25, 5.85), 4.3, 2.3, boxstyle="round,pad=.15",
                           facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.35)
    ax.add_patch(left)
    ax.add_patch(right)
    ax.text(2.6, 7.72, "original signed algebra", ha="center", fontsize=11, color=INK)
    ax.text(2.6, 7.15, r"$\mathcal{E}_0=K[T_0,\sigma_0]/(F_0,\sigma_0^2-F_0')$",
            ha="center", fontsize=10.2, color=INK)
    ax.text(2.6, 6.48, r"$F_0=-S^{-1}\prod_i(T_0-t_i)$",
            ha="center", fontsize=9.6, color=INK)
    ax.text(9.4, 7.72, "translated integral chart", ha="center", fontsize=11, color=INK)
    ax.text(9.4, 7.15,
            r"$\mathcal{E}_\lambda=K[T_\lambda,\sigma_\lambda]/"
            r"(F_\lambda,\sigma_\lambda^2-F_\lambda')$",
            ha="center", fontsize=9.7, color=INK)
    ax.text(9.4, 6.48,
            r"$F_\lambda=-\frac{1}{S-4\lambda}\prod_i[T_\lambda-(t_i-\lambda)]$",
            ha="center", fontsize=9.2, color=INK)
    arrow(ax, (7.18, 7.0), (4.82, 7.0),
          r"$T_\lambda\mapsto T_0-\lambda,\ \sigma_\lambda\mapsto q\sigma_0$",
          PURPLE, label_offset=(0, .55))
    ax.text(6.0, 6.18, r"$q^2=c_\lambda=S/(S-4\lambda)$",
            ha="center", fontsize=10, color=INK)
    ax.text(6.0, 5.52,
            r"isomorphism over $K(q)$; descent over $K$ iff $c_\lambda\in K^{\times2}$",
            ha="center", fontsize=9.1, color=MUTED,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    ax.text(6.0, 4.88, "Exact fixed-prime fibre product", ha="center",
            fontsize=12, color=INK)
    node(ax, (1.35, 3.72), r"$\mathcal{E}$", BLUE, LIGHT_BLUE, radius=.43, fontsize=11)
    node(ax, (5.0, 3.72), r"$\mathcal{E}_P\oplus\mathcal{E}_g$",
         GREEN, LIGHT_GREEN, radius=.72, fontsize=10)
    node(ax, (10.2, 3.72), r"$B/(R)[\sigma]/(\sigma^2)$",
         ORANGE, LIGHT_ORANGE, radius=.87, fontsize=9)
    arrow(ax, (1.80, 3.72), (4.25, 3.72), "inject", BLUE, label_offset=(0, .47))
    arrow(ax, (5.75, 3.72), (9.30, 3.72), "difference of restrictions",
          ORANGE, label_offset=(0, .48))
    ax.text(6.0, 2.94,
            r"$0\to\mathcal{E}\to\mathcal{E}_P\oplus\mathcal{E}_g"
            r"\to B/(R)[\sigma]/(\sigma^2)\to0$",
            ha="center", fontsize=10.4, color=INK)
    ax.text(6.0, 2.48, r"comparison determinant $R^2$; retained overlap length $2$",
            ha="center", fontsize=9.5, color=MUTED)

    local = FancyBboxPatch((.7, .52), 10.6, 1.42, boxstyle="round,pad=.14",
                           facecolor="white", edgecolor=INK, lw=1.1)
    ax.add_patch(local)
    ax.text(2.45, 1.48, r"$B[\zeta]/(\zeta^4-t^2)$",
            ha="center", fontsize=10.8, color=INK)
    arrow(ax, (3.55, 1.28), (5.10, 1.28), "normalize", GREEN,
          label_offset=(0, .40))
    ax.text(7.42, 1.48,
            r"$B[\zeta]/(\zeta^2-t)\ \oplus\ B[\zeta]/(\zeta^2+t)$",
            ha="center", fontsize=10.2, color=INK)
    ax.text(7.42, .90,
            r"Smith exponents $(0,0,1,1)$; kernel after specialization "
            r"$\langle\zeta^2,\zeta^3\rangle$",
            ha="center", fontsize=9.1, color=MUTED)
    save(fig, DEFINING, "defining-prime-twist-gluing")


def finite_field_twist_descent() -> None:
    """Illustrate the exact F_61 point counts and Frobenius action."""

    fig, ax = plt.subplots(figsize=(11.8, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Signed-cover descent for the witness $(13;4,18,468)$ at $q=61$",
                 fontsize=14.5, color=INK, pad=12)
    ax.text(6.0, 7.34,
            r"$h(r)=4r^4+r^3+35r^2+8r+28,\quad"
            r"(t_j)=(4,13,18,41)$",
            ha="center", fontsize=10.7, color=INK)

    roots = [4, 13, 18, 41]
    derivs = [18, 38, 26, 30]
    bs = [6, 25, 28, 11]
    xs = [1.5, 4.0, 6.7, 9.4]
    for xpos, root, deriv, b in zip(xs, roots, derivs, bs):
        node(ax, (xpos, 6.1), "$" + str(root) + "$", BLUE, LIGHT_BLUE,
             radius=.34, fontsize=10)
        ax.text(xpos, 5.57, f"$h'({root})={deriv}$: nonsquare",
                ha="center", fontsize=8.8, color=PURPLE)
        ax.text(xpos, 5.14, "$" + str(b) + f"^2=2\\cdot{deriv}$",
                ha="center", fontsize=8.8, color=GREEN)

    original = FancyBboxPatch((.55, 2.65), 3.1, 1.65, boxstyle="round,pad=.14",
                              facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.3)
    extension = FancyBboxPatch((4.45, 2.65), 3.1, 1.65, boxstyle="round,pad=.14",
                               facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    twist = FancyBboxPatch((8.35, 2.65), 3.1, 1.65, boxstyle="round,pad=.14",
                           facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.3)
    ax.add_patch(original)
    ax.add_patch(extension)
    ax.add_patch(twist)
    ax.text(2.10, 3.86, r"original: $\eta^2=h'(r)$", ha="center", fontsize=10, color=INK)
    ax.text(2.10, 3.31, r"$\#\mathcal{S}_1(\mathbb{F}_{61})=0$",
            ha="center", fontsize=11, color=ORANGE)
    ax.text(6.00, 3.86, r"extend: $w^2=2$", ha="center", fontsize=10, color=INK)
    ax.text(6.00, 3.31, r"$\eta_j=\pm(b_j/2)w$: 8 points",
            ha="center", fontsize=10, color=BLUE)
    ax.text(9.90, 3.86, r"twist: $\eta^2=2h'(r)$", ha="center", fontsize=10, color=INK)
    ax.text(9.90, 3.31, r"$\#\mathcal{S}_2(\mathbb{F}_{61})=8$",
            ha="center", fontsize=11, color=GREEN)
    arrow(ax, (3.70, 3.48), (4.39, 3.48), "base change", BLUE,
          label_offset=(0, .45))
    arrow(ax, (7.60, 3.48), (8.29, 3.48),
          r"$\eta_2=w\eta_1$ over $\mathrm{F}_{61^2}$", GREEN,
          label_offset=(0, .45))

    ax.text(6.0, 1.82,
            r"$w^{61}=-w$: Frobenius is four disjoint transpositions, "
            r"$N_n=0$ for odd $n$ and $8$ for even $n$.",
            ha="center", fontsize=9.7, color=INK)
    ax.text(6.0, 1.23,
            r"$Z_{\mathcal{S}_1}(T)=(1-T^2)^{-4}$; "
            r"$\operatorname{Tr}(\mathrm{Frob})=0$ but "
            r"$\operatorname{Tr}_{\mathcal{S}/\mathbb{F}_{61}}(1)=8$.",
            ha="center", fontsize=9.5, color=INK)
    ax.text(6.0, .56,
            "The extension and the twist are exact typed constructions; neither deletes the original ES witness.",
            ha="center", fontsize=9.1, color=MUTED)
    save(fig, CONT_B, "finite-field-twist-descent")


def arithmetic_frame_sieve() -> None:
    """Show every valuation branch used by Theorem E and its exact obstruction."""

    fig, ax = plt.subplots(figsize=(11.8, 7.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis("off")
    ax.set_title("Arithmetic nonsingularity of the odd receiving frame",
                 fontsize=14.5, color=INK, pad=12)

    top = FancyBboxPatch((3.35, 7.10), 5.30, .86, boxstyle="round,pad=.12",
                         facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    ax.add_patch(top)
    ax.text(6.0, 7.67,
            r"positive integral ES witness, prime $p\equiv1\ (\mathrm{mod}\ 12)$",
            ha="center", va="center", fontsize=10.2, color=INK)
    ax.text(6.0, 7.31, r"$N=S^6F\in\mathbb{Z}$; test $N\ne0$ before dividing by $S$",
            ha="center", va="center", fontsize=9.2, color=MUTED)

    arrow(ax, (6.0, 7.08), (3.0, 6.10), "exact divisibility split", PURPLE,
          label_offset=(-.55, .33))
    arrow(ax, (6.0, 7.08), (9.0, 6.10), "exact divisibility split", PURPLE,
          label_offset=(.55, .33))

    type_i = FancyBboxPatch((.55, 4.10), 5.0, 1.95, boxstyle="round,pad=.14",
                            facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=1.3)
    type_ii = FancyBboxPatch((6.45, 4.10), 5.0, 1.95, boxstyle="round,pad=.14",
                             facecolor=LIGHT_GREEN, edgecolor=GREEN, lw=1.3)
    ax.add_patch(type_i)
    ax.add_patch(type_ii)
    ax.text(3.05, 5.68, r"Type I: $x,y\in\mathbb{Z}_p^\times$, $z=pZ$",
            ha="center", fontsize=10.2, color=INK)
    ax.text(3.05, 5.20,
            r"$x\not\equiv y$: E2, discriminant $-511$; $v_p(N)=0$",
            ha="center", fontsize=9.0, color=INK)
    ax.text(3.05, 4.72,
            r"$y=x+pw$: E3, square class $1241$; $v_p(N)=2$",
            ha="center", fontsize=9.0, color=INK)
    ax.text(3.05, 4.32, "The diagonal is calculated, not discarded.",
            ha="center", fontsize=8.8, color=ORANGE)

    ax.text(8.95, 5.68, r"Type II: $x=pX$, $y=pY$, $z=Z$",
            ha="center", fontsize=10.2, color=INK)
    ax.text(8.95, 5.20,
            r"positivity forces $v_p(x)=v_p(y)=1$",
            ha="center", fontsize=9.0, color=INK)
    ax.text(8.95, 4.72,
            r"E4: $N/p^2\equiv-5Z^6(4t^2-7t+4)$",
            ha="center", fontsize=9.0, color=INK)
    ax.text(8.95, 4.32, r"discriminant $-15$; hence $v_p(N)=2$",
            ha="center", fontsize=8.8, color=GREEN)

    result = FancyBboxPatch((1.0, 1.20), 10.0, 2.05, boxstyle="round,pad=.15",
                            facecolor="white", edgecolor=INK, lw=1.35)
    ax.add_patch(result)
    ax.text(6.0, 2.92,
            r"$\left(\frac{-511}{p}\right)="
            r"\left(\frac{1241}{p}\right)="
            r"\left(\frac{-15}{p}\right)=-1$",
            ha="center", fontsize=11.0, color=PURPLE)
    ax.text(6.0, 2.42,
            r"$\Longrightarrow\ N\ne0\ \Longrightarrow\ "
            r"\det O=4\chi N/S^3\ne0$ for every witness at that prime",
            ha="center", fontsize=10.0, color=INK)
    ax.text(6.0, 1.94,
            r"quadratic reciprocity gives $3456$ reduced classes modulo $521220$",
            ha="center", fontsize=9.5, color=BLUE)
    ax.text(6.0, 1.53,
            "The five-prime, 163-witness census checks the valuations; it is not the quantified proof.",
            ha="center", fontsize=8.9, color=MUTED)
    arrow(ax, (3.05, 4.06), (4.75, 3.27), color=ORANGE)
    arrow(ax, (8.95, 4.06), (7.25, 3.27), color=GREEN)
    ax.text(6.0, .45,
            "Failure of one character condition is not a singularity certificate.",
            ha="center", fontsize=9.3, color=MUTED)
    save(fig, CONT_B, "arithmetic-frame-sieve")


def determinant_heat_mechanism() -> None:
    """Display the exact determinant-ratio chain and the distinct heat actions."""

    fig, ax = plt.subplots(figsize=(11.8, 7.1))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis("off")
    ax.set_title("Native determinant returns and finite heat certificates",
                 fontsize=14.5, color=INK, pad=12)

    left = FancyBboxPatch((.45, 4.15), 5.35, 3.28, boxstyle="round,pad=.14",
                          facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=1.3)
    right = FancyBboxPatch((6.20, 4.15), 5.35, 3.28, boxstyle="round,pad=.14",
                           facecolor=LIGHT_PURPLE, edgecolor=PURPLE, lw=1.3)
    ax.add_patch(left)
    ax.add_patch(right)
    ax.text(3.12, 7.08, "Consecutive native Gram determinants",
            ha="center", fontsize=10.8, color=INK)
    ax.text(3.12, 6.55,
            r"$r_L=d_{L+1}/d_L=(1+\beta_L)^{-1}$",
            ha="center", fontsize=10.1, color=BLUE)
    ax.text(3.12, 6.00,
            r"$\epsilon_L^2=a_L^2(1-r_{L-1})(1-r_L)/r_L$",
            ha="center", fontsize=10.0, color=INK)
    ax.text(3.12, 5.45, r"$\Theta\leq\epsilon_L$",
            ha="center", fontsize=10.0, color=ORANGE)
    ax.text(3.12, 4.91,
            r"$-\log(r_{L-1}r_L)\geq2\operatorname{arsinh}(\Theta/a_L)$",
            ha="center", fontsize=9.6, color=GREEN)
    ax.text(3.12, 4.48, "Sharp for the stated one-scalar constraint.",
            ha="center", fontsize=8.8, color=MUTED)

    ax.text(8.88, 7.08, r"$T(t)=A-tQ$, $Q^2=0$, original metric $G$",
            ha="center", fontsize=10.5, color=INK)
    ax.text(8.88, 6.50,
            r"$\mathcal{H}_\tau=\operatorname{tr}e^{-\tau T^2}$  (holomorphic)",
            ha="center", fontsize=9.7, color=PURPLE)
    ax.text(8.88, 5.99,
            r"$\mathcal{P}_\tau=\operatorname{tr}e^{-\tau T^{\dagger_G}T}$  (positive)",
            ha="center", fontsize=9.7, color=BLUE)
    ax.text(8.88, 5.43, r"$a_1=\frac{1}{2}\|T-T^{\dagger_G}\|_{\mathrm{HS},G}^2$",
            ha="center", fontsize=9.5, color=INK)
    ax.text(8.88, 4.88,
            r"$\frac{4}{7}\tau a_1\leq\Re\mathcal{H}_\tau-\mathcal{P}_\tau"
            r"\leq\frac{10}{7}\tau a_1$ if $\tau R^2\leq1/8$",
            ha="center", fontsize=9.2, color=GREEN)
    ax.text(8.88, 4.47, "The two heat functions are not identified.",
            ha="center", fontsize=8.8, color=MUTED)

    bottom = FancyBboxPatch((.90, 1.20), 10.2, 2.10, boxstyle="round,pad=.15",
                            facecolor="white", edgecolor=INK, lw=1.3)
    ax.add_patch(bottom)
    ax.text(6.0, 2.88,
            r"$\mathcal{R}_q=\log\frac{d_{q-1}d_q}{d_{2q-1}d_{2q}}"
            r"\geq2\sum_{L=q}^{2q-1}\operatorname{arsinh}(\Theta/a_L)$",
            ha="center", fontsize=10.4, color=BLUE)
    ax.text(6.0, 2.35,
            r"finite stopping: $|\Delta_\tau-\Delta_{\tau,m}|\leq"
            r"\tau a_1\dfrac{(2m+1)x^m}{m!\{1-3x/(m+1)\}}$",
            ha="center", fontsize=9.6, color=PURPLE)
    ax.text(6.0, 1.82,
            "The determinant return and heat gap are necessary finite-dimensional constraints;",
            ha="center", fontsize=8.9, color=MUTED)
    ax.text(6.0, 1.48,
            "neither is the whole assembled arithmetic action or a global endpoint theorem.",
            ha="center", fontsize=8.9, color=MUTED)
    arrow(ax, (3.13, 4.10), (4.75, 3.32), color=BLUE)
    arrow(ax, (8.87, 4.10), (7.25, 3.32), color=PURPLE)
    save(fig, CONT_B, "determinant-heat-mechanism")


if __name__ == "__main__":
    quartic_transform()
    local_fibres()
    fixed_q_example()
    odd_divisor_crossing()
    raw_tetrahedron()
    fixed_input_cover()
    finite_boundary_fibre()
    capacity_partition()
    capacity_sharp_bound()
    positive_real_rank_crossing()
    residue_trace_factorization()
    residue_native_gram_bridge()
    integral_normalization_smith()
    defining_prime_twist_and_gluing()
    arithmetic_frame_sieve()
    determinant_heat_mechanism()
    finite_field_twist_descent()
    print("generated 17 figures (PDF and PNG)")
