"""Generate sp_topic_3_two_paths.png — two distinct increasing paths from (0,0) to (3,2).

Both use exactly three R-steps and two U-steps, but the steps appear in
different orders, illustrating that a path is determined by the sequence
order of its R/U moves.
"""
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 2, figsize=(11.5, 5.6))

paths = [
    ([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)], "R R R U U"),
    ([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2)], "U R U R R"),
]

for ax, (path, seq) in zip(axs, paths):
    for i in range(4):
        ax.axvline(i, color='#e6e6e6', linewidth=0.7, zorder=1)
    for j in range(3):
        ax.axhline(j, color='#e6e6e6', linewidth=0.7, zorder=1)
    xs, ys = np.meshgrid(np.arange(4), np.arange(3))
    ax.scatter(xs.ravel(), ys.ravel(), s=22, color='#999999', zorder=2)

    xp = [p[0] for p in path]
    yp = [p[1] for p in path]
    ax.plot(xp, yp, color='#2c6cb0', linewidth=3.5, zorder=3,
            solid_capstyle='round')
    ax.scatter(xp, yp, s=55, color='#4a90e2', edgecolor='#1f4f8c',
               linewidth=1.2, zorder=4)

    ax.scatter([0, 3], [0, 2], s=160, color='#e2924a',
               edgecolor='#8c4f1f', linewidth=2, zorder=5)
    ax.text(-0.2, -0.45, r'$(0,0)$', fontsize=13, ha='right',
            color='#8c4f1f', fontweight='bold')
    ax.text(3.15, 2.25, r'$(3,2)$', fontsize=13, ha='left',
            color='#8c4f1f', fontweight='bold')

    ax.set_title(f'Step sequence: {seq}', fontsize=14, pad=10)

    ax.set_xlim(-0.7, 4.0)
    ax.set_ylim(-0.9, 2.7)
    ax.set_aspect('equal')
    ax.axis('off')

fig.suptitle(
    r'Two distinct paths from $(0,0)$ to $(3,2)$ — '
    r'same multiset of steps, different order',
    fontsize=14, y=1.02
)
fig.text(
    0.5, 0.02,
    r"Both paths use 3 R-steps and 2 U-steps. "
    r"Total such paths $= \binom{5}{3} = \binom{5}{2} = 10$.",
    fontsize=12, ha='center', color='#333333'
)

plt.tight_layout(rect=[0, 0.04, 1, 0.97])
plt.savefig('sp_topic_3_two_paths.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved sp_topic_3_two_paths.png")
