from random import *
from typing import Type

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}. He pensado un número entre el 1 y el 100, "
      f"\ny sólo tienes 8 intentos para intentar adivinar cuál es ese número.")

aleatorio = randint(1, 100)
intentos = 8
confirmacion = True

while confirmacion:

    aux = int(input("\n¿Cuál crees que es el número? "))
    intentos -= 1

    if intentos >= 1 and 0 <= aux > 100:
        print("El número que has elegido no está permitido, inténtalo de nuevo.")

    elif intentos >= 1 and aux < aleatorio:
        print("El número que has elegido es menor. Inténtalo de nuevo.")

    elif intentos >= 1 and aux > aleatorio:
        print("El número que has elegido es mayor. Inténtalo de nuevo.")

    elif intentos >= 1 and aux == aleatorio:
        print(f"¡Felicidades! has acertado, y te ha tomado {8 - intentos} intentos.")

    if intentos == 0:
        confirmacion = False

        if aux < aleatorio:
            print("\nEl número que has elegido es menor."
                  "\nHas agotado tus intentos.")

        else:
            print("\nEl número que has elegido es mayor."
                  "\nHas agotado tus intentos.")




