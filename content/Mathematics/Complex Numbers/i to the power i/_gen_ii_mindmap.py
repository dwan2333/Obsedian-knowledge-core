"""ii_mindmap.png — concept map for the i^i note."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13, 9.8))

cw, ch = 4.6, 2.0
ax.add_patch(mpatches.FancyBboxPatch((-cw / 2, -ch / 2), cw, ch,
             boxstyle='round,pad=0.1,rounding_size=0.3',
             facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4))
ax.text(0, 0.34, r"$i^{\,i}$", fontsize=26, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.52, r"$=e^{-\pi/2}\approx 0.2079$", fontsize=13,
        ha='center', va='center', color='white', zorder=5)

topics = [
    ("1 . The puzzle",
     "Repeated multiplication\n"
     "breaks for complex powers.\n"
     r"Define $e^x$ as its series:" "\n"
     r"$1+x+\frac{x^2}{2}+\cdots$"),
    ("2 . One value",
     r"Solve $e^x=i\Rightarrow x=\frac{\pi}{2}i$." "\n"
     r"$i^{\,i}=(e^{\pi i/2})^{i}$" "\n"
     r"$=e^{-\pi/2}\approx 0.208$." "\n"
     "Imaginary^imaginary = real!"),
    ("3 . Why (dynamics)",
     r"$\frac{d}{dt}e^{it}=i\,e^{it}$." "\n"
     "Velocity = position\n"
     r"rotated $90^\circ$ $\to$ circle" "\n"
     "(tangent $\perp$ radius)."),
    ("4 . The power $i$",
     "Outer $i$ rotates every\n"
     r"velocity $90^\circ$ more:" "\n"
     r"$e^{it}\to e^{-t}$ (decay)." "\n"
     r"Reach $e^{-\pi/2}$ at $t=\frac{\pi}{2}$."),
    ("5 . Infinitely many",
     r"$e^x=i$ has $\infty$ solutions" "\n"
     r"$x=i(\frac{\pi}{2}+2\pi k)$, so" "\n"
     r"$i^{\,i}=e^{-\pi/2-2\pi k}$:" "\n"
     r"$111.3,\;0.208,\;0.000388\dots$"),
]
palette = [
    ('#4a90e2', '#1f4f8c'), ('#e2924a', '#8c4f1f'), ('#7bb55c', '#3d7530'),
    ('#b76db4', '#6e3a6c'), ('#d4a04a', '#8c6520'),
]
angles = [pi / 2 + i * 2 * pi / 5 for i in range(5)]
radius = 6.9
bw, bh = 4.9, 2.6
for i, ((title, body), (fc, ec)) in enumerate(zip(topics, palette)):
    th = angles[i]
    x = radius * cos(th); y = radius * sin(th)
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5, zorder=1)
    ax.add_patch(mpatches.FancyBboxPatch((x - bw / 2, y - bh / 2), bw, bh,
                 boxstyle='round,pad=0.08,rounding_size=0.25',
                 facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.95, zorder=2))
    ax.text(x, y + bh / 2 - 0.38, title, fontsize=12.5, ha='center',
            va='center', color='white', fontweight='bold', zorder=3)
    ax.text(x, y - 0.32, body, fontsize=9.7, ha='center', va='center',
            color='white', zorder=3)

ax.set_title(r"$i^{\,i}$ — concept map", fontsize=15, pad=14, fontweight='bold')
ax.set_xlim(-10.6, 10.6); ax.set_ylim(-10.0, 10.2)
ax.set_aspect('equal'); ax.axis('off')
plt.tight_layout()
plt.savefig('ii_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ii_mindmap.png")
