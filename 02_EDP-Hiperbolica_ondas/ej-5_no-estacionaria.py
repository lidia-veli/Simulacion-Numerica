'''
ONDA NO ESTACIONARIA
f=g=0
w[j][0]=3*sin(k*j)

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
v_max = h/k  # (bM)/(dN)
v = verificar_velocidad_maxima(v, v_max)

# Inicializar matriz de soluciones
w = np.zeros((N+1, M+1))


# Condiciones contorno
def f(x):
    return 0

def g(x):
    return 0

for i in range(1, N):  # eje X
    x_i = a + i*h
    w[i][0] = f(x_i)
    w[i][1] = w[i][0] + k*g(x_i)  

for j in range(1, M):  # eje Y
    y_i = c + j*k
    w[0][j] = 3*np.sin(k*j)
    w[N][j] = 0


met_gs_hiperbolicas(a,b,c,d, N,M,p, w)
