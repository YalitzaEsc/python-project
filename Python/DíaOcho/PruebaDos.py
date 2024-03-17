def multiplos():
    x = 0
    while True:
        x += 1 * 7
        yield x


generador = multiplos()
print(next(generador))
print(next(generador))
