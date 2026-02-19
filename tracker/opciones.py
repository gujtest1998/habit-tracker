import csv
from config import BASE_DIR

from .colores import ROJO, VERDE, CIAN, INVERSION, RESET, print_color
from .checks import comprobar_categoria, comprobar_horas_temp, normalizar, validar_horas, validar_borrar_temporizador
from .guardar import registrar, registrar_categoria, habito
from .cargar import mostrar_registros, mostrar_temporizadores, contar_temporizador, contar_habitos, mostrar_categorias,dev_temporizador_id,dev_lista_habitos_cat, dev_categoria_id, dev_habito_id, dev_lista_temporizadores_cat
from .inputs import pedir_nombre_temp, pedir_horas_temp, pedir_fecha_temp, pedir_nombre_registro, pedir_categoria_borrar, pedir_temporizador_borrar, pedir_habito_borrar
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
        print_color("\nRegistrar un nuevo hábito\n",INVERSION)
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
                print_color("\nSe ha añadido el hábito "+nombre+" en la categoría "+categoria+" con un objetivo de "+objetivo+" horas.",VERDE)
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
        print_color("\nCrear un temporizador\n",INVERSION)
        nombre = pedir_nombre_temp(lista_minus,lista)
        if normalizar(nombre) == "volver" or normalizar(nombre) == "salir":
            return False
        fecha = pedir_fecha_temp()  
        while True:
            horas = pedir_horas_temp()
            id_habito = dev_habito_id(nombre)
            temporizadores = mostrar_temporizadores()
            contador_horas = comprobar_horas_temp(temporizadores,horas,fecha)

            if contador_horas > 24:
                print_color("El total de horas registradas para esta actividad no puede ser mayor de 24",ROJO)
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
        print_color(volver, CIAN)
        while True:
            print_color("\nEliminar un hábito\n",INVERSION)
            borrar = pedir_habito_borrar()
            if borrar:
                return False    
    else:
        print_color("\nNo existe ningún hábito a eliminar.",CIAN)
def opcion_borrar_tempo():
    # muestra previamente todos los registros a eliminar
    lista = mostrar_temporizadores()

    if lista:
        print("\nEstos son los temporizadores ya registrados: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item["nombre"]}: Horas '{item["horas"]}' Fecha '{item["fecha"]}'")
        print_color(volver,CIAN)
        while True:
            print_color("\nEliminar un temporizador\n",INVERSION)
            borrar = pedir_temporizador_borrar(lista)
            if borrar == None:
                return False
            else:
                seguro = input(f"\n{ROJO}¿Estás seguro de que quieres borrar el hábito {borrar["nombre"]} con {borrar["horas"]} horas registradas del día {borrar["fecha"]}? s/n: {RESET}")
                seguro = seguro.lower()

                if seguro == "s" or seguro == "si":
                    habito = borrar_temporizador(borrar["id"],borrar)
                    return
                elif seguro == "n" or seguro == "no":
                    return
    else:
        print_color("\nNo existe ningún temporizador a eliminar.",CIAN)

def opcion_borrar_categoria():
    # muestra previamente todos los registros a eliminar
    lista = mostrar_categorias()

    if lista:
        print("\nEstos son las categorias ya registradas: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
        print_color(volver,CIAN)
        while True:
            print_color("\nEliminar una categoría\n",INVERSION)
            borrar = pedir_categoria_borrar()
            if borrar == None:
                return False
    else:
        print_color("\nNo existe ninguna categoria a eliminar.",CIAN)

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
        print_color("No existen elementos a eliminar.",CIAN)

