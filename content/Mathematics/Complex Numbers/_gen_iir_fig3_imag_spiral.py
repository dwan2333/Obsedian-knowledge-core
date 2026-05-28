"""Generate iir_fig3_imag_spiral.png — discrete imaginary compounding spiral.

Starting at $1, multiply by (1 + i) each year. Track the first 8 years on
the complex plane: 1 -> 1+i -> 2i -> -2+2i -> -4 -> -4-4i -> -8i -> 8-8i -> 16.
Shows the 45-degree spiral with sqrt(2) scaling per step.
"""
import math
import cmath
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
PURPLE = '#b76db4'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#cccccc'

# Compute the spiral: M_k = (1 + i)^k starting from M_0 = 1.
N = 8
points = [(1 + 1j) ** k for k in range(N + 1)]

fig, ax = plt.subplots(figsize=(11, 11))

# Background grid
for v in range(-18, 19, 4):
    ax.axhline(v, color=GRID, linewidth=0.5, zorder=0)
    ax.axvline(v, color=GRID, linewidth=0.5, zorder=0)

# Main axes
ax.axhline(0, color=MUTE, linewidth=1.0, zorder=1)
ax.axvline(0, color=MUTE, linewidth=1.0, zorder=1)

# Axis labels
ax.text(17.5, -0.6, 'Re', fontsize=13, color=TEXT,
        ha='right', va='top', fontweight='bold', style='italic')
ax.text(-0.6, 17.5, 'Im', fontsize=13, color=TEXT,
        ha='right', va='top', fontweight='bold', style='italic')

# Reference markers on real axis
for x in [-16, -8, -4, -2, -1, 1, 2, 4, 8, 16]:
    ax.plot([x, x], [-0.3, 0.3], color=MUTE, linewidth=0.8, zorder=2)
    ax.text(x, -0.9, str(x), fontsize=9, color=MUTE,
            ha='center', va='top')
# Reference markers on imag axis
for y in [-16, -8, -4, -2, -1, 1, 2, 4, 8, 16]:
    ax.plot([-0.3, 0.3], [y, y], color=MUTE, linewidth=0.8, zorder=2)
    ax.text(-0.6, y, f'{y}i', fontsize=9, color=MUTE,
            ha='right', va='center')

# Draw spiral as arrows from each point to next
COLORS = [ORANGE_EDGE, BLUE_EDGE, GREEN_EDGE, PURPLE_EDGE,
          ORANGE_EDGE, BLUE_EDGE, GREEN_EDGE, PURPLE_EDGE]

for k in range(N):
    p0, p1 = points[k], points[k + 1]
    ax.annotate('', xy=(p1.real, p1.imag),
                xytext=(p0.real, p0.imag),
                arrowprops=dict(arrowstyle='->', color=COLORS[k],
                                lw=2.0, alpha=0.93,
                                mutation_scale=14),
                zorder=4)

# Plot points and label them
LABELS = [r'$M_0 = 1$', r'$M_1 = 1+i$', r'$M_2 = 2i$',
          r'$M_3 = -2+2i$', r'$M_4 = -4$', r'$M_5 = -4-4i$',
          r'$M_6 = -8i$', r'$M_7 = 8-8i$', r'$M_8 = 16$']
OFFSETS = [(0.6, 0.5), (0.6, 0.4), (0.4, 0.6), (-0.4, 0.6),
           (-0.4, -1.1), (-0.5, -0.9), (0.5, -1.1), (0.6, -0.8),
           (0.6, 0.5)]
DOT_COLORS = [TEXT, ORANGE, BLUE, GREEN, PURPLE,
              ORANGE, BLUE, GREEN, PURPLE]

for k, (p, lbl, (dx, dy), c) in enumerate(zip(points, LABELS, OFFSETS, DOT_COLORS)):
    ax.scatter([p.real], [p.imag], s=80, color=c,
               edgecolor='black', linewidth=1.4, zorder=5)
    ax.text(p.real + dx, p.imag + dy, lbl,
            fontsize=11, color=TEXT, fontweight='bold',
            ha='left' if dx >= 0 else 'right',
            va='bottom' if dy >= 0 else 'top',
            bbox=dict(boxstyle='round,pad=0.2',
                      facecolor='white', edgecolor='none', alpha=0.85))

# Highlight the start and -4 milestone
ax.scatter([1], [0], s=250, marker='*', color='gold',
           edgecolor='#aa8b3a', linewidth=1.4, zorder=6)
ax.scatter([-4], [0], s=250, marker='*', color='#d97777',
           edgecolor='#7a3030', linewidth=1.4, zorder=6)
ax.scatter([16], [0], s=250, marker='*', color='#77d977',
           edgecolor='#307a30', linewidth=1.4, zorder=6)

# Annotate key milestones
ax.annotate('Year 4: debt of \\$4!',
            xy=(-4, 0), xytext=(-12, -3),
            fontsize=11.5, color='#7a3030', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#7a3030', lw=1.4),
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='#ffe8e8', edgecolor='#7a3030'))
ax.annotate('Year 8: $\\$16$ asset',
            xy=(16, 0), xytext=(7, 3.5),
            fontsize=11.5, color='#307a30', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#307a30', lw=1.4),
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='#e8ffe8', edgecolor='#307a30'))

# Title
ax.set_title(r'Discrete imaginary compounding: $M_{k+1} = M_k (1+i)$,'
             '\nrotating $45\\degree$ and scaling by $\\sqrt{2}$ per year',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-17, 19)
ax.set_ylim(-15, 17)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('iir_fig3_imag_spiral.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig3_imag_spiral.png")
