'''
Ecuación de Poisson
0<x<1, 0<y<1
Au = xy(1-x)(1-y) 
u(0,y) = u(1,y) = 0
u(x,0) = u(x,1) = 0
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from edp_eliptica import met_gs_elipticas

# Condiciones iniciales
a, b = 0, 1
c, d = 0, 1
N, M = 20, 20

# Tamaño del paso
h = (b-a)/N
k = (d-c)/M

# Matriz de soluciones
w = np.zeros((N+1, M+1))

# Condiciones de frontera
def f(i, j):
    '''lagrangiano'''
    x = (a+i*h)
    y = (c+j*k)
    return x*y*(1-x)*(1-y)

w[:][0] = 0  # u(x,0)
w[:][M] = 0  # u(x,1)
w[0][:] = 0  # u(0,y)
w[N][:] = 0  # u(1,y)


if __name__ == '__main__':
    met_gs_elipticas(a,b,c,d, N,M,h,k, w,f)
