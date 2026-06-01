"""Generate lf_fig4_change_of_base.png — parallel log_2 and log_10 ladders
linked by the 0.3 multiplier.

Three columns of values: number x, log_2(x), log_10(x). Each row is a power
of 2 chosen so log_2(x) is a nice integer. Arrows between log_2 and log_10
show "x 0.3" — visualizing that the two logarithm bases are related by a
constant multiplier.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

fig, ax = plt.subplots(figsize=(11, 8))

# Powers of 2 to display (log_10 values rounded to 1 decimal)
rows = [
    (1,      "$1$",                    0,  "0"),
    (2,      "$2$",                    1,  "0.3"),
    (8,      "$8$",                    3,  "0.9"),
    (64,     "$64$",                   6,  "1.8"),
    (1024,   r"$1{,}024 \approx 10^3$", 10, "3.0"),
    (1048576, "$10^6$",                 20, "6.0"),
]

# Layout: x and y positions
x_num = 0.5      # number label x
x_log2 = 4.5     # log_2 column x
x_log10 = 8.5    # log_10 column x
y_start = 7.0
y_step = -1.0

# Column headers
ax.text(x_num, y_start + 0.9, 'number $x$',
        fontsize=14, color=TEXT, ha='center', va='center',
        fontweight='bold')
ax.text(x_log2, y_start + 0.9, r'$\log_2(x)$',
        fontsize=14, color=BLUE_EDGE, ha='center', va='center',
        fontweight='bold')
ax.text(x_log10, y_start + 0.9, r'$\log_{10}(x) \approx$',
        fontsize=14, color=ORANGE_EDGE, ha='center', va='center',
        fontweight='bold')

# Horizontal divider under headers
ax.plot([x_num - 1.2, x_log10 + 1.2], [y_start + 0.4, y_start + 0.4],
        color=TEXT, linewidth=1.6, zorder=2)

# Draw rows
for i, (num, num_lbl, l2, l10_lbl) in enumerate(rows):
    y = y_start + i * y_step

    # Number cell
    ax.text(x_num, y, num_lbl, fontsize=13, color=TEXT,
            ha='center', va='center')

    # log_2 cell
    ax.scatter([x_log2], [y], s=600, color=BLUE,
               edgecolor=BLUE_EDGE, linewidth=1.6, zorder=3)
    ax.text(x_log2, y, f'${l2}$', fontsize=14, color='white',
            ha='center', va='center', fontweight='bold', zorder=4)

    # log_10 cell (plain numeric, "≈" lives in the header)
    ax.scatter([x_log10], [y], s=600, color=ORANGE,
               edgecolor=ORANGE_EDGE, linewidth=1.6, zorder=3)
    ax.text(x_log10, y, l10_lbl, fontsize=14, color='white',
            ha='center', va='center', fontweight='bold', zorder=4)

    # Arrow from log_2 to log_10 with x 0.3 multiplier
    ax.annotate('', xy=(x_log10 - 0.5, y), xytext=(x_log2 + 0.5, y),
                arrowprops=dict(arrowstyle='->', color=GREEN_EDGE,
                                lw=2.0, mutation_scale=14),
                zorder=2)
    ax.text((x_log2 + x_log10) / 2, y + 0.22, r'$\times 0.3$',
            fontsize=11, color=GREEN_EDGE, fontweight='bold',
            ha='center', va='bottom')

# Footer with formula
ax.text((x_num + x_log10) / 2, y_start + 6 * y_step - 0.6,
        r'$\log_{10}(x) = \log_2(x) \cdot \log_{10}(2) \approx 0.3 \cdot \log_2(x)$',
        fontsize=13, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fff8dc', edgecolor='#aa8b3a', linewidth=1.5),
        fontweight='bold')

# Annotation: source of 0.3
ax.text((x_num + x_log10) / 2, y_start + 6 * y_step - 1.6,
        r'(from $2^{10} = 1024 \approx 10^3 \Rightarrow \log_{10}(2) \approx 3/10$)',
        fontsize=11, color=MUTE, ha='center', va='center',
        fontstyle='italic')

ax.set_title('Change of base: $\\log_2$ and $\\log_{10}$ differ by a constant factor',
             fontsize=14, pad=14, color=TEXT, fontweight='bold')

ax.set_xlim(-1, 10)
ax.set_ylim(-0.5, 9.5)
ax.set_aspect('auto')
ax.axis('off')

plt.tight_layout()
plt.savefig('lf_fig4_change_of_base.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig4_change_of_base.png")
