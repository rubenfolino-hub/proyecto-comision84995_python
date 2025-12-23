"""
📌 POLIMORFISMO EN POO (Python)

👉 El polimorfismo es un principio de la Programación Orientada a Objetos
   que permite que un mismo método (o función) se comporte de manera
   diferente según el objeto que lo invoque.

✅ Características:
- "Un mismo nombre, múltiples comportamientos".
- Se da cuando varias clases diferentes implementan un método con el mismo nombre.
- Facilita el uso de una interfaz común para distintos tipos de objetos.
- Puede usarse tanto con herencia como sin ella (duck typing en Python).

-------------------------------------------------------
🔹 Ejemplo básico con herencia:
"""

class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miauuuu!"

# Uso del polimorfismo
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    print(animal.hacer_sonido())


"""
🔹 Polimorfismo con Duck Typing (Python no necesita herencia obligatoria):
"""

class Pato:
    def hablar(self):
        return "Cuac cuac"

class Persona:
    def hablar(self):
        return "Hola, soy una persona"

def hacer_hablar(objeto):
    print(objeto.hablar())

hacer_hablar(Pato())     # Cuac cuac
hacer_hablar(Persona())  # Hola, soy una persona

"""
Aquí no importa si tienen herencia común,
lo importante es que ambos tienen el método "hablar".
Esto es duck typing: "si camina como pato y suena como pato... es un pato".
"""


"""
✅ Beneficios del polimorfismo:
1. Permite escribir código más flexible y reutilizable.
2. Reduce la necesidad de condicionales (if/else) para distinguir objetos.
3. Facilita la extensibilidad: se pueden agregar nuevas clases sin modificar el código existente.
4. Se integra naturalmente con la herencia.

-------------------------------------------------------
🔹 Ejemplo práctico en una aplicación:
Supongamos un sistema de pagos que soporta diferentes métodos:
"""

class Pago:
    def procesar(self, monto):
        raise NotImplementedError("Este método debe ser implementado")

class PagoConTarjeta(Pago):
    def procesar(self, monto):
        return f"Procesando pago con tarjeta de ${monto}"

class PagoConPaypal(Pago):
    def procesar(self, monto):
        return f"Procesando pago con PayPal de ${monto}"

# Cliente usando polimorfismo
def realizar_pago(pago: Pago, monto):
    print(pago.procesar(monto))
# Cliente.realizar_pago(PagoConTarjeta(), 10000)
pagos = [PagoConTarjeta(), PagoConTarjeta(), PagoConPaypal()]

for pago in pagos:
    realizar_pago(pago, 50000)

"""
Salida:
Procesando pago con tarjeta de $1000
Procesando pago con PayPal de $2000

👉 Aquí se ve el poder del polimorfismo: la función "realizar_pago"
puede trabajar con cualquier clase de pago sin importar cómo esté implementada.
"""
