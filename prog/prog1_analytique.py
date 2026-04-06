import numpy as np
import matplotlib.pyplot as plt
Omega=1.
q=np.array([1.,2.,5.])
dt=0.05
T=20.
delta=q**2-4*Omega**2
omega0=np.sqrt(abs(delta[0]))/2
omega1=(-q[2]+np.sqrt(delta[2]))/2
omega2=(-q[2]-np.sqrt(delta[2]))/2
rad=np.pi/180
theta0=10*rad

def theta1(t):
    return theta0*np.exp(-q[0]*t/2)*np.cos(omega0*t)+(theta0*q[0]/2*omega0)*np.exp(-q[0]*t/2)*np.sin(omega0*t)
def theta2(t):
    return theta0*(q[1]/2*t+1)*np.exp(-q[1]/2*t)
def theta5(t):
    return theta0*(1-1/(1-omega1/omega2))*np.exp(omega1*t)+theta0/(1-omega1/omega2)*np.exp(omega2*t)

tvalues=np.arange(0,T,dt)
theta1=theta1(tvalues)
theta2=theta2(tvalues)
theta5=theta5(tvalues)

plt.plot(tvalues,theta1,label="q=1")
plt.plot(tvalues,theta2,label="q=2")
plt.plot(tvalues,theta5,label="q=5")
plt.grid()
plt.xlabel("t")
plt.ylabel(r"$\theta(t)$")
plt.title("Angle du pendule en fonction du temps à différents régimes"
          +"\n"+"q=1: Régime pseudo-périodique"
          +"\n"+"q=2: Régime critique"
          +"\n"+"q=5: Régime apériodique")
plt.legend()
plt.savefig("Graphe_TP2_Q1_analytique",bbox_inches='tight')
plt.show()
