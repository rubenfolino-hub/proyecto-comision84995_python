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
ejercicio_1()

 