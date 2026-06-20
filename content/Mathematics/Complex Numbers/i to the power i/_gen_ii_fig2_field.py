"""ii_fig2_field.png — the dynamic rule d/dt e^{it} = i e^{it}: at every point the
velocity is the position vector rotated 90deg, producing a counterclockwise
whirlpool whose flow lines are circles."""
import matplotlib.pyplot as plt
import numpy as np

BLUE, GREEN = '#1f4f8c', '#3d7530'
fig, ax = plt.subplots(figsize=(8.4, 8.4))

# vector field: velocity at z = i*z  ->  (x,y) -> (-y, x)
g = np.linspace(-2.2, 2.2, 17)
X, Y = np.meshgrid(g, g)
U, V = -Y, X
M = np.hypot(U, V); M[M == 0] = 1
ax.quiver(X, Y, U / M, V / M, color='#9bb3d6', scale=34, width=0.0035,
          alpha=0.8, zorder=1)

# unit circle = the flow line through 1
tt = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(tt), np.sin(tt), color='#cc4444', lw=2.0, zorder=2,
        label='flow line through $1$ (the unit circle)')

# highlighted position + velocity pair
a = np.deg2rad(52)
px, py = np.cos(a), np.sin(a)
vx, vy = -np.sin(a), np.cos(a)   # i * position
ax.annotate('', xy=(px, py), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=3))
ax.annotate('', xy=(px + vx, py + vy), xytext=(px, py),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
ax.text(px * 0.52 - 0.05, py * 0.52 + 0.12, 'position', color=BLUE,
        fontsize=12.5, fontweight='bold', rotation=a*180/np.pi-90 if False else 0)
ax.text(px + vx - 0.05, py + vy + 0.10, 'velocity\n' + r'$=\,i\times$ position',
        color=GREEN, fontsize=12, fontweight='bold', ha='center')

ax.scatter([0], [1], s=120, color='#cc4444', edgecolor='white', zorder=6)
ax.text(0.06, 1.06, r'$i$', color='#cc4444', fontsize=15, fontweight='bold')
ax.scatter([1], [0], s=70, color='#cc4444', edgecolor='white', zorder=6)
ax.text(1.06, -0.16, r'$1$', color='#cc4444', fontsize=13)

ax.set_title(r"Velocity $=$ position rotated $90^\circ$  $\Rightarrow$  motion around a circle",
             fontsize=13.5, fontweight='bold', pad=10)
ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.3, 2.3)
ax.set_aspect('equal'); ax.axis('off')
ax.legend(loc='lower left', fontsize=10.5, framealpha=0.95)
plt.tight_layout()
plt.savefig('ii_fig2_field.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ii_fig2_field.png")
