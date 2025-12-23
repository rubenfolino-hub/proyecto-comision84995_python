

"""
En Tech Connect se va a realizar un torneo de fútbol interno de la compañía. Como
parte del equipo de desarrollo, te solicitan desarrollar un programa que permita calcular
el promedio final de los equipos de fútbol del torneo.
Para ello, debes considerar tres aspectos:
✓ Jugaron 20 partidos durante el torneo.
✓ Los partidos poseen diferente puntaje según el resultado:
○ Ganado: 3 puntos
○ Empatado: 1 punto
○ Perdido 0 puntos
✓ El promedio final resulta de la cantidad de puntos totales divididos la cantidad de
partidos.
Cada una de las cantidades de partidos ganados, empatados o perdidos debe
solicitarse al usuario utilizando la función input().
✓ partidos_ganados 8
✓ partido_empatados 7
✓ partido_perdidos 5

"""


#cantidad de partidos
p_jugados = 20
p_ganados = 8
p_empatados = 7
p_perdidos = 5

#puntaje de partidos
pto_ganado = 3
pto_empatado = 1
pto_perdido = 0

#cálculo de promedio final
print("promedio_final :", ((p_ganados * pto_ganado + p_empatados * pto_empatado + p_perdidos * pto_perdido)) / p_jugados)



#interacción con usuario

dato1 = input("partidos_ganados ")
print("partidos ganados: ",dato1)
dato2 = input("partidos_empatados ")
print("partidos empatados: ",dato2)
dato3 = input("partidos_perdidos ")
print("partidos perdidos: ",dato3)


#cálculo de promedio final con datos interactivos
print("promedio_final :", (int(dato1) * pto_ganado + int(dato2) * pto_empatado + int(dato3) * pto_perdido) / p_jugados)


