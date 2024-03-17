from os import system


def turno_perfumeria():
    x = 0

    while True:
        x += 1
        yield "P" + str(x)


def turno_farmacia():
    x = 0

    while True:
        x += 1
        yield "F" + str(x)


def turno_cosmetica():
    x = 0

    while True:
        x += 1
        yield "C" + str(x)


def decorador(area):
    system('clear')
    print("Su turno es el:")

    if area == 1:
        print(next(cosmetica))
    elif area == 2:
        print(next(farmacia))
    else:
        print(next(perfumeria))

    print("Por favor espere y será atendido.")


cosmetica = turno_cosmetica()
farmacia = turno_farmacia()
perfumeria = turno_perfumeria()

