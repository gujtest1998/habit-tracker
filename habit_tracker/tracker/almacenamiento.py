import csv
from config import BASE_DIR
from pathlib import Path

def escribir(habito, tiempo):

    ruta = BASE_DIR / "datos" / "registro.csv"
    ruta.parent.mkdir(exist_ok=True)

    encabezado = not ruta.exists() or ruta.stat().st_size == 0

    with open(ruta, mode="a", newline="",encoding="utf-8") as archivo:
        campos = ["habito","tiempo"]
        writer = csv.DictWriter(archivo, fieldnames=campos)

        if encabezado:
            writer.writeheader()
        writer.writerow({"habito": habito, "tiempo": tiempo})

    

   
