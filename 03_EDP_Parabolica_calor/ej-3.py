'''
f(x) = exp(-(x-2.5)**2)
'''


import numpy as np
import matplotlib.pyplot as plt


# PARÁMETROS
a, b = 0, 5
c, d = 0, 10
N, M = 40, 400  # tienen que ser iguales

# conductividad
v = 0.5

# Tamaño del paso
h = (b-a)/N
k = (d-c)/M 


# MATRIZ SOLUCIONES
w = np.zeros((M+1, N+1))


# CONDICIONES FRONTERA
def f(x):
    return np.exp(-(x-2.5)**2)

for i in range(1,N):  # eje x
    x_i = a + i*h
    w[0][i] = f(x_i)

for j in range(1,M):  # eje t
    y_i = (c+j*k)
    w[j][0] = 0
    w[j][N] = 0


# Gauss-Seidel
for _ in range(100):  # sistema lineal
    for i in range(1,N):
        for j in range(1,M):
            w[j][i] = ( (k/h**2)*(w[j][i+1]+w[j][i-1]) + (1+h*i)*w[j-1][i] ) / (1 + h*i - k*h*i + 2*k/h**2)


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
