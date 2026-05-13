"""Generate cnf_fig4_angle_sum.png — cis(alpha) * cis(beta) = cis(alpha+beta).

Three radii on the unit circle, at angles alpha, beta (separately drawn from
the positive real axis), and alpha+beta (the product). The picture shows that
multiplication of unit complex numbers is the SAME as adding their angles —
which is exactly why complex multiplication produces the angle-sum identities.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE_EDGE = '#1f4f8c'
GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

A = np.radians(30.0)        # alpha
B = np.radians(45.0)        # beta
S = A + B                   # alpha + beta = 75 deg

Pa = np.array([np.cos(A), np.sin(A)])
Ps = np.array([np.cos(S), np.sin(S)])

fig, ax = plt.subplots(figsize=(9, 8))

# Axes.
ax.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.axvline(0, color=MUTE, linewidth=0.9, zorder=1)
ax.text(1.45, -0.04, "Re", fontsize=12, color=MUTE, ha='left', va='top')
ax.text(-0.04, 1.45, "Im", fontsize=12, color=MUTE, ha='right', va='bottom')

# Unit circle.
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=1.8, zorder=2)
ax.add_patch(circ)

# Tick at 1.
ax.plot([1, 1], [-0.04, 0.04], color=BLUE_EDGE, linewidth=1.5, zorder=2)
ax.text(1, -0.10, "1", fontsize=11, color=BLUE_EDGE,
        ha='center', va='top', fontweight='bold')

# Radius to cis(alpha) — green.
ax.plot([0, Pa[0]], [0, Pa[1]], color=GREEN_EDGE, linewidth=2.6,
        solid_capstyle='round', zorder=3)
ax.scatter(Pa[0], Pa[1], s=58, color=GREEN_EDGE, zorder=5)
ax.text(Pa[0] + 0.04, Pa[1] - 0.05, r"$\mathrm{cis}(\alpha)$",
        fontsize=13, color=GREEN_EDGE,
        ha='left', va='top', fontweight='bold')

# Radius to cis(alpha+beta) — purple.
ax.plot([0, Ps[0]], [0, Ps[1]], color=PURPLE_EDGE, linewidth=2.6,
        solid_capstyle='round', zorder=3)
ax.scatter(Ps[0], Ps[1], s=58, color=PURPLE_EDGE, zorder=5)
ax.text(Ps[0] - 0.03, Ps[1] + 0.06,
        r"$\mathrm{cis}(\alpha+\beta)$",
        fontsize=13, color=PURPLE_EDGE,
        ha='right', va='bottom', fontweight='bold')

# Angle alpha arc (from x-axis to cis(alpha)).
arc_a = mpatches.Arc((0, 0), 0.45, 0.45, angle=0,
                     theta1=0, theta2=np.degrees(A),
                     color=GREEN_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_a)
ax.text(0.30 * np.cos(A / 2), 0.30 * np.sin(A / 2), r"$\alpha$",
        fontsize=14, color=GREEN_EDGE,
        ha='center', va='center', fontweight='bold', zorder=5)

# Angle beta arc (from cis(alpha) to cis(alpha+beta)).
arc_b = mpatches.Arc((0, 0), 0.85, 0.85, angle=0,
                     theta1=np.degrees(A), theta2=np.degrees(S),
                     color=PURPLE_EDGE, linewidth=2.0, zorder=4)
ax.add_patch(arc_b)
beta_mid = (A + S) / 2.0
ax.text(0.55 * np.cos(beta_mid), 0.55 * np.sin(beta_mid), r"$\beta$",
        fontsize=14, color=PURPLE_EDGE,
        ha='center', va='center', fontweight='bold', zorder=5)

# Title and explanation strip.
ax.set_title("Complex multiplication adds angles:  "
             r"$\mathrm{cis}(\alpha)\cdot\mathrm{cis}(\beta)=\mathrm{cis}(\alpha+\beta)$",
             fontsize=13, pad=10, color=TEXT, fontweight='bold')

# Below-diagram identity.
ax.text(0.0, -1.40,
        r"$\mathrm{Re}[\,\mathrm{cis}(\alpha)\,\mathrm{cis}(\beta)\,]"
        r"\;=\;\cos(\alpha+\beta)\;=\;\cos\alpha\cos\beta - \sin\alpha\sin\beta$",
        fontsize=12, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.set_xlim(-1.45, 1.65)
ax.set_ylim(-1.85, 1.45)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('cnf_fig4_angle_sum.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved cnf_fig4_angle_sum.png")
