def alfabetizador(palabra):
    letras = []
    letra_sn_repetir = []

    for letra in palabra:
        letras.append(letra)

    for letra in letras:
        if letra not in letra_sn_repetir:
            letra_sn_repetir.append(letra)

    return sorted(letra_sn_repetir)


print(alfabetizador("Ferrocarril"))
