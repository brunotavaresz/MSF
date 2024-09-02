# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:19:41 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

vA = 70/3.6
aP = 2

t = np.linspace(0, 20)

plt.plot(t, vA * t)
plt.show()

plt.plot(t, vA*t, label="Carro A")
plt.plot(t, 0.5*aP*(t**2), label="Policia")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.show()

t_cruza = 70/3.6
x = t_cruza ** 2

print("Tempo de cruzamento: ", t_cruza)
print("Distancia de cruzamento: ", x)
