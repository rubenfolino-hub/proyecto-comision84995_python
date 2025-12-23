##############################################
#          Listas en Python – Nivel Inicial  #
##############################################

# ¿Qué es una lista?
# Una lista es una estructura que guarda varios elementos juntos, en orden.



lista = []
lista_1 = list()
lista_str = ["manzana", "uva", "silla", "mesa"]
#               0        1        2       3      ....
#print(lista_str[1], lista_str[0], lista_str[3])
lista_2 = lista_str[0:2] # ["manzana", "uva"]
lista_3 = lista_str # Esto va a modificar lista_str
# print(lista_str)
# print(lista_2 + ["naranja"])
print(lista_str[::-1]) # esto devuelve el ultimo elemento
print(lista_str[-1]) # Estoy accediendo al indice, por lo tanto me devuelve el elemento que este en este indice.
print("Hola que tal"[::-1])
lista_copia = lista_str[:] # Esto NO VA a modificar la lista_str
print(lista_copia, "----", lista_str)

lista_str.append("PC")
lista_str.append("monitor") # Agrega un elemento en la ultima posicion de la lista
lista_str.insert(0, "teclado") # Agrega un elemento en el indice indicado (indice, elemento)
print(lista_str)
dato_1 = lista_str.remove("teclado") # Elimina el elemento cuando lo encuentra, si hay repetidos eleimina el que esta mas a la izq
dato = lista_str.pop() # Elimina el ultimo elemento y lo DEVUELVE
dato_2 = lista_str.pop(1) # Elimino por indice

# lista_str = ["manzana", "uva", "silla", "mesa"]
# lista_str[0] = "tabla"  Reemplazo el elemento en el indice.
# print(lista_str)

print(len(lista_str)) # Devuelve el largo de la lista
lista_int = [4, 5, 7, 1, 10, 1]
print(sum(lista_int)) # Suma todos los elementos de una lista

print(f"Sorted: {sorted(lista_int)[::-1]}")
print(f"Sorted: {sorted(lista_str)}")
lista_str.sort()
print(lista_str)
lista_str.reverse() # lista_str[::-1]
print(lista_str)

print(lista_int.count(1)) # Devuelve la cantidad de veces que aparece en la lista
print(lista_int.index(7)) # Devuelve el indice del elemento en la lista

lista_elementos = [1, "hola", None, True, [], 4.5] # Bool = False, True
print(lista_elementos)

"""
Partirás de:

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
list(list(int()))
Debes llegar a:

matriz = [
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]

"""
matriz = [ [5, 8, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]
matriz[0].append(7)
matriz[1].append(5)
matriz[2].append(4)
matriz[3].append(9)
print(matriz)
# matriz = [
#     [1, 5, 1], # indice 0
#     [2, 1, 2], # indice 1
#     [3, 0, 1], # indice 2
#     [1, 4, 4] # indice 3
# ]

# matriz[0].append(sum(matriz[0]))
# matriz[1].append(sum(matriz[1]))
# matriz[2].append(sum(matriz[2]))
# matriz[3].append(sum(matriz[3]))
# print(matriz)

########

# matriz = [[1, 5, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]
# lista_1 = matriz[0]
# suma_1 = sum(lista_1)
# lista_1.append(suma_1)
# lista_2 = matriz[1]
# suma_2 = sum(lista_2)
# lista_2.append(suma_2)
# lista_3 = matriz[2]
# suma_3 = sum(lista_3)
# lista_3.append(suma_3)
# lista_4 = matriz[3]
# suma_4 = sum(lista_4)
# lista_4.append(suma_4)
# print(matriz)

#################

# matriz = [
# [1, 5, 1],
# [2, 1, 2],
# [3, 0, 1],
# [1, 4, 4]
# ]
# matriz[0].append(sum(matriz[0])) 
# matriz[1].append(sum(matriz[1])) 
# matriz[2].append(sum(matriz[2])) 
# matriz[3].append(sum(matriz[3])) 
# print('\t su matriz es', matriz)