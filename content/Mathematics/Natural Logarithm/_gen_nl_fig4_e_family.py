"""Generate nl_fig4_e_family.png — e^{rx} and A^x are the same family.

Left: e^{rx} for several rates r. Right: A^x for several bases A. Both sweep the
identical family of exponential curves through (0,1); a base swap A = e^r is just
a rate rescale.
"""
import matplotlib.pyplot as plt
import numpy as np

PALETTE = ['#4a90e2', '#7bb55c', '#e2924a', '#b76db4', '#c0392b']
TEXT = '#333333'

x = np.linspace(-1.2, 2.2, 300)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 5.6), sharey=True)

# Left: e^{rx}
rs = [0.3, 0.6, 1.0, 1.5]
for r, c in zip(rs, PALETTE):
    axL.plot(x, np.exp(r * x), color=c, linewidth=2.4,
             label=fr"$r={r}$")
axL.set_title(r"$e^{rx}$  (vary the rate $r$)", fontsize=14, color=TEXT)
axL.legend(fontsize=10, loc='upper left')

# Right: A^x
As = [1.4, 2.0, 3.0, 4.5]
for A, c in zip(As, PALETTE):
    axR.plot(x, A ** x, color=c, linewidth=2.4, label=fr"$A={A}$")
axR.set_title(r"$A^{x}$  (vary the base $A$)", fontsize=14, color=TEXT)
axR.legend(fontsize=10, loc='upper left')

for ax in (axL, axR):
    ax.axhline(0, color='#999999', lw=0.9)
    ax.axvline(0, color='#999999', lw=0.9)
    ax.scatter([0], [1], s=45, color='#333333', zorder=5)
    ax.annotate("(0, 1)", (0, 1), textcoords="offset points", xytext=(8, -14),
                fontsize=10, color=TEXT)
    ax.set_ylim(-0.4, 8)
    ax.grid(True, color='#ececec', linewidth=0.7)
    ax.set_xlabel("$x$", fontsize=12)

fig.suptitle(r"Same family of curves: choosing base $A$ $=$ choosing rate $r=\ln A$  (so $A^x = e^{(\ln A)x}$)",
             fontsize=13.5, color=TEXT, y=1.02)
plt.tight_layout()
plt.savefig('nl_fig4_e_family.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved nl_fig4_e_family.png")
