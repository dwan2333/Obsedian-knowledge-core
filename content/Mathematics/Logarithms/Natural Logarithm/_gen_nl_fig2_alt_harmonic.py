"""Generate nl_fig2_alt_harmonic.png — alternating harmonic series -> ln 2.

Partial sums of 1 - 1/2 + 1/3 - 1/4 + ... plotted against the number of terms.
They oscillate with shrinking amplitude and zero in on ln(2) ~= 0.693.
"""
import matplotlib.pyplot as plt
from math import log

BLUE = '#1f4f8c'
GREEN = '#3d7530'      # forward (+) steps
RED = '#a83227'        # backward (-) steps
TEXT = '#333333'

terms = [1, -1/2, 1/3, -1/4, 1/5, -1/6, 1/7, -1/8, 1/9, -1/10]
labels = [r"$+1$", r"$-\frac{1}{2}$", r"$+\frac{1}{3}$", r"$-\frac{1}{4}$",
          r"$+\frac{1}{5}$", r"$-\frac{1}{6}$", r"$+\frac{1}{7}$",
          r"$-\frac{1}{8}$", r"$+\frac{1}{9}$", r"$-\frac{1}{10}$"]
S, acc = [], 0.0
for t in terms:
    acc += t
    S.append(acc)
n = list(range(1, len(S) + 1))
ln2 = log(2)

fig, ax = plt.subplots(figsize=(10.5, 6.2))

# Target line.
ax.axhline(ln2, color=BLUE, lw=1.8, ls='--', zorder=2)
ax.text(len(S) + 0.15, ln2, r"$\ln 2 \approx 0.693$", color=BLUE, va='center',
        ha='left', fontsize=13, fontweight='bold')

# Zigzag of partial sums.
ax.plot(n, S, color='#999999', lw=1.6, zorder=2)
for i, (xi, yi) in enumerate(zip(n, S)):
    c = GREEN if terms[i] > 0 else RED
    ax.scatter([xi], [yi], s=70, color=c, zorder=4)
    off = 15 if terms[i] > 0 else -24
    ax.annotate(labels[i], (xi, yi), textcoords="offset points",
                xytext=(0, off), ha='center', fontsize=12, color=c)

ax.set_xlabel("number of terms added", fontsize=12, color=TEXT)
ax.set_ylabel("partial sum", fontsize=12, color=TEXT)
ax.set_title(r"$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \cdots = \ln 2$",
             fontsize=15, color=TEXT, pad=12)
ax.set_xlim(0.4, len(S) + 1.9)
ax.set_ylim(0.40, 1.10)
ax.grid(True, color='#ececec', linewidth=0.7)
ax.set_xticks(n)

plt.tight_layout()
plt.savefig('nl_fig2_alt_harmonic.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved nl_fig2_alt_harmonic.png")
