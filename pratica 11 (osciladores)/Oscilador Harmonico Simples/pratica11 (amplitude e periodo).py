# Uma mola exerce uma força 𝐹𝑥 = −𝑘 𝑥 𝑡 , em que 𝑘 é a constante elástica da mola, num corpo de massa 𝑚.
# Considere 𝑘 = 1 N/m e 𝑚 = 1 kg.

# Calcule a amplitude do movimento e o seu período, usando os resultados numéricos.

import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
m = 1
k = 1
t0 = 0
tf = 500
n = int((tf-t0)/dt)
w = np.sqrt(k/m)
t = np.linspace(t0, tf, n)
psi = 0
A = 4

x = A*np.cos(w*t+psi)

x2 = np.empty(n)
x2[0] = 4

v = np.empty(n)
v[0] = 0

a = np.empty(n)
a[0] = 0

arrayx = []
periodos = []
tempos = []
for i in range(n-1):
    a[i] = -k*x2[i]/m
    v[i+1] = v[i] + a[i]*dt
    x2[i+1] = x2[i]+v[i+1]*dt

    if x[i-1] < x[i] > x[i+1]:
        arrayx.append(x[i])
        tempos.append(t[i])

amplitude = sum(arrayx)/len(arrayx)


print("Amplitude: ", amplitude)


for i in range(len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])

periodo = sum(periodos)/len(periodos)
print("Período: ", periodo)
