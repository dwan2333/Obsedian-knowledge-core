"""Generate pi_fig2_pizza_area.png — visual derivation of A = pi * r^2 via
rearranging pie slices into an approximate rectangle of width r and length pi*r.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'; BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'; ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
TEXT = '#222'; MUTE = '#888'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal'); ax.axis('off')

# --- LEFT panel: the original circle of radius 1 ---
N_SLICES = 16
circ = mpatches.Circle((0, 0), 1, facecolor='none',
                       edgecolor=BLUE_EDGE, linewidth=2.0, zorder=3)
ax1.add_patch(circ)
for i in range(N_SLICES):
    a = 2 * math.pi * i / N_SLICES
    x, y = math.cos(a), math.sin(a)
    color = ORANGE if i % 2 else BLUE
    wedge = mpatches.Wedge((0, 0), 1,
                           360 * i / N_SLICES, 360 * (i + 1) / N_SLICES,
                           facecolor=color, edgecolor='white',
                           linewidth=1.2, alpha=0.55, zorder=2)
    ax1.add_patch(wedge)
# Radius label
ax1.annotate('', xy=(1, 0.0), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color=TEXT, lw=2.0))
ax1.text(0.5, -0.10, r'$r$', fontsize=14, color=TEXT,
         ha='center', va='top', fontweight='bold')
ax1.set_xlim(-1.4, 1.4); ax1.set_ylim(-1.4, 1.4)
ax1.set_title(r'Circle of radius $r$, sliced into 16 wedges',
              fontsize=12, color=BLUE_EDGE, fontweight='bold', pad=8)

# --- RIGHT panel: the wedges rearranged into a rectangle ---
# Width = r (vertical), Length = pi*r (horizontal)
# Top edge alternates wedge tips and crusts; bottom edge alternates the opposite.
# We'll draw 16 thin triangles arranged with bases alternating up/down.
L = math.pi  # length = pi * 1 (since r = 1)
W = 1        # height = r
wedge_w = L / (N_SLICES / 2)  # 8 wedges along top, 8 along bottom

# Bottom wedges: base on bottom (y=0), tip up
for i in range(N_SLICES // 2):
    color = ORANGE if i % 2 else BLUE
    x0 = i * 2 * wedge_w
    # Triangle vertices
    pts = [(x0, 0), (x0 + 2 * wedge_w, 0), (x0 + wedge_w, W)]
    poly = plt.Polygon(pts, facecolor=color, edgecolor='white',
                       linewidth=1.2, alpha=0.55, zorder=2)
    ax2.add_patch(poly)
# Top wedges: base on top (y=W), tip down — offset by wedge_w to interlock
for i in range(N_SLICES // 2):
    color = BLUE if i % 2 else ORANGE
    x0 = i * 2 * wedge_w + wedge_w  # offset
    pts = [(x0, W), (x0 + 2 * wedge_w, W), (x0 + wedge_w, 0)]
    poly = plt.Polygon(pts, facecolor=color, edgecolor='white',
                       linewidth=1.2, alpha=0.55, zorder=2)
    ax2.add_patch(poly)

# Bounding rectangle (dashed) for emphasis
rect = mpatches.Rectangle((0, 0), L, W, fill=False,
                          edgecolor=TEXT, linewidth=1.6,
                          linestyle='--', zorder=4)
ax2.add_patch(rect)

# Length label (pi*r)
ax2.annotate('', xy=(L, -0.18), xytext=(0, -0.18),
             arrowprops=dict(arrowstyle='<->', color=GREEN_EDGE, lw=1.8))
ax2.text(L / 2, -0.32, r'Length $= \pi r$',
         fontsize=14, color=GREEN_EDGE, ha='center', va='top',
         fontweight='bold')
# Width label (r)
ax2.annotate('', xy=(-0.18, W), xytext=(-0.18, 0),
             arrowprops=dict(arrowstyle='<->', color=GREEN_EDGE, lw=1.8))
ax2.text(-0.32, W / 2, r'Width $= r$',
         fontsize=14, color=GREEN_EDGE, ha='right', va='center',
         fontweight='bold', rotation=90)

# Final area formula
ax2.text(L / 2, W + 0.45,
         r'Area $= \pi r \times r = \pi r^2$',
         fontsize=15, color=BLUE_EDGE, ha='center', va='center',
         fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                   edgecolor='#aa8b3a', linewidth=1.6))

ax2.set_xlim(-0.55, L + 0.2)
ax2.set_ylim(-0.7, W + 0.95)
ax2.set_title('Slices rearranged into a rectangle',
              fontsize=12, color=ORANGE_EDGE, fontweight='bold', pad=8)

fig.suptitle(r'Why $A = \pi r^2$: rearrange the slices, get a rectangle of width $r$, length $\pi r$',
             fontsize=14, y=1.02, fontweight='bold')

plt.tight_layout()
plt.savefig('pi_fig2_pizza_area.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pi_fig2_pizza_area.png")
