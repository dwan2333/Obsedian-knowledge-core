"""Generate iir_mindmap.png — concept map for Imaginary Interest & Continuous Rotation.

Central node = $r = i$ -> $e^{it}$ = rotation. Five surrounding nodes covering:
1. The puzzle (imaginary rate), 2. Compound interest math, 3. The number e,
4. Imaginary input + rotation, 5. e^{it} = unit circle.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13.5, 10))

# Center node
center_w, center_h = 4.6, 1.9
center = mpatches.FancyBboxPatch(
    (-center_w / 2, -center_h / 2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(center)
ax.text(0, 0.35, r"$r = i\;\Rightarrow\; M(t) = e^{it}$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.30, "Imaginary interest is rotation",
        fontsize=11.5, ha='center', va='center',
        color='white', zorder=5)

topics = [
    ("1. The puzzle",
     r"Bank pays $r = \sqrt{-1}$" "\n"
     "annual interest. Sounds" "\n"
     "absurd; the right read" "\n"
     "is rotation, not growth"),
    ("2. Compound interest",
     r"$\Delta M = r \Delta t \cdot M$" "\n"
     r"$M(T) = M(0)(1{+}r\Delta t)^n$" "\n"
     "Same constant multiplier" "\n"
     "applied $n$ times $\\to$ growth"),
    ("3. The number $e$",
     r"$e = \lim_{n\to\infty}(1+1/n)^n$" "\n"
     "$\\approx 2.71828$" "\n"
     r"$M(T) = M(0)\, e^{rT}$" "\n"
     "continuous compounding"),
    ("4. Imaginary input",
     r"$\Delta M = i\Delta t\cdot M$" "\n"
     r"$\Rightarrow$ change perpendicular" "\n"
     "to current value" "\n"
     "Discrete: spiral outward"),
    ("5. Continuous limit",
     r"$\Delta t \to 0$" "\n"
     "perpendicular nudges don't" "\n"
     "grow magnitude $\\to$ circle" "\n"
     r"$e^{i\pi}{=}{-1}$ in $\pi$ yrs"),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # orange
    ('#4a90e2', '#1f4f8c'),  # blue
    ('#7bb55c', '#3d7530'),  # green
    ('#b76db4', '#6e3a6c'),  # purple
    ('#d4a04a', '#8c6520'),  # yellow
]

n_topics = len(topics)
radius = 5.8
box_w, box_h = 4.0, 2.2

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, node_palette)):
    theta = pi / 2 - i * (2 * pi / n_topics)
    x = radius * cos(theta)
    y = radius * sin(theta)

    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5,
            linestyle='-', zorder=1)
    box = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.94, zorder=2
    )
    ax.add_patch(box)
    ax.text(x, y + box_h / 2 - 0.32, title,
            fontsize=12, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.25, body,
            fontsize=10, ha='center', va='center',
            color='white', zorder=3)

ax.set_title("Imaginary Interest and Continuous Rotation — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-8.6, 8.6)
ax.set_ylim(-8.4, 8.4)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('iir_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved iir_mindmap.png")
