"""Generate pc4_fig3_log_bases.png — log curves for several bases on shared axes.

Used by Section 4.4 (Graphs of Logarithmic Functions) to show that base
controls the steepness but the shape is universal: all pass through (1, 0).
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

x = np.linspace(0.05, 10, 500)
ax.plot(x, np.log2(x),  color='#2c6cb0', linewidth=2.8, label=r'$\log_2 x$')
ax.plot(x, np.log(x),   color='#b88455', linewidth=2.8, label=r'$\ln x = \log_e x$')
ax.plot(x, np.log10(x), color='#5e7c5e', linewidth=2.8, label=r'$\log_{10} x$')

# Mark the universal anchor point (1, 0)
ax.scatter([1], [0], s=120, color='#b13a2e', zorder=5, edgecolor='#8c1c14', linewidth=1.5)
ax.annotate('All bases share $(1,\\,0)$', xy=(1, 0), xytext=(3.5, -2.2),
            fontsize=12, color='#8c1c14',
            arrowprops=dict(arrowstyle='->', color='#8c1c14', lw=1.2))

# Vertical asymptote at x = 0
ax.axvline(0, color='#888888', linewidth=1, linestyle='--', alpha=0.7)
ax.text(0.2, -3.3, 'asymptote $x = 0$', fontsize=10, color='#666666',
        style='italic', rotation=90)

ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$\\log_b x$', fontsize=14)
ax.set_title('Logarithms in different bases — same shape, different steepness',
             fontsize=14, pad=12)
ax.legend(loc='lower right', fontsize=12, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.axhline(0, color='#999999', linewidth=0.7)
ax.set_xlim(0, 10)
ax.set_ylim(-4, 4)

plt.tight_layout()
plt.savefig('pc4_fig3_log_bases.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_fig3_log_bases.png')
