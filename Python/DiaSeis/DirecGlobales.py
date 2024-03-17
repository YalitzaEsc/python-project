from pathlib import Path

carpeta = Path('/Users/claudiainzunza/Desktop/Textos txt') / 'otro_archivo.txt'


mi_archivo = open(carpeta)
print(mi_archivo.read())
