#Consigna TP1

BASE_DE_DATOS = {}

def almacenar_usuario(usuario: str, contrasena: str):
    global BASE_DE_DATOS 
    BASE_DE_DATOS[usuario] = contrasena
    print(f"\n Usuario '{usuario}' registrado y almacenado exitosamente")

def registrar_usuario():
    global BASE_DE_DATOS 
    
    print("\n---  REGISTRO DE NUEVO USUARIO ---")
    
    while True:
        nombre_usuario = input("Ingrese el nombre de usuario (o 'salir' para cancelar): ").strip()
        
        if nombre_usuario.lower() == 'salir':
            print("Registro cancelado.")
            return
        
        if nombre_usuario in BASE_DE_DATOS:
            print(f"X El nombre de usuario '{nombre_usuario}' ya existe. Intente con otro.")
        elif len(nombre_usuario) < 3:
            print("X El nombre de usuario debe tener al menos 3 caracteres.")
        else:
            break

    while True:
        contrasena = input("Ingrese la contraseña: ").strip()
        
        if len(contrasena) < 6:
            print("X La contraseña debe tener al menos 6 caracteres.")
        else:
            break
    
    almacenar_usuario(nombre_usuario, contrasena)


def login_usuario():
    print("\n---  INICIO DE SESIÓN ---")
    
    usuario = input("Nombre de usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    if usuario in BASE_DE_DATOS:
        if BASE_DE_DATOS[usuario] == contrasena:
            print(f"\n Bienvenido, {usuario} Sesión iniciada correctamente.")
        else:
            print("\nX Contraseña incorrecta.")
    else:
        print(f"\nX El usuario '{usuario}' no se encuentra registrado.")

def mostrar_usuarios():
    print("\n---  USUARIOS REGISTRADOS ---")
    
    if not BASE_DE_DATOS:
        print("La base de datos está vacía. No hay usuarios registrados.")
        return
    
    print(f"Total de usuarios registrados: {len(BASE_DE_DATOS)}")
    print("-" * 30)

    for usuario, contrasena in BASE_DE_DATOS.items():
        print(f" Usuario: {usuario} | Longitud Contraseña: {len(contrasena)}")
    
    print("-" * 30)

def ejecutar_programa():
    print(" BIENVENIDO AL SISTEMA DE GESTIÓN DE USUARIOS")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión (Login)")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            login_usuario()
        elif opcion == '3':
            mostrar_usuarios()
        elif opcion == '4':
            print("\n Gracias por usar el sistema.")
            break
        else:
            print("\nX Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_programa()
    
