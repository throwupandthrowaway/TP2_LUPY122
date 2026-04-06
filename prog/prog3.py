import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

Omega=1.
q=0.5
Fe=np.array([1.4,1.44,1.465,1.5])
Omegae=2*Omega/3
df=np.dtype([("Omega",float),("q",float),("Fe",float),("Omegae",float)])
dt=0.05
T=100.
t=0.
tvalues=np.arange(0.,T,dt)
n=tvalues.size
rad=np.pi/180
theta0=10*rad
y0=np.zeros(2)
y0[0]=theta0
y1=np.zeros(2)
y1[0]=theta0
y2=np.zeros(2)
y2[0]=theta0
y3=np.zeros(2)
y3[0]=theta0
thetavalues0=np.zeros(n)
thetavalues1=np.zeros(n)
thetavalues2=np.zeros(n)
thetavalues3=np.zeros(n)


p0=np.array((Omega,q,Fe[0],Omegae),dtype=df)[()]  #Libre
p1=np.array((Omega,q,Fe[1],Omegae),dtype=df)[()]  #Amorti
p2=np.array((Omega,q,Fe[2],Omegae),dtype=df)[()]  #Amorti avec excitation
p3=np.array((Omega,q,Fe[3],Omegae),dtype=df)[()]  #Amorti avec excitation

def deriv(t,y,params):
    dy=np.zeros(y.size)
    dy[0]=y[1]  #y=dtheta/dt
    dy[1]=-params[1]*y[1]-params[0]**2*np.sin(y[0])+params[2]*np.sin(params[3]*t)   #dy/dt=-q*y-Omega**2*sin(theta)+Fe*sin(Omegae*t)
    return dy

for i in range(n):
    thetavalues0[i]=y0[0]
    t=tvalues[i]
    y0=rk4(t,dt,y0,deriv,p0)
    if y0[0]>np.pi:
        y0[0]-=2*np.pi
    elif y0[0]<-np.pi:
        y0[0]+=2*np.pi

for i in range(n):
    thetavalues1[i]=y1[0]
    t=tvalues[i]
    y1=rk4(t,dt,y1,deriv,p1)
    if y1[0]>np.pi:
        y1[0]-=2*np.pi
    elif y1[0]<-np.pi:
        y1[0]+=2*np.pi

for i in range(n):
    thetavalues2[i]=y2[0]
    t=tvalues[i]
    y2=rk4(t,dt,y2,deriv,p2)
    if y2[0]>np.pi:
        y2[0]-=2*np.pi
    elif y2[0]<-np.pi:
        y2[0]+=2*np.pi

for i in range(n):
    thetavalues3[i] = y3[0]
    y3 = rk4(tvalues[i], dt, y3, deriv, p3)
    if y3[0]>np.pi:
        y3[0]-=2*np.pi
    elif y3[0]<-np.pi:
        y3[0]+=2*np.pi

plt.plot(tvalues,thetavalues0,label=r"$F_e=1.4rad.s^{-2}$")
plt.ylabel(r"$\theta(t)$")
plt.xlabel("t")
plt.grid()
plt.title(r"Angle du pendule en fonction du temps à $F_e=1.4rad.s^{-2}$")
plt.savefig("Graphe_TP2_Q3_0",bbox_inches='tight')
plt.show()

plt.plot(tvalues,thetavalues1,label=r"$F_e=1.44rad.s^{-2}$")
plt.ylabel(r"$\theta(t)$")
plt.xlabel("t")
plt.grid()
plt.title(r"Angle du pendule en fonction du temps à $F_e=1.44rad.s^{-2}$")
plt.savefig("Graphe_TP2_Q3_1",bbox_inches='tight')
plt.show()

plt.plot(tvalues,thetavalues2,label=r"$F_e=1.465rad.s^{-2}$")
plt.ylabel(r"$\theta(t)$")
plt.xlabel("t")
plt.grid()
plt.title(r"Angle du pendule en fonction du temps à $F_e=1.465rad.s^{-2}$")
plt.savefig("Graphe_TP2_Q3_2",bbox_inches='tight')
plt.show()

plt.plot(tvalues,thetavalues3,label=r"$F_e=1.5rad.s^{-2}$")
plt.ylabel(r"$\theta(t)$")
plt.xlabel("t")
plt.grid()
plt.title(r"Angle du pendule en fonction du temps à $F_e=1.5rad.s^{-2}$")
plt.savefig("Graphe_TP2_Q3_3",bbox_inches='tight')
plt.show()
