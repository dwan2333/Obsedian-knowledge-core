"""Generate lf_fig8_area_under_one_x.png — visualize the connection between
the harmonic partial sum 1 + 1/2 + ... + 1/N and the integral
\int_1^N (1/x) dx = ln(N). The rectangles of height 1/k from x=k to x=k+1
sit just above the curve y = 1/x."""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
TEXT = '#222'; MUTE = '#888'; GRID = '#e6e6e6'

fig, ax = plt.subplots(figsize=(12, 6.5))

# Rectangles for 1 + 1/2 + ... + 1/N
N = 8
for k in range(1, N + 1):
    rect = mpatches.Rectangle((k - 0.5, 0), 1.0, 1.0 / k,
                              facecolor=ORANGE_EDGE, alpha=0.30,
                              edgecolor=ORANGE_EDGE, linewidth=1.2, zorder=3)
    ax.add_patch(rect)
    # Label height
    ax.text(k, 1.0/k + 0.02, f'$\\frac{{1}}{{{k}}}$', fontsize=11,
            ha='center', va='bottom', color=ORANGE_EDGE, fontweight='bold')

# Curve y = 1/x
x = np.linspace(0.5, N + 0.5, 400)
ax.plot(x, 1/x, color=BLUE_EDGE, lw=2.6, zorder=4,
        label=r'$y = \dfrac{1}{x}$')

# Shade area under curve from 1 to N
x_fill = np.linspace(0.5, N + 0.5, 400)
ax.fill_between(x_fill, 0, 1/x_fill, color=BLUE_EDGE, alpha=0.18, zorder=2)

ax.grid(True, color=GRID, lw=0.6, zorder=0)
ax.axhline(0, color=MUTE, lw=0.8, zorder=1)
ax.axvline(0, color=MUTE, lw=0.8, zorder=1)

ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_xlim(0.2, N + 1.5); ax.set_ylim(-0.05, 1.2)

# Title and the key identity
ax.set_title('Harmonic partial sum vs. area under $1/x$',
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.text(N - 0.5, 0.85,
        r'$\sum_{k=1}^{N} \frac{1}{k}$' '\n'
        r'$\approx \int_1^N \dfrac{1}{x}\, dx = \ln N$',
        fontsize=13, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('lf_fig8_area_under_one_x.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig8_area_under_one_x.png")
