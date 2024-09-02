# Um corpo de massa 1 kg move-se num oscilador duplo, com dois pontos de equilíbrio, 𝑥𝑒𝑞 = 1.5 m. O oscilador
# tem a energia potencial 𝐸𝑝 = 1/2 * 𝑘 (𝑥^2 - 𝑥𝑒𝑞^2)^2
# exerce no corpo a força 𝐹𝑥= − 2 𝑘 (𝑥^2 - 𝑥𝑒𝑞^2) * x
# onde 𝑘 = 1 N/m.

# Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor que 1 J?

import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
w = np.sqrt(k/m)
t0 = 0
tf = 100
dt = 0.0001
n = int((tf-t0)/dt)
xeq = 1.5
Em = 0.75

t = np.linspace(t0, tf, n+1)

a = np.empty(n+1)

x = np.empty(n+1)
x[0] = np.sqrt(np.sqrt((2*Em)/k) + xeq**2)

v = np.empty(n+1)
v[0] = 0

for i in range(n):
    a[i] = (-2*k*(x[i]**2-xeq**2)*x[i])/m

    v[i+1] = v[i] + a[i]*dt

    x[i+1] = x[i] + v[i+1]*dt

plt.plot(t, x)
plt.show()
