import matplotlib.pyplot as plt
import numpy as np

v0 = 100/3.6 
teta = np.radians(10)
dt = 0.01
g = 9.8
t0 = 0
tf = 1
m = 0.057

vt= 100/3.6 

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)
aresx = np.empty(n)
aresy = np.empty(n)

x = np.empty(n) 
y = np.empty(n)

v = np.empty(n)
Em = np.empty(n)
fun = np.empty(n)
int_trab_res = np.empty(n)

x[0] = 0
y[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

d = g/vt**2

for i in range(n-1):  
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    aresy[i] = -d*abs(v[i])*vy[i]
    ay[i] = aresy[i]-g
    ax[i] = -d*vx[i]*abs(v[i])
    aresx[i] = ax[i]
    
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]
    
    fun[i] = m*aresx[i]*vx[i] + m*aresy[i]*vy[i]
    int_trab_res[i] = dt*((fun[0] + fun[i])/2 + np.sum(fun[1:i]))
    
    if i == 0:
        print(int_trab_res[i])
    if t[i] < 0.4 < t[i+1]:
        print(int_trab_res[i])
    if t[i] < 0.8 < t[i+1]:
        print(int_trab_res[i])

v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*m*v[n-1]**2 + m*g*y[n-1]
    
plt.plot(t,int_trab_res)
plt.grid()
plt.show()