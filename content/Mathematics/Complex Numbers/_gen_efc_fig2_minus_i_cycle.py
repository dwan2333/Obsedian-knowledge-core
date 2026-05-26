"""Generate efc_fig2_minus_i_cycle.png — powers of -i cycle (clockwise rotation).

Counterpart to the hub's powers-of-i figure. Same four cardinal points but
the rotation direction is CW: -i -> -1 -> i -> 1 -> -i.
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

# Points in CW order: -i, -1, i, 1.
POINTS = [
    ((0, -1), r"$-i$",  r"$(-i)^1$", ORANGE_EDGE),
    ((-1, 0), r"$-1$",  r"$(-i)^2$", GREEN_EDGE),
    ((0, 1),  r"$i$",   r"$(-i)^3$", PURPLE_EDGE),
    ((1, 0),  r"$1$",   r"$(-i)^4$", '#aa6644'),
]

fig, ax = plt.subplots(figsize=(8, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.55, -0.05, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.05, 1.55, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.6, zorder=2)
ax.add_patch(circ)

# Plot each point with two labels.
for (x, y), val_lbl, pow_lbl, col in POINTS:
    ax.scatter([x], [y], s=110, color=col, edgecolor='white',
               linewidth=2.0, zorder=5)
    r = np.array([x, y])
    if np.linalg.norm(r) > 0:
        outward = r / np.linalg.norm(r)
    else:
        outward = np.array([1.0, 0])
    lbl_pos = r + 0.24 * outward
    pow_pos = r + 0.48 * outward
    ax.text(lbl_pos[0], lbl_pos[1], val_lbl,
            fontsize=18, color=col, ha='center', va='center',
            fontweight='bold')
    ax.text(pow_pos[0], pow_pos[1], pow_lbl,
            fontsize=13, color=col, ha='center', va='center')

# CW arrows connecting the cycle: -i -> -1 -> i -> 1 -> -i.
arc_pairs = [
    ((0, -1), (-1, 0), ORANGE_EDGE),   # -i -> -1 (lower-left arc)
    ((-1, 0), (0, 1),  GREEN_EDGE),    # -1 -> i (upper-left arc)
    ((0, 1),  (1, 0),  PURPLE_EDGE),   # i -> 1 (upper-right arc)
    ((1, 0),  (0, -1), '#aa6644'),     # 1 -> -i (lower-right arc)
]
for (p1, p2, col) in arc_pairs:
    a1 = np.degrees(np.arctan2(p1[1], p1[0]))
    a2 = np.degrees(np.arctan2(p2[1], p2[0]))
    # CW arc means we need theta1 > theta2 in standard math angles.
    # The Arc primitive in mpatches draws CCW from theta1 to theta2.
    # To get CW visual sweep, we just swap the order and add 360 if needed.
    if a1 < a2:
        a1 += 360
    arc = mpatches.Arc((0, 0), 2.0, 2.0,
                       angle=0, theta1=a2, theta2=a1,
                       color=col, linewidth=2.2, zorder=3)
    ax.add_patch(arc)
    # Arrowhead just before the END of the CW sweep (toward p2).
    # Going CW means decreasing angle from a1 down to a2.
    # The arrow points to p2; the tail is just *after* p2 in the CW direction.
    tip_ang = np.radians(a2)
    end_ang = np.radians(a2 + 4)  # 4 degrees BEFORE p2 in CW direction means + in standard
    ax.annotate('', xy=(np.cos(tip_ang), np.sin(tip_ang)),
                xytext=(np.cos(end_ang), np.sin(end_ang)),
                arrowprops=dict(arrowstyle='->', color=col, lw=2.0,
                                mutation_scale=18),
                zorder=4)

# Center caption.
ax.text(0, 0, r"$\times\,(-i)$", fontsize=18, color=TEXT,
        ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='circle,pad=0.30',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_title("Powers of $-i$ — each $\\times (-i)$ is a 90$\\degree$ CW rotation",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

# Footnote.
ax.text(0.0, -1.85,
        r"$(-i)^1 = -i$,  $(-i)^2 = -1$,  $(-i)^3 = i$,  $(-i)^4 = 1$  "
        "(opposite spin to powers of $i$)",
        fontsize=11, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.3))

ax.set_xlim(-1.85, 1.85)
ax.set_ylim(-2.20, 1.65)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efc_fig2_minus_i_cycle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efc_fig2_minus_i_cycle.png")
