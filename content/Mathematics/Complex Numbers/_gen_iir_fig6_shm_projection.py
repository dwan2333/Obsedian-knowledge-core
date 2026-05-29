"""Generate iir_fig6_shm_projection.png — circular motion projected to cosine.

Two side-by-side panels:
LEFT: rotating point on unit circle in (Re, Im) plane. A vertical dashed line
drops from the point to the real axis showing the "shadow" / projection.
RIGHT: cos(omega*t) wave over time, with the same point's x-coordinate
marked at the corresponding t.

This makes visible the claim "simple harmonic motion is the shadow of
circular motion on a line."
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
GRID = '#e6e6e6'

# Time at which we mark the "current" point
omega = 1.0
T_now = 1.2  # rad

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 6),
                                gridspec_kw={'width_ratios': [1, 1.5]})

# ---- LEFT panel: unit circle with rotating point and shadow ----

# Axes
ax1.axhline(0, color=MUTE, linewidth=0.9, zorder=1)
ax1.axvline(0, color=MUTE, linewidth=0.9, zorder=1)

# Unit circle
circ = mpatches.Circle((0, 0), 1.0, fill=False,
                       edgecolor=BLUE_EDGE, linewidth=2.4, zorder=2)
ax1.add_patch(circ)

# Tick labels
for x, lbl in [(1, '1'), (-1, '-1')]:
    ax1.plot([x, x], [-0.04, 0.04], color=MUTE, linewidth=1.0, zorder=2)
    ax1.text(x, -0.15, lbl, fontsize=10, color=MUTE,
             ha='center', va='top')
ax1.text(0.06, 1.02, 'i', fontsize=10, color=MUTE, ha='left', va='bottom')
ax1.text(0.06, -1.02, '-i', fontsize=10, color=MUTE, ha='left', va='top')

# Axis labels
ax1.text(1.42, -0.08, 'Re = position', fontsize=11, color=TEXT,
         ha='right', va='top', fontstyle='italic')
ax1.text(-0.06, 1.42, 'Im', fontsize=11, color=TEXT,
         ha='right', va='top', fontstyle='italic')

# Current rotating point
x_now = math.cos(omega * T_now)
y_now = math.sin(omega * T_now)

# Arc showing path traveled (from t=0 to t=T_now)
theta_arc = np.linspace(0, omega * T_now, 80)
ax1.plot(np.cos(theta_arc), np.sin(theta_arc),
         color=GREEN_EDGE, linewidth=3.0, zorder=3)

# Radius vector to current point
ax1.annotate('', xy=(x_now, y_now), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE,
                             lw=2.4, mutation_scale=16),
             zorder=4)

# Current point
ax1.scatter([x_now], [y_now], s=180, color=ORANGE,
            edgecolor=ORANGE_EDGE, linewidth=2.0, zorder=5)

# Vertical drop line to real axis (the "shadow")
ax1.plot([x_now, x_now], [y_now, 0], color=PURPLE_EDGE, linewidth=1.8,
         linestyle='--', zorder=4)

# Shadow point on the real axis
ax1.scatter([x_now], [0], s=180, color=PURPLE,
            edgecolor=PURPLE_EDGE, linewidth=2.0, zorder=6)
ax1.text(x_now + 0.05, -0.25, f'shadow:\nx = cos(ωt) = {x_now:.2f}',
         fontsize=11, color=PURPLE_EDGE, fontweight='bold',
         ha='left', va='top')

# Label rotating point
ax1.text(x_now + 0.10, y_now + 0.06, f'$e^{{i\\omega t}}$',
         fontsize=13, color=ORANGE_EDGE, fontweight='bold',
         ha='left', va='bottom')

ax1.set_title('Circular motion: $e^{i\\omega t}$',
              fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax1.set_xlim(-1.55, 1.55)
ax1.set_ylim(-1.55, 1.55)
ax1.set_aspect('equal')
ax1.axis('off')

# ---- RIGHT panel: cosine wave (the projection) ----

t_axis = np.linspace(0, 4 * math.pi, 600)
cos_wave = np.cos(omega * t_axis)

ax2.grid(True, color=GRID, linewidth=0.7, zorder=0)
ax2.axhline(0, color=MUTE, linewidth=0.9, zorder=1)

# Full wave
ax2.plot(t_axis, cos_wave, color=BLUE_EDGE, linewidth=2.4, zorder=3,
         label=r'$x(t) = \cos(\omega t)$')

# Highlight portion up to T_now
mask = t_axis <= T_now
ax2.plot(t_axis[mask], cos_wave[mask], color=GREEN_EDGE, linewidth=3.2,
         zorder=4)

# Mark current point
ax2.scatter([T_now], [x_now], s=180, color=PURPLE,
            edgecolor=PURPLE_EDGE, linewidth=2.0, zorder=5)

# Drop line from x-axis to point
ax2.plot([T_now, T_now], [0, x_now], color=PURPLE_EDGE, linewidth=1.6,
         linestyle='--', zorder=4)

# Horizontal connector to show this = same shadow value
ax2.annotate(f'x = {x_now:.2f}', xy=(T_now, x_now),
             xytext=(T_now - 0.5, x_now + 0.25),
             fontsize=11, color=PURPLE_EDGE, fontweight='bold',
             ha='right', va='bottom',
             arrowprops=dict(arrowstyle='->', color=PURPLE_EDGE,
                             lw=1.2))

# Period markers
for n_period in range(1, 3):
    t_p = n_period * 2 * math.pi / omega
    if t_p < t_axis[-1]:
        ax2.axvline(t_p, color=MUTE, linewidth=0.8, linestyle=':',
                    alpha=0.6, zorder=1)

# Pi tick labels
pi_ticks = [0, math.pi, 2*math.pi, 3*math.pi, 4*math.pi]
pi_lbls = ['0', 'π', '2π', '3π', '4π']
ax2.set_xticks(pi_ticks)
ax2.set_xticklabels(pi_lbls)

# Mark T_now with vertical tick
ax2.scatter([T_now], [0], s=30, color=PURPLE_EDGE, zorder=5)
ax2.text(T_now, -1.15, f't = {T_now:.2f}', fontsize=9, color=PURPLE_EDGE,
         ha='center', va='top', fontweight='bold')

ax2.set_xlabel('t (time)', fontsize=11, color=TEXT)
ax2.set_ylabel('x (position)', fontsize=11, color=TEXT)
ax2.set_title('Projection to real axis: $x(t) = \\cos(\\omega t)$',
              fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax2.set_xlim(-0.2, 4*math.pi + 0.2)
ax2.set_ylim(-1.3, 1.5)
ax2.legend(loc='upper right', fontsize=10, frameon=True)

fig.suptitle('Simple harmonic motion is the shadow of $e^{i\\omega t}$ on the real line',
             fontsize=14, y=1.0, color=TEXT, fontweight='bold')

plt.tight_layout()
plt.savefig('iir_fig6_shm_projection.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig6_shm_projection.png")
