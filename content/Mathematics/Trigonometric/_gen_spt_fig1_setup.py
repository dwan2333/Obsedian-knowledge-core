"""Generate spt_fig1_setup.png — the unit-circle right triangle re-drawn standalone.

Legs sin(theta) (vertical, right) and cos(theta) (horizontal, bottom),
hypotenuse 1 (diagonal), right angle bottom-right, angle theta bottom-left.
Mirrors what Grant Sanderson draws at 1:05:14-1:06:01 of Lockdown math ep. 3.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_FACE, BLUE_EDGE = '#4a90e2', '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
TEXT, MUTE = '#222222', '#666666'

# Place vertices. Use a 3-4-5 style proportion for visual clarity.
# Bottom-left = (0,0), bottom-right = (4,0), top-right = (4,3).
# That maps to: angle theta at (0,0), right angle at (4,0).
# cos(theta) = 4/5 = 0.8, sin(theta) = 3/5 = 0.6. theta = arctan(3/4).
A = np.array([0.0, 0.0])  # angle theta vertex
B = np.array([4.0, 0.0])  # right angle vertex
C = np.array([4.0, 3.0])  # top vertex

fig, ax = plt.subplots(figsize=(8, 6))

# Triangle as a filled polygon (light blue with darker edge).
tri = mpatches.Polygon([A, B, C], closed=True,
                       facecolor=BLUE_FACE, alpha=0.18,
                       edgecolor=BLUE_EDGE, linewidth=2.5,
                       zorder=2)
ax.add_patch(tri)

# Right-angle marker at B.
ra_size = 0.25
ax.plot([B[0] - ra_size, B[0] - ra_size, B[0]],
        [B[1], B[1] + ra_size, B[1] + ra_size],
        color=BLUE_EDGE, linewidth=1.6, zorder=3)

# Angle theta arc at A.
arc = mpatches.Arc(A, 0.9, 0.9, angle=0,
                   theta1=0, theta2=np.degrees(np.arctan2(C[1] - A[1], C[0] - A[0])),
                   color=ORANGE_EDGE, linewidth=2.2, zorder=3)
ax.add_patch(arc)
ax.text(0.62, 0.22, r"$\theta$", fontsize=20, color=ORANGE_EDGE,
        ha='left', va='bottom', fontweight='bold', zorder=4)

# Side labels.
# Bottom leg: cos(theta).
ax.text(2.0, -0.28, r"$\cos\theta$", fontsize=18, color=TEXT,
        ha='center', va='top', fontweight='bold')
# Right leg: sin(theta).
ax.text(4.18, 1.5, r"$\sin\theta$", fontsize=18, color=TEXT,
        ha='left', va='center', fontweight='bold')
# Hypotenuse: label "1" perpendicular-offset from midpoint.
hyp_mid = (A + C) / 2.0
# Outward-normal direction (up-left of hyp).
hyp_dir = (C - A) / np.linalg.norm(C - A)
hyp_norm = np.array([-hyp_dir[1], hyp_dir[0]])
label_pos = hyp_mid + 0.32 * hyp_norm
ax.text(label_pos[0], label_pos[1], r"$1$", fontsize=20, color=TEXT,
        ha='center', va='center', fontweight='bold',
        rotation=np.degrees(np.arctan2(hyp_dir[1], hyp_dir[0])))

# Vertex dots.
for v in [A, B, C]:
    ax.scatter(v[0], v[1], s=42, color=BLUE_EDGE, zorder=5)

# Vertex labels (small, italic).
ax.text(A[0] - 0.12, A[1] - 0.12, "", fontsize=10)  # plain corner

# Title strip.
ax.set_title("Setup — the unit-circle right triangle, re-drawn standalone",
             fontsize=14, pad=16, color=TEXT)

ax.set_xlim(-0.7, 5.4)
ax.set_ylim(-0.9, 3.7)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('spt_fig1_setup.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved spt_fig1_setup.png")
