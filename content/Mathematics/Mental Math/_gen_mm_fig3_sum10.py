"""Generate mm_fig3_sum10.png — same first digit, last digits sum to 10.

Two rows: 44x46 = 2024 and the opening teaser 86x84 = 7224.
head = first digit x next integer ; tail = product of the last digits.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = ('#cfe0f2', '#1f4f8c')
ORANGE = ('#f5e0c0', '#8c5a1f')
TEXT = '#222222'

fig, ax = plt.subplots(figsize=(10.5, 5.4))

def example(y, prob, head, head_calc, tail, tail_calc, ans, note):
    ax.text(0.3, y, prob, ha='left', va='center', fontsize=22, color=TEXT,
            fontweight='bold')
    ax.text(2.5, y, r"$\rightarrow$", ha='center', va='center', fontsize=22,
            color='#888888')
    # head
    ax.add_patch(mpatches.FancyBboxPatch((3.1, y - 0.55), 1.35, 1.1,
                 boxstyle='round,pad=0.03,rounding_size=0.12',
                 facecolor=BLUE[0], edgecolor=BLUE[1], linewidth=2.2))
    ax.text(3.775, y, head, ha='center', va='center', fontsize=26,
            color=BLUE[1], fontweight='bold')
    ax.text(3.775, y - 0.92, head_calc, ha='center', va='center', fontsize=12.5,
            color=BLUE[1])
    # tail
    ax.add_patch(mpatches.FancyBboxPatch((4.65, y - 0.55), 1.35, 1.1,
                 boxstyle='round,pad=0.03,rounding_size=0.12',
                 facecolor=ORANGE[0], edgecolor=ORANGE[1], linewidth=2.2))
    ax.text(5.325, y, tail, ha='center', va='center', fontsize=26,
            color=ORANGE[1], fontweight='bold')
    ax.text(5.325, y - 0.92, tail_calc, ha='center', va='center', fontsize=12.5,
            color=ORANGE[1])
    # answer
    ax.text(6.35, y, r"$=$", ha='center', va='center', fontsize=22,
            color='#888888')
    ax.text(7.8, y, ans, ha='center', va='center', fontsize=28, color=TEXT,
            fontweight='bold')
    ax.text(0.3, y - 1.45, note, ha='left', va='center', fontsize=11.5,
            color='#555555', style='italic')

example(4.2, "44 × 46", "20", r"$4 \times 5$", "24", r"$4 \times 6$", "2024",
        "first digits equal (4);  last digits 4 + 6 = 10")
example(1.7, "86 × 84", "72", r"$8 \times 9$", "24", r"$6 \times 4$", "7224",
        "the opening teaser — same trick (8;  6 + 4 = 10)")

ax.text(3.775, 5.45, "head: first digit × next", ha='center', va='center',
        fontsize=11.5, color='#555555', style='italic')
ax.text(5.325, 5.45, "tail: last × last", ha='center', va='center',
        fontsize=11.5, color='#555555', style='italic')

ax.set_title("Trick 3 — same first digit, last digits sum to 10",
             fontsize=15, color=TEXT, fontweight='bold', pad=10)
ax.set_xlim(0, 9.5)
ax.set_ylim(-0.2, 6.2)
ax.axis('off')
plt.tight_layout()
plt.savefig('mm_fig3_sum10.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved mm_fig3_sum10.png")
