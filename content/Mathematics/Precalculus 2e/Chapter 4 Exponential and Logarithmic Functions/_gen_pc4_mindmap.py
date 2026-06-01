"""Generate pc4_mindmap.png — Chapter 4 (Exp/Log Functions) concept map.

Center: chapter title. 8 surrounding nodes for sections 4.1-4.8, arranged
radially. Same paper-aesthetic palette and layout pattern as the other
chapter mindmaps in the vault (sp_mindmap.py, lf_mindmap.py).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi

fig, ax = plt.subplots(figsize=(13, 10))

# Central hub
center_w, center_h = 3.6, 1.6
hub = mpatches.FancyBboxPatch(
    (-center_w/2, -center_h/2), center_w, center_h,
    boxstyle='round,pad=0.1,rounding_size=0.3',
    facecolor='#1f4f8c', edgecolor='#0f2f5c', linewidth=2.0, zorder=4
)
ax.add_patch(hub)
ax.text(0, 0.25, 'Chapter 4',
        fontsize=17, ha='center', va='center',
        color='white', fontweight='bold', zorder=5)
ax.text(0, -0.30, 'Exp & Log Functions',
        fontsize=13, ha='center', va='center',
        color='white', zorder=5)

# 8 satellite nodes for 4.1 through 4.8
topics = [
    ('4.1 Exponential\nFunctions',
     'growth/decay,\ne, compound\ninterest'),
    ('4.2 Graphs of\nExponentials',
     'parent shapes,\nshifts, reflections,\nstretches'),
    ('4.3 Logarithmic\nFunctions',
     'inverse of $b^x$;\n$\\log_b x = y$\n$\\Leftrightarrow b^y = x$'),
    ('4.4 Graphs of\nLogarithms',
     'mirror of exp;\nshifts, stretches,\ndomain $> 0$'),
    ('4.5 Logarithm\nProperties',
     'product, quotient,\npower, change-of-\nbase'),
    ('4.6 Exp & Log\nEquations',
     'one-to-one,\ntaking logs,\nextraneous solutions'),
    ('4.7 Models',
     'half-life,\nNewton cooling,\nlogistic growth'),
    ('4.8 Fitting\nModels to Data',
     'exponential\nregression,\nlog regression'),
]

palette = [
    ('#e2924a', '#8c4f1f'),
    ('#4a90e2', '#1f4f8c'),
    ('#7bb55c', '#3d7530'),
    ('#b76db4', '#6e3a6c'),
    ('#d4a04a', '#8c6520'),
    ('#5e7c5e', '#3d5630'),
    ('#b88455', '#7a5535'),
    ('#9aa0a8', '#5a5d6e'),
]

n = len(topics)
radius = 5.0
box_w, box_h = 3.0, 1.95

for i, ((title, body), (fc, ec)) in enumerate(zip(topics, palette)):
    theta = pi/2 - i * (2 * pi / n)
    x = radius * cos(theta)
    y = radius * sin(theta)

    # connector
    ax.plot([0, x], [0, y], color='#bbbbbb', linewidth=1.4, zorder=1)

    # node box
    box = mpatches.FancyBboxPatch(
        (x - box_w/2, y - box_h/2), box_w, box_h,
        boxstyle='round,pad=0.08,rounding_size=0.25',
        facecolor=fc, edgecolor=ec, linewidth=1.8, alpha=0.94, zorder=2
    )
    ax.add_patch(box)

    # title (bold)
    ax.text(x, y + box_h/2 - 0.35, title,
            fontsize=11, ha='center', va='center',
            color='white', fontweight='bold', zorder=3)
    # body
    ax.text(x, y - 0.22, body,
            fontsize=9.5, ha='center', va='center',
            color='white', zorder=3)

ax.set_title('Precalculus 2e — Chapter 4 concept map',
             fontsize=15, pad=10, fontweight='bold')

ax.set_xlim(-7.8, 7.8)
ax.set_ylim(-7.4, 7.4)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('pc4_mindmap.png', dpi=220, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved pc4_mindmap.png')
