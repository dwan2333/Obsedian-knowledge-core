"""Generate lf_fig7_harmonic_blocks.png — divergence proof of the harmonic
series by grouping into powers-of-2 blocks, each block summing to > 1/2."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE_EDGE = '#1f4f8c'; ORANGE_EDGE = '#8c4f1f'; GREEN_EDGE = '#3d7530'
PURPLE_EDGE = '#6e3a6c'; TEXT = '#222'; MUTE = '#888'

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_aspect('auto'); ax.axis('off')

# Series terms 1/1, 1/2, 1/3, ..., 1/32 with grouping brackets
# Groups: [1], [1/2], [1/3, 1/4], [1/5..1/8], [1/9..1/16], [1/17..1/32]
groups = [
    ([1], 'first', None, None),
    ([2], 'second', None, None),
    (list(range(3, 5)), '$\\tfrac{1}{3} + \\tfrac{1}{4} > \\tfrac{1}{4}+\\tfrac{1}{4} = \\tfrac{1}{2}$', '> 1/2', BLUE_EDGE),
    (list(range(5, 9)), '$\\tfrac{1}{5}{+}\\tfrac{1}{6}{+}\\tfrac{1}{7}{+}\\tfrac{1}{8} > 4\\cdot \\tfrac{1}{8} = \\tfrac{1}{2}$', '> 1/2', ORANGE_EDGE),
    (list(range(9, 17)), '$8$ terms $> 8\\cdot \\tfrac{1}{16} = \\tfrac{1}{2}$', '> 1/2', GREEN_EDGE),
    (list(range(17, 33)), '$16$ terms $> 16 \\cdot \\tfrac{1}{32} = \\tfrac{1}{2}$', '> 1/2', PURPLE_EDGE),
]

# Layout: each term takes 0.5 units of x; series is on y=0
DX = 0.55
all_x = []
all_labels = []
for grp in groups:
    indices, comment, lb, col = grp
    for idx in indices:
        all_x.append(len(all_x) * DX)
        all_labels.append(idx)

# Draw the fractions
for x, idx in zip(all_x, all_labels):
    color = TEXT
    ax.text(x, 0, f'$\\tfrac{{1}}{{{idx}}}$', fontsize=13, ha='center', va='center',
            color=color, fontweight='bold')
    if idx > 1:
        ax.text(x - DX/2, 0, '$+$', fontsize=12, ha='center', va='center',
                color=MUTE)

# Draw brackets and labels for each group
x_pos = 0
y_bracket = -0.55
y_label = -1.05
for indices, comment, lb, col in groups:
    n = len(indices)
    if n == 0:
        continue
    if lb is None:
        # singletons (first, second) — no bracket
        x_pos += n * DX
        continue
    x_start = (all_x.index(indices[0])) * 1
    x_start_xy = all_x[all_labels.index(indices[0])]
    x_end_xy = all_x[all_labels.index(indices[-1])]
    # Bracket
    ax.annotate('', xy=(x_end_xy + DX/3, y_bracket),
                xytext=(x_start_xy - DX/3, y_bracket),
                arrowprops=dict(arrowstyle='-', color=col, lw=2.4))
    ax.plot([x_start_xy - DX/3, x_start_xy - DX/3],
            [y_bracket, y_bracket + 0.15], color=col, lw=2.4)
    ax.plot([x_end_xy + DX/3, x_end_xy + DX/3],
            [y_bracket, y_bracket + 0.15], color=col, lw=2.4)
    # Comment
    midx = (x_start_xy + x_end_xy) / 2
    ax.text(midx, y_label, comment, fontsize=11, color=col,
            ha='center', va='center', fontweight='bold')

# Bottom conclusion
ax.text((all_x[0] + all_x[-1]) / 2, -2.0,
        r'sum $> 1 + \dfrac{1}{2} + \dfrac{1}{2} + \dfrac{1}{2} + \dfrac{1}{2} + \cdots \to \infty$',
        fontsize=14, ha='center', va='center', color=TEXT, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.4))

# Add "..." at the end
ax.text(all_x[-1] + DX, 0, r'$+\cdots$', fontsize=13,
        ha='left', va='center', color=MUTE, fontweight='bold')

ax.set_xlim(-0.5, all_x[-1] + 1.5)
ax.set_ylim(-2.5, 0.6)
ax.set_title('The harmonic series diverges — group into blocks, each block exceeds $1/2$',
             fontsize=13, pad=14, color=TEXT, fontweight='bold')

plt.tight_layout()
plt.savefig('lf_fig7_harmonic_blocks.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig7_harmonic_blocks.png")
