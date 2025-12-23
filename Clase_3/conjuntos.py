# conjuntos.py
# ==============================
# CONJUNTOS EN PYTHON (set)
# ==============================
# Un conjunto es una colección desordenada de elementos únicos (sin duplicados).
# Se usa para operaciones matemáticas como unión, intersección o diferencia.

# Crear un conjunto
conjunto = {1, 2, 3, 4}
print("Conjunto inicial:", conjunto)

# También se puede crear con el constructor set()
conjunto2 = set([3, 4, 5, 6])
print("Conjunto creado con set():", conjunto2)

# Los conjuntos eliminan automáticamente duplicados
conjunto3 = {1, 2, 2, 3, 3, 4}
print("Conjunto sin duplicados:", conjunto3)

# ==============================
# MÉTODOS DE LOS CONJUNTOS
# ==============================

# 1. add() -> Agrega un elemento al conjunto
conjunto.add(5)
print("\nadd():", conjunto)

# 2. remove() -> Elimina un elemento. Lanza error si no existe
conjunto.remove(1)
print("remove():", conjunto)

# 3. discard() -> Elimina un elemento, pero NO lanza error si no existe
conjunto.discard(99)
print("discard():", conjunto)

# 4. pop() -> Elimina y devuelve un elemento aleatorio (porque no hay orden)
elemento = conjunto.pop()
print("pop(): se eliminó", elemento, "=>", conjunto)

# 5. clear() -> Elimina todos los elementos
temp = {10, 20, 30}
temp.clear()
print("clear():", temp)

# ==============================
# OPERACIONES ENTRE CONJUNTOS
# ==============================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 6. union() o "|" -> Une dos conjuntos sin duplicados
print("\nunion():", a.union(b))
print("Operador | :", a | b)

# 7. intersection() o "&" -> Devuelve los elementos comunes
print("intersection():", a.intersection(b))
print("Operador & :", a & b)

# 8. difference() o "-" -> Devuelve los elementos que están en 'a' pero no en 'b'
print("difference():", a.difference(b))
print("Operador - :", a - b)

# 9. symmetric_difference() o "^" -> Devuelve elementos que están en uno u otro, pero no en ambos
print("symmetric_difference():", a.symmetric_difference(b))
print("Operador ^ :", a ^ b)

# ==============================
# MÉTODOS RELACIONADOS CON SUBCONJUNTOS
# ==============================

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

# 10. issubset() -> True si todos los elementos de x están en y
print("\nissubset():", x.issubset(y))  # True

# 11. issuperset() -> True si y contiene todos los elementos de x
print("issuperset():", y.issuperset(x))  # True

# 12. isdisjoint() -> True si no tienen ningún elemento en común
print("isdisjoint():", x.isdisjoint({8, 9}))  # True

# ==============================
# COPIA DE CONJUNTOS
# ==============================

# 13. copy() -> Devuelve una copia del conjunto
original = {100, 200, 300}
copia = original.copy()
print("\ncopy():", copia)

# ==============================
# CONJUNTOS INMUTABLES (frozenset)
# ==============================
# Un frozenset es como un set, pero no se puede modificar (no admite add, remove, etc.)
frozen = frozenset([1, 2, 3, 3])
print("\nfrozenset:", frozen)

# Se pueden hacer operaciones entre conjuntos y frozensets
print("Unión entre set y frozenset:", {2, 3, 4}.union(frozen))

# ==============================
# CONCLUSIÓN
# ==============================
# Los conjuntos son ideales para:
# - Eliminar duplicados
# - Comparar colecciones
# - Realizar operaciones matemáticas (unión, intersección, diferencia)
