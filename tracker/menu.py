from .cargar import mostrar_registros, mostrar_categorias, mostrar_temporizadores
from .opciones import opcion_registro, opcion_temporizador, opcion_borrar, opcion_borrar_todo, opcion_borrar_tempo
from .guardar import habito
from .checks import normalizar
from .colores import ROJO, VERDE, CIAN, RESET

import tkinter as tk
def mostrar_menu():
    # se repite en bucle hasta que se pulse Salir
    while True:
        print("\n========= MENÚ DE OPCIONES =========")
        print("1. Registrar un nuevo hábito (100%)")
        print("2. Crear un temporizador")
        print("3. Eliminar elementos")
        print("4. Modificar elementos")
        print("5. Mostrar estadísticas")
        print("6. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
            break
def mostrar_menu_borrar():
    while True:
     # se repite en bucle hasta que se pulse Salir
        print("\n========= MENÚ DE BORRADO =========")
        print("1. Eliminar un hábito")
        print("2. Eliminar un temporizador")
        print("3. Eliminar todos los elementos")
        print("4. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not borrar(opcion):
            break
#opciones del menú principal  
def opcion_1():
    opcion_registro()
    return True

def opcion_2():
    opcion_temporizador()
    return True

def opcion_3():
    lista = mostrar_registros()
    if lista:
        mostrar_menu_borrar()
    else:
        print("\nActualmente no existe ningún elemento a eliminar.")
    return True

def opcion_4():
    print("En desarrollo")
    return True

def opcion_5():
    print("Prueba")
    mostrar_registros()
    return True

def opcion_6():
    print("Cerrando aplicación...")
    return False
# según la elección escogida en el menú, redirige a las funciones de arriba
menu = {
    "1": opcion_1,
    "2": opcion_2,
    "3": opcion_3,
    "4": opcion_4,
    "5": opcion_5,
    "6": opcion_6
}

def seleccionar(opcion):
    # normaliza tanto volver como salir, y cierra el menú actual
    if normalizar(opcion) in ("volver", "salir"):
        return False
    # si la opción escogida está en el diccionario menu, redirige a la opción escogida
    if opcion in menu:
        return menu[opcion]()
    else:
        print("\nOpción no válida.\n")
        return True
# las distintas opciones del menu borrar           
def borrar_1():
    opcion_borrar()
    return True
def borrar_2():
    opcion_borrar_tempo()
    return True
def borrar_3():
    opcion_borrar_todo()
    return True
def borrar_4():
    #sale del bucle
    return False
# diccionario que contiene la redirección de las funciones
menu_borrar = {
    "1": borrar_1,
    "2": borrar_2,
    "3": borrar_3,
    "4": borrar_4,
}
    
def borrar(opcion):
    # si el usuario escribe volver o salir también sale de la aplicación
    if normalizar(opcion) in("volver","salir"):
        return False
    # si la opcion coincide con una del diccionario menu_borrar, redirige a esa función
    if opcion in menu_borrar:
        return menu_borrar[opcion]()
    else:
        print(f"\n{ROJO}Opción no válida.{RESET}\n")
        return True