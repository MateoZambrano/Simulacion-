import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

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

     # Dibujar el eje x (horizontal) en y=0
    plt.axhline(0, color="black", linewidth=1, linestyle="-")  # Eje x
    
    # Dibujar el eje y (vertical) en x=0
    plt.axvline(0, color="black", linewidth=1, linestyle="-")  # Eje y
    
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

if __name__ == "__main__":
    MetodoNewton()