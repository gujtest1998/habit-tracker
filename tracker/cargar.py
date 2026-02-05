import csv
from config import BASE_DIR


def mostrar_registros(temporizador = None):
    
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        return []
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
        return []
    contador = 0
    temporizadores = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
       
        for fila in lector:
            print(fila)
            contador +=1
            temporizadores.append({
                "nombre": fila[1],
                "horas": fila[2],
                "fecha": fila[3]
                })
    return temporizadores
    
def contar_temporizador(nombre):
   
    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return []
    

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        contador = 0
        for fila in lector:
           if fila[1] == nombre:
               contador = contador + 1
    return contador

def contar_id(fichero):
   
    ruta = BASE_DIR / "datos" / f"{fichero}"
    print(ruta)

    if not ruta.exists():
        return 0
    
    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)
        contador = 0
        for _ in lector:
            contador = contador + 1
    return contador