"""Generate mm_fig2_square5.png — squaring a 2-digit number ending in 5.

75^2: head = 7x8 = 56 (the first digit times the next integer), tail = 25
(always, since 5x5 = 25). Answer 5625.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = ('#cfe0f2', '#1f4f8c')
ORANGE = ('#f5e0c0', '#8c5a1f')
TEXT = '#222222'

fig, ax = plt.subplots(figsize=(10, 4.4))

ax.text(0.3, 1.5, r"$75^2$", ha='left', va='center', fontsize=30, color=TEXT,
        fontweight='bold')
ax.text(1.9, 1.5, r"$\rightarrow$", ha='center', va='center', fontsize=26,
        color='#888888')

# head block
ax.add_patch(mpatches.FancyBboxPatch((2.6, 0.95), 1.5, 1.1,
             boxstyle='round,pad=0.03,rounding_size=0.12',
             facecolor=BLUE[0], edgecolor=BLUE[1], linewidth=2.2))
ax.text(3.35, 1.5, "56", ha='center', va='center', fontsize=30,
        color=BLUE[1], fontweight='bold')
ax.text(3.35, 0.55, r"head: $7 \times 8$", ha='center', va='center',
        fontsize=14, color=BLUE[1])
ax.text(3.35, 2.45, "first digit × next", ha='center', va='center',
        fontsize=12, color='#555555', style='italic')

# tail block
ax.add_patch(mpatches.FancyBboxPatch((4.35, 0.95), 1.5, 1.1,
             boxstyle='round,pad=0.03,rounding_size=0.12',
             facecolor=ORANGE[0], edgecolor=ORANGE[1], linewidth=2.2))
ax.text(5.1, 1.5, "25", ha='center', va='center', fontsize=30,
        color=ORANGE[1], fontweight='bold')
ax.text(5.1, 0.55, r"tail: $5 \times 5$", ha='center', va='center',
        fontsize=14, color=ORANGE[1])
ax.text(5.1, 2.45, "always 25", ha='center', va='center', fontsize=12,
        color='#555555', style='italic')

ax.text(6.2, 1.5, r"$=$", ha='center', va='center', fontsize=26, color='#888888')
ax.text(7.6, 1.5, "5625", ha='center', va='center', fontsize=32, color=TEXT,
        fontweight='bold')

ax.set_title(r"Trick 2 — squaring a two-digit number ending in 5",
             fontsize=15, color=TEXT, fontweight='bold', pad=10)
ax.set_xlim(0, 9)
ax.set_ylim(0, 3)
ax.axis('off')
plt.tight_layout()
plt.savefig('mm_fig2_square5.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved mm_fig2_square5.png")
