"""Generate efm_fig1_unit_circle.png — Euler's formula on the unit circle.

A unit circle on the complex plane. A point on the circle at angle theta has
coordinates (cos theta, sin theta), labeled as both the Cartesian point AND
as the complex number e^(i*theta). The radius is drawn; perpendicular dashed
lines show cos(theta) and sin(theta) projections.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

T = np.radians(55.0)
P = np.array([np.cos(T), np.sin(T)])

fig, ax = plt.subplots(figsize=(9, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.45, -0.05, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.05, 1.45, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.8, zorder=2)
ax.add_patch(circ)

# Tick labels for 1, -1, i, -i.
for x, lbl in [(1, "1"), (-1, "-1")]:
    ax.plot([x, x], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.4, zorder=2)
    ax.text(x, -0.13, lbl, fontsize=11, color=BLUE_EDGE,
            ha='center', va='top', fontweight='bold')
for y, lbl in [(1, "i"), (-1, "-i")]:
    ax.plot([-0.04, 0.04], [y, y], color=BLUE_EDGE, linewidth=1.4, zorder=2)
    ax.text(-0.08, y, lbl, fontsize=11, color=BLUE_EDGE,
            ha='right', va='center', fontweight='bold')

# Radius to the point.
ax.plot([0, P[0]], [0, P[1]], color=ORANGE_EDGE, linewidth=2.8,
        solid_capstyle='round', zorder=3)
ax.scatter(P[0], P[1], s=72, color=ORANGE_EDGE, zorder=5)

# Cos and sin projections (dashed).
ax.plot([0, P[0]], [0, 0], color=GREEN_EDGE, linewidth=2.6, zorder=3)
ax.plot([P[0], P[0]], [0, P[1]], color=GREEN_EDGE, linewidth=2.0,
        linestyle='--', zorder=3)

# Angle theta arc.
arc = mpatches.Arc((0, 0), 0.5, 0.5, angle=0,
                   theta1=0, theta2=np.degrees(T),
                   color=ORANGE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc)
ax.text(0.32 * np.cos(T / 2), 0.32 * np.sin(T / 2), r"$\theta$",
        fontsize=16, color=ORANGE_EDGE, ha='center', va='center',
        fontweight='bold', zorder=5)

# Side labels.
ax.text(P[0] / 2.0, -0.07, r"$\cos\theta$", fontsize=14, color=GREEN_EDGE,
        ha='center', va='top', fontweight='bold')
ax.text(P[0] + 0.04, P[1] / 2.0, r"$\sin\theta$", fontsize=14, color=GREEN_EDGE,
        ha='left', va='center', fontweight='bold')

# Label the point with TWO names: the Cartesian coordinates and e^(i*theta).
ax.text(P[0] + 0.06, P[1] + 0.10,
        r"$(\cos\theta,\,\sin\theta)$",
        fontsize=13, color=ORANGE_EDGE,
        ha='left', va='bottom', fontweight='bold')
ax.text(P[0] + 0.06, P[1] - 0.06,
        r"$= e^{i\theta}$",
        fontsize=15, color=ORANGE_EDGE,
        ha='left', va='top', fontweight='bold')

# Below-diagram boxed identity.
ax.text(0.0, -1.50,
        r"$e^{i\theta} = \cos\theta + i\sin\theta$",
        fontsize=18, color=TEXT, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_title("Euler's formula on the unit circle",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-1.55, 1.85)
ax.set_ylim(-2.05, 1.45)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efm_fig1_unit_circle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efm_fig1_unit_circle.png")
