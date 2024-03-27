'''
0<x<1, 0<y<1
Au = 0 
u(0,y) = u(1,y) = u(x,0) = u(x,1) = 0
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

# Crear matriz donde guardaremos las soluciones
w = np.zeros((N+1, M+1))

# Condiciones de frontera
def f(i, j):
    '''funcion lagrangiano'''
    x = (a+i*h)
    y = (c+j*k)
    return 0

for i in range(N+1):
    x = (a+i*h)
    w[i][0] = 0  # u(x,0)
    w[i][M] = 0  # u(x,1)

for j in range(M+1):
    y = (c+j*k)
    w[0][j] = 0   # u(0,y)
    w[N][j] = 0  # u(1,y)



if __name__ == '__main__':
    met_gs_elipticas(a,b,c,d, N,M,h,k, w,f)
