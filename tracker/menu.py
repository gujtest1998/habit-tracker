from .cargar import mostrar_registros
from .opciones import opcion_registro, opcion_temporizador, opcion_borrar, opcion_borrar_todo, opcion_borrar_tempo
from .guardar import habito
from .checks import normalizar

import tkinter as tk
def mostrar_menu():
    # se repite en bucle hasta que se pulse Salir
    while True:
        print("\n========= MENÚ DE OPCIONES =========")
        print("1. Registrar un nuevo hábito")
        print("2. Crear un temporizador")
        print("3. Eliminar elementos")
        print("4. Modificar elementos")
        print("5. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
            break
def mostrar_menu_borrar():
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
    # si el usuario escribe volver o salir también sale de la aplicación
    if normalizar(opcion) == "volver" or normalizar(opcion) == "salir":
        return False
    # cada opcion marcada redirige a su propia funcion del fichero opciones.py
    match opcion:
        case "1":
            opcion_registro()
            return True
        case "2":
            opcion_temporizador()
            return True
        case "3":
            mostrar_menu_borrar()
            return True
        case "4":
            print("En desarrollo")
            return True    
        case "5":
            print("Cerrando aplicación...")
            return False
        case "6":
            print("Prueba")
            mostrar_registros()
        case _:
            print("\nOpción no válida. Introduce una de las opciones.\n")
            return True

def borrar(opcion):
    # si el usuario escribe volver o salir también sale de la aplicación
    if normalizar(opcion) == "volver" or normalizar(opcion) == "salir":
        return False
    # cada opcion marcada redirige a su propia funcion del fichero opciones.py
    match opcion:
        case "1":
            opcion_borrar()
            return True
        case "2":
            opcion_borrar_tempo()
            return True
        case "3":
            opcion_borrar_todo()
            return True
        case "4":
            #sale del bucle
            return False
        case _:
            print("\nOpción no válida. Introduce una de las opciones.\n")
            return True