"""Generate ipt_mindmap.png — concept map for the Inverse Pythagorean Theorem note."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(12.5, 9.2))

cw, ch = 4.6, 1.9
center = mpatches.FancyBboxPatch(
    (-cw / 2, -ch / 2), cw, ch,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4)
ax.add_patch(center)
ax.text(0, 0.34, r"$\dfrac{1}{a^2} + \dfrac{1}{b^2} = \dfrac{1}{h^2}$",
        fontsize=18, ha='center', va='center', color='white',
        fontweight='bold', zorder=5)
ax.text(0, -0.46, "Inverse Pythagorean Theorem", fontsize=12.5, ha='center',
        va='center', color='white', zorder=5)

topics = [
    ("1. The setup",
     r"Drop altitude $h$ to $c$." "\n"
     r"Foot splits $c$ into" "\n"
     r"$c_1 + c_2 = c$." "\n"
     "Three right triangles."),
    ("2. Similarity",
     "AA: shared acute angle\n"
     "+ right angle.\n"
     "Transitivity $\\Rightarrow$ all three\n"
     "similar. Redraw aligned."),
    ("3. Pythagoras proof",
     r"$\frac{a}{c_1}=\frac{c}{a},\ \frac{b}{c_2}=\frac{c}{b}$" "\n"
     r"$\Rightarrow a^2=cc_1,\ b^2=cc_2$." "\n"
     r"Add: $a^2+b^2=c(c_1{+}c_2)$" "\n"
     r"$= c^2$."),
    ("4. Inverse proof",
     r"Area: $\frac{1}{2} ab = \frac{1}{2} ch$" "\n"
     r"$\Rightarrow c = ab/h$." "\n"
     r"Sub into $a^2+b^2=c^2$," "\n"
     r"$\div\, a^2b^2 \Rightarrow$ reciprocals."),
]

palette = [
    ('#e2924a', '#8c4f1f'),
    ('#7bb55c', '#3d7530'),
    ('#b76db4', '#6e3a6c'),
    ('#4a90e2', '#1f4f8c'),
]

n = len(topics)
radius = 5.4
bw, bh = 4.2, 2.25

# place 4 nodes at diagonal positions (NE, SE, SW, NW)
angles = [pi / 4, -pi / 4, -3 * pi / 4, 3 * pi / 4]
for i, ((title, body), (fc, ec)) in enumerate(zip(topics, palette)):
    theta = angles[i]
    x = radius * cos(theta)
    y = radius * sin(theta)
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5, zorder=1)
    box = mpatches.FancyBboxPatch(
        (x - bw / 2, y - bh / 2), bw, bh,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2)
    ax.add_patch(box)
    ax.text(x, y + bh / 2 - 0.34, title, fontsize=12.5, ha='center',
            va='center', color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.22, body, fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("The Inverse Pythagorean Theorem — concept map", fontsize=15,
             pad=10, fontweight='bold')
ax.set_xlim(-8.6, 8.6)
ax.set_ylim(-7.6, 7.8)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('ipt_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved ipt_mindmap.png")
