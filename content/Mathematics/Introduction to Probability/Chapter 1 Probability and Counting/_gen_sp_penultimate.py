"""Generate sp_topic_2_penultimate.png — penultimate-step argument for the recurrence.

Shows that any increasing path reaching (m,n) must come from either (m-1,n)
via a right step, or from (m,n-1) via an up step. These are the two cases
behind |C(m,n)| = |C(m-1,n)| + |C(m,n-1)|.
"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 6.5))

# Local lattice: place (m,n) at (3,2), (m-1,n) at (2,2), (m,n-1) at (3,1)
W, H = 5, 4
for i in range(W):
    ax.axvline(i, color='#e6e6e6', linewidth=0.7, zorder=1)
for j in range(H):
    ax.axhline(j, color='#e6e6e6', linewidth=0.7, zorder=1)
xs, ys = np.meshgrid(np.arange(W), np.arange(H))
ax.scatter(xs.ravel(), ys.ravel(), s=18, color='#bbbbbb', zorder=2)

mx, my = 3, 2

# (m,n) destination
ax.scatter([mx], [my], s=240, color='#e2924a',
           edgecolor='#8c4f1f', linewidth=2.4, zorder=5)
ax.text(mx + 0.2, my + 0.3, r'$(m,n)$', fontsize=15,
        color='#8c4f1f', fontweight='bold')

# (m-1, n)
ax.scatter([mx - 1], [my], s=160, color='#4a90e2',
           edgecolor='#1f4f8c', linewidth=1.8, zorder=4)
ax.text(mx - 1.15, my + 0.3, r'$(m-1,\,n)$', fontsize=13,
        ha='right', color='#1f4f8c', fontweight='bold')

# (m, n-1)
ax.scatter([mx], [my - 1], s=160, color='#4a90e2',
           edgecolor='#1f4f8c', linewidth=1.8, zorder=4)
ax.text(mx + 0.2, my - 1 - 0.05, r'$(m,\,n-1)$', fontsize=13,
        color='#1f4f8c', fontweight='bold')

# Arrow: right step from (m-1,n) to (m,n)
ax.annotate('', xy=(mx - 0.18, my), xytext=(mx - 1 + 0.18, my),
            arrowprops=dict(arrowstyle='->', color='#2c6cb0', lw=3.0))
ax.text((mx - 1 + mx) / 2, my + 0.22, 'right step',
        fontsize=12, ha='center', color='#2c6cb0', fontweight='bold')

# Arrow: up step from (m,n-1) to (m,n)
ax.annotate('', xy=(mx, my - 0.18), xytext=(mx, my - 1 + 0.18),
            arrowprops=dict(arrowstyle='->', color='#2c6cb0', lw=3.0))
ax.text(mx + 0.22, (my - 1 + my) / 2, 'up step',
        fontsize=12, color='#2c6cb0', fontweight='bold')

# Title
ax.set_title(r'Two ways to reach $(m,n)$ — penultimate-step argument',
             fontsize=15, pad=12)

# Equation
eq_y = -1.0
ax.text(2.0, eq_y,
        r'$|C(m,n)| \;=\; |C(m-1,\,n)| \;+\; |C(m,\,n-1)|$',
        fontsize=17, ha='center', color='#333333')
ax.text(2.0, eq_y - 0.65,
        "every increasing path's last step is either right or up",
        fontsize=11, ha='center', color='#666666', style='italic')

ax.set_xlim(-1.2, W + 0.5)
ax.set_ylim(-2.0, H + 0.4)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('sp_topic_2_penultimate.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_topic_2_penultimate.png")
