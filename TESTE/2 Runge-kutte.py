import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(dt, t, x, v, b, p, F0, omega, m, k):
    k1x = dt * v
    k1v = dt * k/m * (-4*p*x**3 - b*v + F0*np.cos(omega*t))
    
    k2x = dt * (v + k1v/2)
    k2v = dt * k/m * (-4*p*(x + k1x/2)**3 - b*(v + k1v/2) + F0*np.cos(omega*(t + dt/2)))
    
    k3x = dt * (v + k2v/2)
    k3v = dt * k/m *(-4*p*(x + k2x/2)**3 - b*(v + k2v/2) + F0*np.cos(omega*(t + dt/2)))
    
    k4x = dt * (v + k3v)
    k4v = dt * k/m *(-4*p*(x + k3x)**3 - b*(v + k3v) + F0*np.cos(omega*(t + dt)))
    
    x_new = x + (k1x + 2*k2x + 2*k3x + k4x) / 6
    v_new = v + (k1v + 2*k2v + 2*k3v + k4v) / 6
    
    return x_new, v_new


b = 0.2  
p = 0.15  
F0 = 7.5 
omega = 1.0  
k= 1
m = 1


x0 = 0.0  
v0 = 0.0  


t0 = 0.0  
tf = 10.0  
dt = 0.01  


t_values = np.arange(t0, tf, dt)
x_values = np.zeros_like(t_values)
v_values = np.zeros_like(t_values)


x_values[0] = x0
v_values[0] = v0


for i in range(1, len(t_values)):
    t = t_values[i-1]
    x = x_values[i-1]
    v = v_values[i-1]
    
    x_new, v_new = runge_kutta4(dt, t, x, v, b, p, F0, omega,m, k)
    
    x_values[i] = x_new
    v_values[i] = v_new

# Plot dos resultados
plt.plot(t_values, x_values, label='Posição')

plt.xlabel('Tempo')
plt.legend()
plt.show()
