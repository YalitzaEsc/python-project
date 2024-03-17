def suma(num1, num2, num3, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    print(f"El tercer valor es {num3}")

    for arg in args:
        print(f"arg = {arg}")

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        total += valor

    return f"El total es igual a {total}."


print(suma(4, 5, 10, 90, 50, x = 5, y = 10, z = 9))
