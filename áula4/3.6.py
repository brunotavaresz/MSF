# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 23:56:23 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

v0 = 0
t0 = 0
tf = 3
g = -9.8
dt = 0.01  # nos é que escolhemos o valor, quanto maior o dt menos pontos no grafico nos teremos
y0 = 0


n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)
v = np.empty(n)  # cria uma lista com n valores vazia
v[0] = 0
y = np.empty(n)
y[0] = 0

for i in range(n-1):  # adicionar valor das velocidades a lista criado em np.empty
    v[i+1] = v[i] + dt*g
    y[i+1] = y[i] + v[i] * dt

plt.plot(t, y, label="Posição em função do tempo")
plt.legend()
plt.xlabel("Tempo (S)")
plt.ylabel("Posição (m)")
plt.show()

for i in range(n-1):  # calcular o valor da posição em t=2
    if ((t[i] > (2-dt) and t[i+1] < (2+dt))):
        print("dt, t, v = ", dt, t[i+1], y[i+1])
