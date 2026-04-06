#Mahery Andriamadison
#21304938
#MAJ2A

import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

Omega=1.
q=0.5
Fe=1.5
Omegae=2*Omega/3
df=np.dtype([("Omega",float),("q",float),("Fe",float),("Omegae",float)])
dt=0.05
T=100.
t=0.
tvalues=np.arange(0.,T,dt)
n=tvalues.size
rad=np.pi/180
theta0=10*rad
theta1=9.999*rad
y0=np.zeros(2)
y0[0]=theta0
y1=np.zeros(2)
y1[0]=theta1
thetavalues0=np.zeros(n)
thetavalues1=np.zeros(n)


p=np.array((Omega,q,Fe,Omegae),dtype=df)[()]

def deriv(t,y,params):
    dy=np.zeros(y.size)
    dy[0]=y[1]  #y=dtheta/dt
    dy[1]=-params[1]*y[1]-params[0]**2*np.sin(y[0])+params[2]*np.sin(params[3]*t)   #dy/dt=-q*y-Omega**2*sin(theta)+Fe*sin(Omegae*t)
    return dy

for i in range(n):
    thetavalues0[i]=y0[0]
    t=tvalues[i]
    y0=rk4(t,dt,y0,deriv,p)
    if y0[0]>np.pi:
        y0[0]-=2*np.pi
    elif y0[0]<-np.pi:
        y0[0]+=2*np.pi

for i in range(n):
    thetavalues1[i]=y1[0]
    t=tvalues[i]
    y1=rk4(t,dt,y1,deriv,p)
    if y1[0]>np.pi:
        y1[0]-=2*np.pi
    elif y1[0]<-np.pi:
        y1[0]+=2*np.pi

plt.plot(tvalues,thetavalues0-thetavalues1,label="diff")
plt.ylabel(r"$\theta(t)$")
plt.xlabel("t")
plt.grid()
plt.title(r"Différence entre $\theta_0=10°$ et $\theta_0=9.999°$")
plt.savefig("Graphe_TP2_Q4",bbox_inches='tight')
plt.show()

plt.plot(tvalues,np.log(abs(thetavalues0-thetavalues1)))
plt.ylabel(r"$ln(\theta_1(t)-\theta_0(t))$")
plt.xlabel("t")
plt.grid()
plt.title(r"Logarithme népérien de la différence entre $\theta_0=10°$ et $\theta_0=9.999°$")
plt.savefig("Graphe_TP2_Q4_Lyapounov",bbox_inches='tight')
plt.show()
