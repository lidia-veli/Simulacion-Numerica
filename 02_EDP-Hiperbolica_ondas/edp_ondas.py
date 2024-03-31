import matplotlib.pyplot as plt
import numpy as np
import sys


def verificar_velocidad_maxima(v, v_max):
    if v > v_max:
        print(f'v={v} debe ser menor que v_max={v_max}')
        sys.exit(1)
    return v


def gauss_seidel_ondas(a,b,c,d, N,M,p, w):
    '''w = (M+1,N+1)'''

    # Implementación de Gauss-Seidel para la ecuación hiperbólica
    for j in range(1, M):
        for i in range(1, N):
            w[j+1][i] = 2*(1-p**2)*w[j][i] + (p**2)*(w[j][i+1] + w[j][i-1]) - w[j-1][i]

    # Malla puntos
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)  # tiempo
    X, Y = np.meshgrid(x, y)

    # Visualización 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, w, cmap='viridis')

    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('Y(x,t)')
    ax.set_title('Solución Ec. Ondas por Met. Gauss-Seidel')

    plt.show()




def met_gs_hiperbolicas(a,b,c,d, N,M,p, w):
    '''w = (N+1,M+1)'''

    # Implementación de Gauss-Seidel para la ecuación hiperbólica
    for j in range(1, M):
        for i in range(1, N):
                w[i][j+1] = 2 *(1-p**2) * w[i][j] + (p**2)*( w[i+1][j] + w[i-1][j])  - w[i][j-1]
                
    # Malla puntos
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    X, Y = np.meshgrid(x, y)

    # Visualización 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, w.T, cmap='viridis')

    ax.set_xlabel('x')
    ax.set_ylabel('y (tiempo)')
    ax.set_zlabel('U(x,y)')
    ax.set_title('Solución Ec. Ondas por Met. Gauss-Seidel')

    plt.show()
