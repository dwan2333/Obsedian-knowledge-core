"""Generate pyth_fig1_rearrangement.png — the rearrangement proof.

Four identical 3-4-5 right triangles packed two ways inside a square of side
A+B = 7. Left panel: hypotenuses face inward, leaving a tilted C^2 hole.
Right panel: triangles re-packed into two rectangles, leaving an A^2 and a B^2
hole. Same four triangles => same uncovered area => A^2 + B^2 = C^2.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

A, B = 3.0, 4.0          # legs
S = A + B                # big square side = 7
TRI = ('#e0746a', '#a83227')      # red triangle face / edge
CSQ = ('#7fb0e0', '#1f4f8c')      # C^2 square (blue)
ASQ = ('#8fc873', '#3d7530')      # A^2 square (green)
BSQ = ('#e0a85c', '#8c5a1f')      # B^2 square (orange)
TEXT = '#222222'

fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 6.6))

def draw_square_border(ax):
    ax.add_patch(mpatches.Rectangle((0, 0), S, S, fill=False,
                 edgecolor='#555555', linewidth=2.0, zorder=5))

def tri(ax, pts):
    ax.add_patch(mpatches.Polygon(pts, closed=True, facecolor=TRI[0],
                 edgecolor=TRI[1], linewidth=1.6, alpha=0.95, zorder=3))

# ---- LEFT PANEL: tilted C^2 hole ----
draw_square_border(axL)
# inner tilted square C^2 (blue)
inner = [(A, 0), (S, A), (S - A, S), (0, S - A)]   # (3,0),(7,3),(4,7),(0,4)
axL.add_patch(mpatches.Polygon(inner, closed=True, facecolor=CSQ[0],
              edgecolor=CSQ[1], linewidth=2.0, zorder=2))
# four corner triangles
tri(axL, [(A, 0), (S, 0), (S, A)])          # bottom-right
tri(axL, [(S, A), (S, S), (S - A, S)])      # top-right
tri(axL, [(S - A, S), (0, S), (0, S - A)])  # top-left
tri(axL, [(0, S - A), (0, 0), (A, 0)])      # bottom-left
axL.text(S / 2, S / 2, r"$C^2$", fontsize=26, ha='center', va='center',
         color='white', fontweight='bold', zorder=4)
axL.set_title("Four triangles around a tilted hole", fontsize=13, color=TEXT)

# ---- RIGHT PANEL: A^2 and B^2 holes ----
draw_square_border(axR)
# B^2 square (side B=4) bottom-left, orange
axR.add_patch(mpatches.Rectangle((0, 0), B, B, facecolor=BSQ[0],
              edgecolor=BSQ[1], linewidth=2.0, zorder=2))
# A^2 square (side A=3) top-right, green
axR.add_patch(mpatches.Rectangle((B, B), A, A, facecolor=ASQ[0],
              edgecolor=ASQ[1], linewidth=2.0, zorder=2))
# bottom-right rectangle (B..S x 0..B) split into two triangles
tri(axR, [(B, 0), (S, 0), (S, B)])
tri(axR, [(B, 0), (S, B), (B, B)])
# top-left rectangle (0..B x B..S) split into two triangles
tri(axR, [(0, B), (B, B), (B, S)])
tri(axR, [(0, B), (B, S), (0, S)])
axR.text(B / 2, B / 2, r"$B^2$", fontsize=24, ha='center', va='center',
         color='white', fontweight='bold', zorder=4)
axR.text(B + A / 2, B + A / 2, r"$A^2$", fontsize=20, ha='center', va='center',
         color='white', fontweight='bold', zorder=4)
axR.set_title("Same triangles re-packed: two holes", fontsize=13, color=TEXT)

for ax in (axL, axR):
    ax.set_xlim(-0.6, S + 0.6)
    ax.set_ylim(-0.6, S + 0.6)
    ax.set_aspect('equal')
    ax.axis('off')

fig.suptitle(r"Uncovered area can't change  $\Rightarrow\;\; A^2 + B^2 = C^2$",
             fontsize=17, fontweight='bold', color=TEXT, y=0.04)
plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig('pyth_fig1_rearrangement.png', dpi=220,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Saved pyth_fig1_rearrangement.png")
