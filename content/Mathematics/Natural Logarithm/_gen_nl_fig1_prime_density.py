"""Generate nl_fig1_prime_density.png — the Prime Number Theorem.

Density of primes near N is about 1/ln(N). Plotted on a log-N axis, with the
measured trillion data point (37 primes in 1000 numbers => 1 in 27.0) marked
against the prediction 1/ln(10^12) = 1 in 27.6.
"""
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#1f4f8c'
ORANGE_F, ORANGE_E = '#e2924a', '#8c4f1f'
TEXT = '#333333'

fig, ax = plt.subplots(figsize=(9.2, 6.0))

N = np.logspace(1, 13, 500)
density = 1.0 / np.log(N)
ax.semilogx(N, density, color=BLUE, linewidth=2.6, zorder=3,
            label=r"prediction  $1/\ln(N)$")

# A couple of labelled points along the prediction curve.
for n, txt in [(1e2, "1 in 4.6"), (1e6, "1 in 13.8")]:
    d = 1.0 / np.log(n)
    ax.scatter([n], [d], s=45, color=BLUE, zorder=4)
    ax.annotate(txt, (n, d), textcoords="offset points", xytext=(8, 12),
                fontsize=10.5, color=BLUE)

# The measured trillion point: 37 primes in 1000 -> 0.037.
ax.scatter([1e12], [0.037], s=120, color=ORANGE_F, edgecolor=ORANGE_E,
           linewidth=1.6, zorder=5)
ax.annotate("measured near $10^{12}$:\n37 primes / 1000 = 1 in 27.0",
            (1e12, 0.037), textcoords="offset points", xytext=(-60, -62),
            ha='center', fontsize=10.5, color=ORANGE_E,
            arrowprops=dict(arrowstyle='->', color=ORANGE_E, lw=1.4))
# Prediction at trillion.
d12 = 1.0 / np.log(1e12)
ax.annotate(r"prediction $1/\ln(10^{12})$" "\n" "= 1 in 27.6", (1e12, d12),
            textcoords="offset points", xytext=(-70, 46), ha='center',
            fontsize=10.5, color=BLUE,
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.2))

ax.set_xlabel(r"$N$  (size of the numbers)", fontsize=12, color=TEXT)
ax.set_ylabel("proportion that are prime", fontsize=12, color=TEXT)
ax.set_title(r"Prime Number Theorem: density near $N \approx \dfrac{1}{\ln N}$",
             fontsize=14, color=TEXT, pad=12)
ax.grid(True, which='both', color='#e6e6e6', linewidth=0.7)
ax.legend(fontsize=11, loc='upper right')
ax.set_ylim(0, 0.45)

plt.tight_layout()
plt.savefig('nl_fig1_prime_density.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved nl_fig1_prime_density.png")
