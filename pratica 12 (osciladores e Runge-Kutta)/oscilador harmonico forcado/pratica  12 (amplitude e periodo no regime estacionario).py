# Um corpo de massa 1 kg move-se num oscilador harmónico forçado. Se a posição de equilíbrio for a
# origem do eixo xeq = 0 m, o oscilador harmónico tem a energia potencial Ep = 1/2 * k * x ^2
# e exerce no corpo a força Fx = -k * x
# O oscilador é amortecido pela força -b * vx e sujeito à força externa F0 * cos(wf * t). 

# Considere k = 1 N/m, b = 0.05 kg/s, F0 = 7.5 N e wf = 1.0 rad/s.

# b) Calcule a amplitude do movimento e o seu período no regime estacionário, usando os resultados numéricos.

import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.05
F0 = 7.5
w = -1

t0 = 0
tf = 400
dt = 0.001
n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
x = np.empty(n)
v = np.empty(n)
v[0] = -4
x[0] = -2

for i in range(n-1):
    a[i] = (-k*x[i]/m) - (b*v[i]/m) + (F0*np.cos(t[i])/m)
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt

maxes = []
tempos = []
for i in range(n):
    if t[i] > 200:
        if x[i-1] < x[i] > x[i+1]:
            maxes.append(x[i])
            tempos.append(t[i])

amplitude = sum(maxes)/len(maxes)
print("Amplitude: ", amplitude)

periodos = []
for i in range(len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])

periodo = sum(periodos)/len(periodos)
print("Período: ", periodo)
