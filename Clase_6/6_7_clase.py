# Unidad 6: Excepciones y Programación Orientada a Objetos en Python

"""
Esta unidad se centra en el manejo de excepciones y los principios básicos de la Programación Orientada a Objetos en Python.
Incluye actividades prácticas para fortalecer la comprensión de estos conceptos.
"""

# ---------------------------------------
# Actividad: Desafío de errores
# ---------------------------------------

def dividir(a, b):
    ...

# Ejemplo de uso:
resultado = dividir(10, 2)
print(f"Resultado de dividir 10 entre 2: {resultado}")

resultado = dividir(10, 0)
print(f"Resultado de dividir 10 entre 0: {resultado}")
# Al dividir entre 0, se retorna None

# ---------------------------------------
# Actividad: Desafío de excepciones
# ---------------------------------------

def dividir_con_excepcion(a, b):
    ...

# Ejemplo de uso:
dividir_con_excepcion(10, 0)  # Mostrará el mensaje: No se puede dividir entre cero


# ---------------------------------------
# Actividad: Diagrama de clases
# ---------------------------------------

"""
Representación del siguiente escenario en un diagrama de clases:
1. La clase `Persona` actúa como clase base.
2. `Empleado` y `Cliente` heredan de `Persona`.
3. `Empleado` tiene un atributo de `sueldo_bruto`.
4. `Directivo` (una subclase de `Empleado`) tiene una `categoría` y subordinados.
5. `Cliente` añade un `telefono_de_contacto`.

"""

# ---------------------------------------
# Ejemplo en Python: Programación Orientada a Objetos
# ---------------------------------------

class Persona:
    """
    Clase base para representar a una persona.
    
    Atributos:
    nombre (str): El nombre de la persona.
    edad (int): La edad de la persona.
    """
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    """
    Clase para representar a un empleado, derivada de Persona.
    
    Atributos adicionales:
    sueldo_bruto (float): El sueldo bruto del empleado.
    """
    
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    """
    Clase para representar a un directivo, derivada de Empleado.
    
    Atributos adicionales:
    categoria (str): Categoría del directivo.
    subordinados (list): Lista de empleados subordinados.
    """
    
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Cliente(Persona):
    """
    Clase para representar a un cliente, derivada de Persona.
    
    Atributos adicionales:
    telefono_de_contacto (str): Teléfono de contacto del cliente.
    """
    
    def __init__(self, nombre, edad, telefono_de_contacto):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono_de_contacto

# Ejemplo de uso:

# Crear objetos de cada clase
empleado = Empleado("Ana", 30, 35000)
directivo = Directivo("Carlos", 45, 50000, "Gerente")
cliente = Cliente("Luis", 28, "123-456-789")

# Agregar subordinado
directivo.agregar_subordinado(empleado)

# Imprimir detalles
print(f"Empleado: {empleado.nombre}, Edad: {empleado.edad}, Sueldo: {empleado.sueldo_bruto}")
print(f"Directivo: {directivo.nombre}, Edad: {directivo.edad}, Categoría: {directivo.categoria}")
print(f"Cliente: {cliente.nombre}, Edad: {cliente.edad}, Teléfono: {cliente.telefono_de_contacto}")

