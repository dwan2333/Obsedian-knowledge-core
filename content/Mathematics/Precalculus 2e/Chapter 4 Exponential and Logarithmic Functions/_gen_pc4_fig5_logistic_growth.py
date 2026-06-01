"""Generate pc4_fig5_logistic_growth.png — logistic growth S-curve with carrying capacity.

Used by Section 4.7 (Exponential and Logarithmic Models) to show how unlimited
exponential growth gets bent into a sigmoid when a carrying-capacity ceiling
is added — populations, infections, market saturation, etc.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

# Logistic: P(t) = K / (1 + A * e^{-r t})
K, r, A = 100, 0.6, 50
t = np.linspace(0, 18, 500)
P = K / (1 + A * np.exp(-r * t))

# For comparison, pure exponential up to where it would exceed K
exp_t = np.linspace(0, 7, 200)
exp_curve = 2 * np.exp(0.6 * exp_t)
exp_curve = np.where(exp_curve <= K * 1.4, exp_curve, np.nan)

ax.plot(t, P, color='#2c6cb0', linewidth=3.0,
        label='Logistic $P(t) = \\dfrac{K}{1 + A e^{-rt}}$')
ax.plot(exp_t, exp_curve, color='#b88455', linewidth=2.0, linestyle='--', alpha=0.7,
        label='Pure exponential (no ceiling)')

# Carrying capacity line
ax.axhline(K, color='#5e7c5e', linewidth=1.5, linestyle=':', alpha=0.85)
ax.text(17.5, K + 3, '$K$ — carrying capacity', fontsize=11, color='#3d5630',
        ha='right', style='italic')

# Inflection point at t = ln(A)/r where P = K/2
t_inf = np.log(A) / r
P_inf = K / 2
ax.scatter([t_inf], [P_inf], s=120, color='#b13a2e', zorder=5,
           edgecolor='#8c1c14', linewidth=1.5)
ax.annotate('inflection at $P = K/2$\n(growth fastest here)',
            xy=(t_inf, P_inf), xytext=(t_inf + 2, P_inf - 25),
            fontsize=11, color='#8c1c14',
            arrowprops=dict(arrowstyle='->', color='#8c1c14', lw=1.2))

ax.set_xlabel('time $t$', fontsize=14)
ax.set_ylabel('$P(t)$ — population', fontsize=14)
ax.set_title('Logistic growth — exponential bent by carrying capacity $K$',
             fontsize=14, pad=12)
ax.legend(loc='center right', fontsize=11, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xlim(0, 18)
ax.set_ylim(0, 140)

plt.tight_layout()
plt.savefig('pc4_fig5_logistic_growth.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_fig5_logistic_growth.png')
