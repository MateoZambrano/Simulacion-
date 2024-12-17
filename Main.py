from Taylor import Taylor_series
from Newton import MetodoNewton
from DiferenciasFinitas import diferencias_finitas
from SistemaENoLineales import *
from EcuacionesLineales import *
import os

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    """
    Menú principal para seleccionar entre el Teorema de Taylor y el Método de Newton.
    """
    while True:
        print("\nSelecciona una opción:")
        print("1. Serie de Taylor")
        print("2. Método de Newton")
        print("3. Diferencias Finitas")
        print("4. Sistemas de ecuaciones no lineales")
        print("5. Ecuaciones Lineales")
        print("6. Salir")
        
        choice = input("Ingrese el número de la opción que desea: ")
        
        if choice == "1":
            limpiar_consola()
            Taylor_series()     
        elif choice == "2":
            limpiar_consola()
            #print("Codigo aun no exist")
            MetodoNewton()
        elif choice == "3":
            limpiar_consola()
            #print("Codigo aun no exist")
            diferencias_finitas()
        elif choice == "4":
            limpiar_consola()
            Sistema_No_lineales()
        elif choice == "5":
            limpiar_consola()
            Ecuaciones_lineales()
        elif choice == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

# Llamar al menú principal
main()