from datetime import datetime
from .checks import normalizar, validar_horas, comprobar_registro
from .colores import ROJO, VERDE, CIAN, RESET,print_color
def pedir_nombre_registro():
     while True:
        nombre = input("Nombre a registrar: ")
     # devuelve el número de veces que el nombre está registrado
        comprobado = comprobar_registro(nombre)

        # si está registrado, vuelve a pedir el nombre
        if comprobado > 0:
            print_color("Esté hábito ya está registrado. Por favor, introduce uno nuevo.", ROJO)
            continue
        else: 
            return nombre        
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
            print_color(f"\nPor favor, introduce un temporizador de la lista.",ROJO)

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
                        print_color(f"\nLa fecha no puede ser superior a la fecha actual.",ROJO)
                        continue
                except ValueError:
                    print_color(f"\nFormato incorrecto. Debe ser AAAA-MM-DD",ROJO)
                    continue
            return fecha
        