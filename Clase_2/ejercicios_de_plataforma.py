


listas = [1, "pepe", "hola",25]

print(listas[1])

tuplas = (1, "pepe", "hola",25)

print(listas[0])


conjuntos = {1,0,3,5,5,5,8,9}
print(conjuntos)


#ejercicio de datos

#1) qué tipo de datos son los siguientes?
a="Hola Mundo"	
b=[1, 10, 100]	
c=-25	
d=(8, 100, -12)	
e=1.167	
f=["Hola", "Mundo"]	
g=' '	
h=(1, -5, "Hola!")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))


#2) determinar mentalmente lo siguiente:

a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)

print("\n")
print(a * 5)	
print(a - b)	
print(c + "Mundo")	
print(c * 2)	
print(c[-1])	
print(c[1:])	
print(d + d)	
print(e[1])	
print(e+(7,8,9))


'''
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada 
fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

Partirás de:

matriz = [

[1, 5, 1],

[2, 1, 2],

[3, 0, 1],

[1, 4, 4]

]

Debes llegar a:

matriz = [

[1, 5, 1, 7],

[2, 1, 2, 5],

[3, 0, 1, 4],

[1, 4, 4, 9]

]

'''

matriz = [

[1, 5, 1],

[2, 1, 2],

[3, 0, 1],

[1, 4, 4]

]

print(matriz)



matriz_modificada = matriz[0].append(sum(matriz[0])) 
matriz_modificada = matriz[1].append(sum(matriz[1])) 
matriz_modificada = matriz[2].append(sum(matriz[2])) 
matriz_modificada = matriz[3].append(sum(matriz[3])) 
print(matriz)


# Práctica con conjuntos

paises = {"Inglaterra", "USA", "México"}
print(paises)

agregados = {"Islandia", "Italia", "Argentina y Portugal", "USA"}

paises_completos = paises.update(agregados)
print(paises)

eliminado1 = paises.remove("Italia")
print(paises)


"""

Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:

Ejemplo del output solicitado:

Juan tiene 25 años, y vive en Carrera 7 - Bogotá 
"""


nombre = input("poné tu nombre forr@: ")
edad = input("ahora tu edad put@: ")
dirección = input("no olvides tu dirección idiota: ")
print(nombre, " tiene ",edad, "años, y vive en ", dirección)


