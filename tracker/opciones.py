import csv
from config import BASE_DIR

from .colores import ROJO, VERDE, CIAN, RESET, print_color
from .checks import comprobar_registro, comprobar_horas_temp, normalizar, validar_horas
from .guardar import registrar, registrar_categoria, habito
from .cargar import mostrar_registros, mostrar_temporizadores, contar_temporizador, contar_habitos, mostrar_categorias,dev_temporizador_id,dev_lista_habitos_cat, dev_categoria_id, dev_habito_id, dev_lista_temporizadores_cat
from .inputs import pedir_nombre_temp, pedir_horas_temp, pedir_fecha_temp, pedir_nombre_registro
from .borrar import borrar_habito, borrar_temporizadores, borrar_csv, borrar_temporizador, borrar_categoria

from datetime import datetime
# se guarda en una variable para luego simplemente mostrarlo en pantalla

volver = f"\nConsejo: Escribe 'volver' si quieres salir al menú de opciones."
print_color(volver, CIAN)

def opcion_registro():
    # extrae un listado de los hábitos registrados en el csv
    lista = mostrar_registros()

    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        
        # recorre el listado, numerandolo con el nombre al lado
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
        print_color(volver, CIAN)

    while True: #empieza el bucle para seguir creando habitos
        print_color("\nOpción seleccionada: Registrar un nuevo hábito",CIAN)
        nombre = pedir_nombre_registro()
        
        # da la opción de introducir volver y salir en todas sus variables
        if normalizar(nombre) == "volver" or normalizar(nombre) == "salir":
            return False
        
        # si no está registrado, prosigue con el resto de inputs
        categoria = input("Categoria: ")

        while True:
            objetivo = input("Objetivo (horas): ")
            
            # comprueba que las horas sean mayores que 0 y no contengan letras u otros caracteres
            if validar_horas(objetivo):
                registrar_categoria(categoria)
                id_categoria = dev_categoria_id(categoria)
                registrar(nombre, id_categoria, objetivo)
                print_color("\nAñadido "+nombre+", categoria: "+categoria+", objetivo: "+objetivo+".",VERDE)
                break

def opcion_temporizador():

    lista = mostrar_registros() # devuelve el listado de habitos registrados
    lista_minus = [item.lower() for item in lista]

    if lista:
        print("\nEstos son los hábitos ya registrados: \n")

        # recorre el listado, numerandolo con el nombre al lado
        for i, item in enumerate(sorted(lista), start=1):
            print(f"{i} - {item}")
        print_color(volver, CIAN)
        
    while True: #empieza el bucle para seguir creando temporizadores
        print_color("\nOpción seleccionada: Crear un temporizador",CIAN)
        nombre = pedir_nombre_temp(lista_minus,lista)
        if normalizar(nombre) == "volver" or normalizar(nombre) == "salir":
            return False
        fecha = pedir_fecha_temp()  
        while True:
            horas = pedir_horas_temp()
            id_habito = dev_habito_id(nombre)
            temporizadores = mostrar_temporizadores()
            print(temporizadores)
            contador_horas = comprobar_horas_temp(temporizadores,horas,fecha)
            if contador_horas > 24:
                print_color("\nEl total de horas registradas para esta actividad no puede ser mayor de 24",ROJO)
                continue #si la actividad supera las 24 horas el mismo día, vuelve a pedir las horas
            else:     
                habito(id_habito,nombre,horas,fecha)
                print_color(f"\nSe han añadido {horas} horas al temporizador {nombre} con fecha {fecha}",VERDE)
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
            habitos = contar_habitos(borrar)
            if habitos == False:
                print_color("Este hábito no existe.",ROJO)
            else:
                seguro = input(f"\n{ROJO}¿Estás seguro de que quieres borrar el hábito {borrar}?\nSe eliminarán {temporizadores} registros de horas asociados. s/n: {RESET}")
                seguro = seguro.lower()
            
                if seguro == "s" or seguro == "si":
                    habito = borrar_habito(borrar,dev_habito_id(borrar))
                    registros = borrar_temporizadores(dev_temporizador_id(borrar),temporizadores)
                elif seguro == "n" or seguro == "no":
                    return
    else:
        print_color("\nNo hay ningún hábito a borrar.",CIAN)
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
                print_color(f"Opcion no valida",ROJO)
            #valor = lista[borrar]
            #temporizadores = contar_temporizador(borrar)
            seguro = input(f"\n{ROJO}¿Estás seguro de que quieres borrar el hábito {borrar["nombre"]} con {borrar["horas"]} horas registradas del día {borrar["fecha"]}? s/n: {RESET}")

            seguro = seguro.lower()

            if seguro == "s" or seguro == "si":
                habito = borrar_temporizador(borrar["id"],borrar)
                print(habito)
            elif seguro == "n" or seguro == "no":
                return
    else:
        print_color("No hay ningún temporizador a eliminar.",CIAN)

def opcion_borrar_categoria():
    # muestra previamente todos los registros a eliminar
    lista = mostrar_categorias()
    if lista:
        print("\nEstos son las categorias ya registradas: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
        print(volver)
        while True:
            
            borrar = input("\nIntroduce el nombre del elemento a borrar: ")
            id_categoria = dev_categoria_id(borrar)
            
            lista_habitos = dev_lista_habitos_cat(id_categoria)
            lista_temporizadores = dev_lista_temporizadores_cat(lista_habitos,id_categoria)

            if normalizar(borrar) == "volver" or normalizar(borrar) == "salir":
                return False
            
            #temporizadores = contar_temporizador(borrar)
            seguro = input(f"\n{ROJO}La categoria {borrar} tiene {len(lista_habitos)} hábitos asociados, con {len(lista_temporizadores)} registros de tiempo. ¿Estás seguro de que quieres borrar esta categoría? s/n: {RESET}")
            seguro = seguro.lower()
            
            if seguro == "s" or seguro == "si":
                habito = borrar_categoria(borrar,id_categoria,lista_habitos,lista_temporizadores)
                #registros = borrar_temporizadores(borrar)
            elif seguro == "n" or seguro == "no":
                return
    else:
        print_color("\nNo hay ninguna categoria a borrar.",CIAN)

def opcion_borrar_todo():
    lista1 = mostrar_temporizadores()
    lista2 = mostrar_registros()
    lista3 = mostrar_categorias()

    if lista1 or lista2 or lista3:
        seguro = input(f"\n{ROJO}¿Estás seguro de que quieres borrar todos los registros? s/n:{RESET} ")

        seguro = seguro.lower()

        if seguro == "s" or seguro == "si":

            borrar_csv("categorias.csv")
            borrar_csv("habitos.csv")
            borrar_csv("temporizadores.csv")
            print(f"{VERDE}Todos los registros han sido eliminados.{RESET}")
        elif seguro == "n" or seguro == "no":
            return
    else:
        print_color("No hay elementos a borrar.",CIAN)

