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
    if lista:
        print("\nEstos son los hábitos ya registrados: \n")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
    return lista
    
