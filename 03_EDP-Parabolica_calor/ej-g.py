import numpy as np
from edp_calor import gauss_seidel_iter_calor

# Entrada de parámetros
# Condiciones iniciales
a, b = 0, 5
c, d = 0, 10
N = 40
M = 400

# conductividad
v = 0.5

#Tamaño pasos
h = (b-a)/N
k = (d-c)/M 

# Inicializar matriz w con dimensiones N x M
w = np.zeros((M+1, N+1))

# Definición de la función f(x)
def f(x):
    return np.exp(-(h*i-b/2)**2)

# Condiciones iniciales y de frontera
for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

for i in range(1, N):
    w[0][i] = f(h*i)


gauss_seidel_iter_calor(a,b,c,d, N,M,h,k, w,v)

