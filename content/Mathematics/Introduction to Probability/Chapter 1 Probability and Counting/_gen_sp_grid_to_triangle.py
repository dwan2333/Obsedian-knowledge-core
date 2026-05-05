"""Generate sp_topic_5_grid_to_triangle.png — lattice rotates 45° into Pascal's triangle.

Two-panel figure. Left: lattice points (a, b) labeled with binomial(a+b, a).
Right: same numbers rearranged as Pascal's triangle. Anti-diagonals of
the lattice (constant a + b) correspond to rows of the triangle and share
a color.
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


fig, axs = plt.subplots(1, 2, figsize=(13.5, 6.8))

# Diagonal/row palette — light to dark
diag_fc = ['#fce8d4', '#fdd6a8', '#f5b66e', '#e2924a', '#c4731f']
diag_ec = ['#d0a878', '#b88a4f', '#a06a2c', '#8c4f1f', '#6e3a14']

N = 4  # 5 rows / 5 anti-diagonals

# === LEFT: lattice grid ===
ax = axs[0]
for a in range(N + 1):
    for b in range(N + 1):
        d = a + b
        if d > N:
            continue
        v = binom(d, a)
        circ = mpatches.Circle((a, b), 0.34, facecolor=diag_fc[d],
                               edgecolor=diag_ec[d], linewidth=1.6, zorder=3)
        ax.add_patch(circ)
        ax.text(a, b, str(v), fontsize=12, ha='center', va='center',
                color='#333333', fontweight='bold', zorder=4)

# Axis arrows
ax.annotate('', xy=(N + 0.8, -0.4), xytext=(-0.5, -0.4),
            arrowprops=dict(arrowstyle='->', color='#666666', lw=1.4))
ax.text(N + 0.95, -0.4, r'$a$', fontsize=13, va='center', color='#666666')
ax.annotate('', xy=(-0.5, N + 0.8), xytext=(-0.5, -0.4),
            arrowprops=dict(arrowstyle='->', color='#666666', lw=1.4))
ax.text(-0.5, N + 0.95, r'$b$', fontsize=13, ha='center', color='#666666')

ax.set_title(r'Lattice: value at $(a,b)$ is $\binom{a+b}{a}$',
             fontsize=14, pad=14)
ax.set_xlim(-1.1, N + 1.6)
ax.set_ylim(-1.1, N + 1.6)
ax.set_aspect('equal')
ax.axis('off')

# === RIGHT: Pascal's triangle ===
ax = axs[1]
rows = N + 1
sx, sy = 0.95, 1.0
for n in range(rows):
    for k in range(n + 1):
        x = (k - n / 2.0) * sx
        y = -n * sy
        v = binom(n, k)
        circ = mpatches.Circle((x, y), 0.32, facecolor=diag_fc[n],
                               edgecolor=diag_ec[n], linewidth=1.6, zorder=3)
        ax.add_patch(circ)
        ax.text(x, y, str(v), fontsize=12, ha='center', va='center',
                color='#333333', fontweight='bold', zorder=4)
    ax.text(-(rows / 2) * sx - 0.6, -n * sy, f'Row {n}',
            fontsize=10, ha='right', va='center', color='#888888')

ax.set_title(r"Pascal's Triangle — same numbers, rotated 45°",
             fontsize=14, pad=14)
ax.set_xlim(-(rows / 2) * sx - 1.5, (rows / 2) * sx + 1.0)
ax.set_ylim(-rows * sy + 0.1, 0.8)
ax.set_aspect('equal')
ax.axis('off')

# Suptitle and caption
fig.suptitle(
    r"Same numbers, two viewpoints: lattice (left) $\to$ "
    r"Pascal's triangle (right) by 45° rotation",
    fontsize=14, y=1.02
)
fig.text(
    0.5, 0.02,
    r'Each anti-diagonal of the lattice (constant $a+b$) maps to a row '
    r'of the triangle. Same shade = same row.',
    fontsize=12, ha='center', color='#333333'
)

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig('sp_topic_5_grid_to_triangle.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_topic_5_grid_to_triangle.png")
