"""Generate efm_mindmap.png — concept map for Euler's Formula via exp(x).

Central node = e^(i*theta) = cos theta + i sin theta. Five surrounding nodes
covering: 1. the goal, 2. exp() as polynomial, 3. the addition property,
4. the spiral picture, 5. the two faces (real vs imag).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13, 9.5))

# Center node.
center_w, center_h = 4.2, 1.8
center = mpatches.FancyBboxPatch(
    (-center_w / 2, -center_h / 2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(center)
ax.text(0, 0.30, r"$e^{i\theta} = \cos\theta + i\sin\theta$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.25, "Euler's formula",
        fontsize=12, ha='center', va='center',
        color='white', zorder=5)

# Five topic nodes.
topics = [
    ("1. The Goal",
     r"$e^{i\theta} = \cos\theta + i\sin\theta$" "\n"
     r"Special case $e^{i\pi} = -1$" "\n"
     "(Euler's identity)" "\n"
     "Naive reading is gibberish"),
    ("2. exp() is a polynomial",
     r"$\exp(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!}$" "\n"
     "Not repeated multiplication" "\n"
     r"$e^x$ is just shorthand for" "\n"
     "this infinite polynomial"),
    ("3. Defining property",
     r"$\exp(a+b) = \exp(a)\exp(b)$" "\n"
     "Addition in $\\to$ mult out" "\n"
     r"$\Rightarrow \exp(0) = 1$" "\n"
     r"$\Rightarrow \exp(n) = e^n$"),
    ("4. The spiral",
     "Plug in $i\\theta$:" "\n"
     "powers of $i$ rotate $90\\degree$," "\n"
     "$1/n!$ shrinks magnitudes" "\n"
     "$\\to$ spirals to point on circle"),
    ("5. Two faces of exp",
     "Real input: $\\exp(x) = e^x$" "\n"
     "(constant $e \\approx 2.718$)" "\n"
     "Imag input: periodic" "\n"
     "(constant $2\\pi i$)"),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # orange
    ('#4a90e2', '#1f4f8c'),  # blue
    ('#7bb55c', '#3d7530'),  # green
    ('#b76db4', '#6e3a6c'),  # purple
    ('#d4a04a', '#8c6520'),  # yellow
]

n_topics = len(topics)
radius = 5.6
box_w, box_h = 3.8, 2.1

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, node_palette)):
    theta = pi / 2 - i * (2 * pi / n_topics)
    x = radius * cos(theta)
    y = radius * sin(theta)

    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5,
            linestyle='-', zorder=1)
    box = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2
    )
    ax.add_patch(box)
    ax.text(x, y + box_h / 2 - 0.32, title,
            fontsize=12, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.22, body,
            fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("Euler's Formula via $\\exp(x)$ — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-8.2, 8.2)
ax.set_ylim(-7.8, 8.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efm_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efm_mindmap.png")
