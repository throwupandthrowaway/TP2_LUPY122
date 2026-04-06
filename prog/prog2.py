import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

Omega=1.
q=np.array([0.,1.])
Fe=np.array([0.,1.])
Omegae=2*Omega/3
df=np.dtype([("Omega",float),("q",float),("Fe",float),("Omegae",float)])
dt=0.05
T=20.
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
thetavalues0=np.zeros(n)
dtheta0=np.zeros(thetavalues0.size)
thetavalues1=np.zeros(n)
dtheta1=np.zeros(thetavalues1.size)
thetavalues2=np.zeros(n)
dtheta2=np.zeros(thetavalues2.size)


p0=np.array((Omega,q[0],Fe[0],Omegae),dtype=df)[()]  #Libre
p1=np.array((Omega,q[1],Fe[0],Omegae),dtype=df)[()]  #Amorti
p2=np.array((Omega,q[1],Fe[1],Omegae),dtype=df)[()]  #Amorti avec excitation

def deriv(t,y,params):
    dy=np.zeros(y.size)
    dy[0]=y[1]  #y=dtheta/dt
    dy[1]=-params[1]*y[1]-params[0]**2*y[0]+params[2]*np.sin(params[3]*t)   #dy/dt=-q*u-Omega**2*theta+Fe*sin(Omegae*t)
    return dy

for i in range(n):
    thetavalues0[i]=y0[0]
    dtheta0[i]=y0[1]
    t=tvalues[i]
    y0=rk4(t,dt,y0,deriv,p0)

for i in range(n):
    thetavalues1[i]=y1[0]
    dtheta1[i]=y1[1]
    t=tvalues[i]
    y1=rk4(t,dt,y1,deriv,p1)
    
for i in range(n):
    thetavalues2[i]=y2[0]
    dtheta2[i]=y2[1]
    t=tvalues[i]
    y2=rk4(t,dt,y2,deriv,p2)

plt.plot(thetavalues0,dtheta0,label="Régime libre")
plt.plot(thetavalues1,dtheta1,label="Régime libre amorti")
plt.plot(thetavalues2,dtheta2,label="Régime amorti avec force d'excitation")
plt.xlabel(r"$\theta(t)$")
plt.ylabel(r"$\frac{d\theta}{dt}$")
plt.grid()
plt.title("Espace des phases du pendule"
          +"\n"+r"Bleu: régime libre $(q=0,\,F_e=0)$"
          +"\n"+r"Orange: régime libre amorti $(q=1,\,F_e=0)$"
          +"\n"+r"Vert: régime amorti avec force d'excitation $(q=1,\,F_e=1)$")
plt.savefig("Graphe_TP2_Q2",bbox_inches='tight')
plt.show()
