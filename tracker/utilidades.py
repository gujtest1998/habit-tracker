ROJO = "\033[31m"
VERDE = "\033[32m"
CIAN = "\033[36m"
INVERSION = "\033[7m"
RESET = "\033[0m"

import os

def print_color(texto,color):
    RESET = "\033[0m"
    print(f"{color}{texto}{RESET}")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def preguntar_seguir(seguir):
    while True:
        if seguir in ("s", "si"):
            limpiar_pantalla()
            return True
        elif seguir in ("n", "no"):
            limpiar_pantalla()
            return False
        else:
            print("Respuesta no válida.")
            break
        