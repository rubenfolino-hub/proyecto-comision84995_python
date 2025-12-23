...
"""
El formato de registro es: Nombre de usuario y Contraseña. clave : valor

Utilizar una función para almacenar la información y otra función para mostrar la información.

Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).

Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
"""

BD = {} # User : Password

def registro():
    ... # Para almacenar informacion (usuario: contraseña).


def mostrar_registros():
    ... # Mostrar los usuarios registrados.

def login():
    ... # Aca voy a simular un logeo.


def main():
    
    while True:
        # Mostrar un menu.
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            ...
        elif opcion == "2":
            ...
        elif opcion == "4":
            print("saliendo del programa.")
            break