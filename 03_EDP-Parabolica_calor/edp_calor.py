import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel_iter_calor(a,b,c,d, N,M,h,k, w,v):
    '''
    w --> (M+1, N+1)
    '''
    # Implementación del método de Gauss-Seidel iterativo
    for j in range(0, M):
        for i in range(1, N):
            w[j+1][i]= (1-2*k*v**2/h**2)*w[j][i] + (k*v**2/h**2)*(w[j][i+1]+w[j][i-1])

    # Malla
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    x, y = np.meshgrid(x, y)

    # Creación de la figura 3D y los ejes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficación de la superficie
    ax.plot_surface(x, y, w, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U(x,t)')
    ax.set_title('Solución Ec. Calor')

    plt.show()



def met_calor_ana(a,b,c,d, N,M,h,k, w,v):
    '''
    i (1,N) --> x
    j (1,M) --> y
    '''
    # Implementación del método de Gauss-Seidel (ITERADO)
    for _ in range(400):  # Iteraciones en el tiempo
        for j in range(1, M):  
            for i in range(1, N):  
                w[i][j] = (1-2*k*v**2/h**2)*w[i-1][j] + (k*v**2/h**2)*(w[i-1][j+1] + w[i][j-1] + w[i-1][j-1] + w[i-1][j+1])/4

    w_np = np.array(w)

    #Mostramos la grafica de la matriz
    #definir coordenadas
    x = np.linspace(a, b, N+1)
    y = np.linspace(b, d, M+1)
    X, Y = np.meshgrid(x, y)


    #graficar
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, w_np.T, cmap='viridis') #el .T es para que se adapte a los valores

    #etiquetas
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('U(x,y)')
    ax.set_title('Solución Ec. de Calor por Met. Iterativo Gauss-Seidel')

    #mostramos
    plt.show()

