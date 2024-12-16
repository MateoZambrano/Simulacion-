import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Función que representa el sistema de ecuaciones no lineales
def system_of_equations(vars, eqs):
    x, y = vars
    res = []
    for eq in eqs:
        res.append(eval(eq))
    return res
def Sistema_No_lineales():
    # Solicitar al usuario que ingrese las ecuaciones
    print("Ingresa el sistema de ecuaciones de la forma f(x, y) = 0:")
    n = int(input("¿Cuántas ecuaciones tiene el sistema? (Por ejemplo, 2): "))
    equations = []
    for i in range(n):
        eq = input(f"Ecuación {i+1} (por ejemplo, x**2 + y**2 - 4): ")
        equations.append(eq)

    # Establecer una suposición inicial
    initial_guess = [1, 1]  # Puedes cambiar este valor si es necesario

    # Resolver el sistema de ecuaciones
    solution = optimize.fsolve(system_of_equations, initial_guess, args=(equations))

    # Mostrar la solución
    print(f"La solución es: x = {solution[0]}, y = {solution[1]}")

    # Graficar las ecuaciones y la solución
    # Definir el rango de valores para x y y
    x_vals = np.linspace(-3, 3, 400)
    y_vals = np.linspace(-3, 3, 400)

    # Crear una malla de puntos para evaluar las ecuaciones
    X, Y = np.meshgrid(x_vals, y_vals)

    # Graficar cada ecuación
    for eq in equations:
        Z = eval(eq.replace("x", "X").replace("y", "Y"))
        plt.contour(X, Y, Z, levels=[0], label=eq)

    # Graficar la solución
    plt.plot(solution[0], solution[1], 'go', label=f"Solución: ({solution[0]:.2f}, {solution[1]:.2f})")

    # Etiquetas y título
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Sistema de Ecuaciones No Lineales")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    Sistema_No_lineales()