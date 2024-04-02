'''
f(x) = exp(-(x-b/2)**2)
'''


import numpy as np
import matplotlib.pyplot as plt


# PARÁMETROS
a, b = 0, 5
c, d = 0, 10
N = 40
M = 400

# conductividad
v = 0.5

# Tamaño del paso
h = (b-a)/N
k = (d-c)/M 


# MATRIZ SOLUCIONES
w = np.zeros((M+1, N+1))


# CONDICIONES FRONTERA
def f(x):
    return np.exp(-(x-b/2)**2)

for j in range(1, M):  # eje t
    y_i = (c+j*k)
    w[j][0] = 0
    w[j][N] = 0

for i in range(1, N):  # eje x
    x_i = a + i*h
    w[0][i] = f(x_i)
    w[1][1] = 0


# lambda
L = k*v**2/h**2

# Método Diferencias progresivas
for j in range(0, M):
    for i in range(1, N):
        w[j+1][i]= (1-2*L)*w[j][i] + L*(w[j][i+1]+w[j][i-1])

# Malla -------------------------------------------------------------------
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
