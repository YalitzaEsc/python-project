def contar_primos(numero):

    cant_primos = 0
    lista_primos = []

    if numero < 2:
        return "0"

#salto de 2 en 2 porque los números pares no son primos
    for num in range(2, numero, 2):
        if numero % num == 0:
            pass
        else:
            lista_primos.append(num)
            cant_primos += 1

    print(f"La cantidad de números primos que hay desde 0 hasta {numero} es {cant_primos}. "
                 f"Y son los siguientes: \n{lista_primos}")


contar_primos(0)
