#import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

def diferencias_finitas():
    """
    Resuelve una ecuación diferencial de segundo orden utilizando diferencias finitas.
    """
    # Solicitar datos al usuario
    L = float(input("Ingresa la longitud del dominio (L): "))
    N = int(input("Ingresa el número de puntos en la malla (N): "))

    print("Define la función f(x) (por ejemplo: sin(np.pi * x), x**2): ")
    func_input = input("f(x) = ")
    
    # Definir función f(x)
    f = lambda x: eval(func_input)
    
    # Calcular el tamaño del paso
    h = L / (N + 1)

    # Crear malla
    x = np.linspace(0, L, N + 2)
    print(f"Número de puntos en la malla (incluyendo extremos): {len(x)}")
    print(f"Distribución de puntos: {x}")

    # Construir el sistema de ecuaciones
    A = np.zeros((N, N))
    b = np.zeros(N)

    for i in range(N):
        A[i, i] = -2 / h**2
        if i > 0:
            A[i, i - 1] = 1 / h**2
        if i < N - 1:
            A[i, i + 1] = 1 / h**2
        b[i] = f(x[i + 1])

    # Resolver el sistema
    u = np.linalg.solve(A, b)

    # Añadir las condiciones de frontera
    u = np.concatenate(([0], u, [0]))

    # Dibujar el eje x (horizontal) en y=0
    plt.axhline(0, color="black", linewidth=1, linestyle="-")  # Eje x
    
    # Dibujar el eje y (vertical) en x=0
    plt.axvline(0, color="black", linewidth=1, linestyle="-")  # Eje y
    
    # Graficar la solución
    plt.plot(x, u, label='Solución numérica')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.title('Solución de la ecuación diferencial 1D')
    plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
    plt.grid(True)
    plt.legend()
    plt.show()

# Llamar a la función
if __name__ == "__mian__":
    diferencias_finitas()