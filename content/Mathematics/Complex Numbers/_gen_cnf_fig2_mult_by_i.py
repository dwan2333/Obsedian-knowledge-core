"""Generate cnf_fig2_mult_by_i.png — multiplication by i = 90 deg CCW rotation.

Show 3 + 2i (point (3, 2), blue vector) and i*(3 + 2i) = -2 + 3i (point (-2, 3),
orange vector). A curved arrow indicates the 90-degree counterclockwise rotation
from the first to the second. The annotation makes the rotation explicit.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_FACE, BLUE_EDGE = '#4a90e2', '#1f4f8c'
ORANGE_FACE, ORANGE_EDGE = '#e2924a', '#8c4f1f'
GREEN_EDGE = '#3d7530'
TEXT = '#222222'
MUTE = '#888888'

fig, ax = plt.subplots(figsize=(9, 8))

# Background grid.
for x in range(-4, 5):
    ax.axvline(x, color='#eeeeee', linewidth=0.5, zorder=0)
for y in range(-2, 5):
    ax.axhline(y, color='#eeeeee', linewidth=0.5, zorder=0)

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(4.5, -0.30, "Re", fontsize=12, color=MUTE, ha='right', va='top')
ax.text(-0.20, 4.5, "Im", fontsize=12, color=MUTE, ha='right', va='top', rotation=90)

# Tick marks on real and imaginary axes.
for x in range(-3, 5):
    if x == 0: continue
    ax.plot([x, x], [-0.07, 0.07], color=MUTE, linewidth=1.0, zorder=2)
for y in range(-1, 5):
    if y == 0: continue
    ax.plot([-0.07, 0.07], [y, y], color=MUTE, linewidth=1.0, zorder=2)

# Original vector: 3 + 2i (blue).
ax.annotate('', xy=(3, 2), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=BLUE_EDGE, lw=2.8,
                            mutation_scale=22),
            zorder=4)
ax.scatter([3], [2], s=70, color=BLUE_EDGE, zorder=5)
ax.text(3.05, 1.85, r"$3 + 2i$", fontsize=15, color=BLUE_EDGE,
        ha='left', va='top', fontweight='bold')

# Rotated vector: -2 + 3i (orange).
ax.annotate('', xy=(-2, 3), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=2.8,
                            mutation_scale=22),
            zorder=4)
ax.scatter([-2], [3], s=70, color=ORANGE_EDGE, zorder=5)
ax.text(-2.10, 3.25, r"$i \cdot (3 + 2i) = -2 + 3i$",
        fontsize=14, color=ORANGE_EDGE,
        ha='center', va='bottom', fontweight='bold')

# Arc indicating the 90-degree rotation from (3,2) to (-2,3).
# Both points are on a circle of radius sqrt(13). The arc covers 90 deg
# CCW from the angle of (3,2) to the angle of (-2,3).
r = np.sqrt(13.0)
ang1 = np.degrees(np.arctan2(2, 3))   # ~ 33.7
ang2 = np.degrees(np.arctan2(3, -2))  # ~ 123.7
arc = mpatches.Arc((0, 0), 2 * r, 2 * r,
                   angle=0, theta1=ang1, theta2=ang2,
                   color=GREEN_EDGE, linewidth=2.2, linestyle='--', zorder=3)
ax.add_patch(arc)

# Arrow head on the arc near the end (just before ang2).
end_ang = np.radians(ang2 - 4)
tip_ang = np.radians(ang2)
ax.annotate('', xy=(r * np.cos(tip_ang), r * np.sin(tip_ang)),
            xytext=(r * np.cos(end_ang), r * np.sin(end_ang)),
            arrowprops=dict(arrowstyle='->', color=GREEN_EDGE,
                            lw=2.0, mutation_scale=18),
            zorder=4)

# Label the 90 deg.
mid_ang = np.radians((ang1 + ang2) / 2)
lx = (r + 0.55) * np.cos(mid_ang)
ly = (r + 0.55) * np.sin(mid_ang)
ax.text(lx, ly, r"$90\degree$ CCW", fontsize=13, color=GREEN_EDGE,
        ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.25',
                  facecolor='white', edgecolor=GREEN_EDGE, linewidth=1.0))

# Below-diagram derivation strip.
ax.text(0.7, -1.4,
        r"$i \cdot (3 + 2i) = 3i + 2i^2 = 3i + 2(-1) = -2 + 3i$",
        fontsize=14, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_title(r"Multiplication by $i$ = 90$\degree$ counterclockwise rotation",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-3.8, 4.5)
ax.set_ylim(-2.3, 4.6)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_fig2_mult_by_i.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_fig2_mult_by_i.png")
