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
            lista.append(fila[0])
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
            contador +=1
            temporizadores.append({
                "nombre": fila[0],
                "horas": fila[1],
                "fecha": fila[2]
                })
    return temporizadores
    
