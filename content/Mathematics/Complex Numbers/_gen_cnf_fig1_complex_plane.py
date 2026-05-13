"""Generate cnf_fig1_complex_plane.png — the complex plane with two example vectors.

The horizontal axis is the real axis, vertical is the imaginary axis. Imaginary
axis is annotated with i, -i, -2i tick marks. Two example complex numbers are
drawn as vectors from the origin: 4+i (green) and -2+2i (orange).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

fig, ax = plt.subplots(figsize=(9, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(5.0, -0.35, "Real axis", fontsize=12, color=MUTE,
        ha='right', va='top', style='italic')
ax.text(-0.25, 3.4, "Imaginary axis", fontsize=12, color=MUTE,
        ha='right', va='top', style='italic', rotation=90)

# Grid (light).
for x in range(-3, 6):
    ax.axvline(x, color='#eeeeee', linewidth=0.5, zorder=0)
for y in range(-2, 4):
    ax.axhline(y, color='#eeeeee', linewidth=0.5, zorder=0)

# Tick marks and labels on the imaginary axis.
for y, lbl in [(1, 'i'), (-1, '-i'), (-2, '-2i'), (2, '2i')]:
    ax.plot([-0.08, 0.08], [y, y], color=BLUE_EDGE, linewidth=1.4, zorder=2)
    ax.text(-0.18, y, lbl, fontsize=14, color=BLUE_EDGE,
            ha='right', va='center', fontweight='bold')

# Tick marks on the real axis.
for x in range(-2, 5):
    if x == 0:
        continue
    ax.plot([x, x], [-0.08, 0.08], color=MUTE, linewidth=1.2, zorder=2)
    ax.text(x, -0.18, str(x), fontsize=10, color=MUTE,
            ha='center', va='top')

# Origin label.
ax.text(-0.15, -0.18, "0", fontsize=11, color=TEXT,
        ha='right', va='top', fontweight='bold')

# Vector 1: 4 + i — green.
ax.annotate('', xy=(4, 1), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=GREEN_EDGE, lw=2.6,
                            mutation_scale=20),
            zorder=4)
ax.scatter([4], [1], s=58, color=GREEN_EDGE, zorder=5)
ax.text(4.0, 1.25, r"$4 + i$", fontsize=15, color=GREEN_EDGE,
        ha='left', va='bottom', fontweight='bold')

# Vector 2: -2 + 2i — orange.
ax.annotate('', xy=(-2, 2), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=2.6,
                            mutation_scale=20),
            zorder=4)
ax.scatter([-2], [2], s=58, color=ORANGE_EDGE, zorder=5)
ax.text(-2.0, 2.25, r"$-2 + 2i$", fontsize=15, color=ORANGE_EDGE,
        ha='center', va='bottom', fontweight='bold')

# Highlight i with a small marker (it's the unit imaginary).
ax.scatter([0], [1], s=60, color=BLUE_EDGE, zorder=5)
ax.text(0.18, 1, r"$i$", fontsize=14, color=BLUE_EDGE,
        ha='left', va='center', fontweight='bold')

ax.set_title("The complex plane — points as vectors",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-3.5, 5.3)
ax.set_ylim(-2.5, 3.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_fig1_complex_plane.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_fig1_complex_plane.png")
