from tracker import nuevo

def mostrar_menu():
    while True:
        print("=== MENÚ DE OPCIONES ===")
        print("1. Registrar un temporizador nuevo")
        print("2. Seleccionar un temporizador")
        print("3. Ver estadísticas")

        opcion = input("\nSelecciona una opción: ")

        if not seleccionar(opcion):
            break
        
def seleccionar(opcion):
    if opcion == "1":
        nombre = input("Nombre a registrar: ")
        categoria = input("Categoria: ")
        nuevo(nombre, categoria)
    elif opcion == "2":
        nombre = input("Nombre a temporizar: ")
        horas = input("Horas: ")
        nuevo(nombre, horas)
    elif opcion == "3":
        print("Estado")
    else:
        print("\nOpción no válida. Introduce una de las opciones.\n")
        return True
    return False
