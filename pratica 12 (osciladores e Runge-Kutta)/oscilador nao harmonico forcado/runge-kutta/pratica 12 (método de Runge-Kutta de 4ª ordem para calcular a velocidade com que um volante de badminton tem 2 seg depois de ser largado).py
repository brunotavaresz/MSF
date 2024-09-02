#  Implemente o método de Runge-Kutta de 4ª ordem para calcular a velocidade com que um volante de badmington atinge 2 s 
# depois de ser largado. A velocidade terminal do volante é de 6.80 m/s, e a aceleração é ay(t) = g- g/vt^2 * vy * vy
# Compare o valor obtido com o valor exato, de acordo com a lei vy(t) = vt * tanh(gt/vt)

#...

import numpy as np
import matplotlib.pyplot as plt


def acelera(t, x, vx):
    ax = g-g/vt**2*np.abs(vx)*vx
    return ax


def rk4(t, x, vx, dt):
    # Modificado
    ax1 = acelera(t, x, vx)
    c1v = ax1*dt
    c1x = vx*dt
    ax2 = acelera(t+dt/2., x+c1x/2., vx+c1v/2.)
    c2v = ax2*dt
    c2x = (vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3 = acelera(t+dt/2., x+c2x/2., vx+c2v/2.)
    c3v = ax3*dt
    c3x = (vx+c2v/2.)*dt
    ax4 = acelera(t+dt, x+c3x, vx+c3v)
    c4v = ax4*dt
    c4x = (vx+c3v)*dt
    xp = x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp = vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp, vxp


dt = 0.5
tf = 2.0
n = np.int(tf/dt)

g = 9.80
vt = 6.80

t0 = 0
x0 = 0
vx0 = 0

t = np.zeros(n+1)
xrk4 = np.zeros(n+1)
vxrk4 = np.zeros(n+1)  # rk4


t[0] = t0
vxrk4[0] = vx0
xrk4[0] = x0
tem = t0
xet = x0
vxet = vx0




plt.grid()
plt.plot(t, vxrk4, label="Runge-Kutta")
plt.xlabel("Tempo(s)")
plt.ylabel("Velocidade(m/s)")
plt.legend()
plt.show()