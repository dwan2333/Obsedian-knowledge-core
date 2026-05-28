"""Generate iir_fig4_spiral_to_circle.png — discrete spiral vs continuous limit.

Three panels showing the path of (1 + i*delta_t)^n starting at 1, with
n*delta_t = pi (one half-rotation worth of time). As delta_t -> 0, the
jagged outward spiral collapses onto a perfect unit semicircle from 1 to -1.

Panels:
- delta_t = pi/4 (4 big steps) -> big outward spiral
- delta_t = pi/20 (20 medium steps) -> gentler spiral
- delta_t -> 0 (continuous) -> unit semicircle (exact)
"""
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
TEXT = '#222222'
MUTE = '#888888'

fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

# Choose total time T = pi (one half-rotation in the continuous limit)
T = math.pi
configs = [
    (4, ORANGE_EDGE, r'$\Delta t = \pi/4$, 4 steps'),
    (20, BLUE_EDGE, r'$\Delta t = \pi/20$, 20 steps'),
    (None, GREEN_EDGE, r'$\Delta t \to 0$ (continuous)'),
]

for ax, (n, color, label) in zip(axes, configs):
    # Background axes
    ax.axhline(0, color=MUTE, linewidth=0.8, zorder=1)
    ax.axvline(0, color=MUTE, linewidth=0.8, zorder=1)

    # Reference unit circle (faint dashed)
    ref = mpatches.Circle((0, 0), 1.0, fill=False, edgecolor=MUTE,
                          linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)
    ax.add_patch(ref)

    # Tick labels on axes
    for x, lbl in [(1, '1'), (-1, '-1')]:
        ax.plot([x, x], [-0.04, 0.04], color=MUTE, linewidth=1.0, zorder=2)
        ax.text(x, -0.17, lbl, fontsize=10, color=MUTE,
                ha='center', va='top')
    ax.text(0.06, 1.02, 'i', fontsize=10, color=MUTE,
            ha='left', va='bottom')

    if n is None:
        # Continuous: trace the unit semicircle from 1 to -1
        theta = np.linspace(0, math.pi, 200)
        xs = np.cos(theta)
        ys = np.sin(theta)
        ax.plot(xs, ys, color=color, linewidth=3.0, zorder=4)
        ax.scatter([1], [0], s=70, color='gold',
                   edgecolor='#aa8b3a', linewidth=1.2, zorder=5)
        ax.scatter([-1], [0], s=70, color='#d97777',
                   edgecolor='#7a3030', linewidth=1.2, zorder=5)
        # Show waypoint i
        ax.scatter([0], [1], s=70, color='#88aadd',
                   edgecolor=BLUE_EDGE, linewidth=1.2, zorder=5)
        ax.text(0.08, 1.05, r'$e^{i\pi/2}=i$', fontsize=10, color=BLUE_EDGE,
                ha='left', va='bottom', fontweight='bold')
        ax.text(-1.05, -0.12, r'$e^{i\pi}=-1$', fontsize=10, color='#7a3030',
                ha='right', va='top', fontweight='bold')
        ax.text(1.05, -0.12, r'$e^{0}=1$', fontsize=10, color='#aa8b3a',
                ha='left', va='top', fontweight='bold')
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-1.8, 1.8)
    else:
        # Discrete: walk (1 + i*delta_t)^k for k=0..n
        dt = T / n
        factor = 1 + 1j * dt
        points = [factor ** k for k in range(n + 1)]
        xs = [p.real for p in points]
        ys = [p.imag for p in points]

        # Draw arrows between consecutive points
        for k in range(n):
            p0, p1 = points[k], points[k + 1]
            ax.annotate('', xy=(p1.real, p1.imag),
                        xytext=(p0.real, p0.imag),
                        arrowprops=dict(arrowstyle='->', color=color,
                                        lw=1.6, alpha=0.92,
                                        mutation_scale=10),
                        zorder=3)
        # Dots at each point
        ax.scatter(xs, ys, s=24, color=color, edgecolor='white',
                   linewidth=0.6, zorder=4)
        ax.scatter([xs[0]], [ys[0]], s=80, color='gold',
                   edgecolor='#aa8b3a', linewidth=1.2, zorder=5)
        # Endpoint label
        final = points[-1]
        ax.scatter([final.real], [final.imag], s=80, color='#d97777',
                   edgecolor='#7a3030', linewidth=1.2, zorder=5)
        ax.text(final.real + 0.15, final.imag + 0.15,
                f'end:\n{final.real:+.2f}{final.imag:+.2f}i',
                fontsize=9.5, color='#7a3030', fontweight='bold',
                ha='left', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2',
                          facecolor='white', edgecolor='#7a3030',
                          linewidth=0.8))
        # Auto-fit
        max_r = max(abs(p) for p in points) * 1.25
        ax.set_xlim(-max_r, max_r)
        ax.set_ylim(-max_r, max_r)

    ax.set_aspect('equal')
    ax.set_title(label, fontsize=12, pad=8, color=color, fontweight='bold')
    ax.axis('off')

fig.suptitle('As $\\Delta t \\to 0$, the outward spiral collapses onto the unit circle',
             fontsize=14, y=1.00, color=TEXT, fontweight='bold')

plt.tight_layout()
plt.savefig('iir_fig4_spiral_to_circle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig4_spiral_to_circle.png")
