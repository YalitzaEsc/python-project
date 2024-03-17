from random import *
from os import system
from colorama import Fore

palabras = ["Electricidad", "Escuela", "Videojuegos", "Estrella",
            "Computadora", "Perfume", "Flor", "Fuego",
            "Carreras", "Cantante", "Jardin", "Ingenieria"]

definiciones = ["Forma de energía que produce efectos luminosos, mecánicos, caloríficos, \n" \
                "químicos, etc., y que se debe a la separación o movimiento de los electrones " \
                "que forman los átomos.",
                "Institución destinada a la enseñanza, en especial la primaria, que proporciona conocimientos\n " \
                "que se consideran básicos en la alfabetización.",

                "Aplicación interactiva orientada al entretenimiento que, a través de ciertos mandos o controles,\n " \
                "permite simular experiencias en la pantalla de un televisor, una computadora u otro dispositivo electrónico.",

                "Cuerpo celeste de gran tamaño, constituido por plasma, con forma esférica, que brilla con luz propia.",

                "Máquina electrónica capaz de almacenar información y tratarla automáticamente mediante operaciones matemáticas\n " \
                "y lógicas controladas por programas informáticos.",

                "Producto, por lo general líquido, que utilizan hombres y mujeres sobre su cuerpo para desprender un olor agradable.",

                "Parte de la planta encargada de la reproducción.",

                "Conjunto de partículas o moléculas incandescentes de materia combustible, \n"
                "capaces de emitir calor y luz, producto de una reacción química de oxidación acelerada.",

                "Competición de velocidad, en la que los competidores tienen que completar un determinado trayecto o distancia empleando \n" \
                "para ello el menor tiempo posible, o bien recorrer el mayor trayecto posible en cierto tiempo fijo.",

                "Persona que se dedica profesionalmente a cantar.",

                "Terreno en el que se cultivan plantas y flores ornamentales para hacer de él un lugar agradable.",

                "Arte y técnica de aplicar los conocimientos científicos a la invención, diseño, perfeccionamiento y manejo de nuevos \n" \
                "procedimientos en la industria y otros campos de aplicación científicos."]


def elegir_palabra(lista):
    palabra = choice(lista).lower()
    return palabra


def definir_palabra(palabra):
    num_definicion = palabras.index(palabra.capitalize())
    definicion = definiciones[num_definicion]

    print(Fore.LIGHTWHITE_EX + f'La definición de la palabra que te ha tocado es la siguiente: \n\n"{definicion}"')



def separar_palabra(palabra):
    letras = []

    for letra in palabra:
        letras.append(letra)
    return letras


def descifrar(lista):
    letras_cifradas = []

    for letra in lista:
        letras_cifradas.append("–")
    return letras_cifradas


def preguntar(lista_letras, cifras):
    print(f"\nCuentas con 6 vidas para ganar. \nLas letras son: {cifras}")

    jugar = True
    vidas = 6
    letras_utilizadas = []

    while jugar:
        seleccion = input("\nElije una letra: ")
        system('clear')

        if seleccion not in letras_utilizadas:
            letras_utilizadas.append(seleccion)
        else:
            seleccion = input(f"Ya has elegido esa letra antes. Elije otra: ")

        if seleccion in lista_letras:

            lista_pos = []
            i = -1

            for letra in lista_letras:
                i += 1
                if seleccion == letra:
                    lista_pos.append(i)

                    for pos in lista_pos:
                        cifras[pos] = seleccion

            if '–' not in cifras:
                print(f"\n¡Felicidades, has adivinado! \nLa palabra es '{''.join(lista_letras)}'.")
                jugar = False
            else:
                print(f"¡Muy bien! Tu palabra es: {cifras}.")

        else:
            vidas -= 1
            print(f"La letra '{seleccion}' no se encuentra en la palabra.")

            if vidas > 1:
                print(f"Te restan {vidas} vidas.")
            elif vidas == 1:
                print(f"Te resta {vidas} vida.")
            elif vidas == 0:
                print("Te has quedado sin vidas. Inténtalo de nuevo")
                jugar = False


palabra_elegida = elegir_palabra(palabras)
definir_palabra(palabra_elegida)
letras = separar_palabra(palabra_elegida)
letras_des = descifrar(letras)
preguntar(letras, letras_des)
