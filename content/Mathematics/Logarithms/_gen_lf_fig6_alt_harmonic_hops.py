"""Generate lf_fig6_alt_harmonic_hops.png — number-line hops visualizing the
alternating harmonic series converging to ln(2)."""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'; TEXT = '#222'; MUTE = '#888'

fig, ax = plt.subplots(figsize=(13, 5))
ax.set_aspect('equal'); ax.axis('off')

# Number line from 0 to 1.1, y=0
ax.plot([0, 1.1], [0, 0], color=TEXT, lw=2.0, solid_capstyle='round')
# Tick marks at 0, 0.5, 1
for xt, lbl in [(0, '0'), (0.5, '0.5'), (1, '1'), (math.log(2), r'$\ln 2 \approx 0.693$')]:
    ax.plot([xt, xt], [-0.04, 0.04], color=TEXT, lw=1.6)
    color = GREEN_EDGE if lbl.startswith('$\\ln') else TEXT
    weight = 'bold' if lbl.startswith('$\\ln') else 'normal'
    ax.text(xt, -0.10, lbl, fontsize=11, color=color,
            ha='center', va='top', fontweight=weight)

# Partial sums of alternating harmonic series
N_TERMS = 8
partial = [0.0]
for k in range(1, N_TERMS + 1):
    sign = (-1) ** (k + 1)
    partial.append(partial[-1] + sign / k)

# Draw arcs between consecutive partial sums
ARC_HEIGHTS = [0.30, 0.16, 0.10, 0.07, 0.05, 0.04, 0.03, 0.025]
arc_colors = [BLUE_EDGE, ORANGE_EDGE, BLUE_EDGE, ORANGE_EDGE,
              BLUE_EDGE, ORANGE_EDGE, BLUE_EDGE, ORANGE_EDGE]
for k in range(N_TERMS):
    x0, x1 = partial[k], partial[k+1]
    h = ARC_HEIGHTS[k]
    direction = 1  # arcs go up
    # Quadratic Bezier-style arc using a few points
    t = np.linspace(0, 1, 50)
    arc_x = (1-t)*x0 + t*x1
    # parabolic bump
    arc_y = 4*h*t*(1-t)
    ax.plot(arc_x, arc_y, color=arc_colors[k], lw=1.8, alpha=0.85, zorder=4)
    # arrowhead at end of arc
    dx = (arc_x[-1] - arc_x[-2])
    dy = (arc_y[-1] - arc_y[-2])
    ax.annotate('', xy=(arc_x[-1], arc_y[-1]),
                xytext=(arc_x[-1] - dx, arc_y[-1] - dy),
                arrowprops=dict(arrowstyle='->', color=arc_colors[k], lw=2.0),
                zorder=5)
    # Label only first few hops
    if k < 5:
        sign = '+' if k % 2 == 0 else '-'
        if k == 0:
            lbl = '$+1$'
        else:
            lbl = f'${sign}\\dfrac{{1}}{{{k+1}}}$'
        midx = (x0 + x1) / 2
        midy = h + 0.03
        ax.text(midx, midy, lbl, fontsize=11, color=arc_colors[k],
                ha='center', va='bottom', fontweight='bold')

# Mark partial sums
for k, p in enumerate(partial):
    ax.scatter([p], [0], s=60, color=arc_colors[max(0, k-1)] if k > 0 else GREEN_EDGE,
               edgecolor='white', linewidth=1.0, zorder=6)

# Highlight the limit (ln 2 ≈ 0.693)
ax.axvline(math.log(2), color=GREEN_EDGE, lw=1.4, linestyle='--',
           alpha=0.6, zorder=2)
ax.scatter([math.log(2)], [0], s=250, marker='*', color=GREEN_EDGE,
           edgecolor='white', linewidth=1.6, zorder=7)

# Title and footer
ax.text(0.55, 0.50,
        r'$1 - \tfrac{1}{2} + \tfrac{1}{3} - \tfrac{1}{4} + \tfrac{1}{5} - \cdots = \ln 2$',
        fontsize=15, color=TEXT, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_xlim(-0.05, 1.15); ax.set_ylim(-0.30, 0.65)

plt.tight_layout()
plt.savefig('lf_fig6_alt_harmonic_hops.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig6_alt_harmonic_hops.png")
