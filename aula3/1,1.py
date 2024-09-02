# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:37:28 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

conv = 1e3/3.6e3 #km to ms

v0_A = 70 * conv
v0_B = 0
a0_B = 2

dt = 0.01
t0 = 0
tf = 50
Nt = int((tf-t0)/dt+1)
t = np.linspace(0, tf, Nt)

x_A = np.zeros((Nt,))
v_A = np.ones((Nt,)) * v0_A
x_B = np.zeros((Nt,))
v_B = np.append([v0_B], np.zeros((Nt-1,)))

for i in range(Nt-1):
    x_A[i + 1] = x_A[i] + v_A[i]* dt
    v_B[i + 1] = v_B[i] + a0_B * dt
    x_B[i + 1] = x_B[i] + v_B[i] * dt
    
plt.figure()
plt.plot(t, x_A, "r-", label="Carro A")
plt.plot(t, x_B, "b-", label="Carro de pratulha")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.title("Trajetórias dos carros (Metodo de Euler)")
plt.legend()
plt.grid()
plt.show()