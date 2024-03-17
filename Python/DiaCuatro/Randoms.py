from random import *

#Número entero
aleatorio = randint(1, 50)
print(aleatorio)

#Número fraccional, con una decimal, entre el 1 y el 20
aleatorio_dos = round(uniform(1,20), 1)
print(aleatorio_dos)

#Literalmente cualquier número, positivo, entero, negativo, fraccional
aleatorio_tres = random()
print(aleatorio_tres)

#Elige un elemento al azar de una lista
colores = ["azul", "verde", "amarillo", "rojo"]
color_aleatorio = choice(colores)
print(color_aleatorio)

#Crea una lista de número entre el 5 y el 50 con saltos de 5 en 5
numeros = list(range(5, 50, 5))
#Revuelve los elementos de la lista de forma aleatoria
shuffle(numeros)
print(numeros)










