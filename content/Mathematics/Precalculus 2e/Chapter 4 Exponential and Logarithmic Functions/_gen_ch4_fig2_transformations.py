"""Generate ch4_fig2_transformations.png — exponential function transformations.

4-panel showing the parent f(x) = 2^x and the effect of:
(a) horizontal/vertical shifts: f(x+c) + d
(b) vertical stretch/compression: a*f(x)
(c) reflection over x-axis: -f(x) and reflection over y-axis: f(-x)
(d) general transformation form
"""
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
GOLD_EDGE = '#8c6520'
TEXT = '#222'
MUTE = '#888'
GRID = '#e6e6e6'

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
x = np.linspace(-3, 3, 400)
parent = 2 ** x

def setup_axes(ax, title, title_color):
    ax.axhline(0, color=MUTE, lw=0.8, linestyle='--', zorder=1)
    ax.axvline(0, color=MUTE, lw=0.8, zorder=1)
    ax.grid(True, color=GRID, lw=0.6, zorder=0)
    ax.set_xlim(-3, 3); ax.set_ylim(-4, 8)
    ax.set_title(title, fontsize=12, pad=8, color=title_color, fontweight='bold')
    ax.plot(x, parent, color=MUTE, linewidth=1.8, linestyle='--', alpha=0.7,
            label=r'parent $f(x) = 2^x$', zorder=2)

# Panel (a): shifts
ax = axes[0, 0]
setup_axes(ax, '(a) Shifts: $f(x{+}c) + d$', BLUE_EDGE)
ax.plot(x, 2**(x + 1) - 3, color=BLUE_EDGE, linewidth=2.4, zorder=3,
        label=r'$2^{x+1} - 3$ (left 1, down 3)')
ax.axhline(-3, color=BLUE_EDGE, lw=0.8, linestyle=':', alpha=0.7)
ax.legend(loc='upper left', fontsize=10)

# Panel (b): stretches
ax = axes[0, 1]
setup_axes(ax, '(b) Vertical stretches: $a \\cdot f(x)$', GREEN_EDGE)
ax.plot(x, 4 * 2**x, color=GREEN_EDGE, linewidth=2.4, zorder=3,
        label=r'$4 \cdot 2^x$ (stretch ×4)')
ax.plot(x, 0.25 * 2**x, color=ORANGE_EDGE, linewidth=2.4, zorder=3,
        label=r'$(1/4) \cdot 2^x$ (compress ×1/4)')
ax.legend(loc='upper left', fontsize=10)

# Panel (c): reflections
ax = axes[1, 0]
setup_axes(ax, '(c) Reflections', PURPLE_EDGE)
ax.plot(x, -(2**x), color=PURPLE_EDGE, linewidth=2.4, zorder=3,
        label=r'$-2^x$ (over x-axis)')
ax.plot(x, 2**(-x), color=GOLD_EDGE, linewidth=2.4, zorder=3,
        label=r'$2^{-x}$ (over y-axis)')
ax.legend(loc='upper left', fontsize=10)

# Panel (d): general form summary
ax = axes[1, 1]
ax.axis('off')
ax.text(0.5, 0.95, 'General transformation form', fontsize=14,
        ha='center', va='top', color=TEXT, fontweight='bold',
        transform=ax.transAxes)
ax.text(0.5, 0.80, r'$f(x) = a \cdot b^{\,x+c} + d$',
        fontsize=20, ha='center', va='top', color=BLUE_EDGE, fontweight='bold',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))
table_y = [0.58, 0.48, 0.38, 0.28]
labels = [
    ('$a$', 'vertical stretch ($|a|{>}1$) or compression ($|a|{<}1$); sign flips reflection'),
    ('$b$', r'base: growth if $b{>}1$, decay if $0{<}b{<}1$'),
    ('$c$', 'horizontal shift: $+c$ shifts LEFT by $c$'),
    ('$d$', 'vertical shift; new horizontal asymptote $y=d$'),
]
for (sym, desc), y in zip(labels, table_y):
    ax.text(0.1, y, sym, fontsize=15, color=BLUE_EDGE, fontweight='bold',
            transform=ax.transAxes, va='center')
    ax.text(0.22, y, desc, fontsize=11, color=TEXT,
            transform=ax.transAxes, va='center', wrap=True)
ax.text(0.5, 0.10, 'Order of operations matters when composing transformations.',
        fontsize=10, ha='center', va='top', color=MUTE,
        style='italic', transform=ax.transAxes)

fig.suptitle('Transformations of exponential functions',
             fontsize=15, y=1.0, fontweight='bold')
plt.tight_layout()
plt.savefig('ch4_fig2_transformations.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig2_transformations.png")
