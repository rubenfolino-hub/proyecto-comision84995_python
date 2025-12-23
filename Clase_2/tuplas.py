##############################################
#            Tuplas en Python – Básico       #
##############################################

# ¿Qué es una tupla?
# Una tupla es como una lista, pero INMUTABLE.
# Eso significa que no se puede modificar después de ser creada.

numeros = (1, 2, 3, 4, 2, 2)
tupla = tuple()
tupla_vacia = ()
tupla_un_elemento = (1,)

print(numeros[0])
print(numeros[-1])

# Slices (funcionan igual que en listas)
print(numeros[1:3])   # (2, 3)
print(numeros[:2])    # (1, 2)
print(numeros[::-1])  # (4, 3, 2, 1)

print(len(numeros))

print(1 in numeros)
print("gola" in numeros)

print(numeros.count(2))
print(numeros.index(3))

lista = [1, 2, 3]

tupla = tuple(lista)
nueva_lista = list(tupla)

print(tupla, nueva_lista)

# Porque usar tuplas?

# - Porque son mas rapidas que las listas
# - Son seguras: no se pueden modificar por accidente (ej)
# - Y se usan cuando se quieren proteger datos.