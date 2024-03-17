mi_archivo = open('prueba1.txt', encoding='cp1252', errors = 'surrogateescape')


una_linea = mi_archivo.readline()
print(una_linea.upper())

#rstrio() es para quitar el salto de línea
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)


for linea in mi_archivo:
    print("Aquí dice: " + linea)

mi_archivo.close()




