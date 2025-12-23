

"""

Partirás de
matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
list(list(int()))


Debes llegar a
matriz = [
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]

"""


matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz[0].append(7)
matriz[1].append(5)
matriz[2].append(4)
matriz[3].append(9)
print(matriz)



numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros)