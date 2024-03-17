import os

#Para obtener la ruta actual con la que estamos trabajando
ruta = os.getcwd()
print(ruta)

#Para cambiar la ruta con la que estamos trabajando y acceder o crear un archivo
os.chdir('//Users//claudiainzunza//Desktop//Textos txt')

archivo = open('otro_archivo.txt', 'w')
archivo.write("Esta es una nueva prueba para crear una archivo desde cero.")
archivo.close()

archivo = open('otro_archivo.txt')
print(archivo.read())
archivo.close()

#Para crear carpetas nuevas
'''os.makedirs('//Users//claudiainzunza//Desktop//Textos txt//Otra')'''
#Para borrar carpetas (se elimina la última carpeta de la ruta)
'''os.rmdir('//Users//claudiainzunza//Desktop//Textos txt//Otra')'''

ruta = '//Users//claudiainzunza//Desktop//Textos txt//otro_archivo.txt'
#Nos da el nombre del archivo al que estamos accediendo
nombre_archivo = os.path.basename(ruta)
print(nombre_archivo)

#Nos da la ruta del directorio
nombre_dir = os.path.dirname(ruta)
print(nombre_dir)

#Nos da tanto la ruta como el nombre del archivo en una tupla
nombre = os.path.split(ruta)
print(nombre)

otro_archivo = open('//Users//claudiainzunza//Desktop//Textos txt//otro_archivo.txt')
print(otro_archivo.read())
otro_archivo.close()






