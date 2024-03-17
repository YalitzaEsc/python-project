nombres = ["Juan", "Claudia", "Yalitza", "Carlos", "Liah"]
nombres_letraC = []

for nombre in nombres:
    if nombre.startswith("C"):
        nombres_letraC.append(nombre)

print(f"Los nombres que empiezan con la letra 'C' son: \n")
for nombre in nombres_letraC:
    print(nombre)


letras = ['A', 'B', 'C', 'D']
print("\n")

for letra in letras:
    print(f"La letra número {letras.index(letra) + 1}  es la '{letra}'.")


numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


frase = "Python es genial."

for letra in frase:
    print(letra)

for letra in "Python":
    print(letra)

for numero in (1, 2, 3):
    print(numero)

for elemento in [[1,2], [3, 4], [5, 6]]:
    print(elemento)

for a, b in [[1,2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {"Clave1": "a", "Clave2": "b", "Clave3": "c"}

for item in dic.items():
    print(item)

for value in dic.values():
    print(value)

for a, b in dic.items():
    print(a, b)

