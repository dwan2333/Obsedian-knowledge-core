"""Generate ipt_fig2_three_similar.png — the three similar triangles.

Small, medium and large right triangles redrawn at the same orientation
(right angle bottom-left, shorter leg vertical, longer leg horizontal). All are
3-4-5 shaped. Scales: small hyp = a = 3 (x0.6), medium hyp = b = 4 (x0.8),
large hyp = c = 5 (x1.0).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

GREEN = ('#8fc873', '#3d7530')
ORANGE = ('#e0a85c', '#8c5a1f')
BLUE = ('#7fb0e0', '#1f4f8c')
TEXT = '#222222'

def triangle(ax, x0, scale, face, edge, vlab, hlab, hyplab, name):
    """Right angle at (x0,0); vertical leg 3*scale, horizontal leg 4*scale."""
    vt = 3.0 * scale
    hz = 4.0 * scale
    P0 = (x0, 0.0)            # right angle (bottom-left)
    P1 = (x0 + hz, 0.0)       # bottom-right
    P2 = (x0, vt)             # top
    ax.add_patch(mpatches.Polygon([P0, P1, P2], closed=True, facecolor=face,
                 edgecolor=edge, linewidth=2.2, alpha=0.92, zorder=2))
    # right-angle marker
    r = 0.18
    ax.plot([x0 + r, x0 + r, x0], [0, r, r], color=edge, linewidth=1.2, zorder=4)
    # labels
    ax.text(x0 - 0.18, vt / 2, vlab, fontsize=15, color=TEXT, ha='right',
            va='center', fontweight='bold')
    ax.text(x0 + hz / 2, -0.22, hlab, fontsize=15, color=TEXT, ha='center',
            va='top', fontweight='bold')
    # hypotenuse label (mid of P1-P2, offset outward up-right)
    mx, my = (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2
    ax.text(mx + 0.18, my + 0.12, hyplab, fontsize=16, color=edge, ha='left',
            va='bottom', fontweight='bold')
    ax.text(x0 + hz / 2, vt + 0.55, name, fontsize=12, color=edge,
            ha='center', va='bottom', style='italic')

fig, ax = plt.subplots(figsize=(13, 5.4))

triangle(ax, 0.0, 0.6, GREEN[0], GREEN[1], r"$c_1$", r"$h$", r"$a$", "small")
triangle(ax, 3.6, 0.8, ORANGE[0], ORANGE[1], r"$h$", r"$c_2$", r"$b$", "medium")
triangle(ax, 8.0, 1.0, BLUE[0], BLUE[1], r"$a$", r"$b$", r"$c$", "large")

# similarity tildes
ax.text(3.0, 1.0, r"$\sim$", fontsize=26, color=TEXT, ha='center', va='center')
ax.text(7.2, 1.3, r"$\sim$", fontsize=26, color=TEXT, ha='center', va='center')

# the two proportions
ax.text(6.0, -1.9,
        r"$\dfrac{a}{c_1} = \dfrac{c}{a}\ \Rightarrow\ a^2 = c\,c_1"
        r"\qquad\qquad \dfrac{b}{c_2} = \dfrac{c}{b}\ \Rightarrow\ b^2 = c\,c_2$",
        fontsize=16, color=TEXT, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))

ax.set_title("Redraw the three similar triangles in the same orientation",
             fontsize=14, pad=12, color=TEXT)
ax.set_xlim(-1.0, 12.6)
ax.set_ylim(-2.9, 4.1)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('ipt_fig2_three_similar.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved ipt_fig2_three_similar.png")
