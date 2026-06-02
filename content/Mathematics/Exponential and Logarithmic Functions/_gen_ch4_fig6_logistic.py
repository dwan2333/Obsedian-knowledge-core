"""Generate ch4_fig6_logistic.png — logistic growth curve with carrying capacity.

Shows f(t) = c / (1 + a*e^{-bt}) — S-shaped curve approaching carrying
capacity c. Three regions annotated: exponential-like growth phase,
inflection point, saturation toward c.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222'
MUTE = '#888'
GRID = '#e6e6e6'

# Logistic: f(t) = c / (1 + a e^{-bt})
c = 100  # carrying capacity
a = 20   # initial inverse-ratio
b = 0.6
t = np.linspace(0, 12, 600)
f = c / (1 + a * np.exp(-b * t))

fig, ax = plt.subplots(figsize=(12, 7))
ax.grid(True, color=GRID, lw=0.6, zorder=0)
ax.axhline(0, color=MUTE, lw=0.9, zorder=1)
ax.axvline(0, color=MUTE, lw=0.9, zorder=1)

# Carrying capacity asymptote
ax.axhline(c, color=ORANGE_EDGE, lw=1.6, linestyle='--', zorder=2,
           alpha=0.85, label=f'Carrying capacity $c = {c}$')

# Inflection point: t* = ln(a)/b, f(t*) = c/2
t_inflect = math.log(a) / b
f_inflect = c / 2
ax.scatter([t_inflect], [f_inflect], s=180, color=PURPLE_EDGE,
           edgecolor='white', linewidth=2.0, zorder=7)
ax.annotate(f'Inflection point\n$t = \\ln(a)/b \\approx {t_inflect:.2f}$\n$f = c/2 = {f_inflect}$',
            xy=(t_inflect, f_inflect),
            xytext=(t_inflect + 1.5, 40),
            fontsize=10.5, color=PURPLE_EDGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=PURPLE_EDGE, lw=1.4),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f3e0f0',
                      edgecolor=PURPLE_EDGE))

# Main curve
ax.plot(t, f, color=BLUE_EDGE, linewidth=3.0, zorder=4,
        label=r'$f(t) = \dfrac{c}{1 + a\, e^{-bt}}$')

# Annotate three regions
ax.text(1, 18, 'Phase 1:\nnear-exponential\ngrowth', fontsize=10,
        color=GREEN_EDGE, fontweight='bold', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f1d8',
                  edgecolor=GREEN_EDGE, linewidth=1.0))
ax.text(t_inflect, 95, 'Phase 2:\nlinear-like\nat inflection', fontsize=10,
        color=PURPLE_EDGE, fontweight='bold', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f3e0f0',
                  edgecolor=PURPLE_EDGE, linewidth=1.0))
ax.text(10, 60, 'Phase 3:\nsaturation\ntoward $c$', fontsize=10,
        color=ORANGE_EDGE, fontweight='bold', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffeed8',
                  edgecolor=ORANGE_EDGE, linewidth=1.0))

# y-intercept
y_int = c / (1 + a)
ax.scatter([0], [y_int], s=120, color=GREEN_EDGE, edgecolor='white',
           linewidth=1.6, zorder=6, marker='*')
ax.text(-0.5, y_int, f'$f(0) = {y_int:.1f}$', fontsize=10,
        color=GREEN_EDGE, fontweight='bold', ha='right', va='center')

ax.set_xlabel('Time $t$', fontsize=12)
ax.set_ylabel('$f(t)$', fontsize=12)
ax.set_title('Logistic growth model: bounded by carrying capacity',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax.legend(loc='center right', fontsize=11)
ax.set_xlim(-0.8, 12.2)
ax.set_ylim(-8, 115)

# Real-world callout
ax.text(6, 8,
        'Real-world fits: spread of a disease in a closed population,'
        '\nadoption of a new technology, growth of a species with limited resources.',
        fontsize=10, color=TEXT, ha='center', va='center', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f4f4ee',
                  edgecolor=MUTE, linewidth=1.0))

plt.tight_layout()
plt.savefig('ch4_fig6_logistic.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig6_logistic.png")
