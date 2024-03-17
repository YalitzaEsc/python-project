class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pío. Mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")


piolín = Pajaro('amarillo', 'canario')

piolín.piar()
piolín.volar(60)

















