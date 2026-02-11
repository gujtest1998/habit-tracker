import csv
from config import BASE_DIR

from .checks import comprobar_registro, comprobar_horas_temp, normalizar, validar_horas
from .guardar import registrar, registrar_categoria, habito
from .cargar import mostrar_registros, mostrar_temporizadores, contar_temporizador, mostrar_categorias
from .inputs import pedir_nombre_temp, pedir_horas_temp, pedir_fecha_temp
from .borrar import borrar_habito, borrar_temporizadores, borrar_csv, borrar_temporizador

from datetime import datetime
# se guarda en una variable para luego simplemente mostrarlo en pantalla
volver = "\nConsejo: Escribe 'volver' si quieres salir al menú de opciones."

def opcion_registro():
    # extrae un listado de los hábitos registrados en el csv
    lista = mostrar_registros()

    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        
        # recorre el listado, numerandolo con el nombre al lado
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
        print(volver)

    while True:
        nombre = input("\nHábito a registrar: ")
        
        # da la opción de introducir volver y salir en todas sus variables
        if normalizar(nombre) == "volver" or normalizar(nombre) == "salir":
            return False
        
        # devuelve el número de veces que el nombre está registrado
        comprobado = comprobar_registro(nombre)

        # si está registrado, vuelve a pedir el nombre
        if comprobado > 0:
            print("\nEsté hábito ya está registrado. Por favor, introduce uno nuevo.")
            continue        
        # si no está registrado, prosigue con el resto de inputs
        categoria = input("Categoria: ")

        while True:
            objetivo = input("Objetivo (horas): ")
            
            # comprueba que las horas sean mayores que 0 y no contengan letras u otros caracteres
            if validar_horas(objetivo):
                registrar(nombre, categoria, objetivo)
                registrar_categoria(categoria)
                print("\nAñadido "+nombre+", categoria: "+categoria+", objetivo: "+objetivo+".")
                break

def opcion_temporizador():

    lista = mostrar_registros() # devuelve el listado de habitos registrados
    lista_minus = [item.lower() for item in lista]

    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
    while True: #empieza el bucle para seguir creando temporizadores
        nombre = pedir_nombre_temp(lista_minus,lista)
        if normalizar(nombre) == "volver" or normalizar(nombre) == "salir":
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
            #borrar = normalizar(borrar)
            if normalizar(borrar) == "volver" or normalizar(borrar) == "salir":
                return False
            temporizadores = contar_temporizador(borrar)
            seguro = input(f"\n¿Estás seguro de que quieres borrar el hábito {borrar}?\nSe eliminarán {temporizadores} registros de horas asociados. s/n: ")

            seguro = seguro.lower()
            
            if seguro == "s" or seguro == "si":
                habito = borrar_habito(borrar)
                registros = borrar_temporizadores(borrar)
            elif seguro == "n" or seguro == "no":
                print("\nSabia decisión.")
    else:
        print("\nNo hay ningún registro para borrar.")
def opcion_borrar_tempo():
    # muestra previamente todos los registros a eliminar
    lista = mostrar_temporizadores()

    if lista:
        print("\nEstos son los temporizadores ya registrados: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item["nombre"]}: Horas '{item["horas"]}' Fecha '{item["fecha"]}'")
        print(volver)
        while True:
            borrar = input("\nIntroduce el número del elemento a borrar: ")
            if normalizar(borrar) == "volver" or normalizar(borrar) == "salir":
                return False
            borrar = int(borrar)
            if borrar >= 1 and borrar <= len(lista):
                borrar = lista[borrar - 1]
            else:
                print("Opcion no valida")
            #valor = lista[borrar]
            #temporizadores = contar_temporizador(borrar)
            seguro = input(f"\n¿Estás seguro de que quieres borrar el hábito {borrar["nombre"]} con {borrar["horas"]} registradas del día {borrar["fecha"]}? s/n: ")

            seguro = seguro.lower()

            if seguro == "s" or seguro == "si":
                habito = borrar_temporizador(borrar["id"],borrar)
                print(habito)
            elif seguro == "n" or seguro == "no":
                print("\nSabia decisión.")
    else:
        print("No hay hábitos para eliminar.")
def opcion_borrar_todo():
    lista1 = mostrar_temporizadores()
    lista2 = mostrar_registros()
    lista3 = mostrar_categorias()

    if lista1 or lista2 or lista3:
        seguro = input("\n¿Estás seguro de que quieres borrar todos los registros? s/n: ")

        seguro = seguro.lower()

        if seguro == "s" or seguro == "si":

            borrar_csv("categorias.csv")
            borrar_csv("registro.csv")
            borrar_csv("temporizadores.csv")
            print("Todos los registros han sido eliminados.")
        elif seguro == "n" or seguro == "no":
            print("\nSabia decisión.")
    else:
        print("No hay elementos a borrar.")

