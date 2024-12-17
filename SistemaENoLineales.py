import numpy as np
import matplotlib.pyplot as plt

# Método de bisección
def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    """
    Método de bisección para encontrar la raíz de una función no lineal en [a, b].

    Args:
        func (function): La función a resolver.
        a (float): Extremo izquierdo del intervalo.
        b (float): Extremo derecho del intervalo.
        tol (float): Tolerancia para el criterio de parada.
        max_iter (int): Número máximo de iteraciones.

    Returns:
        (float, list): Aproximación de la raíz y lista de puntos intermedios [(a, b, c)].
    """
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")

    iter_count = 0
    iter_points = []  # Almacena los puntos (a, b, c) y las aproximaciones

    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  # Punto medio
        iter_points.append((a, b, c))  # Guarda los puntos para graficar

        print(f"Iteración {iter_count + 1}: a = {a:.5f}, b = {b:.5f}, c = {c:.5f}, f(c) = {func(c):.5f}")

        if func(c) == 0:  # Encontramos la raíz exacta
            return c, iter_points
        elif func(a) * func(c) < 0:  # La raíz está en [a, c]
            b = c
        else:  # La raíz está en [c, b]
            a = c
        iter_count += 1

    return (a + b) / 2, iter_points  # Aproximación de la raíz y puntos intermedios

# Función principal
def ecuacion_no_lineal():
    print("Calculadora de raíces de ecuaciones no lineales usando el Método de Bisección.")
    
    # Solicitar la ecuación al usuario
    eq = input("Ingresa la ecuación en términos de x (por ejemplo, x**3 - 4*x - 9): ")
    func = lambda x: eval(eq)

    # Solicitar el intervalo [a, b]
    a = float(input("Ingresa el extremo izquierdo del intervalo (a): "))
    b = float(input("Ingresa el extremo derecho del intervalo (b): "))

    # Solicitar la tolerancia y el número máximo de iteraciones
    tol = float(input("Ingresa la tolerancia deseada (por ejemplo, 1e-5): "))
    max_iter = int(input("Ingresa el número máximo de iteraciones permitido: "))

    # Verificar que la función cambia de signo
    if func(a) * func(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        return

    # Resolver con el método de bisección
    root, iter_points = bisection_method(func, a, b, tol=tol, max_iter=max_iter)
    print(f"\nLa raíz aproximada de la ecuación es: x = {root:.5f}")

    # Graficar la función y las iteraciones
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = [func(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label=f"f(x) = {eq}")
    plt.axhline(0, color='black', linewidth=0.5)  # Eje x

    # Graficar los puntos de las iteraciones
    for i, (a_iter, b_iter, c_iter) in enumerate(iter_points):
        plt.scatter(c_iter, func(c_iter), color='blue', alpha=0.7)
        plt.text(c_iter, func(c_iter), f"{i+1}: {c_iter:.4f}", fontsize=8, ha='right')

    # Agregar el eje x (línea horizontal en y = 0)
    plt.axhline(0, color="black", linewidth=2, linestyle="-")

    # Agregar el eje y (línea vertical en x = 0)
    plt.axvline(0, color="black", linewidth=2, linestyle="-")

    # Graficar la raíz aproximada
    plt.scatter(root, func(root), color='red', label=f"Raíz aproximada: x = {root:.5f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Bisección - Solución de Ecuaciones No Lineales")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ecuacion_no_lineal()

