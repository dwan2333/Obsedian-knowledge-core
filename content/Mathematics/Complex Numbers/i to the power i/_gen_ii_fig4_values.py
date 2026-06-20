"""ii_fig4_values.png — e^x = i has infinitely many solutions (wind around the
circle any whole number of extra times), so i^i has infinitely many real values
e^{-pi/2 - 2*pi*k}."""
import matplotlib.pyplot as plt
import numpy as np

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.8, 6.4),
                               gridspec_kw={'width_ratios': [1, 1.12]})
C0, C1, C2 = '#3d7530', '#1f4f8c', '#b76db4'   # k=-1, k=0, k=+1

# ---- LEFT: three windings that all land on i ----
tt = np.linspace(0, 2 * np.pi, 400)
axL.plot(np.cos(tt), np.sin(tt), color='#dddddd', lw=1.4)
# k=0: +pi/2 (quarter, CCW) radius 1.0
a = np.linspace(0, np.pi/2, 100); r = 1.0
axL.plot(r*np.cos(a), r*np.sin(a), color=C1, lw=3.4, solid_capstyle='round')
# k=+1: +5pi/2 (one loop + quarter), spiral out 1.02->1.22
a = np.linspace(0, 5*np.pi/2, 400); r = np.linspace(1.04, 1.24, a.size)
axL.plot(r*np.cos(a), r*np.sin(a), color=C2, lw=2.2, alpha=0.9)
# k=-1: -3pi/2 (three-quarter, CW), radius 0.84
a = np.linspace(0, -3*np.pi/2, 300); r = 0.84
axL.plot(r*np.cos(a), r*np.sin(a), color=C0, lw=2.2, alpha=0.9)
axL.scatter([0], [1], s=240, marker='*', color='#cc4444', edgecolor='white',
            zorder=6)
axL.text(0.08, 1.12, r'$i$', fontsize=16, color='#cc4444', fontweight='bold')
axL.scatter([1], [0], s=60, color='#888', zorder=6, edgecolor='white')
axL.text(1.06, -0.2, r'$1$', fontsize=12)
# legend-ish labels
axL.text(-1.95, -1.45, r'$+\frac{\pi}{2}$', color=C1, fontsize=14, fontweight='bold')
axL.text(-1.25, -1.45, r'$+\frac{5\pi}{2}$ (extra loop)', color=C2, fontsize=12.5, fontweight='bold')
axL.text(0.75, -1.45, r'$-\frac{3\pi}{2}$ (backwards)', color=C0, fontsize=12.5, fontweight='bold')
axL.set_title(r"$e^{x}=i$ has infinitely many solutions $x=i\left(\frac{\pi}{2}+2\pi k\right)$",
              fontsize=12.5, fontweight='bold')
axL.set_xlim(-2.0, 2.0); axL.set_ylim(-1.7, 1.7)
axL.set_aspect('equal'); axL.axis('off')

# ---- RIGHT: resulting values on a log axis ----
vals = [(-1, np.exp(3*np.pi/2), C0, r'$k=-1$' + '\n' + r'$e^{3\pi/2}\approx 111.3$'),
        (0,  np.exp(-np.pi/2),  C1, r'$k=0$' + '\n' + r'$e^{-\pi/2}\approx 0.2079$'),
        (1,  np.exp(-5*np.pi/2),C2, r'$k=1$' + '\n' + r'$e^{-5\pi/2}\approx 0.000388$')]
for k, val, c, lab in vals:
    axR.scatter([val], [0], s=150, color=c, edgecolor='white', zorder=5)
    dy = 0.12 if k != 0 else -0.18
    axR.annotate(lab, xy=(val, 0), xytext=(val, dy), fontsize=11.5, color=c,
                 ha='center', va='bottom' if dy > 0 else 'top', fontweight='bold')
axR.axhline(0, color='#888', lw=1.4, zorder=1)
axR.set_xscale('log')
axR.set_xlim(1e-4, 1e3); axR.set_ylim(-0.4, 0.4)
axR.set_yticks([])
axR.set_xlabel(r'value of $i^{\,i}=e^{-\pi/2-2\pi k}$  (log scale)', fontsize=12)
axR.spines[['top', 'right', 'left']].set_visible(False)
axR.set_title(r"...so $i^{\,i}$ takes infinitely many real values",
              fontsize=12.5, fontweight='bold')
axR.grid(axis='x', color='#eee', lw=0.8); axR.set_axisbelow(True)

plt.tight_layout()
plt.savefig('ii_fig4_values.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ii_fig4_values.png")
