"""Generate iir_fig7_shm_phase_space.png — phase space of a mass on a spring.

Single panel: 2D plane with horizontal axis = position x, vertical axis =
v/omega (rescaled velocity). Plot the closed circular orbit traced by the
state (x, v/omega) as the mass oscillates. Mark key states:
- (1, 0): max stretch, zero velocity
- (0, 1): zero displacement, max velocity (moving toward +x... wait, in phase space the rotation direction matters)
- (-1, 0): max compression, zero velocity
- (0, -1): zero displacement, max velocity in opposite direction

Annotate the orbit with the discrete update rule from the video:
delta_x = v * delta_t (horizontal change proportional to velocity)
delta_v = -(k/m) * x * delta_t (vertical change proportional to negative position)
This is exactly the "perpendicular nudge" pattern -- rotation by 90 degrees.

This makes the imaginary-interest <-> SHM bridge explicit.
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
RED = '#7a3030'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

fig, ax = plt.subplots(figsize=(10.5, 10))

# Background grid
for g in [-1.5, -1.0, -0.5, 0.5, 1.0, 1.5]:
    ax.axhline(g, color=GRID, linewidth=0.6, zorder=0)
    ax.axvline(g, color=GRID, linewidth=0.6, zorder=0)

# Main axes
ax.axhline(0, color=MUTE, linewidth=1.0, zorder=1)
ax.axvline(0, color=MUTE, linewidth=1.0, zorder=1)

# Axis labels
ax.text(1.85, -0.10, 'position x', fontsize=14, color=TEXT,
        ha='right', va='top', fontweight='bold', fontstyle='italic')
ax.text(-0.08, 1.85, 'velocity / ω', fontsize=14, color=TEXT,
        ha='right', va='top', fontweight='bold', fontstyle='italic')

# The orbit -- a unit circle (after rescaling v -> v/omega)
orbit_theta = np.linspace(0, 2 * math.pi, 200)
ax.plot(np.cos(orbit_theta), np.sin(orbit_theta),
        color=BLUE_EDGE, linewidth=2.6, zorder=2)

# Tick labels at +-1
for x, lbl in [(1, '1'), (-1, '-1'), (0, '')]:
    if lbl:
        ax.plot([x, x], [-0.04, 0.04], color=MUTE, linewidth=1.0, zorder=2)
        ax.text(x, -0.13, lbl, fontsize=10, color=MUTE,
                ha='center', va='top')
for y, lbl in [(1, '1'), (-1, '-1')]:
    ax.plot([-0.04, 0.04], [y, y], color=MUTE, linewidth=1.0, zorder=2)
    ax.text(-0.06, y, lbl, fontsize=10, color=MUTE,
            ha='right', va='center')

# Direction arrows around the orbit (clockwise rotation -- physics convention
# for SHM in (x, v) phase space). We want delta_x = v*dt and delta_v = -omega^2*x*dt.
# At (1, 0): v=0, so dx=0. At (0, 1) [x=0, v/omega = 1]: dx = v*dt > 0, dv/omega = -x*dt = 0.
# Hmm let me think -- with state (x, v/omega), update is:
#   dx/dt = v
#   d(v/omega)/dt = (1/omega) * (-omega^2 x) = -omega * x
# Rescaling t -> tau = omega*t: dx/dtau = v/omega, d(v/omega)/dtau = -x
# So in (x, v/omega) plane the orbit is a clockwise circle:
#   At (1, 0): rotation vector is (0, -1) -- points DOWN. So clockwise.
# Let me place arrowheads showing CCW... wait. d(x)/dtau = v/omega (which is the y-coord).
# At (1, 0): dx/dtau = 0, d(v/omega)/dtau = -1. So state moves DOWN. Yes clockwise.

# Place arrowheads at 4 cardinal points showing direction of motion
arrow_angles = [0, math.pi/2, math.pi, 3*math.pi/2]  # at right, top, left, bottom
for a in arrow_angles:
    p_at = (math.cos(a), math.sin(a))
    # Tangent direction for CLOCKWISE motion: 90 degrees right of radial outward.
    # In (x, y) = (cos a, sin a), the tangent CCW is (-sin a, cos a). For CW it's (sin a, -cos a).
    tan_dir = (math.sin(a), -math.cos(a))
    # Arrow tip 0.08 ahead along tangent
    ahead = (p_at[0] + 0.06 * tan_dir[0], p_at[1] + 0.06 * tan_dir[1])
    ax.annotate('', xy=ahead, xytext=p_at,
                arrowprops=dict(arrowstyle='->', color=BLUE_EDGE,
                                lw=2.4, mutation_scale=20),
                zorder=3)

# Mark key states with labels
states = [
    (1, 0, 'Max stretch\n(x=A, v=0)', (0.10, -0.18), GOLD, GOLD_EDGE),
    (0, -1, 'Max speed left\n(x=0, v=-ωA)', (-0.05, -0.18), PURPLE, PURPLE_EDGE),
    (-1, 0, 'Max compress\n(x=-A, v=0)', (-0.10, 0.16), ORANGE, ORANGE_EDGE),
    (0, 1, 'Max speed right\n(x=0, v=+ωA)', (0.05, 0.18), GREEN, GREEN_EDGE),
]

for x, y, lbl, (dx, dy), face, edge in states:
    ax.scatter([x], [y], s=260, color=face, edgecolor=edge,
               linewidth=2.0, zorder=5)
    ha = 'left' if dx > 0 else 'right' if dx < 0 else 'center'
    va = 'top' if dy < 0 else 'bottom'
    ax.text(x + dx, y + dy, lbl, fontsize=10.5, color=edge,
            ha=ha, va=va, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.25',
                      facecolor='white', edgecolor=edge, linewidth=1.0))

# Discrete update rule annotations (the video's quiz answer)
ax.text(0, -1.85,
        r'Discrete update from $\ddot x = -\omega^2 x$:'
        '\n'
        r'$\Delta x = v\,\Delta t$    $\Delta(v/\omega) = -\omega\,x\,\Delta t$',
        fontsize=12, color=TEXT, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

# Connection to imaginary interest (callout in upper right)
ax.text(1.65, 1.65,
        'Same as imaginary interest!\n'
        r'$z = x + i(v/\omega)$' '\n'
        r'$\dot z = -i\omega\,z$' '\n'
        r'$z(t) = z(0)\,e^{-i\omega t}$',
        fontsize=11, color=RED, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#ffe8e8', edgecolor=RED, linewidth=1.4),
        fontweight='bold')

# Title
ax.set_title('SHM phase space: orbit in (position, velocity/$\\omega$) is a circle\n'
             'identical to imaginary-interest rotation',
             fontsize=14, pad=14, color=TEXT, fontweight='bold')

ax.set_xlim(-2.0, 2.0)
ax.set_ylim(-2.2, 2.0)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('iir_fig7_shm_phase_space.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig7_shm_phase_space.png")
