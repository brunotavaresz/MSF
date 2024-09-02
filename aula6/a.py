import numpy as np
import matplotlib.pyplot as plt

ti = 0
tf = 1
dt = 0.001
n = int((tf-ti)/dt)
g = 9.8
v0 = 100/3.6
ang = np.radians(10)

t = np.linspace(ti, tf, 1000)

vx = np.empty(n+1)
vx[0] = v0 * np.cos(ang)
vy = np.empty(n+1)
vy[0] = v0 * np.sin(ang)
ax = np.empty(n+1)
ax[0] = 0
ay = np.empty(n+1)
ay[0] = -g
y = np.empty(n+1)
y[0] = 0
x = np.empty(n+1)
x[0] = 0

for i in range(n):
    ay[i] = -g
    ax[i] = 0
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt


for i in range(n):
    if (y[i] > y[i+1]):
        print("Altura máxima:", y[i])
        break

for i in range(n):
    if (y[i] * y[i+1] < 0 ):
        print("Alcance e tempo:", x[i], t[i])
        break


plt.plot(x, y, label="a")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()