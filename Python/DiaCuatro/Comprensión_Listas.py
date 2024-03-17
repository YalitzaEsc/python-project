palabra = "Python"

lista = [letra for letra in palabra]
print(lista)


lista_dos = [letra for letra in "Hola"]
print(lista_dos)

lista_tres = [n if n * 2 >= 10 else "no" for n in range(0, 21, 2)]
print(lista_tres)

pies = [10, 50, 40, 30]
metros = [p * 3.281 for p in pies]
print(metros)


