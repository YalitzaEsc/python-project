from random import *

# Lista inicial con los palitos
palitos = ['-', '--', '---', '----']


# Lista que mezcle los palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle al usuario que elija un número
def preguntar():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)


# verificar el resultado
def verificar_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("Ya que has elegido el palito más corto, has perdido.")
    else:
        print("Te has salvado.")


palitos_mezclados = mezclar(palitos)
palito_elegido = preguntar()
verificar_intento(palitos_mezclados, palito_elegido)

