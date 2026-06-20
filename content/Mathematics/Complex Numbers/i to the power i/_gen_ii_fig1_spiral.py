"""ii_fig1_spiral.png — partial sums of the Taylor series for e^(i*pi/2) added
tip-to-tail spiral inward and converge to the point i on the unit circle."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math

th = np.pi / 2
terms = [(1j * th) ** k / math.factorial(k) for k in range(14)]
S = np.cumsum(terms)              # partial sums S_0 .. S_13
pts = np.concatenate(([0 + 0j], S))   # start path at origin

GREEN, YELLOW, BLUE = '#3d7530', '#8c6520', '#1f4f8c'
fig, ax = plt.subplots(figsize=(8.2, 8.2))

# unit circle
tt = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(tt), np.sin(tt), color='#cc4444', lw=1.6, alpha=0.7,
        label='unit circle')

# tip-to-tail term vectors (first 8), alternating colours
for k in range(8):
    z0, z1 = pts[k], pts[k + 1]
    c = YELLOW if k % 2 else GREEN
    ax.annotate('', xy=(z1.real, z1.imag), xytext=(z0.real, z0.imag),
                arrowprops=dict(arrowstyle='->', color=c, lw=2.0, alpha=0.9))
# remaining tail as a thin spiral line
ax.plot(pts.real, pts.imag, color=BLUE, lw=1.1, alpha=0.55, zorder=1)
ax.scatter(S.real[:12], S.imag[:12], s=16, color=BLUE, zorder=4)

# the limit point i
ax.scatter([0], [1], s=240, marker='*', color='#cc4444',
           edgecolor='white', linewidth=1.2, zorder=6)
ax.annotate(r'converges to $i = e^{\,i\pi/2}$', xy=(0, 1), xytext=(0.55, 1.42),
            fontsize=13, color='#cc4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#cc4444', lw=1.6))
ax.annotate(r'start at $1$', xy=(1, 0), xytext=(1.05, -0.5), fontsize=11.5,
            color=GREEN, arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.4))
ax.text(-1.75, 1.55, r"$e^{i\theta}=1+i\theta+\frac{(i\theta)^2}{2}+"
        r"\frac{(i\theta)^3}{6}+\cdots$", fontsize=12.5, color='#222222')

ax.axhline(0, color='#bbb', lw=0.8, zorder=0); ax.axvline(0, color='#bbb', lw=0.8, zorder=0)
ax.set_title(r"Summing the series for $e^{i\pi/2}$: a spiral that lands on $i$",
             fontsize=13.5, fontweight='bold', pad=10)
ax.set_xlim(-1.9, 1.9); ax.set_ylim(-0.9, 1.9)
ax.set_aspect('equal'); ax.axis('off')
ax.legend(loc='lower left', fontsize=10.5, framealpha=0.95)
plt.tight_layout()
plt.savefig('ii_fig1_spiral.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ii_fig1_spiral.png")
