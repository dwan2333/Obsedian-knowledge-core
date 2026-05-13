"""Generate spt_fig3_unit_circle.png — cos^2(theta) on the unit circle.

Unit circle centered at origin; point P = (cos T, sin T) in the first quadrant.
Triangle OQP with O=(0,0), Q=(cos T, 0), P=(cos T, sin T):
  - bottom leg OQ has length cos(theta)
  - right leg QP has length sin(theta)
  - hypotenuse OP has length 1
Drop altitude from Q onto OP. Foot F = (cos^2 T) * (cos T, sin T).
The segment OF along the radius has length cos^2(theta) — bold-highlighted.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

# Pick a wider angle so the radius is more horizontal-leaning,
# which makes the cos^2(theta) segment visually distinguishable.
T = np.radians(38.0)
O = np.array([0.0, 0.0])
P = np.array([np.cos(T), np.sin(T)])
Q = np.array([np.cos(T), 0.0])
F = np.dot(Q, P) * P  # length OF = cos^2(T)

fig, ax = plt.subplots(figsize=(10, 8))

# Axes lines.
ax.axhline(0, color=MUTE, linewidth=0.8, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.8, zorder=1)
ax.text(1.30, -0.04, "x", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.04, 1.30, "y", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle(O, 1.0, fill=False,
                       edgecolor=MUTE, linewidth=1.4, zorder=2)
ax.add_patch(circ)

# Triangle OQP — bottom leg (cos), right leg (sin), hypotenuse (radius).
ax.plot([O[0], Q[0]], [O[1], Q[1]], color=GREEN_EDGE, linewidth=2.4, zorder=3)
ax.plot([Q[0], P[0]], [Q[1], P[1]], color=GREEN_EDGE, linewidth=2.4, zorder=3)
# Radius OP — drawn in two parts to show the bold segment clearly.
# First: the bold OF segment (= cos^2 theta) in orange.
ax.plot([O[0], F[0]], [O[1], F[1]],
        color=ORANGE_EDGE, linewidth=5.0, solid_capstyle='round', zorder=4)
# Then: the remaining FP segment in regular blue.
ax.plot([F[0], P[0]], [F[1], P[1]], color=BLUE_EDGE, linewidth=2.0, zorder=3)

# Altitude QF as dashed.
ax.plot([Q[0], F[0]], [Q[1], F[1]],
        color='#444444', linewidth=1.6, linestyle='--', zorder=3)

# Right-angle marker at Q.
ra = 0.05
ax.plot([Q[0] - ra, Q[0] - ra, Q[0]],
        [Q[1], Q[1] + ra, Q[1] + ra],
        color=GREEN_EDGE, linewidth=1.5, zorder=5)
# Right-angle marker at F.
OP_unit = P / np.linalg.norm(P)
perp = np.array([-OP_unit[1], OP_unit[0]])
if np.dot(perp, Q - F) < 0:
    perp = -perp
p1 = F - ra * OP_unit
p2 = p1 + ra * perp
p3 = F + ra * perp
ax.plot([p1[0], p2[0], p3[0]],
        [p1[1], p2[1], p3[1]],
        color='#444444', linewidth=1.3, zorder=5)

# Angle theta at origin — bigger arc, label placed clearly inside.
arc_O = mpatches.Arc(O, 0.5, 0.5, angle=0,
                     theta1=0, theta2=np.degrees(T),
                     color=ORANGE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_O)
# Label theta INSIDE the angle, between the x-axis and the radius,
# at half the angle radius.
theta_label_r = 0.18
theta_label_ang = T / 2.0
ax.text(theta_label_r * np.cos(theta_label_ang),
        theta_label_r * np.sin(theta_label_ang),
        r"$\theta$", fontsize=15, color=ORANGE_EDGE,
        ha='center', va='center', fontweight='bold', zorder=5)

# Side labels for the inner triangle — pushed well away from clutter.
# cos(theta) — below the x-axis along the bottom leg.
ax.text(Q[0] / 2.0, -0.06, r"$\cos\theta$", fontsize=14, color=GREEN_EDGE,
        ha='center', va='top', fontweight='bold')
# sin(theta) — to the right of the right leg.
ax.text(Q[0] + 0.03, (Q[1] + P[1]) / 2.0, r"$\sin\theta$",
        fontsize=14, color=GREEN_EDGE, ha='left', va='center',
        fontweight='bold')
# "1" on the FP portion of the radius (not on OF, which is now the bold cos^2
# segment). Place it perpendicular-offset OUTSIDE (above-left).
mid_FP = (F + P) / 2.0
outward = np.array([-OP_unit[1], OP_unit[0]])
# Make sure outward points AWAY from the triangle interior (i.e. up-left).
if outward[0] > 0:
    outward = -outward
pos_one = mid_FP + 0.10 * outward
ax.text(pos_one[0], pos_one[1], r"$1$", fontsize=14, color=BLUE_EDGE,
        ha='center', va='center', fontweight='bold',
        rotation=np.degrees(np.arctan2(OP_unit[1], OP_unit[0])))

# Vertex markers.
ax.scatter(P[0], P[1], s=42, color=BLUE_EDGE, zorder=6)
ax.scatter(O[0], O[1], s=36, color=BLUE_EDGE, zorder=6)
ax.scatter(Q[0], Q[1], s=32, color=GREEN_EDGE, zorder=6)
ax.scatter(F[0], F[1], s=44, color=ORANGE_EDGE, zorder=6)

# Point label P (outside the circle, top-right).
ax.text(P[0] + 0.04, P[1] + 0.05, r"$(\cos\theta,\sin\theta)$",
        fontsize=11, color=BLUE_EDGE, ha='left', va='bottom')

# Bold-segment label cos^2(theta) — placed BELOW the diagram with a leader arrow
# pointing to the segment. This puts it well clear of the theta-arc clutter.
ax.annotate(r"$\cos^2\theta$" "\n(bold segment along the radius)",
            xy=((F[0] + 0.0) / 2.0, (F[1] + 0.0) / 2.0),
            xytext=(-0.55, -0.55),
            fontsize=14, color=ORANGE_EDGE, fontweight='bold',
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=1.6,
                            connectionstyle='arc3,rad=0.2'))

# Title.
ax.set_title(r"Where $\cos^2\theta$ lives on the unit circle",
             fontsize=14, pad=12, color=TEXT)

ax.set_xlim(-1.30, 1.45)
ax.set_ylim(-0.95, 1.40)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('spt_fig3_unit_circle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved spt_fig3_unit_circle.png")
