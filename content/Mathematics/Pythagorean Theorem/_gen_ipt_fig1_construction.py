"""Generate ipt_fig1_construction.png — blackpenredpen's setup.

Right triangle: vertical leg a, horizontal leg b, right angle at bottom-left,
hypotenuse c. Drop the altitude h from the right angle onto c; its foot F splits
c into c1 (next to leg a) and c2 (next to leg b).  a=3, b=4, c=5.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

O = np.array([0.0, 0.0])    # right angle
T = np.array([0.0, 3.0])    # top  (leg a from O to T)
R = np.array([4.0, 0.0])    # right (leg b from O to R)

BLACK = '#222222'
RED = '#c0392b'
PINK = '#c2185b'
BLUE_EDGE = '#1f4f8c'

# Foot of altitude from O onto hypotenuse T-R.
TR = R - T
TRu = TR / np.linalg.norm(TR)
F = T + np.dot(O - T, TRu) * TRu       # = (1.44, 1.92)

fig, ax = plt.subplots(figsize=(7.4, 6.6))

# Triangle outline.
ax.add_patch(mpatches.Polygon([O, R, T], closed=True, fill=False,
             edgecolor=BLACK, linewidth=2.4, zorder=3))
# Altitude (pink dashed).
ax.plot([O[0], F[0]], [O[1], F[1]], color=PINK, linewidth=2.0,
        linestyle='--', zorder=3)

# Right-angle markers.
r = 0.26
ax.plot([r, r, 0], [0, r, r], color=BLACK, linewidth=1.4, zorder=4)   # at O
perp = np.array([-TRu[1], TRu[0]])
if np.dot(perp, O - F) < 0:
    perp = -perp
a1 = F - r * TRu; a2 = a1 + r * perp; a3 = F + r * perp
ax.plot([a1[0], a2[0], a3[0]], [a1[1], a2[1], a3[1]],
        color=PINK, linewidth=1.3, zorder=4)

def olabel(p, q, text, color, dist=0.34, fs=17):
    p, q = np.asarray(p), np.asarray(q)
    mid = (p + q) / 2
    d = (q - p); d = d / np.linalg.norm(d)
    n = np.array([-d[1], d[0]])
    # push away from triangle centroid
    cen = (O + R + T) / 3
    if np.dot(n, mid - cen) < 0:
        n = -n
    pos = mid + dist * n
    ax.text(pos[0], pos[1], text, fontsize=fs, color=color, ha='center',
            va='center', fontweight='bold')

# Leg labels.
ax.text(-0.30, 1.5, r"$a$", fontsize=18, color=BLACK, ha='right', va='center',
        fontweight='bold')
ax.text(2.0, -0.32, r"$b$", fontsize=18, color=BLACK, ha='center', va='top',
        fontweight='bold')
# Altitude label.
mid_h = (O + F) / 2
ax.text(mid_h[0] + 0.12, mid_h[1] - 0.10, r"$h$", fontsize=16, color=PINK,
        ha='left', va='top', fontweight='bold')
# Hypotenuse segments c1 (T->F) and c2 (F->R), in red.
olabel(T, F, r"$c_1$", RED, dist=0.30)
olabel(F, R, r"$c_2$", RED, dist=0.30)

# vertex dots
for v in (O, R, T, F):
    ax.scatter(v[0], v[1], s=36, color=BLUE_EDGE, zorder=5)

ax.text(2.0, 3.5, r"$c_1 + c_2 = c$", fontsize=15, color=BLACK, ha='center',
        va='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                               edgecolor='#aa8b3a', linewidth=1.5))

ax.set_title("One altitude $h$ splits $c$ into $c_1$ and $c_2$",
             fontsize=13, pad=10, color=BLACK)
ax.set_xlim(-1.1, 4.7)
ax.set_ylim(-0.9, 4.0)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('ipt_fig1_construction.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved ipt_fig1_construction.png")
