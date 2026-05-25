"""Generate efm_fig3_spiral.png — exp(i*pi) as tip-to-tail spiraling vectors.

The key visual: each term (i*pi)^n / n! is a vector whose direction is a power
of i (90 deg rotation per step) and whose magnitude is pi^n / n!. The vectors
are placed tip-to-tail starting from the origin. The cumulative sum converges
to -1 on the real axis.

Implementation note: matplotlib's mathtext doesn't support \mathbb / \bigl etc.,
so we stick to basic notation in labels.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'

# Number of terms of the series to draw.
N_TERMS = 18
theta = math.pi

# Compute the cumulative partial sums of (i*theta)^n / n!.
# In complex arithmetic, i*theta = 0 + theta*j.
i_theta = 0 + theta * 1j
points = [0 + 0j]
for n in range(N_TERMS):
    term = (i_theta ** n) / math.factorial(n)
    points.append(points[-1] + term)

# Color cycle for vectors so they're easy to distinguish.
COLORS = ['#e2924a', '#4a90e2', '#7bb55c', '#b76db4',
          '#d4a04a', '#aa6644']
def col_for(n):
    return COLORS[n % len(COLORS)]

fig, ax = plt.subplots(figsize=(12, 8))

# Background grid and axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)

# Faint unit circle for reference.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=MUTE, linewidth=1.2,
                       linestyle='--', alpha=0.7, zorder=1)
ax.add_patch(circ)

# Tick marks at -1 and 1 (and at i, -i).
for x, lbl in [(1, "1"), (-1, "-1")]:
    ax.plot([x, x], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.2, zorder=2)
    ax.text(x, -0.18, lbl, fontsize=11, color=BLUE_EDGE,
            ha='center', va='top', fontweight='bold')
ax.text(0.04, 1.05, "i", fontsize=11, color=BLUE_EDGE,
        ha='left', va='bottom', fontweight='bold')

# Draw each term as an arrow from points[n] to points[n+1].
for n in range(N_TERMS):
    p_from = points[n]
    p_to = points[n + 1]
    if abs(p_to - p_from) < 0.04:
        continue  # too tiny to draw
    ax.annotate('', xy=(p_to.real, p_to.imag),
                xytext=(p_from.real, p_from.imag),
                arrowprops=dict(arrowstyle='->', color=col_for(n),
                                lw=1.8, alpha=0.92,
                                mutation_scale=12),
                zorder=3)

# Label a few key partial sums.
def label_at(idx, text, dx=0.15, dy=0.10):
    p = points[idx]
    ax.scatter([p.real], [p.imag], s=46,
               color=col_for(idx - 1) if idx > 0 else '#888',
               zorder=5)
    ax.text(p.real + dx, p.imag + dy, text,
            fontsize=10, color=TEXT,
            ha='left', va='bottom')

label_at(0, "start: 0", dx=0.10, dy=-0.18)
label_at(1, r"$+1$", dx=0.10, dy=0.10)
label_at(2, r"$+i\pi$ (up $\approx 3.14$)", dx=0.05, dy=0.10)
label_at(3, r"$-\pi^2/2$ (left $\approx 4.93$)", dx=-0.05, dy=-0.15)
label_at(4, r"$-i\pi^3/6$", dx=0.10, dy=-0.20)
label_at(6, r"more terms", dx=0.15, dy=0.10)

# Highlight the target endpoint -1.
ax.scatter([-1], [0], s=200, marker='*', color='gold',
           edgecolor='#aa8b3a', linewidth=1.4, zorder=6)
ax.text(-1.0, -0.45, r"converges to $-1$",
        fontsize=13, color=TEXT, ha='center', va='top',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.3))

ax.set_title(r"$\exp(i\pi)$ as tip-to-tail spiraling vectors",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

# Boxed identity below.
ax.text(0.5, -3.6,
        r"$\exp(i\pi) = 1 + i\pi + \frac{(i\pi)^2}{2!} + \frac{(i\pi)^3}{3!} + \cdots = -1$",
        fontsize=14, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_xlim(-5.5, 6.5)
ax.set_ylim(-4.6, 4.6)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efm_fig3_spiral.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efm_fig3_spiral.png")
