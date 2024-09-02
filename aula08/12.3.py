import numpy as np
import matplotlib.pyplot as plt

P = 0.4 * 735.4975
vi = 1
m = 75
Cres = 0.9
A = 0.3
p = 1.225
u = 0.004
g = 9.8

ti = 0
tf = 2000
dt = 0.001

n = int((tf-ti)/dt)
t = np.linspace(ti, tf, n)

x = np.empty(n)
x[0] = 0
vx = np.empty(n)
vx[0] = vi
v = np.empty(n)
v[0] = vi
ax = np.empty(n)
ax[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = -u*g - (Cres/(2*m))*A*p*v[i]*vx[i] + (P/(m*v[i]))
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt 
    if (x[i] < 2000 + dt) and (x[i+1] > 2000 - dt):
        print("Tempo: ", t[i])
        
v[n-1] = np.sqrt(vx[n-1]**2)

plt.plot(t, v)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid()