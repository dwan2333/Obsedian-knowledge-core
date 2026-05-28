"""Generate iir_fig2_timeline.png — discrete compounding derivation timeline.

Horizontal timeline of total length T, divided into n tiny steps of width
delta_t. Each step shows the rule delta_M = r * delta_t * M, leading to
M -> M(1 + r*delta_t). Mirrors the on-screen drawing at [14:42].
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
TEXT = '#222222'
MUTE = '#888888'

fig, ax = plt.subplots(figsize=(12, 5.5))

# Main timeline
x0, x1 = 0.6, 11.4
y_line = 1.4
ax.plot([x0, x1], [y_line, y_line], color=TEXT, linewidth=2.2, zorder=2)

# Tick marks (n=10 segments)
n_seg = 10
xs = [x0 + i * (x1 - x0) / n_seg for i in range(n_seg + 1)]
for x in xs:
    ax.plot([x, x], [y_line - 0.08, y_line + 0.08],
            color=TEXT, linewidth=1.5, zorder=3)

# T bracket above
y_bracket = 2.05
ax.annotate('', xy=(x1, y_bracket), xytext=(x0, y_bracket),
            arrowprops=dict(arrowstyle='<->', color=BLUE_EDGE, lw=1.8))
ax.text((x0 + x1) / 2, y_bracket + 0.18, r'$T$  (total time)',
        fontsize=13, ha='center', va='bottom',
        color=BLUE_EDGE, fontweight='bold')

# delta_t bracket on one segment (segment 3)
xa, xb = xs[3], xs[4]
y_dt = y_line + 0.32
ax.annotate('', xy=(xb, y_dt), xytext=(xa, y_dt),
            arrowprops=dict(arrowstyle='<->', color=ORANGE_EDGE, lw=1.5))
ax.text((xa + xb) / 2, y_dt + 0.12, r'$\Delta t$',
        fontsize=12, ha='center', va='bottom',
        color=ORANGE_EDGE, fontweight='bold')

# delta_M arrow below the same segment
y_dm = y_line - 0.35
ax.annotate('', xy=(xb, y_dm), xytext=(xa, y_dm),
            arrowprops=dict(arrowstyle='->',
                            color=ORANGE_EDGE, lw=1.8,
                            connectionstyle='arc3,rad=0.35'))
ax.text((xa + xb) / 2, y_dm - 0.22,
        r'$\Delta M = r \cdot \Delta t \cdot M$',
        fontsize=12, ha='center', va='top', color=ORANGE_EDGE,
        fontweight='bold')

# Starting label "$100" at left
ax.text(x0, y_line + 0.36, r'\$100', fontsize=12,
        ha='center', va='bottom', color=TEXT, fontweight='bold')

# n = T/delta_t formula box
ax.text(6.0, 0.18,
        r'$n = T/\Delta t$ steps total $\;\;\Rightarrow\;\; '
        r'M \to M(1 + r\Delta t)\;\;\Rightarrow\;\;'
        r'M(T) = M(0)(1+r\Delta t)^n$',
        fontsize=12.5, ha='center', va='center', color=TEXT,
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

ax.text(6.0, 3.0,
        'Discrete compounding: slice $T$ into $n$ tiny steps of width $\\Delta t$',
        fontsize=13, ha='center', va='center', color=TEXT,
        fontweight='bold')

ax.set_xlim(0, 12)
ax.set_ylim(-0.4, 3.6)
ax.set_aspect('auto')
ax.axis('off')

plt.tight_layout()
plt.savefig('iir_fig2_timeline.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_fig2_timeline.png")
