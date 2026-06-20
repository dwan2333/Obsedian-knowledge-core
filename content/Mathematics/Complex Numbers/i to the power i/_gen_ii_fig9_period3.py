"""ii_fig9_period3.png — choosing a different branch (i = e^{i 5pi/2}) makes the
same power tower bounce in a period-3 cycle: 'period 3 implies chaos'."""
import matplotlib.pyplot as plt
import numpy as np
import cmath, math

BLUE='#1f4f8c'; PURPLE='#6e3a6c'; GREY='#cccccc'; TEXT='#222222'
# principal branch orbit (for contrast, left)
def orbit(coef,n,keep=None):
    a=1+0j; out=[a]
    for k in range(n):
        a=cmath.exp(1j*coef*a); out.append(a)
    return out
prin=orbit(math.pi/2,70)
per3=orbit(5*math.pi/2,400)
cycle=per3[-9:]   # settled 3-cycle (repeats)

fig,(axL,axR)=plt.subplots(1,2,figsize=(13,6.4))
for ax in (axL,axR):
    tt=np.linspace(0,2*np.pi,300)
    ax.plot(np.cos(tt),np.sin(tt),color=GREY,lw=1.1,ls='--')
    ax.axhline(0,color='#bbb',lw=0.7); ax.axvline(0,color='#bbb',lw=0.7)
    ax.set_aspect('equal'); ax.axis('off')

# left: principal -> converges
xs=[z.real for z in prin]; ys=[z.imag for z in prin]
axL.plot(xs,ys,color=BLUE,lw=1.2,alpha=0.6)
axL.scatter([prin[-1].real],[prin[-1].imag],s=200,marker='*',color=BLUE,edgecolor='white',zorder=6)
axL.set_title(r"Principal branch $i=e^{i\pi/2}$ : converges",fontsize=12.5,fontweight='bold',color=BLUE)
axL.set_xlim(-1.2,1.4); axL.set_ylim(-0.3,1.4)

# right: 5pi/2 branch -> period-3 cycle
distinct=[]
for z in cycle:
    if not any(abs(z-d)<1e-3 for d in distinct): distinct.append(z)
cx=[z.real for z in distinct]; cy=[z.imag for z in distinct]
# triangle connecting the 3 cycle points
order=distinct+[distinct[0]]
axR.plot([z.real for z in order],[z.imag for z in order],color=PURPLE,lw=1.6,ls='-',alpha=0.7)
axR.scatter(cx,cy,s=170,color=PURPLE,edgecolor='white',zorder=6)
for i,z in enumerate(distinct):
    axR.annotate(f'%.2f%+.2fi'%(z.real,z.imag),xy=(z.real,z.imag),
                 xytext=(z.real+0.05,z.imag+0.08),fontsize=10.5,color=PURPLE,fontweight='bold')
axR.set_title(r"Branch $i=e^{i5\pi/2}$ : period-3 cycle (chaos)",fontsize=12.5,fontweight='bold',color=PURPLE)
axR.set_xlim(-0.25,1.25); axR.set_ylim(-0.2,1.15)

fig.suptitle(r"Same tower, different branch of $i^x$ — convergence vs. a period-3 orbit",
             fontsize=14,fontweight='bold',y=1.0)
plt.tight_layout()
plt.savefig('ii_fig9_period3.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ii_fig9_period3.png")
