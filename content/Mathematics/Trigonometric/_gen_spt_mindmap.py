"""Generate spt_mindmap.png — concept map for the Sneaky Pythagorean Proof.

Central node = the identity. Five surrounding topic nodes for the note's
sections, arranged radially clockwise from the top.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13, 9.5))

# Center node.
center_w, center_h = 4.0, 1.7
center = mpatches.FancyBboxPatch(
    (-center_w / 2, -center_h / 2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(center)
ax.text(0, 0.28, r"$\sin^2\theta + \cos^2\theta = 1$",
        fontsize=18, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.32, "via similar triangles",
        fontsize=13, ha='center', va='center',
        color='white', zorder=5)

# Topic nodes — five sections of the note.
topics = [
    ("1. Setup",
     r'"Where is $\cos^2\theta$?"' "\n"
     r"Re-draw the triangle:" "\n"
     r"legs $\sin\theta,\cos\theta$," "\n"
     r"hypotenuse $1$."),
    ("2. The construction",
     r"Drop altitude from" "\n"
     r"right-angle vertex" "\n"
     r"onto the hypotenuse $\to$" "\n"
     r"two similar sub-triangles."),
    (r"3. Lower piece $= \cos^2\theta$",
     r"$\cos\theta = S / \cos\theta$" "\n"
     r"$\Rightarrow S = \cos^2\theta$" "\n"
     r"Angle $\theta$ doing" "\n"
     '"double duty."'),
    (r"4. Upper piece $= \sin^2\theta$",
     r"Angle chase: $\alpha + \theta = 90\degree$" "\n"
     r"$\Rightarrow \theta$ reappears up top." "\n"
     r"$\sin\theta = S' / \sin\theta$" "\n"
     r"$\Rightarrow S' = \sin^2\theta$."),
    ("5. Punchline + bonus",
     r"Hypotenuse $1 = \cos^2\theta + \sin^2\theta$." "\n"
     r"Bonus: substitute $x=\alpha/2$" "\n"
     r"in $\cos^2 x = \frac{1+\cos 2x}{2}$" "\n"
     r"$\Rightarrow$ half-angle identity."),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # 1 orange — setup
    ('#4a90e2', '#1f4f8c'),  # 2 blue   — construction
    ('#7bb55c', '#3d7530'),  # 3 green  — lower
    ('#b76db4', '#6e3a6c'),  # 4 purple — upper
    ('#d4a04a', '#8c6520'),  # 5 yellow — punchline
]

n_topics = len(topics)
radius = 5.4
box_w, box_h = 3.7, 2.1

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, node_palette)):
    theta = pi / 2 - i * (2 * pi / n_topics)
    x = radius * cos(theta)
    y = radius * sin(theta)

    # Connector line.
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5,
            linestyle='-', zorder=1)

    # Node box.
    box = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2
    )
    ax.add_patch(box)

    # Title row.
    ax.text(x, y + box_h / 2 - 0.32, title,
            fontsize=12, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    # Body text.
    ax.text(x, y - 0.20, body,
            fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title(r"Sneaky Proof of the Pythagorean Identity — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-8.0, 8.0)
ax.set_ylim(-7.5, 8.0)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('spt_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved spt_mindmap.png")
