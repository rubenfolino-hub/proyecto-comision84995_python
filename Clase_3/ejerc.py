"""
A partir de una lista realizar las siguientes tareas sin modificar la lista original:

- Borrar los elementos duplicados
- Ordenar la lista de mayor a menor
- Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )
- Realizar una suma de todos los números que quedan (sum(lista))
- Añadir como primer elemento de la lista la suma realizada insert(0, suma)
- Finalmente, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
"""

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

lista_1 = lista # Esto esta MAL X
lista_copia = lista.copy()
lista_copia_1 = lista[:]

lista_copia = list(set(lista_copia)) # {5, 12, 16, 17, -12, 23, 24, -5, 29}
print(lista_copia)

lista_copia.sort(reverse=True)
# lista_copia.sort()[::-1]
# lista_copia.reverse()
print(lista_copia)

for numero in lista_copia[:]: # [inicio:fin] 0 : len(lista_copia) - 1
    if numero % 2 == 1:
        lista_copia.remove(numero)

# print(lista_copia)
###########################
lista_sin_impares = [n for n in lista_copia if n % 2 == 0] # []
lista_nueva = []
for n in lista_copia:
    if n % 2 == 1:
        lista_nueva.append(n)
print(lista_sin_impares)
###########################

print(sum(lista_copia))

suma = sum(lista_copia)
lista_copia.insert(0, suma)

print(lista_copia)

############################
# [40, 24, 16, 12, -12]
############################
primer_numero = lista_copia[0]
suma = sum(lista_copia[1:])

print(f"El Primer numero es: {primer_numero} y la suma a partir del segundo {suma}. Es igual? {primer_numero==suma}")
