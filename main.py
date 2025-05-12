# main.py

def saludar(nombre):
    print(f"Hola como estas, {nombre}!")

if __name__ == "__main__":
    nombre_usuario = input("¿Cuál es tu nombre? ")
    saludar(nombre_usuario)
