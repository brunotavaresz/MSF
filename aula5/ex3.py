# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 09:26:54 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

x0, y0 = 0, 0
v1 = [3, 4]
v2 = [1 , -3/4]

fig, ax = plt.subplots()
ax.plot(x0, y0, 'o', markersize= 8)

ax.arrow(x0,y0,v1[0],v1[1],color='r',width=0.03)
ax.arrow(x0, y0, v2[0], v2[1], color='r', width =0.03)
ax.set_aspect('equal')
plt.show()


#theta = [np.pi/2, np.cos(60), ]

##_---------------------------------------------------------------------------

conv = np.pi/100
theta = np.array([np.pi/2, 60*conv, -np.pi*7/6, 310 * conv])
F = 5
x0 = 0
y0 = 0
vet = np.array([F * np.cos(theta), F * np.sin(theta)])

fig, ax = plt.subplots()
for i in range(len(theta)):
    ax.arrow(x0, y0, vet[0,i], vet[1, i], color='r', width = 0.03)
    ax.set_aspect('equal')
plt.show()

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

t=np.linspace(1,4,4)
r = np.array([2*t, t**2])
v = np.array([np.ones(len(t),)*2, 2*t])
x0 = 0
y0 = 0

fig, ax = plt.subplots(1,2)
for i in range(len(t)):
    ax[0].arrow(x0, y0, r[0,i], r[1, i], width = 0.05)
    ax[1].arrow(r[0,i], r[1, i], v[0,i], v[1, i], width = 0.05)
ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
plt.show()

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<