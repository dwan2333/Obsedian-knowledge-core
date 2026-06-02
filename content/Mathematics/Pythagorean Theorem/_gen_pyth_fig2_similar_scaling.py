"""Generate pyth_fig2_similar_scaling.png — the similar-triangles scaling proof.

The base 3-4-5 triangle is scaled by C, by A and by B. The three copies
interlock into one rectangle (25 wide x 12 tall, using A=3,B=4,C=5):
  - x C  (blue)   : right-angle vertex at (9,12); hypotenuse CC = C^2 is the base
  - x A  (green)  : left piece, top edge AA = A^2
  - x B  (orange) : right piece, top edge BB = B^2
Bottom edge C^2 = top edge (A^2 + B^2)  =>  A^2 + B^2 = C^2.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE = ('#7fb0e0', '#1f4f8c')
GREEN = ('#8fc873', '#3d7530')
ORANGE = ('#e0a85c', '#8c5a1f')
TEXT = '#222222'

W, H = 25.0, 12.0
apex = (9.0, 12.0)            # right-angle vertex of the xC triangle

fig, ax = plt.subplots(figsize=(11.5, 6.4))

# xC triangle (blue): base is the bottom edge = C^2
ax.add_patch(mpatches.Polygon([(0, 0), (W, 0), apex], closed=True,
             facecolor=BLUE[0], edgecolor=BLUE[1], linewidth=2.2,
             alpha=0.92, zorder=2))
# xA triangle (green): left
ax.add_patch(mpatches.Polygon([(0, 0), apex, (0, H)], closed=True,
             facecolor=GREEN[0], edgecolor=GREEN[1], linewidth=2.2,
             alpha=0.92, zorder=2))
# xB triangle (orange): right
ax.add_patch(mpatches.Polygon([(W, 0), (W, H), apex], closed=True,
             facecolor=ORANGE[0], edgecolor=ORANGE[1], linewidth=2.2,
             alpha=0.92, zorder=2))
# rectangle outline
ax.add_patch(mpatches.Rectangle((0, 0), W, H, fill=False,
             edgecolor='#444444', linewidth=2.4, zorder=4))

# Edge labels
ax.text(W / 2, -1.1, r"$C^2 = C\cdot C$", fontsize=18, ha='center', va='top',
        color=BLUE[1], fontweight='bold')
ax.text(apex[0] / 2, H + 0.5, r"$A^2$", fontsize=17, ha='center', va='bottom',
        color=GREEN[1], fontweight='bold')
ax.text((apex[0] + W) / 2, H + 0.5, r"$B^2$", fontsize=17, ha='center',
        va='bottom', color=ORANGE[1], fontweight='bold')
ax.text(-0.6, H / 2, r"$AB$", fontsize=14, ha='right', va='center', color=TEXT)
ax.text(W + 0.6, H / 2, r"$AB$", fontsize=14, ha='left', va='center', color=TEXT)

# Shared internal edges AC (xC|xA) and BC (xC|xB)
ax.text(4.0, 6.4, r"$AC$", fontsize=13, ha='center', va='center',
        color='#333333', rotation=np.degrees(np.arctan2(12, 9)))
ax.text(17.8, 6.4, r"$BC$", fontsize=13, ha='center', va='center',
        color='#333333', rotation=np.degrees(np.arctan2(0 - 12, 25 - 9)))

# Right-angle marker at apex (the xC triangle's right angle)
d = 0.7
v1 = np.array([0 - apex[0], 0 - apex[1]], float); v1 /= np.linalg.norm(v1)
v2 = np.array([W - apex[0], 0 - apex[1]], float); v2 /= np.linalg.norm(v2)
p1 = np.array(apex) + d * v1
p2 = p1 + d * v2
p3 = np.array(apex) + d * v2
ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]],
        color=BLUE[1], linewidth=1.4, zorder=5)

ax.text(W / 2, H + 2.5,
        r"$A^2 + B^2 \;=\; C^2$   (top edge $=$ bottom edge)",
        fontsize=18, ha='center', va='bottom', color=TEXT, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.45', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_xlim(-2.6, W + 2.6)
ax.set_ylim(-2.6, H + 5.2)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('pyth_fig2_similar_scaling.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pyth_fig2_similar_scaling.png")
