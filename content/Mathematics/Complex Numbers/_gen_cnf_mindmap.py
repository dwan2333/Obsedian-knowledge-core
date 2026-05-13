"""Generate cnf_mindmap.png — concept map for Complex Number Fundamentals.

Central node = the punchline (complex multiplication = rotation/scaling).
Surrounding nodes = the 4 sections of the note + 1 bonus node.
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
ax.text(0, 0.30, "Complex multiplication", fontsize=14,
        ha='center', va='center', color='white', fontweight='bold', zorder=5)
ax.text(0, -0.05, "= rotation + scaling", fontsize=14,
        ha='center', va='center', color='white', fontweight='bold', zorder=5)
ax.text(0, -0.42, r"on the 2D complex plane", fontsize=11,
        ha='center', va='center', color='white', zorder=5)

# Topic nodes — five.
topics = [
    ("1. Build the plane",
     r"$i^2 = -1$" "\n"
     r"$i$ lives one unit" "\n"
     r"above the real line" "\n"
     r"$a + bi \leftrightarrow (a,b)$"),
    ("2. Operations",
     r"Add component-wise" "\n"
     r"Mult by $i$ = rotate $90\degree$" "\n"
     r"Mult by $z$ = rotate + stretch" "\n"
     r"(send $1\to z$)"),
    ("3. Trig identities",
     r"$\mathrm{cis}(\alpha)\,\mathrm{cis}(\beta) = \mathrm{cis}(\alpha\!+\!\beta)$" "\n"
     r"FOIL $\Rightarrow$ angle-sum:" "\n"
     r"$\cos(\alpha\!+\!\beta), \sin(\alpha\!+\!\beta)$" "\n"
     r"$z^2 \Rightarrow$ double-angle"),
    ("4. Roots in the plane",
     r"$z^2 = i$ $\Rightarrow$ 2 roots" "\n"
     r"at $45\degree, 225\degree$" "\n"
     r"$x^3 = 1$ $\Rightarrow$ 3 roots" "\n"
     r"at $0\degree, 120\degree, 240\degree$"),
    ("5. Toward Euler",
     r"$\mathrm{cis}$ turns + into $\times$" "\n"
     r"$\to$ the exponential property" "\n"
     r"$\to$ rename it" "\n"
     r"$e^{i\alpha} = \cos\alpha + i\sin\alpha$"),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # orange — setup
    ('#4a90e2', '#1f4f8c'),  # blue   — operations
    ('#7bb55c', '#3d7530'),  # green  — trig identities
    ('#b76db4', '#6e3a6c'),  # purple — roots
    ('#d4a04a', '#8c6520'),  # yellow — Euler
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
            fontsize=9.5, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("Complex Number Fundamentals — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-8.2, 8.2)
ax.set_ylim(-7.8, 8.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_mindmap.png")
