"""Generate a walkthrough of De Morgan's Law 1 via Venn diagram shading.

Produces a 2x3 grid of panels showing:
  Row 1: A∪B  |  (A∪B)^c  |  reference (regions labeled, no shading)
  Row 2: A^c  |  B^c      |  A^c ∩ B^c

The reader can then see that the (A∪B)^c panel and the A^c ∩ B^c panel
shade identical regions — proof of Law 1 by inspection.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BG = '#fafaf5'
SHADE = '#d6443f'
SHADE_ALPHA = 0.55
A_STROKE = '#2c6cb0'
B_STROKE = '#b06c2c'

# Circle parameters
A_CENTER = (3.7, 3.4)
B_CENTER = (6.3, 3.4)
R = 1.8


def draw_frame(ax, title, show_region_labels=False):
    """Draw the empty Venn diagram frame (U rect, circle outlines, labels)."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=13, fontweight='bold', pad=8)

    # Universe background
    bg = mpatches.Rectangle((0.2, 0.2), 9.6, 5.6, linewidth=0, facecolor=BG)
    ax.add_patch(bg)


def finish_frame(ax, show_region_labels=False):
    """Draw outlines & labels ON TOP of any shading."""
    # U border
    border = mpatches.Rectangle((0.2, 0.2), 9.6, 5.6, linewidth=1.5,
                                 edgecolor='#333', facecolor='none')
    ax.add_patch(border)

    # Circle outlines
    circA = mpatches.Circle(A_CENTER, R, linewidth=2.2,
                             edgecolor=A_STROKE, facecolor='none')
    ax.add_patch(circA)
    circB = mpatches.Circle(B_CENTER, R, linewidth=2.2,
                             edgecolor=B_STROKE, facecolor='none')
    ax.add_patch(circB)

    # Set labels
    ax.text(9.55, 5.55, 'U', fontsize=13, fontweight='bold', ha='right', va='top')
    ax.text(2.2, 5.0, 'A', fontsize=15, fontweight='bold', color='#1f4f8c')
    ax.text(7.8, 5.0, 'B', fontsize=15, fontweight='bold', color='#8c4f1f')

    if show_region_labels:
        ax.text(2.8, 3.4, '(1)', fontsize=12, fontweight='bold', ha='center', va='center')
        ax.text(5.0, 3.4, '(3)', fontsize=12, fontweight='bold', ha='center', va='center')
        ax.text(7.2, 3.4, '(2)', fontsize=12, fontweight='bold', ha='center', va='center')
        ax.text(5.0, 0.9, '(4)', fontsize=12, fontweight='bold', ha='center', va='center')


def shade_circles(ax, which):
    """Shade one or both circles with semitransparent color.

    `which` is a subset of {'A', 'B'}."""
    if 'A' in which:
        a = mpatches.Circle(A_CENTER, R, facecolor=SHADE, alpha=SHADE_ALPHA, linewidth=0)
        ax.add_patch(a)
    if 'B' in which:
        b = mpatches.Circle(B_CENTER, R, facecolor=SHADE, alpha=SHADE_ALPHA, linewidth=0)
        ax.add_patch(b)


def shade_outside(ax, which_circles_to_cut_out):
    """Shade the whole universe, then 'cut out' (repaint with BG) the named circles."""
    rect = mpatches.Rectangle((0.2, 0.2), 9.6, 5.6,
                               facecolor=SHADE, alpha=SHADE_ALPHA, linewidth=0)
    ax.add_patch(rect)
    # Overpaint cut-out circles with the BG color (opaque)
    if 'A' in which_circles_to_cut_out:
        a = mpatches.Circle(A_CENTER, R, facecolor=BG, linewidth=0)
        ax.add_patch(a)
    if 'B' in which_circles_to_cut_out:
        b = mpatches.Circle(B_CENTER, R, facecolor=BG, linewidth=0)
        ax.add_patch(b)


# ---------- Build the 2x3 grid ----------

fig, axes = plt.subplots(2, 3, figsize=(15, 7.5))

# Row 1 Panel 1: A ∪ B → shade both circles (regions 1, 2, 3)
draw_frame(axes[0, 0], r'$A \cup B$  (shades regions 1, 2, 3)')
shade_circles(axes[0, 0], {'A', 'B'})
finish_frame(axes[0, 0], show_region_labels=True)

# Row 1 Panel 2: (A ∪ B)^c → shade outside both (region 4)
draw_frame(axes[0, 1], r'$(A \cup B)^c$  (shades region 4)')
shade_outside(axes[0, 1], {'A', 'B'})
finish_frame(axes[0, 1], show_region_labels=True)

# Row 1 Panel 3: reference (no shading), all regions labeled
draw_frame(axes[0, 2], 'Reference (no shading)')
finish_frame(axes[0, 2], show_region_labels=True)

# Row 2 Panel 1: A^c → shade universe minus A (regions 2, 4)
draw_frame(axes[1, 0], r'$A^c$  (shades regions 2, 4)')
shade_outside(axes[1, 0], {'A'})
finish_frame(axes[1, 0], show_region_labels=True)

# Row 2 Panel 2: B^c → shade universe minus B (regions 1, 4)
draw_frame(axes[1, 1], r'$B^c$  (shades regions 1, 4)')
shade_outside(axes[1, 1], {'B'})
finish_frame(axes[1, 1], show_region_labels=True)

# Row 2 Panel 3: A^c ∩ B^c → intersection of the above; equals (A∪B)^c
# So shade the outside-both region (region 4)
draw_frame(axes[1, 2], r'$A^c \cap B^c$  (shades region 4)')
shade_outside(axes[1, 2], {'A', 'B'})
finish_frame(axes[1, 2], show_region_labels=True)

plt.suptitle(
    r"De Morgan's Law 1: $(A \cup B)^c = A^c \cap B^c$  —  both sides shade region (4)",
    fontsize=15, y=1.00, fontweight='bold'
)
plt.tight_layout()
plt.savefig('chapter1_fig_demorgan_shading_steps.png',
            dpi=180, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved chapter1_fig_demorgan_shading_steps.png")
