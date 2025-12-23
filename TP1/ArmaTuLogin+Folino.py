

# Consigna TP1: Script para un sistema básico de registro e inicio de sesión.
# Utiliza un diccionario en memoria (BASE_DE_DATOS) para almacenar la información.

# BASE DE DATOS GLOBAL: Diccionario que almacena usuarios y contraseñas.
# Clave (Key): Nombre de usuario (string)
# Valor (Value): Contraseña (string)
BASE_DE_DATOS = {}

def almacenar_usuario(usuario: str, contrasena: str):
    """
    Función: Almacena el usuario y la contraseña en la BASE_DE_DATOS.
    """
    # Se declara 'global' para modificar el diccionario fuera de la función.
    global BASE_DE_DATOS 
    
    # Almacena el par usuario:contraseña en el diccionario.
    BASE_DE_DATOS[usuario] = contrasena
    
    # Muestra una confirmación de éxito.
    print(f"\n Usuario '{usuario}' registrado y almacenado exitosamente")

def registrar_usuario():
    """
    Función: Gestiona la interacción con el usuario para registrar una nueva cuenta, 
    aplicando validaciones.
    """
    global BASE_DE_DATOS 
    
    print("\n---  REGISTRO DE NUEVO USUARIO ---")
    
    # Bucle para solicitar y validar el nombre de usuario.
    while True:
        nombre_usuario = input("Ingrese el nombre de usuario (o 'salir' para cancelar): ").strip()
        
        # Opción para cancelar el registro y salir de la función.
        if nombre_usuario.lower() == 'salir':
            print("Registro cancelado.")
            return
        
        # Validación 1: El usuario ya existe en la BASE_DE_DATOS.
        if nombre_usuario in BASE_DE_DATOS:
            print(f"X El nombre de usuario '{nombre_usuario}' ya existe. Intente con otro.")
        # Validación 2: Longitud mínima del nombre de usuario (3 caracteres).
        elif len(nombre_usuario) < 3:
            print("X El nombre de usuario debe tener al menos 3 caracteres.")
        # Si las validaciones son correctas, sale del bucle.
        else:
            break

    # Bucle para solicitar y validar la contraseña.
    while True:
        contrasena = input("Ingrese la contraseña: ").strip()
        
        # Validación 3: Longitud mínima de la contraseña (6 caracteres).
        if len(contrasena) < 6:
            print("X La contraseña debe tener al menos 6 caracteres.")
        # Si la validación es correcta, sale del bucle.
        else:
            break
    
    # Llama a la función de almacenamiento con los datos validados.
    almacenar_usuario(nombre_usuario, contrasena)


def login_usuario():
    """
    Función: Intenta iniciar sesión verificando las credenciales contra la BASE_DE_DATOS.
    """
    print("\n---  INICIO DE SESIÓN ---")
    
    # Solicita credenciales de entrada.
    usuario = input("Nombre de usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    # 1. Verifica si el usuario existe como clave en el diccionario.
    if usuario in BASE_DE_DATOS:
        # 2. Si existe, compara la contraseña ingresada con la almacenada (el valor del diccionario).
        if BASE_DE_DATOS[usuario] == contrasena:
            print(f"\n Bienvenido, {usuario} Sesión iniciada correctamente.")
        # Contraseña incorrecta.
        else:
            print("\nX Contraseña incorrecta.")
    # Usuario no encontrado/no registrado.
    else:
        print(f"\nX El usuario '{usuario}' no se encuentra registrado.")

def mostrar_usuarios():
    """
    Función: Muestra una lista de todos los usuarios registrados y la longitud de sus contraseñas.
    """
    print("\n---  USUARIOS REGISTRADOS ---")
    
    # Verifica si la base de datos está vacía.
    if not BASE_DE_DATOS:
        print("La base de datos está vacía. No hay usuarios registrados.")
        return
    
    # Muestra el total de usuarios registrados.
    print(f"Total de usuarios registrados: {len(BASE_DE_DATOS)}")
    print("-" * 30)

    # Itera sobre cada par clave (usuario) y valor (contraseña) del diccionario.
    for usuario, contrasena in BASE_DE_DATOS.items():
        # Muestra el nombre de usuario y la longitud de la contraseña.
        print(f" Usuario: {usuario} | Longitud Contraseña: {len(contrasena)}")
    
    print("-" * 30)

def ejecutar_programa():
    """
    Función: Bucle principal que muestra el menú e invoca las funciones correspondientes.
    """
    print(" BIENVENIDO AL SISTEMA DE GESTIÓN DE USUARIOS")

    # Bucle infinito para mantener el menú en ejecución.
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión (Login)")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        # Control de flujo según la opción seleccionada.
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            login_usuario()
        elif opcion == '3':
            mostrar_usuarios()
        elif opcion == '4':
            print("\n Gracias por usar el sistema.")
            # Rompe el bucle 'while True' y termina el programa.
            break
        else:
            print("\nX Opción no válida. Por favor, ingrese un número del 1 al 4.")

# Punto de entrada del script (ejecución principal).
# Asegura que 'ejecutar_programa()' solo se llame si el script se ejecuta directamente.
if __name__ == "__main__":
    ejecutar_programa()


    

