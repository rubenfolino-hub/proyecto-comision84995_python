##############################################
#        Diccionarios (dict) en Python       #
##############################################

# ¿Qué es un diccionario?
# Es una colección de pares "clave: valor".
# Se usa para guardar información relacionada.

diccionario = {}
diccionario_1 = dict()

diccionario = {"Hola": "Que tal", "frutas": ["manzana", "uva"], "numeros": [1, 4, 67]}

diccionario_2 = {
    "usuarios": {
        "user": "nicolas12",
        "password": "1234",
        "dni": 123321312
    }
}

persona = {
    "Nombre": "Ana",
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Córdoba"
}
print(persona)

# Acceder a los valores
print(persona["Nombre"])
print(persona.get("nombree", "Esta KEY no existe en el dict"))

persona["nombre"] = "Ezequiel"
persona["Nombre2"] = "Ruben"
print(persona)

del persona["Nombre2"]

print(persona)

nombre = persona.pop("nombre")
print(persona, nombre)

#persona.clear()
print(persona)

print(persona.keys())      # dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values())    # dict_values(['Ana', 30, 'Córdoba'])
print(persona.items())     # dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Córdoba')])

print("edad" in persona)
print("hola" in persona)

"""
Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018.
Y mostrarlo por pantalla.

Datos para la resolución:
1990: 'Alemania',
1994: 'Brasil',
1998: 'Francia',
2002: 'Brasil',
2006: 'Italia',
2010: 'España',
2014: 'Alemania'
2018: 'Francia'
"""
equipos = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia'
}

