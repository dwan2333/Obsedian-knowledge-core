"""Generate pc4_fig1_exp_growth_decay.png — exponential growth vs decay parent curves.

Used by Section 4.1 (Exponential Functions) to anchor the visual difference
between b > 1 (growth) and 0 < b < 1 (decay).
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

x = np.linspace(-3, 3, 400)
growth = 2 ** x
decay = (0.5) ** x

ax.plot(x, growth, color='#2c6cb0', linewidth=3.0, label=r'$f(x)=2^x$ — growth ($b > 1$)')
ax.plot(x, decay, color='#b88455', linewidth=3.0, label=r'$g(x)=(1/2)^x$ — decay ($0 < b < 1$)')

# Mark the common point (0, 1)
ax.scatter([0], [1], s=120, color='#b13a2e', zorder=5, edgecolor='#8c1c14', linewidth=1.5)
ax.annotate('Both pass through $(0,\\,1)$', xy=(0, 1), xytext=(-2.5, 5.5),
            fontsize=12, color='#8c1c14',
            arrowprops=dict(arrowstyle='->', color='#8c1c14', lw=1.2))

# Horizontal asymptote
ax.axhline(0, color='#888888', linewidth=1, linestyle='--', alpha=0.7)
ax.text(2.8, 0.15, 'horizontal asymptote\n$y = 0$', fontsize=10, color='#666666',
        ha='right', style='italic')

ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$f(x)$', fontsize=14)
ax.set_title('Exponential growth vs decay — shared $y$-intercept $(0,\\,1)$',
             fontsize=14, pad=12)
ax.legend(loc='upper center', fontsize=12, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xlim(-3, 3)
ax.set_ylim(-0.5, 8)

plt.tight_layout()
plt.savefig('pc4_fig1_exp_growth_decay.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_fig1_exp_growth_decay.png')
