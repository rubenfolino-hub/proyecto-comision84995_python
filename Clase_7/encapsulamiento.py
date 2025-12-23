"""
Resumen: Encapsulamiento en POO con Python
-------------------------------------------

El encapsulamiento es un pilar de la Programación Orientada a Objetos (POO).
Permite controlar el acceso a los atributos y métodos de una clase,
protegidos o privados, para mantener la integridad de los datos.

Tipos de atributos según su visibilidad:

1. Públicos:
   - Se definen normalmente (ej: self.nombre).
   - Son accesibles desde fuera de la clase sin restricciones.

2. Protegidos:
   - Se nombran con un guion bajo (ej: self._edad).
   - Convención: indican que deben usarse solo dentro de la clase
     y sus subclases, aunque técnicamente se pueden acceder desde fuera.

3. Privados:
   - Se nombran con doble guion bajo (ej: self.__dni).
   - Python aplica "name mangling" (_NombreClase__atributo),
     lo que dificulta el acceso directo desde fuera de la clase.

Uso de getters y setters:
   - Los getters permiten obtener el valor de un atributo privado.
   - Los setters permiten modificar el valor de un atributo privado
     controlando la validez de los datos.
   - Se pueden implementar con métodos o con la función property().

"""

# Ejemplo de Encapsulamiento con Python

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre        # Público
        self._edad = edad           # Protegido
        self.__dni = dni            # Privado

    # Getter para __dni
    def validar(self):
        return True

    def get_dni(self):
        if self.validar():
            return self.__dni
        return "No tenes permisos para ver el dni"
        # Getter y Setter usando property

    @property # Decorador.
    def edad(self):
        if self.validar():
            return self._edad
        return "No tenes permisos"

    # Setter para __dni con validación
    def set_dni(self, nuevo_dni): # "3798472732".. 23765472 ... "gh2854729"
        if isinstance(nuevo_dni, str) and nuevo_dni.isdigit():
            self.__dni = nuevo_dni
        else:
            print("DNI inválido. Debe ser un número en formato string.")

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")


# Uso de la clase
p = Persona("Juan", 30, "12345678")

print("Nombre (público):", p.nombre)
print("Edad (protegido, accedida con property):", p.edad)

# Intento de acceder a __dni directamente falla
# print(p.__dni)  # AttributeError

# # Acceso correcto con getter
print("DNI (con getter):", p.get_dni())

# # Cambiar valor con setter
p.set_dni("87654321")
print("Nuevo DNI:", p.get_dni())

# # Usando setter de property
p.edad = -5      # Mensaje de error
p.edad = 35
print("Edad actualizada:", p.edad)
