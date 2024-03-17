# *args

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total


print(suma(4, 5, 6, 9))


def suma_dos(*args):
    return sum(args)


print(suma_dos(1, 5, 4, 0))
