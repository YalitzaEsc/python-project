def chequear_tres_cifras(listaprueba):
    lista_tres_cifras = []

    for n in listaprueba:
        if n in range(100, 1000):
            lista_tres_cifras.append(n)
        else:
            pass

    return lista_tres_cifras


resultado = chequear_tres_cifras([90, 600, 2000])
print(resultado)


def todos_positivos(lista_numeros):
    booleano = True

    for n in lista_numeros:
        if n <= 0:
            booleano = False

    return booleano


resultado_dos = todos_positivos([10, 20, 20, 70])
print(resultado_dos)
