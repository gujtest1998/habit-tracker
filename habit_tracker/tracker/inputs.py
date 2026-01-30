from datetime import datetime

def pedir_nombre_temp(lista):
    while True:
        try:
            nombre = input("\nNombre a temporizar: ")
            if nombre not in lista:
                print("Por favor, introduce un temporizador de la lista.")
                continue   
            else:
                return nombre
        except ValueError:
            print("\nHay que introducir un número decimal.")

def pedir_horas_temp():
    while True:
        horas = float(input("Horas: "))
        if horas == 0:
            print("No se pueden introducir 0 horas.")
            continue
        if horas < 0:
            print("No se pueden introducir horas negativas")
            continue
        return horas

def pedir_fecha_temp():
    while True:
            fecha = input("Introduce la fecha (AAAA-MM-DD) o déjalo vacío para hoy: ")
            
            if fecha == "":
                fecha = datetime.now().date()
            else:
                try:
                    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
                    fecha_hoy = datetime.now().date()

                    if fecha > fecha_hoy:
                        print("\nLa fecha no puede ser superior a la fecha actual.")
                        continue
                except ValueError:
                    print("Formato incorrecto. Debe ser AAAA-MM-DD")
                    continue
            return fecha
        