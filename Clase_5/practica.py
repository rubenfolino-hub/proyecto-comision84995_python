"""
Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto

Si se ingresa algo que no sea número, debe indicar que se ingrese un número.
Información a tener en cuenta:
Se recuerda que los años bisiestos son múltiplos de 4,
pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

"""

def es_numero(dato):
    if dato.isdigit():
        return True
    return False


def anio_bisiesto(anio):
    while not es_numero(anio):
        anio = input("Ingrese un año: ")
    anio = int(anio)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El anio {anio} es bisiesto!")
        return None

    print(f"El anio {anio} no es bisiesto")

# anio_bisiesto(input("Ingrese un anio: "))


"""

Realiza una función llamada area_rectangulo() que devuelva
el área del rectángulo a partir de una base y una altura.
Calcula el área de un rectángulo de 15 de base y 10 de altura
🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""


def area_rectangulo(base, altura):
    area = base * altura
    return area
res = area_rectangulo(15, 10)
print(res)
# def area_rectangulo():
#     base=15
#     altura=10
#     global area
#     area= base*altura
#     return area
# area_rectangulo()
# print(f"El area del rectangulo es de {area}")


"""
Actividad: Conversiones tipos de datos Consigna: Pasaremos de milímetros a metros según el parámetro de la función.
Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros.
1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y mostremos los milímetros.
2- Si recibe 3 argumentos, supone que son metros, centímetros y los convierte a milímetros.

"""

def convertir_milimetros(*args): # args la vamos a tratar como una lista
    if len(args) == 1:
        milimetros = args[0]
        metros = milimetros / 1000
        centimetros = milimetros /10
        print(f"Milimetros: {milimetros} mm")
        print(f"Centimetros: {centimetros} cm")
        print(f"Metros: {metros} mts")
    elif len(args) == 3:
        metros, centimetros, milimetros = args
        metros_x_milimetros = metros *1000
        cm_x_milimetros = centimetros * 10
        print(f"Milimetros: {milimetros} mm")
        print(f"Centimetros a mm: {cm_x_milimetros} mm")
        print(f"Metros a mm: {metros_x_milimetros} mm")
    else:
        print("La cantidad de argumentos no es ni 1 ni 3.")

convertir_milimetros(10)
convertir_milimetros(1, 1, 1)
