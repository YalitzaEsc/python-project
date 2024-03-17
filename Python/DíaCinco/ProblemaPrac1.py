def devolver_distintos(num_uno, num_dos, num_tres):
    suma = num_uno + num_dos + num_tres
    lista_num = [num_uno, num_dos, num_tres]

    num_mayor = 0
    num_menor = 16
    resultado = 0

    if suma > 15:
        for num in lista_num:
            if num > num_mayor:
                resultado = num

    elif suma < 10:
        for num in lista_num:
            if num < num_menor:
                resultado = num

    else:
        lista_num.sort()
        resultado = lista_num[1]

    return resultado


print(devolver_distintos(5, 2, 1))
