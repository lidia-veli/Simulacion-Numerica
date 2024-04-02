'''
f(x) = exp(-(x-b/2)**2)
'''


import numpy as np
import matplotlib.pyplot as plt

from edp_calor import difer_regres_calor


# PARÁMETROS
a, b = 0, 5
c, d = 0, 10
N, M = 40, 40  # tienen que ser iguales

# conductividad
v = 0.5

# Tamaño del paso
h = (b-a)/N
k = (d-c)/M 


# MATRIZ SOLUCIONES
w = np.zeros((N+1, M+1))


# CONDICIONES FRONTERA
def f(x):
    return np.exp(-(x-b/2)**2)

for i in range(N+1):  # eje x
    x_i = a + i*h
    w[i][0] = f(x_i)
    w[i][M] = 0

for j in range(M+1):  # eje t
    y_i = (c+j*k)
    w[0][j] = 0
    w[N][j] = 0


difer_regres_calor(a,b,c,d, N,M,h,k, w,v)
