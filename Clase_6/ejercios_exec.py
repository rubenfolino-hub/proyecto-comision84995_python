"""
Consigna:

En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y retorna el valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal de la función.

>>> def dividir(a, b):

return a/b

Pista: Valor indeterminado

"""

def dividir(a, b): # Fallo potencial, en matematicas b = 0
    if b == 0:
        return None
    return a / b

def dividir_excep(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None

def dividir_excep(a, b):
    try:
        a=int(input("Ingresa un numero: "))
        b=int(input("ingresa otro numero: "))
    except Exception:
        print(None)
    finally:
        return a/b

print(dividir_excep(10, 5))
print(dividir_excep(0, 5))
print(dividir_excep(10, 0))
print(dividir(10, 5))
print(dividir(0, 5))
print(dividir(10, 0))

def main():
    ...
    # division_1 = dividir_excep(10, 5)
    # division_2 = dividir_excep(0, 5)
    # division_3 = dividir_excep(10, 0)
    # if division_1 is None or division_2 is None or division_3 is None:
    #     print("Ocurrio un error en el proceso de dividir numeros")
    # pass
