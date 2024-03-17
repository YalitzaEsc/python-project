nombre = input("¿Cuál es tu nombre? ")
ventas = input("¿Cuál fue el monto de ventas que lograste el último mes? ")

print(f"Hola, {nombre}. El total de comisiones que te corresponde este mes, según tus ventas, es de {round(int(ventas)*100/13, 2)} pesos.")
