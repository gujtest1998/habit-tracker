import csv
from config import BASE_DIR
from pathlib import Path
from .checks import comprobar_categoria

def habito(nombre, tiempo):
    ruta = BASE_DIR / "datos" / "temporizadores.csv"
    ruta.parent.mkdir(exist_ok=True)

    encabezado = not ruta.exists() or ruta.stat().st_size == 0

    with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
        campos = ["temporizador", "tiempo"]
        writer = csv.DictWriter(archivo, fieldnames=campos)

        if encabezado:
            writer.writeheader()
        writer.writerow({"temporizador": nombre, "tiempo": tiempo})

def registrar(registro, categoria):

    ruta = BASE_DIR / "datos" / "registro.csv"
    ruta.parent.mkdir(exist_ok=True)

    encabezado = not ruta.exists() or ruta.stat().st_size == 0

    with open(ruta, mode="a", newline="",encoding="utf-8") as archivo:
        campos = ["registro","categoria"]
        writer = csv.DictWriter(archivo, fieldnames=campos)

        if encabezado:
            writer.writeheader()
        writer.writerow({"registro": registro, "categoria": categoria})

def registrar_categoria(categoria):

    ruta = BASE_DIR / "datos" / "categorias.csv"
    ruta.parent.mkdir(exist_ok=True)

    encabezado = not ruta.exists() or ruta.stat().st_size == 0

    with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
        campos = ["categoria"]
        writer = csv.DictWriter(archivo, fieldnames=campos)

        if encabezado:
            writer.writeheader()
        if not comprobar_categoria(categoria) >= 1:
            writer.writerow({"categoria": categoria})    
    

   
