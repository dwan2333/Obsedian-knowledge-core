"""Generate pyth_fig4_super_theorem.png — the Super Theorem.

A right triangle (3-4-5) with a semicircle built outward on each side. Because
every shape's area is the SAME constant k times (side)^2, the constant cancels
and small + medium = large for any shape, not just squares.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

A, B = 3.0, 4.0
O = np.array([0.0, 0.0])     # right angle
P = np.array([B, 0.0])       # bottom-right
Q = np.array([0.0, A])       # top-left

TRI = ('#e0746a', '#a83227')
GREEN = ('#8fc873', '#3d7530')    # side A (small)
ORANGE = ('#e0a85c', '#8c5a1f')   # side B (medium)
BLUE = ('#7fb0e0', '#1f4f8c')     # hypotenuse C (large)
TEXT = '#222222'

fig, ax = plt.subplots(figsize=(8.8, 8.2))

def semicircle(p, q, third, face, edge, label, lpad=0.55, fs=17):
    """Semicircle on segment p-q, bulging away from `third` vertex."""
    p, q, third = map(np.asarray, (p, q, third))
    mid = (p + q) / 2.0
    rad = np.linalg.norm(q - p) / 2.0
    base = np.degrees(np.arctan2((q - p)[1], (q - p)[0]))
    # outward normal direction (away from third vertex)
    normal = np.array([-(q - p)[1], (q - p)[0]], float)
    normal /= np.linalg.norm(normal)
    if np.dot(normal, mid - third) < 0:
        normal = -normal
        base += 180.0
    wedge = mpatches.Wedge(mid, rad, base, base + 180.0, facecolor=face,
                           edgecolor=edge, linewidth=2.0, alpha=0.55, zorder=1)
    ax.add_patch(wedge)
    lp = mid + (rad + lpad) * normal
    ax.text(lp[0], lp[1], label, fontsize=fs, ha='center', va='center',
            color=edge, fontweight='bold', zorder=4)

# Semicircles on the three sides.
semicircle(O, Q, P, GREEN[0], GREEN[1], "small\n(side $A$)", lpad=0.7, fs=13)
semicircle(O, P, Q, ORANGE[0], ORANGE[1], "medium\n(side $B$)", lpad=0.7, fs=13)
semicircle(P, Q, O, BLUE[0], BLUE[1], "large\n(side $C$)", lpad=0.9, fs=13)

# Triangle on top.
ax.add_patch(mpatches.Polygon([O, P, Q], closed=True, facecolor=TRI[0],
             edgecolor=TRI[1], linewidth=2.2, alpha=0.95, zorder=3))
# Right-angle marker.
r = 0.26
ax.plot([r, r, 0], [0, r, r], color=TRI[1], linewidth=1.4, zorder=4)
# Side labels on the triangle.
ax.text(-0.22, A / 2, r"$A$", fontsize=15, ha='right', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(B / 2, 0.22, r"$B$", fontsize=15, ha='center', va='bottom',
        color='white', fontweight='bold', zorder=5)

# One-line algebra box.
ax.text(0.2, -3.4,
        r"$k A^2 + k B^2 = k C^2 \;\Rightarrow\;$ small $+$ medium $=$ large",
        fontsize=15, ha='center', va='center', color=TEXT, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.45', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))
ax.text(0.2, -4.15,
        "works for squares, semicircles, pentagons — any shape",
        fontsize=11.5, ha='center', va='center', color='#555555', style='italic')

ax.set_title("The Super Theorem: attach any shape to the three sides",
             fontsize=13, pad=10, color=TEXT)
ax.set_xlim(-3.6, 5.2)
ax.set_ylim(-4.7, 4.6)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('pyth_fig4_super_theorem.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pyth_fig4_super_theorem.png")
