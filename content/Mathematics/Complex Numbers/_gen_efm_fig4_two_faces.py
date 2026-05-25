"""Generate efm_fig4_two_faces.png — exp(x) branches: real vs imaginary inputs.

Branching diagram. Top: exp(x) box. Two branches:
  Real branch (left): exp(x) = e^x  with the constant e at the leaf.
  Imaginary branch (right): exp(i*theta) periodic with period 2*pi*i.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_FACE, BLUE_EDGE = '#4a90e2', '#1f4f8c'
GREEN_FACE, GREEN_EDGE = '#7bb55c', '#3d7530'
PURPLE_FACE, PURPLE_EDGE = '#b76db4', '#6e3a6c'
ORANGE_FACE, ORANGE_EDGE = '#e2924a', '#8c4f1f'
YELLOW_FACE, YELLOW_EDGE = '#d4a04a', '#8c6520'
TEXT = '#222222'
MUTE = '#888888'

fig, ax = plt.subplots(figsize=(12, 9))

# Top node: exp(x) function.
center = mpatches.FancyBboxPatch(
    (-2.0, 2.7), 4.0, 1.5,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor=BLUE_FACE, edgecolor=BLUE_EDGE, linewidth=2.4, zorder=4
)
ax.add_patch(center)
ax.text(0, 3.65, r"$\exp(x)$",
        fontsize=22, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, 3.10, r"$= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$",
        fontsize=13, ha='center', va='center',
        color='white', zorder=5)

# Left branch — REAL input.
left_box = mpatches.FancyBboxPatch(
    (-5.8, 0.0), 4.6, 1.8,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor=ORANGE_FACE, edgecolor=ORANGE_EDGE, linewidth=2.2, zorder=4
)
ax.add_patch(left_box)
ax.text(-3.5, 1.50, r"Real input  $x \in \mathbb{R}$",
        fontsize=14, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(-3.5, 0.95, r"$\exp(x) = \exp(1)^x = e^x$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(-3.5, 0.35, r"exponential growth",
        fontsize=11, ha='center', va='center',
        color='white', zorder=5, style='italic')

# Right branch — IMAGINARY input.
right_box = mpatches.FancyBboxPatch(
    (1.2, 0.0), 4.6, 1.8,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor=PURPLE_FACE, edgecolor=PURPLE_EDGE, linewidth=2.2, zorder=4
)
ax.add_patch(right_box)
ax.text(3.5, 1.50, r"Imaginary input  $i\theta$",
        fontsize=14, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(3.5, 0.95, r"$\exp(i\theta) = \cos\theta + i\sin\theta$",
        fontsize=14, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(3.5, 0.35, r"unit-circle motion",
        fontsize=11, ha='center', va='center',
        color='white', zorder=5, style='italic')

# Connector lines.
ax.annotate('', xy=(-3.5, 1.85), xytext=(-0.8, 2.7),
            arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE,
                            lw=2.4, mutation_scale=20),
            zorder=3)
ax.annotate('', xy=(3.5, 1.85), xytext=(0.8, 2.7),
            arrowprops=dict(arrowstyle='->', color=PURPLE_EDGE,
                            lw=2.4, mutation_scale=20),
            zorder=3)

# Leaf constants for each branch.
leaf_left = mpatches.FancyBboxPatch(
    (-5.0, -2.4), 3.0, 1.4,
    boxstyle='round,pad=0.08,rounding_size=0.25',
    facecolor=YELLOW_FACE, edgecolor=YELLOW_EDGE, linewidth=2.0, zorder=4
)
ax.add_patch(leaf_left)
ax.text(-3.5, -1.4, r"$e := \exp(1)$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(-3.5, -1.95, r"$\approx 2.71828\ldots$",
        fontsize=12, ha='center', va='center',
        color='white', zorder=5)

leaf_right = mpatches.FancyBboxPatch(
    (2.0, -2.4), 3.0, 1.4,
    boxstyle='round,pad=0.08,rounding_size=0.25',
    facecolor=GREEN_FACE, edgecolor=GREEN_EDGE, linewidth=2.0, zorder=4
)
ax.add_patch(leaf_right)
ax.text(3.5, -1.4, r"period $= 2\pi i$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(3.5, -1.95, r"$\exp(i\theta + 2\pi i) = \exp(i\theta)$",
        fontsize=11, ha='center', va='center',
        color='white', zorder=5)

# Connect branches to their leaf constants.
ax.annotate('', xy=(-3.5, -1.0), xytext=(-3.5, 0.0),
            arrowprops=dict(arrowstyle='->', color=YELLOW_EDGE,
                            lw=2.0, mutation_scale=16),
            zorder=3)
ax.annotate('', xy=(3.5, -1.0), xytext=(3.5, 0.0),
            arrowprops=dict(arrowstyle='->', color=GREEN_EDGE,
                            lw=2.0, mutation_scale=16),
            zorder=3)

# Bottom annotation.
ax.text(0, -3.40,
        r'"Each of these constants is a child of the function $\exp(x)$, '
        "but the way they're related happens along different dimensions.\"",
        fontsize=11, color=TEXT, ha='center', va='center',
        style='italic')

ax.set_title("The two faces of $\\exp(x)$ — real vs imaginary inputs",
             fontsize=15, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-7.0, 7.0)
ax.set_ylim(-3.8, 4.8)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efm_fig4_two_faces.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efm_fig4_two_faces.png")
