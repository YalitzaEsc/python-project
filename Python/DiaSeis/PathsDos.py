from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_pedrera.txt") #duplica la ruta de 'guia' pero llama a otro archivo de texto

print(base)
print(guia)
print(guia2)

print(guia.parent) #Regresa el antecesor al directorio actual de la ruta
print(guia.parent.parent)

print('\n')

guia3 = Path(Path.home(), "Desktop/Europa")

for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

'''en_europa = guia3.relative_to(Path("Europa"))
en_espania = guia3.relative_to(Path("España"))
print(en_europa)
print(en_espania)'''









