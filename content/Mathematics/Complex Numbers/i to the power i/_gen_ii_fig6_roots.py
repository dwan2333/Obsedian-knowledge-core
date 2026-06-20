"""ii_fig6_roots.png — fractional powers are multi-valued: the n distinct n-th
roots sit at n evenly-spaced points on a circle."""
import matplotlib.pyplot as plt
import numpy as np

BLUE='#1f4f8c'; RED='#a83227'; GREY='#cccccc'; TEXT='#222222'
fig,(axL,axR)=plt.subplots(1,2,figsize=(12.6,6.3))

def plane(ax,R,pts,labels,title,col):
    tt=np.linspace(0,2*np.pi,400)
    ax.plot(R*np.cos(tt),R*np.sin(tt),color=GREY,lw=1.4,ls='--')
    ax.axhline(0,color='#bbb',lw=0.8); ax.axvline(0,color='#bbb',lw=0.8)
    for (z,lab) in zip(pts,labels):
        ax.plot([0,z.real],[0,z.imag],color=col,lw=1.2,alpha=0.45)
        ax.scatter([z.real],[z.imag],s=110,color=col,edgecolor='white',zorder=5)
        # label offset outward
        a=np.angle(z); ax.text(z.real+0.13*np.cos(a)*R/abs(z) if abs(z)>1e-9 else 0.2,
                               z.imag+0.16*np.sin(a)*R/abs(z) if abs(z)>1e-9 else 0.2,
                               lab,fontsize=12.5,color=col,fontweight='bold',
                               ha='center',va='center')
    lim=R*1.5
    ax.set_xlim(-lim,lim); ax.set_ylim(-lim,lim); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(title,fontsize=13,fontweight='bold',color=TEXT,pad=8)

# left: 4th roots of 16  -> 2, 2i, -2, -2i
R=2.0
pts=[2+0j,0+2j,-2+0j,0-2j]
labs=[r'$2$',r'$2i$',r'$-2$',r'$-2i$']
plane(axL,R,pts,labs,r"$\sqrt[4]{16}$ : four solutions of $x^4=16$",BLUE)

# right: four values of 2^(1/4) = 2^(1/4)*{1,i,-1,-i}
r=2**0.25
pts=[r*1,r*1j,-r*1,-r*1j]
labs=[r'$\sqrt[4]{2}$',r'$\sqrt[4]{2}\,i$',r'$-\sqrt[4]{2}$',r'$-\sqrt[4]{2}\,i$']
plane(axR,r,pts,labs,r"$2^{1/4}$ : four values, $\sqrt[4]{2}\cdot\{1,i,-1,-i\}$",RED)

fig.suptitle(r"Fractional powers are multi-valued — the $n$-th roots are $n$ evenly-spaced points",
             fontsize=14,fontweight='bold',y=1.0)
plt.tight_layout()
plt.savefig('ii_fig6_roots.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ii_fig6_roots.png")
