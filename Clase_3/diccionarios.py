# diccionarios.py
# ==============================
# DICCIONARIOS EN PYTHON (dict)
# ==============================
# Un diccionario es una colección de pares clave: valor.
# Las claves deben ser únicas e inmutables (strings, números o tuplas).
# Los valores pueden ser de cualquier tipo.

# Crear un diccionario
persona = {
    "nombre": "Nicolás",
    "edad": 30,
    "profesion": "Desarrollador"
}

print("Diccionario inicial:", persona)

# También se puede crear con dict()
persona2 = dict(nombre="Micaela", edad=25, profesion="Diseñadora")
print("Creado con dict():", persona2)

# ==============================
# ACCESO A VALORES
# ==============================

# Acceder a un valor por su clave
print("\nAcceder a clave 'nombre':", persona["nombre"])

# get() -> Devuelve el valor si existe, o un valor por defecto si no
print("get('altura'):", persona.get("altura", "No especificada"))

# ==============================
# MODIFICAR Y AGREGAR ELEMENTOS
# ==============================

# Agregar una nueva clave
persona["altura"] = 1.86
print("\nAgregar clave 'altura':", persona)

# Modificar un valor existente
persona["edad"] = 31
print("Modificar clave 'edad':", persona)

# ==============================
# ELIMINAR ELEMENTOS
# ==============================

# pop() -> Elimina una clave y devuelve su valor
edad = persona.pop("edad")
print("\npop('edad'):", edad, "| Diccionario:", persona)

# popitem() -> Elimina el último par insertado (en Python 3.7+)
ultimo = persona.popitem()
print("popitem():", ultimo, "| Diccionario:", persona)

# del -> Elimina una clave directamente
del persona["altura"]
print("del clave 'altura':", persona)

# clear() -> Vacía el diccionario
temp = {"a": 1, "b": 2}
temp.clear()
print("clear():", temp)

# ==============================
# MÉTODOS DE DICCIONARIOS
# ==============================

d = {"a": 1, "b": 2, "c": 3}

# 1. keys() -> Devuelve las claves
print("\nkeys():", d.keys())

# 2. values() -> Devuelve los valores
print("values():", d.values())

# 3. items() -> Devuelve pares (clave, valor)
print("items():", d.items())

# 4. update() -> Combina otro diccionario o pares clave=valor
d.update({"d": 4, "a": 100})
print("update():", d)

# 5. copy() -> Crea una copia del diccionario
copia = d.copy()
print("copy():", copia)

# ==============================
# MÉTODOS DE CONSTRUCCIÓN
# ==============================

# 6. fromkeys() -> Crea un nuevo diccionario con claves dadas y un valor inicial
claves = ["x", "y", "z"]
nuevo = dict.fromkeys(claves, 0)
print("\nfromkeys():", nuevo)

# ==============================
# RECORRER DICCIONARIOS
# ==============================

usuario = {"nombre": "Leo", "rol": "Admin", "activo": True}

print("\nRecorrer claves:")
for clave in usuario:
    print(clave)

print("Recorrer claves y valores con items():")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# ==============================
# COMPRENSIONES DE DICCIONARIOS
# ==============================
# Se puede crear un diccionario con una expresión compacta
cuadrados = {x: x**2 for x in range(5)}
print("\nDiccionario por comprensión:", cuadrados)

# ==============================
# VERIFICAR CLAVES Y VALORES
# ==============================
print("\n'a' en d?:", "a" in d)
print("100 en d.values()?:", 100 in d.values())

# ==============================
# EJEMPLOS PRÁCTICOS
# ==============================

# Contar frecuencia de letras en una palabra
palabra = "banana"
frecuencia = {}
for letra in palabra:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1
print("\nFrecuencia de letras:", frecuencia)

# ==============================
# CONCLUSIÓN
# ==============================
# Los diccionarios son ideales para:
# - Asociar datos (clave: valor)
# - Buscar valores rápidamente
# - Representar objetos, configuraciones o registros
