# tuplas.py
# ==============================
# TUPLAS EN PYTHON
# ==============================
# Una tupla es una colección ordenada e inmutable de elementos.
# Se parecen a las listas, pero no se pueden modificar (no se pueden agregar, eliminar o cambiar elementos).
# Se usan para representar datos que no deben cambiar a lo largo del programa.

# ==============================
# CREACIÓN DE TUPLAS
# ==============================

# Tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# Tupla con elementos
numeros = (1, 2, 3, 4, 5)
print("Tupla de números:", numeros)

# Tupla con distintos tipos de datos
mixta = ("Nicolás", 30, True, 1.85)
print("Tupla mixta:", mixta)

# Tupla con un solo elemento (¡importante la coma!)
una_sola = (5,)
print("Tupla con un solo elemento:", una_sola, "| Tipo:", type(una_sola))

# También se pueden crear sin paréntesis (tuple packing)
tupla_sin_parentesis = 10, 20, 30
print("Tupla sin paréntesis:", tupla_sin_parentesis)

# ==============================
# ACCESO A ELEMENTOS
# ==============================
print("\nPrimer elemento:", numeros[0])
print("Último elemento:", numeros[-1])
print("Slice [1:4]:", numeros[1:4])

# ==============================
# INMUTABILIDAD
# ==============================
# No se puede modificar una tupla una vez creada
# numeros[0] = 10  # ❌ Esto da error

# ==============================
# MÉTODOS DE LAS TUPLAS
# ==============================
t = (1, 2, 2, 3, 4, 2, 5)

# count() -> Cuenta cuántas veces aparece un valor
print("\ncount(2):", t.count(2))

# index() -> Devuelve la primera posición de un valor
print("index(3):", t.index(3))

# ==============================
# OPERACIONES CON TUPLAS
# ==============================

# Concatenar tuplas
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print("\nConcatenación:", t3)

# Repetir elementos
repetida = t1 * 3
print("Repetida 3 veces:", repetida)

# Verificar si un elemento está en la tupla
print("¿2 está en t1?:", 2 in t1)
print("¿9 está en t1?:", 9 in t1)

# Longitud de una tupla
print("Longitud de t3:", len(t3))

# ==============================
# RECORRER TUPLAS
# ==============================
print("\nRecorrer elementos de una tupla:")
for n in t1:
    print(n)

# ==============================
# DESEMPAQUETADO DE TUPLAS
# ==============================
# Se puede asignar cada elemento a una variable
persona = ("Mica", 25, "Diseñadora")
nombre, edad, profesion = persona
print("\nDesempaquetado:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Profesión:", profesion)

# También se puede usar * para capturar varios valores
valores = (1, 2, 3, 4, 5)
primero, *medio, ultimo = valores
print("\nUsando * para desempaquetar:")
print("Primero:", primero)
print("Medio:", medio)
print("Último:", ultimo)

# ==============================
# TUPLAS ANIDADAS
# ==============================
coordenadas = ((1, 2), (3, 4), (5, 6))
print("\nTuplas anidadas:", coordenadas)
print("Acceder a coordenada [1][0]:", coordenadas[1][0])

# ==============================
# CONVERTIR ENTRE LISTAS Y TUPLAS
# ==============================
lista = [10, 20, 30]
tupla_convertida = tuple(lista)
print("\nLista convertida a tupla:", tupla_convertida)

lista_nueva = list(tupla_convertida)
print("Tupla convertida a lista:", lista_nueva)

# ==============================
# USOS COMUNES DE LAS TUPLAS
# ==============================

# 1. Como claves en diccionarios (porque son inmutables)
puntos = {
    (0, 0): "Origen",
    (1, 2): "Punto A",
    (2, 3): "Punto B"
}
print("\nDiccionario con tuplas como claves:", puntos)

# ==============================
# CONCLUSIÓN
# ==============================
# Las tuplas se usan cuando:
# - Querés agrupar datos inmutables (que no deben cambiar)
# - Necesitás eficiencia (las tuplas ocupan menos memoria que las listas)
# - Trabajás con coordenadas, registros o retornos múltiples
