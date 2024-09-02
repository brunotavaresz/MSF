import numpy as np
import matplotlib.pyplot as plt

ti = 0
tf = 2
dt = 0.001
n = int((tf-ti)/dt)
g = 9.8
v0 = (100*1000)/3600
ang = np.radians(10)
vT = (100*1000)/3600
D = g / vT**2


t = np.linspace(ti, tf, 1000)

ax = np.empty(n+1)
ay = np.empty(n+1)
v = np.empty(n+1)
vx = np.empty(n+1)
vy = np.empty(n+1)
y = np.empty(n+1)
x = np.empty(n+1)


ax[0] = 0
ay[0] = -g
v[0] = v0
vx[0] = v0 * np.cos(ang)
vy[0] = v0 * np.sin(ang)
y[0] = 0
x[0] = 0


for i in range(n):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    ay[i] = -g - D*vy[i]*v[i]
    ax[i] = - D*vx[i]*v[i]
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    
for i in range(n-1):
    if (y[i] > y[i+1]):
        print("Altura máxima:", y[i])
        break

for i in range(n-1):
    if (y[i] * y[i+1] < 0 ):
        print("Alcance e tempo:", x[i], t[i])
        break

xanalitico = x[0] + vx[0]*t
yanalitico = y[0] + vy[0]*t - 1/2*g*t**2



plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.plot(x, y, "r--", label="Com resistência")
plt.plot(xanalitico, yanalitico, "k--", label="Sem resistência")
plt.legend()
plt.show()

