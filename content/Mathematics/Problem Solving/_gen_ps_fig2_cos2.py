"""ps_fig2_cos2.png — two views of one length prove cos^2 = (1+cos2t)/2."""
import matplotlib.pyplot as plt
import numpy as np, math

BLUE='#1f4f8c'; GREEN='#3d7530'; RED='#a83227'; GREY='#888'; TEXT='#222'
th=math.radians(38)
fig,(axL,axR)=plt.subplots(1,2,figsize=(13.4,6.6))

# ---- LEFT: double projection ----
tt=np.linspace(0,np.pi/2,100)
axL.plot(np.cos(tt),np.sin(tt),color=GREY,lw=1.3,ls='--')
axL.plot([0,1.05],[0,0],color='#bbb',lw=1); axL.plot([0,0],[0,1.05],color='#bbb',lw=1)
Pt=np.array([math.cos(th),math.sin(th)])
axL.plot([0,Pt[0]],[0,Pt[1]],color=BLUE,lw=2.2)               # radius length 1
axL.plot([Pt[0],Pt[0]],[Pt[1],0],color=RED,lw=1.6,ls='--')     # drop to x-axis
axL.scatter([Pt[0]],[0],s=30,color=RED,zorder=5)
# project (cos t,0) back onto the radius -> point at distance cos^2 t along radius
d=math.cos(th)**2
F=np.array([d*math.cos(th),d*math.sin(th)])
axL.plot([math.cos(th),F[0]],[0,F[1]],color=GREEN,lw=1.6,ls='--')
axL.scatter([F[0]],[F[1]],s=30,color=GREEN,zorder=5)
axL.annotate(r'$\cos^2\theta$',xy=(F[0]/2,F[1]/2),xytext=(0.12,0.12),fontsize=13,color=GREEN,fontweight='bold')
axL.annotate(r'$\sin^2\theta$',xy=((F[0]+Pt[0])/2,(F[1]+Pt[1])/2),xytext=(0.52,0.62),fontsize=13,color=RED,fontweight='bold',
             arrowprops=dict(arrowstyle='->',color=RED,lw=1.1))
axL.text(math.cos(th)/2,-0.08,r'$\cos\theta$',fontsize=12,color=TEXT,ha='center')
axL.text(0.16,0.045,r'$\theta$',fontsize=12,color=TEXT)
axL.set_title(r"Double projection: $\cos^2\theta+\sin^2\theta=1$ along the radius",fontsize=12,fontweight='bold')
axL.set_xlim(-0.1,1.15); axL.set_ylim(-0.15,1.1); axL.set_aspect('equal'); axL.axis('off')

# ---- RIGHT: Thales / inscribed right triangle ----
r=0.5; O=np.array([0,0]); VL=np.array([-0.5,0]); VR=np.array([0.5,0])
C=np.array([r*math.cos(2*th), r*math.sin(2*th)])
F2=np.array([C[0],0])
tt=np.linspace(0,2*np.pi,300)
axR.plot(r*np.cos(tt),r*np.sin(tt),color=GREY,lw=1.3)
axR.plot([VL[0],VR[0]],[0,0],color=TEXT,lw=1.6)               # diameter (hyp=1)
axR.plot([VL[0],C[0]],[VL[1],C[1]],color=TEXT,lw=1.6)         # leg
axR.plot([VR[0],C[0]],[VR[1],C[1]],color=TEXT,lw=1.6)         # leg
axR.plot([C[0],F2[0]],[C[1],F2[1]],color=GREEN,lw=1.6,ls='--')# altitude
axR.plot([O[0],C[0]],[O[1],C[1]],color=RED,lw=1.8)            # radius to C
for X,lab,dx,dy in [(VL,r'$\theta$',0.05,0.05),(O,'O',0,-0.07),(C,'',0,0)]:
    axR.scatter([X[0]],[X[1]],s=35,color=TEXT,zorder=6)
axR.text(VL[0]+0.07,0.04,r'$\theta$',fontsize=13,color=TEXT)
axR.text(C[0]+0.02,C[1]+0.03,r'$90^\circ$',fontsize=10,color=TEXT)
axR.text((O[0]+C[0])/2-0.02,(O[1]+C[1])/2+0.03,r'$2\theta$',fontsize=12,color=RED,fontweight='bold')
# L bracket from VL to F2
axR.annotate('',xy=(F2[0],-0.07),xytext=(VL[0],-0.07),arrowprops=dict(arrowstyle='<->',color=GREEN,lw=1.6))
axR.text((VL[0]+F2[0])/2,-0.14,r'$L=\cos^2\theta=\frac{1}{2}(1+\cos2\theta)$',fontsize=12,color=GREEN,
         fontweight='bold',ha='center')
axR.text(0,-0.30,r'radius $=\frac{1}{2}$,  so $L=\frac{1}{2}+\frac{1}{2}\cos2\theta$',fontsize=11,color=TEXT,ha='center')
axR.set_title("Inscribed right triangle (Thales): the same $L$, two ways",fontsize=12,fontweight='bold')
axR.set_xlim(-0.62,0.62); axR.set_ylim(-0.4,0.6); axR.set_aspect('equal'); axR.axis('off')

fig.suptitle(r"One length described two ways $\Rightarrow\ \cos^2\theta=\frac{1}{2}(1+\cos2\theta)$",
             fontsize=14,fontweight='bold',y=1.0)
plt.tight_layout()
plt.savefig('ps_fig2_cos2.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ps_fig2_cos2.png")
