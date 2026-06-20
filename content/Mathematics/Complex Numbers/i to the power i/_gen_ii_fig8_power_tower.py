"""ii_fig8_power_tower.png — the power tower i^i^i^... = orbit of a_{n+1}=i^{a_n}
(principal branch) spirals in the complex plane to the fixed point 0.4383+0.3606i."""
import matplotlib.pyplot as plt
import numpy as np
import cmath, math

BLUE='#1f4f8c'; RED='#a83227'; GREY='#cccccc'; TEXT='#222222'
a=1+0j; orbit=[a]
for _ in range(70):
    a=cmath.exp(1j*math.pi/2*a); orbit.append(a)
xs=[z.real for z in orbit]; ys=[z.imag for z in orbit]
fp=orbit[-1]

fig,ax=plt.subplots(figsize=(8.6,8))
tt=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(tt),np.sin(tt),color=GREY,lw=1.2,ls='--')
ax.axhline(0,color='#bbb',lw=0.8); ax.axvline(0,color='#bbb',lw=0.8)

# orbit path
ax.plot(xs,ys,color=BLUE,lw=1.3,alpha=0.6,zorder=2)
ax.scatter(xs[:14],ys[:14],s=24,color=BLUE,zorder=3,edgecolor='white',linewidth=0.5)
# label the first few rungs
for i,lab in [(0,r'$a_0=1$'),(1,r'$i$'),(2,r'$i^i=0.208$')]:
    z=orbit[i]
    ax.annotate(lab,xy=(z.real,z.imag),xytext=(z.real+0.12,z.imag+0.12),
                fontsize=11,color=BLUE)
# fixed point
ax.scatter([fp.real],[fp.imag],s=240,marker='*',color=RED,edgecolor='white',zorder=6)
ax.annotate(r'converges to $\approx 0.4383+0.3606\,i$',xy=(fp.real,fp.imag),
            xytext=(fp.real+0.35,fp.imag-0.45),fontsize=12.5,color=RED,fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.6))
ax.text(-1.15,1.28,r'$a_{n+1}=i^{\,a_n}=\exp(\frac{\pi}{2}\,i\,a_n)$',
        fontsize=13,color=TEXT)
ax.set_title(r"The power tower $i^{i^{i^{\cdot^{\cdot}}}}$ spirals to a fixed point",
             fontsize=13.5,fontweight='bold',color=TEXT,pad=8)
ax.set_xlim(-1.25,1.45); ax.set_ylim(-0.35,1.45); ax.set_aspect('equal'); ax.axis('off')
plt.tight_layout()
plt.savefig('ii_fig8_power_tower.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ii_fig8_power_tower.png")
