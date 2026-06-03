"""Generate nl_fig3_grouping_proof.png — harmonic series diverges (block proof).

Group the harmonic terms into blocks of size 2, 4, 8, 16. Each block is bounded
below by (#terms) x (smallest term) = 1/2, so the sum exceeds 1 + 1/2 + 1/2 + ...
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#1f4f8c'
GREEN_E = '#3d7530'
TEXT = '#333333'
GREY = '#777777'

fig, ax = plt.subplots(figsize=(12.4, 5.2))

# The terms laid out along a row.
groups = [
    (["$1$"], None, None),
    ([r"$\frac{1}{2}$"], None, None),
    ([r"$\frac{1}{3}$", r"$\frac{1}{4}$"], r"$>2\cdot\frac{1}{4}$", r"$\frac{1}{2}$"),
    ([r"$\frac{1}{5}$", r"$\frac{1}{6}$", r"$\frac{1}{7}$", r"$\frac{1}{8}$"], r"$>4\cdot\frac{1}{8}$", r"$\frac{1}{2}$"),
    ([r"$\frac{1}{9}$", r"$\cdots$", r"$\frac{1}{16}$"], r"$>8\cdot\frac{1}{16}$", r"$\frac{1}{2}$"),
    ([r"$\frac{1}{17}$", r"$\cdots$", r"$\frac{1}{32}$"], r"$>16\cdot\frac{1}{32}$", r"$\frac{1}{2}$"),
]

x = 0.0
gap = 0.55
term_w = 0.95
y_terms = 2.0
for terms, bound, half in groups:
    x0 = x
    for t in terms:
        ax.text(x + term_w / 2, y_terms, t, ha='center', va='center',
                fontsize=15, color=TEXT)
        if t != terms[-1]:
            ax.text(x + term_w, y_terms, "+", ha='center', va='center',
                    fontsize=13, color=GREY)
        x += term_w + 0.32
    x1 = x - 0.32
    # bracket + bound for the multi-term blocks
    if bound is not None:
        ybr = y_terms - 0.55
        ax.plot([x0 + 0.1, x0 + 0.1, x1 - 0.1, x1 - 0.1],
                [ybr + 0.12, ybr, ybr, ybr + 0.12], color=GREEN_E, lw=1.8)
        ax.text((x0 + x1) / 2, ybr - 0.34, bound, ha='center', va='center',
                fontsize=13, color=GREEN_E)
        ax.text((x0 + x1) / 2, ybr - 0.92, "$=$ " + half, ha='center',
                va='center', fontsize=14, color=GREEN_E, fontweight='bold')
    x += gap
    # plus sign between groups
    if (terms, bound, half) != groups[-1]:
        ax.text(x - gap / 2 - 0.1, y_terms, "+", ha='center', va='center',
                fontsize=14, color=GREY)

ax.text(x + 0.2, y_terms, r"$+\;\cdots$", ha='left', va='center',
        fontsize=15, color=TEXT)

# Conclusion line.
ax.text(x / 2, -0.30,
        r"$\Rightarrow\;\; 1 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \cdots \;=\; \infty$",
        ha='center', va='center', fontsize=17, color=TEXT, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff8dc',
                  edgecolor='#aa8b3a', linewidth=1.6))
ax.text(x / 2, -0.95, "infinitely many halves — the sum grows without bound",
        ha='center', va='center', fontsize=10.5, color=GREY, style='italic')

ax.set_title(r"Grouping proof: the harmonic series diverges (each block $>\frac{1}{2}$)",
             fontsize=14, color=TEXT, pad=10)
ax.set_xlim(-0.4, x + 1.4)
ax.set_ylim(-1.2, 2.7)
ax.axis('off')
plt.tight_layout()
plt.savefig('nl_fig3_grouping_proof.png', dpi=220, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved nl_fig3_grouping_proof.png")
