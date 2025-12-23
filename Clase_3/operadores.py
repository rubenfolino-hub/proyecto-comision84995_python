a = 5
b = 4

print(f"suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicaicon: {a * b}")
print(f"Division decimal: {a / b}")
print(f"Division entera: {a // b}")
print(f"Potencia: {a ** b}")
print(f"Modulo/Resto: {a % b}")

### OPERADORES LOGICOS True / False
true = True
false = False
# and // or
print(true and true) # True
print(true and false) # False
print(false and false) # False
print(true or true) # True
print(true or false) # True
print(false or false) # False
print(true and (true or false))


"""
expresiones = [
False == True,  False
10 >= 2*4, True
33/3 == 11, True
True > False, True // True = 1 False = 0
True*5 == 2.5*2, True
]

"""

"""
expresiones = [
not False, True
not 3 == 5, True
33/3 == 11 and 5 > 2, True
True or False, True
True*5 == 2.5*2 or 123 >= 23, True
12 > 7 and True < False, False
]

"""


"""
Consigna: Crear una variable que almacene si se cumplen todas las condiciones.
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable
que almacene si se cumplen todas las siguientes condiciones,
encadenando operadores lógicos en una sola línea:

NOMBRE sea diferente de cuatro asteriscos "****"
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35
Desde un input conseguir las variables:

"""

nombre = input("Ingrese un nombre: ")
edad = int(input("ingrese una edad: "))

nombre_dif_asteriscos = nombre != "****"
longitud_de_caracteres =  8 > len(nombre) >= 4
longitud_de_caracteres =  len(nombre) >= 4 and len(nombre) < 8
edad_entre_dos_numeros = edad > 5 and edad < 20
edad_entre_dos_numeros_2 = 20 > edad > 5
edad_multiplicada_por_tres_mayor_que = edad * 3 > 35

valor_final = nombre_dif_asteriscos and edad_entre_dos_numeros_2 and edad_multiplicada_por_tres_mayor_que and longitud_de_caracteres

print(f"El valor final con los datos ingresados es: {valor_final}")