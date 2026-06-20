"""ps_fig1_inscribed.png — the Inscribed Angle Theorem: central angle = 2x the
inscribed angle, proved by splitting into isosceles triangles."""
import matplotlib.pyplot as plt
import numpy as np

BLUE='#1f4f8c'; GREEN='#3d7530'; RED='#a83227'; GREY='#888'; TEXT='#222'
fig,ax=plt.subplots(figsize=(8,8))
import math
O=np.array([0,0]); R=1.0
P=np.array([0,1.0])
A=np.array([math.cos(math.radians(210)),math.sin(math.radians(210))])
B=np.array([math.cos(math.radians(330)),math.sin(math.radians(330))])
tt=np.linspace(0,2*np.pi,400)
ax.plot(R*np.cos(tt),R*np.sin(tt),color=GREY,lw=1.5)
# radii
for X,c in [(A,GREEN),(B,GREEN),(P,BLUE)]:
    ax.plot([O[0],X[0]],[O[1],X[1]],color=c,lw=2)
    mid=(O+X)/2; perp=np.array([-(X-O)[1],(X-O)[0]]); perp=perp/np.linalg.norm(perp)*0.03
    ax.plot([mid[0]-perp[0],mid[0]+perp[0]],[mid[1]-perp[1],mid[1]+perp[1]],color=c,lw=2)
# chords PA, PB
ax.plot([P[0],A[0]],[P[1],A[1]],color=TEXT,lw=1.6)
ax.plot([P[0],B[0]],[P[1],B[1]],color=TEXT,lw=1.6)
# points
for X,lab,dx,dy in [(P,'P',0,0.08),(A,'A',-0.09,-0.03),(B,'B',0.09,-0.03),(O,'O',0.05,0.06)]:
    ax.scatter([X[0]],[X[1]],s=55,color=TEXT,zorder=6)
    ax.text(X[0]+dx,X[1]+dy,lab,fontsize=14,fontweight='bold',ha='center',color=TEXT)
# inscribed angle theta_S at P (split alpha,beta by radius OP)
ax.text(-0.10,0.74,r'$\alpha$',fontsize=13,color=GREEN)
ax.text(0.11,0.74,r'$\beta$',fontsize=13,color=GREEN)
ax.annotate(r'$\theta_S=\alpha+\beta$',xy=(0,0.85),xytext=(0.62,0.92),fontsize=14,color=BLUE,
            fontweight='bold',arrowprops=dict(arrowstyle='->',color=BLUE,lw=1.4))
# base angles alpha at A, beta at B
ax.text(A[0]+0.16,A[1]+0.10,r'$\alpha$',fontsize=13,color=GREEN)
ax.text(B[0]-0.16,B[1]+0.10,r'$\beta$',fontsize=13,color=GREEN)
# central angles
ax.text(-0.13,0.18,r"$\alpha'$",fontsize=12,color=RED)
ax.text(0.10,0.18,r"$\beta'$",fontsize=12,color=RED)
ax.annotate(r'$\theta_L=2\theta_S$',xy=(0,-0.34),xytext=(0.55,-0.78),fontsize=15,color=RED,
            fontweight='bold',arrowprops=dict(arrowstyle='->',color=RED,lw=1.6))
# arc for theta_L at bottom
arc=np.linspace(math.radians(210),math.radians(330),60)
ax.plot(0.30*np.cos(arc),0.30*np.sin(arc),color=RED,lw=2)
ax.text(-1.28,1.15,"radii equal (tick marks)\n→ 3 isosceles triangles",fontsize=11,color=GREEN)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.35,1.45); ax.set_aspect('equal'); ax.axis('off')
ax.set_title("Inscribed Angle Theorem: central angle is twice the inscribed angle",
             fontsize=13.5,fontweight='bold',color=TEXT,pad=8)
plt.tight_layout()
plt.savefig('ps_fig1_inscribed.png',dpi=220,bbox_inches='tight',facecolor='white')
plt.close(); print("Saved ps_fig1_inscribed.png")
