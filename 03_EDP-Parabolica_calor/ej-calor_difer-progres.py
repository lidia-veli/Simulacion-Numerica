'''
f(x) = exp(-(x-b/2)**2)
'''


import numpy as np
import matplotlib.pyplot as plt

from edp_calor import difer_progres_calor


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


difer_progres_calor(a,b,c,d, N,M,h,k, w,v)
