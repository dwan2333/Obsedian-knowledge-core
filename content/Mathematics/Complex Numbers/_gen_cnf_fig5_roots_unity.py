"""Generate cnf_fig5_roots_unity.png — the cube roots of unity on the unit circle.

Three points equally spaced at angles 0, 120, 240 degrees. Each is labeled
with its coordinates: 1, -1/2 + i*sqrt(3)/2, -1/2 - i*sqrt(3)/2.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'

ANGLES_DEG = [0, 120, 240]
COLORS_FACE = [ORANGE_EDGE, GREEN_EDGE, PURPLE_EDGE]
LABELS = [
    r"$1$",
    r"$-\frac{1}{2} + i\frac{\sqrt{3}}{2}$",
    r"$-\frac{1}{2} - i\frac{\sqrt{3}}{2}$",
]

fig, ax = plt.subplots(figsize=(8, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.40, -0.04, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.04, 1.40, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.8, zorder=2)
ax.add_patch(circ)

# Ticks at 1, -1, i, -i.
for x, lbl in [(1, "1"), (-1, "-1")]:
    ax.plot([x, x], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.5, zorder=2)
    ax.text(x, -0.12, lbl, fontsize=10, color=BLUE_EDGE,
            ha='center', va='top')
for y, lbl in [(1, "i"), (-1, "-i")]:
    ax.plot([-0.04, 0.04], [y, y], color=BLUE_EDGE, linewidth=1.5, zorder=2)
    ax.text(-0.06, y, lbl, fontsize=10, color=BLUE_EDGE,
            ha='right', va='center')

# Plot each root with its radius and label.
for ang_deg, col, lbl in zip(ANGLES_DEG, COLORS_FACE, LABELS):
    ang = np.radians(ang_deg)
    P = np.array([np.cos(ang), np.sin(ang)])
    ax.plot([0, P[0]], [0, P[1]], color=col, linewidth=2.4,
            solid_capstyle='round', zorder=3)
    ax.scatter(P[0], P[1], s=72, color=col, zorder=5)
    # Label position: outward radial offset.
    lp = 1.18 * P
    ax.text(lp[0], lp[1], lbl, fontsize=13, color=col,
            ha='center', va='center', fontweight='bold')

# Connect the three roots with light dashed lines (showing equilateral triangle).
pts = [(np.cos(np.radians(a)), np.sin(np.radians(a))) for a in ANGLES_DEG]
tri = mpatches.Polygon(pts, closed=True, fill=False,
                       edgecolor=MUTE, linewidth=1.2,
                       linestyle='--', zorder=2)
ax.add_patch(tri)

# Annotate the 120-degree spacing.
for i, ang_deg in enumerate(ANGLES_DEG):
    next_deg = ANGLES_DEG[(i + 1) % len(ANGLES_DEG)]
    mid_deg = (ang_deg + next_deg) / 2 if next_deg > ang_deg else (ang_deg + (next_deg + 360)) / 2
    mid_ang = np.radians(mid_deg)
    if i == 0:  # only annotate one arc for clarity.
        arc = mpatches.Arc((0, 0), 0.7, 0.7, angle=0,
                           theta1=ang_deg, theta2=next_deg,
                           color=MUTE, linewidth=1.5, zorder=4)
        ax.add_patch(arc)
        ax.text(0.45 * np.cos(mid_ang), 0.45 * np.sin(mid_ang),
                r"$120\degree$", fontsize=12, color=MUTE,
                ha='center', va='center', fontweight='bold')

# Title and identity below.
ax.set_title(r"Cube roots of unity: solutions to $x^{3} = 1$",
             fontsize=14, pad=12, color=TEXT, fontweight='bold')

ax.text(0.0, -1.55,
        r"$x^{3} = 1$  $\Rightarrow$  three roots equally spaced on the unit circle "
        r"at $0\degree, 120\degree, 240\degree$",
        fontsize=12, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_xlim(-1.65, 1.65)
ax.set_ylim(-1.95, 1.55)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_fig5_roots_unity.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_fig5_roots_unity.png")
