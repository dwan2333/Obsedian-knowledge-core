"""Generate ch4_fig3_log_inverse.png — log as inverse of exponential.

f(x) = 2^x and g(x) = log_2(x) reflected across y=x. Shows the
inverse relationship: the log graph is the exp graph flipped over the
diagonal. Includes vertical asymptote x=0 for log and horizontal asymptote
y=0 for exp.
"""
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
TEXT = '#222'
MUTE = '#888'
GRID = '#e6e6e6'

fig, ax = plt.subplots(figsize=(9, 9))

# Grid and axes
ax.grid(True, color=GRID, lw=0.6, zorder=0)
ax.axhline(0, color=MUTE, lw=0.9, zorder=1)
ax.axvline(0, color=MUTE, lw=0.9, zorder=1)

# y = x diagonal
x_diag = np.linspace(-1, 8, 100)
ax.plot(x_diag, x_diag, color=MUTE, lw=1.4, linestyle=':',
        alpha=0.7, zorder=2, label=r'$y = x$ (mirror line)')

# Exponential: f(x) = 2^x
x_exp = np.linspace(-3, 3, 400)
y_exp = 2 ** x_exp
ax.plot(x_exp, y_exp, color=BLUE_EDGE, linewidth=2.8, zorder=4,
        label=r'$f(x) = 2^x$')
# Asymptote line for exp
ax.axhline(0, color=BLUE_EDGE, lw=0.8, linestyle='--', alpha=0.4, zorder=1)

# Logarithm: g(x) = log_2(x)
x_log = np.linspace(0.05, 8, 400)
y_log = np.log2(x_log)
ax.plot(x_log, y_log, color=ORANGE_EDGE, linewidth=2.8, zorder=4,
        label=r'$g(x) = \log_2(x)$')
# Asymptote line for log
ax.axvline(0, color=ORANGE_EDGE, lw=0.8, linestyle='--', alpha=0.4, zorder=1)

# Mark corresponding pairs
pairs = [(0, 1, '(0, 1)', '(1, 0)', 1, 0),
         (1, 2, '(1, 2)', '(2, 1)', 2, 1),
         (2, 4, '(2, 4)', '(4, 2)', 4, 2),
         (3, 8, '(3, 8)', '(8, 3)', 8, 3)]
for ex_x, ex_y, lbl_exp, lbl_log, log_x, log_y in pairs:
    # Point on exp curve
    ax.scatter([ex_x], [ex_y], s=70, color=BLUE_EDGE, edgecolor='white',
               linewidth=1.5, zorder=6)
    # Point on log curve (swapped coords)
    ax.scatter([log_x], [log_y], s=70, color=ORANGE_EDGE, edgecolor='white',
               linewidth=1.5, zorder=6)
    # Dotted line connecting paired points
    ax.plot([ex_x, log_x], [ex_y, log_y], color=MUTE, lw=0.7,
            linestyle=':', alpha=0.5, zorder=2)

# Labels for one pair
ax.annotate('(2, 4) on $2^x$', xy=(2, 4), xytext=(0.5, 5.5),
            fontsize=11, color=BLUE_EDGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=BLUE_EDGE, lw=1.2))
ax.annotate('(4, 2) on $\\log_2(x)$', xy=(4, 2), xytext=(5.2, 0.5),
            fontsize=11, color=ORANGE_EDGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=1.2))

# Title
ax.set_title('A logarithm is the inverse of an exponential\n(reflect $2^x$ across $y=x$ to get $\\log_2(x)$)',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-2.5, 8.5); ax.set_ylim(-2.5, 8.5)
ax.set_aspect('equal')
ax.legend(loc='lower right', fontsize=11, frameon=True, framealpha=0.95)
ax.set_xlabel('x', fontsize=11); ax.set_ylabel('y', fontsize=11)

plt.tight_layout()
plt.savefig('ch4_fig3_log_inverse.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig3_log_inverse.png")
