"""Generate iir_fig5_eit_circle.png — e^{it} on the unit circle with key points.

Unit circle with annotations: e^{0}=1, e^{i*pi/2}=i, e^{i*pi}=-1, e^{i*3pi/2}=-i,
e^{2*pi*i}=1. Counter-clockwise arrow showing direction of travel at angular
speed 1 rad/yr.
"""
import math
import numpy as np
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
GOLD = '#d4a04a'
GOLD_EDGE = '#8c6520'
TEXT = '#222222'
MUTE = '#888888'

fig, ax = plt.subplots(figsize=(10, 10))

# Background grid
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)

# Axis labels
ax.text(1.45, -0.08, 'Re', fontsize=12, color=TEXT,
        ha='right', va='top', fontweight='bold', style='italic')
ax.text(-0.06, 1.45, 'Im', fontsize=12, color=TEXT,
        ha='right', va='top', fontweight='bold', style='italic')

# Unit circle
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=2.6, zorder=2)
ax.add_patch(circ)

# Direction arrow (counterclockwise) -- draw at angle near 30deg
arc_pts = np.linspace(math.radians(20), math.radians(60), 30)
arc_xs = 1.18 * np.cos(arc_pts)
arc_ys = 1.18 * np.sin(arc_pts)
ax.plot(arc_xs, arc_ys, color=GREEN_EDGE, linewidth=2.0, zorder=3)
# Arrowhead at end of arc
end_a = math.radians(60)
ax.annotate('', xy=(1.18 * math.cos(end_a + 0.04),
                    1.18 * math.sin(end_a + 0.04)),
            xytext=(1.18 * math.cos(end_a),
                    1.18 * math.sin(end_a)),
            arrowprops=dict(arrowstyle='->', color=GREEN_EDGE,
                            lw=2.2, mutation_scale=18),
            zorder=4)
ax.text(1.22 * math.cos(math.radians(40)),
        1.22 * math.sin(math.radians(40)),
        r'$+t$ (counterclockwise)',
        fontsize=11, color=GREEN_EDGE, fontweight='bold',
        rotation=-50, rotation_mode='anchor',
        ha='center', va='center')

# Key e^{it} points
key_points = [
    (0,         r'$e^{i \cdot 0} = 1$',          (0.12, -0.18), GOLD, GOLD_EDGE),
    (math.pi/2, r'$e^{i\pi/2} = i$',             (0.05,  0.12), BLUE, BLUE_EDGE),
    (math.pi,   r'$e^{i\pi} = -1$',              (-0.12, -0.18), ORANGE, ORANGE_EDGE),
    (3*math.pi/2, r'$e^{i \cdot 3\pi/2} = -i$', (0.05, -0.18), PURPLE, PURPLE_EDGE),
]

for theta, label, (dx, dy), face, edge in key_points:
    x, y = math.cos(theta), math.sin(theta)
    ax.scatter([x], [y], s=240, color=face,
               edgecolor=edge, linewidth=2.0, zorder=5)
    # Arrow from origin to point (faint)
    ax.plot([0, x], [0, y], color=edge, linewidth=1.0,
            linestyle=':', alpha=0.5, zorder=2)
    # Label
    ha = 'left' if dx > 0 else 'right' if dx < 0 else 'center'
    va = 'bottom' if dy > 0 else 'top'
    ax.text(x + dx, y + dy, label, fontsize=14, color=edge,
            ha=ha, va=va, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='white', edgecolor=edge, linewidth=1.4))

# Euler's identity callout
ax.text(0, -1.65,
        r'After $t = \pi$ years at imaginary interest:'
        '\n'
        r'$e^{i\pi} = -1 \;\Leftrightarrow\; e^{i\pi}+1=0$',
        fontsize=13, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

# Title
ax.set_title('$e^{it}$: walking around the unit circle at speed 1 rad/yr',
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.95, 1.55)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('iir_fig5_eit_circle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig5_eit_circle.png")
