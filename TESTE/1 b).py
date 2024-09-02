import numpy as np
import matplotlib.pyplot as plt

def graphnormal(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.plot(x, y, color='m')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()
    
def graphpoints(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.plot(x, y, color='red', marker="o")
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()

def main():
    # Condições iniciais
    k = 1  # constante elástica
    m = 1  # massa
    v0 = 0  # velocidade inicial
    x0 = 2.2  # posição inicial
    alpha = 0.05

    # Passo temporal para o Método de Euler
    dt = 0.001  # passo temporal
    t0 = 0.00  # tempo inicial
    tf = 15.00  # tempo final
    n = np.int((tf - t0) / dt)  # nº de passos a realizar

    # Criar os arrays para o Método de Euler
    t = np.zeros(n + 1)
    ax = np.zeros(n + 1)
    vx = np.zeros(n + 1)
    x = np.zeros(n + 1)
    Ep = np.zeros(n + 1)
    Em = np.zeros(n + 1)

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

        Em[i] = 0.5*m*vx[i]**2 + Ep[i]



    # Gráfico da lei do movimento
    graphnormal(t, x, "Sistema Mola-Corpo", "t (s)", "x (m)")
    
    graphpoints(t, Em, "Sistema Mola-Corpo", "Tempo (s)", "Energia Mecânica (J)")
    for i in range(n):
        if 3-dt < t[i + 1] < 3+dt:
            print('A energia mecânica do movimento é {:.2f} J.'.format(Em[i+1]))
            break

main()