

#ejercicio de slicing


#nombre y apellido con un tema de la unidad 2 (en teoria no sirve como solución)
cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]
print(cadena_volteada)

division = cadena_volteada.split()
conjunto_para_nombre_completo = set(division)

nombre_completo = division[0:2]
print(nombre_completo)


#nombre y apellido con operaciones de la unidad 1
cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]
print(cadena_volteada)
cadena_volteada_sin_comas = cadena_volteada.replace(",","")

division = cadena_volteada_sin_comas.split()
nombre = division[0]
apellido = division[1]
nombre_y_apellido = nombre + " " + apellido
print(nombre_y_apellido)

nota = division[2]
print(nota)

materia = division[3]
print(materia)

#NOMBRE APELLIDO ha sacado un NOTA en MATERIA

completo = nombre_y_apellido + " ha sacado un " + nota + " en " + materia
print(completo)
