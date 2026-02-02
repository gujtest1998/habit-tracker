from .cargar import mostrar_registros
from .opciones import opcion_registro, opcion_temporizador, opcion_borrar, opcion_borrar_todo
from .guardar import habito

import tkinter as tk
def mostrar_menu():
    # se repite en bucle hasta que se pulse Salir
    while True:
        print("\n========= MENÚ DE OPCIONES =========")
        print("1. Registrar un nuevo hábito")
        print("2. Crear un temporizador")
        print("3. Eliminar elementos")
        print("4. Modificar elementos")
        print("5. Salir.")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
            break
def mostrar_menu_borrar():
    print("\nConsejo: Escribe 'volver' para salir al menú de opciones.")
     # se repite en bucle hasta que se pulse Salir
    while True:
        print("\n========= MENÚ DE BORRADO =========")
        print("1. Eliminar un hábito")
        print("2. Eliminar un temporizador")
        print("3. Eliminar todos los elementos")
        print("4. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not borrar(opcion):
            break
def seleccionar(opcion):
    # cada opcion marcada redirige a su propia funcion
    if opcion == "1":
        #print("hola")
        opcion_registro()

        return True
    elif opcion == "2":
        opcion_temporizador()
        return True
    elif opcion == "3":
        mostrar_menu_borrar()
        return True
    elif opcion == "4":
        print("En desarrollo")
        return True
    elif opcion == "5":
        return False
    elif opcion == "6":
        print("Prueba")
        mostrar_registros()

    else:
        print("\nOpción no válida. Introduce una de las opciones.\n")
        return True

def borrar(opcion):
    # cada opcion marcada redirige a su propia funcion
    if opcion == "1":
        opcion_borrar()
        return True
    elif opcion == "2":
        print("Sección en desarrollo.")
        return True
    elif opcion == "3":
        opcion_borrar_todo()
        return True
    elif opcion == "4":
        return False
    elif opcion == "volver":
        mostrar_menu()
    else:
        print("\nOpción no válida. Introduce una de las opciones.\n")
        return True
