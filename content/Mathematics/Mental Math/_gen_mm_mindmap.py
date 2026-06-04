"""Generate mm_mindmap.png — concept map for the Mental Math tricks note."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(12.5, 9.2))

cw, ch = 4.4, 1.8
center = mpatches.FancyBboxPatch(
    (-cw / 2, -ch / 2), cw, ch,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4)
ax.add_patch(center)
ax.text(0, 0.30, "Mental Math", fontsize=19, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.42, "multiply faster than a calculator", fontsize=11.5,
        ha='center', va='center', color='white', zorder=5)

topics = [
    ("Trick 1 —  × 11",
     "Split the digits, insert\n"
     "adjacent-pair sums:\n"
     r"$a\,|\,(a{+}b)\,|\,b$." "\n"
     "Carry left if a sum > 9.\n"
     r"$54{\to}594,\ 68{\to}748$"),
    ("Trick 2 — ends in 5",
     r"Square of $\overline{a5}$:" "\n"
     r"head $= a(a{+}1)$," "\n"
     "tail $= 25$ always.\n"
     r"$75^2 = 56\,|\,25 = 5625$"),
    ("Trick 3 — sum to 10",
     "Same first digit, last\n"
     "digits add to 10:\n"
     r"$a(a{+}1)\,|\,(b\times c)$." "\n"
     r"$44{\times}46 = 20\,|\,24$"),
    ("Why it works",
     r"$(10a{+}b)(10a{+}c)$" "\n"
     r"$=100\,a(a{+}1)+bc$" "\n"
     r"when $b{+}c=10$." "\n"
     "Trick 2 is the case\n"
     r"$b=c=5$."),
]

palette = [
    ('#e2924a', '#8c4f1f'),
    ('#7bb55c', '#3d7530'),
    ('#b76db4', '#6e3a6c'),
    ('#4a90e2', '#1f4f8c'),
]

angles = [pi / 4, -pi / 4, -3 * pi / 4, 3 * pi / 4]
radius = 5.5
bw, bh = 4.3, 2.4
for i, ((title, body), (fc, ec)) in enumerate(zip(topics, palette)):
    th = angles[i]
    x = radius * cos(th)
    y = radius * sin(th)
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5, zorder=1)
    box = mpatches.FancyBboxPatch(
        (x - bw / 2, y - bh / 2), bw, bh,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2)
    ax.add_patch(box)
    ax.text(x, y + bh / 2 - 0.34, title, fontsize=12.5, ha='center',
            va='center', color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.28, body, fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("Mental Math Multiplication Tricks — concept map", fontsize=15,
             pad=10, fontweight='bold')
ax.set_xlim(-8.6, 8.6)
ax.set_ylim(-8.0, 8.2)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('mm_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved mm_mindmap.png")
