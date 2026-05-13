"""Generate cnf_fig3_rotation_number.png — the rotation number cos(theta) + i sin(theta).

A unit circle on the complex plane. A point on the unit circle at angle theta
has coordinates (cos(theta), sin(theta)). The radius is drawn to that point;
the horizontal projection labeled cos(theta), the vertical projection labeled
sin(theta). This is the foundational picture for connecting complex numbers to
trig identities — multiplying by this point rotates the plane by theta.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

T = np.radians(50.0)
P = np.array([np.cos(T), np.sin(T)])

fig, ax = plt.subplots(figsize=(8, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.35, -0.04, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.04, 1.35, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.8, zorder=2)
ax.add_patch(circ)

# Tick labels at 1, -1, i, -i on the axes.
for x, lbl in [(1, "1"), (-1, "-1")]:
    ax.plot([x, x], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.5, zorder=2)
    ax.text(x, -0.10, lbl, fontsize=11, color=BLUE_EDGE,
            ha='center', va='top', fontweight='bold')
for y, lbl in [(1, "i"), (-1, "-i")]:
    ax.plot([-0.04, 0.04], [y, y], color=BLUE_EDGE, linewidth=1.5, zorder=2)
    ax.text(-0.08, y, lbl, fontsize=11, color=BLUE_EDGE,
            ha='right', va='center', fontweight='bold')

# Radius to the point.
ax.plot([0, P[0]], [0, P[1]], color=ORANGE_EDGE, linewidth=2.8,
        solid_capstyle='round', zorder=3)
ax.scatter(P[0], P[1], s=70, color=ORANGE_EDGE, zorder=5)

# Horizontal projection (cos).
ax.plot([0, P[0]], [0, 0], color=GREEN_EDGE, linewidth=3.4,
        solid_capstyle='round', zorder=3)
# Vertical projection (sin).
ax.plot([P[0], P[0]], [0, P[1]], color=GREEN_EDGE, linewidth=2.4,
        linestyle='--', zorder=3)

# Angle theta arc at origin.
arc = mpatches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0,
                   theta2=np.degrees(T),
                   color=ORANGE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc)
ax.text(0.27 * np.cos(T / 2), 0.27 * np.sin(T / 2), r"$\theta$",
        fontsize=15, color=ORANGE_EDGE, ha='center', va='center',
        fontweight='bold', zorder=5)

# Label the radius "1" perpendicular-offset.
mid_OP = P / 2.0
OP_unit = P / np.linalg.norm(P)
normal = np.array([-OP_unit[1], OP_unit[0]])
if normal[0] < 0:
    normal = -normal
pos1 = mid_OP + 0.10 * normal
ax.text(pos1[0], pos1[1], r"$1$", fontsize=13, color=ORANGE_EDGE,
        ha='center', va='center', fontweight='bold',
        rotation=np.degrees(np.arctan2(OP_unit[1], OP_unit[0])))

# Label cos(theta) below the horizontal projection.
ax.text(P[0] / 2, -0.10, r"$\cos\theta$", fontsize=14, color=GREEN_EDGE,
        ha='center', va='top', fontweight='bold')
# Label sin(theta) to the right of the vertical projection.
ax.text(P[0] + 0.04, P[1] / 2, r"$\sin\theta$", fontsize=14,
        color=GREEN_EDGE, ha='left', va='center', fontweight='bold')

# Label the point itself with the complex number form.
ax.text(P[0] + 0.05, P[1] + 0.05,
        r"$\cos\theta + i\sin\theta$",
        fontsize=13, color=ORANGE_EDGE,
        ha='left', va='bottom', fontweight='bold')

# Below-diagram annotation strip.
ax.text(0.0, -1.30,
        r"$z = \cos\theta + i\sin\theta$"
        "\nMultiplying any complex number by this $z$ rotates it by $\\theta$.",
        fontsize=12, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_title("The rotation number on the unit circle",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-1.45, 1.55)
ax.set_ylim(-1.75, 1.45)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_fig3_rotation_number.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_fig3_rotation_number.png")
