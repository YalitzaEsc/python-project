def mi_generador_uno():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g_uno = mi_generador_uno()
print(next(g_uno))
print(next(g_uno))
print('Hola')
print(next(g_uno))


def mi_generador():
    for n in range(1, 5):
        yield n * 10


g = mi_generador()
print(next(g))
print(next(g))


def secuencia():
    x = 0
    while True:
        x += 1

    yield x


generador = secuencia()
print(next(generador))
print(next(generador))


