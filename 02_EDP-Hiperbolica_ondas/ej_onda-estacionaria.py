import numpy as np
from edp_ondas import gauss_seidel_ondas, verificar_velocidad_maxima


# Parámetros
a, b = 0, np.pi  # eje x
c, d = 0, 40   # eje t
N = 40
M = 400

# Velocidad
v = 0.4
# 0.1: 0.5 ciclos
# 0.2: 1+ ciclo
# 0.4: 2.5 ciclos

# Tamaño pasos
h = (b-a)/N
k = (d-c)/M
p = (v*k)/h


# Condición de estabilidad (velocidad maxima)
v_max = h/k  # (bM)/(dN)
v = verificar_velocidad_maxima(v, v_max)

# Inicializar matriz de soluciones
w = np.zeros((M+1, N+1))


# Condiciones contorno
def f(x):
    # modificable
    return x*(b-x)

def g(x):
    # modificable
    return 0

for i in range(1,N):  # eje X
    x_i = a + i*h
    w[0][i] = f(x_i)  # frontera inferior
    w[1][i] = w[0][i] + k*g(x_i)  # frontera superior

for j in range(1,M):  # eje t
    #y_i = c + j*k
    w[j][0] = 0  # frontera ezquierda
    w[j][N] = 0  # frontera derecha


gauss_seidel_ondas(a,b,c,d, N,M,p, w)
