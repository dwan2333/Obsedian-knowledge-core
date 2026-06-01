"""Generate lf_mindmap.png — concept map for Logarithm Fundamentals.

Central node = log_b(a) intuition. Six surrounding nodes covering:
1. Zero-counting intuition, 2. Triangle of power, 3. Product / power rules,
4. No log(a+b), 5. Log scales (Richter / COVID), 6. Change of base.
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
ax.text(0, 0.35, r"$\log_b(a) = n \Leftrightarrow b^n = a$",
        fontsize=15, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.30, "Log = the missing exponent",
        fontsize=11.5, ha='center', va='center',
        color='white', zorder=5)

topics = [
    ("1. Zero-counting",
     r"$\log_{10}(10^n) = n$" "\n"
     "counts zeros" "\n"
     "Multiplicative $\\to$ additive" "\n"
     "This is the whole game"),
    ("2. Triangle of power",
     "Base $b$, exp $n$, result $a$" "\n"
     "$b^n = a$" "\n"
     "Hide any vertex $\\to$" "\n"
     "log, root, or exponent"),
    ("3. Product / power",
     r"$\log(ab) = \log a + \log b$" "\n"
     r"$\log(a^n) = n \log a$" "\n"
     "From intuition, not memorization:" "\n"
     "zeros add when you multiply"),
    ("4. No $\\log(a+b)$",
     r"Adding INSIDE doesn't work" "\n"
     r"$\log(a+b) \approx \log(\max(a,b))$" "\n"
     "Logs are built around" "\n"
     "multiplication, not addition"),
    ("5. Log scales in nature",
     "Richter: $+1 = \\times 32$" "\n"
     "COVID: $\\times 10$ every 16 d" "\n"
     "Log scale flattens" "\n"
     "exponentials to lines"),
    ("6. Change of base",
     r"$\log_b(a) = \frac{\log_c(a)}{\log_c(b)}$" "\n"
     r"$\log_{10}(2) \approx 0.3$" "\n"
     "from $2^{10} \\approx 10^3$" "\n"
     "Bridge CS $\\leftrightarrow$ engineering"),
]

node_palette = [
    ('#e2924a', '#8c4f1f'),  # orange
    ('#4a90e2', '#1f4f8c'),  # blue
    ('#7bb55c', '#3d7530'),  # green
    ('#b76db4', '#6e3a6c'),  # purple
    ('#d4a04a', '#8c6520'),  # yellow
    ('#cd6680', '#7a3030'),  # red
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

ax.set_title("Logarithm Fundamentals — concept map",
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-8.6, 8.6)
ax.set_ylim(-8.4, 8.4)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('lf_mindmap.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_mindmap.png")
