''' METODO GAUSS-SEIDEL PARA ECUACIONES DIFERENCIALES PARCIALES ELIPTICAS
Diferencias finitas'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def met_gs_elipticas(a,b,c,d, N,M,h,k, w,f):

    # Iteración Gauss-Seidel
    for _ in range(100):  # sistema lineal
        for i in range(1, N):
            for j in range(1, M):
                w[i][j] = ( k**2 * (w[i+1][j] + w[i-1][j])+ h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i, j))/(2*(h**2 + k**2))

    w_np = np.array(w)

    # Malla de puntos
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    X, Y = np.meshgrid(x, y)

    # Visualización 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, w_np, cmap='viridis', edgecolor='none')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('U(x,y)')
    ax.set_title('Solución EDP Elíptica por Met. Gauss-Seidel')

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()
