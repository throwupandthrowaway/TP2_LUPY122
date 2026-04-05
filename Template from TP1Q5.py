#Example: d^2x/dt^2=-omega^2x

import numpy as np
def deriv(t,y,params):  #Separate the 2nd order ODE into 2 1st order ODEs
    dy=np.zeros(y.size)
    omega=params
    dy[0]=y[1]  #y=dx/dt
    dy[1]=-omega**2*y[0]    #dy/dt=-omega**2x
    return dy   #Here y[0]=x (so dy[0]=dx/dt) and y[1]=y (so dy[1]=dy/dt)

#You don't need to touch that it's already taken care of
#Just make sure euler.py is in the same directory as your script
from euler import euler
omega=1
t=0
dt=0.01 #Time step
Tmax=20
Tvalues=np.arange(0,Tmax,dt)
n=Tvalues.size
xvalues=np.empty(n) #Position curve
vvalues=np.empty(n) #Velocity curve
x0=1    #Initial values
v0=0
y=np.empty(2)   #Create a vector containing both curves
y[0]=x0
y[1]=v0

for i in range(n):
    xvalues[i]=y[0]
    vvalues[i]=y[1]
    t=Tvalues[i]
    y=euler(t,dt,y,deriv,omega)
    
import matplotlib.pyplot as plt
plt.plot(Tvalues,xvalues,label="x(t)")
plt.plot(Tvalues,vvalues,label="v(t)")
