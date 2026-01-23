import csv
from config import BASE_DIR

def comprobar_registro(habito):
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        return 0

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contador = 0
        for fila in lector:
            if fila[0] == habito:
                contador += 1
        return int(contador)
def leer_csv():
    
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        return []
    
    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila[0])
