import matplotlib.pyplot as plt
import numpy as np
import sys


def verificar_velocidad_maxima(v, v_max):
    if v > v_max:
        print(f'v={v} debe ser menor que v_max={v_max}')
        sys.exit(1)
    return v


def met_gs_hiperbolicas(a,b,c,d, N,M,p, w):

    # Implementación de Gauss-Seidel para la ecuación hiperbólica
    for j in range(1, M):
        for i in range(1, N):
                w[i][j+1] = 2 *(1 - p**2) * w[i][j] + (p**2)*(w[i+1][j] + w[i-1][j]) - w[i][j-1]
                
    # Malla puntos
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    X, Y = np.meshgrid(x, y)

    # Visualización 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, w.T, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y (tiempo)')
    ax.set_zlabel('U(x,y)')
    ax.set_title('Solución Ec. de Ondas por Met. Gauss-Seidel')

    plt.show()
