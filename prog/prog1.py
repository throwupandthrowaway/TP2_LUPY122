import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

Omega=1.
q=np.array([1.,2.,5.])
df=np.dtype([('Omega',float),('q',float)])
dt=0.05
T=20.
t=0.
tvalues=np.arange(0.,T,dt)
n=tvalues.size
rad=np.pi/180
theta0=10*rad
y0=np.zeros(2)
y1=np.zeros(2)
y2=np.zeros(2)
thetavalues0=np.zeros(n)
thetavalues1=np.zeros(n)
thetavalues2=np.zeros(n)


p0=np.array((Omega,q[0]),dtype=df)[()]    #A dataframe that groups every parameter
p1=np.array((Omega,q[1]),dtype=df)[()]
p2=np.array((Omega,q[2]),dtype=df)[()]    

def deriv(t,y,params):
    dy=np.zeros(y.size)
    dy[0]=y[1]  #y=dtheta/dt
    dy[1]=-params[1]**y[1]-params[0]**2*y[0]   #dy/dt=-q*u-Omega**2*theta
    return dy

for i in range(n):
    thetavalues0[i]=y0[0]
    t=tvalues[i]
    y0=rk4(t,dt,y0,deriv,p0)

for i in range(n):
    thetavalues1[i]=y1[0]
    t=tvalues[i]
    y1=rk4(t,dt,y1,deriv,p1)
    
for i in range(n):
    thetavalues2[i]=y2[0]
    t=tvalues[i]
    y2=rk4(t,dt,y2,deriv,p2)

plt.plot(tvalues,thetavalues0,label="q=1")
plt.plot(tvalues,thetavalues1,label="q=2")
plt.plot(tvalues,thetavalues2,label="q=5")
plt.title("Mouvement du pendule à différents régimes"
          +"\n"+"q=1: Régime pseudo-périodique"
          +"\n"+"q=2: Régime critique"
          +"\n"+"q=5: Régime apériodique")
plt.legend()
plt.savefig("Graphe_TP2_Q1")
plt.show()
