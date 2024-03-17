class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Moo! Mi nombre es {self.nombre}.")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Beeh! Mi nombre es {self.nombre}.")


vaca_uno = Vaca("Lola")
oveja_uno = Oveja("Nube")

vaca_uno.hablar()
oveja_uno.hablar()

animales = [vaca_uno, oveja_uno]

for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca_uno)
animal_habla(oveja_uno)


































