"""Generate pi_fig1_polygon_bounds.png — inscribed hexagon (lower bound) and
circumscribed square (upper bound) on the same circle to show 3 < pi < 4."""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
TEXT = '#222'; MUTE = '#888'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
for ax in (ax1, ax2):
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
    # Unit circle (radius 1, diameter 2)
    ax.add_patch(mpatches.Circle((0, 0), 1, fill=False,
                                 edgecolor=BLUE_EDGE, linewidth=2.4, zorder=3))
    # Diameter line, labeled "2"
    ax.plot([-1, 1], [0, 0], color=MUTE, linewidth=1.0,
            linestyle='--', zorder=2)

# --- LEFT panel: inscribed hexagon (perimeter 6) ---
hex_angles = [math.pi / 3 * i + math.pi / 2 for i in range(7)]
hx = [math.cos(a) for a in hex_angles]
hy = [math.sin(a) for a in hex_angles]
ax1.fill(hx, hy, facecolor=GREEN_EDGE, alpha=0.18, edgecolor=GREEN_EDGE,
         linewidth=2.4, zorder=4)
# Equilateral-triangle subdivision (lines from center to vertices)
for x, y in zip(hx[:-1], hy[:-1]):
    ax1.plot([0, x], [0, y], color=GREEN_EDGE, linewidth=0.9,
             linestyle=':', alpha=0.7, zorder=4)
# Side-length label "1" on each side
for i in range(6):
    midx = (hx[i] + hx[i+1]) / 2
    midy = (hy[i] + hy[i+1]) / 2
    ax1.text(midx * 1.12, midy * 1.12, '1', fontsize=11,
             color=GREEN_EDGE, ha='center', va='center', fontweight='bold')
# Diameter label "2"
ax1.text(0, -0.12, '2', fontsize=12, color=MUTE,
         ha='center', va='top', fontweight='bold')
# Perimeter and bound
ax1.text(0, -1.85, r'Inscribed hexagon: perimeter $= 6$',
         fontsize=12, ha='center', color=GREEN_EDGE, fontweight='bold')
ax1.text(0, -2.05, r'$C > 6 \;\Rightarrow\; \pi > \dfrac{6}{2} = 3$',
         fontsize=14, ha='center', color=GREEN_EDGE, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f1d8',
                   edgecolor=GREEN_EDGE))
ax1.set_ylim(-2.4, 1.6)
ax1.set_title('Lower bound', fontsize=13, color=GREEN_EDGE,
              fontweight='bold', pad=10)

# --- RIGHT panel: circumscribed square (perimeter 8) ---
sq = mpatches.Rectangle((-1, -1), 2, 2, facecolor=ORANGE_EDGE, alpha=0.12,
                        edgecolor=ORANGE_EDGE, linewidth=2.4, zorder=4)
ax2.add_patch(sq)
# Side-length label "2" on each side
ax2.text(0, 1.12, '2', fontsize=11, color=ORANGE_EDGE,
         ha='center', va='bottom', fontweight='bold')
ax2.text(0, -1.12, '2', fontsize=11, color=ORANGE_EDGE,
         ha='center', va='top', fontweight='bold')
ax2.text(-1.12, 0, '2', fontsize=11, color=ORANGE_EDGE,
         ha='right', va='center', fontweight='bold')
ax2.text(1.12, 0, '2', fontsize=11, color=ORANGE_EDGE,
         ha='left', va='center', fontweight='bold')
# Diameter label
ax2.text(0, -0.12, '2', fontsize=12, color=MUTE,
         ha='center', va='top', fontweight='bold')
ax2.text(0, -1.85, r'Circumscribed square: perimeter $= 8$',
         fontsize=12, ha='center', color=ORANGE_EDGE, fontweight='bold')
ax2.text(0, -2.05, r'$C < 8 \;\Rightarrow\; \pi < \dfrac{8}{2} = 4$',
         fontsize=14, ha='center', color=ORANGE_EDGE, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffeed8',
                   edgecolor=ORANGE_EDGE))
ax2.set_ylim(-2.4, 1.6)
ax2.set_title('Upper bound', fontsize=13, color=ORANGE_EDGE,
              fontweight='bold', pad=10)

fig.suptitle(r'Archimedes\' two bounds: $3 < \pi < 4$',
             fontsize=14, y=0.98, fontweight='bold')

plt.tight_layout()
plt.savefig('pi_fig1_polygon_bounds.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pi_fig1_polygon_bounds.png")
