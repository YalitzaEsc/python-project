nombres = ["Claudia", "Yalitza", "Liah", "Victoria"]
edades = [65, 29, 43]
ciudades = ["Madrid", "CDMX", "Lima"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

nombres = ["Claudia", "Yalitza", "Liah", "Victoria"]
edades = [65, 29, 43, 76]

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
