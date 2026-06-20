"""ps_fig4_histogram.png — distribution of floor(x/y): P(=n). Even bars (green)
sum to 1-ln2/2 = 0.6534; odd bars (red) sum to ln2/2 = 0.3466 (= the 'mistake')."""
import matplotlib.pyplot as plt
import numpy as np, math

GREEN='#3d7530'; RED='#a83227'; TEXT='#222'
def P(n):
    return 0.5 if n==0 else 1.0/(2*n*(n+1))
ns=list(range(0,11))
ps=[P(n) for n in ns]
cols=[GREEN if n%2==0 else RED for n in ns]
fig,ax=plt.subplots(figsize=(10,5.6))
ax.bar(ns,ps,color=cols,edgecolor='white',width=0.82)
for n,p in zip(ns,ps):
    if p>0.012: ax.text(n,p+0.008,f'{p:.3f}',ha='center',fontsize=9,color=TEXT)
even=1-0.5*math.log(2); odd=0.5*math.log(2)
ax.text(5.2,0.40,"even floor (0,2,4,...)\n"+r"sum $=1-\frac{1}{2}\ln2="+f"{even:.4f}$",
        color=GREEN,fontsize=12,fontweight='bold')
ax.text(5.2,0.27,"odd floor (1,3,5,...)\n"+r"sum $=\frac{1}{2}\ln2="+f"{odd:.4f}$"+"  ← the tempting wrong answer",
        color=RED,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$n=\lfloor x/y\rfloor$',fontsize=12)
ax.set_ylabel(r'$P(\lfloor x/y\rfloor=n)$',fontsize=12)
ax.set_title(r"Distribution of $\lfloor x/y\rfloor$ for $x,y$ uniform on $[0,1]$ (Python: even $\approx0.65294$)",
             fontsize=12.5,fontweight='bold',color=TEXT,pad=10)
ax.set_xticks(ns); ax.set_ylim(0,0.56)
ax.spines[['top','right']].set_visible(False); ax.grid(axis='y',color='#eee'); ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('ps_fig4_histogram.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ps_fig4_histogram.png")
