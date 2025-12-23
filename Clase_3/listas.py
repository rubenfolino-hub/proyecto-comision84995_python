# listas.py
# ==============================
# LISTAS EN PYTHON
# ==============================
# Una lista es una colección ordenada y mutable.
# Se usan para almacenar múltiples elementos en una sola variable.

# ==============================
# CREACIÓN DE LISTAS
# ==============================
# Lista vacía
lista_vacia = []
print("Lista vacía:", lista_vacia)

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
print("Lista de números:", numeros)

# Lista con distintos tipos de datos
mixta = ["Nicolás", 30, True, 1.85]
print("Lista mixta:", mixta)

# Lista de listas (anidada)
anidada = [[1, 2], [3, 4], [5, 6]]
print("Lista anidada:", anidada)

# ==============================
# ACCESO A ELEMENTOS
# ==============================
print("\nPrimer elemento:", numeros[0])
print("Último elemento:", numeros[-1])
print("Slice [1:4]:", numeros[1:4])

# ==============================
# MODIFICAR ELEMENTOS
# ==============================
numeros[0] = 100
print("\nModificar primer elemento:", numeros)

# ==============================
# AGREGAR ELEMENTOS
# ==============================

# append() -> Agrega un elemento al final
numeros.append(6)
print("\nappend(6):", numeros)

# insert() -> Inserta un elemento en una posición específica
numeros.insert(2, 200)
print("insert(2, 200):", numeros)

# extend() -> Agrega múltiples elementos (otra lista)
numeros.extend([7, 8, 9])
print("extend([7, 8, 9]):", numeros)

# ==============================
# ELIMINAR ELEMENTOS
# ==============================

# pop() -> Elimina y devuelve el último elemento (o el de un índice)
ultimo = numeros.pop()
print("\nElemento eliminado con pop():", ultimo, "| Lista:", numeros)

# remove() -> Elimina la primera aparición de un valor
numeros.remove(200)
print("remove(200):", numeros)

# del -> Elimina por índice o toda la lista
del numeros[0]
print("del numeros[0]:", numeros)

# clear() -> Vacía la lista
temp = [1, 2, 3]
temp.clear()
print("clear():", temp)

# ==============================
# MÉTODOS DE LISTAS
# ==============================
letras = ["a", "b", "c", "d", "a", "b"]

# count() -> Cuenta cuántas veces aparece un valor
print("\ncount('a'):", letras.count("a"))

# index() -> Devuelve la primera posición de un valor
print("index('c'):", letras.index("c"))

# reverse() -> Invierte el orden de la lista
letras.reverse()
print("reverse():", letras)

# sort() -> Ordena la lista (alfabéticamente o numéricamente)
numeros2 = [5, 2, 8, 1, 3]
numeros2.sort()
print("sort() creciente:", numeros2)

# Orden descendente
numeros2.sort(reverse=True)
print("sort(reverse=True):", numeros2)

# copy() -> Crea una copia de la lista
copia = numeros2.copy()
print("copy():", copia)

# ==============================
# FUNCIONES INTEGRADAS ÚTILES
# ==============================
valores = [10, 20, 30, 40, 50]

print("\nlen(valores):", len(valores))        # Cantidad de elementos
print("sum(valores):", sum(valores))          # Suma de los valores
print("max(valores):", max(valores))          # Valor máximo
print("min(valores):", min(valores))          # Valor mínimo
print("sorted(valores):", sorted(valores))    # Devuelve una nueva lista ordenada
print("sorted(valores, reverse=True):", sorted(valores, reverse=True))

# ==============================
# RECORRER LISTAS
# ==============================
print("\nRecorrer lista con for:")
for numero in valores:
    print(numero)

print("Recorrer con índice y valor usando enumerate():")
for i, numero in enumerate(valores):
    print(f"Índice {i}: Valor {numero}")

# ==============================
# OPERACIONES CON LISTAS
# ==============================
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenar listas
c = a + b
print("\nConcatenación:", c)

# Repetir elementos
repetida = a * 3
print("Repetida 3 veces:", repetida)

# Verificar si un elemento está en la lista
print("¿2 está en a?:", 2 in a)
print("¿9 está en a?:", 9 in a)

# ==============================
# LISTAS ANIDADAS
# ==============================
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatriz 3x3:", matriz)
print("Elemento [1][2]:", matriz[1][2])

# ==============================
# CONVERTIR ENTRE LISTAS Y OTROS TIPOS
# ==============================
tupla = (10, 20, 30)
lista_desde_tupla = list(tupla)
print("\nTupla convertida a lista:", lista_desde_tupla)

cadena = "Python"
lista_desde_cadena = list(cadena)
print("Cadena convertida a lista:", lista_desde_cadena)

# ==============================
# USOS COMUNES DE LAS LISTAS
# ==============================
# 1. Almacenar colecciones de datos
nombres = ["Mica", "Nico", "Leo", "Sofi"]

# 2. Filtrar elementos
mayores_a_3 = [x for x in [1, 4, 6, 2] if x > 3]
print("\nFiltrar mayores a 3:", mayores_a_3)

# 3. Listas de listas para tablas o matrices
tabla = [
    ["Producto", "Precio"],
    ["Pan", 100],
    ["Leche", 200]
]
print("Tabla:", tabla)

# ==============================
# CONCLUSIÓN
# ==============================
# Las listas son uno de los tipos más versátiles en Python.
# Permiten almacenar datos, modificarlos, ordenarlos y filtrarlos fácilmente.
# Son ideales para trabajar con colecciones dinámicas.
