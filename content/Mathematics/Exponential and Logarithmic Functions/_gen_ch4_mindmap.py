"""Generate ch4_mindmap.png — concept map for Chapter 4.

Central node: Exponential & Logarithmic Functions. 8 surrounding nodes,
one per section.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(14, 11))

# Center node
center_w, center_h = 5.0, 2.0
center = mpatches.FancyBboxPatch(
    (-center_w / 2, -center_h / 2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(center)
ax.text(0, 0.30, "Exp & Log",
        fontsize=18, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.30, "Inverse functions modeling multiplicative growth",
        fontsize=11, ha='center', va='center',
        color='white', zorder=5, style='italic')

topics = [
    ("4.1 Exponential Functions",
     r"$f(x) = a b^x$" "\n"
     "compound interest" "\n"
     "the number $e$"),
    ("4.2 Graphs of Exp",
     "growth vs decay shape" "\n"
     "y-intercept = $a$" "\n"
     "asymptote $y = d$" "\n"
     "transformations"),
    ("4.3 Logarithmic Functions",
     r"$\log_b(a) = $ exponent" "\n"
     "inverse of exp" "\n"
     "$\\log$, $\\ln$ conventions"),
    ("4.4 Graphs of Log",
     "domain $x > 0$" "\n"
     "vertical asymptote" "\n"
     "transformations" "\n"
     "(mirror of exp graph)"),
    ("4.5 Log Properties",
     "product / quotient / power" "\n"
     "rules" "\n"
     "change of base" "\n"
     "expand / condense"),
    ("4.6 Exp/Log Equations",
     "one-to-one property" "\n"
     "common base method" "\n"
     "take $\\log$ of both sides" "\n"
     "extraneous solutions"),
    ("4.7 Models",
     "half-life decay" "\n"
     "doubling time" "\n"
     "Newton's cooling" "\n"
     "logistic growth"),
    ("4.8 Fitting Data",
     "regression on data" "\n"
     "exp / log / logistic" "\n"
     "scatter plot $\\to$ model"),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # orange
    ('#4a90e2', '#1f4f8c'),  # blue
    ('#7bb55c', '#3d7530'),  # green
    ('#b76db4', '#6e3a6c'),  # purple
    ('#d4a04a', '#8c6520'),  # yellow
    ('#cd6680', '#7a3030'),  # red
    ('#5dc9b8', '#2c7b6f'),  # teal
    ('#a87dc0', '#574270'),  # lavender
]

n_topics = len(topics)
radius = 6.8
box_w, box_h = 3.6, 2.0

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
    ax.text(x, y + box_h / 2 - 0.30, title,
            fontsize=11, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.25, body,
            fontsize=9.5, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("Chapter 4 — Exponential and Logarithmic Functions — concept map",
             fontsize=16, pad=10, fontweight='bold')

ax.set_xlim(-9.5, 9.5); ax.set_ylim(-9.5, 9.5)
ax.set_aspect('equal'); ax.axis('off')

plt.tight_layout()
plt.savefig('ch4_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_mindmap.png")
