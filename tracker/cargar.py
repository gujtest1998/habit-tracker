import csv
from config import BASE_DIR
from .checks import normalizar


def mostrar_registros(temporizador = None):
    
    ruta = BASE_DIR / "datos" / "habitos.csv"

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
                "id_habito": fila[1],
                "nombre": fila[2],
                "horas": fila[3],
                "fecha": fila[4]
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
            if normalizar(fila[2]) == normalizar(nombre):
                contador = contador + 1
    return contador
def contar_habitos(nombre):
    ruta = BASE_DIR / "datos" / "habitos.csv"
    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        contador = 0
        for fila in lector:
            if normalizar(fila[1]) == normalizar(nombre):
                contador = contador + 1
    return contador
def contar_temporizador_cat(id_habito):

    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        contador = 0
        for fila in lector:
            if fila[1] == id_habito:
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

def dev_habito_id(habito):
    ruta = BASE_DIR / "datos" / "habitos.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            if fila[1].lower() == habito.lower():
                return fila[0]
def dev_temporizador_id(temporizador):
    ruta = BASE_DIR / "datos" / "habitos.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            if fila[0].lower() == temporizador.lower():
                return fila[0]
def dev_lista_habitos_cat(id_categoria):
    ruta = BASE_DIR / "datos" / "habitos.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        lista = []
        for fila in lector:
            if fila[2] == id_categoria:
                lista.append(fila) 
        return lista  
def dev_lista_temporizadores_cat(lista_habitos,id_categoria):
    ruta = BASE_DIR / "datos" / "temporizadores.csv"
    
    lista_habitos_id = [habito[0] for habito in lista_habitos]

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        lista = []
        for fila in lector:
            if fila[1] in lista_habitos_id:
                lista.append(fila) 
        return lista  
            
def dev_categoria_id(categoria):
    ruta = BASE_DIR / "datos" / "categorias.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            if fila[1].lower() == categoria.lower():
                return fila[0]

