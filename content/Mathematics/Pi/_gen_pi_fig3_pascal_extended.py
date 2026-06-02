"""Generate pi_fig3_pascal_extended.png — Pascal's triangle rows 0-5 plus the
extended rows above (n=-1, n=-2) and a fractional row (n=1/2).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'; TEXT = '#222'; MUTE = '#888'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_aspect('equal'); ax.axis('off')

# Standard Pascal rows (0 to 5) — drawn lower part
std_rows = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]
# Negative-n rows (extended upward) — rotated copy of Pascal
neg_rows = {
    -1: ['1', '-1', '1', '-1', '1', '-1'],
    -2: ['1', '-2', '3', '-4', '5', '-6'],
}
# Fractional row n=1/2
half_row = ['1', '1/2', '-1/8', '1/16', '-5/128', '7/256']

# Layout: y-axis represents row index, x-axis is column position
DX = 1.6  # horizontal spacing
DY = 1.1  # vertical spacing

def draw_row(values, y, color_edge, color_face, label, label_color):
    n = len(values)
    x_start = -(n - 1) * DX / 2
    for i, val in enumerate(values):
        x = x_start + i * DX
        circ = mpatches.Circle((x, y), 0.42, facecolor=color_face,
                               edgecolor=color_edge, linewidth=1.6, zorder=3)
        ax.add_patch(circ)
        ax.text(x, y, str(val), fontsize=11, ha='center', va='center',
                color='white', fontweight='bold', zorder=4)
    # Row label on the left
    ax.text(x_start - 1.4, y, label, fontsize=12.5,
            color=label_color, fontweight='bold', ha='right', va='center')

# Draw from top to bottom
y_neg2 = 4 * DY
y_neg1 = 3 * DY
y_zero = 2 * DY
y_half = DY  # between row 0 and row 1
y_one = 0
y_two = -DY
y_three = -2 * DY
y_four = -3 * DY
y_five = -4 * DY

# Extended negative rows
draw_row(neg_rows[-2], y_neg2, ORANGE_EDGE, '#e2924a', r'$n = -2$', ORANGE_EDGE)
draw_row(neg_rows[-1], y_neg1, ORANGE_EDGE, '#e2924a', r'$n = -1$', ORANGE_EDGE)
# Boundary marker
ax.plot([-7, 7], [y_zero + DY * 0.55, y_zero + DY * 0.55],
        color=MUTE, lw=0.8, linestyle=':')
ax.text(7.5, y_zero + DY * 0.55, 'extended above', fontsize=10,
        color=MUTE, ha='left', va='center', style='italic')

# Standard rows 0-5
draw_row([str(v) for v in std_rows[0]], y_zero, BLUE_EDGE, '#4a90e2', r'$n = 0$', BLUE_EDGE)
# Fractional row 1/2 (between 0 and 1)
draw_row(half_row, y_half, PURPLE_EDGE, '#b76db4', r'$n = 1/2$', PURPLE_EDGE)
draw_row([str(v) for v in std_rows[1]], y_one, BLUE_EDGE, '#4a90e2', r'$n = 1$', BLUE_EDGE)
draw_row([str(v) for v in std_rows[2]], y_two, BLUE_EDGE, '#4a90e2', r'$n = 2$', BLUE_EDGE)
draw_row([str(v) for v in std_rows[3]], y_three, BLUE_EDGE, '#4a90e2', r'$n = 3$', BLUE_EDGE)
draw_row([str(v) for v in std_rows[4]], y_four, BLUE_EDGE, '#4a90e2', r'$n = 4$', BLUE_EDGE)
draw_row([str(v) for v in std_rows[5]], y_five, BLUE_EDGE, '#4a90e2', r'$n = 5$', BLUE_EDGE)

# Title
ax.set_title("Pascal's triangle — extended above (integer rows) and between (fractional rows)",
             fontsize=14, pad=14, color=TEXT, fontweight='bold')

# Legend
ax.text(-8, -5 * DY, 'Standard rows', fontsize=11, color=BLUE_EDGE,
        ha='left', va='center', fontweight='bold')
ax.text(-3.5, -5 * DY, '· Negative rows (rotated copy of standard)',
        fontsize=11, color=ORANGE_EDGE, ha='left', va='center', fontweight='bold')
ax.text(-8, -5 * DY - 0.6, 'Fractional row n=1/2 → coefficients of $(1+x)^{1/2}$',
        fontsize=11, color=PURPLE_EDGE, ha='left', va='center', fontweight='bold')

ax.set_xlim(-10, 10); ax.set_ylim(-6 * DY, 5.5 * DY)

plt.tight_layout()
plt.savefig('pi_fig3_pascal_extended.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pi_fig3_pascal_extended.png")
