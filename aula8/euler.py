import matplotlib.pyplot as plt


k = 1.0 
m = 1.0 
x0 = 4.0 
v0 = 0.0 
dt = 0.1 
t_max = 10.0 


x_list = [x0]
v_list = [v0]
t_list = [0]


for i in range(int(t_max / dt)):
    x = x_list[-1]
    v = v_list[-1]
    a = -(k / m) * x
    x_new = x + v * dt
    v_new = v + a * dt
    x_list.append(x_new)
    v_list.append(v_new)
    t_list.append((i + 1) * dt)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(t_list, x_list)
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Posição (m)')
ax1.set_title('Posição do corpo ligado à mola')
ax2.plot(t_list, v_list)
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Velocidade (m/s)')
ax2.set_title('Velocidade do corpo ligado à mola')
plt.show()