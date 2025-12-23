# Asociacion
"""
Es una relación débil, donde dos clases se relacionan pero pueden existir por separado.
Por ejemplo, un Profesor enseña en un Curso, pero ambos pueden existir por separado.

"""

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def ensenar(self, alumno):
        print(f"{self.nombre} enseña a {alumno.nombre}")

    def saludar(self):
        print(f"Hola me llamo {self.nombre}")

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

prof = Profesor("Ana")
alumno = Alumno("Juan")
prof.ensenar(alumno)


# Composicion

"""
Un Coche tiene un Motor.
Si el coche deja de existir, el motor también.
Una clase contiene otra clase como parte esencial: si el objeto principal se destruye, los objetos contenidos también desaparecen
"""

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def encender(self):
        print(f"Motor encendido con potencia {self.potencia}")

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("150HP") 

auto = Coche("Toyota")
print(auto.motor.potencia)
auto.motor.encender()


# Agregacion

"""
Una Escuela tiene Profesores.
Si la escuela cierra, los profesores pueden trabajar en otro lugar.
Es una relación “tiene un”, pero más débil que la composición.
El objeto contenido puede existir sin el objeto que lo contiene.
En la práctica, se parece mucho a la asociación, pero suele representar una relación de conjunto.
"""

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

prof1 = Profesor("Ana")
prof2 = Profesor("Luis")

escuela = Escuela("Colegio Central")
escuela.agregar_profesor(prof1)
escuela.agregar_profesor(prof2)

# Generalizacion / Herencia

"""
Perro y Gato son Animales.
Comparten características pero cada uno puede tener comportamientos propios.
"""

class Animal: # Clase Padre / base
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        print(f"{self.nombre} se mueve")

class Perro(Animal): # Clase Hijo de Animal
    def ladrar(self):
        print("Guau!")

class Gato(Animal): # Clase Hija de Animal
    def maullar(self):
        print("Miau!")

perro = Perro("Firulais")
perro.mover()
perro.ladrar()

gato = Gato("Mishi")
gato.mover()
gato.maullar()

for animal in [Perro("Firulais"), Perro("Fede"), Gato("Mishi"), Gato("algo")]:  # Polimorfismo
    animal.mover()




"""
| Relación           | Ejemplo en la vida real | Dependencia | Frase clave            |
| ------------------ | ----------------------- | ----------- | ---------------------- |
| **Composición**    | Auto → Motor            | Fuerte      | “Es parte de”          |
| **Asociación**     | Profesor → Curso        | Débil       | “Usa / conoce a”       |
| **Agregación**     | Curso → Estudiantes     | Media       | “Tiene un conjunto de” |
| **Generalización** | Perro → Animal          | Herencia    | “Es un”                |

"""