def verificador(*args):
    lista = []
    i = 0

    for arg in args:
        lista.append(arg)

    for numero in lista:
        if numero == 0:
            i += 1
            if i >= 2:
                r = True
            else:
                r = False
        else:
            pass

    return r


print(verificador(1, 2, 4, 5, 6, 0))
