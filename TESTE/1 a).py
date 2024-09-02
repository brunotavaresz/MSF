import numpy as np
import matplotlib.pyplot as plt


def graphnormal(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.plot(x, y, color='m')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()
    
def main():

    k = 1 
    m = 1  
    v0 = 0  
    x0 = -8 
    alpha = 0.05

    
    dt = 0.001  
    t0 = 0.00  
    tf = 15.00 
    n = np.int((tf - t0) / dt)  

    # Criar os arrays para o Método de Euler
    t = np.zeros(n + 1)
    ax = np.zeros(n + 1)
    vx = np.zeros(n + 1)
    x = np.zeros(n + 1)
    Ep = np.zeros(n + 1)

    # Iniciar os arrays
    x[0] = x0
    vx[0] = v0

    # Método de Euler-Cromer
    for i in range(n):
        t[i+1] = t[i] + dt

        ax[i] = -(k/m)*x[i] - (3*alpha*(x[i]**2))/m

        vx[i+1] = vx[i] + ax[i]*dt

        x[i+1] = x[i] + vx[i+1]*dt

        Ep[i] = 0.5*k*(x[i]**2) + alpha*(x[i]**3)


    # Gráfico Energia Potencial
    graphnormal(x, Ep, "Sistema Mola-Corpo", "x (m)", "Energia Potencial (J)")

main()
