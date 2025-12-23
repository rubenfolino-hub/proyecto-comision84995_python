"""
Explicación de cada sección:
Estructura de Menú: Cada opción en el menú de ejercicio_1 permite realizar una operación matemática específica entre dos números. Incluye validación de entrada para manejar errores.

Validación de Número Impar: ejercicio_2 solicita un número impar y repite el proceso hasta recibir un número correcto.

Suma de Impares: ejercicio_3 usa range para sumar números impares hasta 100 de manera eficiente.

Cálculo de Media: ejercicio_4 permite al usuario especificar cuántos números quiere sumar y calcula su media.

Validación en Lista: ejercicio_5 pide un número entre 0 y 9, verificando si pertenece a una lista del 0 al 9.

Generación de Listas Dinámicas: ejercicio_6 utiliza range y conversión a listas para crear diferentes listas según los parámetros solicitados."""




# 4.9 Actividad práctica

# ¡Instrucciones e iteración!
# Realiza los ejercicios 1, 2, 3, 4, 5 y 6. A continuación están detallados con ejemplos adicionales.
"""
Ejercicio 1:
Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
1. Mostrar una suma de los dos números
2. Mostrar una resta de los dos números (el primero menos el segundo)
3. Mostrar una multiplicación de los dos números
4. Salir del programa
"""
def ejercicio_1():
    menu = {
        "1": "Mostrar Suma",
        "2": "Mostrar restar",
        "3": "Mostrar multiplicacion",
        "4": "Salir del programa"
    }
    while True:
        for opcion, descripcion in menu.items():
            print(f"{opcion} - {descripcion}")
        opcion = input("Ingrese una opcion: ")
        if opcion in menu:
            if opcion == "4":
                print("Salgo del programa")
                break
            numero_1 = int(input("ingrese un numero entero: "))
            numero_2 = int(input("ingrese un numero entero: "))
            if opcion == "1":
                print(f"Suma: {numero_1 + numero_2}")
            elif opcion == "2":
                print(f"Resta: {numero_1 - numero_2}")
            else:
                print(f"Multiplicacion: {numero_1 * numero_2}")
        else:
            print("Opcion no valida")
# ejercicio_1()

# Ejercicio 2:
# Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

def ejercicio_2():
    pass
    
# Ejercicio 3:
# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100.

def ejercicio_3():
    pass

# Ejercicio 4:
# Escribe un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.

def ejercicio_4():
    pass

# Ejercicio 5:
# Escribe un programa que pida al usuario un número entero del 0 al 9.
# Mientras el número no sea correcto, se repite el proceso.
# Luego debe comprobar si el número está en una lista de números y notificarlo.

def ejercicio_5():
    pass

# Ejercicio 6:
# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
"""Todos los números del 0 al 10 [0, 1, 2, ..., 10]

Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto)) """
def ejercicio_6():
    pass
# Llamada a funciones de cada ejercicio para pruebas
# Puedes descomentar las siguientes líneas para ejecutar los ejercicios uno por uno

# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()



"""
Actividad: Crédito Bancario
Consigna:

Para aprobar un crédito, el cliente debe ser mayor de edad.
Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.
En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito

Datos iniciales

edad = 15
antigüedad = 10
ingreso = 1500
"""
mayor_de_edad = 18
antiguedad_minima = 3
ingresos_minimos = 2500
ingresos_minimos_sin_antiguedad = 4000
######################################
edad = 18
antiguedad = 2
ingreso = 4000
    
# Nico
# if edad >= mayor_de_edad:
#     if antiguedad >= antiguedad_minima and ingreso > ingresos_minimos:
#         print("Su credito ha sido aprobado")
#     elif ingreso >= ingresos_minimos_sin_antiguedad:
#         print("Su credito ha sido aprobado")
#     else:
#         print("No es apto credito por antiguedad o ingresos")
# else:
#     print("No es apto credito por edad")

# Clemente
# if edad >= 18:
#     print("Cliente es mayor de edad, revisando el resto:")
#     if antiguedad >= 3 and ingreso > 2500:
#         print("CRÉDITO APROBADO")
#     elif ingreso >= 4000:
#         print("CRÉDITO APROBADO")
#     else:
#         print("CRÉDITO RECHAZADO x Antiguedad o ingresos")
# else:
#     print("Rechazado: Cliente es menor de edad")

# # Mati
# if edad >= 18:
#     if antiguedad >= 3:
#         if ingreso > 2500:
#             print("Crédito aprobado")
#         else:
#             print("Crédito no aprobado")
#     else:
#         if ingreso >= 4000:
#             print("Crédito aprobado")
#         else:
#             print("Crédito no aprobado")

# # Tomas
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     antiguedad = int(input("Ingrese su antiguedad: "))
#     if antiguedad>=3:
#         ingreso = int(input("Ingrese sus ingresos: "))
#         if ingreso>2500:
#             print("Usted aprueba para el credito")
#         else:
#             print("Usted no aprueba para el credito")
#     else:
#         ingreso = int(input("Ingrese sus ingresos: "))
#         if ingreso >= 4000:
#             print("Usted aprueba para el credito")
#         else:
#             print("Usted no aproba para el credito")
# else:
#     print("Usted no aplica para el credito")
# edad = 15
# antiguedad = 10
# ingreso = 1500
# if edad > 18:
#     if antiguedad >= 3 and ingreso > 2500:
#         print("ok")
#     else:
#         if ingreso >= 4000:
#             print("ok")
#         else:
#             print("poco ingreso")
# else:
#     print("sos menor")
# edad=int(input("Ingrese su edad: "))
# antiguedad=int(input("Ingrese su antiguedad financiera"))
# ingreso=int(input("Ingrese sus ingresos: "))
# if edad >= 18:      
#     if antiguedad>=3 and ingreso>=2500:
#         print("Credito aprobado")
#     elif antiguedad<3 and ingreso>4000:
#         print("Credito aprobado")
#     else:
#          print("Credito rechazado")
# else:
#     print("Credito rechazado")
    
"""
Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input ().

Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa debe validar dicha acción.

Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.

Duración: 10/15 minutos.

"""


numero = int(input("Ingresar un numero: "))
numero_2 = int(input("Ingresar un segundo numero: "))
resultado = 0

while True:
    opcion = input("Por favor ingrese la opcion correspondiente a la operacion a realizar: 1 = Suma,  2 = Resta, 3 = Multiplicacion, 4 = Salir del programa: ")
    
    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        break
    else: 
       print("Por favor ingrese una opcion valida.")
       
if opcion == "1":
    resultado = numero + numero_2
    print(resultado)
elif opcion == "2":
    resultado = numero - numero_2
    print(resultado)
elif opcion == "3":
    resultado = numero * numero_2
    print(resultado)
elif opcion == "4":
    print("Fin del programa")