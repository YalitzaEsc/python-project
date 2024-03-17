class Madre:
    def hablar(self):
        print("Hola.")


class Padre:
    def reir(self):
        print("Hahaha.")

    def hablar(self):
        print("Hey!")


class Hija(Padre, Madre):
    pass


class Nieta(Hija):
    pass


mi_nieta = Nieta()
mi_nieta.hablar()
mi_nieta.reir()













