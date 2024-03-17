texto = input("Ingrese un texto de su elección: ").lower()
palabras = texto.split()

letra1 = input("Ingrese una letra: ").lower()
letra2 = input("Ingrese una segunda letra: ").lower()
letra3 = input("Ingrese una tercera letra: ").lower()

print(f"\nLa letra '{letra1}' aparece {texto.count(letra1)} veces.")
print(f"La letra '{letra2}' aparece {texto.count(letra2)} veces.")
print(f"La letra '{letra3}' aparece {texto.count(letra3)} veces.")

print(f"\nLa longitud de su texto es de {len(palabras)} palabras y {len(texto)} caracteres.")
print(f"La primera letra de su texto es la {texto[0]}.")
print(f"La última letra de su texto es la {texto[-1]}.")

palabras.reverse()
texto_invertido = " ".join(palabras)
print("\nSu texto quedaría de la siguiente manera al ser invertido: " + texto_invertido)

verd_falso = "python" in texto
diccionario = {True: "Sí.", False: "No."}
print(f"¿La palabra 'Python' aparece en su texto? {diccionario[verd_falso]}")


