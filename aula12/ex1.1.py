import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.05
F0 = 7.5
w = -1
wf = np.sqrt(k/m)

t0 = 0
tf = 400
dt = 0.001
n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
x = np.empty(n)
v = np.empty(n)
v[0] = 0
x[0] = 4

for i in range(n-1):
    a[i] = (-k*x[i]/m) - (b*v[i]/m) + (F0*np.cos(t[i])/m)
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt        

A_est = (F0 / m) / np.sqrt((wf **2 - w **2) ** 2 + (b*wf/m)**2)
    
x_est = A_est * np.cos(wf * t)


plt.figure()                                                                               
plt.plot(t, x)
plt.grid() 


plt.plot(t,x_est, 'r-', label = 'analytico')
plt.show()


