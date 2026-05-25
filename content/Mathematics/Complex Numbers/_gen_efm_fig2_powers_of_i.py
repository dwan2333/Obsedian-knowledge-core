"""Generate efm_fig2_powers_of_i.png — powers of i as 90-degree rotations.

Four points on the unit circle at the four cardinal directions: 1 (right), i
(up), -1 (left), -i (down). Curved arrows between them show the 90 deg CCW
rotation cycle: 1 -> i -> -1 -> -i -> 1.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'

# Four cardinal points on the unit circle.
POINTS = [
    ((1, 0),  r"$1$",   r"$i^0$",  ORANGE_EDGE),
    ((0, 1),  r"$i$",   r"$i^1$",  GREEN_EDGE),
    ((-1, 0), r"$-1$",  r"$i^2$",  PURPLE_EDGE),
    ((0, -1), r"$-i$",  r"$i^3$",  '#aa6644'),
]

fig, ax = plt.subplots(figsize=(8, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.55, -0.04, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.04, 1.55, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.6, zorder=2)
ax.add_patch(circ)

# Plot each point with two labels: value + power.
for (x, y), val_lbl, pow_lbl, col in POINTS:
    ax.scatter([x], [y], s=110, color=col, edgecolor='white',
               linewidth=2.0, zorder=5)
    # Outward direction for label placement.
    r = np.array([x, y])
    if np.linalg.norm(r) > 0:
        outward = r / np.linalg.norm(r)
    else:
        outward = np.array([1.0, 0])
    lbl_pos = r + 0.22 * outward
    pow_pos = r + 0.45 * outward
    ax.text(lbl_pos[0], lbl_pos[1], val_lbl,
            fontsize=18, color=col, ha='center', va='center',
            fontweight='bold')
    ax.text(pow_pos[0], pow_pos[1], pow_lbl,
            fontsize=14, color=col, ha='center', va='center')

# Curved arrows showing the rotation cycle:
# 1 -> i, i -> -1, -1 -> -i, -i -> 1.
arc_pairs = [
    ((1, 0),  (0, 1),  ORANGE_EDGE),   # 1 -> i
    ((0, 1),  (-1, 0), GREEN_EDGE),    # i -> -1
    ((-1, 0), (0, -1), PURPLE_EDGE),   # -1 -> -i
    ((0, -1), (1, 0),  '#aa6644'),     # -i -> 1
]
for (p1, p2, col) in arc_pairs:
    # Arc center at origin, radius 1.
    a1 = np.degrees(np.arctan2(p1[1], p1[0]))
    a2 = np.degrees(np.arctan2(p2[1], p2[0]))
    if a2 < a1:
        a2 += 360
    arc = mpatches.Arc((0, 0), 2.0, 2.0,
                       angle=0, theta1=a1, theta2=a2,
                       color=col, linewidth=2.2,
                       linestyle='-', zorder=3)
    ax.add_patch(arc)
    # Arrowhead just before the end of the arc.
    end_ang = np.radians(a2 - 3)
    tip_ang = np.radians(a2)
    ax.annotate('', xy=(np.cos(tip_ang), np.sin(tip_ang)),
                xytext=(np.cos(end_ang), np.sin(end_ang)),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.0,
                                mutation_scale=18),
                zorder=4)

# Center caption "x i" indicating multiplication step.
ax.text(0, 0, r"$\times\,i$", fontsize=22, color=TEXT,
        ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='circle,pad=0.35',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_title("Powers of $i$ — each $\\times i$ is a 90$\\degree$ CCW rotation",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

# Below-diagram annotation.
ax.text(0.0, -1.85,
        r"$1 \cdot i = i$,  $i^2 = -1$,  $i^3 = -i$,  $i^4 = 1$  (cycle repeats every 4 powers)",
        fontsize=12, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.3))

ax.set_xlim(-1.85, 1.85)
ax.set_ylim(-2.20, 1.65)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efm_fig2_powers_of_i.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efm_fig2_powers_of_i.png")
