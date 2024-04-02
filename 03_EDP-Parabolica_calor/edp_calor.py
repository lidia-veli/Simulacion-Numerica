import numpy as np
import matplotlib.pyplot as plt


def difer_progres_calor(a,b,c,d, N,M,h,k, w,v):
    '''
    w --> (M+1, N+1)
    '''
    # lambda
    L = k*v**2/h**2

    # Método Diferencias progresivas
    for j in range(0, M):
        for i in range(1, N):
            w[j+1][i]= (1-2*L)*w[j][i] + L*(w[j][i+1]+w[j][i-1])

    # Malla
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    x, y = np.meshgrid(x, y)

    # Creación de la figura 3D y los ejes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficación de la superficie
    ax.plot_surface(x, y, w, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x,t)')
    ax.set_title('Solución Ec. Calor')

    plt.show()


def difer_regres_calor(a,b,c,d, N,M,h,k, w,v):
    '''
    w --> (M+1, N+1)
    '''
    # lambda
    L = k*v**2/h**2

    # Gauss-Seidel
    for _ in range(100):  # sistema lineal
        for i in range(1, N):
            for j in range(1, M):
                w[i][j] = (L*(w[i+1][j]+w[i-1][j-1]) + w[i][j-1]) / (1+2*L)


    # Malla
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    x, y = np.meshgrid(x, y)

    # Creación de la figura 3D y los ejes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficación de la superficie
    ax.plot_surface(x, y, w, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x,t)')
    ax.set_title('Solución Ec. Calor')

    plt.show()
