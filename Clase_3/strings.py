# strings.py
# ==============================
# STRINGS EN PYTHON
# ==============================
# Un string (cadena) es una secuencia inmutable de caracteres.
# Se usan para representar texto.

# ==============================
# CREACIÓN DE STRINGS
# ==============================
texto1 = "Hola mundo"
texto2 = 'Python es genial'
texto3 = """Este es un texto
que ocupa varias líneas""" # Doc-strings
print("Texto 1:", texto1)
print("Texto 2:", texto2)
print("Texto 3:", texto3)

# ==============================
# ACCESO A CARACTERES Y SLICES
# ==============================
palabra = "Python"
print("\nPrimer carácter:", palabra[0])
print("Último carácter:", palabra[-1])
print("Slice [1:4]:", palabra[1:4]) # yth
print("Cada dos letras:", palabra[::2]) # Phn
print("Invertido:", palabra[::-1])

# ==============================
# CONCATENACIÓN Y REPETICIÓN
# ==============================
saludo = "Hola" + " " + "Nico"
print("\nConcatenado:", saludo) # Hola Nico

repetido = "Hi! " * 3
print("Repetido:", repetido) # Hi! Hi! Hi! 

# ==============================
# LONGITUD Y VERIFICACIÓN
# ==============================
print("\nlen('Python'):", len(palabra)) # 6
print("'Py' in palabra?:", "Py" in palabra) # True / Verdadero
# palabra = "Python"
print("'java' not in palabra?:", "java" not in palabra) # True

# ==============================
# MÉTODOS DE STRINGS
# ==============================
frase = "  hola mundo en Python  "

# 1. upper() -> Convierte a mayúsculas
print("\nupper():", frase.upper()) # "  HOLA MUNDO EN PYTHON  "

# 2. lower() -> Convierte a minúsculas
print("lower():", frase.lower()) # "  hola mundo en python  "

# 3. capitalize() -> Primera letra mayúscula
print("capitalize():", frase.capitalize()) # "Hola mundo en python"

# 4. title() -> Primera letra de cada palabra mayúscula
print("title():", frase.title())

# 5. strip() -> Elimina espacios al inicio y final
print("strip():", frase.strip()) # hola mundoo en Python

# 6. lstrip() / rstrip() -> Elimina espacios solo a la izquierda o derecha
print("lstrip():", frase.lstrip())
print("rstrip():", frase.rstrip())

# 7. replace() -> Reemplaza texto
print("replace('mundo', 'Coder'):", frase.replace("mundo", "Coder"))

# 8. split() -> Divide el string en una lista
print("split():", frase.split())

# 9. split(',') -> Divide por otro separador
datos = "Python,Java,C++"
print("split(','):", datos.split(","))

# 10. join() -> Une una lista en un string
lenguajes = ["Python", "Java", "C++"]
print("join():", " | ".join(lenguajes))

# 11. find() -> Devuelve el índice de la primera aparición
print("find('Python'):", frase.find("Python"))

# 12. count() -> Cuenta cuántas veces aparece un substring
print("count('o'):", frase.count("o"))

# 13. startswith() / endswith()
print("startswith('hola'):", frase.strip().startswith("h")) # True
print("endswith('Python'):", frase.strip().endswith("Pythonn")) # False

# 14. isalpha(), isdigit(), isalnum(), isspace()
cadena1 = "Hola"
cadena2 = "123"
cadena3 = "Hola123"
cadena4 = "   "

print("\nisalpha():", cadena1.isalpha())
print("isdigit():", cadena2.isdigit())
print("isalnum():", cadena3.isalnum())
print("isspace():", cadena4.isspace())

# 15. center() -> Centra el texto
print("\ncenter(20, '*'):", palabra.center(20, "*"))

# ==============================
# FORMATEO DE STRINGS
# ==============================

# f-strings (recomendado)
nombre = "Mica"
edad = 25

# format()
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))
print("Mi nombre es {n} y tengo {e} años.".format(e=edad, n=nombre))

# % formatting (antigua)
print("Tengo %d años y me llamo %s" % (edad, nombre))

# ---------------------------------------
#  F-STRINGS (Formateo moderno)
# ---------------------------------------
print("14. F-Strings:")
numero = 4
print(f" hola {{ {numero} }}")

print(f"Hola, me llamo {nombre} y tengo {edad} años")

# Podemos hacer operaciones dentro del f-string
print(f"El año que viene tendré {edad + 1} años")

# También se puede aplicar formateo a números
precio = 1234.56789
print("\n15. F-strings con formateo numérico:")

# Limitar decimales (2 después de la coma)
print(f"Precio con 2 decimales: {precio:.2f}")  # 1234.57

# Mostrar separador de miles
print(f"Precio con separador de miles: {precio:,.2f}")  # 1,234.57

# Mostrar porcentaje
porcentaje = 0.25678
print(f"Porcentaje: {porcentaje:.2%}")  # 25.68%

# Alinear texto
print("\n16. Alineación:")
print(f"{'Izquierda':<15} | {'Centro':^15} | {'Derecha':>15}")

# ---------------------------------------
#  MULTILÍNEAS
# ---------------------------------------
print("\n17. Strings multilínea:")
texto_largo = """Este es un texto
que ocupa
varias líneas."""
print(texto_largo)


# ==============================
# STRING MULTILÍNEA Y ESCAPE
# ==============================
texto = "Línea 1\nLínea 2\nLínea 3"
print("\nTexto con salto de línea:\n", texto)

# Escapar comillas
frase = "Ella dijo: \"Hola\""
frase1 = 'Ella dijo: "Hola"'
print("Con comillas escapadas:", frase)
print("Con comillas escapadas:", frase1)
# ==============================
# ITERAR SOBRE UN STRING
# ==============================
print("\nRecorrer string con for:")
for letra in "Hola":
    print(letra)

# ==============================
# FUNCIONES ÚTILES CON STRINGS
# ==============================
texto = "python"
print("\nlen(texto):", len(texto))
print("sorted(texto):", sorted(texto))  # Devuelve lista de letras ordenadas
print("max(texto):", max(texto))        # Letra mayor (según Unicode)
print("min(texto):", min(texto))        # Letra menor (según Unicode)

# ==============================
# EJEMPLOS PRÁCTICOS
# ==============================

# Contar vocales en una palabra
palabra = "programacion"
vocales = "aeiou"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print("\nCantidad de vocales:", contador)

# Verificar si una palabra es palíndromo
palabra = "neuquen"
es_palindromo = palabra == palabra[::-1] # neuquen
print("¿'neuquen' es palíndromo?:", es_palindromo)

# ==============================
# CONCLUSIÓN
# ==============================
# Los strings son inmutables y se usan constantemente en Python.
# Sus métodos permiten limpiar, formatear, buscar y transformar texto fácilmente.
# Son fundamentales para manejo de datos, entrada de usuario y salida en pantalla.
