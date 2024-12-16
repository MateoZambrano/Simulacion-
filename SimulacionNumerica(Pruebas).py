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
    Taylor_series()

def MetodoNewton():
    """
    Resuelve una ecuación no lineal usando el método de Newton y genera una gráfica.
    """
    # Definir la variable simbólica
    x = sp.symbols('x')
    
    # Solicitar entrada al usuario
    func_input = input("Ingresa la ecuación f(x) = 0 (por ejemplo, x**2 - 2): ")
    x0 = float(input("Ingresa una aproximación inicial x0: "))
    tol = float(input("Ingresa la tolerancia para el método de Newton: "))
    max_iter = int(input("Ingresa el número máximo de iteraciones: "))
    
    # Convertir la entrada de la función a una expresión simbólica
    func = sp.sympify(func_input)
    func_prime = sp.diff(func, x)  # Derivada de la función
    
    # Convertir las funciones a numéricas para graficar
    f_lambdified = sp.lambdify(x, func, modules=["numpy"])
    f_prime_lambdified = sp.lambdify(x, func_prime, modules=["numpy"])
    
    # Método de Newton
    xi = x0
    iterations = []
    for i in range(max_iter):
        f_val = func.subs(x, xi)
        f_prime_val = func_prime.subs(x, xi)
        if abs(f_prime_val) < 1e-12:  # Evitar divisiones por cero
            print("La derivada se aproxima a cero. Método de Newton fallido.")
            return
        xi_new = xi - f_val / f_prime_val
        iterations.append((xi, f_val))
        print(f"Iteración {i+1}: x = {xi_new}, f(x) = {f_val}")
        if abs(xi_new - xi) < tol:
            print(f"\nRaíz encontrada: x = {xi_new}")
            break
        xi = xi_new
    
    # Graficar la función y las aproximaciones
    x_vals = np.linspace(x0 - 2, x0 + 2, 500)
    y_vals = f_lambdified(x_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {func_input}", color="blue")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    
    # Dibujar las tangentes
    for xi, f_val in iterations:
        tangent = f_prime_lambdified(xi) * (x_vals - xi) + f_lambdified(xi)
        plt.plot(x_vals, tangent, linestyle="--", label=f"Tangente en x = {xi}")
        plt.scatter([xi], [f_lambdified(xi)], color="red")  # Punto de la tangente
    
    plt.title("Método de Newton: Evolución hacia la raíz")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
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
    diferencias_finitas()

def main():
    """
    Menú principal para seleccionar entre el Teorema de Taylor y el Método de Newton.
    """
    while True:
        print("\nSelecciona una opción:")
        print("1. Serie de Taylor")
        print("2. Método de Newton")
        print("3. Diferencias Finitas")
        print("4. Salir")
        
        choice = input("Ingrese el número de la opción que desea: ")
        
        if choice == "1":
            Taylor_series()     
        elif choice == "2":
            MetodoNewton()
        elif choice == "3":
            diferencias_finitas()
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

# Llamar al menú principal
main()

