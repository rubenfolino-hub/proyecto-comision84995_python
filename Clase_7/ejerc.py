"""
Actividad: Implementación en Python

Implementar la Clase de Alumno, directamente en Python.

Aclaraciones Generales:
- El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
- El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos de 5 puntos desaprueba la materia, más de 5 puntos aprueba.
    Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
- Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.

"""

class Alumno:
    def __init__ (self, nombre, nota):
       self.nombre = nombre
       self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} y Nota: {self.nota}")


    def resultado(self):
        if self.nota < 5:
            return f"El alumno {self.nombre} con la nota {self.nota} esta desaprobado"
        return f"El alumno {self.nombre} con la nota {self.nota} esta aprobado"

alumno_1 = Alumno("renzo", 3)
alumno_2 = Alumno("Nicolas", 2)
print(alumno_1.resultado())
alumno_1.imprimir()

print(alumno_2.resultado())
alumno_2.imprimir()


"""
Ejercicio 12.2. 
a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción con la suma de ambas.
c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción con el producto de ambas.

"""
class Fraccion:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"

    def __add__(self, otra_fraccion):
        # if isinstance(Fraccion, otra_fraccion) is False:
        #     raise ValueError("Para sumar es necesario que sea una fraccion.")
        nuevo_dividendo = self.dividendo * otra_fraccion.divisor + self.divisor * otra_fraccion.dividendo
        nuevo_divisor = self.divisor * otra_fraccion.divisor
        
        return Fraccion(nuevo_dividendo, nuevo_divisor)

    def __mul__(self, otro):
        nuevo_dividendo = self.dividendo * otro.dividendo
        nuevo_divisor = self.divisor * otro.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor)

fraccion = Fraccion(1, 2)
fraccion_2 = Fraccion(1, 2)
fraccion_3 = fraccion + fraccion_2
fraccion_4 = fraccion_3 * fraccion
print(fraccion, fraccion_2, fraccion_3, fraccion_4)


"""
Ejercicio 12.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

"""