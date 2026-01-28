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
        print("3. Borrar un hábito")
        print("4. Borrar todos los hábitos")
        print("5. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
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
        opcion_borrar()
        return True
    elif opcion == "4":
        opcion_borrar_todo()
        return True
    elif opcion == "5":
        return False
    elif opcion == "6":
        print("Prueba")
        mostrar_registros()

    else:
        print("\nOpción no válida. Introduce una de las opciones.\n")
        return True
