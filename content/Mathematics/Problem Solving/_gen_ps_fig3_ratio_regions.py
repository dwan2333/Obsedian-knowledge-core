"""ps_fig3_ratio_regions.png — the unit square; floor(x/y) is EVEN on the green
regions (above y=x, and the strips for 2,4,6,...), whose total area is 1-ln2/2."""
import matplotlib.pyplot as plt
import numpy as np

GREEN='#7bb55c'; GED='#3d7530'; RED='#d08070'; GREY='#888'; TEXT='#222'
fig,ax=plt.subplots(figsize=(7.6,7.6))
xs=np.linspace(0,1,400)

# even regions (floor = 0,2,4,...) shaded green; odd (1,3,5..) light red
# floor=0: y>x  (top triangle)
ax.fill_between(xs, xs, 1, color=GREEN, alpha=0.55, lw=0)
# strips: floor=n on x/(n+1) < y <= x/n  -> between y=x/(n+1) and y=x/n
for n in range(1,12):
    lo=xs/(n+1); hi=xs/n
    col=GREEN if n%2==0 else RED
    al=0.55 if n%2==0 else 0.35
    ax.fill_between(xs, lo, hi, color=col, alpha=al, lw=0)
# boundary lines y = x/n
for n in range(1,8):
    ax.plot(xs, xs/n, color=GREY, lw=0.9, alpha=0.7)
    if n<=4:
        ax.text(1.005, 1/n, (r'$y=x$' if n==1 else rf'$y=\frac{{x}}{{{n}}}$'),
                fontsize=10, color=GREY, va='center')

ax.text(0.30,0.74,r'$\lfloor x/y\rfloor=0$',fontsize=12,color=GED,fontweight='bold',rotation=0)
ax.text(0.74,0.30,r'$=1$',fontsize=10,color='#a83227',rotation=33)
ax.text(0.82,0.205,r'$=2$',fontsize=10,color=GED,rotation=22)
ax.set_xlim(0,1.16); ax.set_ylim(0,1.04); ax.set_aspect('equal')
ax.set_xlabel('$x$',fontsize=12); ax.set_ylabel('$y$',fontsize=12)
ax.set_xticks([0,0.5,1]); ax.set_yticks([0,0.5,1])
ax.set_title(r"$\lfloor x/y\rfloor$ is even on the green regions — total area $=1-\frac{1}{2}\ln 2\approx0.6534$",
             fontsize=12.5,fontweight='bold',color=TEXT,pad=10)
ax.spines[['top','right']].set_visible(False)
# legend
import matplotlib.patches as mp
ax.legend(handles=[mp.Patch(color=GREEN,alpha=0.55,label='even floor (0,2,4,...)'),
                   mp.Patch(color=RED,alpha=0.35,label='odd floor (1,3,5,...)')],
          loc='upper right',fontsize=9.5,framealpha=0.95)
plt.tight_layout()
plt.savefig('ps_fig3_ratio_regions.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ps_fig3_ratio_regions.png")
