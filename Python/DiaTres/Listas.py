mi_lista = ["A", "B", "C"]
otra_lista = ["Hola", 24, 78.9]

print(type(mi_lista))
print(len(mi_lista))
print(otra_lista[0])
print(mi_lista[1:])
print(otra_lista[0:2])

print(mi_lista + otra_lista)

lista_tres = mi_lista + otra_lista
print(lista_tres)

lista_tres[0] = 45
print(lista_tres)

lista_tres.append("H")
print(lista_tres)

lista_tres.pop()
print(lista_tres)

lista_tres.pop(1)
print(lista_tres)

eliminado = lista_tres.pop(0)
print(lista_tres)
print(eliminado)


lista_alfab = ["g", "r", "a", "s", "c", "d", "e"]
lista_alfab.sort()
print(lista_alfab)


lista_alfab.reverse()
print(lista_alfab)

