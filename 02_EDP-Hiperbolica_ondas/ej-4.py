'''
f(x)=0 si x no pertenece a [1,3]
f(x)=1 si x pertenece a [1,3]

b=6, d=24, N=600, M=2400, v=0.5
'''

import numpy as np
from edp_ondas import met_gs_hiperbolicas, verificar_velocidad_maxima


# Condiciones iniciales
a, b = 0, 6
c, d = 0, 24
N = 600
M = 2400

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


# Condiciones contorno
def f(x):
    if x>=1 and x<=3:
        return 1
    else:
        return 0

def g(x):
    return 0

for i in range(1, N):  # eje X
    x_i = a + i*h
    w[i][0] = f(x_i)
    w[i][1] = w[i][0] + k*g(x_i)  

for j in range(1, M):  # eje Y
    y_i = c + j*k
    w[0][j] = 0
    w[N][j] = 0


met_gs_hiperbolicas(a,b,c,d, N,M,p, w)
