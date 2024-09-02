# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])
X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])


fig, ax = plt.subplots()
ax.plot(L, X ,'r.')
ax.set_xlabel('L (cm)')
ax.set_ylabel("X (cm)")
ax.set_title('L vs. X')
ax.grid()
plt.show()

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


m, b, r2, dm, db = lin_reg(x=L, y=X, print_res=1)

X_fit = L * m + b

fig, ax =  plt.subplots()
ax.plot(L, X, "r.")
ax.plot(L, X_fit, "b")
ax.set_xlabel("L (cm)")
ax.set_ylabel("X (cm)")
ax.set_title("L vs. X")
ax.grid()
plt.show()


    