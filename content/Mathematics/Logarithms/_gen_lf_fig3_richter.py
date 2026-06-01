"""Generate lf_fig3_richter.png — Richter magnitude vs energy (log scale).

Shows that +1 on the Richter scale = x32 in energy. Plots energy on a log
y-axis with magnitude on x-axis. Annotates each integer magnitude with the
TNT equivalent and the x32 multiplicative jumps.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
RED = '#7a3030'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

# Richter scale anchor points (magnitude -> TNT equivalent in kg)
# Calibration: magnitude 2 = 1 metric ton = 1000 kg
# Each +1 step multiplies by 32
mags = np.arange(0, 10)
# Choose calibration so that magnitude 2 = 1000 kg TNT
# energy = C * 32^R; at R=2, energy = 1000 kg -> C * 32^2 = 1000 -> C = 1000/1024 ~ 0.977
C = 1000.0 / (32 ** 2)
energies = C * (32.0 ** mags)

# Named example events
events = {
    2: ("Small quarry blast", "1 ton TNT"),
    4: ("Felt locally", "1 kt TNT"),
    5: ("Damaging quake", "32 kt TNT"),
    6: ("Large city quake", "1 Mt TNT"),
    7: ("Major regional", "32 Mt TNT"),
    8: ("Great quake", "1 Gt TNT"),
    9: ("Mega-quake (2011 Tohoku)", "32 Gt TNT"),
}

fig, ax = plt.subplots(figsize=(12, 7))

# Bars showing the energy
bar_colors = [ORANGE if m in events else MUTE for m in mags]
bars = ax.bar(mags, energies, color=bar_colors, edgecolor=ORANGE_EDGE,
              linewidth=1.5, alpha=0.85, zorder=3, width=0.7)

# Log y-axis (exponential growth becomes linear visually)
ax.set_yscale('log')
ax.grid(True, color=GRID, linewidth=0.6, which='both', zorder=0)

# Annotate "x32" between consecutive bars
for m in range(1, 9):
    if m in events or (m - 1) in events:
        y_mid = math.sqrt(energies[m] * energies[m - 1])
        ax.annotate('', xy=(m, energies[m] * 0.85),
                    xytext=(m - 1, energies[m - 1] * 1.15),
                    arrowprops=dict(arrowstyle='->', color=GREEN_EDGE,
                                    lw=1.6, mutation_scale=12,
                                    connectionstyle='arc3,rad=-0.2'),
                    zorder=5)
        ax.text(m - 0.5, y_mid * 1.6, r'$\times 32$',
                fontsize=10, color=GREEN_EDGE, fontweight='bold',
                ha='center', va='bottom')

# Event labels on top of bars
for m, (name, tnt) in events.items():
    ax.text(m, energies[m] * 1.3, f'{name}\n({tnt})',
            fontsize=9, color=TEXT, ha='center', va='bottom',
            fontweight='bold')

# Highlight key insight at top
ax.text(4.5, 5e10,
        r'Each $+1$ on Richter scale $\;=\;\times 32$ in energy released',
        fontsize=14, color=RED, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#ffe8e8', edgecolor=RED, linewidth=1.6),
        fontweight='bold')

# Formula at bottom
ax.text(4.5, 0.02,
        r'$\mathrm{TNT}(R) = C \cdot 32^R \quad\Longleftrightarrow\quad'
        r'\log_{32}(\mathrm{TNT}) = S + R$',
        fontsize=12, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc', edgecolor='#aa8b3a', linewidth=1.4))

ax.set_xlabel('Richter magnitude $R$ (linear)', fontsize=12, color=TEXT)
ax.set_ylabel('Energy released (kg TNT equivalent, log scale)',
              fontsize=12, color=TEXT)
ax.set_title('Richter scale: additive on $R$, multiplicative on energy',
             fontsize=14, pad=12, color=TEXT, fontweight='bold')
ax.set_xticks(mags)
ax.set_xlim(-0.6, 9.6)
ax.set_ylim(0.01, 2e11)

plt.tight_layout()
plt.savefig('lf_fig3_richter.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig3_richter.png")
