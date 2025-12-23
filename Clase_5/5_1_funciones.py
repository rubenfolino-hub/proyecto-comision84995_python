
# --------------------------------------------------------------
# Creación de Funciones
# --------------------------------------------------------------
def saludar():
    """
    Esta función imprime un mensaje de saludo.
    """
    print("Hola, ¿cómo estás?")

# Llamada a la función
#saludar()
# Salida esperada: Hola, ¿cómo estás?

# --------------------------------------------------------------
# Parámetros y Argumentos
# --------------------------------------------------------------
def saludar_con_nombre(nombre, segundo_nombre=None):
    """
    Esta función recibe un nombre como parámetro y saluda a esa persona.
    """
    if segundo_nombre is None:
        print(f"Hola, {nombre}, ¿cómo estás?") # f-strings
    else:
        print(f"Hola, {nombre} - {segundo_nombre}, ¿cómo estás?")

# Llamada a la función con un argumento:
#saludar_con_nombre("Ezequiel", "Nicolas")
# # Salida esperada: Hola, Juan, ¿cómo estás?
def decision(nombre=None, segundo_nombre=None):
    if nombre is None and segundo_nombre is None:
        saludar()
    else:
        saludar_con_nombre(nombre, segundo_nombre)


# var = decision("Nicolas", "ezequiel")
# print(var)
# # --------------------------------------------------------------
# # Retorno de Valores
# # --------------------------------------------------------------

def sumar(a, b, c=0):
    """
    Esta función toma dos números como parámetros y retorna su suma.
    """
    return a + b + c

# # Llamada a la función y almacenando el resultado:
# resultado = sumar(100, sumar(2, 5, 3))
# print(resultado)
# # Salida esperada: 8

# # --------------------------------------------------------------
# # Sintaxis Básica de una Función
# # --------------------------------------------------------------

def multiplicar(a, b):
    """
    Toma dos números y retorna su producto.
    """
    resultado = a * b
    return resultado

# # Llamada a la función:
print(multiplicar(4, 5))
# # Salida esperada: 20

# # --------------------------------------------------------------
# # Ejemplo Práctico
# # --------------------------------------------------------------

def crear_saludo(nombre):
    """
    Recibe un nombre y retorna un mensaje de saludo.
    """
    mensaje = f"Hola, {nombre}!"
    return mensaje

# # Llamada a la función:
resultado = crear_saludo("Ana")
print(f"Resultado: {resultado}")
# # Salida esperada: Hola, Ana!

# # --------------------------------------------------------------
# # Definición y Llamada de una Función
# # --------------------------------------------------------------

# # Definición de una función:
def restar(a: int = 0, b: int = 0, c: int = 0) -> int:
    """
    Resta el segundo parámetro del primero y retorna el resultado.
    """
    return a - b - c

# # Llamada a la función:
# resultado = restar(a=10, b="a", c=5)
# print(resultado)
# # Salida esperada: 5

# # --------------------------------------------------------------
# # Ejemplo de Función Básica
# # --------------------------------------------------------------

# def saludar_simple():
#     """
#     Imprime un mensaje de saludo.
#     """
#     print("Estoy saludando desde la función")

# # Llamada a la función
# saludar_simple()
# # Salida esperada: Estoy saludando desde la función

# # --------------------------------------------------------------
# # Ejemplo Completo
# # --------------------------------------------------------------

# # Este ejemplo incluye una función definida y llamada en el código principal.
# def despedirse():
#     """
#     Imprime un mensaje de despedida.
#     """
#     print("Adiós, hasta luego!")

# # Llamada a la función
# despedirse()
# # Salida esperada: Adiós, hasta luego!

# # --------------------------------------------------------------
# # Conclusión
# # --------------------------------------------------------------

