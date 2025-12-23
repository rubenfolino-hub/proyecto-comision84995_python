# =========================================
# MÉTODOS Y ATRIBUTOS EN PYTHON
# =========================================

# 1) ATRIBUTOS:
# - Son variables asociadas a una clase o a una instancia (objeto).
# - Pueden ser:
#   * De instancia -> propios de cada objeto.
#   * De clase -> compartidos por todos los objetos de la clase.

class Persona:
    # Atributo de clase (compartido por todas las instancias)
    especie = "Humano"

    def __init__(self, nombre, edad):
        # Atributos de instancia (propios de cada objeto)
        self.nombre = nombre
        self.edad = edad


# Uso
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

print(p1.nombre)        # Ana  (atributo de instancia)
print(p2.nombre)        # Luis
print(p1.especie)       # Humano (atributo de clase)
print(p2.especie)       # Humano
Persona.especie = "Robot"
print(p1.especie)       # Humano (atributo de clase)
print(p2.especie)       # Humano


# 2) MÉTODOS:
# - Funciones definidas dentro de una clase.
# - Tipos:
#   * De instancia -> acceden y modifican atributos del objeto (self).
#   * De clase -> trabajan a nivel de clase, usan cls en lugar de self.
#   * Estáticos -> no acceden ni a la clase ni a la instancia directamente.


class Calculadora:
    # Atributo de clase
    historial = []

    def __init__(self, valor):
        self.valor = valor  # atributo de instancia

    # Método de instancia
    def sumar(self, numero):
        self.valor += numero
        Calculadora.historial.append(f"Suma: {numero}")
        return self.valor

    # Método de clase
    @classmethod
    def ver_historial(cls):
        return cls.historial

    # Método estático
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0


# Uso
calc = Calculadora(10)
print(calc.sumar(5))             # 15
print(calc.sumar(20))            # 35

# Método de clase (se llama con la clase directamente o con el objeto)
print(Calculadora.ver_historial())  # ['Suma: 5', 'Suma: 20']

# Método estático
print(Calculadora.es_par(10))    # True
print(calc.es_par(7))            # False


# =========================================
# RESUMEN
# =========================================
# - Atributos de instancia: únicos de cada objeto.
# - Atributos de clase: compartidos por todos.
# - Métodos de instancia: usan self, acceden a datos de un objeto.
# - Métodos de clase: usan cls, acceden a la clase en general.
# - Métodos estáticos: no usan ni self ni cls, son funciones auxiliares.
