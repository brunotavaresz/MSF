import numpy as np
import matplotlib.pyplot as plt

global t,g,vt,v

dt = 0.1
tf = 3.0
t0 = 0
N= int(np.ceil((tf-t0)/dt) + 1 )

g = 9.80
vt = 6.80

x0 = 0
vx0 = 0

t = np.linspace(t0, tf, N)

y,v = [np.zeros(N), np.zeros(N)]
y[0] , v[0] = [0,0]

def acel2 (t,g,vt,v):
    return g - (g/vt**2) * np.abs(v) * v

def rk4(t, v, x, acel2, **kwargs):
    N = len(t)
    dt =t[1] - t[0]
    g, vt = [kwargs["g"]], kwargs["vt"]
    for i in range(N-1):
        a1 = acel2(t[i], g, vt, v[i])
        c1v = a1 *dt
        c1x =  v[i] *dt
        a2 = acel2(t[i] + dt /2, g, vt, v[i] + c1v/2.)
        c2v = a2 * dt
        c2x = (v[i] + c1v / 2.)*dt
        a3 = acel2(t[i] + dt/2, g, vt, v[i] + c2v/2.)
        c3v = a3 * dt
        c3x = (v[i] + c2v /2.) * dt
        a4 = acel2( t[i] + dt, g, vt, v[i] + c3v)
        c4 = a4 *dt
        c4x = (v[i] + c3v) * dt
        x[i+1] = x[i] + (c1x+2. * c2x+2. * c3x+c4x)/6
        v[i+1] = v[i] + (c1x+2. * c2x+2. * c3x+c4x)/6
    return x, v

y, v = rk4(t,y,v,acel2, g=g, vt= vt)

plt.figure()
plt.plot(t, y , 'r-')

y2, v2 = [np.zeros(N), np.zeros(N)]
y2[0], v2[0] = [0,0]


for i in range(N-1):
    a= acel2(t, g, vt, v[i])
    v2 [i+1] = v2 [i] + a *dt
    y2 [i+1] = y2[i] + v2[i] * dt
    
v_analitycal = vt * np.tanh(g * t/vt)

erro_rk4 = np.abs(v_analitycal - v)
erro_euler = np.abs(v_analitycal - v2)

fig, axs = plt.subplots(2, 1, figsize = (9,7))
axs[0].plot(t, erro_euler)
axs[1].plot(t, erro_rk4)