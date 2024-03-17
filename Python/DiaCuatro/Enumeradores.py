lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)


for indice, item in enumerate(lista):
    print(indice, item)

for indice, item in enumerate(range(50, 55)):
    print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples[1])
