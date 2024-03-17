lista_letras = ['a', 'b', 'c', 'a', 'a']

seleccion = 'a'
lista_pos = []
i = -1

for letra in lista_letras:
    i += 1
    if seleccion == letra:
        lista_pos.append(i)

print(lista_pos)


