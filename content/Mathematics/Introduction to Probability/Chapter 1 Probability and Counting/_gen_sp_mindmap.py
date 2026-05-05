"""Generate sp_mindmap.png — concept map for Pascal's Identity via Grid Paths.

Central node is the topic. Five surrounding nodes are the five sections of
the note, arranged radially clockwise from the top.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(12, 9))

# Center node
center_w, center_h = 3.4, 1.5
center = mpatches.FancyBboxPatch(
    (-center_w / 2, -center_h / 2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(center)
ax.text(0, 0.22, r"Pascal's Identity",
        fontsize=16, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.30, "via Grid Paths",
        fontsize=13, ha='center', va='center',
        color='white', zorder=5)

# Topic nodes
topics = [
    ("1. Setup",
     r"Increasing paths" "\n"
     r"$(0,0)\to(m,n)$" "\n"
     r"right or up only" "\n"
     r"$C(m,n)$ = the set"),
    ("2. Recursive count",
     r"Last step right or up:" "\n"
     r"$|C(m,n)|=$" "\n"
     r"$|C(m{-}1,n)|+|C(m,n{-}1)|$"),
    ("3. Direct count",
     r"Path = sequence of" "\n"
     r"$m$ R's and $n$ U's" "\n"
     r"$|C(m,n)|=\binom{m+n}{m}$"),
    ("4. Pascal's identity",
     r"Equate the two counts:" "\n"
     r"$\binom{n}{k}=$" "\n"
     r"$\binom{n{-}1}{k{-}1}+\binom{n{-}1}{k}$"),
    ("5. Pascal's triangle",
     r"Rotate the grid 45°." "\n"
     r"Each entry = sum of" "\n"
     r"the two above it."),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # 1 orange
    ('#4a90e2', '#1f4f8c'),  # 2 blue
    ('#7bb55c', '#3d7530'),  # 3 green
    ('#b76db4', '#6e3a6c'),  # 4 purple
    ('#d4a04a', '#8c6520'),  # 5 yellow-brown
]

n_topics = len(topics)
radius = 4.8
box_w, box_h = 3.2, 1.9

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, node_palette)):
    # Start at top (theta = pi/2), rotate clockwise
    theta = pi / 2 - i * (2 * pi / n_topics)
    x = radius * cos(theta)
    y = radius * sin(theta)

    # Connector
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5,
            linestyle='-', zorder=1)

    # Node box
    box = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2
    )
    ax.add_patch(box)

    # Title row
    ax.text(x, y + box_h / 2 - 0.32, title,
            fontsize=12, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    # Body
    ax.text(x, y - 0.18, body,
            fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title(r"Pascal's Identity via Grid Paths — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-7.2, 7.2)
ax.set_ylim(-6.5, 7.0)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('sp_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_mindmap.png")
