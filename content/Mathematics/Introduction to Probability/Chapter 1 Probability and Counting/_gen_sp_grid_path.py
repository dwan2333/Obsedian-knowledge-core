"""Generate sp_topic_1_grid_path.png — example increasing path on the integer grid.

Replaces the Nano Banana Pro version, which violated the definition by drawing
a smooth diagonal line. This version draws a correct staircase path made of
right and up steps only.
"""
import matplotlib.pyplot as plt
import numpy as np

m, n = 5, 4
fig, ax = plt.subplots(figsize=(9, 6))

# Lattice grid lines and points
for i in range(m + 1):
    ax.axvline(i, color='#e6e6e6', linewidth=0.7, zorder=1)
for j in range(n + 1):
    ax.axhline(j, color='#e6e6e6', linewidth=0.7, zorder=1)
xs, ys = np.meshgrid(np.arange(m + 1), np.arange(n + 1))
ax.scatter(xs.ravel(), ys.ravel(), s=22, color='#999999', zorder=2)

# Staircase path (right and up steps only)
path = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2),
        (4, 2), (4, 3), (5, 3), (5, 4)]
xp = [p[0] for p in path]
yp = [p[1] for p in path]
ax.plot(xp, yp, color='#2c6cb0', linewidth=3.5, zorder=3, solid_capstyle='round')
ax.scatter(xp, yp, s=55, color='#4a90e2', edgecolor='#1f4f8c',
           linewidth=1.2, zorder=4)

# Endpoints highlighted
ax.scatter([0, m], [0, n], s=160, color='#e2924a',
           edgecolor='#8c4f1f', linewidth=2, zorder=5)
ax.text(-0.3, -0.45, r'$(0,0)$', fontsize=15, ha='right',
        color='#8c4f1f', fontweight='bold')
ax.text(m + 0.2, n + 0.3, r'$(m,n)$', fontsize=15, ha='left',
        color='#8c4f1f', fontweight='bold')

# Title
ax.set_title(r'An increasing path from $(0,0)$ to $(m,n)$',
             fontsize=16, pad=14)

# Allowed-moves legend (right side)
lx = m + 1.0
ax.annotate('', xy=(lx + 1.2, n), xytext=(lx + 0.2, n),
            arrowprops=dict(arrowstyle='->', color='#1f4f8c', lw=2.2))
ax.text(lx + 1.4, n, 'right step', fontsize=12, va='center', color='#1f4f8c')

ax.annotate('', xy=(lx + 0.6, n - 1.0), xytext=(lx + 0.6, n - 1.8),
            arrowprops=dict(arrowstyle='->', color='#1f4f8c', lw=2.2))
ax.text(lx + 0.85, n - 1.4, 'up step',
        fontsize=12, va='center', color='#1f4f8c')

ax.text(lx + 0.2, n - 2.6, 'no diagonals\nno left, no down',
        fontsize=11, color='#888888', style='italic')

# Caption
ax.text(m / 2, -1.1, r'$C(m,n)$ = the set of all such paths',
        fontsize=13, ha='center', color='#333333')

ax.set_xlim(-1.2, m + 3.5)
ax.set_ylim(-1.6, n + 0.8)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('sp_topic_1_grid_path.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_topic_1_grid_path.png")
