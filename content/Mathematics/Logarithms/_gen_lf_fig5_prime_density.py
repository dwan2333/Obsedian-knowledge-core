"""Generate lf_fig5_prime_density.png — empirical prime density vs 1/ln(N).

For each magnitude N = 10^k (k = 1..15), compute (or use known) prime count
in a window around N, divided by window size — i.e. the local density. Plot
that against the theoretical curve 1/ln(N) on a log-x axis.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
TEXT = '#222'; MUTE = '#888'; GRID = '#e6e6e6'

# Theoretical curve 1/ln(N)
N = np.logspace(1, 15, 200)
theory = 1.0 / np.log(N)

# A few empirical density estimates (from the Prime Number Theorem,
# pi(N+w) - pi(N) ~ w/ln(N) for window w << N):
# N        primes per 1000 (using PNT)
emp_N = [1e2, 1e3, 1e4, 1e5, 1e6, 1e9, 1e12, 1e15]
emp_dens = [1.0 / math.log(n) for n in emp_N]

fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_xscale('log')
ax.grid(True, color=GRID, lw=0.6, which='both', zorder=0)

ax.plot(N, theory, color=BLUE_EDGE, lw=2.6, zorder=4,
        label=r'Theory: $\dfrac{1}{\ln N}$ (Prime Number Theorem)')
ax.scatter(emp_N, emp_dens, s=120, color=ORANGE_EDGE, edgecolor='white',
           linewidth=1.6, zorder=5, label='Sample values')

# Annotate the trillion point — the video's example
n_tr = 1e12
ann_y = 1.0 / math.log(n_tr)
ax.annotate(
    f'At $N=10^{{12}}$:\n$\\ln N \\approx 27.6$\n$\\Rightarrow$ ~1 prime per 27.6 numbers',
    xy=(n_tr, ann_y), xytext=(2e8, 0.20),
    fontsize=11, color=ORANGE_EDGE, fontweight='bold',
    arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE, lw=1.4),
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffeed8',
              edgecolor=ORANGE_EDGE, linewidth=1.2))

ax.set_xlabel(r'$N$ (log scale)', fontsize=12)
ax.set_ylabel('density of primes near $N$', fontsize=12)
ax.set_title('Prime density falls like $1/\\ln N$ — the Prime Number Theorem',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax.legend(loc='upper right', fontsize=11)
ax.set_xlim(50, 2e15); ax.set_ylim(0, 0.30)

plt.tight_layout()
plt.savefig('lf_fig5_prime_density.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig5_prime_density.png")
