"""Generate pyth_mindmap.png — concept map for the Pythagorean Theorem note.

Central node = the theorem. Five surrounding topic nodes for the note's
sections, arranged radially clockwise from the top.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13, 9.8))

# Center node.
cw, ch = 4.2, 1.8
center = mpatches.FancyBboxPatch(
    (-cw / 2, -ch / 2), cw, ch,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4)
ax.add_patch(center)
ax.text(0, 0.30, r"$A^2 + B^2 = C^2$", fontsize=19, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.34, "Pythagorean Theorem", fontsize=13, ha='center', va='center',
        color='white', zorder=5)

topics = [
    ("1. Theorem & History",
     "Statement of the theorem.\n"
     "A misnomer — known to the\n"
     "Babylonians 1000 yrs before\n"
     "Pythagoras."),
    ("2. Three Classic Proofs",
     "Rearrangement (4 triangles).\n"
     "Euclid's area-shearing.\n"
     "Similar triangles scaled\n"
     r"by $A,B,C$ $\to$ rectangle."),
    ("3. The Simplest Proof",
     "Super Theorem: ANY shape\n"
     "on the sides works.\n"
     "Drop the altitude $\\to$ three\n"
     "similar triangles; done."),
    ("4. The Cosine Rule",
     r"$A^2 + B^2 - 2AB\cos\gamma = C^2$." "\n"
     r"Pythagoras at $\gamma=90\degree$." "\n"
     r"$60\degree,120\degree$ cases;" "\n"
     "Pythagorean triples."),
    ("5. Generalizations",
     "Inverse Pythagoras (altitude).\n"
     "Equal-area flank triangles.\n"
     "3D/4D box diagonals.\n"
     "de Gua: squared AREAS."),
]

palette = [
    ('#e2924a', '#8c4f1f'),   # orange
    ('#4a90e2', '#1f4f8c'),   # blue
    ('#7bb55c', '#3d7530'),   # green
    ('#b76db4', '#6e3a6c'),   # purple
    ('#d4a04a', '#8c6520'),   # yellow
]

n = len(topics)
radius = 5.6
bw, bh = 3.9, 2.25

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, palette)):
    theta = pi / 2 - i * (2 * pi / n)
    x = radius * cos(theta)
    y = radius * sin(theta)
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5, zorder=1)
    box = mpatches.FancyBboxPatch(
        (x - bw / 2, y - bh / 2), bw, bh,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2)
    ax.add_patch(box)
    ax.text(x, y + bh / 2 - 0.34, title, fontsize=12.5, ha='center',
            va='center', color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.22, body, fontsize=9.6, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("The Pythagorean Theorem — concept map", fontsize=15, pad=10,
             fontweight='bold')
ax.set_xlim(-8.4, 8.4)
ax.set_ylim(-8.0, 8.4)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('pyth_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pyth_mindmap.png")
