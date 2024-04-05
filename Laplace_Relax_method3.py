#Tu código tiene algunos errores menores que podemos corregir. Aquí está la versión corregida:

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def laplace_relaxation(N, M, dx, dy, V0_func, boundary_params, tolerance=1e-5, max_iterations=10000):
    """
    Resuelve la ecuación de Laplace utilizando el método de relajación.

    Parámetros:
    - N (int): Número de puntos de la red en la dirección x.
    - M (int): Número de puntos de la red en la dirección y.
    - dx (float): Paso en la dirección x.
    - dy (float): Paso en la dirección y.
    - V0_func (function): Función de condiciones de frontera V0(x, y).
    - boundary_params (dict): Parámetros necesarios para la función V0_func.
    - tolerance (float, opcional): Tolerancia para la convergencia. Valor predeterminado es 1e-5.
    - max_iterations (int, opcional): Número máximo de iteraciones. Valor predeterminado es 10000.

    Retorna:
    - V (numpy.ndarray): Matriz 2D con la solución de la ecuación de Laplace.
    """
    # Inicialización de la matriz de potenciales V
    V = np.zeros((N, M))

    # Condiciones de frontera
    for i in range(N):
        V[i, 0] = V0_func(i*dx, 0, **boundary_params)  # borde inferior
        V[i, -1] = V0_func(i*dx, dy*(M-1), **boundary_params)  # borde superior
    for j in range(M):
        V[0, j] = V0_func(0, j*dy, **boundary_params)  # borde izquierdo
        V[-1, j] = V0_func(dx*(N-1), j*dy, **boundary_params)  # borde derecho

    # Iteraciones hasta convergencia
    for _ in range(max_iterations):
        V_old = V.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + V_old[i, j+1] + V_old[i, j-1])

        # Comprobación de convergencia
        if np.max(np.abs(V - V_old)) < tolerance:
            break

    return V

def V0(x, y, V0_bottom, V0_top, V0_left, V0_right):
    """
    Define las condiciones de frontera V0(x, y).

    Parámetros:
    - x (float): Coordenada en x.
    - y (float): Coordenada en y.
    - V0_bottom (float): Valor en el borde inferior (y=0).
    - V0_top (float): Valor en el borde superior (y=b).
    - V0_left (float): Valor en el borde izquierdo (x=0).
    - V0_right (float): Valor en el borde derecho (x=a).

    Retorna:
    - float: Valor del potencial en el punto (x, y).
    """
    if x == 0:
        return V0_left
    elif x == a:
        return V0_right
    elif y == 0:
        return V0_bottom
    elif y == b:
        return V0_top
    else:
        return 0 # para puntos dentro del dominio D

def analytical_solution(x, y, V0, a, b):
    """
    Calcula la solución analítica de la ecuación de Laplace.

    Parámetros:
    - x (numpy.ndarray): Coordenadas en x.
    - y (numpy.ndarray): Coordenadas en y.
    - V0 (float): Valor de V0.
    - a (float): Longitud en x.
    - b (float): Longitud en y.

    Retorna:
    - V_analytical (numpy.ndarray): Solución analítica de la ecuación de Laplace.
    """
    V_analytical = np.zeros_like(x)
    for n in range(1, 100):
        V_analytical += ((-4 * V0 / np.pi) * (np.sinh(np.pi * n * (x - a) / b) * np.sin(np.pi * n * y / b))) / (n * np.sinh(np.pi * n * a / b))
    return V_analytical


if __name__ == "__main__":
    # Parámetros del problema
    N = int(input("Ingrese el número de puntos de la red en la dirección x (N): "))
    M = int(input("Ingrese el número de puntos de la red en la dirección y (M): "))
    dx = float(input("Ingrese el paso en la dirección x: "))
    dy = float(input("Ingrese el paso en la dirección y: "))
    a = N * dx  # longitud en x
    b = M * dy  # longitud en y

    # Condiciones de frontera
    V0_bottom = float(input("Ingrese el valor de V0 en el borde inferior (y=0): "))
    V0_top = float(input("Ingrese el valor de V0 en el borde superior (y=b): "))
    V0_left = float(input("Ingrese el valor de V0 en el borde izquierdo (x=0): "))
    V0_right = float(input("Ingrese el valor de V0 en el borde derecho (x=a): "))

    boundary_params = {
        'V0_bottom': V0_bottom,
        'V0_top': V0_top,
        'V0_left': V0_left,
        'V0_right': V0_right
    }

    # Resolución del problema
    V = laplace_relaxation(N, M, dx, dy, V0, boundary_params)
    print(V)

    # Calculando la solución analitica
    x = np.linspace(0, a, N)
    y = np.linspace(0, b, M)
    X, Y = np.meshgrid(x, y)
    V_analytical = analytical_solution(X, Y, V0_bottom, a, b)
    V_analytical_mean = np.mean(V_analytical)
    print("El valor final del potencial promedio (analitico) es:", V_analytical_mean)

    # Calcular el promedio de los potenciales en toda la malla
    promedio_potencial = np.mean(V)
    print("El valor final del potencial promedio (numérico) es:", promedio_potencial)

    # Cálculo del error porcentual
    error_porcentual = np.abs((promedio_potencial - V_analytical_mean) / V_analytical_mean) * 100
    print("El error porcentual es :", error_porcentual)

    # Visualización de la solución (opcional)
    plt.contourf(X, Y, V, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución ec. Laplace Método de relajación (2D)')
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, V, cmap='coolwarm')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V')
    ax.set_title('Solución ec. Laplace Método de relajación (3D)')
    plt.show()

    # Visualización de la solución analítica
    plt.contourf(X, Y, V_analytical, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución analítica de la ec. Laplace (2D)')
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, V_analytical, cmap='coolwarm')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V')
    ax.set_title('Solución analítica de la ec. Laplace (3D)')
    plt.show()