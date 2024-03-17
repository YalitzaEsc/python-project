from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/claudiainzunza/Desktop/Textos txt/otro_archivo.txt')
ruta_windows = PureWindowsPath(carpeta) #Regresa la ruta en versión de windows

print(carpeta.stem) #Nombre del archivo sin extensión
print(carpeta.name) #Nombre del archivo
print(carpeta.suffix) #Extensión del archivo
print(carpeta.read_text()) #Leer el archivo

if not carpeta.exists():
    print("Este archivo sí existe.")
else:
    print("Genial, sí existe.")


