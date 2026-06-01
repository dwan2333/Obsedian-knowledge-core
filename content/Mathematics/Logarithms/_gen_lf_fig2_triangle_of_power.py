"""Generate lf_fig2_triangle_of_power.png — three triangles showing
exponent / root / log as three faces of the same b^n = a relationship.

The triangle: top vertex = exponent n, bottom-left = base b, bottom-right
= result a. Each panel hides one vertex and labels the operation that
recovers it.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = '#4a90e2'
BLUE_EDGE = '#1f4f8c'
ORANGE = '#e2924a'
ORANGE_EDGE = '#8c4f1f'
GREEN = '#7bb55c'
GREEN_EDGE = '#3d7530'
PURPLE = '#b76db4'
PURPLE_EDGE = '#6e3a6c'
TEXT = '#222222'
MUTE = '#888888'
GRID = '#e6e6e6'

fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.8))

# Vertices of each triangle (in panel coordinates):
TOP = (0.0, 1.4)
BL = (-1.0, 0.0)
BR = (1.0, 0.0)

# Triangle drawing helper
def draw_triangle(ax, missing, label_color):
    """Draw the three sides of the triangle, then label vertices.
    `missing` is one of 'top', 'bl', 'br' — the vertex to leave empty."""
    # Triangle edges
    for p, q in [(TOP, BL), (BL, BR), (BR, TOP)]:
        ax.plot([p[0], q[0]], [p[1], q[1]],
                color=TEXT, linewidth=2.4, solid_capstyle='round',
                zorder=2)

    # Vertex labels (drawn as filled circles + text)
    def vertex(pos, lbl, missing_this, face, edge):
        if missing_this:
            # Empty circle for unknown
            ax.scatter([pos[0]], [pos[1]], s=900, facecolor='white',
                       edgecolor=label_color, linewidth=2.4,
                       zorder=5, marker='o')
            ax.text(pos[0], pos[1], '?', fontsize=20, color=label_color,
                    ha='center', va='center', fontweight='bold', zorder=6)
        else:
            ax.scatter([pos[0]], [pos[1]], s=900, facecolor=face,
                       edgecolor=edge, linewidth=2.0, zorder=5)
            ax.text(pos[0], pos[1], lbl, fontsize=15, color='white',
                    ha='center', va='center', fontweight='bold', zorder=6)

    vertex(TOP, '$n$',  missing == 'top', BLUE, BLUE_EDGE)
    vertex(BL,  '$b$',  missing == 'bl',  GREEN, GREEN_EDGE)
    vertex(BR,  '$a$',  missing == 'br',  ORANGE, ORANGE_EDGE)

# ---- Panel 1: exponent unknown -> logarithm ----
ax = axes[0]
draw_triangle(ax, 'top', BLUE_EDGE)
ax.set_title('Unknown: exponent\n$\\Rightarrow$ logarithm',
             fontsize=13, pad=10, color=BLUE_EDGE, fontweight='bold')
ax.text(0, -0.65, r'$\log_b(a) = n$',
        fontsize=15, ha='center', va='center',
        color=BLUE_EDGE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3',
                  facecolor='#dceaf7', edgecolor=BLUE_EDGE, linewidth=1.4))
ax.text(0, -1.10, '"$b$ to the what equals $a$?"',
        fontsize=10, ha='center', va='center',
        color=TEXT, fontstyle='italic')

# ---- Panel 2: base unknown -> nth root ----
ax = axes[1]
draw_triangle(ax, 'bl', GREEN_EDGE)
ax.set_title('Unknown: base\n$\\Rightarrow$ $n$-th root',
             fontsize=13, pad=10, color=GREEN_EDGE, fontweight='bold')
ax.text(0, -0.65, r'$\sqrt[n]{a} = b$',
        fontsize=15, ha='center', va='center',
        color=GREEN_EDGE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3',
                  facecolor='#e3f1d8', edgecolor=GREEN_EDGE, linewidth=1.4))
ax.text(0, -1.10, '"What number to the $n$ gives $a$?"',
        fontsize=10, ha='center', va='center',
        color=TEXT, fontstyle='italic')

# ---- Panel 3: result unknown -> exponentiation ----
ax = axes[2]
draw_triangle(ax, 'br', ORANGE_EDGE)
ax.set_title('Unknown: result\n$\\Rightarrow$ exponentiation',
             fontsize=13, pad=10, color=ORANGE_EDGE, fontweight='bold')
ax.text(0, -0.65, r'$b^n = a$',
        fontsize=15, ha='center', va='center',
        color=ORANGE_EDGE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3',
                  facecolor='#f6ddc4', edgecolor=ORANGE_EDGE, linewidth=1.4))
ax.text(0, -1.10, '"$b$ to the $n$ equals what?"',
        fontsize=10, ha='center', va='center',
        color=TEXT, fontstyle='italic')

# Common limits / axes off
for ax in axes:
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.5, 2.1)
    ax.set_aspect('equal')
    ax.axis('off')

fig.suptitle('Triangle of power: one relationship, three faces',
             fontsize=14, y=1.0, color=TEXT, fontweight='bold')

plt.tight_layout()
plt.savefig('lf_fig2_triangle_of_power.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved lf_fig2_triangle_of_power.png")
