"""Generate efc_fig1_cart_polar.png — Cartesian = polar representation of a complex number.

A point z in the first quadrant of the complex plane shown with BOTH its
Cartesian coordinates (x, y) and polar coordinates (r, theta). Right triangle
visible. Both labels z = x + iy and z = r*e^(i*theta) shown.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
ORANGE_EDGE = '#8c4f1f'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'

# Pick a point in the first quadrant.
T = np.radians(38.0)
R = 2.6
P = np.array([R * np.cos(T), R * np.sin(T)])
Q = np.array([P[0], 0])  # foot of perpendicular

fig, ax = plt.subplots(figsize=(10, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(3.4, -0.15, "Re(z)", fontsize=13, color=MUTE,
        ha='right', va='top', style='italic')
ax.text(-0.10, 2.3, "Im(z)", fontsize=13, color=MUTE,
        ha='right', va='top', style='italic', rotation=90)

# Light grid.
for g in [-1, 1, 2, 3]:
    ax.axhline(g, color='#eeeeee', linewidth=0.5, zorder=0)
    ax.axvline(g, color='#eeeeee', linewidth=0.5, zorder=0)

# Right triangle.
ax.plot([0, P[0]], [0, 0], color=GREEN_EDGE, linewidth=2.8,
        solid_capstyle='round', zorder=3)  # x leg
ax.plot([P[0], P[0]], [0, P[1]], color=GREEN_EDGE, linewidth=2.8,
        solid_capstyle='round', zorder=3)  # y leg
ax.plot([0, P[0]], [0, P[1]], color=ORANGE_EDGE, linewidth=3.0,
        solid_capstyle='round', zorder=3)  # hypotenuse r

# Right-angle marker at Q.
ra = 0.10
ax.plot([Q[0] - ra, Q[0] - ra, Q[0]],
        [Q[1], Q[1] + ra, Q[1] + ra],
        color=GREEN_EDGE, linewidth=1.4, zorder=4)

# Angle theta arc at origin.
arc = mpatches.Arc((0, 0), 0.6, 0.6, angle=0,
                   theta1=0, theta2=np.degrees(T),
                   color=PURPLE_EDGE, linewidth=2.2, zorder=4)
ax.add_patch(arc)
ax.text(0.42 * np.cos(T / 2), 0.42 * np.sin(T / 2), r"$\theta$",
        fontsize=17, color=PURPLE_EDGE, ha='center', va='center',
        fontweight='bold', zorder=5)

# Side labels.
ax.text(P[0] / 2, -0.16, r"$x$", fontsize=15, color=GREEN_EDGE,
        ha='center', va='top', fontweight='bold')
ax.text(P[0] + 0.08, P[1] / 2, r"$y$", fontsize=15, color=GREEN_EDGE,
        ha='left', va='center', fontweight='bold')
# r label on the hypotenuse, perpendicular-offset.
mid = P / 2
norm = np.array([-P[1], P[0]]) / np.linalg.norm(P)
lbl_r = mid + 0.16 * norm
ax.text(lbl_r[0], lbl_r[1], r"$r$", fontsize=16, color=ORANGE_EDGE,
        ha='center', va='center', fontweight='bold',
        rotation=np.degrees(T))

# Point dot.
ax.scatter(P[0], P[1], s=85, color=BLUE_EDGE,
           edgecolor='white', linewidth=2, zorder=6)
# Foot of perpendicular dot.
ax.scatter(Q[0], Q[1], s=42, color=GREEN_EDGE, zorder=5)

# Point label with both forms.
ax.annotate('', xy=(P[0], P[1]),
            xytext=(P[0] + 0.55, P[1] + 0.45),
            arrowprops=dict(arrowstyle='-', color='#888888', lw=1.0),
            zorder=3)
ax.text(P[0] + 0.60, P[1] + 0.55,
        r"$z = x + i\,y$" "\n" r"$= r\,e^{i\theta}$",
        fontsize=14, color=BLUE_EDGE,
        ha='left', va='bottom', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#f0f4fa',
                  edgecolor=BLUE_EDGE, linewidth=1.4))

# Below: derivation hint.
ax.text(1.5, -0.95,
        r"$x = r\cos\theta$,    $y = r\sin\theta$    $\Rightarrow$    "
        r"$e^{i\theta} = \cos\theta + i\sin\theta$",
        fontsize=13, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_title("Cartesian = polar: equate the two forms to derive Euler's formula",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-0.6, 4.2)
ax.set_ylim(-1.5, 3.0)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efc_fig1_cart_polar.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efc_fig1_cart_polar.png")
