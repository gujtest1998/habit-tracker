import csv
from config import BASE_DIR

def borrar_habito(borrar):
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        print("No existe el archivo")
        return
    filas_restantes = []
    filas_originales = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas_originales.append(fila)
            if fila[1] != borrar:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)

    if len(filas_originales) == len(filas_restantes):
        return (f"El registro '{borrar}' no existe.")
    else:
        return (f"Registro '{borrar}' eliminado.")
    
def borrar_temporizadores(temporizador):
    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        print("No existe el archivo")
        return
    filas_restantes = []
    filas_originales = []
    

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas_originales.append(fila)
            if fila[1] != temporizador:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)

    if len(filas_originales) == len(filas_restantes):
        return (f"El temporizador '{temporizador}' no existe.")
    else:
        return (f"Todos los temporizadores asociados a '{temporizador}' han sido eliminados.")

def borrar_csv(fichero):
    ruta = BASE_DIR / "datos" / f"{fichero}"

    with open(ruta, "w", encoding="utf-8"):
        pass