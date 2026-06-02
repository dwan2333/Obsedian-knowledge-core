"""Generate ch4_fig1_growth_decay.png — exponential growth vs decay graphs.

Side-by-side: f(x) = 2^x (growth) and g(x) = (1/2)^x (decay). Shows the
y-intercept at (0, 1), horizontal asymptote y=0, and the mirror-image
structure of growth and decay around the y-axis.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
TEXT = '#222'
MUTE = '#888'
GRID = '#e6e6e6'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), sharey=True)

x = np.linspace(-3, 3, 400)
growth = 2 ** x
decay = 0.5 ** x

# Growth panel
ax1.axhline(0, color=MUTE, lw=0.8, linestyle='--', zorder=1)
ax1.plot(x, growth, color=BLUE_EDGE, linewidth=2.6, zorder=3, label=r'$f(x) = 2^x$')
ax1.scatter([0], [1], s=80, color=BLUE_EDGE, edgecolor='white', linewidth=1.8, zorder=5)
ax1.annotate('y-intercept (0, 1)', xy=(0, 1), xytext=(0.5, 2.5), fontsize=10,
             color=BLUE_EDGE, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=BLUE_EDGE, lw=1.2))
ax1.text(2.4, 0.3, r'horizontal asymptote $y=0$', fontsize=9.5, color=MUTE,
         ha='right', va='top', style='italic')
ax1.set_xlim(-3, 3); ax1.set_ylim(-0.5, 8.5)
ax1.grid(True, color=GRID, lw=0.6); ax1.axvline(0, color=MUTE, lw=0.8)
ax1.set_xlabel('x', fontsize=11); ax1.set_ylabel('f(x)', fontsize=11)
ax1.set_title(r'Exponential growth: $b > 1$', fontsize=13, pad=12, color=BLUE_EDGE, fontweight='bold')
ax1.legend(loc='upper left', fontsize=11)

# Decay panel
ax2.axhline(0, color=MUTE, lw=0.8, linestyle='--', zorder=1)
ax2.plot(x, decay, color=ORANGE_EDGE, linewidth=2.6, zorder=3, label=r'$g(x) = (1/2)^x$')
ax2.scatter([0], [1], s=80, color=ORANGE_EDGE, edgecolor='white', linewidth=1.8, zorder=5)
ax2.annotate('y-intercept (0, 1)', xy=(0, 1), xytext=(-2.5, 2.5), fontsize=10,
             color=ORANGE_EDGE, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=1.2))
ax2.text(2.4, 0.3, r'horizontal asymptote $y=0$', fontsize=9.5, color=MUTE,
         ha='right', va='top', style='italic')
ax2.set_xlim(-3, 3); ax2.set_ylim(-0.5, 8.5)
ax2.grid(True, color=GRID, lw=0.6); ax2.axvline(0, color=MUTE, lw=0.8)
ax2.set_xlabel('x', fontsize=11)
ax2.set_title(r'Exponential decay: $0 < b < 1$', fontsize=13, pad=12, color=ORANGE_EDGE, fontweight='bold')
ax2.legend(loc='upper right', fontsize=11)

fig.suptitle('Exponential functions $f(x) = ab^x$: same shape, mirrored direction',
             fontsize=14, y=1.0, fontweight='bold')
plt.tight_layout()
plt.savefig('ch4_fig1_growth_decay.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig1_growth_decay.png")
