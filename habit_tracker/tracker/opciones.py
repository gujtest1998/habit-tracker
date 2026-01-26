import csv
from config import BASE_DIR

from .checks import comprobar_registro
from .guardar import registrar

def opcion_registro():
    while True:
        nombre = input("Nombre a registrar: ")
        comprobado = comprobar_registro(nombre)

        if comprobado > 0:
            print("\nEsté hábito ya está registrado. Por favor, introduce uno nuevo.")
                
        else:
            categoria = input("Categoria: ")
            registrar(nombre, categoria)
            print("\nTemporizador "+nombre+" bajo la categoria "+categoria+" registrado con éxito.\n")

def opcion_borrar(borrar):
    ruta = BASE_DIR / "datos" / "registro.csv"

    if not ruta.exists():
        print("No existe el archivo")
        return
    filas_restantes = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != borrar:
                filas_restantes.append(fila)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas_restantes)
    print(f"Registro '{borrar}' eliminado.")

def opcion_borrar_todo():
    ruta = BASE_DIR / "datos" / "registro.csv"

    with open(ruta, "w", encoding="utf-8"):
        pass

    print("Todos los registros han sido eliminados.")