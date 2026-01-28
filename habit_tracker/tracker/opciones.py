import csv
from config import BASE_DIR

from .checks import comprobar_registro
from .guardar import registrar, registrar_categoria, habito
from .cargar import mostrar_registros

from datetime import datetime


def opcion_registro():
    
    lista = mostrar_registros()
    while True:
        
        nombre = input("\nNombre a registrar: ")
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
            print("\nAñadido "+nombre+", categoria: "+categoria+", objetivo: "+objetivo+".\n")

def opcion_temporizador():

    lista = mostrar_registros()

    while True: 
        try:
            nombre = input("\nNombre a temporizar: ")
            if nombre not in lista:
                print("Por favor, introduce un temporizador ya registrado.")
                continue

            horas = float(input("Horas: "))
    
            fecha = input("Introduce la fecha (AAAA-MM-DD) o déjalo vacío para hoy: ")
            if fecha == "":
                fecha = datetime.now().date()
            else:
                while True:
                    try:
                        fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Formato incorrecto. Debe ser AAAA-MM-DD")

            habito(nombre, horas,fecha)
            print("\nAnotado el tiempo para el temporizador "+nombre+"\n")
        except ValueError:
            print("\nHay que introducir un número decimal.")

def opcion_borrar():
    # muestra previamente todos los registros a eliminar
    mostrar_registros()
    while True:
        borrar = input("\nIntroduce el nombre del elemento a borrar: ")
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

def opcion_borrar_todo():
    ruta = BASE_DIR / "datos" / "registro.csv"

    with open(ruta, "w", encoding="utf-8"):
        pass

    print("Todos los registros han sido eliminados.")