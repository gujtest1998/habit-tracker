import csv
from config import BASE_DIR
from .checks import normalizar


def mostrar_registros(temporizador = None):
    
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        return 0
    contador = 0
    lista = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            contador +=1
            lista.append(fila[1])
    return lista
    
def mostrar_temporizadores():
    
    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return 0
    contador = 0
    temporizadores = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            #print(fila)
            contador +=1
            temporizadores.append({
                "id": fila[0],
                "nombre": fila[1],
                "horas": fila[2],
                "fecha": fila[3]
                })
    return temporizadores
def mostrar_categorias(temporizador = None):
    
    ruta = BASE_DIR / "datos" / "categorias.csv"

    if not ruta.exists():
        return 0
    contador = 0
    lista = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            contador +=1
            lista.append(fila[1])
    return lista

def contar_temporizador(nombre):

    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        contador = 0
        for fila in lector:
            if normalizar(fila[1]) == normalizar(nombre):
               contador = contador + 1
            else:
               return False
    return contador

def contar_id(fichero):
   
    ruta = BASE_DIR / "datos" / f"{fichero}"

    if not ruta.exists():
        return 0
    
    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        ids = [int(fila["id"]) for fila in lector]
    return max(ids, default=0) + 1

def categoria_id(categoria):
    ruta = BASE_DIR / "datos" / "categorias.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            if fila[1].lower() == categoria.lower():
                return fila[0]

  