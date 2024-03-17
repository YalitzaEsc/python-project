for numero in range(5):
    print(numero)

for numero in range(5+1):
    print(numero)

for numero in range(20, 31):
    print(numero)

for numero in range(10, 20, 2):
    print(numero)

lista = list(range(1, 1001))
print(lista)

suma_cuadrados = 0
for numero in range(1, 16):
    numero **= 2;
    suma_cuadrados += numero

    print(suma_cuadrados)
