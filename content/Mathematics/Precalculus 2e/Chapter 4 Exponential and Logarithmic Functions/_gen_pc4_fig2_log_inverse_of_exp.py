"""Generate pc4_fig2_log_inverse_of_exp.png — the log curve as mirror of exp over y = x.

Used by Section 4.3 (Logarithmic Functions) to anchor the core idea that
log_b is the inverse of b^x, which means their graphs are reflections of each
other across the diagonal y = x.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.5, 7))

# Exponential 2^x for x in [-2, 3]
x_exp = np.linspace(-2, 3, 400)
y_exp = 2 ** x_exp
ax.plot(x_exp, y_exp, color='#2c6cb0', linewidth=3.0, label=r'$f(x)=2^x$ (exponential)')

# Logarithm log_2(x) for x in (0.1, 8] — the inverse
x_log = np.linspace(0.1, 8, 400)
y_log = np.log2(x_log)
ax.plot(x_log, y_log, color='#b88455', linewidth=3.0, label=r'$g(x)=\log_2 x$ (logarithm)')

# Mirror line y = x
diag = np.linspace(-3, 8, 200)
ax.plot(diag, diag, color='#888888', linewidth=1.5, linestyle='--', alpha=0.7,
        label=r'$y = x$ (mirror axis)')

# Mark a corresponding pair: (1, 2) on exp, (2, 1) on log
ax.scatter([1, 2], [2, 1], s=110, color='#b13a2e', zorder=5,
           edgecolor='#8c1c14', linewidth=1.5)
ax.plot([1, 2], [2, 1], color='#b13a2e', linewidth=1, alpha=0.5)
ax.text(0.4, 2.3, '$(1,\\,2)$ on $2^x$', fontsize=11, color='#8c1c14')
ax.text(2.2, 0.8, '$(2,\\,1)$ on $\\log_2 x$', fontsize=11, color='#8c1c14')

ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$y$', fontsize=14)
ax.set_title('Logarithm = reflection of exponential across $y = x$',
             fontsize=14, pad=12)
ax.legend(loc='upper left', fontsize=11, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_aspect('equal')
ax.set_xlim(-3, 8)
ax.set_ylim(-3, 8)
ax.axhline(0, color='#999999', linewidth=0.7)
ax.axvline(0, color='#999999', linewidth=0.7)

plt.tight_layout()
plt.savefig('pc4_fig2_log_inverse_of_exp.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_fig2_log_inverse_of_exp.png')
