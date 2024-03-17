if 25 > 45:
    print("Es incorrecto")
else:
    print("Es correcto")


edad = 16
calificacion = 7

if edad < 18:
    print("Eres menor de edad.")
    if calificacion >= 8:
        print("Estás aprobado.")
    else:
        print("No estás aprobado.")
else:
    print("Eres adulto.")



num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")

elif num2 > num1:
    print(f"{num2} es mayor que {num1}")

else:
    print(f"{num1} y {num2} son iguales")


