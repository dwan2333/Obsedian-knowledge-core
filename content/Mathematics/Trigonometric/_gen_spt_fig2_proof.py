"""Generate spt_fig2_proof.png — the Sneaky Proof of the Pythagorean Identity.

The same triangle as fig1, but with the altitude dropped from the right-angle
vertex B onto the hypotenuse AC. That altitude meets AC at the foot F, splitting
AC into:
  - lower segment AF, of length S = cos^2(theta)
  - upper segment FC, of length S' = sin^2(theta)
Both sub-triangles ABF and BCF are similar to the original triangle ABC.
The angle theta appears at A (original), at B (lower sub-triangle's bottom-left
vertex, same as A — same angle, just emphasised), and at B in the upper
sub-triangle (via the angle chase alpha + theta + 90 = 180).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_FACE, BLUE_EDGE = '#4a90e2', '#1f4f8c'
GREEN_FACE, GREEN_EDGE = '#7bb55c', '#3d7530'
PURPLE_FACE, PURPLE_EDGE = '#b76db4', '#6e3a6c'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'

# Same proportions as fig1 (3-4-5).
A = np.array([0.0, 0.0])  # angle theta vertex (bottom-left)
B = np.array([4.0, 0.0])  # right-angle vertex (bottom-right)
C = np.array([4.0, 3.0])  # top vertex (angle alpha)

# Foot of perpendicular from B onto line AC.
# Project (B - A) onto unit vector along (C - A).
AC = C - A
AC_unit = AC / np.linalg.norm(AC)
F = A + np.dot(B - A, AC_unit) * AC_unit  # exact F

fig, ax = plt.subplots(figsize=(10, 7.2))

# Lower sub-triangle ABF: green-tinted fill.
tri_low = mpatches.Polygon([A, B, F], closed=True,
                           facecolor=GREEN_FACE, alpha=0.22,
                           edgecolor=GREEN_EDGE, linewidth=2.2, zorder=2)
ax.add_patch(tri_low)
# Upper sub-triangle FBC: purple-tinted fill.
tri_up = mpatches.Polygon([F, B, C], closed=True,
                          facecolor=PURPLE_FACE, alpha=0.22,
                          edgecolor=PURPLE_EDGE, linewidth=2.2, zorder=2)
ax.add_patch(tri_up)

# Heavy outline of big triangle on top.
big = mpatches.Polygon([A, B, C], closed=True,
                       fill=False, edgecolor=BLUE_EDGE, linewidth=2.6,
                       zorder=3)
ax.add_patch(big)

# Altitude BF as a dashed line.
ax.plot([B[0], F[0]], [B[1], F[1]],
        color='#444444', linewidth=1.8, linestyle='--', zorder=3)

# Right-angle markers.
# At B (bottom-right): along the inside.
ra = 0.22
ax.plot([B[0] - ra, B[0] - ra, B[0]],
        [B[1], B[1] + ra, B[1] + ra],
        color=BLUE_EDGE, linewidth=1.5, zorder=4)
# At F (foot of altitude on AC): small square on the AC side, on the side
# where B is (interior of the triangle).
# Square axes: along AC and perpendicular toward B.
perp = np.array([-AC_unit[1], AC_unit[0]])
# Make sure perp points toward B (interior).
if np.dot(perp, B - F) < 0:
    perp = -perp
p1 = F - ra * AC_unit
p2 = p1 + ra * perp
p3 = F + ra * perp
ax.plot([p1[0], p2[0], p3[0]],
        [p1[1], p2[1], p3[1]],
        color='#444444', linewidth=1.4, zorder=4)

# Angle theta at A (original triangle).
theta_deg = np.degrees(np.arctan2(C[1] - A[1], C[0] - A[0]))
arc_A = mpatches.Arc(A, 0.95, 0.95, angle=0,
                     theta1=0, theta2=theta_deg,
                     color=ORANGE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_A)
ax.text(0.62, 0.18, r"$\theta$", fontsize=18, color=ORANGE_EDGE,
        ha='left', va='bottom', fontweight='bold', zorder=5)

# Angle alpha at C (top of big triangle).
# Vector CA and CB.
CA = (A - C); CA_ang = np.degrees(np.arctan2(CA[1], CA[0]))
CB = (B - C); CB_ang = np.degrees(np.arctan2(CB[1], CB[0]))
# Arc goes from smaller angle to larger angle.
arc_C = mpatches.Arc(C, 1.2, 1.2, angle=0,
                     theta1=min(CA_ang, CB_ang),
                     theta2=max(CA_ang, CB_ang),
                     color=PURPLE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_C)
ax.text(C[0] - 0.55, C[1] - 0.55, r"$\alpha$", fontsize=17,
        color=PURPLE_EDGE, ha='center', va='center',
        fontweight='bold', zorder=5)

# Angle theta at B (upper sub-triangle): between BC and BF.
# Vector BC and BF.
BC = (C - B); BC_ang = np.degrees(np.arctan2(BC[1], BC[0]))
BF = (F - B); BF_ang = np.degrees(np.arctan2(BF[1], BF[0]))
arc_B_up = mpatches.Arc(B, 0.75, 0.75, angle=0,
                        theta1=min(BC_ang, BF_ang),
                        theta2=max(BC_ang, BF_ang),
                        color=ORANGE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_B_up)
# Label position: midpoint of the arc, just inside.
mid_ang = np.radians((BC_ang + BF_ang) / 2)
lx = B[0] + 0.55 * np.cos(mid_ang)
ly = B[1] + 0.55 * np.sin(mid_ang)
ax.text(lx, ly, r"$\theta$", fontsize=15, color=ORANGE_EDGE,
        ha='center', va='center', fontweight='bold', zorder=5)

# Side labels of the big triangle.
ax.text(2.0, -0.32, r"$\cos\theta$", fontsize=16, color=TEXT,
        ha='center', va='top', fontweight='bold')
ax.text(4.2, 1.5, r"$\sin\theta$", fontsize=16, color=TEXT,
        ha='left', va='center', fontweight='bold')

# Segment labels on the hypotenuse: AF = S = cos^2(theta), FC = S' = sin^2(theta).
# Place each label outward-normal from each segment's midpoint.
def offset_label(p_from, p_to, text, color, fontsize=15, distance=0.42):
    mid = (p_from + p_to) / 2
    direction = (p_to - p_from); direction = direction / np.linalg.norm(direction)
    normal = np.array([-direction[1], direction[0]])
    pos = mid + distance * normal
    ax.text(pos[0], pos[1], text,
            fontsize=fontsize, color=color,
            ha='center', va='center', fontweight='bold',
            rotation=np.degrees(np.arctan2(direction[1], direction[0])),
            zorder=6)

offset_label(A, F, r"$S=\cos^2\theta$", GREEN_EDGE)
offset_label(F, C, r"$S'=\sin^2\theta$", PURPLE_EDGE)

# Vertex dots.
for v in [A, B, C, F]:
    ax.scatter(v[0], v[1], s=42, color=BLUE_EDGE, zorder=6)

# Identity at the bottom, boxed.
ax.text(2.0, -1.2,
        r"$1 \;=\; \cos^2\theta \;+\; \sin^2\theta$",
        fontsize=20, color=TEXT, ha='center', va='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.8))

ax.set_title("Drop the altitude — the hypotenuse splits into "
             r"$\cos^2\theta$ + $\sin^2\theta$",
             fontsize=14, pad=14, color=TEXT)

ax.set_xlim(-0.9, 6.0)
ax.set_ylim(-1.9, 4.0)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('spt_fig2_proof.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved spt_fig2_proof.png")
