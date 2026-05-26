"""Generate efc_fig3_maclaurin.png — Maclaurin series approximations of cos and sin.

Two side-by-side panels:
  Left  — cos(theta) and partial sums of degree 2, 4, 6, 8.
  Right — sin(theta) and partial sums of degree 1, 3, 5, 7.
Show how higher-degree polynomials hug the true curve over a wider range.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#1f4f8c'
ORANGE = '#8c4f1f'
GREEN = '#3d7530'
PURPLE = '#6e3a6c'
YELLOW = '#8c6520'
TEXT = '#222222'

fig, (ax_c, ax_s) = plt.subplots(1, 2, figsize=(14, 6))

thetas = np.linspace(-2 * math.pi, 2 * math.pi, 800)

# True cos and sin.
true_cos = np.cos(thetas)
true_sin = np.sin(thetas)

# Partial sums.
def cos_partial(theta, n_terms):
    """Sum the first n_terms of the Maclaurin series for cos(theta)."""
    out = np.zeros_like(theta)
    for k in range(n_terms):
        out = out + ((-1) ** k) * theta ** (2 * k) / math.factorial(2 * k)
    return out

def sin_partial(theta, n_terms):
    out = np.zeros_like(theta)
    for k in range(n_terms):
        out = out + ((-1) ** k) * theta ** (2 * k + 1) / math.factorial(2 * k + 1)
    return out

# Cos panel.
ax_c.axhline(0, color='#cccccc', linewidth=0.8)
ax_c.axvline(0, color='#cccccc', linewidth=0.8)
ax_c.plot(thetas, true_cos, color=BLUE, linewidth=3.0,
          label=r"$\cos\theta$ (true)", zorder=5)
ax_c.plot(thetas, cos_partial(thetas, 2), color=ORANGE, linewidth=1.6,
          linestyle='--',
          label=r"$1 - \theta^2/2!$  (degree 2)")
ax_c.plot(thetas, cos_partial(thetas, 3), color=GREEN, linewidth=1.6,
          linestyle='--',
          label=r"$+\,\theta^4/4!$  (degree 4)")
ax_c.plot(thetas, cos_partial(thetas, 4), color=PURPLE, linewidth=1.6,
          linestyle='--',
          label=r"$-\,\theta^6/6!$  (degree 6)")
ax_c.plot(thetas, cos_partial(thetas, 5), color=YELLOW, linewidth=1.6,
          linestyle='--',
          label=r"$+\,\theta^8/8!$  (degree 8)")
ax_c.set_xlim(-2 * math.pi, 2 * math.pi)
ax_c.set_ylim(-2.0, 2.0)
ax_c.set_xticks([-2 * math.pi, -math.pi, 0, math.pi, 2 * math.pi])
ax_c.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
ax_c.set_title(r"$\cos\theta$ as a Maclaurin polynomial — even powers only",
               fontsize=12, color=TEXT, fontweight='bold')
ax_c.legend(loc='lower center', fontsize=9, framealpha=0.92)
ax_c.grid(alpha=0.3)

# Sin panel.
ax_s.axhline(0, color='#cccccc', linewidth=0.8)
ax_s.axvline(0, color='#cccccc', linewidth=0.8)
ax_s.plot(thetas, true_sin, color=BLUE, linewidth=3.0,
          label=r"$\sin\theta$ (true)", zorder=5)
ax_s.plot(thetas, sin_partial(thetas, 1), color=ORANGE, linewidth=1.6,
          linestyle='--',
          label=r"$\theta$  (degree 1)")
ax_s.plot(thetas, sin_partial(thetas, 2), color=GREEN, linewidth=1.6,
          linestyle='--',
          label=r"$-\,\theta^3/3!$  (degree 3)")
ax_s.plot(thetas, sin_partial(thetas, 3), color=PURPLE, linewidth=1.6,
          linestyle='--',
          label=r"$+\,\theta^5/5!$  (degree 5)")
ax_s.plot(thetas, sin_partial(thetas, 4), color=YELLOW, linewidth=1.6,
          linestyle='--',
          label=r"$-\,\theta^7/7!$  (degree 7)")
ax_s.set_xlim(-2 * math.pi, 2 * math.pi)
ax_s.set_ylim(-2.0, 2.0)
ax_s.set_xticks([-2 * math.pi, -math.pi, 0, math.pi, 2 * math.pi])
ax_s.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
ax_s.set_title(r"$\sin\theta$ as a Maclaurin polynomial — odd powers only",
               fontsize=12, color=TEXT, fontweight='bold')
ax_s.legend(loc='lower center', fontsize=9, framealpha=0.92)
ax_s.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('efc_fig3_maclaurin.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved efc_fig3_maclaurin.png")
