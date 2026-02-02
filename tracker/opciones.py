import csv
from config import BASE_DIR

from .checks import comprobar_registro, comprobar_horas_temp
from .guardar import registrar, registrar_categoria, habito
from .cargar import mostrar_registros, mostrar_temporizadores
from .inputs import pedir_nombre_temp, pedir_horas_temp, pedir_fecha_temp

from datetime import datetime

volver = "\nConsejo: Escribe 'volver' si quieres salir al menú de opciones."

def opcion_registro():
    
    lista = mostrar_registros()
    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
        print(volver)
    while True:

        nombre = input("\nHábito a registrar: ")

        if nombre == "volver":
            return False

        comprobado = comprobar_registro(nombre)

        if comprobado > 0:
            print("\nEsté hábito ya está registrado. Por favor, introduce uno nuevo.")
                
        else:
            categoria = input("Categoria: ")
            objetivo = input("Objetivo (horas): ")
            if objetivo == "":
                objetivo = "0"
            registrar(nombre, categoria, objetivo)
            registrar_categoria(categoria)
            print("\nAñadido "+nombre+", categoria: "+categoria+", objetivo: "+objetivo+".")

def opcion_temporizador():

    lista = mostrar_registros() # devuelve el listado de habitos registrados
    lista_minus = [item.lower() for item in lista]
    print(lista_minus)

    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
        print(volver)
    while True: #empieza el bucle para seguir creando temporizadores
        nombre = pedir_nombre_temp(lista_minus,lista)
        if nombre == "volver":
            return False
        while True:
            horas = pedir_horas_temp()
            fecha = pedir_fecha_temp()              
            temporizadores = mostrar_temporizadores()
            contador_horas = comprobar_horas_temp(temporizadores, horas, fecha)
            if contador_horas > 24:
                print("Esta actividad no puede superar las 24 horas")    
                continue #si la actividad supera las 24 horas el mismo día, vuelve a pedir las horas
            else:
                habito(nombre,horas,fecha)
                print(f"\nSe han añadido {horas} horas al temporizador {nombre} con fecha {fecha}") 
                break # una vez es correcto, sale del bucle de horas y dias y vuelve al bucle original
        continue 
        

def opcion_borrar():
    # muestra previamente todos los registros a eliminar
    lista = mostrar_registros()
    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
        print(volver)
    while True:
        
        borrar = input("\nIntroduce el nombre del elemento a borrar: ")
        if borrar == "volver":
            return False
        seguro = input("\n¿Estás seguro de que quieres borrar este elemento? s/n: ")

        seguro = seguro.lower()

        if seguro == "s" or seguro == "si":
            ruta = BASE_DIR / "datos" / "registro.csv"

            if not ruta.exists():
                print("No existe el archivo")
                return
            filas_restantes = []
            filas_originales = []

            with open(ruta, newline="", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    filas_originales.append(fila)
                    if fila[0] != borrar:
                        filas_restantes.append(fila)
            with open(ruta, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(filas_restantes)
        
            if len(filas_originales) == len(filas_restantes):
                print(f"El registro '{borrar}' no existe.")
            else:
                print(f"Registro '{borrar}' eliminado.")
        elif seguro == "n" or seguro == "no":
            print("\nSabia decisión.")

def opcion_borrar_todo():

    seguro = input("\n¿Estás seguro de que quieres borrar todos los registros? s/n: ")

    seguro = seguro.lower()

    if seguro == "s" or seguro == "si":

        ruta = BASE_DIR / "datos" / "registro.csv"

        with open(ruta, "w", encoding="utf-8"):
            pass

        print("Todos los registros han sido eliminados.")
    elif seguro == "n" or seguro == "no":
        print("\nSabia decisión.")