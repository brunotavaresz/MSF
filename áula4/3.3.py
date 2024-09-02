# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 23:49:52 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 0
t0 = 0
tf = 4
g = -9.8
dt = 0.001 

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)
v = np.empty(n)


for i in range(n-1):  
    v[i+1] = v[i] + dt*g

plt.plot(t, v, label="Aceleração")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.show()

for i in range(n-1):  # calcular o valor da velocidade em t=3s
    if ((t[i] > (3-dt) and t[i+1] < (3+dt))):
        print("dt, t, v = ", dt, t[i+1], v[i+1])