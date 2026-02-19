from datetime import datetime
from .checks import normalizar, validar_horas, comprobar_registro, validar_borrar_temporizador
from .cargar import contar_habitos, contar_temporizador, dev_habito_id
from .borrar import borrar_temporizadores, borrar_habito
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
        nombre = input("Nombre a temporizar: ")
        nombre = normalizar(nombre)

        for i, item in enumerate(lista_minus):
            if item == nombre:
                return lista[i]
        if nombre == "volver":
            return nombre
        else:
            print_color(f"Por favor, introduce un temporizador de la lista.",ROJO)

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
                        print_color(f"La fecha no puede ser superior a la fecha actual.",ROJO)
                        continue
                except ValueError:
                    print_color(f"Formato incorrecto. Debe ser AAAA-MM-DD",ROJO)
                    continue
            return fecha
def pedir_habito_borrar():
    while True:
        borrar = input("Introduce el nombre del elemento a borrar: ")
        if normalizar(borrar) == "volver" or normalizar(borrar) == "salir":
            return borrar
        temporizadores = contar_temporizador(borrar)
        habitos = contar_habitos(borrar)
        if habitos == False:
            print_color("Este hábito no existe.",ROJO)
            continue
        else:
            seguro = input(f"\n{ROJO}¿Estás seguro de que quieres borrar el hábito {borrar}?\nSe eliminarán {temporizadores} registros de horas asociados. s/n: {RESET}")
            seguro = seguro.lower()
            
            if seguro == "s" or seguro == "si":
                registros = borrar_temporizadores(dev_habito_id(borrar),temporizadores)
                habito = borrar_habito(borrar,dev_habito_id(borrar))
                print_color(f"\nEl hábito {borrar} se ha eliminado con éxito.",VERDE)
                return
            elif seguro == "n" or seguro == "no":
                return
def pedir_temporizador_borrar(lista):
    while True:
        borrar = input("Introduce el número del elemento a borrar: ")
        if normalizar(borrar) == "volver" or normalizar(borrar) == "salir":
            return None
        else:
            validado = validar_borrar_temporizador(borrar,lista)

            if validado is None:
                continue
            else:
                return validado