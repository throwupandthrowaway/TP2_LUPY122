#Example: d^2x/dt^2=-omega^2x

import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

def deriv(t,y,params):  #Define your derivative function
    dy=np.zeros(y.size)
    dy[0]=y[1]  #y=dx/dt
    dy[1]=-params**2*y[0]   #dy/dt=-omega**2x
    return dy

omega = 1
t = 0
dt = 0.001 
tmax = 100 #libre de choix
tValues = np.arange(0, tmax, dt)
n = tValues.size
xValues = np.empty(n)   #Create your set of values

x0 = 1 
v0 = 0 
y = np.empty(2) #Create your vector
y[0] = x0   #Initial values
y[1] = v0

xAnalytique = x0*np.cos(omega*tValues)

for i in range(n):
    xValues[i]=y[0]
    t=tValues[i]
    y=rk4(t, dt, y, deriv, omega)   #That's it, just let rk4  do the work
    
plt.plot(tValues,xValues-xAnalytique)
