from tracker import habito, registrar, comprobar_registro, leer_csv
import tkinter as tk
def mostrar_menu():
    while True:
        print("\n========= MENÚ DE OPCIONES =========")
        print("1. Registrar un temporizador nuevo")
        print("2. Seleccionar un temporizador")
        print("3. Ver estadísticas")
        print("4. Salir")
        print("====================================")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
            break
        
def seleccionar(opcion):
    if opcion == "1":

        nombre = input("Nombre a registrar: ")
        comprobado = comprobar_registro(nombre)
        if comprobado > 0:
            print("\nEsté hábito ya está registrado. Por favor, introduce uno nuevo.")
        else:
            categoria = input("Categoria: ")
            registrar(nombre, categoria)
            print("\nTemporizador "+nombre+" bajo la categoria "+categoria+" registrado con éxito.")
        return True
    elif opcion == "2":
        nombre = input("Nombre a temporizar: ")
        horas = input("Horas: ")
        habito(nombre, horas)
        print("\nAnotado el tiempo para el temporizador "+nombre)
        return True
    elif opcion == "3":
        print("Estado")
        return True
    elif opcion == "4":
        return False
    elif opcion == "5":
        print("Prueba")
        leer_csv()

    else:
        print("\nOpción no válida. Introduce una de las opciones.\n")
        return True
