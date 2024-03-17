#Modo sólo lectura, puede también omitirse la 'r'
mi_archivo = open('prueba.txt', 'r')

#Se resetea el archivo si ya existe, si no, lo crea
mi_archivo = open('prueba.txt', 'w')

#Si no existe el archivo, lo crea, si ya existe, empieza a escribir desde el final
mi_archivo = open('prueba.txt', 'a')

mi_archivo.close()

#Las ''' son para crear saltos de línea
archivo = open('prueba1.txt', 'w')
archivo.write('''Hola.
¿cómo estás?''')
#Para escribir una lista de strings, sin espacios entre cada elemento y en la misma línea:
archivo.writelines(['hola', 'mundo', 'cómo', 'estás'])

archivo.close()

archivo_dos = open('prueba2.txt', 'w')
lista = ['Hola', 'mi', 'nombre', 'es', 'Claudia']

for palabra in lista:
    archivo_dos.writelines(palabra + " ")

archivo_dos.close()

archivo_dos = open('prueba2.txt')
print(archivo_dos.read())

