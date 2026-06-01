"""Generate pc4_fig4_half_life_decay.png — half-life decay curve with marked halvings.

Used by Section 4.7 (Exponential and Logarithmic Models) to show how a
radioactive (or analogously decaying) quantity halves on a fixed schedule.
Uses a generic substance with half-life T = 5 (some time unit).
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

T_HALF = 5.0
t = np.linspace(0, 30, 600)
N0 = 100
# N(t) = N0 * (1/2)^(t/T_half)
N = N0 * (0.5) ** (t / T_HALF)

ax.plot(t, N, color='#2c6cb0', linewidth=3.0, label='$N(t) = N_0 \\cdot (1/2)^{t/T_{1/2}}$')

# Mark each half-life
for k in range(1, 7):
    t_k = k * T_HALF
    N_k = N0 * (0.5) ** k
    ax.scatter([t_k], [N_k], s=80, color='#b13a2e', zorder=5,
               edgecolor='#8c1c14', linewidth=1.3)
    ax.plot([t_k, t_k], [0, N_k], color='#b13a2e', linewidth=0.7,
            linestyle=':', alpha=0.6)
    ax.text(t_k, N_k + 4, f'$N_0/{2**k}$', fontsize=10, ha='center', color='#8c1c14')

# Horizontal lines marking the halving levels
for k in range(1, 5):
    level = N0 * (0.5) ** k
    ax.axhline(level, color='#888888', linewidth=0.6, linestyle=':', alpha=0.4)

ax.text(28, 4, 'asymptote $N = 0$', fontsize=10, color='#666666',
        style='italic', ha='right')

ax.set_xlabel('time $t$', fontsize=14)
ax.set_ylabel('$N(t)$ — quantity remaining', fontsize=14)
ax.set_title('Radioactive (half-life) decay with $T_{1/2} = 5$',
             fontsize=14, pad=12)
ax.legend(loc='upper right', fontsize=12, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xlim(0, 30)
ax.set_ylim(0, 110)

plt.tight_layout()
plt.savefig('pc4_fig4_half_life_decay.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_fig4_half_life_decay.png')
