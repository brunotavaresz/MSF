import numpy as np
import matplotlib.pyplot as plt

def maximo(xm1, xm2, xm3, ym1, ym2, ym3):
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    a = ym1 / (xab * xac)
    b = -ym2 / (xab * xbc)
    c = ym3 / (xac * xbc)

    xmla = (b + c) * xm1 + (a + c) * xm2 + (a + b) * xm3
    xmax = 0.5 * xmla / (a + b + c)

    xta = xmax - xm1
    xtb = xmax - xm2
    xtc = xmax - xm3

    ymax = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xmax, ymax

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
    
def graphbars(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.bar(x, y)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()
    
def abfourier(tp, xp, it0, it1, nf):
    # cálculo dos coeficientes de Fourier a_nf e b_nf
    #       a_nf = 2/T integral ( x cos nw) dt entre it0 e tt1
    # integracao numerica pelo aproximação trapezoidal
    # input: matrizes tempo tp
    #        posição xp
    #        indices inicial it0
    #        final   it1  (ao fim de um período)
    #        nf índice de Fourier
    # output: af_bf e bf_nf

    dt = tp[1] - tp[0]
    per = tp[it1] - tp[it0]
    ome = 2 * np.pi / per

    s1 = xp[it0] * np.cos(nf * ome * tp[it0])
    s2 = xp[it1] * np.cos(nf * ome * tp[it1])
    st = xp[it0 + 1:it1] * np.cos(nf * ome * tp[it0 + 1:it1])
    soma = np.sum(st)
    q1 = xp[it0] * np.sin(nf * ome * tp[it0])
    q2 = xp[it1 - 1] * np.sin(nf * ome * tp[it1 - 1])
    qt = xp[it0 + 1:it1 - 1] * np.sin(nf * ome * tp[it0 + 1:it1 - 1])
    somq = np.sum(qt)

    intega = ((s1 + s2) / 2 + soma) * dt
    af = 2 / per * intega
    integq = ((q1 + q2) / 2 + somq) * dt
    bf = 2 / per * integq
    return af, bf

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



    lmax = []  # lista com os máximos
    lmin = []   # lista com os mínimos
    for i in range(n):
        if np.abs(x[i - 1]) < np.abs(x[i]) > np.abs(x[i + 1]):
            tmax, xmax = maximo(t[i - 1], t[i], t[i + 1], x[i - 1], x[i], x[i + 1])
            if xmax > 0:
                lmax.append((tmax,xmax))
            else:
                lmin.append((tmax,xmax))

    print("O movimento efetua-se ente {:.2f} e {:.2f}m".format(sum([x[1] for x in lmax])/len(lmax), sum([x[1] for x in lmin])/len(lmin)))

    # Período
    count = 0
    ldif = []
    for i in range(len(lmax)):
        if i != 0:
            ldif.append(lmax[i][0] - lmax[count][0])
            count += 1

    T = sum(ldif) / len(ldif)


    F = 1/T
    print("A frequência do movimento é {:.2f}Hz".format(F))

    # Determinação dos Coeficientes de Fourier
    print(T / dt) 

    a = np.zeros(20)    
    b = np.zeros(20)    
    n = np.zeros(20)    

    for i in range(20):
        n[i] = i
        a[i], b[i] = abfourier(t, x, 0, int(T / dt), i)


    graphbars(n, a, "Coeficiente de Fourier - an", "an", "n")


    graphbars(n, b, "Coeficiente de Fourier - bn", "bn", "n")

    a, b = abfourier(t, x, 0, int(T / dt), 1)

    print("Os coeficientes de Fourier são, aproximadamente, a = {:.2f}, b = {:.2f}.".format(abs(a), abs(b)))

main()