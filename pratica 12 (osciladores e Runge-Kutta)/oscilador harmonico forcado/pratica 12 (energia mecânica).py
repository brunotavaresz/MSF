# Um corpo de massa 1 kg move-se num oscilador harmónico forçado. Se a posição de equilíbrio for a
# origem do eixo xeq = 0 m, o oscilador harmónico tem a energia potencial Ep = 1/2 * k * x ^2
# e exerce no corpo a força Fx = -k * x
# O oscilador é amortecido pela força -b * vx e sujeito à força externa F0 * cos(wf * t). 

# Considere k = 1 N/m, b = 0.05 kg/s, F0 = 7.5 N e wf = 1.0 rad/s.

# e) Calcula a energia mecânica, é constante ao longo do tempo?

import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 400
dt = 0.01
n = int((tf-t0)/dt)
k = 1
b = 0.05
F0 = 7.5
m = 1
w = 1

t = np.linspace(t0, tf, n)

a = np.empty(n)

v = np.empty(n)
v[0] = -4

x = np.empty(n)
x[0] = -2

for i in range(n-1):
    a[i] = (-k*x[i])/m - (b*v[i])/m + (F0*np.cos(w*t[i]))/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

Em = 1/2*m*v**2 + 1/2*k*x**2

plt.plot(t, Em)
plt.grid()
plt.show()
