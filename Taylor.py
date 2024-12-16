import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

def Taylor_series():
    """
    Calcula la aproximación de Taylor de una funcion y genera su grafica comparativa.
    """
    # Definimos la variable simbolica
    x = sp.symbols('x')

    # Solicitar entrada del usuario para la función y el punto a alrededor del cual se expande la serie
    func_input = (input("Ingresa la función f(x) (por ejemplo, sin(x), exp(x), log(x)): "))
    a = float(input("Ingrese el punto a alrededor del cual se expande la serie: "))
    n = int(input("Ingresa el grado del polinomio de Taylor (un entero positivo): "))

    # convertir la entrada de la función a una expreción simbólica
    func = sp.sympify(func_input)

    # Contruir el polinomio de Taylor 
    taylor_polynomial = 0
    for i in range(n+1):
        term = (func.diff(x, i).subs(x, a) / sp.factorial(i))*(x-a)**i
        taylor_polynomial += term

    # Convertir la función y el polinomio a una función númerica para la grafica 
    f_lambdified = sp.lambdify(x, func, modules=["numpy"])
    taylor_lambdified = sp.lambdify(x, taylor_polynomial, modules=["numpy"])

    # Definir un rango de valores para x
    x_vals = np.linspace(a - 2, a + 2, 500)
    y_vals = f_lambdified(x_vals)
    taylor_vals = taylor_lambdified(x_vals)

    # Graficar las funciones
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"Función original: {func_input}", color="blue")
    plt.plot(x_vals, taylor_vals, label=f"Taylor (grado {n})", linestyle="--", color="red")
    plt.scatter([a], [f_lambdified(a)], color="black", label=f"Punto a = {a}")
    
     # Agregar la recta numérica en y = 0
    plt.axhline(0, color="black", linewidth=1, linestyle="--", label="Recta numérica")

    # Agregar el eje x (línea horizontal en y = 0)
    plt.axhline(0, color="black", linewidth=2, linestyle="-")

    # Agregar el eje y (línea vertical en x = 0)
    plt.axvline(0, color="black", linewidth=2, linestyle="-")

    # Agregar punto a en la recta numérica
    plt.scatter(a, 0, color="green", zorder=5, label=f"Posición de a en la recta numérica")
    
    # Etiquetas y título 
    plt.title("Serie de Taylor vs Función Original")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(a, color="green", linewidth=0.5, linestyle="--", label=f"Expansión en a = {a}")
    plt.legend()
    plt.grid(True)
    plt.show()

    #Mostrar el polinomio de Taylor
    print(f"\nPolinomio de Taylor de grado {n} alrededor de a = {a}:")
    print(taylor_polynomial)

# llamar a la función
#Taylor_series()

if __name__ == "__main__":
    Taylor_series()