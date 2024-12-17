import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Función para ingresar una ecuación
def ingresar_ecuacion():
    ecuacion_str = input("Introduce la ecuación (usa 'x' y 'y' como variables): ")
    lado_izquierdo, lado_derecho = ecuacion_str.split('=')
    ecuacion = sp.Eq(sp.sympify(lado_izquierdo), sp.sympify(lado_derecho))
    return ecuacion

# Función para resolver el sistema de ecuaciones
def resolver_ecuaciones(ecuaciones, variables):
    soluciones = sp.linsolve(ecuaciones, *variables)
    return soluciones

# Función para graficar el sistema de ecuaciones (solo para 2 variables)
def graficar_ecuaciones(ecuaciones, variables):
    x_vals = np.linspace(-5, 5, 200)
    y_vals = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    # Graficamos las ecuaciones
    for ecuacion in ecuaciones:
        # Evaluar la ecuación y obtener los valores en la malla
        Z = np.zeros(X.shape)
        
        for i, (x, y) in enumerate(zip(X.flatten(), Y.flatten())):
            # Evaluamos la diferencia entre ambos lados de la ecuación (lado izquierdo - lado derecho)
            lhs = ecuacion.lhs.subs(variables[0], x).subs(variables[1], y)
            rhs = ecuacion.rhs.subs(variables[0], x).subs(variables[1], y)
            Z.flat[i] = float(lhs - rhs)  # Calculamos la diferencia
            
        Z = Z.reshape(X.shape)
        # Graficamos el contorno donde la diferencia es cero (es decir, la intersección)
        plt.contour(X, Y, Z, levels=[0], colors='blue')
    
    # Dibujar el eje x (horizontal) en y=0
    plt.axhline(0, color="black", linewidth=1, linestyle="-")  # Eje x
    
    # Dibujar el eje y (vertical) en x=0
    plt.axvline(0, color="black", linewidth=1, linestyle="-")  # Eje y

    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica del Sistema de Ecuaciones')
    plt.grid(True)
    plt.show()

# Función principal
def Ecuaciones_lineales():
    # Definir las variables
    x, y = sp.symbols('x y')

    # Ingresar las ecuaciones
    ecuaciones = []
    num_ecuaciones = int(input("¿Cuántas ecuaciones tiene el sistema? (Solo ecuaciones 2*2 para que la gráfica sea visible): "))
    for i in range(num_ecuaciones):
        ecuacion = ingresar_ecuacion()
        ecuaciones.append(ecuacion)

    # Resolver el sistema de ecuaciones
    soluciones = resolver_ecuaciones(ecuaciones, [x, y])
    print(f"Solución del sistema de ecuaciones: {soluciones}")

    # Graficar las ecuaciones si es un sistema de 2 variables
    if num_ecuaciones == 2:
        graficar_ecuaciones(ecuaciones, [x, y])

if __name__ == "__main__":
    Ecuaciones_lineales()
