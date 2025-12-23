

#contador = 1

#while contador == 1 :
#    print (contador)


# CONTROL + C para parar el bucle INFINITO


contador = 1

while contador <= 5 :
    print (contador)
    contador += 1


frutas = ["manzana", "plátano", "cereza"]
for fruta in frutas:
    print(fruta)

frutas = ["\nmanzana", "plátano", "cereza"]
for caleta in frutas:
    print(caleta)


for letra in "Python":
    print(letra)

print('\n')

for i in range(5):
    print(i)

print('\n')

numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] *= 2
print(numeros)

print('\n')

numeros2 = (numeros * 2)
print(numeros2)



print('\n')
# Para ver la diferencia de usar "F" en el print

frutas = ["manzana", "plátano", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")


print('\n')


frutas = ["manzana", "plátano", "cereza"]
for indice, fruta in enumerate(frutas):
    print("Índice: {indice}, Fruta: {fruta}")