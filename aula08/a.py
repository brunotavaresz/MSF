import numpy as np
import matplotlib.pyplot as plt

m = 75
Cres = 0.9
A = 0.3
p = 1.225
u = 0.004
g = 9.8
P = 0.4 * 735.4975
vi = 1
t0 = 0
tf = 100
dt = 0.001
tol = 0.000001
teta = np.radians(5)

n = int(tf/dt)
t = np.linspace(t0, tf, n)

ax = np.empty(n)
vx = np.empty(n)
x = np.empty(n)
v = np.empty(n)

ax[0] = 0
vx[0] = vi
x[0] = 0
v[0] = vi


for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = -u*g*np.cos(teta) - (Cres/(2*m))*A*p*(vx[i]) * \
        v[i] + P/(m*v[i]) - g*np.sin(teta)
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    v[n-1] = np.sqrt(vx[n-1]**2)

    if (vx[i]-vx[i-1] < tol):
        print("Velociadade Terminal = ", vx[i])
        break

plt.plot(t, v, color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid()
plt.show()