class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pío. Mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")

    #Método de clase
    @classmethod
    def poner_huevos(cls, cant):
        print(f"Puso {cant} huevos.")
        cls.alas = False
        print(Pajaro.alas)

    #Método estático
    @staticmethod
    def mirar():
        print("El pájaro mira.")



piolín = Pajaro('amarillo', 'canario')

piolín.volar(60)
piolín.pintar_negro()
piolín.alas = False
print(piolín.alas)


#Los métodos de clase no encesitan una instancia para ejecutarse
#Por lo tanto tampoco pueden a acceder a las instancias
Pajaro.poner_huevos(4)


#Los métodos estáticos no pueden acceder ni a los atributos
#de la clase ni a los de las instancias
Pajaro.mirar()
