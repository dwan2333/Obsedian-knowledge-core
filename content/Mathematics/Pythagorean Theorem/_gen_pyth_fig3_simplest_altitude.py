"""Generate pyth_fig3_simplest_altitude.png — the "simplest proof".

Right triangle with the right angle at the origin (legs A vertical, B horizontal,
hypotenuse C). Drop the altitude from the right-angle vertex onto the hypotenuse;
its foot F splits the triangle into two smaller triangles, each SIMILAR to the
whole. The shape "attached to each side" is the triangle itself, so
Area(small) + Area(medium) = Area(large) holds by construction.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

A, B = 3.0, 4.0                 # legs: A vertical, B horizontal
O = np.array([0.0, 0.0])        # right-angle vertex
P = np.array([B, 0.0])          # foot of horizontal leg
Q = np.array([0.0, A])          # top of vertical leg

BLUE_EDGE = '#1f4f8c'
GREEN = ('#8fc873', '#3d7530')
PURPLE = ('#b76db4', '#6e3a6c')
TEXT = '#222222'

# Foot F of the perpendicular from O onto line P-Q.
PQ = Q - P
PQu = PQ / np.linalg.norm(PQ)
F = P + np.dot(O - P, PQu) * PQu

fig, ax = plt.subplots(figsize=(8.6, 7.0))

# Two sub-triangles (shaded).
ax.add_patch(mpatches.Polygon([O, P, F], closed=True, facecolor=GREEN[0],
             alpha=0.30, edgecolor=GREEN[1], linewidth=2.0, zorder=2))
ax.add_patch(mpatches.Polygon([O, F, Q], closed=True, facecolor=PURPLE[0],
             alpha=0.30, edgecolor=PURPLE[1], linewidth=2.0, zorder=2))
# Big triangle outline on top.
ax.add_patch(mpatches.Polygon([O, P, Q], closed=True, fill=False,
             edgecolor=BLUE_EDGE, linewidth=2.6, zorder=3))
# Altitude OF dashed.
ax.plot([O[0], F[0]], [O[1], F[1]], color='#444444', linewidth=1.8,
        linestyle='--', zorder=3)

# Right-angle marker at O (between the two legs).
r = 0.28
ax.plot([r, r, 0], [0, r, r], color=BLUE_EDGE, linewidth=1.5, zorder=4)
# Right-angle marker at F (altitude meets hypotenuse).
perp = np.array([-PQu[1], PQu[0]])
if np.dot(perp, O - F) < 0:
    perp = -perp
a1 = F - r * PQu
a2 = a1 + r * perp
a3 = F + r * perp
ax.plot([a1[0], a2[0], a3[0]], [a1[1], a2[1], a3[1]],
        color='#444444', linewidth=1.4, zorder=4)

# Side labels.
ax.text(-0.28, A / 2, r"$A$", fontsize=18, ha='right', va='center',
        color=TEXT, fontweight='bold')
ax.text(B / 2, -0.30, r"$B$", fontsize=18, ha='center', va='top',
        color=TEXT, fontweight='bold')
mid_hyp = (P + Q) / 2
ax.text(mid_hyp[0] + 0.30, mid_hyp[1] + 0.22, r"$C$", fontsize=18,
        ha='left', va='bottom', color=TEXT, fontweight='bold')
# Altitude label.
mid_alt = (O + F) / 2
ax.text(mid_alt[0] + 0.10, mid_alt[1] - 0.12, r"$h$", fontsize=14,
        ha='left', va='top', color='#444444')

# Vertex dots.
for v in (O, P, Q, F):
    ax.scatter(v[0], v[1], s=40, color=BLUE_EDGE, zorder=5)

# Caption identity.
ax.text(2.0, -1.45,
        r"$\mathrm{Area}_{\rm small} + \mathrm{Area}_{\rm medium} = \mathrm{Area}_{\rm large}$",
        fontsize=15, ha='center', va='center', color=TEXT, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.45', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))
ax.text(2.0, -2.25, "all three triangles are similar", fontsize=12,
        ha='center', va='center', color='#555555', style='italic')

ax.set_title("Drop one altitude: the triangle splits into two similar copies",
             fontsize=13, pad=12, color=TEXT)
ax.set_xlim(-1.2, 4.7)
ax.set_ylim(-2.8, 3.7)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('pyth_fig3_simplest_altitude.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pyth_fig3_simplest_altitude.png")
