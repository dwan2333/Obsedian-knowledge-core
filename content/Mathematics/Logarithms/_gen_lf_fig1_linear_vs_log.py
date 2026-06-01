"""Generate lf_fig1_linear_vs_log.png — exponential growth on linear vs log axes.

Two side-by-side panels of the same data: COVID-style exponential growth over ~50
days. Left panel: linear y-axis (the steep "curve"). Right panel: log y-axis
(a straight line). Visualizes why "log scale" is the natural language for
multiplicative growth.
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
YELLOW = '#d4a04a'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

# Synthesize exponential growth resembling COVID-19 cases outside mainland China
# Roughly: ~30 cases at day 0, doubling every 5 days
days = np.arange(0, 50)
cases = 30 * np.power(10, days / 16.0)  # x10 every 16 days, matching video

# Add a touch of noise so points look realistic
np.random.seed(42)
noise = 1 + 0.08 * (np.random.rand(len(days)) - 0.5)
cases = cases * noise

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.8))

# ---- LEFT panel: linear y-axis ----
ax1.scatter(days, cases, s=42, color=YELLOW, edgecolor='#8c6520',
            linewidth=1.2, zorder=4)
ax1.set_yscale('linear')
ax1.set_xlabel('Days since Jan 22', fontsize=11, color=TEXT)
ax1.set_ylabel('Cases', fontsize=11, color=TEXT)
ax1.set_title('Linear y-axis: exponential blows up',
              fontsize=13, pad=10, color=TEXT, fontweight='bold')
ax1.grid(True, color=GRID, linewidth=0.6)
ax1.set_xlim(-1, 51)
ax1.set_ylim(0, max(cases) * 1.1)

# Annotation showing the curve "blows up"
ax1.annotate('Hard to extrapolate:\nwhere does it cross 1M?',
             xy=(45, cases[45]),
             xytext=(25, max(cases) * 0.75),
             fontsize=11, color=ORANGE_EDGE, fontweight='bold',
             ha='center',
             arrowprops=dict(arrowstyle='->', color=ORANGE_EDGE,
                             lw=1.4),
             bbox=dict(boxstyle='round,pad=0.3',
                       facecolor='#ffeed8', edgecolor=ORANGE_EDGE))

# ---- RIGHT panel: log y-axis ----
ax2.scatter(days, cases, s=42, color=YELLOW, edgecolor='#8c6520',
            linewidth=1.2, zorder=4)
ax2.set_yscale('log')

# Linear regression in log-space to overlay best-fit line
log_cases = np.log10(cases)
slope, intercept = np.polyfit(days, log_cases, 1)
fit_days = np.linspace(0, 80, 100)
fit_cases = 10 ** (slope * fit_days + intercept)
ax2.plot(fit_days, fit_cases, color=GREEN_EDGE, linewidth=2.4,
         linestyle='--', label=r'Best-fit: $\times 10$ every $\approx 16$ days',
         zorder=3)

# Mark 1M threshold
ax2.axhline(1e6, color='#7a3030', linewidth=1.5, linestyle=':', zorder=2)
ax2.text(80, 1.2e6, '1M threshold', fontsize=10, color='#7a3030',
         ha='right', va='bottom', fontweight='bold')

# Mark intersection of fit with 1M
t_cross = (np.log10(1e6) - intercept) / slope
ax2.scatter([t_cross], [1e6], s=160, color='#7a3030',
            edgecolor='#3a1010', linewidth=1.5, zorder=5, marker='*')
ax2.annotate(f'crosses 1M at day {t_cross:.0f}\n(~April 5, 2020)',
             xy=(t_cross, 1e6),
             xytext=(t_cross - 18, 1e7),
             fontsize=10, color='#7a3030', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#7a3030',
                             lw=1.4),
             bbox=dict(boxstyle='round,pad=0.3',
                       facecolor='#ffe8e8', edgecolor='#7a3030'))

ax2.set_xlabel('Days since Jan 22', fontsize=11, color=TEXT)
ax2.set_ylabel('Cases (log scale)', fontsize=11, color=TEXT)
ax2.set_title('Log y-axis: exponential is a straight line',
              fontsize=13, pad=10, color=TEXT, fontweight='bold')
ax2.grid(True, color=GRID, linewidth=0.6, which='both')
ax2.set_xlim(-1, 86)
ax2.set_ylim(10, 1e8)
ax2.legend(loc='lower right', fontsize=10, frameon=True)

fig.suptitle('Same data, two y-axes — log scale exposes multiplicative growth',
             fontsize=14, y=1.01, color=TEXT, fontweight='bold')

plt.tight_layout()
plt.savefig('lf_fig1_linear_vs_log.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig1_linear_vs_log.png")
