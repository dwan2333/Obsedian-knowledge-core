"""Generate pi_fig4_quarter_circle.png — quarter circle with area from 0 to 1/2
decomposed into a 30-deg sector (area = pi/12) and a right triangle (area = sqrt(3)/8).
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'; TEXT = '#222'; MUTE = '#888'

fig, ax = plt.subplots(figsize=(10, 9))
ax.set_aspect('equal')

# Quarter-circle arc (top-right) from (1,0) to (0,1)
theta_arc = np.linspace(0, math.pi / 2, 200)
x_arc = np.cos(theta_arc); y_arc = np.sin(theta_arc)
ax.plot(x_arc, y_arc, color=BLUE_EDGE, linewidth=2.4, zorder=4)

# Sector shading: 0 to 30 degrees (= 0 to pi/6 radians)
# Region under arc from x=0 to x=1/2
# Decompose into:
#   - 30-deg circular sector: triangle from (0,0) to (1/2, sqrt(3)/2) plus the arc segment
# Actually it's: the region from the origin out to (1/2, sqrt(3)/2) along the radius,
# bounded by the arc from (1/2, sqrt(3)/2) up to (1,0) -- no wait.
# Simpler: the area under the curve y = sqrt(1-x^2) from x=0 to x=1/2
# equals (sector from theta=60 to theta=90, which is 30 deg) + (right triangle (0,0)-(1/2,0)-(1/2, sqrt(3)/2))
# Actually 30 deg sector in the upper part:
# The angle at (1/2, sqrt(3)/2) from positive x-axis is 60 deg.
# The "30-deg sector" mentioned is the sector from angle=60 to angle=90 (so 30 degrees wide).
# And the right triangle is (0,0)-(1/2, 0)-(1/2, sqrt(3)/2), area = (1/2)*(1/2)*(sqrt(3)/2) = sqrt(3)/8.

# Sector (purple): from 60 deg to 90 deg
sec_theta = np.linspace(math.pi / 3, math.pi / 2, 100)
sec_x = np.concatenate([[0], np.cos(sec_theta), [0]])
sec_y = np.concatenate([[0], np.sin(sec_theta), [0]])
ax.fill(sec_x, sec_y, facecolor=PURPLE_EDGE, alpha=0.35,
        edgecolor=PURPLE_EDGE, linewidth=1.6, zorder=3)

# Triangle (green): (0,0), (1/2, 0), (1/2, sqrt(3)/2)
tri_x = [0, 0.5, 0.5, 0]
tri_y = [0, 0, math.sqrt(3) / 2, 0]
ax.fill(tri_x, tri_y, facecolor=GREEN_EDGE, alpha=0.30,
        edgecolor=GREEN_EDGE, linewidth=1.6, zorder=3)

# Axes
ax.axhline(0, color=MUTE, lw=1.0, zorder=2)
ax.axvline(0, color=MUTE, lw=1.0, zorder=2)

# Mark points
ax.scatter([0, 1, 0.5, 0.5], [0, 0, 0, math.sqrt(3) / 2],
           s=70, color=TEXT, edgecolor='white', linewidth=1.4, zorder=6)
ax.text(0, -0.07, '0', fontsize=11, color=MUTE, ha='center', va='top')
ax.text(0.5, -0.07, r'$\frac{1}{2}$', fontsize=14, color=TEXT,
        ha='center', va='top', fontweight='bold')
ax.text(1, -0.07, '1', fontsize=11, color=MUTE, ha='center', va='top')
ax.text(0.55, math.sqrt(3) / 2, r'$\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)$',
        fontsize=11, color=TEXT, ha='left', va='center', fontweight='bold')

# Triangle base label (1/2)
ax.text(0.25, -0.07, r'$\frac{1}{2}$', fontsize=11, color=GREEN_EDGE,
        ha='center', va='top', fontweight='bold')
# Triangle height label (sqrt(3)/2)
ax.text(0.53, math.sqrt(3) / 4, r'$\frac{\sqrt{3}}{2}$',
        fontsize=12, color=GREEN_EDGE, ha='left', va='center', fontweight='bold')

# Sector label
ax.text(0.18, 0.55, r'$\dfrac{\pi}{12}$', fontsize=18, color=PURPLE_EDGE,
        ha='center', va='center', fontweight='bold')
# Triangle label
ax.text(0.31, 0.20, r'$\dfrac{\sqrt{3}}{8}$', fontsize=18, color=GREEN_EDGE,
        ha='center', va='center', fontweight='bold')

# 30-degree marker
ax.add_patch(mpatches.Arc((0, 0), 0.4, 0.4,
                          angle=0, theta1=60, theta2=90,
                          color=PURPLE_EDGE, linewidth=2.0))
ax.text(0.10, 0.21, r'$30^\circ$', fontsize=10, color=PURPLE_EDGE,
        ha='center', va='center', fontweight='bold')

# Radius lines to the inflection point and to (1,0)
ax.plot([0, 0.5], [0, math.sqrt(3) / 2], color=PURPLE_EDGE,
        linewidth=1.4, linestyle='--', alpha=0.7, zorder=4)
ax.plot([0, 1], [0, 0], color=MUTE, linewidth=0.8,
        linestyle=':', alpha=0.5, zorder=2)

# Title
ax.set_title(r'Integral $\int_0^{1/2}\sqrt{1-x^2}\,dx$ = $30^\circ$ sector $\frac{\pi}{12}$ + right triangle $\frac{\sqrt{3}}{8}$',
             fontsize=13, pad=10, color=TEXT, fontweight='bold')

# Footer formula
ax.text(0.6, -0.30,
        r'$\frac{\pi}{12} + \frac{\sqrt{3}}{8} = \int_0^{1/2}\sqrt{1-x^2}\,dx$' '\n'
        r'$\Rightarrow\;\;\; \pi = 12\,\left[\int_0^{1/2}\sqrt{1-x^2}\,dx - \frac{\sqrt{3}}{8}\right]$',
        fontsize=13, color=TEXT, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_xlim(-0.15, 1.2); ax.set_ylim(-0.55, 1.15)
ax.axis('off')

plt.tight_layout()
plt.savefig('pi_fig4_quarter_circle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pi_fig4_quarter_circle.png")
