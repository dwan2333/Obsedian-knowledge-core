"""Generate ch4_fig4_log_rules.png — visual cheat-sheet of the 4 log rules.

Four panels, one per rule (product, quotient, power, change-of-base),
each with the rule formula prominently displayed and a concrete numerical
example showing it works.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'; BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'; ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'; GREEN_EDGE = '#3d7530'
PURPLE = '#b76db4'; PURPLE_EDGE = '#6e3a6c'
TEXT = '#222'

fig, axes = plt.subplots(2, 2, figsize=(13.5, 9))

rules = [
    ('Product Rule', BLUE_EDGE, BLUE,
     r'$\log_b(MN) = \log_b(M) + \log_b(N)$',
     'Example:',
     r'$\log_{10}(100 \cdot 1000)$',
     r'$= \log_{10}(100) + \log_{10}(1000)$',
     r'$= 2 + 3 = 5$',
     r'(Check: $\log_{10}(100{,}000) = 5$ ✓)'),
    ('Quotient Rule', ORANGE_EDGE, ORANGE,
     r'$\log_b\!\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)$',
     'Example:',
     r'$\log_{10}\!\left(\frac{1000}{10}\right)$',
     r'$= \log_{10}(1000) - \log_{10}(10)$',
     r'$= 3 - 1 = 2$',
     r'(Check: $\log_{10}(100) = 2$ ✓)'),
    ('Power Rule', GREEN_EDGE, GREEN,
     r'$\log_b(M^n) = n \cdot \log_b(M)$',
     'Example:',
     r'$\log_{10}(100^3)$',
     r'$= 3 \cdot \log_{10}(100)$',
     r'$= 3 \cdot 2 = 6$',
     r'(Check: $\log_{10}(10^6) = 6$ ✓)'),
    ('Change of Base', PURPLE_EDGE, PURPLE,
     r'$\log_b(M) = \frac{\log_c(M)}{\log_c(b)}$',
     'Example:',
     r'$\log_{2}(8)$',
     r'$= \frac{\log_{10}(8)}{\log_{10}(2)} = \frac{0.903}{0.301}$',
     r'$= 3$',
     r'(Check: $2^3 = 8$ ✓)'),
]

for (title, edge, face, formula, ex_lbl, ex1, ex2, ex3, ex4), ax in zip(rules, axes.flat):
    ax.axis('off')

    # Title bar
    title_box = mpatches.FancyBboxPatch(
        (0.05, 0.85), 0.9, 0.10,
        boxstyle='round,pad=0.02,rounding_size=0.02',
        facecolor=face, edgecolor=edge, linewidth=2.0,
        transform=ax.transAxes
    )
    ax.add_patch(title_box)
    ax.text(0.5, 0.90, title, fontsize=15, color='white',
            ha='center', va='center', fontweight='bold',
            transform=ax.transAxes)

    # Formula
    ax.text(0.5, 0.70, formula, fontsize=18, color=edge,
            ha='center', va='center', fontweight='bold',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                      edgecolor='#aa8b3a', linewidth=1.4))

    # Example label
    ax.text(0.08, 0.50, ex_lbl, fontsize=11, color=TEXT, fontweight='bold',
            ha='left', va='center', transform=ax.transAxes)

    # Example lines
    for y, line, fs in [(0.40, ex1, 14), (0.30, ex2, 13),
                        (0.18, ex3, 14), (0.05, ex4, 10)]:
        weight = 'bold' if fs >= 14 else 'normal'
        color = edge if fs >= 14 else TEXT
        ax.text(0.5, y, line, fontsize=fs, color=color, fontweight=weight,
                ha='center', va='center', transform=ax.transAxes,
                style=('italic' if line.startswith('(') else 'normal'))

fig.suptitle('Logarithm rules: same operations as exponents, expressed inside-out',
             fontsize=15, y=1.0, fontweight='bold')
plt.tight_layout()
plt.savefig('ch4_fig4_log_rules.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig4_log_rules.png")
