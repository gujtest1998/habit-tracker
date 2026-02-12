from datetime import datetime
from .checks import normalizar, validar_horas
from .colores import ROJO, VERDE, CIAN, RESET

def pedir_nombre_temp(lista_minus,lista):
    while True:
        nombre = input("\nNombre a temporizar: ")
        nombre = normalizar(nombre)

        for i, item in enumerate(lista_minus):
            if item == nombre:
                return lista[i]
        if nombre == "volver":
            return nombre
        else:
            print(f"\n{ROJO}Por favor, introduce un temporizador de la lista.{RESET}")

def pedir_horas_temp():
    while True:
        horas = input("Duración de la actividad (horas): ")
        if validar_horas(horas):
            return horas

def pedir_fecha_temp():
    while True:
            fecha = input("Introduce la fecha (AAAA-MM-DD) o déjalo vacío para hoy: ")
            
            if fecha == "":
                fecha = datetime.now().date()
            else:
                try:
                    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
                    fecha_hoy = datetime.now().date()

                    if fecha > fecha_hoy:
                        print(f"\n{ROJO}La fecha no puede ser superior a la fecha actual.{RESET}")
                        continue
                except ValueError:
                    print(f"\n{ROJO}Formato incorrecto. Debe ser AAAA-MM-DD{RESET}")
                    continue
            return fecha
        