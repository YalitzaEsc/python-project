texto = "Éste es mi texto"

resultado = texto.upper()
print(resultado)

resultado_dos = texto.split()
print(resultado_dos)
print(type(resultado_dos))

resultado_tres = texto.split("t")
print(resultado_tres)

resultado_cuatro = texto.capitalize()
print(resultado_cuatro)

resultado_cinco = texto.lower()
print(resultado_cinco)


a = "Aprender"
b = "Python"
c = "es"
d = "aburrido"
e = " ".join([a, b, c, d])

print("\n")
print(e)
print(type(e))

resultado_seis = texto.find("s")
print("\n")
print(resultado_seis)

resultado_siete = texto.replace("mi", "su")
print("\n")
print(resultado_siete)
