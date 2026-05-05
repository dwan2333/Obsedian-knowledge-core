"""Generate sp_topic_4_triangle.png — Pascal's triangle (rows 0-5) with C(4,1)+C(4,2)=C(5,2) highlighted.

Replaces the Nano Banana Pro version, which had a "abve" typo and rendered
Pascal's identity as garbled sigma notation.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


fig, ax = plt.subplots(figsize=(9, 8.5))

rows = 6  # 0 through 5
sx, sy = 1.0, 1.1

positions = {}
for n in range(rows):
    for k in range(n + 1):
        x = (k - n / 2.0) * sx
        y = -n * sy
        positions[(n, k)] = (x, y)

        v = binom(n, k)
        bg, fg, edge = '#fafaf5', '#333333', '#cccccc'
        if (n, k) in [(4, 1), (4, 2)]:
            bg, fg, edge = '#e2924a', 'white', '#8c4f1f'
        elif (n, k) == (5, 2):
            bg, fg, edge = '#4a90e2', 'white', '#1f4f8c'

        circ = mpatches.Circle((x, y), 0.34, facecolor=bg,
                               edgecolor=edge, linewidth=1.6, zorder=2)
        ax.add_patch(circ)
        ax.text(x, y, str(v), fontsize=14, ha='center', va='center',
                color=fg, fontweight='bold', zorder=3)

# Arrows: from (4,1) and (4,2) to (5,2)
src1 = positions[(4, 1)]
src2 = positions[(4, 2)]
dst = positions[(5, 2)]

ax.annotate('', xy=(dst[0] - 0.12, dst[1] + 0.40),
            xytext=(src1[0] + 0.20, src1[1] - 0.34),
            arrowprops=dict(arrowstyle='->', color='#1f4f8c', lw=2.5))
ax.annotate('', xy=(dst[0] + 0.12, dst[1] + 0.40),
            xytext=(src2[0] - 0.20, src2[1] - 0.34),
            arrowprops=dict(arrowstyle='->', color='#1f4f8c', lw=2.5))

# Row labels
for n in range(rows):
    y = -n * sy
    x_lbl = -(rows / 2.0) * sx - 0.6
    ax.text(x_lbl, y, f'Row {n}', fontsize=11, ha='right', va='center',
            color='#888888')

# Title
ax.set_title("Pascal's Triangle — every entry is the sum of the two above",
             fontsize=15, pad=14)

# Identity equations at bottom
y_eq = -rows * sy - 0.0
ax.text(0, y_eq - 0.55,
        r'$\binom{5}{2} \;=\; \binom{4}{1} \,+\, \binom{4}{2} \;=\; 4 \,+\, 6 \;=\; 10$',
        fontsize=15, ha='center', color='#1f4f8c', fontweight='bold')
ax.text(0, y_eq - 1.3,
        r"Pascal's identity: $\;\binom{n}{k} \;=\; \binom{n-1}{k-1} \,+\, \binom{n-1}{k}$",
        fontsize=14, ha='center', color='#333333')

ax.set_xlim(-(rows / 2.0) * sx - 1.6, (rows / 2.0) * sx + 1.0)
ax.set_ylim(y_eq - 1.9, 0.7)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('sp_topic_4_triangle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_topic_4_triangle.png")
