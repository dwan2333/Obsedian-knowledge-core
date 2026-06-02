"""Generate ch4_fig5_decay_models.png — half-life decay curve.

Shows N(t) = N0 * e^(-k t) with three half-life markers (after 1, 2, 3
half-lives the quantity is at 1/2, 1/4, 1/8 of N0). Concrete example:
carbon-14 with half-life ~5730 years.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'
ORANGE_EDGE = '#8c4f1f'
GREEN_EDGE = '#3d7530'
RED = '#7a3030'
TEXT = '#222'
MUTE = '#888'
GRID = '#e6e6e6'

# Carbon-14: half-life T = 5730 years -> k = ln(2) / 5730
T_half = 5730
k = math.log(2) / T_half
N0 = 100  # percent of original amount

t = np.linspace(0, 4 * T_half, 600)
N = N0 * np.exp(-k * t)

fig, ax = plt.subplots(figsize=(12, 7))

ax.grid(True, color=GRID, lw=0.6, zorder=0)
ax.axhline(0, color=MUTE, lw=0.9, zorder=1)
ax.axvline(0, color=MUTE, lw=0.9, zorder=1)

# Main curve
ax.plot(t, N, color=BLUE_EDGE, linewidth=3.0, zorder=4,
        label=r'$N(t) = N_0\, e^{-kt}$ with $k = \ln(2)/T_{1/2}$')

# Half-life markers
for n_half in [1, 2, 3]:
    t_mark = n_half * T_half
    n_mark = N0 / (2 ** n_half)
    # Vertical dashed line
    ax.plot([t_mark, t_mark], [0, n_mark], color=ORANGE_EDGE,
            lw=1.4, linestyle='--', alpha=0.7, zorder=3)
    # Horizontal dashed line
    ax.plot([0, t_mark], [n_mark, n_mark], color=ORANGE_EDGE,
            lw=1.4, linestyle='--', alpha=0.7, zorder=3)
    # Dot at the curve
    ax.scatter([t_mark], [n_mark], s=120, color=ORANGE_EDGE,
               edgecolor='white', linewidth=1.6, zorder=6)
    # Label
    ax.annotate(f'$N_0/{2**n_half}$ after\n{n_half} half-life{"s" if n_half > 1 else ""}',
                xy=(t_mark, n_mark),
                xytext=(t_mark + 600, n_mark + 6),
                fontsize=10.5, color=ORANGE_EDGE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=1.0))

# Starting point
ax.scatter([0], [N0], s=160, color=GREEN_EDGE, edgecolor='white',
           linewidth=1.8, zorder=7, marker='*')
ax.text(-700, N0 + 3, r'$N_0$ (initial)', fontsize=11.5,
        color=GREEN_EDGE, fontweight='bold', va='center', ha='right')

# Horizontal asymptote
ax.text(4 * T_half * 0.95, 4, r'$N \to 0$ as $t \to \infty$',
        fontsize=10, color=MUTE, style='italic', ha='right')

# x-axis half-life ticks
ax.set_xticks([0, T_half, 2*T_half, 3*T_half, 4*T_half])
ax.set_xticklabels([f'0', f'$T_{{1/2}}$', f'$2\\,T_{{1/2}}$',
                    f'$3\\,T_{{1/2}}$', f'$4\\,T_{{1/2}}$'])

ax.set_xlabel('Time $t$', fontsize=12)
ax.set_ylabel('Amount remaining $N(t)$ (% of $N_0$)', fontsize=12)
ax.set_title('Exponential decay (half-life model): every $T_{1/2}$, amount drops by half',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax.legend(loc='upper right', fontsize=11)
ax.set_xlim(-1500, 4.2 * T_half)
ax.set_ylim(-8, 110)

# Carbon-14 callout
ax.text(2 * T_half, 80,
        r'Example: $\text{C}^{14}$ has $T_{1/2} \approx 5730$ yr.' '\n'
        r'After $11{,}460$ yr ($2 T_{1/2}$), $25\%$ remains.',
        fontsize=11, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

plt.tight_layout()
plt.savefig('ch4_fig5_decay_models.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ch4_fig5_decay_models.png")
