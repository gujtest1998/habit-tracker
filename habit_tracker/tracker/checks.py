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
    
def comprobar_categoria(categoria):
    ruta = BASE_DIR / "datos" / "categorias.csv"

    if not ruta.exists():
        return 0
    
    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return any(fila["categoria"] == categoria for fila in lector)