ROJO = "\033[31m"
VERDE = "\033[32m"
CIAN = "\033[36m"
RESET = "\033[0m"

def print_color(texto,color):
    RESET = "\033[0m"
    print(f"{color}{texto}{RESET}")