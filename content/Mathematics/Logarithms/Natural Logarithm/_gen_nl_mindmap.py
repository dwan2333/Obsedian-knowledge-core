"""Generate nl_mindmap.png — concept map for The Natural Logarithm note."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(12.5, 9.4))

cw, ch = 4.4, 1.8
center = mpatches.FancyBboxPatch(
    (-cw / 2, -ch / 2), cw, ch,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4)
ax.add_patch(center)
ax.text(0, 0.32, r"$\ln x = y \Leftrightarrow e^y = x$", fontsize=17,
        ha='center', va='center', color='white', fontweight='bold', zorder=5)
ax.text(0, -0.40, "Why is it NATURAL?", fontsize=12.5, ha='center',
        va='center', color='white', zorder=5)

topics = [
    ("1. What ln is",
     r"$\ln x$: '$e$ to the what?'" "\n"
     r"$\ln(10)\approx 2.3$." "\n"
     "The motivating question:\n"
     "why THIS base?"),
    ("2. Hidden in primes",
     "Prime density near $N$\n"
     r"$\approx 1/\ln(N)$ (PNT)." "\n"
     "Prime-power 'game' on\n"
     r"series $\to \ln$ of the sum."),
    ("3. Hidden in series",
     r"$1-\frac{1}{2}+\frac{1}{3}-\cdots=\ln 2$." "\n"
     "Harmonic series diverges\n"
     "(block proof) but grows\n"
     r"like $\ln(N)+\gamma$."),
    ("4. What e really is",
     r"$e^{rx}$, $A^x$, $\pi^{rx}$ all" "\n"
     "sweep the same family.\n"
     r"$e$ is a convention; it's 'right'" "\n"
     r"because $\frac{d}{dx}e^x=e^x$."),
]

palette = [
    ('#e2924a', '#8c4f1f'),
    ('#7bb55c', '#3d7530'),
    ('#b76db4', '#6e3a6c'),
    ('#4a90e2', '#1f4f8c'),
]

angles = [pi / 4, -pi / 4, -3 * pi / 4, 3 * pi / 4]   # NE, SE, SW, NW
radius = 5.5
bw, bh = 4.3, 2.3
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
    ax.text(x, y - 0.22, body, fontsize=9.8, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("The Natural Logarithm — concept map", fontsize=15, pad=10,
             fontweight='bold')
ax.set_xlim(-8.6, 8.6)
ax.set_ylim(-8.0, 8.2)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('nl_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved nl_mindmap.png")
