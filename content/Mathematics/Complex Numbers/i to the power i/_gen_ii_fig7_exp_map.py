"""ii_fig7_exp_map.png — how exp(r x) reshapes the plane (here r=ln2, i.e. 2^x):
real inputs -> a log-spaced ray along the positive reals; imaginary inputs ->
the unit circle. When r turns imaginary the two roles swap."""
import matplotlib.pyplot as plt
import numpy as np

BLUE='#1f4f8c'; RED='#a83227'; GREEN='#3d7530'; GREY='#cccccc'; TEXT='#222222'
r=np.log(2)
fig,ax=plt.subplots(figsize=(9.6,7.2))

tt=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(tt),np.sin(tt),color=GREY,lw=1.3,ls='--',label='unit circle')
ax.axhline(0,color='#bbb',lw=0.8); ax.axvline(0,color='#bbb',lw=0.8)

# image of REAL inputs k -> e^{r k} on positive real axis (log-spaced)
ks=[-2,-1,0,1,2]
for k in ks:
    v=np.exp(r*k)
    ax.scatter([v],[0],s=80,color=RED,edgecolor='white',zorder=6)
    ax.text(v,-0.17,f'$2^{{{k}}}$',color=RED,fontsize=11,ha='center')
ax.annotate('real inputs  →  log-spaced positive reals',xy=(2,0),xytext=(1.05,-0.78),
            color=RED,fontsize=12,fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.4))

# image of IMAGINARY inputs i*k -> e^{r i k} on the unit circle
for k in range(0,9):
    ang=r*k
    z=np.exp(1j*ang)
    ax.scatter([z.real],[z.imag],s=55,color=BLUE,edgecolor='white',zorder=6)
ax.annotate('imaginary inputs  →  the unit circle\n(step $=\ln 2$ radians)',
            xy=(np.cos(r*3),np.sin(r*3)),xytext=(-2.15,1.15),color=BLUE,fontsize=12,
            fontweight='bold',ha='left',
            arrowprops=dict(arrowstyle='->',color=BLUE,lw=1.4))

# mark f(1)=2, f(0)=1, f(-1)=1/2
for v,lab,c in [(1,'$f(0)=1$','#555'),(2,'$f(1)=2$',GREEN),(0.5,'$f(-1)=\tfrac12$',GREEN)]:
    ax.scatter([v],[0],s=30,color=c,zorder=7)
ax.set_title(r"$f(x)=\exp(\ln 2\cdot x)=2^{x}$ : how it reshapes the plane",
             fontsize=13.5,fontweight='bold',color=TEXT,pad=8)
ax.set_xlim(-2.4,4.2); ax.set_ylim(-1.7,1.7); ax.set_aspect('equal'); ax.axis('off')
plt.tight_layout()
plt.savefig('ii_fig7_exp_map.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ii_fig7_exp_map.png")
