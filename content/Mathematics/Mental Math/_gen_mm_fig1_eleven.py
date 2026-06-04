"""Generate mm_fig1_eleven.png — the x11 digit choreography.

Three rows: 54x11=594 (basic), 68x11=748 (carry), 352x11=3872 (3-digit).
Brown = original outer digits, green = inserted adjacent-sum, red = changed by carry.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BROWN = ('#efe2cc', '#7a5a30')
GREEN = ('#cfe8bf', '#3d7530')
RED = ('#f3ccc5', '#a83227')
TEXT = '#222222'
KIND = {'n': BROWN, 's': GREEN, 'c': RED}

fig, ax = plt.subplots(figsize=(11, 7))
bw, bh = 0.92, 0.92

def box(x, y, txt, kind, fs=23):
    face, edge = KIND[kind]
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), bw, bh, boxstyle='round,pad=0.02,rounding_size=0.09',
        facecolor=face, edgecolor=edge, linewidth=2.0, zorder=2))
    ax.text(x + bw / 2, y + bh / 2, txt, ha='center', va='center',
            fontsize=fs, color=edge, fontweight='bold', zorder=3)

def row(y, prob, boxes, ans, caption):
    ax.text(0.2, y + bh / 2, prob, ha='left', va='center', fontsize=18,
            color=TEXT, fontweight='bold')
    x = 3.5
    for txt, kind in boxes:
        box(x, y, txt, kind)
        x += bw + 0.16
    ax.text(x + 0.15, y + bh / 2, "= " + ans, ha='left', va='center',
            fontsize=18, color=TEXT, fontweight='bold')
    ax.text(3.5, y - 0.30, caption, ha='left', va='top', fontsize=12.5,
            color='#555555', style='italic')

row(5.1, "54 × 11", [("5", 'n'), ("9", 's'), ("4", 'n')], "594",
    "middle digit = 5 + 4 = 9")
row(2.9, "68 × 11", [("7", 'c'), ("4", 's'), ("8", 'n')], "748",
    "6 + 8 = 14  →  write 4, carry the 1 onto 6 → 7")
row(0.6, "352 × 11", [("3", 'n'), ("8", 's'), ("7", 's'), ("2", 'n')], "3872",
    "gaps: 3 + 5 = 8  and  5 + 2 = 7")

# legend
ax.add_patch(mpatches.FancyBboxPatch((3.5, -1.15), 0.4, 0.4,
             boxstyle='round,pad=0.02,rounding_size=0.06',
             facecolor=GREEN[0], edgecolor=GREEN[1], linewidth=1.6))
ax.text(4.05, -0.95, "inserted sum", fontsize=11, va='center', color='#555')
ax.add_patch(mpatches.FancyBboxPatch((6.2, -1.15), 0.4, 0.4,
             boxstyle='round,pad=0.02,rounding_size=0.06',
             facecolor=RED[0], edgecolor=RED[1], linewidth=1.6))
ax.text(6.75, -0.95, "changed by carry", fontsize=11, va='center', color='#555')

ax.set_title("Trick 1 — multiplying by 11", fontsize=16, color=TEXT,
             fontweight='bold', pad=12)
ax.set_xlim(0, 9.7)
ax.set_ylim(-1.5, 6.4)
ax.axis('off')
plt.tight_layout()
plt.savefig('mm_fig1_eleven.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved mm_fig1_eleven.png")
