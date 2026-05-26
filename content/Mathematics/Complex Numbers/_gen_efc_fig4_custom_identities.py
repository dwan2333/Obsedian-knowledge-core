"""Generate efc_fig4_custom_identities.png — unit circle with labeled e^(i*theta) at common angles.

Show: theta = 0, pi/6, pi/4, pi/3, pi/2, 2pi/3, 3pi/4, 5pi/6, pi with each
point labeled with its exact closed-form e^(i*theta) value.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
YELLOW_EDGE = '#8c6520'
TEXT = '#222222'
MUTE = '#888888'

# Labeled angles and their closed-form expressions.
ANGLES = [
    (0,              r"$1$",                                     "0",         ORANGE_EDGE),
    (math.pi / 6,    r"$\frac{\sqrt{3}}{2} + \frac{i}{2}$",      r"$\pi/6$",  GREEN_EDGE),
    (math.pi / 4,    r"$\frac{\sqrt{2}}{2}(1 + i)$",             r"$\pi/4$",  PURPLE_EDGE),
    (math.pi / 3,    r"$\frac{1}{2} + i\frac{\sqrt{3}}{2}$",     r"$\pi/3$",  YELLOW_EDGE),
    (math.pi / 2,    r"$i$",                                     r"$\pi/2$",  '#aa6644'),
    (2 * math.pi / 3,r"$-\frac{1}{2} + i\frac{\sqrt{3}}{2}$",    r"$2\pi/3$", '#5588cc'),
    (3 * math.pi / 4,r"$-\frac{\sqrt{2}}{2}(1 - i)$",            r"$3\pi/4$", '#cc6688'),
    (5 * math.pi / 6,r"$-\frac{\sqrt{3}}{2} + \frac{i}{2}$",     r"$5\pi/6$", '#558866'),
    (math.pi,        r"$-1$",                                    r"$\pi$",    ORANGE_EDGE),
]

fig, ax = plt.subplots(figsize=(13, 11))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.55, -0.05, "Re", fontsize=13, color=MUTE, ha='left', va='top')
ax.text(-0.05, 1.55, "Im", fontsize=13, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.8, zorder=2)
ax.add_patch(circ)

# Tick labels.
for x, lbl in [(1, "1"), (-1, "-1")]:
    ax.plot([x, x], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.4, zorder=2)
    ax.text(x, -0.15, lbl, fontsize=11, color=BLUE_EDGE,
            ha='center', va='top', fontweight='bold')
for y, lbl in [(1, "i"), (-1, "-i")]:
    ax.plot([-0.04, 0.04], [y, y], color=BLUE_EDGE, linewidth=1.4, zorder=2)
    ax.text(-0.08, y, lbl, fontsize=11, color=BLUE_EDGE,
            ha='right', va='center', fontweight='bold')

# Plot each labeled point.
for theta, val, ang_lbl, col in ANGLES:
    P = np.array([math.cos(theta), math.sin(theta)])
    # Radius from origin (thin, muted).
    ax.plot([0, P[0]], [0, P[1]], color=col, linewidth=1.6,
            alpha=0.55, zorder=3)
    ax.scatter(P[0], P[1], s=85, color=col, edgecolor='white',
               linewidth=1.8, zorder=5)
    # Outward direction for label placement.
    outward = P / np.linalg.norm(P) if np.linalg.norm(P) > 0 else np.array([1.0, 0.0])
    lbl_pos = P + 0.28 * outward
    # Box around the closed-form value.
    ax.text(lbl_pos[0], lbl_pos[1], val,
            fontsize=13, color=col,
            ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='white',
                      edgecolor=col, linewidth=1.2))
    # Angle label inside, on the radius.
    inner_pos = P * 0.45
    ax.text(inner_pos[0], inner_pos[1], ang_lbl,
            fontsize=10, color=col,
            ha='center', va='center', fontstyle='italic')

# Footer box: the master identity.
ax.text(0.0, -1.70,
        r"$e^{i\theta} = \cos\theta + i\sin\theta$ — plug in any $\theta$ to get a designer identity",
        fontsize=13, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.45',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_title("Custom Euler identities — $e^{i\\theta}$ at common angles",
             fontsize=15, pad=12, color=TEXT, fontweight='bold')

ax.set_xlim(-2.05, 2.05)
ax.set_ylim(-2.0, 1.85)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('efc_fig4_custom_identities.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efc_fig4_custom_identities.png")
