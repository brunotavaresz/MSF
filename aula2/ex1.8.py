# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:24:18 2023

@author: User

"""

import numpy as np
import matplotlib.pyplot as plt


T = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

plt.scatter(T, E)
plt.xlabel("Temperatura (Kelvin)")
plt.ylabel("Energia (Joules)")
plt.show()
x = np.log(T)
y = np.log(E)

def lin_reg(x, y, print_res):
    
    if len(x) != len(y):
        raise ValueError('ERROR: x and y must be the same length in lin_reg(x, y)!')
    N = len(x)
    if N < 3:
        raise ValueError('ERROR: N must be higher than 2')
    
    # summations
    s_x = np.sum(x)
    s_y = np.sum(y)
    s_xy = np.sum(x * y)
    s_x2 = np.sum(x ** 2)
    s_y2 = np.sum(y ** 2)
    
    # linear regression parameters
    m = (N * s_xy - s_x * s_y) / (N * s_x2 - s_x ** 2)
    b = (s_x2 * s_y - s_x * s_xy) / (N * s_x2 - s_x ** 2)
    
    # squared correlation coefficient
    r2 = ((N * s_xy - s_x * s_y)**2) / ((N * s_x2 - s_x ** 2)*(N * s_y2 - s_y ** 2))

    # errors
    dm = np.abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    db = dm * np.sqrt(s_x2 / N)
    
    if print_res == 1:
        print("s_x, s_y, s_xy, s_x2, s_y2, m, b, r2, dm, db:")
        print([s_x, s_y, s_xy, s_x2, s_y2, m, b, r2, dm, db])
    
    return m, b, r2, dm, db


m, b, r2, dm, db = lin_reg(x, y, 0)
logEfit = m * x + b
plt.plot(x,y,'.')
# a = np.polyfit(np.log(x), np.log(y), 1)

plt.plot(x, logEfit)

plt.show(x, np.exp(logEfit))


