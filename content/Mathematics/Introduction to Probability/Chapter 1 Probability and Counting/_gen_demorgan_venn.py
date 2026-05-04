"""Generate the De Morgan's Laws Venn diagram for Chapter 1.

Produces a 4-region Venn diagram with regions (1), (2), (3), (4) labeled.
Used to illustrate the Venn-diagram reading of De Morgan's laws in
Chapter 1 (Main).md, inserted after Example 1.2.2 (Coin Flips).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

# Universe rectangle (U)
rect = mpatches.Rectangle(
    (0.2, 0.2), 9.6, 5.6,
    linewidth=2, edgecolor='#333333', facecolor='#fafaf5'
)
ax.add_patch(rect)

# Circle A (left)
circA = mpatches.Circle(
    (3.7, 3.4), 1.8,
    linewidth=2, edgecolor='#2c6cb0', facecolor='#4a90e2', alpha=0.28
)
ax.add_patch(circA)

# Circle B (right, overlapping A)
circB = mpatches.Circle(
    (6.3, 3.4), 1.8,
    linewidth=2, edgecolor='#b06c2c', facecolor='#e2924a', alpha=0.28
)
ax.add_patch(circB)

# U label (top-right of universe)
ax.text(9.55, 5.55, 'U', fontsize=22, fontweight='bold',
        ha='right', va='top', color='#333333')

# A / B set labels (outside the circles, near their tops)
ax.text(2.2, 5.0, 'A', fontsize=22, fontweight='bold', color='#1f4f8c')
ax.text(7.8, 5.0, 'B', fontsize=22, fontweight='bold', color='#8c4f1f')

# Region (1) — A only
ax.text(2.8, 3.4, '(1)', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#1f4f8c')
ax.text(2.8, 2.95, 'A only', fontsize=11, ha='center', va='center')

# Region (3) — A ∩ B (overlap, centered between circle centers)
ax.text(5.0, 3.4, '(3)', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#663f1f')
ax.text(5.0, 2.95, r'$A \cap B$', fontsize=12, ha='center', va='center')

# Region (2) — B only
ax.text(7.2, 3.4, '(2)', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#8c4f1f')
ax.text(7.2, 2.95, 'B only', fontsize=11, ha='center', va='center')

# Region (4) — outside both (bottom of universe, below both circles)
ax.text(5.0, 1.0, '(4)', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#333333')
ax.text(5.0, 0.6, 'outside both (neither in A nor B)',
        fontsize=11, ha='center', va='center', style='italic')

plt.tight_layout()
plt.savefig(
    'chapter1_fig_demorgan_venn.png',
    dpi=220, bbox_inches='tight', facecolor='white'
)
plt.close()
print("Saved chapter1_fig_demorgan_venn.png")
