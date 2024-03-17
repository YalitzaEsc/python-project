monedas = 5

while monedas > 0:
    if monedas > 1:
        print(f"Tienes un total de {monedas} monedas.")
    else:
        print(f"Sólo te queda una {monedas} moneda.")
    monedas -= 1
else:
    print("No tienes más monedas.")


respuesta = "s"
while respuesta == "s":
    respuesta = input("¿Quieres continuar? (s/n)")
else:
    print("De acuerdo.")


nombre = input("Ingresa tu nombre: ")

for letra in nombre:
    if letra == "a":
        break
    print(letra)

for letra in nombre:
    if letra == "d":
        continue
    print(letra)

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)


numero = 20
while numero >= 0:
    print(numero)
    numero -= 1

numero_dos = 50

while numero_dos >= 0:
    if numero_dos % 5 == 0:
        print(numero_dos)
    numero_dos -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

