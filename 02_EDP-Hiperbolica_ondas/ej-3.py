'''
g(x)=sen(x)
b=pi
'''

import numpy as np
from edp_ondas import met_gs_hiperbolicas, verificar_velocidad_maxima


# Condiciones iniciales
a, b = 0, np.pi
c, d = 0, 10
N = 40
M = 400

# Velocidad
v = 0.5

# Tamaño pasos
h = (b-a)/N
k = (d-c)/M
p = (v*k)/h



# Condición de estabilidad (velocidad maxima)
v_max = h/k
v = verificar_velocidad_maxima(v, v_max)

# Inicializar matriz de soluciones
w = np.zeros((N+1, M+1))

def f(x):
    return 0

def g(x):
    return np.sin(x)


# Condiciones de contorno
for i in range(1, N):  # eje X
    x_i = a + i*h
    w[i][0] = f(x_i)
    w[i][1] = w[i][0] + k*g(x_i)

for j in range(1, M):  # eje Y
    y_i = c + j*k
    w[0][j] = 0
    w[N][j] = 0


met_gs_hiperbolicas(a,b,c,d, N,M,p, w)
