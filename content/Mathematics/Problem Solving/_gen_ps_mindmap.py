"""ps_mindmap.png - concept map: 9 problem-solving tips (grouped) + 3 worked proofs."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13.5, 10))
cw, ch = 6.2, 2.0
ax.add_patch(mpatches.FancyBboxPatch((-cw/2, -ch/2), cw, ch,
             boxstyle='round,pad=0.1,rounding_size=0.3',
             facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4))
ax.text(0, 0.34, "Better Problem Solving", fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.46, "9 tips - 3 worked proofs", fontsize=12, ha='center', va='center',
        color='white', zorder=5)

nodes = [
 ("Understand the setup",
  "1 . Use defining features\n2 . Give meaningful names\n3 . Leverage symmetry"),
 ("Reframe it",
  "4 . Describe one object\n     two different ways\n5 . Draw it; numbers\n     into coordinates\n6 . Ask a simpler version"),
 ("Verify & practice",
  "7 . Read & think a LOT\n     (insight = pattern\n     recognition)\n8 . Gut-check the answer\n9 . Learn programming"),
 ("Inscribed Angle Theorem",
  "Central angle is twice\nthe inscribed angle:\n" + r"$\theta_L=2\theta_S$" + "\n(isosceles + symmetry)"),
 ("Geometry of cosine-squared",
  "One length, two ways:\n" + r"$\cos^2\theta=\frac{1}{2}(1+\cos 2\theta)$" + "\nvia Thales + projection"),
 ("Even floor of  x / y ?",
  "Coords + simpler cases\n+ a series. Answer\n" + r"$1-\frac{1}{2}\ln 2\approx0.6534$" + "\n" + r"(gut-check caught $\frac{1}{2}\ln 2$)"),
]
palette = [('#4a90e2','#1f4f8c'), ('#e2924a','#8c4f1f'), ('#7bb55c','#3d7530'),
           ('#b76db4','#6e3a6c'), ('#d4a04a','#8c6520'), ('#5bb1b0','#2d6470')]
angles = [pi/2 + i*2*pi/6 for i in range(6)]
radius = 7.0; bw, bh = 5.3, 2.9
for i, ((title, body), (fc, ec)) in enumerate(zip(nodes, palette)):
    th = angles[i]; x = radius*cos(th); y = radius*sin(th)
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.5, zorder=1)
    ax.add_patch(mpatches.FancyBboxPatch((x-bw/2, y-bh/2), bw, bh,
                 boxstyle='round,pad=0.08,rounding_size=0.25',
                 facecolor=fc, edgecolor=ec, linewidth=2.0, alpha=0.95, zorder=2))
    ax.text(x, y+bh/2-0.40, title, fontsize=11.3, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    ax.text(x, y-0.36, body, fontsize=9.6, ha='center', va='center', color='white', zorder=3)
ax.set_title("Tips to Be a Better Problem Solver - concept map", fontsize=15, pad=14, fontweight='bold')
ax.set_xlim(-11, 11); ax.set_ylim(-10.5, 10.5); ax.set_aspect('equal'); ax.axis('off')
plt.tight_layout()
plt.savefig('ps_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close(); print("Saved ps_mindmap.png")
