"""Generate pi_fig5_convergence.png — log-scale plot of term sizes for the
binomial integral at x=1 vs x=1/2, showing the dramatic speed-up.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
TEXT = '#222'; MUTE = '#888'; GRID = '#e6e6e6'

# Term sizes for pi from integrated binomial series of (1 - x^2)^{1/2}
# After integration: x, (1/6)x^3, (1/40)x^5, (1/112)x^7, (5/1152)x^9, ...
# So term k has form c_k * x^(2k+1)
# Coefficients in the integrated series:
coeffs = [1.0, 1/6, 1/40, 1/112, 5/1152, 7/2816, 21/13312, 33/30720,
          429/557056, 715/1245184, 2431/5505024]  # rough
# Pre-compute term sizes for both x values
n_terms = len(coeffs)
ks = np.arange(n_terms)
powers = 2 * ks + 1
terms_x1 = np.array([abs(c) * (1.0 ** p) for c, p in zip(coeffs, powers)])
terms_xh = np.array([abs(c) * ((0.5) ** p) for c, p in zip(coeffs, powers)])

fig, ax = plt.subplots(figsize=(11, 6.5))
ax.grid(True, color=GRID, lw=0.6, which='both', zorder=0)
ax.set_yscale('log')

ax.plot(ks + 1, terms_x1, 'o-', color=ORANGE_EDGE, linewidth=2.4,
        markersize=9, label=r'$x = 1$ (integrate to full quarter circle)', zorder=4)
ax.plot(ks + 1, terms_xh, 's-', color=BLUE_EDGE, linewidth=2.4,
        markersize=9, label=r'$x = 1/2$ (integrate to half — Newton\'s trick)',
        zorder=4)

# Annotate the gap at term 10
gap_factor = terms_x1[-1] / terms_xh[-1]
ax.annotate(f'Term 11 is ~{gap_factor:.0e}× larger at $x=1$',
            xy=(11, terms_x1[-1]), xytext=(8, terms_x1[-1] * 100),
            fontsize=10, color=TEXT, ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=TEXT, lw=1.2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff8dc',
                      edgecolor='#aa8b3a', linewidth=1.2))

ax.set_xlabel('Term number', fontsize=12)
ax.set_ylabel('|term size| (log scale)', fontsize=12)
ax.set_title('Convergence speed-up: each term shrinks by an extra factor of $x^2$',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax.legend(loc='lower left', fontsize=11)
ax.set_xlim(0.5, 12)

plt.tight_layout()
plt.savefig('pi_fig5_convergence.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pi_fig5_convergence.png")
