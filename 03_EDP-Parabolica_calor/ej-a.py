#Ec del Calor con Gauss-Seidel
import numpy as np
from edp_calor import met_calor_ana


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


#Matriz
# Inicializar matriz w con dimensiones N x M
w = np.zeros((N+1, M+1))


# # Condiciones contorno (bordes matriz)

def f(x):
    #Cambia dependiendo del ejercicio
    x = a + i*h
    return np.exp(-(x-b/2)**2)

for i in range(1, N):
    x_i = a + i*h
    w[i][0] = f(x_i)
    w[i][1] = 0

for j in range(1, M):
    y_i = c + j*k
    w[0][j] = 0
    w[N][j] = 0


met_calor_ana(a,b,c,d, N,M,h,k, w,v)
