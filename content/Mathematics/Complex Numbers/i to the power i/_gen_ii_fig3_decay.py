"""ii_fig3_decay.png — raising to the power i turns the circular parametrisation
e^{it} into the real decay e^{-t}; the SAME pi/2 of 'time' lands on e^{-pi/2}."""
import matplotlib.pyplot as plt
import numpy as np

BLUE, GREEN, RED = '#1f4f8c', '#3d7530', '#a83227'
fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 6.2))

# ---- LEFT: walk pi/2 around the circle, reach i ----
tt = np.linspace(0, 2 * np.pi, 400)
axL.plot(np.cos(tt), np.sin(tt), color='#cccccc', lw=1.6)
arc = np.linspace(0, np.pi / 2, 120)
axL.plot(np.cos(arc), np.sin(arc), color=BLUE, lw=4, solid_capstyle='round')
axL.annotate('', xy=(np.cos(np.pi/2-0.04), np.sin(np.pi/2-0.04)),
             xytext=(np.cos(np.pi/2-0.18), np.sin(np.pi/2-0.18)),
             arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=3))
axL.scatter([1, 0], [0, 1], s=90, color=['#888', '#cc4444'], zorder=5,
            edgecolor='white')
axL.text(1.04, -0.16, r'$1$', fontsize=13)
axL.text(0.06, 1.05, r'$i$', fontsize=15, color='#cc4444', fontweight='bold')
axL.text(0.40, 0.66, r'$\frac{\pi}{2}$', fontsize=16, color=BLUE)
axL.set_title(r"$e^{it}$ : walk $\frac{\pi}{2}$ of time $\to$ reach $i$",
              fontsize=13, fontweight='bold')
axL.set_xlim(-1.3, 1.4); axL.set_ylim(-1.3, 1.4)
axL.set_aspect('equal'); axL.axis('off')

# ---- RIGHT: decay curve e^{-t}, mark t = pi/2 ----
t = np.linspace(0, 2.6, 400)
axR.plot(t, np.exp(-t), color=RED, lw=3, label=r'$e^{-t}$')
v = np.exp(-np.pi / 2)
axR.plot([np.pi/2, np.pi/2], [0, v], color=BLUE, ls='--', lw=1.6)
axR.plot([0, np.pi/2], [v, v], color=BLUE, ls='--', lw=1.6)
axR.scatter([0, np.pi/2], [1, v], s=80, color=[GREEN, '#cc4444'], zorder=5,
            edgecolor='white')
axR.annotate(r'$e^{-\pi/2}\approx 0.2079$', xy=(np.pi/2, v), xytext=(1.75, 0.46),
             fontsize=13, color='#cc4444', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#cc4444', lw=1.6))
axR.text(0.05, 1.02, r'start at $1$', fontsize=11.5, color=GREEN)
axR.text(np.pi/2 - 0.06, -0.085, r'$\frac{\pi}{2}$', fontsize=15, color=BLUE, ha='center')
axR.set_title(r"$\left(e^{it}\right)^{i}=e^{-t}$ : the same $\frac{\pi}{2}$ of time $\to$ $0.2079$",
              fontsize=13, fontweight='bold')
axR.set_xlabel('time $t$', fontsize=12); axR.set_ylabel('value', fontsize=12)
axR.set_xlim(0, 2.6); axR.set_ylim(0, 1.08)
axR.spines[['top', 'right']].set_visible(False)
axR.grid(color='#eee', lw=0.8); axR.set_axisbelow(True)
axR.legend(loc='upper right', fontsize=12)

fig.suptitle(r"Raising to the power $i$ rotates the dynamics: circular motion $\to$ exponential decay",
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('ii_fig3_decay.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ii_fig3_decay.png")
