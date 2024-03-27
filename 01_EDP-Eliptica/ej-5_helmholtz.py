'''
EC. HELMHOLTZ
0<x<1, 0<y<1
Au + u*L^2 = 0
u(x,0)=u(x,1)=u(0,y)=0
u(1,y)=1
L = 1, 300, 1000
'''


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Condiciones iniciales
a, b = 0, 1
c, d = 0, 1
N = 20
M = 20
L = 300

# Tamaño pasos
h = (b-a)/N
k = (d-c)/M

# Matriz de soluciones
w = np.zeros((N+1, M+1))

# Condiciones frontera
def f(i, j):
    return 0

w[:][0] = 0  # u(x,0)
w[:][M] = 0  # u(x,1)
w[0][:] = 0  # u(0,y)
w[N][:] = 1  # u(1,y)


# Iteración de Gauss-Seidel
for _ in range(100):
    for i in range(1, N):
        for j in range(1, M):
            #w[i][j] = (k**2 * (w[i+1][j] + w[i-1][j]) + h**2 * (w[i][j+1] + w[i][j-1])) / (2 * (k**2 + h**2))
            w[i][j] = ( k**2 * (w[i+1][j] + w[i-1][j])+ h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i,j)) / (2*(h**2+k**2) - (h*k*L)**2)
        
# Convierte la solución a un array de NumPy para la visualización
w_np = np.array(w)

# Crea una malla para las coordenadas x e y
x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
X, Y = np.meshgrid(x, y)

# Visualización en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, w_np, cmap='viridis', edgecolor='none')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('U(x, y)')
ax.set_title('Solución ')

# Añade una barra de colores que mapea los valores a colores
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
