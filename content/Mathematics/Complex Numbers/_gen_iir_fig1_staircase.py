"""Generate iir_fig1_staircase.png — compounding staircase: $100 at 12% annual.

Shows the step function: balance jumps at year-ends. Compares n=1 (annual)
vs n=12 (monthly) vs continuous $100 e^{0.12 t}$ to motivate why compounding
frequency matters and where e comes from.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

P, r, T = 100.0, 0.12, 10.0

# Annual compounding step function (n=1)
years = np.arange(0, int(T) + 1)
balances_annual = P * (1 + r) ** years

# Monthly compounding step function (n=12)
months = np.arange(0, int(T) * 12 + 1)
balances_monthly = P * (1 + r / 12) ** months
t_monthly = months / 12.0

# Continuous compounding curve
t_cont = np.linspace(0, T, 400)
balances_cont = P * np.exp(r * t_cont)

fig, ax = plt.subplots(figsize=(11, 6.5))

# Grid + axes
ax.grid(True, color=GRID, linewidth=0.7, zorder=0)
ax.axhline(P, color=MUTE, linewidth=0.8, linestyle='--', zorder=1)

# Annual step (drawn as actual horizontal segments with vertical jumps)
for i in range(len(years) - 1):
    ax.plot([years[i], years[i + 1]], [balances_annual[i], balances_annual[i]],
            color=ORANGE_EDGE, linewidth=2.4, solid_capstyle='butt', zorder=4)
    ax.plot([years[i + 1], years[i + 1]],
            [balances_annual[i], balances_annual[i + 1]],
            color=ORANGE_EDGE, linewidth=2.4, zorder=4)
ax.scatter(years, balances_annual, s=42, color=ORANGE,
           edgecolor=ORANGE_EDGE, linewidth=1.4, zorder=5,
           label=r'$n=1$: annual, $100(1.12)^t$')

# Monthly step (lighter, more steps so just draw as line)
ax.step(t_monthly, balances_monthly, where='post',
        color=BLUE_EDGE, linewidth=1.6, alpha=0.85, zorder=3,
        label=r'$n=12$: monthly, $100(1.01)^{12t}$')

# Continuous curve
ax.plot(t_cont, balances_cont, color=GREEN_EDGE, linewidth=2.6,
        linestyle='--', zorder=2,
        label=r'$n \to \infty$: continuous, $100\, e^{0.12 t}$')

# Annotate end-point values at T=10
ax.annotate(f'\\${balances_annual[-1]:.2f}', xy=(10, balances_annual[-1]),
            xytext=(10.15, balances_annual[-1] - 6),
            fontsize=11, color=ORANGE_EDGE, fontweight='bold', va='center')
ax.annotate(f'\\${balances_monthly[-1]:.2f}', xy=(10, balances_monthly[-1]),
            xytext=(10.15, balances_monthly[-1] + 5),
            fontsize=11, color=BLUE_EDGE, fontweight='bold', va='center')
ax.annotate(f'\\${balances_cont[-1]:.2f}', xy=(10, balances_cont[-1]),
            xytext=(10.15, balances_cont[-1] + 16),
            fontsize=11, color=GREEN_EDGE, fontweight='bold', va='center')

# Mark $100 starting point
ax.scatter([0], [P], s=70, color='#ffffff', edgecolor=TEXT,
           linewidth=1.8, zorder=6)
ax.text(-0.25, P, r'\$100', fontsize=11, color=TEXT,
        ha='right', va='center', fontweight='bold')

ax.set_xlabel('Time (years)', fontsize=12, color=TEXT)
ax.set_ylabel('Account balance (\\$)', fontsize=12, color=TEXT)
ax.set_title('Compounding the same 12% rate at different frequencies',
             fontsize=13, pad=12, color=TEXT, fontweight='bold')
ax.set_xlim(-0.6, 12.5)
ax.set_ylim(85, 360)
ax.legend(loc='upper left', fontsize=11, frameon=True, framealpha=0.95)

plt.tight_layout()
plt.savefig('iir_fig1_staircase.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig1_staircase.png")
