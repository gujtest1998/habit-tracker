import csv
from config import BASE_DIR
from .checks import normalizar
from .colores import ROJO, VERDE, CIAN, RESET

def borrar_habito(borrar):
    borrar = normalizar(borrar)
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        return 0
    filas_restantes = []
    filas_originales = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas_originales.append(fila)
            if normalizar(fila[1]) != borrar:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)

    if len(filas_originales) == len(filas_restantes):
        return (f"El registro '{borrar}' no existe.")
    else:
        return (f"Registro '{borrar}' eliminado.")
    
def borrar_temporizador(borrar,seleccion):
    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return 0
    filas_restantes = []
    filas_originales = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas_originales.append(fila)
            if normalizar(fila[0]) != borrar:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)

    if len(filas_originales) == len(filas_restantes):
        return (f"{ROJO}El registro '{seleccion}' no existe.{RESET}")
    else:
        return (f"{VERDE}Registro '{seleccion}' eliminado.{RESET}")
    
def borrar_temporizadores(temporizador):
    temporizador = normalizar(temporizador)
    ruta = BASE_DIR / "datos" / "temporizadores.csv"

    if not ruta.exists():
        return 0
    filas_restantes = []
    filas_originales = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas_originales.append(fila)
            if normalizar(fila[1]) != temporizador:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)

    if len(filas_originales) == len(filas_restantes):
        return (f"{ROJO}El temporizador '{temporizador}' no existe.{RESET}")
    else:
        return (f"{VERDE}Todos los temporizadores asociados a '{temporizador}' han sido eliminados.{VERDE}")

def borrar_csv(fichero):
    ruta = BASE_DIR / "datos" / f"{fichero}"

    with open(ruta, "w", encoding="utf-8"):
        pass