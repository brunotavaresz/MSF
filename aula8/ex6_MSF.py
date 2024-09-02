import numpy as np
import matplotlib.pyplot as plt

m = 1
A = 4
dt = 0.02
t0 =0
tf = 40
Nt = int(np.ceil((tf-t0) / dt)+1)

t = np.linspace(ti, tf, Nt)

x = np.zeros(Nt)
vx = np.zeros(Nt)
ax = np.zeros(Nt)


vx[0] = 0
x[0] = A


for i in range(n):
    t[i+1]=t[i]+dt
    r=np.sqrt(x[i]**2+y[i]**2)
    ax[i]=-gm/r**3*x[i]
    ay[i]=-gm/r**3*y[i]
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt x
    
    
for i in range(n):
    t[i+1]=t[i]+dt
    r=np.sqrt(x[i]**2+y[i]**2)
    ax[i]=-gm/r**3*x[i]
    ay[i]=-gm/r**3*y[i]
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    x[i+1]=x[i]+vx[i+1]*dt
    y[i+1]=y[i]+vy[i+1]*dt x
    
"solução analítica"
omega = np.sqrt(k/ m)
vxt= -A * omega * np.sin(omega*t)
xt = A * np.cos(omega*t)
Et= .5 * k * xt**2 + 5 *m* vxt**2
